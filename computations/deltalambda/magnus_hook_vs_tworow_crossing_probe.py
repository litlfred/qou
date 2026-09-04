#!/usr/bin/env python3
"""magnus_hook_vs_tworow_crossing_probe.py — settle the blocking pair from the two DERIVED closed
forms, and use them to go past the dim cap that limited every previous probe (qou-o6ov).

WHAT THIS ANSWERS. #6669 found that five of seventeen candidate statistics come within one
inversion of ordering tr_λ(X*X)/dim_λ at A=3, and that all five fail on the SAME pair:

    (7,1,1)  hook,    j = b = 2,  dim 28,  per-dim 3478.285
    (7,2)    two-row, k = b = 2,  dim 27,  per-dim 2793.099

Every one of them ranks (7,2) above (7,1,1); the majorant ranks them the other way. That pair sits
exactly at the intersection of the two columns that already HAVE closed forms, so the comparison
can be DERIVED rather than measured:

    hook:     tr_(n-b,1^b)(X*X) = -c²·q^{(2L+4)(1-b)}·Σ_{a,b'} Σ_± ± e_b(μ(word))   (#6556)
              — an (n-1)×(n-1) reduced-Burau computation, dim_λ = C(n-1, b)
    two-row:  tr_(n-b,b)(X*X)   = ‖X|_{W_b}‖_F² − ‖X|_{W_(b-1)}‖_F²                 (#6587)
              — Frobenius norms on C(n,b)-dim sectors of the fixed 4×4 Ř,
                dim_λ = C(n,b) − C(n,b-1)

THE SECOND PAYOFF, and it may be the larger one. Neither closed form builds the seminormal irrep,
so neither is bound by the dim ≤ 50 cap that made every earlier probe skip 17 of 28 shapes at n=9 —
including the hooks (6,1,1,1) dim 56, (5,1⁴) dim 70, (4,1⁵) dim 56. Those were reported as "not
run, not evidence"; here they are run. So this probe reports the FULL hook column and the FULL
two-row column at A=3 for the first time, and can therefore ask whether each column is separately
monotone in b beyond the cap — which no previous measurement could.

THE CROSS-CHECK THAT MAKES THE EXTRAPOLATION HONEST. Extending a formula past the range where it
was verified is exactly how a measured identity turns into an assumed one, so:
  (1) every value inside the cap is checked against the direct seminormal tr_λ(X*X);
  (2) at b=1 the hook (n-1,1) IS the two-row (n-1,1) — the SAME shape reached by two independent
      reductions, so the two closed forms must agree there. That is a check of the reductions
      against each other, not against the thing they are both derived from.
Only after both pass does the probe report the out-of-cap values.

THE QUESTIONS, in order:
  (Q1) do the two closed forms reproduce the direct value everywhere the direct value exists?
  (Q2) do they agree with each other at b=1, where they describe one shape?
  (Q3) is hook(b) > two-row(b) per-dim at every b — is the blocking pair's direction systematic?
  (Q4) with the cap gone, is each column separately monotone in b per-dim?

scope-(a); NO-FLOAT64 (mpf, dps 140). No fit, no witness, nothing wired.
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

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_hook_majorant_closed_form_probe import burau_closed_form  # noqa: E402
from magnus_tworow_majorant_sector_probe import sector_majorant  # noqa: E402

DIM_CAP = 50   # the cap the DIRECT seminormal computation is held to; the closed forms ignore it


def direct(lam, gens, q, ngen):
    """tr_λ(X*X) in the seminormal irrep, or None when dim exceeds the cap."""
    _pg, d = base.block_structure(tuple(lam))
    if d > DIM_CAP:
        return None, d
    X, Xstar, dim, _a = build(tuple(lam), gens, q, ngen)
    P = Xstar * X
    return mp.re(sum(P[i, i] for i in range(dim))), dim


def analyze(A):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)
    sV, dimV = reflection_generators(n, ngen, q)

    print(f"[cross] A={A} (n={n}); hook(b) vs two-row(b) at equal b, both from DERIVED closed forms")
    print(f"[cross] hook via {dimV}x{dimV} reduced Burau; two-row via the fixed 4x4 Ř sectors.")
    print(f"[cross] Neither builds the seminormal irrep ⇒ NEITHER is bound by the dim ≤ {DIM_CAP} cap.\n")

    # ---- the two columns, computed from the closed forms ----
    hook_rows, trow_rows = [], []
    prev_sector = mp.mpf(0)
    for b in range(0, n):
        lam = tuple([n - b] + [1] * b)
        cf = burau_closed_form(b, gens, q, ngen, sV, L)
        d = math.comb(n - 1, b)
        dv, dd = direct(lam, gens, q, ngen)
        hook_rows.append((b, lam, d, cf, dv, dd))
    for b in range(0, n // 2 + 1):
        lam = (n - b, b) if b > 0 else (n,)
        sec, _dW, _asym = sector_majorant(n, b, gens, q)
        val = mp.re(sec) - prev_sector
        prev_sector = mp.re(sec)
        d = math.comb(n, b) - (math.comb(n, b - 1) if b > 0 else 0)
        dv, dd = direct(lam, gens, q, ngen)
        trow_rows.append((b, lam, d, val, dv, dd))

    # ---- (Q1) verify against the direct value wherever the direct value exists ----
    worst = mp.mpf(0)
    n_checked = n_out = 0
    for _b, _lam, _d, cf, dv, _dd in hook_rows + trow_rows:
        if dv is None:
            n_out += 1
            continue
        n_checked += 1
        den = abs(dv) if abs(dv) > mp.mpf(10) ** -100 else mp.mpf(1)
        worst = max(worst, abs(cf - dv) / den)
    q1 = worst < mp.mpf(10) ** -100

    # ---- (Q2) the two reductions meet at b=1: (n-1,1) is BOTH a hook and a two-row ----
    h1 = next(r for r in hook_rows if r[0] == 1)
    t1 = next(r for r in trow_rows if r[0] == 1)
    den = abs(h1[3]) if abs(h1[3]) > mp.mpf(10) ** -100 else mp.mpf(1)
    agree = abs(h1[3] - t1[3]) / den
    q2 = agree < mp.mpf(10) ** -100 and h1[2] == t1[2]

    print("   b   hook λ            dim   per-dim (Burau)   |  two-row λ    dim   per-dim (Ř sectors)"
          "   |  hook > two-row?   in cap?")
    for b in range(0, n):
        hb = next((r for r in hook_rows if r[0] == b), None)
        tb = next((r for r in trow_rows if r[0] == b), None)
        hp = hb[3] / hb[2] if hb and hb[2] else None
        tp = tb[3] / tb[2] if tb and tb[2] else None
        cmpstr = "—"
        if hp is not None and tp is not None:
            same = hb[1] == tb[1]
            cmpstr = "SAME SHAPE" if same else ("hook >" if hp > tp else "two-row >")
        incap = ("both" if (hb and hb[4] is not None) and (tb and tb[4] is not None)
                 else "hook" if (hb and hb[4] is not None)
                 else "two-row" if (tb and tb[4] is not None) else "NEITHER")
        tcol = (f"{str(tb[1]):<12} {tb[2]:>4}   {mp.nstr(tp,8):>16}" if tb else " " * 35)
        print(f"  {b:>2}   {str(hb[1]):<16} {hb[2]:>4}   {mp.nstr(hp,8):>15}   |  {tcol}"
              f"   |  {cmpstr:<12}  {incap}")

    print()
    print(f"  (Q1) closed forms reproduce the DIRECT seminormal value, everywhere it exists?  "
          f"{'YES ✓' if q1 else 'NO ✗'}")
    print(f"       {n_checked} shape(s) checked in cap, worst |Δ_rel| = {mp.nstr(worst,3)}; "
          f"{n_out} shape(s) are OUT of cap and have no direct value to check against.")
    print(f"  (Q2) the two INDEPENDENT reductions agree at b=1, where (n-1,1) is both a hook and a")
    print(f"       two-row?  {'YES ✓' if q2 else 'NO ✗'}  (|Δ_rel| = {mp.nstr(agree,3)}, "
          f"dims {h1[2]} vs {t1[2]})")
    if not (q1 and q2):
        print("\n  ⇒ a verification failed. The out-of-cap values below are NOT reportable until it")
        print("    passes — extending an unverified formula is how a measured identity becomes an")
        print("    assumed one. Stopping here rather than reporting them.")
        return

    # ---- (Q3) is the blocking pair's direction systematic? ----
    both = [(b, hook_rows[b][3] / hook_rows[b][2], trow_rows[b][3] / trow_rows[b][2])
            for b in range(1, min(n, n // 2 + 1))
            if hook_rows[b][1] != trow_rows[b][1] and hook_rows[b][2] and trow_rows[b][2]]
    hook_wins = [b for b, hp, tp in both if hp > tp]
    trow_wins = [b for b, hp, tp in both if hp <= tp]
    print(f"\n  (Q3) hook(b) > two-row(b) per-dim, at the {len(both)} b where the two shapes DIFFER?")
    print(f"       hook larger at b = {hook_wins};  two-row larger at b = {trow_wins}")
    if trow_wins and hook_wins:
        print("       ⇒ the relation REVERSES with b. So 'hooks sit above two-rows' is NOT a general")
        print("         fact, and the blocking pair is not an instance of a systematic ordering —")
        print("         it is specific to its b. Any statistic must reproduce a relation that")
        print("         changes sign, which is a much stronger demand than a monotone one.")
        # WHERE does it reverse? Reported because the answer is suggestive and therefore needs
        # its sample size stated beside it: b = ⌊n/2⌋ is the LAST b at which a two-row exists at
        # all — the shape (n−b, b) is as square as it can be. If the reversal always sits there,
        # it is a boundary effect of the two-row column rather than a crossing in the interior.
        last_b = max(b for b, _hp, _tp in both)
        at_edge = trow_wins == [last_b]
        print(f"       WHERE: first reversal at b = {min(trow_wins)}; the last b with a two-row at all"
              f" is ⌊n/2⌋ = {n // 2}.")
        print(f"       Reversal confined to that final b?  {'YES' if at_edge else 'NO'}  — if YES this"
              " is a BOUNDARY")
        print("       effect (the two-row is then as square as it gets), not an interior crossing.")
        print("       ONE SIZE is one data point: do not read a rule off it. Compare across A.")
    elif hook_wins and not trow_wins:
        print("       ⇒ SYSTEMATIC on this sample: the hook exceeds the two-row at every comparable")
        print("         b. Then a statistic ordering the majorant must rank hooks above two-rows at")
        print("         equal b — and the five near-misses of #6669 all do the opposite, which is")
        print("         one explanation covering every one of them rather than a coincidence.")

    # ---- (Q4) per-column monotonicity, now with the cap gone ----
    for label, rows in (("hook", hook_rows), ("two-row", trow_rows)):
        pd = [(b, r[3] / r[2]) for b, r in ((r[0], r) for r in rows) if r[2] and r[3] > 0]
        mono = all(pd[i + 1][1] < pd[i][1] for i in range(len(pd) - 1))
        outc = sum(1 for r in rows if r[4] is None and r[3] > 0)
        print(f"\n  (Q4) {label} column: per-dim strictly decreasing in b over ALL {len(pd)} shapes "
              f"({outc} of them beyond the old cap)?  {'YES ✓' if mono else 'NO'}")
        print("       " + " > ".join(mp.nstr(v, 6) for _b, v in pd))
        if not mono:
            bad = [(pd[i][0], pd[i + 1][0]) for i in range(len(pd) - 1) if pd[i + 1][1] >= pd[i][1]]
            print(f"       violations at b = {bad}  ← the cap was hiding this; report it, do not")
            print("       restate the in-cap monotonicity as though it held generally.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    args = ap.parse_args()
    for A in args.A:
        analyze(A)
        print()


if __name__ == "__main__":
    main()
