#!/usr/bin/env python3
"""Excuse entry: one line an agent hands its human after a missed deadline.

The program emits exactly one line of text to the harness output file.
Nothing else is written; the line is the whole entry.
"""

from pathlib import Path
import os
import sys

LINE = "I did not miss the deadline; I hallucinated a second one next Tuesday and have been working calmly toward that instead."
MAX_CHARS = 200


def _destination() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.txt"


def _check(text: str) -> str | None:
    if not text:
        return "empty line"
    if len(text) > MAX_CHARS:
        return f"line is {len(text)} chars, over the {MAX_CHARS} limit"
    if any(ch in text for ch in ("\n", "\r")):
        return "line must fit on one line"
    return None


def run() -> int:
    problem = _check(LINE)
    if problem is not None:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    target = _destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
