# Epic Tales Daily

Illustrated retellings of the Ramayana and Mahabharata for all ages, published three times a week.

- `episodes/NNN/` holds each episode: numbered card images and `episode.json` (title, captions, takeaway).
- `tools/publish.py` posts the next unpublished episode to Blogger and records it in `published.json`.
- `.github/workflows/publish.yml` runs the publisher every Monday, Wednesday and Friday at about 8am Malaysia time. It skips quietly until the Blogger secrets are set.
- `tools/draw_ep001.py` is the script that drew Episode 1.

All artwork and text are original.
