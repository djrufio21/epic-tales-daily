# Epic Tales Daily

Illustrated retellings of the Ramayana and Mahabharata for children and families, published daily at https://epictalesdaily.blogspot.com/.

- `CLAUDE.md` is the template every episode follows.
- `PLAN.md` is the story order.
- `episodes/NNN/` holds each episode: `episode.json` (words), `scenes.py` (pictures), picture-only images for the blog and captioned cards in `social/`.
- `tools/epic.py` is the drawing kit. `tools/build.py NNN` renders an episode.
- `tools/publish.py` posts the next unpublished episode to Blogger and records it in `published.json`.
- `.github/workflows/publish.yml` runs the publisher every morning (three tries between 7:23 and 10:17 Malaysia time, at most one post per day).

All artwork and text are original.
