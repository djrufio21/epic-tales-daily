"""Upload a built Short to YouTube. Usage: python tools/youtube_upload.py 001 shorts

Runs only once YOUTUBE_REFRESH_TOKEN is saved as a repo secret. It reuses the
GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET from the Blogger setup, but needs its
own refresh token with the youtube.upload scope.

Note: YouTube keeps every upload private until the Google Cloud project passes
YouTube's API audit. Until then, upload by hand from the GitHub release.
"""
import json, os, pathlib, sys, urllib.parse, urllib.request

num, folder = sys.argv[1], pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "shorts")
meta = json.loads((folder / f"{num}.json").read_text())
video = (folder / f"{num}.mp4").read_bytes()

tok = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", urllib.parse.urlencode({
    "client_id": os.environ["GOOGLE_CLIENT_ID"], "client_secret": os.environ["GOOGLE_CLIENT_SECRET"],
    "refresh_token": os.environ["YOUTUBE_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()))["access_token"]

body = json.dumps({
    "snippet": {"title": meta["title"], "description": meta["description"], "tags": meta["tags"],
                "categoryId": meta["categoryId"], "defaultLanguage": "en"},
    "status": {"privacyStatus": os.environ.get("YOUTUBE_PRIVACY", "public"),
               "selfDeclaredMadeForKids": meta["madeForKids"], "containsSyntheticMedia": True},
}).encode()
start = urllib.request.Request(
    "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
    data=body, method="POST", headers={
        "Authorization": f"Bearer {tok}", "Content-Type": "application/json; charset=UTF-8",
        "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(len(video))})
upload_url = urllib.request.urlopen(start).headers["Location"]
put = urllib.request.Request(upload_url, data=video, method="PUT",
                             headers={"Authorization": f"Bearer {tok}", "Content-Type": "video/mp4"})
res = json.load(urllib.request.urlopen(put, timeout=600))
print("Uploaded: https://youtube.com/shorts/" + res["id"])
