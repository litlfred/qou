#!/usr/bin/env python3
"""magnus_sector_trace_monotone_probe.py — is the SECTOR trace the object that decays? (qou-o6ov)

THE REFRAMING BEING TESTED. The ≤2-row irrep traces do not decay in `k` for the true element — the
step `k=3→4` fails at A=3, 4 and 5, and worse with A. But those traces are **differences**. By
`U_q(sl₂)` Schur-Weyl the k-up-spin sector decomposes as `W_k = ⊕_{j≤k} S^{(n−j,j)}`, so

    tr_{W_k}(g)  =  Σ_{j≤k} tr_{(n−j,j)}(g)          and          tr_{(n−k,k)} = tr_{W_k} − tr_{W_{k−1}}

A difference of two decaying sequences need not decay, and the corpus already named this as the
obstruction — the bean records *"a decay BOUND for two-rows must respect the difference structure —
a per-sector triangle inequality does not decay in k."* This probe asks the question from the other
side: **does the sector trace itself decay, per sector dimension?**

    |tr_{W_k}| / dim W_k        with        dim W_k = C(n, k)

If it does while the irrep column does not, then the non-monotonicity the arc has been chasing is an
artifact of taking differences, and the natural object to bound is the sector, not the irrep. That
would turn a run of negatives into a positive direction — and unlike the y-weighting route, it is not
proposing a new mechanism, it is testing one the corpus already identified.

WHY IT IS ALMOST FREE. The sector traces are PARTIAL SUMS of the irrep traces, so no new sweep is
needed beyond the column itself: one pass over `k` gives both. `dim W_k = C(n,k)` is a binomial, not
a hook-length computation.

SIGNS ARE LOAD-BEARING HERE, unlike everywhere else in this arc. The partial sum needs the SIGNED
`tr_{(n−j,j)}`, and those alternate for the true element (A=4: `− + − − + +` across k=1…6) while the
bare element's are essentially all one sign. So this probe cannot be run off `|tr|` data, and the
bare/true comparison is not cosmetic — under ρ_bare the partial sums barely cancel at all.

HAND-COMPUTED PRELIMINARY, to be confirmed or refuted by this run. From the merged A=2/3/4 column
and sign data, `|tr_{W_k}|/C(n,k)` looks monotone decreasing at A=3 and A=4 and NOT at A=2
(rising at `k=2→3`). If that survives, the honest statement is "decays for A ≥ 3", which is a
weaker and more suspicious claim than "decays" — a property that starts holding at the third size
is exactly the shape of a small-size artifact, and this session has already been burned once by
reading a short column as a mechanism.

SCOPE — (a) scope-limited. NO-FLOAT64: mpf end to end, dps 65, `_assert_dps` guard inherited,
no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys
from math import comb

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_true_hecke_element_probe import sweep  # noqa: E402
import magnus_true_hecke_element_probe as TE  # noqa: E402


def shape(n, k):
    return (n - k,) if k == 0 else (n - k, k)


def verdict(name, vals):
    """Report WHERE it breaks; a bare False hides which k is anomalous."""
    bad = [(i + 1, vals[i], vals[i + 1]) for i in range(len(vals) - 1) if vals[i + 1] > vals[i]]
    if not bad:
        return f"    {name}: strictly decreasing ✓"
    out = [f"    {name}: NOT decreasing — {len(bad)} rise(s) ✗"]
    for k, lo, hi in bad:
        out.append(f"        k={k}:  {mp.nstr(lo, 7)} → {mp.nstr(hi, 7)}"
                   f"  (×{mp.nstr(hi / lo, 4) if lo > 0 else '∞'})")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3, 4])
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps
    TE._WANT_DPS = args.dps
    q = base.Q0

    print("[sector] tr_{W_k} = Σ_{j≤k} tr_{(n−j,j)}  (U_q(sl₂) Schur-Weyl), dim W_k = C(n,k).")
    print("[sector] The irrep traces are DIFFERENCES of these. Does the sector trace decay where")
    print(f"[sector] the difference does not?  (dps={args.dps})")

    for A in args.A:
        n = 3 * A
        Z, N = A // 2, A - A // 2
        word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
        ngen = max(g for _c, _d, g in word) + 1
        print(f"\n{'=' * 82}\n  A={A} (n={n})\n")
        print(f"  {'k':>3}  {'λ':<11}{'dim_λ':>7}{'signed tr_λ TRUE':>20}"
              f"{'tr_W_k':>16}{'C(n,k)':>9}{'|tr_W|/C':>13}")

        for elt in ("true", "bare"):
            running = mp.mpf(0)
            ratios, sects = [], []
            if elt == "bare":
                print(f"\n  --- ρ_bare, same table")
            for k in range(n // 2 + 1):
                lam = shape(n, k)
                tr, _f, dim = sweep(lam, word, q, ngen, true_coeffs=(elt == "true"))
                running += tr
                c = comb(n, k)
                r = abs(running) / c
                sects.append(running)
                ratios.append(r)
                if elt == "true":
                    print(f"  {k:>3}  {str(lam):<11}{dim:>7}{mp.nstr(tr, 9):>20}"
                          f"{mp.nstr(running, 9):>16}{c:>9}{mp.nstr(r, 7):>13}")
                else:
                    print(f"  {k:>3}  {str(lam):<11}{dim:>7}{mp.nstr(tr, 9):>20}"
                          f"{mp.nstr(running, 9):>16}{c:>9}{mp.nstr(r, 7):>13}")
            # k=0 is the trivial rep: Ω₂ vanishes there identically (#6387, Lean sorry-free), so
            # tr_W_0 = 0 and the ratio is 0. That is a proved zero, not a data point about decay —
            # monotonicity is asked from k=1, exactly as for the irrep column.
            print(f"\n  MONOTONICITY from k=1  (k=0 is the proved trivial-rep zero, #6387):")
            print(verdict(f"|tr_W_k|/C(n,k)  ρ_{elt}", ratios[1:]))

    print(f"\n{'=' * 82}")
    print("  If the sector ratio decays where the irrep column does not, the arc's")
    print("  non-monotonicity is a difference artifact and the sector is the object to bound.")
    print("  A property that only starts holding at the third size is NOT that — it is the shape")
    print("  of a small-size artifact, and this arc has already been burned by one.")


if __name__ == "__main__":
    main()
