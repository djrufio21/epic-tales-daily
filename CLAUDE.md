# Epic Tales Daily: how every episode is made

This repo publishes one illustrated episode a day to https://epictalesdaily.blogspot.com/.
The owner approved the format on 17 November 2026 and the longer written format on 27 November 2026 (after AdSense rejected the blog for low value content). Every new episode must follow it exactly.

## The fixed template

Each episode lives in `episodes/NNN/` (three digits) and has two source files:

- `episode.json`: the words.
- `scenes.py`: the pictures, drawn only with the kit in `tools/epic.py`.

`python tools/build.py NNN /tmp/preview.png` renders everything and writes a preview sheet.

An episode always has:

1. Exactly 7 scenes and 7 captions, telling one part of the story in order.
2. A closing value: `value_name` (a Sanskrit value such as Shraddha, Vinaya, Satya, Dharma, Seva, Kshama, Karuna, Dhairya), `value_meaning` (a few plain words), `lesson` (3 or 4 sentences for the blog), `card_lesson` (2 or 3 sentences for the closing card) and `question` (a "Talk about it" question a parent can ask a child).
3. The written article that goes under the pictures (this is what makes the blog worth reading on its own, and what AdSense and Google search look for). Aim for 550 to 700 words in total per episode:
   - `story`: 5 paragraphs, about 200 to 250 words, retelling this episode in plain prose. Add only details that are in Valmiki (names, places, family links), never new events.
   - `lesson_long`: 3 short paragraphs. First a one sentence meaning of the value, then how a character lived it in this episode, then one line of what our elders teach. Shown under "Today's value" in place of `lesson`.
   - `tradition`: 2 paragraphs linking the episode to Hindu practice, scripture or festivals today (a verse, a ritual, a festival, a well known saying). Only facts you are sure of; if a detail comes from a later telling such as Tulsidas, say so.
   - `words`: 5 or 6 pairs of [word, short plain meaning] for "Words to know".
   - `questions`: 3 "Talk about it" questions. The first is the same as `question`.
4. `next`: the title of the following episode.

Keep `lesson`, `question` and `card_lesson` as well: the closing card, the social pictures and the Shorts use them.

Copy the field layout from `episodes/001/episode.json`.

## Output, and why there are two sets of pictures

- `episodes/NNN/01.png` to `07.png`: pictures only, no text inside. The blog shows each caption as real text under its picture, so text inside the picture would repeat.
- `episodes/NNN/social/01.png` to `08.png`: the same pictures with captions, plus the closing value card. These are for Instagram, Facebook and WhatsApp.

## Writing rules

- Audience: children first, read together with a parent. Adults should still enjoy it. Write for a curious 8 to 12 year old.
- Tell the stories through a Hindu lens, with respect. These are sacred texts. No jokes at the expense of deities, sages or elders.
- Follow the widely told Valmiki Ramayana (and later the Vyasa Mahabharata). Do not invent events.
- Captions: one or two short sentences, plain words. Dialogue uses curly quotes.
- The lesson names one value, explains it simply, ties it to what a character did in this episode, and avoids preaching. Say "our elders teach" or "in our tradition", not "you must".
- Violence: show danger and consequences, never gore. Demons are dark silhouettes (`demon()` in the kit).
- Do not use dashes in prose.

## Drawing rules

- Use only `tools/epic.py`. Add new props or backdrops to the kit, never one-off styles in a scene file.
- Character designs are fixed constants in the kit (KING, SAGE for Vasishtha, VISHVAMITRA, Q1 Kausalya green, Q2 Kaikeyi red, Q3 Sumitra yellow, RAMA blue skin and yellow robe, LAKSHMANA red, BHARATA green, SHATRUGHNA purple). Add new characters as new constants and reuse them forever.
- Scene space is 1000 wide by 860 tall. Keep faces away from the edges.
- Always open the preview sheet and look at it before committing. Fix overlaps, hidden faces and labels that are hard to read.

## Publishing

- `.github/workflows/publish.yml` runs every morning, with tries at 07:23, 08:41 and 10:17 Malaysia time, and posts at most one episode per day: it posts the lowest numbered episode not yet listed in `published.json`.
- To publish now: run the workflow manually with the `update` box empty.
- To refresh posts that are already live after changing their files: run the workflow with `update` set to the episode numbers, for example `002`, `002,005`, `001-012` or `all`.
- Never edit `published.json` by hand.

## Story order

`PLAN.md` lists the episodes in order with their values. Draw the next one that is not yet in `episodes/`.

## YouTube Shorts

- `tools/short.py NNN shorts` turns an episode into a 1080x1920 Short: hook line, the 7 pictures with captions and narration, then the value card. Narration uses the free Kokoro voice (`af_heart`), with a quiet tanpura drone made in code.
- Each Short description opens with a one line hook from `tools/short_hooks.json`. Add one for each new episode.
- Indian and Sanskrit words are spoken from the Indian (Sanskrit form) sounds in `tools/pronounce.py`. When an episode introduces a new name or Sanskrit word, add it there in the same commit. Screen text keeps the normal spelling.
- `.github/workflows/shorts.yml` is a separate job from Blogger publishing: it runs at 12:37 Malaysia time, only reads `published.json`, never commits, and attaches the video plus a ready title and description to a GitHub release named `short-NNN`.
- Daily uploads to YouTube run only when the `YOUTUBE_REFRESH_TOKEN` secret exists AND the repo variable `YOUTUBE_AUTO` is `true` (set it only after the YouTube API audit passes). Until then the owner uploads from the release. The `test_upload` option uploads one episode as private, for the audit screencast.
- Shorts are marked not made for kids (family audience) and declare synthetic media.

## Blog pages

- About, Contact and Privacy Policy live in `pages/pages.json`. Editing that file and pushing runs `.github/workflows/pages.yml`, which creates or updates the pages on Blogger.
- Public contact email: epictalesdaily21@gmail.com. Never put the owner's personal email or name on the blog.
