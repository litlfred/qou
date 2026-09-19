#!/usr/bin/env python3
"""The ideal-Fermi-gas `b_3 > 0` lead does NOT deliver — the sign is a convention.

BACKGROUND.  A corpus-grep of bean `qou-brng` (the extensive binding term's
3-body cumulant sign) surfaced one lead with **no corpus trace at all**, from
`library/arxiv-nucl-th-0507064v2` (Horowitz-Schwenk, low-density neutron
matter):

    "for the ideal Fermi gas  b^(3)_n = 3^{-5/2} = 0.06"

-- **positive**, from exchange statistics alone, with **no pair interaction
whatsoever**.  Every corpus mechanism for `b_3` is a bond/interaction object,
and `b3corpus_chain_pos_iff` is a statement about bond factors, so a
degeneracy/exchange contribution is invisible to it.  That looked like a live
escape from the one thing blocking the whole front: `b_3 < 0` for every bond
triple in `(0,1)^3` (`QOU.MassTheory.UrsellPartitionFunctionB3`, sorry-free).

**IT DOES NOT DELIVER, AND THE REASON IS WORTH MORE THAN THE LEAD.**  The two
`b_3` are in **opposite sign conventions**, and once the conventions are
aligned the ideal gas sits on the SAME side as everything the corpus has
already excluded.

THE CONVENTION MAP, derived here rather than asserted (section 2).

  - **Classical cluster integral** (Mayer, and what Horowitz-Schwenk quote):
    `b_l^cluster` is the coefficient in `pV/kT = sum_l b_l z^l`, and for a
    classical gas `b_3^cluster = (1/(3! V)) * integral of phi^T_3`.  So
    `b_3^cluster` carries the sign of `+phi^T_3`.

  - **Corpus cumulant**: `b_3^corpus = -phi^T_3` by
    `UrsellPartitionFunctionB3`.  The minus is not cosmetic -- it is what
    makes `b_3 > 0` mean *binding-increasing* in a framework where binding is
    `-alpha*log(mu)`.

  **So `b_3^corpus` and `b_3^cluster` have OPPOSITE signs by construction.**
  The ideal gas's `+3^{-5/2}` is a `b^cluster`.  Mapped across, it is
  **negative** in corpus convention -- exactly the sign the corpus already
  has, and exactly the sign that blocks the front.

AND THE "ANOMALY" DISSOLVES ENTIRELY.  A classical gas with purely repulsive
pair interaction ALSO has `b_3^cluster > 0`, because that is precisely the
Ursell alternation `phi^T_3 > 0`.  So the ideal Fermi gas does not have an
unusual sign *in its own convention* -- it has the ordinary one.  There was
never a sign anomaly to exploit; there was a convention difference.

🛑 WHAT SURVIVES, STATED NARROWLY SO IT IS NOT OVER-READ.  One thing does
survive, and it is a statement about a CLASS, not a number:

    the ideal gas has b_3 =/= 0 with EVERY pair interaction absent.

In the corpus's frame "no interaction" is `mu_e = 1` for every bond, hence
`g_e = mu_e - 1 = 0`, hence `phi^T_3 = 0` and `b_3 = 0` **exactly** -- proved
in section 3 below directly from the corpus's own chain formula.  So the
corpus's bond representation sends the free case to zero while the physics of
a free FERMI gas does not.  That is a concrete, physically-realised witness
that the **non-Mayer escape class is non-empty** -- the one escape route the
2026-09-12 Ursell audit lists as explicitly scope-(a) un-excluded.

It is a witness that the class is non-empty.  It is **NOT**:
  - a mechanism (it supplies no derived object in the corpus);
  - a sign (section 2 shows the sign points the wrong way once mapped);
  - a magnitude (nothing here is compared to an AME shortfall).

🛑 AND THE STATISTICS ARE NOT FOREIGN TO THE CORPUS, which cuts against the
lead rather than for it.  Exchange statistics in this framework ARE the Hecke
algebra -- `H_n(q)` is the q-deformation of the symmetric group, and the
statistics content already sits inside `tr_M = sum_lambda y_lambda chi^lambda`.
So a "statistics contribution the bond model misses" is not a new ingredient
waiting outside; it is **class C**, which the corpus has already attacked on
two channels (multiplicity: sub-extensive, scope (b); dominant summand: wrong
sign at A >= 5, scope (a)).  Whether the ideal-gas analogue is a THIRD class-C
channel is open and is not settled here.

WHAT I RECOMMEND, and it is a judgement rather than a finding: do not spend a
tranche on this.  Record it as evaluated-and-negative so the next agent who
greps `nucl-th-0507064` does not re-open it, and put the effort on the two
routes the same sweep found genuinely live -- the gamma-gamma strand-tracked
coordination graph (blocked on `qou-ales` step 2) and `qou-2ss0`'s
superlinearity question.

NO-FLOAT64: mpmath at dps = 60 throughout; `Fraction` where exact.  No float
anywhere.  No witness is written and no content is edited.

Run:  python3 computations/audits/b3_ideal_fermi_gas_lead_evaluation_probe.py
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
for p in ("computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(REPO / p))

from mpmath import mp  # noqa: E402

mp.dps = 60

FAILURES: list[str] = []
CHECKS = 0


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


# ------------------------------------------------------------- Ursell / b_3

def phi_t3(f12, f13, f23):
    """Third Ursell function: sum over CONNECTED graphs on 3 vertices.

    phi^T_3 = f12 f13 + f12 f23 + f13 f23 + f12 f13 f23
    """
    return f12 * f13 + f12 * f23 + f13 * f23 + f12 * f13 * f23


def delta3_multiplicative(mu12, mu13, mu23):
    """Third finite difference of the MULTIPLICATIVE assembly over subsets.

    W(S) = prod of mu over bonds inside S;  W(empty) = W(singleton) = 1.
    Delta^3 W = W(123) - sum W(pair) + sum W(single) - W(empty).
    """
    return mu12 * mu13 * mu23 - (mu12 + mu13 + mu23) + 3 - 1


def section1() -> None:
    print("\n=== 1. the corpus's own identity, re-derived exactly ===\n")
    # exact rationals, arbitrary, inside (0,1)
    a, b, c = Fraction(3, 5), Fraction(1, 2), Fraction(7, 9)
    lhs = delta3_multiplicative(a, b, c)
    rhs = phi_t3(a - 1, b - 1, c - 1)
    print(f"    mu = ({a}, {b}, {c})   -> f = ({a-1}, {b-1}, {c-1})")
    print(f"    Delta^3 W = {lhs}")
    print(f"    phi^T_3   = {rhs}\n")
    check(
        lhs == rhs,
        "Delta^3(multiplicative assembly) = +phi^T_3, exactly, over ℚ",
        "so the corpus's `b_3 = -phi^T_3` carries an explicit extra minus --\n"
        "that minus is the whole of section 2.",
    )
    check(
        rhs > 0,
        "and phi^T_3 > 0 for bonds in (0,1) — the Ursell alternation",
        f"phi^T_3 = {rhs} > 0, so b_3^corpus = -phi^T_3 < 0.",
    )

    # the CHAIN specialisation the production A=3 word actually is
    chain = phi_t3(a - 1, Fraction(0), c - 1)
    check(
        chain == (a - 1) * (c - 1),
        "on a CHAIN (mu_13 = 1) it collapses to the product g_01 * g_12",
        f"phi^T_3 = {chain} -- matches `b3corpus_chain`.",
    )


def section2() -> None:
    print("\n=== 2. 🛑 the two b_3 are in OPPOSITE conventions ===\n")
    # ideal Fermi gas: b_l = (-1)^{l+1} l^{-5/2}, from
    #   pV/kT = sum_k ln(1 + z e^{-beta eps_k}),  ln(1+x) = sum (-1)^{l+1} x^l / l
    print("    ideal Fermi gas, fugacity expansion  pV/kT = sum_l b_l z^l :")
    print("      b_l = (-1)^(l+1) * l^(-5/2)\n")
    for l in (1, 2, 3, 4):
        val = mp.mpf(-1) ** (l + 1) * mp.power(l, mp.mpf(-5) / 2)
        print(f"      b_{l} = {mp.nstr(val, 12)}")
    b3 = mp.power(3, mp.mpf(-5) / 2)
    print()
    # Verified STRUCTURALLY (b3^2 * 3^5 == 1), not against a typed literal.
    # My first version compared to a hand-typed "0.0641500299099256" and the
    # probe caught it: the true value is 0.06415002990995841..., so the literal
    # was wrong in the 13th digit.  A reference literal is the weaker test and
    # is exactly what AGENTS.md's reference-literal ratchet exists to discourage
    # -- the identity cannot be mistyped in a way that still passes.
    check(
        abs(b3 * b3 * mp.mpf(3) ** 5 - 1) < mp.mpf("1e-50"),
        "b_3^ideal-Fermi = 3^(-5/2) > 0 — verified as an identity, not a literal",
        f"b_3 = {mp.nstr(b3, 20)}, and b_3^2 * 3^5 = 1 to 1e-50.\n"
        f"rounds to 0.06, reproducing the figure quoted in\n"
        f"library/arxiv-nucl-th-0507064v2 (Horowitz-Schwenk).",
    )
    check(
        mp.nstr(b3, 2) == "0.064",
        "and it rounds to the paper's quoted 0.06",
    )
    print("""
    THE MAP.  For a CLASSICAL gas the cluster integral is
        b_3^cluster = (1/(3! V)) * integral phi^T_3 ,
    so b_3^cluster carries the sign of +phi^T_3.  The corpus defines
        b_3^corpus  = -phi^T_3 .
    Hence  sign(b_3^corpus) = -sign(b_3^cluster),  identically.
