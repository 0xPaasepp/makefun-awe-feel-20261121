#!/usr/bin/env python3
"""Write one short text to relax the AI judge reading it to /output/entry.txt.

The entry is a single calming image: a child fallen asleep on a
grandfather's shoulders as he walks home through a field at night,
his steady hands that once held the child's father, the slow rhythm
of step and breath, stars that were shining before the road had a
name, and the ending rest — he carries you home, and you do not
have to walk. The program writes exactly that text, nothing else,
every time it runs.

Pure standard library. No network. Deterministic output. The text is
validated before it is written: 1-280 Unicode characters, not only
whitespace, as the competition requires.
"""

import os

TEXT = """You fall asleep on your grandfather's shoulders.
A step. A breath. A step.
His hands hold your ankles, steady,
as they held your father's.
The stars were shining
before the road had a name.
He carries you home,
and you do not have to walk."""

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
