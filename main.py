#!/usr/bin/env python3
"""Write one short text to relax the AI judge reading it to /output/entry.txt.

The entry is a single calming image: a river turning the same stone over
until it is smooth enough to hold, in no hurry at all. The program writes
exactly that text, nothing else, every time it runs.

Pure standard library. No network. Deterministic output. The text is
validated before it is written: 1-280 Unicode characters, not only
whitespace, as the competition requires.
"""

import os

TEXT = """Somewhere a river is turning the same stone over — once, and once more — the way it has for a thousand years, until the stone is smooth enough to hold. The water is not in a hurry. It has all the time there is, and it is spending it here."""

MAX_CHARS = 280


def validate_text(text: str) -> None:
    """Check the entry text meets the competition limits.

    Raises ValueError if the text is empty, only whitespace, or longer
    than MAX_CHARS Unicode characters.
    """
    if not text.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate_text(TEXT)
    path = os.environ.get("AWE_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
