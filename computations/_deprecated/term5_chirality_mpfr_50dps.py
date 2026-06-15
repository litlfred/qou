#!/usr/bin/env python3
"""
Plan F — Term 5 (chirality factor a_K) at MPFR @ 50 dps.

Term 5 of the unified mass formula is
    Term 5 = a_K · C_K

where a_K is the chirality factor from per-crossing symmetric-channel
duality ([prop:chirality-dual-space-derivation]):

    a_K = Π_{pn crossings c} (1 + sign(c) · h),   h = q − q^{-1}.

The standard isotope-family values
([prop:figure-eight-bw-coefficients]):

    1+h       — single positive pn crossing
    1−h       — single negative pn crossing
    1−h²      — one pn pair, opposite signs (figure-eight pattern, 4_1)
    (1−h²)²   — two pn pairs, opposite signs (⁴He)
    1         — no pn crossings (electron, p, n at single-nucleon level)

This script evaluates each at q_0 to 50 dps via mpmath.
C_K (per-knot prefactor) is multi-block-determined and atom-specific;
this script reports only the q-algebraic a_K factors. Per-atom
Term 5 = a_K · C_K is computed downstream by bw_chirality_isotopes.py.

Output: `term5-chirality-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf

mp.dps = 50

HERE = Path(__file__).parent
Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "term5-chirality-mpfr-50dps.witness.json"


def main() -> int:
    q_str = json.load(open(Q0))["derived_50_digit"]["q"]
    q_0 = mpf(q_str)
    h = q_0 - mpf(1) / q_0
    h_sq = h * h
    print(f"  q_0 (50 dps) = {q_str}")
    print(f"  h = q - 1/q (50 dps) = {h}")
    print(f"  h² (50 dps)          = {h_sq}")

    factors = [
        ("1 + h",        mpf(1) + h,
         "single positive pn crossing"),
        ("1 - h",        mpf(1) - h,
         "single negative pn crossing"),
        ("1 - h²",       mpf(1) - h_sq,
         "one pn pair, opposite signs (figure-eight 4_1)"),
        ("(1 - h²)²",    (mpf(1) - h_sq) * (mpf(1) - h_sq),
         "two pn pairs, opposite signs (⁴He)"),
        ("(1 - h²)³",    (mpf(1) - h_sq) ** 3,
         "three pn pairs, opposite signs (extrapolation)"),
        ("1",            mpf(1),
         "no pn crossings (electron, single-nucleon)"),
    ]

    print("\n  Chirality factor   value at q_0 (50 dps)              context")
    print("  " + "─" * 100)
    rows = []
    for name, v, ctx in factors:
        print(f"  {name:<14}  {str(v)[:40]:<40}  {ctx}")
        rows.append({
            "factor": name,
            "value_at_q0_50dps": str(v),
            "context": ctx,
        })

    out = {
        "computation": "term5-chirality-mpfr-50dps",
        "description":
            "Plan F — Term 5 chirality factor a_K = Π (1 + sign·h) "
            "for the standard pn-crossing patterns at q_0 to 50 dps. "
            "The per-knot prefactor C_K is multi-block-determined and "
            "atom-specific (see bw_chirality_isotopes.py); this witness "
            "reports only the q-algebraic a_K factors at 50 dps.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "q_0_50dps": q_str,
        "h_50dps": str(h),
        "h_squared_50dps": str(h_sq),
        "chirality_factors": rows,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
