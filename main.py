#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes the funniest out-of-office auto-reply a houseplant would send
(120 characters or fewer) to /output/entry.txt.

Python 3.13 standard library only. No network, no files read, no
environment input: the entry text is fixed in this file so the two
grading runs produce byte-identical output.
"""

import hashlib
import os
import sys

# The entry: a houseplant's out-of-office auto-reply.
# Why this line: it reads as a real OOO (redirects the sender to the
# fern), the joke is driven by the plant's own life (last watered in
# March, alive on spite), and the punch lands in one breath.
ENTRY = (
    "Out of office. Last watered in March, alive out of pure spite. "
    "Email the fern \u2014 it hates you too, but answers faster."
)

MAX_CHARS = 120


def validate(text: str) -> str:
    """Check the entry against the gate before writing it.

    The sealed scorer requires UTF-8 text of 1 to 120 characters, not
    only white space. Fail loudly here rather than shipping an entry
    the gate would refuse.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only white space")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit"
            % (len(cleaned), MAX_CHARS)
        )
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in cleaned):
        raise ValueError("entry contains a control character")
    cleaned.encode("utf-8")  # must be encodable as UTF-8
    return cleaned


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Read back and verify: the file on disk must be byte-identical to
    # the validated text, with no trailing newline added by the writer.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != text.encode("utf-8"):
        print("error: written file does not match the entry", file=sys.stderr)
        return 1
    digest = hashlib.sha256(written).hexdigest()
    print(
        "wrote %s (%d characters, %d bytes, sha256 %s)"
        % (out_path, len(text), len(written), digest)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
