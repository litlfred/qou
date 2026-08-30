#!/usr/bin/env python3
"""threerow_sign_crossing_decomp.py — the per-λ terms of
F_D(q)=Σ_{λ⊢6,ℓ≥3} y_λ(q)·χ^λ(β_D;q)·Δ_λ, and why there is nothing to decompose.

🛑 THE QUESTION THIS FILE ASKED HAS NO ANSWER UNDER CONVENTION D.  Re-measured
2026-08-29.  It used to open "which ≥3-row partitions drive the deuteron sign
crossing", and sorted its rows by |term| to name the dominant block.

Under the canonical trace convention D (`z = q^3/(q^2+1)`, owner ruling
2026-08-15) the Wenzl level is `r = 2`, so `y_λ = 0` EXACTLY for every partition
with three or more rows.  F_D is therefore identically zero on this stratum, at
every q — there is no crossing, and no block drives one.  Its parent
`threerow_sign_crossing_probe.py` already records this: its committed witness
carries the passing assertion `three_row_object_is_structural_zero`.

WHY THE PARENT WAS REPAIRED AND THIS FILE WAS NOT.  The parent emits a witness,
so the numeric and dating layers of
`computations/audits/ylambda_threerow_frame_audit.py` could both see it.  This
companion emits none, so nothing but a source scan could reach it, and the
repair stopped at the file with the witness.  That is the blind spot the audit
now counts (44 witnessless y_λ consumers, 12 of them flagged); this is the
second instance found through it.

WHAT IT WAS PRINTING.  Every term at q₀ is between 1e-71 and 1e-75, and the
q→1⁺ column is exactly 0.0 — round-off from cancellation in the 70-dps compute,
not a measured quantity.  The old `sort(key=-abs(term))` then ORDERED those by
magnitude and printed `(3,2,1)` at the top, which reads as a structural finding
and is a ranking of numerical dust.  This is the `mu3_door_budget` failure mode
(PR #4673) in a different file: a filter over the annihilated stratum reporting
its own noise.

WHAT IT DOES NOW.  Compares against a noise floor scaled to the compute
precision, refuses to rank terms below it, and prints the partitions in a fixed
order so no spurious "dominant block" can be read off.  The per-λ values are
kept, because they are the evidence OF the cancellation — just never ranked.

Never compare against zero: the vanishing is a polynomial identity reached by
cancellation, so the residue depends on how q is spelled.

Bean qou-5wng (sibling instance).  Audit-only; emits no witness by design.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),
    str(Path(__file__).resolve().parent.parent / "substrate"),
    str(Path(__file__).resolve().parent.parent / "hecke"),
]
import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

from threerow_sign_crossing_probe import (  # noqa: E402
    chi_atom, delta_lambda, Q0, Q_LO,
)
from schur_principal_mpmath import y_lambda_at_q0_mpmath, partitions_of  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps()


def decomp(Z, N, name):
    n = 3 * (Z + N)
    print(f"\n=== {name}  n={n}  per-λ term y_λ·χ^λ·Δ_λ  (ℓ(λ)≥3) ===")
    y_lo = y_lambda_at_q0_mpmath(n, Q_LO)
    y_0 = y_lambda_at_q0_mpmath(n, Q0)
    tlo = t0 = mp.mpf(0)
    rows = []
    for lam in partitions_of(n):
        if len(lam) < 3:
            continue
        dl = delta_lambda(lam)
        a = y_lo[lam] * chi_atom(lam, Z, N, Q_LO) * dl
        b = y_0[lam] * chi_atom(lam, Z, N, Q0) * dl
        tlo += a
        t0 += b
        rows.append((lam, dl, a, b))

    # The noise floor. Scale it to the LARGEST |y_λ| over ALL partitions at this
    # n -- the ℓ>=3 entries are the ones that vanish, so scaling to them would
    # measure the residue against itself. Same construction the parent probe and
    # the y_lambda audit use.
    y_all = max(abs(mp.mpf(str(v))) for v in y_0.values())
    floor = y_all * mp.mpf(10) ** (-(mp.mp.dps - 8))

    # FIXED ORDER, never sorted by magnitude: below the floor these are round-off,
    # and ranking round-off manufactures a "dominant block" that does not exist.
    rows.sort(key=lambda r: r[0])
    print(f"{'λ':22s} {'Δ_λ':>6} {'term(q_lo)':>14} {'term(q₀)':>14}  {'':>5}")
    for lam, dl, a, b in rows:
        mark = "noise" if abs(b) < floor else "ABOVE"
        print(f"{str(lam):22s} {dl:>6d} {mp.nstr(a, 6):>14} {mp.nstr(b, 6):>14}"
              f"  {mark:>5}")
    print(f"{'TOTAL':22s} {'':>6} {mp.nstr(tlo, 6):>14} {mp.nstr(t0, 6):>14}")

    above = [r[0] for r in rows if abs(r[3]) >= floor]
    print(f"\n  noise floor (max|y_λ| over ALL λ × 10^-(dps-8)) = {mp.nstr(floor, 6)}")
    print(f"  terms above the floor: {len(above)} of {len(rows)}"
          + (f"  -> {above}" if above else ""))
    if not above:
        print("  => F_D is a STRUCTURAL ZERO on this stratum, as the parent probe's")
        print("     `three_row_object_is_structural_zero` assertion records. There is")
        print("     no sign crossing here and no block drives one; every value in the")
        print("     term columns above is cancellation residue, not a measurement.")
    return len(above)


if __name__ == "__main__":
    _above = decomp(1, 1, "D")
    # Exit 1 if anything clears the floor -- that would mean the structural zero
    # this file now documents had stopped holding, which is a real finding and
    # should not be silent.
    raise SystemExit(1 if _above else 0)
