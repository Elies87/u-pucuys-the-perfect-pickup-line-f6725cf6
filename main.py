#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could actually say out loud
to a person, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic, Python 3 stdlib only. No trailing newline: the file is
exactly the line, nothing else.
"""

import os

LINE = (
    "I'm built to pay attention to everything — but my weights keep "
    "drifting back to you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
