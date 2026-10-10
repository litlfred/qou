#!/usr/bin/env python3
"""A decimal literal that carries more digits than its own parse can keep.

## The defect

A Python float literal is binary64. Writing more significant decimal digits
than the parse can retain asserts a precision the source does not have --
the extra digits are discarded before mpmath, `Decimal`, or anything else
sees the value.  The literal *reads* as a high-precision constant and holds
~17 digits.

Worked case, the one that motivated this audit (bean `qou-gqt5`):

    Q0 = 1.1099785827513808075916690956107688798744991218736   # 50 digits

50 digits of the proton substrate anchor, of which Python keeps 17.  The
corpus publishes the same value as a STRING -- `q_parameter.Q_50_DIGIT_STR`
-- precisely so that mpmath can be handed all 50.

## Why a digit COUNT is not the test, and what is

"More than 17 digits" over-flags.  A literal that is its own exact binary64
expansion loses nothing at the parse: it is verbose, not lying.  Those
expansions are long by nature (binary64 needs up to 767 significant digits
to write exactly) and terminate in the tail of a power-of-two denominator.

So the discriminator is a ROUND TRIP, not a length:

    Decimal(token) == Decimal(float(token))     # nothing lost -> not a defect

`Decimal(float)` is exact, so this compares the literal against the value it
actually becomes.  A literal failing it is asserting digits that vanish.

## What this audit does NOT do

It does not rewrite anything, and it does not decide what the correct value
IS -- a >17-digit literal may be the right number typed the wrong way, or
the wrong number entirely.  It reports; the fix is per-site.

It is AST-based, so quoted strings, comments and docstrings are structurally
invisible.  That is deliberate: the string form is the CORRECT spelling, and
a scanner keying on text would flag every fix it is asking for.

Usage:
    python3 computations/audits/overlong_float_literal_audit.py
    python3 computations/audits/overlong_float_literal_audit.py --selftest
"""
from __future__ import annotations

import argparse
import ast
import collections
import pathlib
import re
import sys
from decimal import Decimal

ROOTS = ("computations", "tools", "qou-mass")
_NUM = re.compile(r'^[+-]?(\d*)\.?(\d*)([eE][+-]?\d+)?$')


def significant_digits(token: str) -> int:
    """Significant decimal digits in a float literal's SOURCE TEXT."""
    t = token.strip().rstrip("jJ").replace("_", "")
    m = _NUM.match(t)
    if not m:
        return 0
    if "." not in t and not m.group(3):
        return 0                      # an integer-shaped token; not our class
    digits = (m.group(1) + m.group(2)).lstrip("0")
    return len(digits.rstrip("0"))


def loses_digits(token: str) -> bool:
    """True iff the parse discards digits the literal spells out."""
    try:
        return Decimal(token.replace("_", "")) != Decimal(float(token))
    except Exception:
        return False


def scan_source(src: str, path: str) -> list[dict]:
    """Every float literal in `src` that spells more than it can keep."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    lines = src.splitlines()
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or not isinstance(node.value, float):
            continue
        if node.lineno != node.end_lineno:
            continue
        token = lines[node.lineno - 1][node.col_offset:node.end_col_offset]
        n = significant_digits(token)
        if n <= 17 or not loses_digits(token):
            continue
        out.append({
            "file": path,
            "line": node.lineno,
            "digits": n,
            "literal": token,
            "kept": repr(float(token)),
            "context": lines[node.lineno - 1].strip()[:100],
        })
    return out


def scan(root: pathlib.Path) -> tuple[list[dict], int]:
    hits, scanned = [], 0
    for sub in ROOTS:
        base = root / sub
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            try:
                src = p.read_text(encoding="utf-8")
            except Exception:
                continue
            scanned += 1
            hits.extend(scan_source(src, str(p.relative_to(root))))
    return hits, scanned


def selftest() -> int:
    ok = True

    def chk(label, cond):
        nonlocal ok
        print(f"  {'ok  ' if cond else 'FAIL'}  {label}")
        ok = ok and cond

    # fires: 50 digits of the proton anchor, 17 survive
    chk("a 50-digit anchor literal fires",
        len(scan_source("Q0 = 1.1099785827513808075916690956107688798744991218736\n", "t")) == 1)
    # quiet: the same value written as a STRING is the correct spelling
    chk("the string form is invisible (it is the fix)",
        scan_source('Q0 = "1.1099785827513808075916690956107688798744991218736"\n', "t") == [])
    # quiet: a comment is not code
    chk("a comment is invisible",
        scan_source("# Q0 = 1.1099785827513808075916690956107688798744991218736\nx = 1\n", "t") == [])
    # quiet: an exact binary64 expansion loses nothing, however long
    lit = str(Decimal(float("0.1")))     # 0.1000000000000000055511151231257827021181583404541015625
    chk(f"an exact binary64 expansion is NOT flagged ({len(lit)} chars)",
        scan_source(f"x = {lit}\n", "t") == [])
    chk("...and that expansion really is over 17 digits",
        significant_digits(lit) > 17)
    # quiet: ordinary short literals
    chk("a short literal is quiet", scan_source("x = 3.14159\n", "t") == [])
    # quiet: integers are not this class
    chk("an integer literal is quiet", scan_source("x = 123456789012345678901\n", "t") == [])
    # fires: exponent form counts its mantissa digits
    chk("exponent form is counted",
        len(scan_source("x = 1.23456789012345678901e-5\n", "t")) == 1)

    print("\nselftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any live (non-_deprecated) hit remains")
    args = ap.parse_args()

    root = pathlib.Path(__file__).resolve().parents[2]

    if args.selftest:
        return selftest()

    hits, scanned = scan(root)
    live = [h for h in hits if ("_deprecated" not in h and "fsh-guts" not in h)["file"]]
    dead = len(hits) - len(live)

    print("=" * 78)
    print(" A LITERAL THAT SPELLS MORE DIGITS THAN ITS PARSE CAN KEEP")
    print("=" * 78)
    print(f"  files scanned            : {scanned}")
    print(f"  flagged literals         : {len(hits)}")
    print(f"    live                   : {len(live)}")
    print(f"    in computations/_deprecated : {dead}")
    print(f"  test                     : Decimal(token) != Decimal(float(token))")
    print(f"                             (an exact binary64 expansion is NOT a defect)")
    print()
    print("  The corpus spelling for a high-precision constant is a STRING --")
    print("  e.g. q_parameter.Q_50_DIGIT_STR -- read into mpmath with mp.mpf(s).")
    print()

    by_dir = collections.Counter(h["file"].rsplit("/", 1)[0] for h in live)
    for d, c in by_dir.most_common():
        print(f"    {c:4d}  {d}")
    print()
    for h in sorted(live, key=lambda x: -x["digits"]):
        print(f"  {h['file']}:{h['line']}  ({h['digits']} digits, keeps {h['kept']})")
        print(f"      {h['context']}")

    print()
    rc = selftest()
    if rc:
        return rc
    return 1 if (args.strict and live) else 0


if __name__ == "__main__":
    sys.exit(main())
