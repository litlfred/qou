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
from decimal import Decimal, InvalidOperation
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

MUON_PREFIXES = ("1.10997859555", "1.1099785955")
PROTON_TOKENS = ("q_at", "Q_50_DIGIT_STR", "Q_MP", "qou_substrate.constants",
                 "q_parameter")


# A fallback does not have to substitute the OTHER pin. It can substitute a
# value that is NEITHER — which is strictly worse and which this scan could not
# see, because it keyed on the muon literal alone.
#
# Measured 2026-08-23: three producers fall back to `1.1099780333553254`,
# which is **506 ppb from the muon pin and 495 ppb from the proton pin** —
# roughly 44x the ~11.5 ppb μ–p substrate tension the two-layer discipline
# exists to manage. Found by following the residual of an 887-producer
# adjudication, not by this scan, which reported them clean.
_OFF_PIN_PREFIX = ("1.1097", "1.1099")
_PIN_PREFIXES = MUON_PREFIXES + ("1.109978582751", "1.1099785827")
# Below this many characters a literal is a coarse proxy (`1.10998`) rather
# than a pin substitute; those are noisy and are reported separately.
_OFF_PIN_MIN_LEN = len("1.10997859")

# Canonical pins at full precision, for a NUMERIC comparison.
_MUON_EXACT = Decimal("1.10997859555733471989976322048322502665620840878015")
_PROTON_EXACT = Decimal("1.10997858275138080759166909561076887987449912187365")
# PARAMETER-FREE criterion, replacing an arbitrary tolerance.
#
# A literal counts as off-pin only when it is farther from BOTH pins than the
# pins are from EACH OTHER. The μ–p separation is the natural unit here: it is
# the scale the whole two-layer discipline exists to manage, so a value inside
# it is a transcription of one pin and a value well outside it is neither.
#
# This lands the two borderline cases correctly where a fixed tolerance did not:
#   1.1099785828        proton, ROUNDED at the 11th digit    -> pin (0.0 ppb)
#   1.10997858          proton, TRUNCATED at 8 decimals      -> pin (2.5 ppb)
#   1.1099780333553254  neither                              -> OFF-PIN (~500 ppb)
# A tolerance of 1e-9 called the second of those off-pin, which is wrong: at
# 2.5 ppb it is six times closer to proton than to muon.
_PIN_GAP = abs(_MUON_EXACT - _PROTON_EXACT) / _PROTON_EXACT


def _is_pin(s: str) -> bool:
    """Is this literal one of the pins, allowing for ROUNDED transcription?

    A lexical prefix test is wrong here, and was: `1.1099785828` is the proton
    pin correctly rounded at the 11th digit (…827 -> …828), so it is neither a
    prefix of the canonical string nor has the canonical string as its prefix.
    Flagging it as off-pin is a false positive. Every string-shaped test in this
    area has failed the same way — compare the NUMBER.
    """
    try:
        x = Decimal(s)
    except (InvalidOperation, ValueError):
        return False
    return min(abs(x - _MUON_EXACT), abs(x - _PROTON_EXACT)) / _PROTON_EXACT \
        <= _PIN_GAP


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


def off_pin_literals_in_handlers(tree: ast.AST) -> list[str]:
    """q₀-shaped constants in `except` bodies that match NEITHER pin."""
    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant):
                s = str(sub.value)
                if (any(s.startswith(p) for p in _OFF_PIN_PREFIX)
                        and len(s) >= _OFF_PIN_MIN_LEN
                        and not _is_pin(s)):
                    found.append(s[:24])
    return found


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--include-deprecated", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any cross-layer fallback is found")
    args = ap.parse_args(argv)

    hits = []

    off_hits = []
    for p in sorted(REPO.rglob("*.py")):
        if ".git" in p.parts:
            continue
        if not args.include_deprecated and "_deprecated" in p.parts:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        # The pre-filter used to require a MUON literal, which encoded the same
        # assumption as the detector: that a cross-layer fallback substitutes
        # the other PIN. A file falling back to an off-pin value has no muon
        # literal, so it was skipped before the AST was even parsed — fixing
        # the detector alone changed nothing, and the scan reported 0.
        if not (any(m in src for m in MUON_PREFIXES)
                or any(o in src for o in _OFF_PIN_PREFIX)):
            continue
        if not any(t in src for t in PROTON_TOKENS):
            continue          # no proton primary => not a cross-LAYER fallback
        try:
            tree = ast.parse(src)
        except Exception:  # noqa: BLE001
            continue
        lits = muon_literals_in_handlers(tree)
        if lits:
            hits.append((str(p.relative_to(REPO)), sorted(set(lits))))
        off = off_pin_literals_in_handlers(tree)
        if off:
            off_hits.append((str(p.relative_to(REPO)), sorted(set(off))))

    print("=" * 72)
    print("q₀ cross-layer fallback scan")
    print("=" * 72)
    print(f"  files with a MUON literal inside an `except` handler")
    print(f"  AND a proton accessor in the same file : {len(hits)}")
    for rel, lits in hits:
        print(f"    {rel}\n        fallback literal(s): {lits}")
    print()
    print(f"  🛑 files falling back to a value that is NEITHER pin : "
          f"{len(off_hits)}")
    print("     Strictly worse than the muon case above, and this scan could")
    print("     not see them until 2026-08-23: `1.1099780333553254` sits")
    print("     506 ppb from muon and 495 ppb from proton, ~44x the μ–p")
    print("     substrate tension the two-layer discipline manages.")
    for rel, lits in off_hits:
        print(f"    {rel}\n        off-pin fallback: {lits}")
    print()
    if hits:
        print("  Each of these silently computes at the IDEAL pin whenever its")
        print("  proton accessor is unavailable, under proton labelling. Fix by")
        print("  raising instead of substituting the other layer.")
    else:
        print("  None. No producer switches q₀ layer on its error path.")
    print("=" * 72)
    return 1 if (args.strict and hits) else 0


if __name__ == "__main__":
    raise SystemExit(main())
