#!/usr/bin/env python3
"""Which q-deformation of the classical Plancherel measure is normalised BY AN IDENTITY?

Bean `qou-oots`. After the R1/R2/R3 requirement derivation, two weight families
survive for the depth-stratified functional Phi_k:

    (A)  d_q^2 / D^2,   D^2 = SUM_mu d_q(mu)^2            (Reshetikhin-Turaev / Verlinde)
    (B)  f^lam * q^{-kappa_lam} * d_q(lam) / [n]_q!        (Molien / fake-degree)

The requirements do not separate them: R2 asks only that the normaliser be
n-INDEPENDENT, and both satisfy that (A trivially, being 1 by construction; B by
`molienSum_eq_qFactorial`). So the choice was left open. This probe asks a
question the requirements do not: which of the two is a q-deformation of the
CLASSICAL Plancherel measure that PRESERVES the identity making it a measure?

The classical Plancherel measure on partitions of n is

    P(lam) = (f^lam)^2 / n!,

a probability measure exactly because of Burnside/RSK: SUM_lam (f^lam)^2 = n!.
Deforming it means replacing n! -> [n]_q! and deforming the numerator, and the
question is which numerator keeps the sum equal to 1 as an IDENTITY.

TWO TESTS, and the second is the sharp one.

T1 asks the concrete question: of the three numerators actually present in this
corpus -- (f^lam)^2, f^lam*q^{-kappa}*d_q, and d_q^2 -- which one, over [n]_q!,
sums to 1? No invented family, just the three objects that exist.

T2 asks whether the kappa EXPONENT is forced. Take the one-parameter family

    w_c(lam) = f^lam * q^{c*kappa_lam} * d_q(lam) / [n]_q!,   c in Z

and ask for which c the sum is 1. MEASURED, c in [-3,3]: exactly TWO work,
c = -1 and c = +1. I predicted one, and the second is not noise -- it is the
conjugation symmetry, verified here over all partitions of n <= 9:

    f^{lam'} = f^lam,   hooks(lam') = hooks(lam) as multisets,   kappa' = -kappa

so lam -> lam' is a bijection carrying the c = +1 summand to the c = -1 summand
term by term. The two are the same measure read on transposed diagrams. This is
the SAME rows-vs-columns duality that qou-j7ef had to invoke to use
Feray-Meliot's q < 1 theorems at the substrate's q > 1, arriving here from a
completely different direction.

So the honest statement is: the exponent is forced UP TO CONJUGATION -- 2 of the
7 tested exponents, with the residual twofold ambiguity being a known and
harmless symmetry, not a free parameter. That is weaker than "unique" and
stronger than "a convention": no exponent other than +-1 makes the object a
measure at all. It is the arithmetic counterpart of the qou-j7ef bridge, where
the same exponent is forced by the Q = q^2 substitution instead.

TWO TRAPS, both mine, both caught by running the probe instead of asserting its
conclusion. The second is above (I predicted a unique exponent and there are
two). The first: the original T1 used the family (f^lam)^a * d_q(lam)^b / [n]_q! with a+b=2 and
and predicted (1,1) would be the normalised member. It is NOT: at n=6 and q=7/5 it
sums to 159430525780859375/348703783477344009, about 0.457. The reason is that
I had dropped the q^{-kappa} factor -- `molienSum_eq_qFactorial` is
SUM f^lam * q^{-kappa_lam} * d_q(lam) = [n]_q!, and kappa is load-bearing, not
decoration. A "Molien weight" written without it is a different object and is
not normalised.

WHY THIS IS THE RIGHT QUESTION, and its limits. It is NOT a fourth requirement --
nothing in R1-R3 forces a family to be normalised by an identity rather than by
division. What it separates is *how* each family earns its normalisation: (B) by
a theorem (Lean, sorry-free, all n, all q>1), (A) by dividing by whatever makes
the sum 1. Both are legitimate measures; only one is a deformation that a
structure theorem hands you. Reported as a discriminator on grounding, and it is
recorded below as EVIDENCE FOR a recommendation, never as a derivation of one.

The Tits-deformation remark that motivates the shape: at generic q,
H_n(q) is isomorphic to C[S_n], so the Wedderburn BLOCK DIMENSION of the block
indexed by lam is the classical f^lam, not d_q(lam). A Plancherel-type measure
weights a block by (block dimension) x (trace-theoretic dimension). The (1,1)
form puts a classical dimension in the block slot and a quantum one in the trace
slot; the (0,2) form puts a quantum dimension in BOTH. This probe does not prove
that reading -- it tests the arithmetic consequence of it.

Exact rational arithmetic at a rational q, so each "= 1" below is an identity at
the tested point rather than an agreement to a tolerance; plus an mpmath pass at
the substrate q0 to confirm nothing depends on the sample point. No float64
anywhere (AGENTS.md NO-FLOAT64 binds probes).
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from fractions import Fraction  # noqa: E402

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

# Reuse the partition/hook machinery already verified by the bridge probe rather
# than re-implementing it -- a second implementation is a second chance to get
# the hook lengths wrong, and this probe's whole content is a sum over them.
from molien_feray_meliot_bridge_probe import (  # noqa: E402
    partitions, hooks, f_lambda, bal_int, molien_weight, content_sum, conjugate,
)


def q_factorial(q, n: int):
    out = 1
    for k in range(1, n + 1):
        out = out * bal_int(q, k)
    return out


def dim_q(q, lam):
    """d_q(lam) = [n]_q! / prod_x [h(x)]_q  (q-hook-length formula)."""
    den = 1
    for h in hooks(lam):
        den = den * bal_int(q, h)
    return q_factorial(q, sum(lam)) / den


def main() -> int:
    set_compute_dps()
    bl = WitnessBuilder("plancherel-deformation-uniqueness")
    bl.set_description(
        "Bean qou-oots. Asks which q-deformation of the classical Plancherel "
        "measure (f^lam)^2/n! is normalised BY AN IDENTITY rather than by "
        "division. Of the three numerators present in this corpus, only "
        "f^lam*q^{-kappa}*d_q sums to 1 over [n]_q! -- and the kappa exponent "
        "is FORCED UP TO CONJUGATION: over c in [-3,3], exactly c = -1 and "
        "c = +1 make f^lam*q^{c*kappa}*d_q a measure, and those two are one "
        "measure read on transposed diagrams (conjugation fixes f^lam and the "
        "hook multiset and negates kappa -- verified over all partitions of "
        "n<=9), which is the same rows-vs-columns duality qou-j7ef needed. No "
        "other exponent normalises at all. Independent arithmetic confirmation "
        "of the qou-j7ef result that the Q = q^2 substitution forces the same "
        "exponent. That weight is the Molien/fake-degree family "
        "and, by that bridge, the literature's q-Plancherel measure M_{n,Q}. "
        "The historical d_q^2/[n]_q! form is NOT normalised, and the surviving "
        "alternative d_q^2/D^2 is that same numerator rescaled by whatever "
        "makes the sum 1. "
        "THIS IS A DISCRIMINATOR ON GROUNDING, NOT A DERIVED REQUIREMENT: "
        "nothing in the R1-R3 requirement set forces a family to be normalised "
        "by a theorem rather than by division, and both survivors are "
        "legitimate probability measures. Recorded as evidence for a "
        "recommendation, not as a proof of one."
    )
    bl.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    bl.add_parameter("family", "w_c(lam) = f^lam * q^{c*kappa_lam} * d_q(lam) / [n]_q!")

    # -- T1: the three numerators that actually exist in the corpus ----------
    q_rat = Fraction(7, 5)
    CANDIDATES = {
        "classical_f_squared": lambda q, lam: Fraction(f_lambda(lam)) ** 2,
        "molien_f_qkappa_dimq": lambda q, lam: (
            Fraction(f_lambda(lam)) * q ** (-content_sum(lam)) * dim_q(q, lam)),
        "historical_dimq_squared": lambda q, lam: dim_q(q, lam) ** 2,
    }
    table, normalised = {}, {}
    for name, num in CANDIDATES.items():
        row, ok = {}, True
        for n in range(1, 9):
            s = sum((num(q_rat, lam) / q_factorial(q_rat, n)
                     for lam in partitions(n)), Fraction(0))
            row[str(n)] = str(s)
            if s != 1:
                ok = False
        table[name], normalised[name] = row, ok
    bl.add_data("T1_exact_sums_at_q_7_over_5", {
        "note": "Exact Fraction arithmetic; each entry is SUM_lam numerator/[n]_q! "
                "at that n. A value of exactly 1 is an identity at this q, not an "
                "agreement to a tolerance.",
        "sums": table,
    })
    only_molien = (normalised["molien_f_qkappa_dimq"]
                   and not normalised["classical_f_squared"]
                   and not normalised["historical_dimq_squared"])
    bl.add_assertion(
        "molien_is_the_unique_normalised_candidate",
        computed="1" if only_molien else "0", expected="1",
        source="Of the three numerators present in the corpus, ONLY "
               "f^lam*q^{-kappa}*d_q sums to exactly 1 over [n]_q! at every "
               "n=1..8 in exact rational arithmetic at q=7/5. (f^lam)^2 gives "
               "n!/[n]_q!; d_q^2 is the historical unnormalised form.",
    )

    # -- T1b: the kappa exponent is FORCED -----------------------------------
    # The sharp test: only c = -1 makes f^lam * q^{c kappa} * d_q a measure.
    cfam, good_c = {}, []
    for c in range(-3, 4):
        ok = True
        row = {}
        for n in range(1, 8):
            s = sum((Fraction(f_lambda(lam)) * q_rat ** (c * content_sum(lam))
                     * dim_q(q_rat, lam) / q_factorial(q_rat, n)
                     for lam in partitions(n)), Fraction(0))
            row[str(n)] = str(s)
            if s != 1:
                ok = False
        cfam[str(c)] = row
        if ok:
            good_c.append(c)
    bl.add_data("T1b_kappa_exponent_family", {
        "note": "w_c(lam) = f^lam * q^{c*kappa_lam} * d_q(lam) / [n]_q!, exact "
                "rational arithmetic at q=7/5, n=1..7. Only the c whose whole row "
                "is 1 gives a probability measure.",
        "normalising_exponents": good_c,
        "sums": cfam,
    })
    # The two survivors are the SAME measure on transposed diagrams. Verified
    # rather than asserted: conjugation fixes f^lam and the hook multiset and
    # negates kappa, so it carries the c=+1 summand to the c=-1 summand.
    conj_ok = all(
        f_lambda(conjugate(lam)) == f_lambda(lam)
        and sorted(hooks(conjugate(lam))) == sorted(hooks(lam))
        and content_sum(conjugate(lam)) == -content_sum(lam)
        for n in range(1, 10) for lam in partitions(n)
    )
    bl.add_data("T1b_why_two_survive", {
        "conjugation_invariances_hold": conj_ok,
        "explanation": "f^{lam'} = f^lam, hooks(lam') = hooks(lam) as multisets, "
                       "and kappa(lam') = -kappa(lam) -- all verified over every "
                       "partition of n <= 9. So lam -> lam' is a bijection "
                       "carrying the c=+1 summand to the c=-1 summand term by "
                       "term: the two normalising exponents are one measure read "
                       "on transposed diagrams, the same rows-vs-columns duality "
                       "qou-j7ef needed to use Feray-Meliot's q<1 theorems at the "
                       "substrate's q>1.",
    })
    bl.add_assertion(
        "kappa_exponent_is_forced_up_to_conjugation",
        computed="1" if (good_c == [-1, 1] and conj_ok) else "0", expected="1",
        source=f"Over c in [-3,3], the exponents making f^lam*q^{{c*kappa}}*d_q a "
               f"measure are exactly {good_c} -- and those two are the same "
               f"measure on transposed diagrams (conjugation invariances verified "
               f"over all partitions of n<=9). So q^{{-kappa}} is forced up to a "
               f"known symmetry, not chosen: no other exponent normalises at all. "
               f"NOTE I predicted a unique exponent; the measurement says two, and "
               f"the second is the rows-vs-columns duality arriving from a "
               f"different direction than in qou-j7ef.",
    )

    # -- T2: (1,1) is not an artifact of the sample q ------------------------
    # A single rational q could in principle be special. Re-run at the substrate
    # q0 in mpmath, and at a second, unrelated rational.
    q_rat2 = Fraction(13, 4)
    second_q_ok = all(
        sum((Fraction(f_lambda(lam)) * q_rat2 ** (-content_sum(lam))
             * dim_q(q_rat2, lam) / q_factorial(q_rat2, n)
             for lam in partitions(n)), Fraction(0)) == 1
        for n in range(1, 9)
    )
    q0 = mp.mpf(Q_50_DIGIT_STR)
    tol = mp.mpf(10) ** (-40)
    q0_sums = {}
    q0_ok = True
    for n in (3, 6, 9, 12):
        s = mp.fsum(molien_weight(q0, lam) for lam in partitions(n))
        q0_sums[str(n)] = fmt(s)
        if abs(s - 1) > tol:
            q0_ok = False
    bl.add_data("T2_independence_of_sample_point", {
        "second_rational_q": str(q_rat2),
        "molien_sums_to_one_at_second_q": second_q_ok,
        "molien_sums_at_substrate_q0": q0_sums,
    })
    bl.add_assertion(
        "normalisation_is_not_a_sample_point_artifact",
        computed="1" if (second_q_ok and q0_ok) else "0", expected="1",
        source="(1,1) sums to exactly 1 at a second unrelated rational q=13/4 "
               "(n=1..8) and to 1 within 1e-40 at the substrate q0 (n=3,6,9,12)",
    )

    # -- T3: how far the OTHER two are from being measures -------------------
    # Reported so the result is a magnitude, not just a boolean. The (0,2) row
    # is the number the corpus already carries; the (2,0) row is new here.
    dev = {}
    for n in (3, 6, 9, 12):
        s02 = mp.fsum(
            (mp.mpf(f_lambda(lam)) ** 0) * dim_q(q0, lam) ** 2 / q_factorial(q0, n)
            for lam in partitions(n))
        s20 = mp.fsum(
            mp.mpf(f_lambda(lam)) ** 2 / q_factorial(q0, n) for lam in partitions(n))
        dev[str(n)] = {"sum_a0_b2_dimq_squared": fmt(s02),
                       "sum_a2_b0_classical": fmt(s20)}
    bl.add_data("T3_how_far_the_others_are", {
        "note": "At the substrate q0. The (0,2) column is the historical "
                "d_q^2/[n]_q! form and reproduces the figures already recorded "
                "in the corpus; the (2,0) column is n!/[n]_q!, which decreases "
                "in n where (0,2) increases -- they fail in OPPOSITE "
                "directions, so no single rescaling repairs both.",
        "per_n": dev,
    })

    bl.save()
    print(f"T1 Molien uniquely normalised among the 3 corpus numerators: {only_molien}")
    for k, v in table.items():
        print(f"   n=6  {k:26s} = {v['6']}")
    print(f"T1b kappa exponents giving a measure (c in [-3,3]): {good_c}"
          f"  [conjugation-equivalent: {conj_ok}]")
    print(f"T2 holds at a second rational q and at q0: {second_q_ok and q0_ok}")
    for n, v in dev.items():
        print(f"T3 n={n:>2}  (0,2)={v['sum_a0_b2_dimq_squared'][:8]}  "
              f"(2,0)={v['sum_a2_b0_classical'][:8]}")
    return 0 if (only_molien and good_c == [-1, 1] and conj_ok
                 and second_q_ok and q0_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
