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


def validate(line: str) -> str:
    """Return the line if it passes the gate, else raise ValueError."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")
    return line


def main() -> None:
    line = validate(ENTRY)
    assert line == ENTRY, "entry text changed unexpectedly"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line, "written entry does not match"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
