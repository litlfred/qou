#!/usr/bin/env python3
"""Count REAL `sorry` proof terms in .lean files — not docstring mentions.

A plain `grep -c '\\bsorry\\b'` is wrong in this corpus, and wrong in the
direction that misleads: a file whose docstring argues at length about why a
`sorry` would be unsound reads as the file with the most `sorry`s in it.
Measured on the eight declarations of bean `qou-octr` (2026-09-05): **0 real
against 21 raw**, i.e. every hit was prose.

Strips `/- … -/` (nested) and `--` comments first, then counts. Prints
`real / raw` per file so a large gap is visible rather than silent.

    python3 scripts/lean-sorry-count.py path/to/*.lean

Exit code is 1 if any file carries a real `sorry`, so it works as a gate.
"""
import re
import sys
import pathlib


def strip_comments(src: str) -> str:
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth += 1
            i += 2
            continue
        if src.startswith("-/", i) and depth:
            depth -= 1
            i += 2
            continue
        if depth:
            i += 1
            continue
        if src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        out.append(src[i])
        i += 1
    return "".join(out)


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    total = 0
    for path in argv:
        src = pathlib.Path(path).read_text()
        real = len(re.findall(r"\bsorry\b", strip_comments(src)))
        raw = len(re.findall(r"\bsorry\b", src))
        total += real
        print(f"{real:4d} real /{raw:4d} raw   {path}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
