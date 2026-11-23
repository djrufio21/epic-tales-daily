"""Turn an episode into a vertical YouTube Short.

Usage: python tools/short.py 001 [out_dir]

Writes out_dir/NNN.mp4 (1080x1920, 30 fps) and out_dir/NNN.json (title,
description, tags) built from episodes/NNN. Narration is made on the machine
with the free Kokoro voice model (no paid service, no account). Indian and
Sanskrit words are spoken from the sound list in tools/pronounce.py. The soft
tanpura drone underneath is generated in code, so there is no music licence
to worry about.

Needs: pip install kokoro-onnx soundfile pillow numpy, plus ffmpeg, plus the
two model files (see MODEL_URLS) in the folder named by KOKORO_DIR
(default: ./.kokoro). The workflow downloads and caches them.
"""
import json, os, pathlib, re, subprocess, sys, urllib.request

import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pronounce import to_phonemes

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOG = "epictalesdaily.blogspot.com"
W, H, FPS, SR = 1080, 1920, 30, 24000
VOICE, SPEED = "af_heart", 0.92
MODEL_URLS = {
    "kokoro.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx",
    "voices.bin": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin",
}

BG = (28, 18, 40)          # deep plum, matches the warm palette of the drawings
GOLD = (246, 196, 83)
CREAM = (255, 246, 228)
PIC_BOX = (0, 360, W, 360 + 940)  # where the 1080x940 picture sits


def font(size, bold=True):
    names = (["Inter-Bold.otf", "Inter-SemiBold.otf", "DejaVuSans-Bold.ttf"] if bold
             else ["Inter-Medium.otf", "Inter-Regular.otf", "DejaVuSans.ttf"])
    for base in ["/usr/share/fonts/opentype/inter", "/usr/share/fonts/truetype/inter",
                 "/usr/share/fonts/truetype/dejavu"]:
        for n in names:
            p = pathlib.Path(base) / n
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default(size)


def wrap(draw, text, f, width):
    lines, line = [], ""
    for word in text.split():
        test = (line + " " + word).strip()
        if draw.textlength(test, font=f) <= width:
            line = test
        else:
            lines.append(line)
            line = word
    return lines + [line] if line else lines


