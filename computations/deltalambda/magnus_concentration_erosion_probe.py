#!/usr/bin/env python3
"""magnus_concentration_erosion_probe.py — what is eating the k=1 share? (qou-o6ov)

WHERE THIS SITS. Everything monotone in this arc has now failed for the true Hecke element: the
≤2-row irrep column decays at **0 of 4** sizes, the sector reframing at **2 of 4** (refuted at the
largest size), and the y-weighted mass fails at A=4. What survives is **concentration, not
monotonicity** — the `k=1` reflection term still carries most of the mass:

    k=1 share of Σ|c_λ|, ρ_true:   77.882 % (A=2)  →  73.499 % (A=3)  →  59.437 % (A=4)

That is eroding, and accelerating: −4.4 points then −14.1. Since concentration is the only surviving
support for the truncation heuristic AND for the reflection-rep sign conjecture (which holds at
A=2,3,4 but whose margin is flat while this share falls), whether it erodes toward a floor or toward
zero is the question the arc now turns on.

THE HYPOTHESIS THIS TESTS, and it links the two surviving findings. Part 1 of
`2026-09-05-magnus-the-sector-trace-decays-where-the-irrep-does-not.md` measures the step `k=3→4`
diverging — raw trace ratio growing ~4.6× per A step against a ceiling falling toward `q²`. If that
same `k=4` term is what eats the `k=1` share, the erosion is not a separate phenomenon: it is the
divergence, seen through the mass rather than through the ratio.

Read off the committed A=3/A=4 outputs by hand, `|c₄|/|c₁|` runs 0.0453 → 0.3184 while `k=1` drops
14.1 points and `k=4` gains ~15.6 — which would make `k=4` essentially the whole story. This probe
computes the per-`k` share table so that is machine-produced rather than arithmetic in a chat
message, and so the *next* A can be added without re-deriving it.

WHAT IT REPORTS. For each A: every `|c_λ|` share, which `k` gained the most share since the previous
A, and the `|c_k|/|c_1|` ratio per `k`. The last is the one that separates "k=1 is shrinking" from
"some other term is growing" — different claims with the same symptom.

SCOPE — (a) scope-limited, cheap sizes only. A=5's column costs hours and is not attempted here; the
A=2..4 trend is three points and a three-point trend is a trend to test, not a law. This arc has
already had one three-point pattern (the sector reframing) refuted by its fourth size.
NO-FLOAT64: mpf end to end, dps 65, `_assert_dps` guard inherited, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from magnus_true_hecke_element_probe import sweep  # noqa: E402
import magnus_true_hecke_element_probe as TE  # noqa: E402


def shape(n, k):
    return (n - k,) if k == 0 else (n - k, k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3, 4])
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps
    TE._WANT_DPS = args.dps
    q = base.Q0

    print("[erosion] Concentration is what survives; it is eroding. Which k is eating the k=1 share?")
    print(f"[erosion] |c_λ| = y_λ·|tr_λ(ρΩ₂^P)|, ρ = the TRUE Hecke element.  (dps={args.dps})")

    prev = None
    for A in args.A:
        n = 3 * A
        Z, N = A // 2, A - A // 2
        word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
        ngen = max(g for _c, _d, g in word) + 1
        yl = y_lambda_at(n, q)
        mp.mp.dps = args.dps        # y_lambda_at resets dps internally (#6710 trap, measured)

        cs = []
        for k in range(n // 2 + 1):
            lam = shape(n, k)
            tr, _f, _d = sweep(lam, word, q, ngen, true_coeffs=True)
            y = yl.get(lam)
            y = abs(mp.mpf(str(y))) if y is not None else mp.mpf(0)
            cs.append(y * abs(tr))
        tot = sum(cs)
        shares = [100 * c / tot if tot > 0 else mp.mpf(0) for c in cs]

        print(f"\n  A={A} (n={n})   Σ|c_λ| = {mp.nstr(tot, 8)}")
        print(f"    {'k':>3}{'share %':>11}{'|c_k|/|c_1|':>14}{'Δ share vs prev A':>20}")
        for k in range(len(cs)):
            rel = cs[k] / cs[1] if len(cs) > 1 and cs[1] > 0 else mp.mpf(0)
            d = ""
            if prev is not None:
                # A k beyond the previous column's length is NEW — the column grows by one shape
                # every two A. Its previous share is 0, not undefined, so its Δ is its whole share.
                # Leaving it blank (the first version of this probe) makes the "biggest gainer"
                # metric structurally blind to an ARRIVING term, which inverted the conclusion:
                # it reported k=2 as the A=2→3 gainer (+1.779) while the newly-arrived k=4 took
                # +3.330, i.e. 76 % of the 4.383 points k=1 lost.
                dv = shares[k] - (prev[k] if k < len(prev) else mp.mpf(0))
                # mp.nstr already carries a '-'; add '+' by hand. A '+' in a STRING format spec is
                # a ValueError, not a no-op.
                d = ("+" if dv >= 0 else "") + mp.nstr(dv, 4)
            print(f"    {k:>3}{mp.nstr(shares[k], 6):>11}{mp.nstr(rel, 6):>14}{d:>20}")

        if prev is not None:
            # Range over the CURRENT column, not the overlap, so arriving k are candidates.
            gains = [(shares[k] - (prev[k] if k < len(prev) else mp.mpf(0)), k)
                     for k in range(len(shares))]
            g = max(gains)
            new = " (NEW this A)" if g[1] >= len(prev) else ""
            print(f"    biggest share GAIN since previous A: k={g[1]}  "
                  f"({mp.nstr(g[0], 4)} points){new}")
            print(f"    k=1 change: {mp.nstr(shares[1] - prev[1], 4)} points")
            if shares[1] < prev[1]:
                frac = 100 * g[0] / (prev[1] - shares[1])
                print(f"    that gainer covers {mp.nstr(frac, 5)} % of what k=1 lost")
        prev = shares

    print("\n  If the biggest gainer is k=4 at every step, the erosion IS the k=3→4 divergence")
    print("  (Part 1), seen through the mass rather than the ratio — one phenomenon, not two.")
    print("  Read |c_k|/|c_1| as well as the share: a falling k=1 share and a rising other-term")
    print("  ratio are the same symptom of different claims.")


if __name__ == "__main__":
    main()
