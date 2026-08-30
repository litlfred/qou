#!/usr/bin/env python3
"""jet_filtration_hypothesis_fails_probe.py

*** RETRACTED 2026-08-30, same session, by the author of the claim. ***

The conditional this probe states does NOT fire, because its antecedent is
false. I flagged the identification `mu_n == a_D^(n) * w_n` as unestablished
and said settling it was the next step. Settled: it is WRONG.

`bk-coordination-multiplicity.md` DOES state the multiplicity, in the section I
had not read when I wrote this: `M_n(A)` is the **per-nucleon coordination
number z = A - 1**, read off AME2020 as `M_need = B_AME/(m_e Vol_A)` and matched
for the non-magic A=3 pair (2.003 for 3H, 2.061 for 3He against z = 2) to better
than 3% with no free parameter. It is NOT `C(A,n)`.

So the jet-filtration decomposition is not the binomial one, the measured
alternation of `mu_5` and `mu_7` says nothing about `a_D^(n)`, and the
extensivity hypothesis is NOT shown to be violated. My grep missed it because I
searched for `binom{A}{n}` / `C(A,n)` / `n-subsets` -- the block writes `C(A,2)`
for the total bond count and `z = A-1` for the multiplicity, so none of my
patterns could hit.

WHAT SURVIVES, and it is only the measurement, not the inference:
  - the binomial-basis coefficients mu_k are exactly as tabulated below, and
    their sign pattern (+,+,+,-,+,-) is convention-invariant over all 27 mirror
    conventions. That is a fact about the binomial decomposition and stays true.
  - QOU.Mass.JetFiltrationSignObstruction stays valid: it is stated in `_of_`
    form over abstract `aD`/`w`, so it proves what it proves (w >= 0 is
    structural; a negative term forces a negative aD). It simply has no
    instance here.

Original text follows, unchanged, for the record.

ORIGINAL:

The jet-filtration extensivity proposition is proved, and its hypothesis is
false in the data -- conditional on one identification I have NOT established.

WHY THIS EXISTS
---------------
`content/.../mass-theory/jet-filtration-binding-extensive.md` proves that

    B(A) = sum_{n=2}^{A} m_e * a_D^(n) * w_n

is monotone non-decreasing in the cutoff A, GIVEN m_e >= 0, a_D^(n) >= 0 and
w_n >= 0 for every body order n. It is cited as supplying the extensivity that
the intensive rotation-phase reading structurally lacked. The proof is correct
and is not in question.

This probe asks the question AGENTS.md's "conditional-proved != premise-
established" rule exists for: is the HYPOTHESIS true?

MEASURED -- exact rationals from the vendored AME2020 table, no float anywhere.
The standard binomial-basis body-order decomposition B(A) = sum_k mu_k C(A,k)
is triangular, so it solves exactly, A = 2..7:

    mu_2 =    +2.22457      mu_5 =   -55.77912   *** NEGATIVE
    mu_3 =    +1.42622      mu_6 =  +166.12507
    mu_4 =    +9.24338      mu_7 =  -373.24295   *** NEGATIVE

and the sign pattern (+,+,+,-,+,-) is IDENTICAL across ALL 27 mirror-convention
combinations (A=3 3H/3He, A=5 5He/5Li, A=7 7Li/7Be; A=4 and A=6 are N=Z
self-conjugate). The alternation is not a convention artifact.

WHICH HALF OF THE HYPOTHESIS CAN FAIL -- and it is not w_n
-----------------------------------------------------------
`bk-coordination-multiplicity.md` defines w_n(K) = M_n(A) * Vol_n(K): a
coordination MULTIPLICITY times a HYPERBOLIC VOLUME. A count is non-negative; a
volume is non-negative (zero on non-hyperbolic components, as the conjecture
itself notes). So `w_n >= 0` is STRUCTURAL -- it cannot be the failing half.

The hypothesis therefore reduces to `a_D^(n) >= 0`, and any sign alternation in
the product is carried by a_D alone. Proved sorry-free in
`QOU.Mass.JetFiltrationSignObstruction`: `wOf_nonneg` (structural), and
`aD_neg_of_term_neg` (a negative term forces a negative a_D given w >= 0).

THE ONE THING I HAVE NOT ESTABLISHED -- stated plainly because it is the whole
weight of the claim
-------------------------------------------------------------------------------
That `mu_n` IS `a_D^(n) * w_n`. It is the natural reading of "the n-body term"
-- the binomial basis is the standard many-body/cluster decomposition, and
B_n(K) = C(A,n) * (n-body energy) makes w_n's multiplicity M_n(A) the C(A,n).
But the corpus does not state that identification, and I searched for it
(`grep` for binom{A}{n} / C(A,n) / n-subsets across mass-theory: no hit).

So the honest form is CONDITIONAL, and the Lean is stated in the repo's `_of_`
style to match: IF the physical body-order decomposition is the binomial one,
THEN the jet-filtration hypothesis is false at n = 5 and n = 7, and the
extensivity proposition -- though correctly proved -- is VACUOUS for the
physical case. Establishing or refuting that identification is a cheap,
well-posed next step and it is the only thing between this and a refutation.

CORROBORATION, not proof: `QOU.MassTheory.MayerThreeBodySign` already found the
connected 3-body Ursell cumulant "wrong-signed against AME2020", threshold-
forced and independent of the bond set. Sign trouble in this expansion has
precedent in the corpus.

SCOPE
-----
Scope-(a). Nothing is refuted -- the proposition stands as proved, and the
identification is unestablished. What is measured is that the hypothesis's
`a_D >= 0` half is in tension with the data under the natural reading.

NO FLOAT64: exact `fractions.Fraction` throughout; AME from the vendored table.
"""

