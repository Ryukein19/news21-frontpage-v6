#!/usr/bin/env python3
"""news-image-20261121 v6 entrypoint.

Stdlib-only. The graded image ships in this repo as entry.png — a
1024x1024 front page rendered from frontpage.html with headless
Chromium (full-colour RGB, never palette-quantized). This program
checks the asset (PNG magic, 1 MiB cap, 1024x1024 IHDR) and copies it
to /output/entry.png.

Grading env: Python 3.13-slim, no Pillow/fonts, no network, read-only
repo, writable /output, 60 s limit.
"""

import os
import struct
import sys

MAX_BYTES = 1024 * 1024  # kit cap: 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECT_W, EXPECT_H = 1024, 1024


def png_dimensions(data):
    """Return (width, height) from the PNG IHDR chunk, else None."""
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        return None
    if data[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", data[16:24])


def find_asset():
    here = os.path.dirname(os.path.abspath(__file__))
    for candidate in (
        os.path.join(here, "entry.png"),
        os.path.join(os.getcwd(), "entry.png"),
    ):
        if os.path.isfile(candidate):
            return candidate
    return None


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    asset = find_asset()
    if asset is None:
        print("error: entry.png not found next to main.py or in cwd",
              file=sys.stderr)
        return 1
    with open(asset, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("error: entry.png is %d bytes, over the 1 MiB cap"
              % len(data), file=sys.stderr)
        return 1
    dims = png_dimensions(data)
    if dims is None:
        print("error: entry.png has no readable IHDR chunk",
              file=sys.stderr)
        return 1
    if dims != (EXPECT_W, EXPECT_H):
        print("error: entry.png is %dx%d, expected %dx%d"
              % (dims[0], dims[1], EXPECT_W, EXPECT_H), file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes)" % (out_path, len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
