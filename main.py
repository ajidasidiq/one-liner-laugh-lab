#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

The prompt: the excuse a robot vacuum gives after eating a sock.
The line is written deterministically to /output/entry.txt, no network,
no input, runs in well under a second.
"""

import os

ENTRY = (
    "I didn't eat your sock. It applied for asylum in my dustbin, "
    "and legally I'm a humanitarian appliance."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert line == ENTRY, "entry text changed unexpectedly"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line, "written entry does not match"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
