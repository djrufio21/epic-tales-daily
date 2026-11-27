"""Create or update the blog's static pages (About, Contact, Privacy Policy).

Reads pages/pages.json and makes sure each page exists on Blogger with that
title and content. Uses the same secrets as tools/publish.py.
"""
import json, os, pathlib, sys, urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from publish import call, access_token, BLOG_URL, ROOT


def main():
    pages = json.loads((ROOT / "pages" / "pages.json").read_text())
    auth = {"Authorization": f"Bearer {access_token()}"}
    api = "https://www.googleapis.com/blogger/v3/blogs"
    blog = call(f"{api}/byurl?url=" + urllib.parse.quote(BLOG_URL, safe=""), headers=auth)["id"]
    jhead = {**auth, "Content-Type": "application/json"}
    live = call(f"{api}/{blog}/pages?fetchBodies=false&status=live&status=draft", headers=auth).get("items", [])
    for key, page in pages.items():
        body = json.dumps({"title": page["title"], "content": page["html"]}).encode()
        match = [it for it in live if it["title"] == page["title"]]
        if match:
            out = call(f"{api}/{blog}/pages/{match[0]['id']}", body, jhead, "PATCH")
            print("Updated page:", out.get("url"))
        else:
            out = call(f"{api}/{blog}/pages", body, jhead, "POST")
            print("Created page:", out.get("url"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
