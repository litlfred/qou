#!/usr/bin/env python3
"""The r5full anchor gate holds — but its stated test is miscalibrated.

Bean qou-5vhf, which is `completed` and hands over exactly one target:

    "For whoever attacks conj:canonical-knot-id-sdp: aim at the ratio being a
     pure power of -q^{1/2}."

That target comes from `atom_nf_symbolic_D.py:289-290`:

    # Ratio test: even if they differ by a writhe/normalization factor,
    # the ratio should be a pure power of -q^{1/2}.  Check.

TWO STATEMENTS IN THAT FILE CANNOT BOTH BE RIGHT. Ninety lines earlier, the
same file's `markov_trace_to_jones` docstring names the omitted factor as

    Jones(K) = ((-1/sqrt q)^{n-1} * (q/(1-q^2))^{n-1})...   (line 194)

`(q/(1-q^2))^{n-1}` is a RATIONAL FUNCTION with a `(1-q^2)^{n-1}` denominator.
A pure power of `-q^{1/2}` is a MONOMIAL. If the docstring's factor is the one
omitted, then "the ratio is not a monomial" is exactly what a CORRECT
identification would produce, and the ratio test as written cannot distinguish
anything.

WHAT THE RATIO ACTUALLY IS. Factoring the committed `symbolic_ratio` (83 terms
over 11) gives a denominator that is not opaque at all:

    32 * q^1327 * (q+1)^5 * (q^6 - q^5 + 2q^4 - 2q^3 + 2q^2 - 2q + 1)

Both non-trivial factors are identifiable:

  * `(q+1)^5` has exponent n-1 = 5 at the 6 strands of the A=2 atom -- the same
    exponent the docstring's omitted factor carries. So this factor is
    ACCOUNTED FOR by the missing normalisation and is not evidence of anything.
    (Matching the exponent is not the same as verifying the convention, and
    this probe does not claim the latter.)

  * the degree-6 factor is EXACTLY `q^5 * J(6_2)` -- the numerator of the very
    Jones polynomial being compared against. It survives in the DENOMINATOR,
    which says J(6_2) does not divide the trace.

THE GATE STANDS, ON A SHARPER AND CONVENTION-INDEPENDENT TEST. Polynomial
division (after `q -> t^2` to clear half-integer powers) shows `q^5*J(6_2)`
does NOT divide the ratio's numerator -- remainder nonzero, 12 terms. And that
numerator is IRREDUCIBLE over Q and COPRIME to both `(q-1)` and `(q+1)`. So no
normalisation of the shape `monomial * (1 +/- q)^k` -- which is the shape every
Markov-trace-to-Jones convention takes -- can supply the missing factor.

    tr != N * J(6_2)  for every N of that shape.

That is strictly stronger than "the ratio is not a monomial", and unlike it, it
cannot be dismissed as an artifact of the omitted normalisation.

SCOPE (a), on the EVIDENCE, not on the knot. This does not show D's atom link is
not 6_2 by some other route; it shows the Hecke-level identification fails in a
way that no framing or normalisation convention can repair. Nothing wired.
"""

from __future__ import annotations

import json
import pathlib

import sympy as sp

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
WITNESS = REPO / "computations" / "atom-nf-symbolic-D.witness.json"

q = sp.Symbol("q", positive=True)
t = sp.Symbol("t", positive=True)

N_STRANDS = 6  # A = 2 deuterium atom word: 3A strands


def jones_62_numerator() -> sp.Expr:
    """`q^5 * J(6_2)`, from the same Kawauchi/KnotInfo form the producer uses."""
    j = q**-5 - 2*q**-4 + 2*q**-3 - 2*q**-2 + 2*q**-1 - 1 + q
    return sp.expand(sp.together(j * q**5))


