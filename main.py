"""Make the Judge Smile, variant 5.

Writes one line, at most 200 characters, about a small good thing
that happened today, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line: a stranger at the photocopy shop pays for you with a
crumpled ten thousand and tells you to keep your coins for the bus
home. Second person, opened mid-moment, one concrete physical
detail, ending on a short warm landing.
"""

import os
from pathlib import Path

ENTRY = (
    "You are counting coins at the photocopy shop when the man behind "
    "you slides a crumpled ten thousand across the counter and says "
    "keep yours for the bus home."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"
    (output_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
