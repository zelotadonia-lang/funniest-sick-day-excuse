#!/usr/bin/env python3
"""Write one original sick-day excuse line to /output/entry.txt."""

import os

ENTRY = "HR lost my leave form and approved 3 days off for last Tuesday."
# One line, 63 characters: inside the gate of 1 to 200 UTF-8 characters.


def validate(text):
    # Gate (RULES.txt): "/output/entry.txt is UTF-8 text of 1 to 200
    # characters, not only white space". Only a valid entry goes to the judge.
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")
    return text


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(text, out_dir)


if __name__ == "__main__":
    main()
