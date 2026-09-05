#!/usr/bin/env python3
"""magnus_hook_rank_crossover_probe.py — the hook does not merely sit low: it crosses from the
MAXIMUM of its b-level to the MINIMUM. (qou-o6ov)

THE SHARPENING. #6729 established on the complete n=9 census that all 6 pointwise-monotonicity
violations have a hook on the low side, and concluded "the obstruction is the hook family". That
understates what the data shows. Ranking each hook within its own level:

    b=2  (7,1,1)   3478.29   MAXIMUM of its level
    b=3  (6,1,1,1) 1671.23   MAXIMUM
    b=4  (5,1⁴)     581.16   MINIMUM
    b=5  (4,1⁵)     134.63   MINIMUM
    b=6  (3,1⁶)      14.32   MINIMUM
    b=7  (2,1⁷)       0.435  MINIMUM

The hook is the TOP of its level at small b and the BOTTOM at large b, crossing between b=3 and
b=4 — which is exactly where #6677 found the hook/two-row ratio crossing 1. So two results this arc
has been treating as separate are one fact: THE HOOK COLUMN DECAYS FASTER THAN EVERY OTHER FAMILY,
and its rank within a level is a clean scalar summary of that.

WHAT THIS PROBE MEASURES, and what it deliberately does not. Establishing "the hook is the MINIMUM
of level b" requires every shape at that level. At n=9 that is available (complete census, #6729).
At n=12 it is NOT and will not be: Σ_λ dim_λ² = 12! so a complete census is ~1e11 operations even
with the sparse kernel. But the interesting half is cheap, because refuting maximality needs only
ONE shape above the hook:

    "hook is the level MAX"  — refuted by a single counterexample   → CHEAP
    "hook is the level MIN"  — needs the whole level                → EXPENSIVE

So at n=12 this probe computes the hook column (reduced Burau, 11×11 — trivial) against the two-row
column (sl_2 weight sectors, C(12,k) ≤ 924 via the #6710 sparse kernel — affordable) and reports,
per level, whether the hook is ABOVE or BELOW the one comparison shape available. That decides
maximality at every b it reaches, and it decides minimality at NO b. The output says which, per row,
rather than letting a partial level read as a complete one.

If the crossover sits at the same b at n=9 and n=12 while n grows by a third, that is evidence the
rank crossover is a real feature and not an n=9 coincidence — which is the one thing #6729's
hook-exclusion result could not distinguish.

scope-(a); NO-FLOAT64 (mpf; dps asserted at every compute entry). Nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_hook_majorant_closed_form_probe import burau_closed_form  # noqa: E402
from magnus_a4_crossing_sparse_probe import sector_majorant_sparse  # noqa: E402
from magnus_n9_stragglers_probe import sparse_majorant  # noqa: E402

_WANT_DPS = None


def _assert_dps(where):
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


def hook_rank_complete(n, gens, q, ngen):
    """n=9 only: the hook's exact RANK within each complete level (1 = maximum)."""
    lvl = {}
    for lam in base.partitions(n):
        lam = tuple(lam)
        v, d, _a = sparse_majorant(lam, gens, q, ngen)
        lvl.setdefault(sum(lam) - lam[0], []).append((lam, v / d))
    out = []
    for b in sorted(lvl):
        rows = sorted(lvl[b], key=lambda r: -r[1])
        if len(rows) < 2 or rows[0][1] <= 0:
            continue
        hk = tuple([n - b] + [1] * b)
        rank = next(i for i, (l, _v) in enumerate(rows) if l == hk) + 1
        out.append((b, rank, len(rows), rows[0][1], rows[-1][1]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[3, 4])
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps
    q = base.Q0

    for A in args.A:
        n = 3 * A
        Z, N = A // 2, A - A // 2
        gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
        ngen = max(gens) + 1
        L = len(gens)
        sV, _ = reflection_generators(n, ngen, q)
        _assert_dps(f"A={A}")

        print(f"[rank] A={A} (n={n})")
        if n <= 9:
            # COMPLETE census is affordable here, so the hook's exact rank is available.
            print(f"  complete census affordable — reporting the hook's EXACT RANK per level")
            print("     b   hook rank / level size   level max      level min      hook is")
            for b, rank, size, hi, lo in hook_rank_complete(n, gens, q, ngen):
                where = ("MAXIMUM" if rank == 1 else
                         "MINIMUM" if rank == size else f"rank {rank}")
                print(f"    {b:>2}   {rank:>6} / {size:<14} {mp.nstr(hi,8):>12}   "
                      f"{mp.nstr(lo,8):>12}   {where}")
        else:
            # Complete census is ~1e11 ops (Σ dim_λ² = n!). Refuting MAXIMALITY needs one shape.
            print(f"  complete census NOT affordable (Σ_λ dim_λ² = {n}! ), so only MAXIMALITY is")
            print(f"  decidable here — one comparison shape suffices to refute it, and no number")
            print(f"  of shapes short of the whole level can establish MINIMALITY.")
            print("     b   hook per-dim     two-row per-dim   hook > two-row?   decides")
            prev = mp.mpf(0)
            for b in range(1, n // 2 + 1):
                hk = burau_closed_form(b, gens, q, ngen, sV, L) / math.comb(n - 1, b)
                sec, _D = sector_majorant_sparse(n, b, gens, q)
                d = math.comb(n, b) - math.comb(n, b - 1)
                tr = (mp.re(sec) - prev) / d
                prev = mp.re(sec)
                if b == 1:
                    print(f"    {b:>2}   {mp.nstr(hk,8):>14}   {mp.nstr(tr,8):>15}   "
                          f"{'same shape':<15}   nothing (they are one shape)")
                    continue
                above = hk > tr
                print(f"    {b:>2}   {mp.nstr(hk,8):>14}   {mp.nstr(tr,8):>15}   "
                      f"{('yes' if above else 'NO'):<15}   "
                      f"{'hook still could be max' if above else 'hook is NOT the level max'}")
        print()


if __name__ == "__main__":
    main()
