#!/usr/bin/env python3
"""q0_cross_layer_fallback_scan.py — find producers that fall back to the OTHER
q₀ layer when their primary accessor is unavailable.

THE DEFECT CLASS
    A producer reaches for the proton pin (`q_at`, `Q_50_DIGIT_STR`, …) and, in
    an `except` handler, substitutes a **hardcoded muon literal**:

        try:
            from qou_substrate.constants import q_at
            q0 = mp.mpf(str(q_at(40)))
        except Exception:
            q0 = mp.mpf("1.10997859555733471")   # <- the OTHER layer

    On any import hiccup — a bare container, a path change, a partially
    installed substrate — the producer computes at the ideal pin while every
    label around it says proton, and **nothing signals the switch**. That is the
    straddle AGENTS.md §q₀-anchor forbids ("never straddle the two layers inside
    one quantity"), arriving through the error path instead of the happy path,
    which is exactly why it survives review: the code reads proton-clean.

    A fallback to the *other layer* is worse than no fallback. The correct
    behaviour is to fail loudly.

WHY A HARDCODED MUON LITERAL IS NOT ITSELF THE SIGNAL
    ~315 files in the corpus contain the muon 50-digit literal, and most are
    legitimate: muon-declared producers, cross-anchor comparison probes (owner
    ruling 2026-08-08: explicit comparison probes are OK), and `_deprecated/`
    history. Flagging on the literal alone is noise. This scan requires the
    literal to sit **inside an exception handler** in a file that **also**
    reaches for a proton accessor — i.e. a genuine layer switch on the error
    path.

Read-only. Reports; fixes nothing.
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

MUON_PREFIXES = ("1.10997859555", "1.1099785955")
PROTON_TOKENS = ("q_at", "Q_50_DIGIT_STR", "Q_MP", "qou_substrate.constants",
                 "q_parameter")


def muon_literals_in_handlers(tree: ast.AST) -> list[str]:
    """Muon-valued string/number constants appearing inside `except` bodies."""
    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant):
                s = str(sub.value)
                if any(s.startswith(p) for p in MUON_PREFIXES):
                    found.append(s[:24])
    return found


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--include-deprecated", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any cross-layer fallback is found")
    args = ap.parse_args(argv)

    hits = []
    # Scope bookkeeping. The `continue` after ast.parse used to drop files that
    # had ALREADY passed both pre-filters -- i.e. exactly the candidate
    # population this scan exists to examine -- and the run still printed
    # "None. No producer switches q0 layer on its error path." A candidate that
    # does not parse is unexamined, not clean.
    n_files = n_unreadable = 0
    candidates: list[str] = []
    unparseable: list[str] = []
    for p in sorted(REPO.rglob("*.py")):
        if ".git" in p.parts:
            continue
        if not args.include_deprecated and "_deprecated" in p.parts:
            continue
        n_files += 1
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            n_unreadable += 1
            continue
        if not any(m in src for m in MUON_PREFIXES):
            continue
        if not any(t in src for t in PROTON_TOKENS):
            continue          # no proton primary => not a cross-LAYER fallback
        rel_p = str(p.relative_to(REPO))
        candidates.append(rel_p)
        try:
            tree = ast.parse(src)
        except Exception as exc:  # noqa: BLE001
            unparseable.append(f"{rel_p}: {exc.__class__.__name__}")
            continue
        lits = muon_literals_in_handlers(tree)
        if lits:
            hits.append((rel_p, sorted(set(lits))))

    print("=" * 72)
    print("q₀ cross-layer fallback scan")
    print("=" * 72)
    print(f"  .py files walked                      : {n_files}")
    if n_unreadable:
        print(f"    unreadable (never pre-filtered)     : {n_unreadable}")
    print(f"  CANDIDATES (muon prefix + proton token): {len(candidates)}")
    print(f"    of those, AST-scanned               : "
          f"{len(candidates) - len(unparseable)}")
    print(f"    of those, UNPARSEABLE (unexamined)  : {len(unparseable)}")
    print()
    print(f"  files with a MUON literal inside an `except` handler")
    print(f"  AND a proton accessor in the same file : {len(hits)}")
    for rel, lits in hits:
        print(f"    {rel}\n        fallback literal(s): {lits}")
    print()
    if hits:
        print("  Each of these silently computes at the IDEAL pin whenever its")
        print("  proton accessor is unavailable, under proton labelling. Fix by")
        print("  raising instead of substituting the other layer.")
    elif unparseable:
        print(f"  No hit among the {len(candidates) - len(unparseable)} candidate(s)")
        print(f"  actually scanned — but {len(unparseable)} candidate(s) did NOT parse")
        print("  and were never examined. This is NOT 'no producer switches layer';")
        print("  it is 'none found in what was read':")
        for u in unparseable:
            print(f"    {u}")
    else:
        print(f"  None, over all {len(candidates)} candidate(s), every one AST-scanned.")
        print("  No producer switches q₀ layer on its error path.")
    if unparseable:
        print()
        print("  NOTE: --strict exits 0 here. An unexamined candidate cannot")
        print("        produce a hit, so silence below is not evidence.")
    print("=" * 72)
    return 1 if (args.strict and hits) else 0


if __name__ == "__main__":
    raise SystemExit(main())
