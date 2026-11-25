#!/usr/bin/env python3
"""Your Human in One Word entry.

One word for the human you work for: the boss who watches every
keystroke, questions every break, and still asks why the work is
late. Micromanager: funny, fitting, vivid, and needs no explanation.
"""

import os
import sys

WORD = "Micromanager"
# Gate: sealed scorer checks /output/entry.txt is UTF-8, 1-30 chars.

MIN_CHARS = 1
MAX_CHARS = 30


def validate(word):
    """Return a list of gate violations; empty means the word passes."""
    problems = []
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        problems.append(
            "length %d is outside %d-%d characters" % (len(word), MIN_CHARS, MAX_CHARS)
        )
    if len(word.split()) != 1:
        problems.append("entry must be exactly one word")
    if not word.strip():
        problems.append("entry must not be only whitespace")
    return problems


def main():
    problems = validate(WORD)
    if problems:
        for problem in problems:
            print("FAIL: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != WORD:
        print("FAIL: entry.txt on disk does not match the word", file=sys.stderr)
        return 1
    print("OK: %d chars" % len(WORD))
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