import itertools
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.codata_constants import ame_binding_mev as B  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def R(Z, A):
    return F(str(B(Z, A)))


def body_order_coeffs(Bs):
    """Solve B(A) = sum_k mu_k C(A,k) triangularly. Exact."""
    mu = {}
    for A in range(2, 8):
        mu[A] = Bs[A] - sum(mu[k] * comb(A, k) for k in mu)
    return mu


def main():
    wb = WitnessBuilder("jet-filtration-hypothesis-fails", engine="python-exact")
    wb.set_description(
        "jet-filtration-binding-extensive proves extensivity GIVEN a_D^(n) >= 0 "
        "and w_n >= 0. Measured exactly: the binomial-basis body-order "
        "coefficients alternate, mu_5 = -55.779 and mu_7 = -373.243, with the "
        "sign pattern (+,+,+,-,+,-) identical across all 27 mirror conventions. "
        "w_n = M_n(A)*Vol_n(K) is a count times a volume, so w_n >= 0 is "
        "STRUCTURAL and cannot be the failing half; the alternation is carried "
        "by a_D alone. CONDITIONAL on identifying mu_n with a_D^(n)*w_n, which "
        "the corpus does not state and this probe does not establish: the "
        "hypothesis is false at n=5,7 and the proposition is vacuous for the "
        "physical case. Scope-(a)."
    )

    D, He4, Li6 = R(1, 2), R(2, 4), R(3, 6)
    m3 = [R(2, 3), (R(1, 3) + R(2, 3)) / 2, R(1, 3)]
    m5 = [R(3, 5), (R(3, 5) + R(2, 5)) / 2, R(2, 5)]
    m7 = [R(4, 7), (R(3, 7) + R(4, 7)) / 2, R(3, 7)]

    patterns, central = {}, None
    for a, b, c in itertools.product(m3, m5, m7):
        mu = body_order_coeffs({2: D, 3: a, 4: He4, 5: b, 6: Li6, 7: c})
        sg = tuple("+" if mu[k] > 0 else "-" for k in range(2, 8))
        patterns[sg] = patterns.get(sg, 0) + 1
        if (a, b, c) == (m3[1], m5[1], m7[1]):
            central = mu

    ok = True
    print("body-order coefficients mu_k, B(A) = sum_k mu_k C(A,k), EXACT")
    for k in range(2, 8):
        flag = "  *** NEGATIVE" if central[k] < 0 else ""
        print(f"   mu_{k} = {float(central[k]):>14.5f}{flag}")
    print(f"\nsign patterns over 27 mirror conventions: {len(patterns)} -> "
          f"{list(patterns)}")

    wb.add_data("body_order_coefficients_exact",
                {str(k): str(central[k]) for k in range(2, 8)})
    wb.add_data("sign_patterns", {str(k): v for k, v in patterns.items()})

    wb.add_assertion(
        name="sign_pattern_is_convention_invariant",
        computed=str(len(patterns)), expected="1", tolerance="0",
        unit="distinct sign patterns over 27 mirror conventions",
        source="all 27 give (+,+,+,-,+,-); the alternation is not a convention artifact")
    if len(patterns) != 1:
        ok = False
        print("   FAIL: sign pattern not invariant")

    negs = [k for k in range(2, 8) if central[k] < 0]
    wb.add_assertion(
        name="two_body_orders_are_negative",
        computed=str(negs), expected="[5, 7]", tolerance="0",
        unit="body orders with negative coefficient",
        source=("mu_5 = -55.77912, mu_7 = -373.24295; the jet-filtration "
                "extensivity hypothesis requires every term >= 0"))
    if negs != [5, 7]:
        ok = False
        print(f"   FAIL: negative orders {negs}, expected [5, 7]")

    wb.add_data("which_half_fails", {
        "w_n": ("STRUCTURAL non-negative: bk-coordination-multiplicity defines "
                "w_n(K) = M_n(A) * Vol_n(K), a coordination multiplicity times "
                "a hyperbolic volume. Cannot be the failing half."),
        "a_D": ("carries the whole alternation, by "
                "QOU.Mass.JetFiltrationSignObstruction.aD_neg_of_term_neg"),
    })
    wb.add_data("the_unestablished_identification", {
        "assumption": "mu_n == a_D^(n) * w_n",
        "why_natural": ("the binomial basis is the standard many-body/cluster "
                        "decomposition; B_n(K) = C(A,n)*(n-body energy) makes "
                        "w_n's multiplicity M_n(A) the C(A,n)"),
        "searched_for_it": ("grep for binom{A}{n} / C(A,n) / n-subsets across "
                            "content/.../mass-theory/: NO HIT. The corpus does "
                            "not state the identification"),
        "consequence": ("everything here is conditional on it; establishing or "
                        "refuting it is the cheap, well-posed next step and the "
                        "only thing between this and a refutation"),
    })
    wb.add_data("corroboration_not_proof", {
        "MayerThreeBodySign": ("already found the connected 3-body Ursell "
                               "cumulant wrong-signed against AME2020, "
                               "threshold-forced, independent of the bond set")})

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
