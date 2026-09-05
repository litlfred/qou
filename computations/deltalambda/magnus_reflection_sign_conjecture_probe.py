#!/usr/bin/env python3
"""magnus_reflection_sign_conjecture_probe.py — the sign conjecture, under D and the TRUE ρ. (qou-o6ov)

THE CONJECTURE, as `magnus_sign_row_truncation_probe.py` states it:

    "As A→∞, sign(P(A)) is determined by the reflection representation (n−1,1)."

with `P(A) = Σ_λ y_λ tr(ρ_λ Ω₂^P)`. Its recorded evidence is a sign margin `|P| / Σ_λ|c_λ|` of
**69 % (A=2) → 99 % (A=3) → 99.9 % (A=4)**, "GROWS with A".

WHY IT NEEDS RE-MEASURING, and both reasons are independent of each other:

1. **Those figures are convention C.** That probe's `y_λ` are the C values
   `(0.4153958, 0.2809296, 0.0227449)` against D's `(0.5054042, 0.2472979, 0)`. Under D the sum has
   only `⌊n/2⌋+1` terms — the ≥3-row shapes it was summing carry weight **zero**.
2. **They are for the WRONG ρ.** `atom_braid_word_3A` returns Hecke letters `c·σ_g + d·1`; the whole
   pre-#6822 arc extracted `[int(t[2]) for t in ...]` and applied a bare `σ_g`, wrong for 54 % of
   letters at A=3.

AND THE MARGIN HAS SHRUNK WHERE IT WAS MEASURED. Under D with the true element, `k=1` carries
**77.9 % / 73.5 / 59.4 %** of the *absolute* mass at A = 2/3/4 — falling with A, not growing
(#6822 + the ≤2-row column probe). A sign conjecture resting on one term's dominance is worth
re-testing when that dominance is measured to be eroding.

WHAT IS MEASURED HERE. The signed contributions `c_λ = y_λ · tr_λ(ρ Ω₂^P)` themselves, not their
moduli, so three separate things can be told apart:

  * `sign(P)`                     — the actual sign of the sum;
  * `sign(c_(n−1,1))`             — the reflection term's sign, which the conjecture says decides it;
  * margin `|P| / Σ_λ |c_λ|`      — how much cancellation there is, i.e. how close the sign is to
                                    flipping. A margin near 1 means the terms mostly agree in sign;
                                    near 0 means the sign is decided by a near-cancellation and is
                                    fragile.

The conjecture is CONFIRMED at a given A only if `sign(P) == sign(c_(n−1,1))`. A large margin is
supporting evidence, not the claim — and a *small* margin with agreeing signs is the interesting
case, because it means the conjecture holds for that A by luck rather than by dominance.

SCOPE — (a) scope-limited, A ≤ 4 at one q₀ unless more are passed. Measures; proves nothing, and a
handful of A is not an "as A→∞" statement either way.
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
from magnus_true_hecke_element_probe import sweep, classify  # noqa: E402
import magnus_true_hecke_element_probe as TE  # noqa: E402


def two_row_shapes(n):
    return [(n - k,) if k == 0 else (n - k, k) for k in range(n // 2 + 1)]


def run_one(A, q, dps):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
    ngen = max(g for _c, _d, g in word) + 1
    ns, ni, na = classify(word, q)
    yl = y_lambda_at(n, q)
    mp.mp.dps = dps                 # y_lambda_at resets dps internally (#6710 trap; measured)

    print(f"\n{'=' * 76}\n  A={A} (n={n}) — {len(word)} letters: σ {ns}, σ⁻¹ {ni}, averaged {na}"
          f"  ⇒ bare form wrong on {ni + na}")
    print(f"  {'k':>3}  {'λ':<12}{'y_λ':>13}{'c_λ  BARE':>17}{'c_λ  TRUE':>17}")

    out = {}
    for elt in ("bare", "true"):
        out[elt] = {"c": [], "shapes": []}
    for k, lam in enumerate(two_row_shapes(n)):
        tb, _f, dim = sweep(lam, word, q, ngen, true_coeffs=False)
        tt, _f2, _ = sweep(lam, word, q, ngen, true_coeffs=True)
        y = yl.get(lam)
        y = mp.mpf(str(y)) if y is not None else mp.mpf(0)
        cb_, ct_ = y * tb, y * tt
        out["bare"]["c"].append(cb_); out["true"]["c"].append(ct_)
        out["bare"]["shapes"].append(lam); out["true"]["shapes"].append(lam)
        print(f"  {k:>3}  {str(lam):<12}{mp.nstr(y, 6):>13}"
              f"{mp.nstr(cb_, 8):>17}{mp.nstr(ct_, 8):>17}")

    for elt in ("bare", "true"):
        cs = out[elt]["c"]
        P = sum(cs)
        abs_sum = sum(abs(x) for x in cs)
        refl = cs[1]                                    # k=1 is (n−1,1), the reflection rep
        margin = abs(P) / abs_sum if abs_sum > 0 else mp.mpf(0)
        agree = (P > 0) == (refl > 0) if P != 0 and refl != 0 else None
        print(f"\n  --- ρ_{elt}")
        print(f"    P(A)            = {mp.nstr(P, 10)}   sign {'+' if P > 0 else '−'}")
        print(f"    c_(n−1,1)       = {mp.nstr(refl, 10)}   sign {'+' if refl > 0 else '−'}")
        print(f"    Σ|c_λ|          = {mp.nstr(abs_sum, 10)}")
        print(f"    margin |P|/Σ|c| = {mp.nstr(100 * margin, 6)} %")
        print(f"    reflection-rep sign conjecture: "
              f"{'HOLDS ✓' if agree else 'FAILS ✗' if agree is False else 'undecided (a zero)'}")
        # A conjecture that holds while the reflection term is NOT the largest is holding by
        # cancellation among the others, not by dominance — worth separating explicitly.
        biggest = max(range(len(cs)), key=lambda i: abs(cs[i]))
        print(f"    largest |c_λ| is at k={biggest} "
              f"({'the reflection rep' if biggest == 1 else 'NOT the reflection rep'})"
              f", carrying {mp.nstr(100 * abs(cs[biggest]) / abs_sum, 5)} % of Σ|c|")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3, 4])
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps
    TE._WANT_DPS = args.dps
    q = base.Q0

    print("[signconj] 'sign(P(A)) is determined by the reflection rep (n−1,1)' — the recorded")
    print("[signconj] evidence (margin 69 → 99 → 99.9 %) is convention C AND the bare-σ ρ.")
    print(f"[signconj] Re-measured here under D and the true Hecke element.  (dps={args.dps})")
    for A in args.A:
        run_one(A, q, args.dps)
    print(f"\n{'=' * 76}")
    print("  Read sign-agreement and margin separately: agreement is the conjecture, the margin")
    print("  is how fragile that agreement is. A shrinking margin with holding signs is the")
    print("  configuration in which the conjecture fails first at some larger A.")


if __name__ == "__main__":
    main()