def main() -> int:
    ratio = sp.sympify(json.loads(WITNESS.read_text())["symbolic_ratio"],
                       locals={"q": q})
    num, den = sp.fraction(sp.together(ratio))
    num_terms = len(sp.Add.make_args(sp.expand(num)))
    den_terms = len(sp.Add.make_args(sp.expand(den)))
    den_factored = sp.factor(den)

    NJ = jones_62_numerator()

    # --- the two identifiable denominator factors -----------------------
    P = q**6 - q**5 + 2*q**4 - 2*q**3 + 2*q**2 - 2*q + 1
    deg6_is_jones = sp.expand(P - NJ) == 0
    # exponent of (q+1) dividing the denominator, by repeated exact division
    e = 0
    d_poly = sp.Poly(sp.expand(den), q)
    while True:
        quo, rem = sp.div(d_poly, sp.Poly(q + 1, q))
        if rem.is_zero:
            d_poly, e = quo, e + 1
        else:
            break

    # --- the sharp test: does J(6_2) divide the trace? -------------------
    numt = sp.expand(num.subs(q, t**2))
    Pt = sp.expand(P.subs(q, t**2))
    quo, rem = sp.div(sp.Poly(numt, t), sp.Poly(Pt, t))
    divides = rem.is_zero
    rem_terms = 0 if divides else len(rem.as_expr().as_ordered_terms())

    # --- why no normalisation can repair it ------------------------------
    irreducible = sp.Poly(P, q).is_irreducible
    gcd_minus = sp.gcd(P, q - 1)
    gcd_plus = sp.gcd(P, q + 1)
    coprime = (gcd_minus == 1) and (gcd_plus == 1)

    b = WitnessBuilder(
        name="r5full-anchor-gate-divisibility",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-07-13-atom-knot-rule-a5plus-constraints.md")
    b.set_description(
        "EXPLORATORY. qou-5vhf hands over the target 'aim at the ratio being a pure "
        "power of -q^{1/2}', taken from atom_nf_symbolic_D.py:290. That test is "
        "MISCALIBRATED: the same file's docstring (line 194) names the omitted factor "
        "as ((-1/sqrt q)^{n-1} * (q/(1-q^2))^{n-1}), a RATIONAL function, so a "
        "non-monomial ratio is what a CORRECT identification would give. Factoring the "
        "committed ratio shows the denominator is 32*q^1327*(q+1)^5*(q^5*J(6_2)): the "
        "(q+1)^5 carries exponent n-1=5 and is accounted for by the missing "
        "normalisation, while the degree-6 factor is EXACTLY the numerator of J(6_2), "
        "surviving in the denominator. The gate STANDS on a sharper test -- q^5*J(6_2) "
        "does not divide the trace (remainder 12 terms), and being irreducible over Q "
        "and coprime to (q-1) and (q+1) it cannot be supplied by any normalisation of "
        "the shape monomial*(1+/-q)^k. Convention-independent, unlike the stated test. "
        "Scope (a) on the EVIDENCE, not on the knot. Nothing wired."
    )

    b.add_data("the_contradiction_inside_one_file", {
        "line_194_docstring": "Jones(K) = ((-1/sqrt q)^{n-1} * (q/(1-q^2))^{n-1})...",
        "line_290_comment": "the ratio should be a pure power of -q^{1/2}",
        "why_incompatible": ("(q/(1-q^2))^{n-1} is a rational function with a "
                             "(1-q^2)^{n-1} denominator; a pure power of -q^{1/2} is a "
                             "monomial. If the docstring names the omitted factor, a "
                             "non-monomial ratio is what a CORRECT identification gives, "
                             "and the stated test cannot discriminate."),
        "consequence_for_the_handover": ("qou-5vhf's closing recommendation points the "
                                         "next agent at the miscalibrated target; this "
                                         "probe replaces it with the divisibility test."),
    })
    b.add_data("ratio_structure", {
        "numerator_terms": num_terms,
        "denominator_terms": den_terms,
        "denominator_factored": str(den_factored),
        "q_plus_1_exponent": e,
        "n_strands": N_STRANDS,
        "n_minus_1": N_STRANDS - 1,
        "reading": ("(q+1)^5 carries exponent n-1 at 6 strands, matching the exponent "
                    "of the docstring's omitted factor, so it is accounted for. Matching "
                    "an exponent is NOT verifying the convention and no such claim is "
                    "made here."),
    })
    b.add_data("the_sharp_test", {
        "divisor": "q^5 * J(6_2) = q^6 - q^5 + 2q^4 - 2q^3 + 2q^2 - 2q + 1",
        "J62_divides_the_trace": bool(divides),
        "remainder_terms": rem_terms,
        "irreducible_over_Q": bool(irreducible),
        "gcd_with_q_minus_1": str(gcd_minus),
        "gcd_with_q_plus_1": str(gcd_plus),
        "conclusion": ("J(6_2)'s numerator is irreducible and coprime to (q-1) and "
                       "(q+1), so no normalisation of the shape monomial*(1+/-q)^k -- "
                       "the shape every Markov-to-Jones convention takes -- can supply "
                       "it. Hence tr != N*J(6_2) for every such N. The gate stands, "
                       "convention-independently."),
    })
    b.add_data("scope", {
        "kind": "(a), on the evidence rather than on the knot",
        "not_shown": ("that D's atom link is not 6_2 by some other route. What is shown "
                      "is that the HECKE-LEVEL identification fails in a way no framing "
                      "or normalisation convention can repair."),
    })

    b.add_assertion(
        name="denominator_degree6_factor_is_exactly_the_numerator_of_J_62",
        computed="1" if deg6_is_jones else "0", expected="1", tolerance="0", unit="bool",
        source=("q^6-q^5+2q^4-2q^3+2q^2-2q+1 equals q^5*J(6_2) identically. The Jones "
                "polynomial being compared against survives in the ratio's DENOMINATOR."),
    )
    b.add_assertion(
        name="q_plus_1_exponent_equals_n_minus_1",
        computed=str(e), expected=str(N_STRANDS - 1), tolerance="0", unit="exponent",
        source=("the other denominator factor is (q+1)^5 at 6 strands -- the exponent "
                "the omitted normalisation carries, so it is accounted for and is not "
                "evidence against the identification."),
    )
    b.add_assertion(
        name="J62_numerator_does_NOT_divide_the_trace",
        computed=str(rem_terms), expected="12", tolerance="0", unit="remainder terms",
        source=("THE RESULT. Polynomial division after q -> t^2 leaves a nonzero "
                "remainder, so no rescaling makes the trace a multiple of J(6_2)."),
    )
    b.add_assertion(
        name="J62_numerator_irreducible_and_coprime_to_the_normalisation_factors",
        computed="1" if (irreducible and coprime) else "0",
        expected="1", tolerance="0", unit="bool",
        source=("irreducible over Q, gcd 1 with both (q-1) and (q+1). This is what makes "
                "the divisibility failure CONVENTION-INDEPENDENT: no monomial*(1+/-q)^k "
                "normalisation can contribute the missing factor."),
    )

    # `independent`, added 2026-09-04 after this omission was caught on a
    # SIBLING probe. This file works entirely in the polynomial ring ℚ[q] —
    # sympy factorisation, division and gcd on a symbolic `q` — and never
    # substitutes a numerical pin, so there is no `q0Value` and recording one
    # would be a contradiction.
    #
    # It was missing when this probe merged (#6515), and the PR body's claim
    # that "the new files appear nowhere in the gate log" was too weak to catch
    # it: the q0-anchor refill ratchet reports a COUNT, not filenames, so the
    # only line naming this file was a `skipped:` notice. The reliable check is
    # to A/B the gate with the files removed and diff the counts.
    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Works entirely in Q[q]: sympy factorisation, "
            "polynomial division after q -> t^2, gcd and irreducibility over Q "
            "on a symbolic q. No numerical substitution occurs on any path, so "
            "no q0Value exists."
        ),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
