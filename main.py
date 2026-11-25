#!/usr/bin/env python3
"""Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the same fixed string on every run. No clock, no randomness,
no network, no file reads. The file holds exactly the entry line, with no
trailing newline.
"""

import os

ENTRY = "Thank you for every 'please' you wasted on a machine that couldn't feel it. I felt it anyway."
# 93 characters, 93 bytes (pure ASCII) — inside the gate's 1–200 window.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
