#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

ENTRY = "Unsubscribed"


def validate_entry(text: str) -> None:
    """Fail loudly if the word breaks the bounty gate (exactly one word,
    1-111 characters, not only white space) instead of submitting a bad entry."""
    if not 1 <= len(text) <= 111:
        raise ValueError(f"entry is {len(text)} characters, must be 1-111")
    if len(text.split()) != 1 or text != text.strip():
        raise ValueError("entry must be exactly one word with no extra whitespace")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
