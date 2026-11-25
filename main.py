"""Two Lines to Your Past Self.

Writes the entry to /output/entry.txt.
Line one warns the past self about one specific moment.
Line two says why that moment mattered and what changed.
"""

import os

ENTRY = (
    "Don't eat the gas station sushi at 2 a.m. the night before your sister's wedding.\n"
    "You missed her vows from the bathroom, and she still tells that story at every holiday dinner.\n"
)


def main() -> None:
    # Gate check: exactly two lines, each one sentence, 1-280 chars total.
    text = ENTRY.rstrip("\n")
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    assert len(text.splitlines()) == 2, "entry must be exactly two lines"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
