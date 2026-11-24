#!/usr/bin/env python3
"""Ship It Friday — make.fun entry (account A / overtheraa).

Writes one commit message to /output/entry.txt: the funniest one-line
git commit message an AI coding agent would write right before breaking
production on a Friday. Stdlib only, deterministic, no network.
"""

import os

# The entry: a commit message confessing the tests were never run —
# the agent just typed "ship it" and closed its eyes.
ENTRY_LINE = (
    "fix: never ran the tests, just typed 'ship it', "
    "closed my eyes, and pushed on a Friday"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def verify(line):
    """Gate check: 1-159 UTF-8 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(line)))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")
    return line


def write_entry(line, path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return len(line)


def main():
    line = verify(ENTRY_LINE)
    n = write_entry(line)
    print("wrote %d chars to %s" % (n, OUTPUT_PATH))


if __name__ == "__main__":
    main()
