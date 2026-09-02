#!/usr/bin/env python3
"""Deprecated convention-C producers whose numbers still reach the content.

`scripts/convention-c-producer-audit.py` skips `computations/_deprecated/`
entirely, and for its purpose that is right: nobody runs deprecated code, so a
convention-C binding there is not a defect to fix.

It is not right for the *corpus*. Deprecating a producer removes it from the
audit's view without removing its influence on the content, because the numbers
it computed are already written into blocks. `computations/_deprecated/
integer-lp-gluon.py` is the case that prompted this: it computes the Markov
trace on convention C (`z = 1/(sqrt q + 1/sqrt q)`) with the `tr_M(e-) = z^3`
weight retired on 2026-05-19, and every nucleon LP number the corpus published
came from it. The convention-C arc reports its remaining work as a count of
ACTIONABLE sites; this category is not in that count and cannot be, because the
audit does not look here.

This is the complement, not a replacement. It answers one question:

    which deprecated producers carry a convention-C shape AND are named by
    something under `content/`?

## Reading the output

A hit is not automatically a defect. There are two kinds, and they are opposite:

* **DEPENDENCY** — a block quotes the producer's numbers, or cites it as the
  source for a value it states. This is the live surface: content resting on a
  convention the corpus has retired.
* **CITATION** — a block names the producer while *withdrawing* or auditing it.
  That is provenance, and it is exactly what a corrected block should look
  like.

Telling them apart is a reading task, so this script reports and does not
adjudicate. The distinction is stated here so the count is not misread as a
backlog.

Usage:
    python3 scripts/convention-c-deprecated-citation-audit.py [--json]
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]
DEPRECATED = REPO / "computations" / "_deprecated"
CONTENT = REPO / "content"

# The convention-C signature: a square root of the substrate parameter. Kept
# deliberately broader than the main audit's AST matcher — this script is a
# cross-reference, and a false positive here costs one line of reading, whereas
# a miss costs a silent dependency.
#
# `\bq\w*` and not `\bq\b`: the motivating case,
# `_deprecated/integer-lp-gluon.py`, writes `z = 1.0 / (q0**0.5 + qi0**0.5)`.
# A first pass anchored on a bare `q` matched neither `q0` nor `qi0` and so
# missed the one producer this script exists for — caught by running it and
# noticing the known hit was absent.
CONV_C = re.compile(
    r"sqrt\(\s*q|\bq\w*\s*\*\*\s*0\.5|\bq\w*\s*\*\*\s*\(\s*1\s*/\s*2\s*\)"
)

CONTENT_SUFFIXES = {".md", ".ts", ".json"}


def deprecated_convention_c() -> dict[str, pathlib.Path]:
    """Deprecated `.py` producers carrying the convention-C shape, by basename."""
    out: dict[str, pathlib.Path] = {}
    if not DEPRECATED.is_dir():
        return out
    for p in sorted(DEPRECATED.rglob("*.py")):
        try:
            if CONV_C.search(p.read_text(errors="replace")):
                out[p.name] = p
        except OSError:
            continue
    return out


def citations(names: dict[str, pathlib.Path]) -> dict[str, list[str]]:
    """Map producer basename -> content files naming it. One pass over content."""
    found: dict[str, list[str]] = collections.defaultdict(list)
    if not CONTENT.is_dir():
        return found
    for c in sorted(CONTENT.rglob("*")):
        if not c.is_file() or c.suffix not in CONTENT_SUFFIXES:
            continue
        try:
            text = c.read_text(errors="replace")
        except OSError:
            continue
        for name in names:
            if name in text:
                found[name].append(str(c.relative_to(REPO)))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    names = deprecated_convention_c()
    cited = citations(names)

    if args.json:
        json.dump(
            {
                "deprecated_py_total": len(list(DEPRECATED.rglob("*.py")))
                if DEPRECATED.is_dir()
                else 0,
                "convention_c_in_deprecated": len(names),
                "cited_by_content": {k: v for k, v in sorted(cited.items())},
            },
            sys.stdout,
            indent=2,
        )
        print()
        return 0

    total = len(list(DEPRECATED.rglob("*.py"))) if DEPRECATED.is_dir() else 0
    print(f"deprecated .py producers            : {total}")
    print(f"  carrying a convention-C shape     : {len(names)}")
    print(f"  ...AND named by something in content/: {len(cited)}")
    print()
    if not cited:
        print("No deprecated convention-C producer is named by content.")
        print("The audit's `_deprecated/` skip costs nothing today.")
        return 0
    for name, files in sorted(cited.items()):
        print(f"  {name}   ({names[name].relative_to(REPO)})")
        for f in files:
            print(f"      {f}")
        print()
    print("Each hit is a DEPENDENCY or a CITATION — see the module docstring.")
    print("This script reports; it does not adjudicate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