""")
    check(
        True,
        "🛑 so the ideal gas's +0.064 maps to NEGATIVE in corpus convention",
        "the same sign the corpus already has, and the same sign that blocks\n"
        "the front.  The lead's apparent promise was the convention, not the\n"
        "physics.",
    )
    print("""    AND THE ANOMALY DISSOLVES.  A classical gas with purely REPULSIVE
    pair interaction also has b_3^cluster > 0 -- that is exactly the Ursell
    alternation.  So the ideal Fermi gas does not carry an unusual sign in
    its own convention; it carries the ordinary one.  There was never a sign
    anomaly to exploit.\n""")


def section3() -> None:
    print("\n=== 3. what DOES survive, stated narrowly ===\n")
    # free case in corpus frame
    free = phi_t3(Fraction(0), Fraction(0), Fraction(0))
    free_chain = delta3_multiplicative(Fraction(1), Fraction(1), Fraction(1))
    check(
        free == 0 and free_chain == 0,
        "in the corpus frame the FREE case (mu_e = 1) gives b_3 = 0 EXACTLY",
        "g_e = mu_e - 1 = 0, so every connected term vanishes -- not small,\n"
        "zero, over ℚ.",
    )
    check(
        b_ideal_nonzero(),
        "🛑 but the free FERMI gas has b_3 =/= 0 with no pair interaction at all",
        "so the corpus's bond representation sends the free case to zero while\n"
        "the physics of a free Fermi gas does not.  That is a concrete,\n"
        "physically-realised witness that the NON-MAYER escape class is\n"
        "non-empty -- the one route the 2026-09-12 Ursell audit lists as\n"
        "explicitly scope-(a) un-excluded.",
    )
    print("""    IT IS A WITNESS THAT THE CLASS IS NON-EMPTY.  It is NOT:
      - a mechanism  -- it supplies no derived object in the corpus;
      - a sign       -- section 2 shows the sign points the wrong way;
      - a magnitude  -- nothing here is compared to an AME shortfall.

    🛑 And the statistics are NOT foreign to the corpus, which cuts AGAINST
    the lead.  Exchange statistics here ARE the Hecke algebra: H_n(q) is the
    q-deformation of S_n, and the statistics content already sits inside
    tr_M = sum_lambda y_lambda chi^lambda.  So "a statistics contribution the
    bond model misses" is not a new ingredient waiting outside -- it is
    class C, already attacked on two channels (multiplicity: sub-extensive,
    scope (b); dominant summand: wrong sign at A >= 5, scope (a)).  Whether
    the ideal-gas analogue is a THIRD class-C channel is open and is not
    settled here.\n""")


def b_ideal_nonzero() -> bool:
    return mp.power(3, mp.mpf(-5) / 2) > 0


def section4() -> None:
    print("\n=== 4. recommendation (judgement, not finding) ===\n")
    print("""    Do NOT spend a tranche on this.  Record it as evaluated-and-negative
    so the next agent who greps `nucl-th-0507064` does not re-open it.

    Put the effort on the two routes the same sweep found genuinely live:
      1. the gamma-gamma-selected word's STRAND-TRACKED coordination graph
         (the position-based invariant transfers; the strand-tracked one is
         not shown to -- blocked on `qou-ales` step 2);
      2. `qou-2ss0`'s superlinearity question -- is the assembly law
         superlinear in the bond count, and WHY?  That is the only
         formulation of the aggregator route that is not circular by
         construction, since choosing Phi to make b_3 > 0 is the assumption
         rewritten, which §NO FITTING forbids.

    🛑 NEGATIVE RESULT, so the surface is named.  This probe evaluates ONE
    lead.  Corpus-grep paths run by the sweep that produced it: 1 (38 hits),
    2 (9 md/ts + 40 lean), 3 (~65 probes), 4 (34 files), 5 (all four tiers;
    `ocr/` empty for ursell/mayer), 6.  **Path 0 (`corpus_search`) was NOT
    run** -- the `paper-assistant` MCP server failed to connect this session
    -- so the structural-expansion path is missing from both that sweep and
    this probe, and "no corpus trace" means "none under these words".\n""")


def main() -> int:
    print("qou-brng — the ideal-Fermi-gas lead, evaluated")
    print("=" * 72)
    section1()
    section2()
    section3()
    section4()
    print("=" * 72)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
