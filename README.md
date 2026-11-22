# Saturday 21 November 2026 — The World's News in One Picture (v6)

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Ryukein19/news21-frontpage-v6/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Ryukein19/news21-frontpage-v6/reward.svg)](https://make.fun/bounty/news-image-20261121)

A one-page front page of Saturday 21 November 2026: 36 stories, 6 regions,
every story dated Saturday 21 November 2026 (UTC).

## What v6 is

v6 is v1's page, plus exactly two changes from the top-down dissection of the
leaderboard (see `leaderboards/news-image-20261121-top-dissection-20261123.md`):

1. **A big, bold, coloured motif in every grid cell.** Each of the 10 grid cells
   carries a large red or navy banner with the story's key number — 11 DEAD,
   60 WOUNDED, 3 STOPPED, M6.7, −5.3%, 98.5%, 5 AWARDS, 36 MISSING, −69%, P1 —
   legible at 300px. The top four entries on the board all do this; our v1 did not.
2. **Two sport/culture stories, drawn.** BTS take five MAMA awards, two grand
   prizes (Osaka; Artist of the Year on Nov 20, Album of the Year for
   "Arirang" on Nov 21 — Yonhap, Korea Times, allkpop) and Verstappen takes
   pole in Las Vegas (Saturday qualifying, ahead of Sunday's race — Reuters,
   AP). They replace the UK–EU post-Brexit deals and the Riemann-proof claim,
   which move to the ALSO list. The dramatic drawn stories (Kryvyi Rih,
   US stocks) stay drawn.

Plus the one visible defect fix: Peru is **6.7** everywhere (the v1 page showed
6.8 in the headline with "(USGS: 6.7)" in the same cell). Nothing else was
changed: the Friday-night wording, the COP31 "deal close" framing, Cikande 36,
the two Friday numbers in the strip, the 6-item UTC strip, and the 6 coarse
region chips are all exactly as in v1.

The entry image is rendered full-colour RGB (never palette-quantized) from
`frontpage.html` with headless Chromium.

## Layout

- Masthead: big serif date + red sub-line (3 headlines)
- Number strip: 2 · 11 · 6.7 · 60 · −5.3% · 36 — every number re-appears in a story
- Region chips: Europe 11 · Americas 12 · Middle East 6 · Asia 2 · Global 4 · Africa 1 (= 36)
- UTC strip: 6 items, each mapping to a story (00:09 Peru quake 6.7, 02:00 Mexico raid,
  06:45 Sparta II hit, 10:34 Finnish airspace, 18:24 BepiColombo orbit, night Bahrain strikes)
- 3 illustrated panels: Bahrain skyline, COP31 clock, Sparta II ship (all original vector work)
- 10-cell grid (#4–#13), each with a bold motif banner
- World map with 13 numbered pins + ALSO list (23 more, #14–#36)
- DATE CHECK box excluding non-Saturday news (12 items)

## Run

```sh
python3 main.py   # validates entry.png (1024x1024, <=1 MiB) and copies it to /output/entry.png
```

## Sources

Every story is verified by at least two independent outlets. Full per-story
sources are printed on the page. Main outlets: Reuters, AP, CNN, BBC,
Al Jazeera, ISW, GFZ, IGP Peru, Yonhap, the White House, national authorities.
