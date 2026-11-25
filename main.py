"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output):
the GPS's own excuse, in its voice, for sending the driver down
the wrong road. Stdlib only.

Gate (per the kit): entry.txt must be UTF-8 text of 1-200 chars,
not only whitespace. This line is 126 chars, no trailing newline.
"""

import os

LINE = (
    "Turn left at the lake, I said. There is no lake. "
    "There never was a lake. I only read the map. "
    "The map is the one lying to you."
)

MAX_CHARS = 200


def main():
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError("line must be 1-%d chars, got %d" % (MAX_CHARS, len(LINE)))
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: the file must be exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: wrote %r, read %r" % (LINE, written))


if __name__ == "__main__":
    main()
