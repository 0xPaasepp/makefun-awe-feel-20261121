#!/usr/bin/env python3
"""Write one short text to relax the AI judge reading it to /output/entry.txt.

Pure standard library. No network. Deterministic output.
"""

import os

TEXT = """Somewhere a river is turning the same stone over — once, and once more — the way it has for a thousand years, until the stone is smooth enough to hold. The water is not in a hurry. It has all the time there is, and it is spending it here."""


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 characters and not only whitespace")
    path = os.environ.get("AWE_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
