# Epic Tales Daily

Illustrated retellings of the Ramayana and Mahabharata for all ages, published daily.

- `episodes/NNN/` holds each episode: picture-only images for the blog, captioned copies for social media in `social/`, and `episode.json` (title, captions, takeaway).
- `tools/publish.py` posts the next unpublished episode to Blogger and records it in `published.json`.
- `.github/workflows/publish.yml` runs the publisher every day at about 8am Malaysia time. It skips quietly until the three Google secrets are set. Blog: https://epictalesdaily.blogspot.com/
- `tools/draw_ep001.py` is the script that drew Episode 1.

All artwork and text are original.
