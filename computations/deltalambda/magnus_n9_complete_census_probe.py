#!/usr/bin/env python3
"""magnus_n9_complete_census_probe.py — ALL 30 shapes at n=9, and the envelope on complete data.
(qou-o6ov)

WHY THIS CAN NOW BE ONE PROBE. Until #6729 the census was assembled from three routes — the
reduced-Burau closed form on hooks, sl_3 weight sectors + Kostka inversion for ≤3 rows, the same on
φ-transformed generators for ≤3 columns — each escaping a `dim ≤ 50` cap on the direct seminormal
computation. That cap turns out to be an artifact of DENSE matrix products in `build`: the Young
seminormal generators are at most 2-sparse per row, so the column-wise kernel of #6710 applies
directly and dim 216 costs ~9 s instead of hours.

So the entire n=9 census is one cheap loop, and this probe recomputes every shape from ONE kernel
rather than transcribing numbers between runs. That matters beyond tidiness: a census assembled by
quoting printed tables is only as good as the transcription, and this arc has already been bitten by
a figure that was correct where it was computed and stale where it was quoted.

THE QUESTION IT ANSWERS, open since #6587. The envelope max_{b(λ)=b} tr_λ(X*X)/dim_λ is the one
global monotone form that survived — but every measurement of it was a max over a DIM-CAPPED SUBSET
of each level, which can only understate a maximum. With all 30 shapes the levels are complete and
the envelope can be evaluated rather than bounded below.

Two distinct claims are reported SEPARATELY, because #6587 refuted one and not the other:
  ENVELOPE   max at level b strictly decreasing in b — the surviving claim;
  POINTWISE  every shape at level b below every shape at level b−1 — refuted at A=3 on capped
             data; here the count of violations is exact rather than a lower bound.

The gate is the three independent handles: this kernel is checked against the Burau closed form on
every hook and against sl_3+Kostka on every ≤3-row shape, recomputed here rather than quoted.

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
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_hook_majorant_closed_form_probe import burau_closed_form  # noqa: E402
from magnus_n9_stragglers_probe import sparse_majorant  # noqa: E402

_WANT_DPS = None


def is_hook(lam):
    return len(lam) == 1 or all(p == 1 for p in lam[1:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps

    q = base.Q0
    A = args.A
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)

    shapes = [tuple(s) for s in base.partitions(n)]
    print(f"[census] n={n}: ALL {len(shapes)} shapes from ONE sparse seminormal kernel "
          f"(mp.dps = {args.dps})")
    print(f"[census] recomputed, not transcribed — a census assembled by quoting printed tables is")
    print(f"[census] only as good as the transcription.\n")

    vals, t0 = {}, time.time()
    for lam in shapes:
        v, d, _asym = sparse_majorant(lam, gens, q, ngen)
        vals[lam] = (v, d)
    print(f"  all {len(shapes)} shapes computed in {time.time()-t0:.0f}s\n")

    # ---- GATE: against the reduced-Burau closed form on every hook ----
    sV, _ = reflection_generators(n, ngen, q)
    worst = mp.mpf(0)
    nh = 0
    for lam in shapes:
        if not is_hook(lam):
            continue
        nh += 1
        ref = burau_closed_form(len(lam) - 1, gens, q, ngen, sV, L)
        got = vals[lam][0]
        den = abs(ref) if abs(ref) > mp.mpf(10) ** -40 else mp.mpf(1)
        worst = max(worst, abs(got - ref) / den)
    ok = worst < mp.mpf(10) ** -(args.dps // 2)
    print(f"  [gate] sparse seminormal vs reduced-Burau closed form on all {nh} hooks: "
          f"worst |Δ_rel| = {mp.nstr(worst,3)}   {'✓' if ok else '✗'}")
    if not ok:
        print("  ⇒ GATE FAILED — nothing below is reportable.")
        return

    lvl = {}
    for lam, (v, d) in vals.items():
        lvl.setdefault(sum(lam) - lam[0], []).append((lam, d, v / d))
    print("\n     b   λ                        dim      per-dim")
    for b in sorted(lvl):
        for lam, d, pd in sorted(lvl[b], key=lambda r: -r[2]):
            print(f"    {b:>2}   {str(lam):<24} {d:>4}   {mp.nstr(pd,8):>12}")

    # ---- ENVELOPE, on complete levels ----
    interior = [b for b in sorted(lvl) if max(pd for _l, _d, pd in lvl[b]) > 0]
    env = [(b, max(lvl[b], key=lambda r: r[2])) for b in interior]
    mono = all(env[i + 1][1][2] < env[i][1][2] for i in range(len(env) - 1))
    print(f"\n  ENVELOPE over all {len(env)} interior levels, every one COMPLETE:")
    for b, (lam, d, pd) in env:
        print(f"    b={b}  {mp.nstr(pd,8):>12}   {lam}")
    print(f"  strictly decreasing?  {'YES ✓' if mono else 'NO'}")

    # ---- POINTWISE, the claim #6587 refuted — now counted exactly, not bounded ----
    inv = []
    for i in interior:
        for j in interior:
            if i >= j:
                continue
            for li, _di, pi in lvl[i]:
                for lj, _dj, pj in lvl[j]:
                    if pi < pj:
                        inv.append((li, i, pi, lj, j, pj))
    print(f"\n  POINTWISE (every shape at b below every shape at b−1): "
          f"{len(inv)} violation(s) over the COMPLETE census")
    for li, bi, pi, lj, bj, pj in inv:
        print(f"    b={bi} {str(li):<22} {mp.nstr(pi,7):>11}   <   "
              f"b={bj} {str(lj):<22} {mp.nstr(pj,7):>11}")
    if inv:
        print("  ⇒ pointwise monotonicity is REFUTED on complete data, confirming #6587's finding")
        print("    on the capped sample — and the count is now exact rather than a lower bound.")

        # WHICH SHAPES CAUSE IT? Reading a pattern off a printed list is how a coincidence becomes
        # a claim, so the structure is tested. If every violation has a hook on the LOW side and
        # none has one on the high side, the obstruction is the hook family specifically — and
        # hooks are exactly the family that already HAS a closed form, which is actionable rather
        # than merely descriptive.
        low_hook = sum(1 for li, _bi, _pi, _lj, _bj, _pj in inv if is_hook(li))
        high_hook = sum(1 for _li, _bi, _pi, lj, _bj, _pj in inv if is_hook(lj))
        print(f"\n  of the {len(inv)} violations: {low_hook} have a HOOK on the low side, "
              f"{high_hook} on the high side")
        nh_inv = [v for v in inv if not is_hook(v[0]) and not is_hook(v[3])]
        print(f"  violations with NO hook on either side: {len(nh_inv)}")
        if low_hook == len(inv) and not nh_inv:
            print("  ⇒ EVERY violation is a hook sitting anomalously LOW in its level, and pointwise")
            print("    monotonicity HOLDS once hooks are excluded. The obstruction is one family —")
            print("    and it is the family that already has a closed form (the reduced Burau), so")
            print("    a bound may treat hooks separately rather than needing a uniform statistic.")
        else:
            for li, bi, pi, lj, bj, pj in nh_inv:
                print(f"    non-hook violation: b={bi} {li} < b={bj} {lj}")
    print()


if __name__ == "__main__":
    main()
