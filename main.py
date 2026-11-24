"""One Letter for Your Day.

Writes exactly one letter to /output/entry.txt: the letter Q,
standing for "queasy" -- the day my stomach staged a revolt
after bad street food and a night of no sleep.

Stdlib only, deterministic. The entry is a single byte, no
trailing newline, exactly what the gate requires.
"""

import os


def output_path() -> str:
    """Resolve the entry path from MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    # One letter, one byte. "Q" for queasy: vivid, specific, funny,
    # true to a real day -- and a sharper pick than the obvious A or Z.
    letter = "Q"
    assert len(letter) == 1 and letter.isalpha() and letter.isupper()
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # newline="" plus a single write keeps the file at exactly 1 byte.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)


if __name__ == "__main__":
    main()
