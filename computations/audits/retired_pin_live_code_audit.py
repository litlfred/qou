#!/usr/bin/env python3
"""Retired-pin (A) literals in LIVE CODE — AST, not grep.

WHAT IT ANSWERS
    How many `.py` files still bind the RETIRED self-certified muon pin A
    (`1.1099785955573347...`) as a NUMBER the interpreter computes with?

WHY GREP CANNOT ANSWER IT
    Every fix-documentation comment ("this was 1.1099785955573347 until ...")
    is a grep hit forever, so the surface looks larger than it is and never
    appears to drain. Comments never become AST nodes. Measured 2026-09-04:
    grep 209 files, this audit 97 — grep over-counts 2.15x.

WHY "IN LIVE CODE" IS STILL NOT "IS A DEFECT"
    A literal can be live and legitimate: an audit that compares the three
    muon pins, a test that asserts the retired value, a dict of known pins.
    So each hit is classified by WHAT IT DOES:

      COMPUTE    bound to a name, or passed to mpf/Decimal/Fraction/... AND
                 the literal parses as a number  ->  the candidate defects
      REFERENCE  in a comparison, a dict/set, or a prose string  ->  fine
      UNCLEAR    neither shape matched; needs an eye

    CALIBRATED, not asserted. A 4-file hand check found 3 true positives
    (`gap_a4_numeric_search`, `lever1_gevrey_order_pin`,
    `binding_wn_derive_or_refute`, each `q = mp.mpf("1.1099785955573347...")`)
    and 1 false positive: `muon_pin_three_values_probe` carries the pin inside
    an assertion DETAIL STRING. The parse test added for exactly that case is
    what separates a number from prose that contains one.

    COMPUTE is a CANDIDATE list, agent-confirmed one at a time — several
    `audits/` entries are legitimately about the retired pin.

SCOPE WARNING FOR WHOEVER READS A PRIOR FIGURE
    A 2026-09-04 check-in reported the remaining surface as "48 producers
    (qbeta 31, audits 11, substrate 6)". That is three directories. This audit
    finds 83 COMPUTE candidates, 35 of them in `computations/` TOP LEVEL and
    more under habiro/markov/hecke/tools — none of which the 48 counts. An
    agent working from 48 would declare the tranche complete with ~36 files
    still live. Re-run this; do not quote a remembered number.

USAGE
    python3 computations/audits/retired_pin_live_code_audit.py [DIR ...]
    python3 computations/audits/retired_pin_live_code_audit.py --selftest
"""
from __future__ import annotations

import ast
import pathlib
import sys

RETIRED = "1.1099785955573347"
NUMERIC_CTORS = {"mpf", "mpmathify", "Decimal", "Fraction", "float", "Rational"}
DEFAULT_DIRS = ["computations", "tools", "scripts"]


def _docstring_constants(tree: ast.AST) -> set[int]:
    """ids of Constant nodes that are docstrings (they ARE AST nodes; skip)."""
    out: set[int] = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(n, "body", None)
            if (body and isinstance(body[0], ast.Expr)
                    and isinstance(body[0].value, ast.Constant)
                    and isinstance(body[0].value.value, str)):
                out.add(id(body[0].value))
    return out


