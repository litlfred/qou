#!/usr/bin/env python3
"""Count REAL `sorry`s in Lean files — comments and docstrings stripped first.

WHY THIS EXISTS
---------------
`grep -c sorry` over this corpus is badly wrong, and wrong in the direction that
wastes an agent's session: it reports work that does not exist.

Our Lean files routinely *say the word* in prose. Every one of these is a
docstring, not a proof obligation:

    "This file proves the algebraic core sorry-free."
    "no `sorry`, no axiom."
    "stated precisely with a cited `sorry`, deferred to MI-2"
    "-- SORRY: needs the argument principle ..."

Measured 2026-08-08: a naive scan of the resurgence arc reported sorries in
ArgumentPrinciple (2), BorelResummation (4), StokesMatrixDescent (1),
SYTBranchingRecursion (3), SYTHookGNW (3), RSKBridge (1), IdentityIHLFBridge (1).
**All seven files are actually clean — 0 real sorries between them.** An agent
tiering "attack vectors" off those numbers would have gone hunting for proof
obligations that were never there.

Refinements that still do NOT work, so nobody re-invents them:
  * `grep -w sorry`            — matches inside "sorry-free" (word boundary at '-')
  * excluding `sorry-free`     — still matches "no `sorry`, no axiom" (backticks)
  * excluding backticked forms — still matches `-- SORRY:` marker comments

The only reliable method is to strip Lean comments (`--` to end-of-line and
nested `/- ... -/`) and then look for `sorry` as a bare token in the remaining
code. That is what this does.

USAGE
  python3 scripts/real-sorry-scan.py [PATH ...]     # default: the whole repo
  python3 scripts/real-sorry-scan.py --list         # one line per occurrence

Exit status is 0 regardless of findings; this is a reporting tool, not a gate.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# `sorry` as a bare token: not part of an identifier, and not backtick-quoted.
SORRY = re.compile(r'(?<![\w`])sorry(?![\w`])')


def blank_lean_comments(src: str) -> str:
    """Replace `--` line comments and nested `/- ... -/` blocks with spaces.

    Comments are BLANKED, not deleted, and newlines are preserved, so the result
    is character- and line-aligned with the input. That alignment is the whole
    point: an earlier version deleted comment text, which desynchronised the line
    mapping and double-counted every hit.

    Nesting matters — Lean block comments nest, and `/-- ... -/` docstrings are
    block comments for this purpose — so this is a character scan, not a regex.
    """
    out: list[str] = []
    i = 0
    depth = 0
    n = len(src)
    while i < n:
        ch = src[i]
        if src.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
            continue
        if src.startswith('-/', i) and depth:
            depth -= 1
            out.append('  ')
            i += 2
            continue
        if depth:
            out.append('\n' if ch == '\n' else ' ')
            i += 1
            continue
        if src.startswith('--', i):
            nl = src.find('\n', i)
            stop = n if nl < 0 else nl
            out.append(' ' * (stop - i))
            i = stop
            continue
        out.append(ch)
        i += 1
    return ''.join(out)


def scan(path: Path) -> list[int]:
    """Return the 1-indexed line numbers of real sorries in `path`."""
    try:
        src = path.read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError):
        return []
    code = blank_lean_comments(src)
    return [i for i, line in enumerate(code.splitlines(), start=1)
            if SORRY.search(line)]


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith('--')]
    verbose = '--list' in argv
    roots = [Path(a) for a in args] or [Path('.')]

    files: list[Path] = []
    for root in roots:
        if root.is_file() and root.suffix == '.lean':
            files.append(root)
        else:
            files.extend(sorted(root.rglob('*.lean')))

    # Skip vendored dependency trees — we only care about our own Lean.
    files = [f for f in files if '.lake' not in f.parts]

    total = 0
    for f in files:
        hits = scan(f)
        if not hits:
            continue
        total += len(hits)
        print(f"{len(hits):3d}  {f}")
        if verbose:
            for ln in hits:
                print(f"       line {ln}")
    print(f"--- TOTAL real sorries: {total}  ({len(files)} files scanned)")
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
