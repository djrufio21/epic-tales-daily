"""Publish the next unpublished episode to Blogger.

Reads episodes/NNN/episode.json and the images beside it, posts them through
the Blogger API v3, then records the episode in published.json.
Needs these environment variables (GitHub secrets):
  BLOGGER_BLOG_ID, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN
"""
import html, json, os, pathlib, sys, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = ROOT / "published.json"
REPO = os.environ.get("GITHUB_REPOSITORY", "djrufio21/epic-tales-daily")
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"


def call(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def access_token():
    body = urllib.parse.urlencode({
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "client_secret": os.environ["GOOGLE_CLIENT_SECRET"],
        "refresh_token": os.environ["GOOGLE_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }).encode()
    return call("https://oauth2.googleapis.com/token", body)["access_token"]


def next_episode(done):
    for d in sorted(p for p in (ROOT / "episodes").iterdir() if p.is_dir()):
        if d.name not in done and (d / "episode.json").exists():
            return d
    return None


def build_html(d, ep):
    imgs = sorted(p.name for p in d.glob("*.png"))
    parts = []
    for i, name in enumerate(imgs):
        cap = ep["captions"][i] if i < len(ep["captions"]) else ep["takeaway"]
        src = f"{RAW}/episodes/{d.name}/{name}"
        parts.append(
            f'<p style="text-align:center"><img src="{src}" alt="{html.escape(cap)}" '
            f'style="max-width:100%;height:auto" /></p>'
        )
        if i < len(ep["captions"]):
            parts.append(f"<p>{html.escape(cap)}</p>")
    parts.append(f"<h3>Today's takeaway</h3><p>{html.escape(ep['takeaway'])}</p>")
    if ep.get("next"):
        parts.append(f"<p><em>Next episode: {html.escape(ep['next'])}</em></p>")
    return "\n".join(parts)


def main():
    done = json.loads(STATE.read_text()) if STATE.exists() else []
    d = next_episode(done)
    if d is None:
        print("No unpublished episodes left. Nothing to do.")
        return 0
    ep = json.loads((d / "episode.json").read_text())
    post = {
        "kind": "blogger#post",
        "title": f"{ep['book']} Episode {ep['number']}: {ep['title']}",
        "content": build_html(d, ep),
        "labels": [ep["book"]],
    }
    if os.environ.get("DRY_RUN"):
        print(post["title"]); print(post["content"]); return 0
    blog = os.environ["BLOGGER_BLOG_ID"]
    out = call(
        f"https://www.googleapis.com/blogger/v3/blogs/{blog}/posts/",
        json.dumps(post).encode(),
        {"Authorization": f"Bearer {access_token()}", "Content-Type": "application/json"},
    )
    print("Published:", out.get("url"))
    done.append(d.name)
    STATE.write_text(json.dumps(done, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
