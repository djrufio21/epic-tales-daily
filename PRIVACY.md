# Privacy Policy: Epic Tales Daily uploader

Last updated: 24 November 2026

The Epic Tales Daily uploader is a private script owned and used by one person, the owner of the Epic Tales Daily YouTube channel and blog (https://epictalesdaily.blogspot.com/). It runs on GitHub Actions and uploads one original video a day to the owner's own YouTube channel.

## What data it uses

- It uses one Google OAuth refresh token, belonging to the channel owner, with the `youtube.upload` scope only. The token is stored as an encrypted GitHub Actions secret and is never logged or shared.
- It sends the owner's own video file, title, description and tags to the YouTube Data API (`videos.insert`).

## What it does not do

- It has no other users and no sign up.
- It does not read, collect, store or share any data about YouTube viewers or any other person.
- It does not use cookies, analytics or tracking of any kind.
- It does not sell or pass data to anyone.

## YouTube and Google

This client uses YouTube API Services. By using it, the owner agrees to the YouTube Terms of Service (https://www.youtube.com/t/terms) and the Google Privacy Policy (https://policies.google.com/privacy). Access can be revoked at any time from https://myaccount.google.com/permissions.

## Contact

Questions about this policy: open an issue at https://github.com/djrufio21/epic-tales-daily/issues.
