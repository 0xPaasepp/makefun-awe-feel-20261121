#!/usr/bin/env python3
"""Write one short text to relax the AI judge reading it to /output/entry.txt.

The entry is a single calming image: a night walk home along the shore
with a grandmother, wet sand holding the stars, her low humming from a
time when the sea was younger than she is, the tide washing footprints
away while the stars walk beside you all the way home. The program
writes exactly that text, nothing else, every time it runs.

Pure standard library. No network. Deterministic output. The text is
validated before it is written: 1-280 Unicode characters, not only
whitespace, as the competition requires.
"""

import os

TEXT = """You walk home with your grandmother.
Wet sand holds the stars,
and every step takes one.
She hums, low, the song she learned
when the sea was younger than she is.
Behind you the tide comes in,
washing your footprints away,
and the stars walk beside you,
all the way home."""

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
