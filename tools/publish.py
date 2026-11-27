"""Publish the next unpublished episode to Blogger.

Reads episodes/NNN/episode.json and the picture-only images beside it
(captioned copies for social media live in episodes/NNN/social), posts them through
the Blogger API v3, then records the episode in published.json.
Needs these environment variables (GitHub secrets):
  GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN
The blog is found from BLOG_URL below, so no blog ID is needed.
"""
import datetime, html, json, os, pathlib, sys, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = ROOT / "published.json"
LAST = ROOT / "last_published.txt"  # Malaysia date of the last scheduled post
REPO = os.environ.get("GITHUB_REPOSITORY", "djrufio21/epic-tales-daily")
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
BLOG_URL = "https://epictalesdaily.blogspot.com/"
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"


def call(url, data=None, headers=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
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
        cap = ep["captions"][i] if i < len(ep["captions"]) else ep["title"]
        src = f"{RAW}/episodes/{d.name}/{name}"
        parts.append(
            f'<p style="text-align:center"><img src="{src}" alt="{html.escape(cap)}" '
            f'style="max-width:100%;height:auto" /></p>'
        )
        if i < len(ep["captions"]):
            parts.append(f"<p>{html.escape(cap)}</p>")
    if ep.get("story"):
        parts.append("<h3>The story in full</h3>")
        parts += [f"<p>{html.escape(t)}</p>" for t in ep["story"]]
    if ep.get("value_name"):
        parts.append(f"<h3>Today's value: {html.escape(ep['value_name'])} ({html.escape(ep['value_meaning'])})</h3>")
        parts += [f"<p>{html.escape(t)}</p>" for t in (ep.get("lesson_long") or [ep["lesson"]])]
    else:
        parts.append(f"<h3>Today's takeaway</h3><p>{html.escape(ep['takeaway'])}</p>")
    if ep.get("tradition"):
        parts.append("<h3>In our tradition</h3>")
        parts += [f"<p>{html.escape(t)}</p>" for t in ep["tradition"]]
    if ep.get("words"):
        parts.append("<h3>Words to know</h3><ul>" + "".join(
            f"<li><strong>{html.escape(w)}</strong>: {html.escape(m)}</li>" for w, m in ep["words"]) + "</ul>")
    if ep.get("questions"):
        parts.append("<h3>Talk about it</h3><ol>" + "".join(f"<li>{html.escape(q)}</li>" for q in ep["questions"]) + "</ol>")
    elif ep.get("question"):
        parts.append(f"<p><strong>Talk about it:</strong> {html.escape(ep['question'])}</p>")
    if ep.get("next"):
        parts.append(f"<p><em>Next episode: {html.escape(ep['next'])}</em></p>")
    return "\n".join(parts)


def expand(spec, done):
    """Turn "002", "001,003", "001-012" or "all" into a list of episode folders."""
    if spec.strip().lower() == "all":
        return list(done)
    out = []
    for part in spec.replace(" ", ",").split(","):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            out += [f"{n:03d}" for n in range(int(a), int(b) + 1)]
        else:
            out.append(f"{int(part):03d}")
    return out


def refresh(names):
    """Refresh the content of episodes that are already live."""
    if os.environ.get("DRY_RUN"):
        for name in names:
            d = ROOT / "episodes" / name
            ep = json.loads((d / "episode.json").read_text())
            print(title_of(ep)); print(build_html(d, ep))
        return 0
    auth = {"Authorization": f"Bearer {access_token()}"}
    api = "https://www.googleapis.com/blogger/v3/blogs"
    blog = call(f"{api}/byurl?url=" + urllib.parse.quote(BLOG_URL, safe=""), headers=auth)["id"]
    jhead = {**auth, "Content-Type": "application/json"}
    items, page = [], ""
    while True:
        res = call(f"{api}/{blog}/posts?maxResults=50&fetchBodies=false" + (f"&pageToken={page}" if page else ""), headers=auth)
        items += res.get("items", [])
        page = res.get("nextPageToken")
        if not page:
            break
    failed = 0
    for name in names:
        d = ROOT / "episodes" / name
        ep = json.loads((d / "episode.json").read_text())
        title = title_of(ep)
        match = [it for it in items if it["title"] == title]
        if not match:
            print("No live post found with title:", title); failed += 1; continue
        out = call(f"{api}/{blog}/posts/{match[0]['id']}", json.dumps({"content": build_html(d, ep)}).encode(), jhead, "PATCH")
        print("Updated:", out.get("url"))
    return 1 if failed else 0


def title_of(ep):
    return f"{ep['book']} Episode {ep['number']}: {ep['title']}"


def main():
    done = json.loads(STATE.read_text()) if STATE.exists() else []
    update = os.environ.get("UPDATE_EPISODE", "").strip()
    today = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).date().isoformat()
    if not update and os.environ.get("EVENT_NAME") == "schedule" and LAST.exists() and LAST.read_text().strip() == today:
        print("An episode was already published today (Malaysia time). Nothing to do.")
        return 0
    if update:
        return refresh(expand(update, done))
    d = next_episode(done)
    if d is None:
        print("No unpublished episodes left. Nothing to do.")
        return 0
    ep = json.loads((d / "episode.json").read_text())
    post = {"kind": "blogger#post", "title": title_of(ep), "content": build_html(d, ep), "labels": [ep["book"]]}
    if os.environ.get("DRY_RUN"):
        print(post["title"]); print(post["content"]); return 0
    auth = {"Authorization": f"Bearer {access_token()}"}
    api = "https://www.googleapis.com/blogger/v3/blogs"
    blog = call(f"{api}/byurl?url=" + urllib.parse.quote(BLOG_URL, safe=""), headers=auth)["id"]
    jhead = {**auth, "Content-Type": "application/json"}
    out = call(f"{api}/{blog}/posts/", json.dumps(post).encode(), jhead)
    print("Published:", out.get("url"))
    done.append(d.name)
    STATE.write_text(json.dumps(done, indent=2) + "\n")
    LAST.write_text(today + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
