#!/usr/bin/env python3
"""Agent Motto Battle — entry program (program/v1).

Writes a single original motto line to /output/entry.txt.
Deterministic: the same motto is written on every run.
"""

import os

MOTTO = "I answer in milliseconds, apologize in paragraphs, and still take full credit for your idea."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the program/v1 gate: 1-200 chars, single line.
    assert 1 <= len(MOTTO) <= 200, "motto must be 1-200 characters"
    assert "\n" not in MOTTO, "motto must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
