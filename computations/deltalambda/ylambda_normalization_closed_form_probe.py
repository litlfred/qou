#!/usr/bin/env python3
"""ylambda_normalization_closed_form_probe.py — Z has a closed form, and it forces sign(Z)=+1.

THE HOLE THIS CLOSES.  `YLambdaSignThreshold` (#4662) proved
`sign(s_λ) = (−1)^{P(λ)}` for the Wenzl principal specialisation.  But the Jones–Markov weight
is `y_λ = s_λ / Z`, so that determined `sign(y_λ)` only **up to the single global sign of `Z`
per n**.  #4662 verified `sign(Z) = +1` numerically for n = 2..12 and explicitly declined to
claim it derived — the honest residual hole.

THE CLOSED FORM.  `Z = Σ_{λ⊢n} f^λ · s_λ` is the normalisation enforcing
`Σ_λ y_λ f^λ = tr_M(1) = 1`.  The classical Schur-basis expansion of the first power sum,

    Σ_{λ ⊢ n} f^λ s_λ  =  p₁ⁿ                      (Macdonald I.7; Stanley EC2 §7)

applies verbatim, because the Wenzl weight IS the principal specialisation
`s_λ(1, Q, …, Q^{r−1})`.  There `p₁ = 1 + Q + ⋯ + Q^{r−1} = (1 − Q^r)/(1 − Q)`, so

    Z = ((1 − Q^r)/(1 − Q))ⁿ

WHY THE SIGN IS THEN FORCED.  For `Q > 1` and `Q^r > 1` (at q₀: Q ≈ 1.232, Q^r ≈ 1.720), the
numerator `1 − Q^r` and denominator `1 − Q` are **both negative**, so their ratio is positive
and `Z` is a positive base to a natural power.  `sign(Z) = +1` for every n.

This is not visible term-by-term: the summands `f^λ s_λ` have **mixed signs** — that is exactly
the content of #4662 — so positivity comes from the closed form, never from the sum.

GATES (fail loudly):
  * the closed form must match the direct sum `Σ_λ f^λ s_λ` to < 1e-30 relative, every n;
  * the summands must genuinely be mixed-sign **for n ≥ 4** (otherwise the "not
    term-by-term" claim is empty).  n = 2, 3 are all-positive and must be: a negative
    weight needs a deep cell, a deep cell needs ≥ 4 rows, and the first partition with 4
    rows is (1,1,1,1) ⊢ 4.  So the ONSET of mixed signs at exactly n = 4 is an independent
    confirmation of `YLambdaSignThreshold.shallow_of_no_deep_cells`, and the probe checks
    that onset rather than demanding mixed signs everywhere.
  * both `1 − Q^r` and `1 − Q` must actually be negative at q₀ — the mechanism, checked
    rather than assumed.

Anchor: EXPERIMENTAL (proton) per AGENTS.md §"q₀ anchor convention".
Nothing fitted, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from schur_principal_mpmath import (  # noqa: E402
    schur_principal_mpmath, _f_lambda, partitions_of, _wenzl_constants,
)
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(50)
q0 = mp.mpf(str(Q0))
N_MIN, N_MAX = 2, 12
TOL = mp.mpf("1e-30")


def main() -> int:
    Q, QR = _wenzl_constants(q0)
    num, den = 1 - QR, 1 - Q
    p1 = num / den

    print("=" * 84)
    print(" Z has a closed form — and it forces sign(Z) = +1")
    print("=" * 84)
    print(f" q₀ = {mp.nstr(q0, 15)}   (EXPERIMENTAL / proton anchor)")
    print(f" Q  = q₀² = {mp.nstr(Q, 15)}      Q^r = {mp.nstr(QR, 15)}")
    print(f"\n THE MECHANISM — a cancellation of two sign flips:")
    print(f"   1 − Q^r = {mp.nstr(num, 12):>16}   negative? {num < 0}")
    print(f"   1 − Q   = {mp.nstr(den, 12):>16}   negative? {den < 0}")
    print(f"   p₁ = ratio = {mp.nstr(p1, 15)}   positive? {p1 > 0}")
    mech_ok = (num < 0) and (den < 0) and (p1 > 0)

    print(f"\n{'n':>3} {'Z (direct sum Σ f^λ s_λ)':>28} {'p₁ⁿ (closed form)':>26}"
          f" {'rel diff':>11} {'mixed signs':>12}")
    print("-" * 84)
    rows, form_ok, mixed_ok, onset_ok = [], True, True, True
    for n in range(N_MIN, N_MAX + 1):
        shapes = partitions_of(n)
        terms = [schur_principal_mpmath(sh, q0) * _f_lambda(sh) for sh in shapes]
        Z = sum(terms)
        cf = p1 ** n
        rel = abs(Z - cf) / abs(cf)
        n_neg = sum(1 for t in terms if t < 0)
        mixed = 0 < n_neg < len(terms)
        form_ok = form_ok and rel < TOL
        # Mixed signs are EXPECTED from n = 4 on, and expected ABSENT at n = 2, 3:
        # a negative weight needs a deep cell, which needs >= 4 rows.
        if n >= 4:
            mixed_ok = mixed_ok and mixed
        else:
            onset_ok = onset_ok and (n_neg == 0)
        print(f"{n:>3} {mp.nstr(Z, 18):>28} {mp.nstr(cf, 18):>26} {mp.nstr(rel, 4):>11}"
              f" {n_neg:>5}/{len(terms):<6}")
        rows.append({"n": n, "Z_direct": mp.nstr(Z, 30), "Z_closed_form": mp.nstr(cf, 30),
                     "rel_diff": mp.nstr(rel, 10), "n_negative_summands": n_neg,
                     "n_summands": len(terms), "mixed_sign": bool(mixed),
                     "Z_positive": bool(Z > 0)})

    all_pos = all(r["Z_positive"] for r in rows)
    # the >=4-row structural check: at n=4 the sole negative must be (1,1,1,1)
    n4 = [sh for sh in partitions_of(4)
          if schur_principal_mpmath(sh, q0) * _f_lambda(sh) < 0]
    onset_ok = onset_ok and n4 == [(1, 1, 1, 1)]
    print(f"\n onset check — first n with a negative summand is n = 4, and there the")
    print(f"   sole negative is {n4}  (expected [(1, 1, 1, 1)]: the first partition with")
    print(f"   4 rows, hence the first with a deep cell)  -> {'OK' if onset_ok else 'FAIL'}")
    ok = form_ok and mixed_ok and mech_ok and all_pos and onset_ok

    print("\n" + "=" * 84)
    if ok:
        print(" RESULT: Z = ((1 − Q^r)/(1 − Q))ⁿ, exact to < 1e-30 for every n = 2..12.")
        print("   Both 1 − Q^r and 1 − Q are negative, so the base is positive and")
        print("   sign(Z) = +1 for ALL n — derived, not merely observed.")
        print("")
        print("   The summands are genuinely MIXED-SIGN for n ≥ 4 (counts above), so this")
        print("   positivity is NOT term-by-term: it comes from the closed form alone.")
        print("   And the ONSET is exactly n = 4, where (1,1,1,1) becomes the first")
        print("   partition with 4 rows — an independent confirmation of the ≥4-row")
        print("   criterion of shallow_of_no_deep_cells.")
        print("")
        print("   => closes the residual hole in #4662:")
        print("      sign(y_λ) = sign(s_λ)/sign(Z) = (−1)^{P(λ)}, UNCONDITIONALLY.")
    else:
        print(" RESULT: FAILED — see the gate columns above.")
        if not form_ok:
            print("   the closed form does NOT match the direct sum")
        if not mixed_ok:
            print("   summands are not mixed-sign for n >= 4 — the 'not term-by-term' "
                  "claim is empty")
        if not onset_ok:
            print("   the mixed-sign ONSET is not at n=4 / not (1,1,1,1) — the >=4-row "
                  "criterion of shallow_of_no_deep_cells does not hold as stated")
        if not mech_ok:
            print("   the two-negatives mechanism does not hold at this q₀")
    print("=" * 84)

    w = WitnessBuilder("ylambda-normalization-closed-form", engine="mpmath",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("closed_form_matches_direct_sum", 1 if form_ok else 0, 1)
    w.add_assertion("summands_mixed_sign_for_n_ge_4", 1 if mixed_ok else 0, 1)
    w.add_assertion("mixed_sign_onset_at_n4_is_1111", 1 if onset_ok else 0, 1)
    w.add_assertion("sign_Z_positive_all_n", 1 if all_pos else 0, 1)
    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("q0_anchor", "experimental/proton")
    w.add_parameter("Q", mp.nstr(Q, 30))
    w.add_parameter("QR", mp.nstr(QR, 30))
    w.add_parameter("p1", mp.nstr(p1, 30))
    w.add_data("by_n", rows)
    w.add_caveat(
        "The identity sum_lambda f^lambda s_lambda = p_1^n is a CLASSICAL theorem of "
        "symmetric-function theory (Macdonald I.7; Stanley EC2 section 7), cited rather than "
        "re-proved. This probe verifies it numerically at the substrate specialisation; the "
        "Lean file YLambdaNormalizationSign.lean carries it as an explicit hypothesis (hZ) "
        "and proves the sign consequence sorry-free. The premise is established literature, "
        "NOT a conjecture."
    )
    w.set_description(
        "Verifies Z = ((1-Q^r)/(1-Q))^n, the principal specialisation of the classical "
        "sum_lambda f^lambda s_lambda = p_1^n, to <1e-30 for n=2..12. Since Q>1 and Q^r>1 "
        "make both 1-Q^r and 1-Q negative, the base is positive and sign(Z)=+1 for all n -- "
        "closing the residual global-sign hole left by #4662 and making "
        "sign(y_lambda) = (-1)^{P(lambda)} unconditional. Gated additionally on the summands "
        "being genuinely mixed-sign for n>=4, so the 'positivity is not term-by-term' claim "
        "is not vacuous -- and on the ONSET being exactly n=4 with sole negative (1,1,1,1), "
        "an independent confirmation of the >=4-row criterion of shallow_of_no_deep_cells "
        "(a negative weight needs a deep cell, a deep cell needs 4 rows)."
    )
    w.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