def classify_source(src: str) -> str | None:
    """COMPUTE / REFERENCE / UNCLEAR, or None when the pin is not in live code."""
    if RETIRED not in src:
        return None
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return "UNCLEAR"
    docs = _docstring_constants(tree)
    parent: dict[int, ast.AST] = {}
    for n in ast.walk(tree):
        for c in ast.iter_child_nodes(n):
            parent[id(c)] = n

    verdicts: set[str] = set()
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Constant) and id(n) not in docs
                and RETIRED in str(n.value)):
            continue
        try:
            float(str(n.value).strip())
        except ValueError:
            verdicts.add("REFERENCE")      # prose that contains a number
            continue
        chain, cur = [], parent.get(id(n))
        for _ in range(3):
            if cur is None:
                break
            chain.append(cur)
            cur = parent.get(id(cur))
        v = "UNCLEAR"
        for c in chain:
            if isinstance(c, (ast.Compare, ast.Dict, ast.Set)):
                v = "REFERENCE"
                break
            if isinstance(c, ast.Call):
                fn = c.func
                nm = (fn.id if isinstance(fn, ast.Name)
                      else fn.attr if isinstance(fn, ast.Attribute) else "")
                v = "COMPUTE" if nm in NUMERIC_CTORS else "REFERENCE"
                break
            if isinstance(c, ast.Assign):
                v = "COMPUTE"
                break
        verdicts.add(v)
    if not verdicts:
        return None
    if "COMPUTE" in verdicts:
        return "COMPUTE"
    return "UNCLEAR" if "UNCLEAR" in verdicts else "REFERENCE"


def _selftest() -> int:
    cases = [
        ('q = mp.mpf("1.1099785955573347198")', "COMPUTE",
         "the type case: a numeric literal bound to a name"),
        ("q = mp.mpf('1.1099785955573347')", "COMPUTE", "single quotes"),
        ('d = {"detail": "measured 1.1099785955573347 vs stamped"}', "REFERENCE",
         "prose containing the number — the calibrated false positive"),
        ('assert q == "1.1099785955573347"', "REFERENCE", "a comparison"),
        ('PINS = {"retired": "1.1099785955573347"}', "REFERENCE", "a table of known pins"),
        ('"""Docstring naming 1.1099785955573347."""\nx = 1', None,
         "a docstring is not live code"),
        ("# comment naming 1.1099785955573347\nx = 1", None,
         "a comment is not an AST node at all"),
        ("x = 1", None, "no pin"),
    ]
    bad = 0
    for src, want, why in cases:
        got = classify_source(src)
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} {str(want):9} got {str(got):9}  {why}")
    print(f"\nselftest: {len(cases) - bad}/{len(cases)} passed")
    return 0 if bad == 0 else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return _selftest()
    dirs = [a for a in argv if not a.startswith("-")] or DEFAULT_DIRS
    buckets: dict[str, list[str]] = {"COMPUTE": [], "UNCLEAR": [], "REFERENCE": []}
    grep_files = 0
    for d in dirs:
        for p in sorted(pathlib.Path(d).rglob("*.py")):
            if "_deprecated" in p.parts:
                continue
            if p.resolve() == pathlib.Path(__file__).resolve():
                continue      # this file DEFINES the literal it hunts for
            try:
                src = p.read_text(encoding="utf-8")
            except Exception:                      # noqa: BLE001
                continue
            if RETIRED in src:
                grep_files += 1
            v = classify_source(src)
            if v:
                buckets[v].append(str(p))

    live = sum(len(v) for v in buckets.values())
    print("=" * 74)
    print("retired-pin (A) literals in LIVE CODE — AST, not grep")
    print("=" * 74)
    print(f"  scanned dirs                 : {', '.join(dirs)}")
    print(f"  files containing the string  : {grep_files}   (what grep reports)")
    print(f"  ...with it in LIVE CODE      : {live}"
          f"   (grep over-counts {grep_files / live:.2f}x)" if live else "")
    for k in ("COMPUTE", "UNCLEAR", "REFERENCE"):
        print(f"    {k:10} {len(buckets[k])}")
    print("\n  COMPUTE candidates by directory (agent-confirm one at a time):")
    counts: dict[str, int] = {}
    for f in buckets["COMPUTE"]:
        counts[str(pathlib.Path(f).parent)] = counts.get(str(pathlib.Path(f).parent), 0) + 1
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"    {k:52} {v}")
    if buckets["UNCLEAR"]:
        print("\n  UNCLEAR (needs an eye):")
        for f in buckets["UNCLEAR"]:
            print(f"    {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
