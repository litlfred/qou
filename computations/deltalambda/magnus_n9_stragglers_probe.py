#!/usr/bin/env python3
"""magnus_n9_stragglers_probe.py — the four n=9 shapes no tensor handle reaches. (qou-o6ov)

WHAT IS LEFT. Of the 30 partitions of 9, the handles now cover 26: the sl_3 weight-sector +
Kostka inversion gives the 12 with ≤3 ROWS, the same machinery on φ-transformed generators
(φ: σ_i ↦ −σ_i⁻¹) gives the 12 with ≤3 COLUMNS — overlapping only in (3,3,3) — and the
reduced-Burau closed form adds 3 further hooks. The remaining four are

    (5,2,1,1) dim 189    (4,3,1,1) dim 216    (4,2,2,1) dim 216    (4,2,1,1,1) dim 189

and each has ≥4 rows AND ≥4 columns, so NEITHER orientation of a k=3 construction reaches
them. k=4 does in principle and is hopeless in practice: the largest weight sector for
n=9, k=4 is multinomial(9; 3,2,2,2) = 7560, against 1680 for k=3, and the kernel cost goes
as D².

THE INVERSION WORTH NOTICING. For exactly these four the DIRECT seminormal construction is
the CHEAPER route — dim ≤ 216 against a 7560-dim weight sector. Every other step of this arc
went the other way (the tensor handles existed precisely to escape the seminormal dim cap),
so the natural instinct here is the wrong one. The cap was never a statement about the
seminormal construction being expensive in absolute terms; it was a budget, and 216 fits it.

Completing these closes n=9 at 30/30 and makes EVERY b-level complete for the first time —
which is what the envelope question (open since #6587) actually needs. Levels b=1,2,3 closed
in #6729; b=4..7 each still miss shapes, and an envelope over a partial level is a lower
bound on a maximum, not a maximum.

VERIFICATION. There is no second route to these four by construction — that is what makes
them stragglers — so they cannot be cross-checked the way every other shape in this arc was.
What IS checked, and stated rather than glossed: the same `build` path is exercised on shapes
that DO have independent references (it is the reference used throughout #6587/#6729 and
agrees with the Burau and sl_2 routes to ~1e-63), and the positivity tr_λ(X*X) ≥ 0 must hold
for every shape since X*X is a positive element. A negative value here would mean the
construction is wrong, and the probe says so rather than reporting the number.

scope-(a); NO-FLOAT64 (mpf; dps asserted at every compute entry). Nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402

_WANT_DPS = None

STRAGGLERS = [(5, 2, 1, 1), (4, 3, 1, 1), (4, 2, 2, 1), (4, 2, 1, 1, 1)]


def _assert_dps(where):
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, default=65)
    ap.add_argument("--shapes", type=str, default="",
                    help="comma-separated subset, e.g. '5,2,1,1' — default all four")
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps

    q = base.Q0
    n = 9
    A = 3
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    shapes = STRAGGLERS
    if args.shapes:
        want = tuple(int(x) for x in args.shapes.split(","))
        shapes = [s for s in STRAGGLERS if s == want]

    print(f"[strag] n={n}: the {len(STRAGGLERS)} shapes with ≥4 rows AND ≥4 columns — no k=3")
    print(f"[strag] orientation reaches them, and k=4's largest weight sector is 7560 vs 1680.")
    print(f"[strag] Direct seminormal (dim ≤ 216) is the CHEAPER route for exactly these.")
    print(f"[strag] mp.dps = {args.dps}, asserted at every compute entry.\n")
    print("   λ                  dim    χ_λ(X*X)             per-dim        b(λ)   positive?   wall")
    ok = True
    for lam in shapes:
        _assert_dps(f"straggler {lam}")
        t0 = time.time()
        X, Xstar, dim, _asym = build(lam, gens, q, ngen)
        P = Xstar * X
        val = mp.re(sum(P[i, i] for i in range(dim)))
        el = time.time() - t0
        pos = val >= 0
        ok = ok and pos
        print(f"  {str(lam):<18} {dim:>4}   {mp.nstr(val,10):>16}  {mp.nstr(val/dim,8):>13}   "
              f"{sum(lam)-lam[0]:>4}   {'yes' if pos else 'NO ✗':<9}  {el:.0f}s")
    print()
    if ok:
        print("  positivity holds on every shape (X*X is a positive element, so it must).")
        print("  ⇒ with these four, n=9 is COMPLETE at 30/30 and every b-level closes — which is")
        print("    what the envelope question needs. No independent second route exists for these")
        print("    four BY CONSTRUCTION; that is what makes them stragglers, and it is a real")
        print("    weakening of the evidence relative to every other shape in this arc.")
    else:
        print("  ⇒ A NEGATIVE VALUE APPEARED. X*X is a positive element, so this is a construction")
        print("    error, not a result. Report it; do not carry the number into the census.")


if __name__ == "__main__":
    main()
