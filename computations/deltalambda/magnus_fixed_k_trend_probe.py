#!/usr/bin/env python3
"""magnus_fixed_k_trend_probe.py — the failure sits at a FIXED k and grows with A. (qou-o6ov)

WHAT THE COLUMN PROBE SHOWED, and what it could not. The ≤2-row column
(`magnus_tworow_column_true_element_probe.py`) reports where monotonicity breaks at each A. Read
across sizes, the breaks are not scattered — the same step `k=3→4` fails at A=3, 4 and 5, and the
A=2 column is simply too short to contain that step. That is a fixed-`k` feature, independent of `n`,
which a per-A monotonicity verdict cannot express.

This probe measures that one step directly, across A, so the trend is the output rather than
something a reader has to reconstruct from three separate tables.

THE QUANTITY, and it is the one the y-weighted sum actually needs. `|c_λ| = y_λ·|tr_λ|` carries no
`dim`, so y-weighted monotonicity at a step is exactly

    |tr_{k+1}| / |tr_k|   <   y_k / y_{k+1}   =   [n−2k+1]_q / [n−2k−1]_q

Both sides are reported, plus their ratio. Quoting `|tr|/dim` against that ceiling is the wrong
comparison and cost a correction earlier in this arc — at the square end `dim` falls sharply, which
inflates `|tr|/dim` by ~2× exactly where the ceiling is tightest.

WHY THE TREND MATTERS MORE THAN THE VERDICT. The weight side is known in closed form and its
behaviour at fixed `k` is forced: as `n` grows, `[n−2k+1]_q/[n−2k−1]_q → q²`, so the protection
available at any fixed `k` **decreases monotonically toward 1.2321** — a ceiling that not only cannot
be raised but *falls*. If the trace ratio at that same `k` grows with A, the two move apart without
bound and the y-weighted route is not merely broken at one size, it is getting worse at a rate.

That is a much stronger negative than "monotonicity fails at A=4", and it is the reason to spend
compute on a fourth and fifth size rather than declaring the question closed at three.

SCOPE — (a) scope-limited. Measures one step per A at one q₀; a rate read off a handful of sizes is
a trend, not an asymptotic statement, and this session has already been caught once treating two
agreeing sizes as a mechanism.
NO-FLOAT64: mpf end to end, dps 65, `_assert_dps` guard inherited, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_true_hecke_element_probe import sweep  # noqa: E402
import magnus_true_hecke_element_probe as TE  # noqa: E402


def qint(m, q):
    if m == 0:
        return mp.mpf(0)
    return (q ** m - q ** (-m)) / (q - 1 / q)


def shape(n, k):
    return (n - k,) if k == 0 else (n - k, k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3, help="the step measured is k -> k+1")
    ap.add_argument("--A", type=int, nargs="+", default=[3, 4, 5])
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps
    TE._WANT_DPS = args.dps
    q = base.Q0
    k = args.k

    print(f"[fixedk] The step k={k}→{k + 1} across A, for the TRUE Hecke element.")
    print(f"[fixedk] y-weighted monotonicity at this step needs  |tr_{k + 1}|/|tr_{k}| < "
          f"[n−2k+1]_q/[n−2k−1]_q.")
    print(f"[fixedk] The ceiling FALLS toward q² = {mp.nstr(q ** 2, 6)} as n grows, so the "
          f"protection erodes with A.  (dps={args.dps})\n")
    print(f"  {'A':>3}{'n':>4}  {'λ_k':<10}{'λ_k+1':<10}{'dim_k':>7}{'dim_k+1':>8}"
          f"{'|tr| ratio':>13}{'ceiling':>11}{'margin':>10}  verdict")

    rows = []
    for A in args.A:
        n = 3 * A
        if k + 1 > n // 2:
            print(f"  {A:>3}{n:>4}  (column has no k={k + 1}; ⌊n/2⌋={n // 2})")
            continue
        Z, N = A // 2, A - A // 2
        word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
        ngen = max(g for _c, _d, g in word) + 1
        lk, lk1 = shape(n, k), shape(n, k + 1)

        t0 = time.time()
        tk, _f, dk = sweep(lk, word, q, ngen, true_coeffs=True)
        tk1, _f2, dk1 = sweep(lk1, word, q, ngen, true_coeffs=True)
        el = time.time() - t0

        if abs(tk) == 0:
            print(f"  {A:>3}{n:>4}  |tr_k| is zero — ratio undefined")
            continue
        ratio = abs(tk1) / abs(tk)
        ceil = qint(n - 2 * k + 1, q) / qint(n - 2 * k - 1, q)
        margin = ceil / ratio
        rows.append((A, n, ratio, ceil, margin))
        print(f"  {A:>3}{n:>4}  {str(lk):<10}{str(lk1):<10}{dk:>7}{dk1:>8}"
              f"{mp.nstr(ratio, 6):>13}{mp.nstr(ceil, 6):>11}{mp.nstr(margin, 5):>10}"
              f"  {'falls ✓' if ratio < ceil else 'RISES ✗'}   ({el:.0f}s)")

    if len(rows) >= 2:
        print(f"\n  TREND at fixed k={k}→{k + 1}:")
        print(f"    |tr| ratio :  " + "  →  ".join(mp.nstr(r[2], 6) for r in rows))
        print(f"    ceiling    :  " + "  →  ".join(mp.nstr(r[3], 6) for r in rows))
        print(f"    margin     :  " + "  →  ".join(mp.nstr(r[4], 5) for r in rows))
        gr = [rows[i + 1][2] / rows[i][2] for i in range(len(rows) - 1)]
        print(f"    trace-ratio growth per A step: "
              + ", ".join(f"×{mp.nstr(g, 4)}" for g in gr))
        print(f"\n  The ceiling is bounded above by [3]_q = {mp.nstr(qint(3, q), 8)} at ANY k and")
        print(f"  falls toward q² = {mp.nstr(q ** 2, 6)} at fixed k as n grows. A trace ratio")
        print(f"  growing while the ceiling falls is the two sides moving apart, not a near miss.")
        print(f"\n  NOT an asymptotic claim: {len(rows)} sizes. Read it as a rate to test, not a limit.")


if __name__ == "__main__":
    main()