def text_block(draw, text, f, top, width=960, fill=CREAM, gap=1.32):
    lh = int(f.size * gap)
    for i, ln in enumerate(wrap(draw, text, f, width)):
        draw.text((W // 2, top + i * lh), ln, font=f, fill=fill, anchor="ma")
    return top + len(wrap(draw, text, f, width)) * lh


def narrate(kokoro, text):
    """Indian and Sanskrit words use the sounds in pronounce.py, the rest is English."""
    text = re.sub("[“”\"]", "", text)
    english = lambda t: kokoro.tokenizer.phonemize(t, "en-us")
    samples, sr = kokoro.create(to_phonemes(text, english), voice=VOICE, speed=SPEED,
                                is_phonemes=True)
    assert sr == SR
    return samples.astype(np.float32)


def tanpura(seconds):
    """A quiet four string drone (Pa Sa Sa Sa), plucked every 2.4 seconds."""
    n = int(seconds * SR)
    out = np.zeros(n, np.float32)
    sa = 130.81  # C3
    strings = [sa * 1.5 / 2, sa, sa, sa / 2]
    t = np.arange(int(SR * 4.5)) / SR
    env = np.exp(-t / 1.6) * (1 - np.exp(-t / 0.02))
    for start in np.arange(0, seconds, 2.4):
        for j, f0 in enumerate(strings):
            tone = sum(np.sin(2 * np.pi * f0 * h * t) / h ** 1.3 for h in range(1, 9))
            s = int((start + j * 0.6) * SR)
            seg = (tone * env).astype(np.float32)[: max(0, n - s)]
            out[s:s + len(seg)] += seg
    out /= max(1e-6, np.abs(out).max())
    return out * 0.07


def frame_base(ep):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((W // 2, 92), "EPIC TALES DAILY", font=font(40), fill=GOLD, anchor="ma")
    d.text((W // 2, 150), f"{ep['book']}  •  Episode {ep['number']}", font=font(34, False),
           fill=(214, 196, 230), anchor="ma")
    text_block(d, ep["title"], font(56), 214, width=980, fill=CREAM, gap=1.18)
    d.text((W // 2, H - 110), f"Full story with pictures: {BLOG}", font=font(30, False),
           fill=(214, 196, 230), anchor="ma")
    return img


def scene_frames(ep, pic, caption, n):
    """Yield n frames: the picture slowly zooms while the caption sits below."""
    base = frame_base(ep)
    d = ImageDraw.Draw(base)
    text_block(d, caption, font(54), 1345, width=950)
    pw, ph = pic.size  # 1080 x 940
    top = PIC_BOX[1]
    for i in range(n):
        z = 1.0 + 0.07 * i / max(1, n - 1)
        cw, ch = pw / z, ph / z
        x0, y0 = (pw - cw) / 2, (ph - ch) * 0.45
        crop = pic.resize((pw, ph), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))
        f = base.copy()
        f.paste(crop, (0, top))
        yield f


def card_frames(ep, card, nxt, n):
    """The closing value card, then a follow prompt for the next episode."""
    base = Image.new("RGB", (W, H), BG)
    c = card.resize((1080, 1350), Image.LANCZOS)
    base.paste(c, (0, 170))
    d = ImageDraw.Draw(base)
    d.text((W // 2, 80), "EPIC TALES DAILY", font=font(40), fill=GOLD, anchor="ma")
    text_block(d, f"Next: {nxt}", font(46), 1580, width=960, fill=GOLD)
    d.text((W // 2, 1720), "Follow for a new episode every day", font=font(36, False),
           fill=CREAM, anchor="ma")
    for _ in range(n):
        yield base


def fade(a, b, k, total, picture_only):
    """Crossfade. Between scenes only the picture fades, so captions never overlap."""
    if not picture_only:
        return Image.blend(a, b, k / total)
    out = b.copy()
    out.paste(Image.blend(a.crop(PIC_BOX), b.crop(PIC_BOX), k / total), PIC_BOX[:2])
    return out


def models():
    d = pathlib.Path(os.environ.get("KOKORO_DIR", ROOT / ".kokoro"))
    d.mkdir(parents=True, exist_ok=True)
    for name, url in MODEL_URLS.items():
        if not (d / name).exists():
            print("Downloading", name)
            urllib.request.urlretrieve(url, d / name)
    from kokoro_onnx import Kokoro
    return Kokoro(str(d / "kokoro.onnx"), str(d / "voices.bin"))


def metadata(ep, seconds):
    book = ep["book"]
    title = f"{ep['title']} | {book} for Kids, Episode {ep['number']}"
    if len(title) > 90:
        title = f"{ep['title']} | {book} Ep {ep['number']}"
    title += " #shorts"
    hooks = json.loads((ROOT / "tools" / "short_hooks.json").read_text())
    hook = hooks.get(f"{ep['number']:03d}", f"Episode {ep['number']} of the {book} for kids: {ep['title']}.")
    desc = "\n\n".join([
        hook,
        f"{book}, Episode {ep['number']}: {ep['title']}",
        f"Value of the day: {ep['value_name']} ({ep['value_meaning']})",
        ep["lesson"],
        f"Talk about it: {ep['question']}",
        f"Read the full illustrated episode: https://{BLOG}/",
        f"Next episode: {ep['next']}\nSubscribe for a new episode every day.",
        f"#{book} #KidsStories #HinduStories #MoralStories #BedtimeStories #IndianMythology #shorts",
    ])
    tags = [book, f"{book} for kids", "Hindu stories for kids", "moral stories", "kids stories",
            "Indian mythology", "bedtime stories", ep["value_name"], "Rama", "Epic Tales Daily"]
    return {"title": title, "description": desc, "tags": tags, "seconds": round(seconds, 1),
            "categoryId": "27", "madeForKids": False}


def build(num, out_dir):
    ep_dir = ROOT / "episodes" / num
    ep = json.loads((ep_dir / "episode.json").read_text())
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    k = models()

    # Narration: a one line hook, the seven captions, then the value and question.
    parts = [f"Episode {ep['number']}. {ep['title']}."] + ep["captions"]
    closing = (f"Today's value is {ep['value_name']}, {ep['value_meaning']}. "
               f"{ep['card_lesson']} Talk about it: {ep['question']}")
    pause = np.zeros(int(SR * 0.45), np.float32)
    clips = [narrate(k, t) for t in parts] + [narrate(k, closing)]
    # The hook plays over the first picture, so join it to caption one.
    clips = [np.concatenate([clips[0], pause, clips[1]])] + clips[2:]
    clips = [np.concatenate([c, pause]) for c in clips]
    clips[-1] = np.concatenate([clips[-1], np.zeros(int(SR * 1.2), np.float32)])

    voice = np.concatenate(clips)
    seconds = len(voice) / SR
    mix = voice + tanpura(seconds)
    mix = mix / max(1.0, np.abs(mix).max() / 0.95)
    wav = out_dir / f"{num}.wav"
    sf.write(wav, mix, SR)

    pics = [Image.open(ep_dir / f"{i:02d}.png").convert("RGB") for i in range(1, 8)]
    card = Image.open(ep_dir / "social" / "08.png").convert("RGB")
    mp4 = out_dir / f"{num}.mp4"
    ff = subprocess.Popen([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", str(wav),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(mp4),
    ], stdin=subprocess.PIPE)

    XF = 8  # crossfade frames
    prev = None
    for idx, clip in enumerate(clips):
        n = max(XF + 1, round(len(clip) / SR * FPS))
        gen = (scene_frames(ep, pics[idx], ep["captions"][idx], n) if idx < 7
               else card_frames(ep, card, ep["next"], n))
        for j, f in enumerate(gen):
            if prev is not None and j < XF:
                f = fade(prev, f, j + 1, XF + 1, idx < 7)
            ff.stdin.write(f.tobytes())
            last = f
        prev = last
    ff.stdin.close()
    if ff.wait():
        sys.exit("ffmpeg failed")
    wav.unlink()
    (out_dir / f"{num}.json").write_text(json.dumps(metadata(ep, seconds), indent=2, ensure_ascii=False))
    print(f"Built {mp4} ({seconds:.0f}s)")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ROOT / "shorts")
