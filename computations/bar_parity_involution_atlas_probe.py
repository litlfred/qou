#!/usr/bin/env python3
"""Which involution is each "bar-even / bar-odd" label computed against?

The corpus applies the words *bar-even* and *bar-odd* to four different
gradings.  PR #4802 read that as a four-way name collision.  It is not: three
of the four are aspects of a **single** involution, and the fourth is a swap.
This probe establishes the atlas exactly, so that keeping the names (the
author's call, 2026-08-08) is safe rather than merely tolerable.

The single involution is ``def:bar-involution`` on ``H_n(q)``:

    bar(sigma_i) = sigma_i^{-1},    bar(q) = q^{-1}

It has **two independently-applicable halves**, and the whole confusion is
that different corpus blocks silently apply different halves:

  * the **coefficient half** ``q -> q^{-1}``, diagram held fixed;
  * the **diagram half** ``sigma_i -> sigma_i^{-1}`` -- geometrically the
    mirror, exchanging positive and negative crossings ``p <-> m``
    (``def:bar-involution`` line 5: "reflecting the braid diagram").

The four gradings, and the half each is graded by:

  A. the Laurent scalar ``E_cross = p*q - m/q`` split as
     ``cosh L`` / ``sinh L``            -- graded by the COEFFICIENT half
  B. the Hecke module split ``e_+`` / ``e_-`` by eigenvalue ``q`` / ``-q^{-1}``
                                        -- FIXED by the full involution
  C. the knot mirror, ``E_sym`` / ``E_asym`` totals
                                        -- graded by the DIAGRAM half
  D. the spin involution ``A = A_+ (+) A_-`` on the sym/alt Hecke block
                                        -- graded by the COEFFICIENT half

So A and D agree (same half, same parity assignment, genuinely the same
grading); C is graded by the *other* half and comes out **anti-correlated**
with A on the channel totals; and B is not a parity grading at all -- the
full involution fixes both of its idempotents.

Two consequences the probe pins down:

  1. Under the **full** involution -- the one ``def:bar-involution`` actually
     defines -- *both* crossing-energy channels are ODD.  The words
     "bar-even/bar-odd" therefore separate the channels only when read
     against the coefficient half.  That is what the notation-register
     disambiguation must say.
  2. The apparent "double inversion" in the strangelet reading is not an
     error in either block: ``cosh L`` is coefficient-EVEN while its channel
     total ``E_sym = (p-m) cosh L`` is diagram-ODD, because the mirror flips
     the multiplicity too.  Both statements are true of the same summand.

Conventions
-----------
q_0 is the **experimental (proton) pin** per the 2026-08-07 owner directive:
``qou_substrate.constants.Q``.  No muon-built cache is read.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

DPS = 50


def parity(f, expr) -> str:
    """Classify ``expr`` as even / odd / neither under the involution ``f``."""
    if sp.simplify(f(expr) - expr) == 0:
        return "even"
    if sp.simplify(f(expr) + expr) == 0:
        return "odd"
    return "neither"


def main() -> int:
    wb = WitnessBuilder("bar-parity-involution-atlas", engine="python")
    wb.set_description(
        "The four corpus gradings labelled bar-even/bar-odd are aspects of "
        "one involution (def:bar-involution) applied by halves: A and D are "
        "graded by the coefficient half q -> 1/q, C by the diagram half "
        "(mirror), and B is swapped, not graded. Under the full involution "
        "both crossing-energy channels are odd."
    )
    wb.set_content_block("obs:crossing-energy-decomposition")

    q, p, m, k = sp.symbols("q p m k", positive=True)

    # --- The three involutions. ------------------------------------------
    # Coefficient half: q -> 1/q, diagram fixed.
    coef = lambda e: e.subs(q, 1 / q)  # noqa: E731
    # Diagram half (mirror): p <-> m, coefficients fixed.
    diag = lambda e: e.subs({p: m, m: p}, simultaneous=True)  # noqa: E731
    # The full bar involution of def:bar-involution: both halves.
    full = lambda e: coef(diag(e))  # noqa: E731

    checks: dict[str, bool] = {}

    # --- Grading A: the Laurent scalar and its two channels. -------------
    e_cross = p * q - m / q
    cosh_L = (q + 1 / q) / 2
    sinh_L = (q - 1 / q) / 2
    e_sym = (p - m) * cosh_L
    e_asym = (p + m) * sinh_L

    checks["split_reconstructs_e_cross"] = (
        sp.simplify(e_cross - (e_sym + e_asym)) == 0
    )

    # The parity atlas: every object against every involution.
    atlas = {}
    for name, expr in [
        ("cosh_L", cosh_L),
        ("sinh_L", sinh_L),
        ("E_sym", e_sym),
        ("E_asym", e_asym),
        ("E_cross", e_cross),
    ]:
        atlas[name] = {
            "coefficient_half": parity(coef, expr),
            "diagram_half_mirror": parity(diag, expr),
            "full_bar_involution": parity(full, expr),
        }

    # A's weights are graded by the coefficient half, as the names say.
    checks["A_cosh_is_coefficient_even"] = atlas["cosh_L"]["coefficient_half"] == "even"
    checks["A_sinh_is_coefficient_odd"] = atlas["sinh_L"]["coefficient_half"] == "odd"

    # C's channel TOTALS are graded by the diagram half -- and come out
    # anti-correlated with A: the cosh channel is mirror-ODD.
    checks["C_E_sym_is_mirror_odd"] = atlas["E_sym"]["diagram_half_mirror"] == "odd"
    checks["C_E_asym_is_mirror_even"] = atlas["E_asym"]["diagram_half_mirror"] == "even"
    checks["C_anticorrelates_with_A"] = (
        atlas["cosh_L"]["coefficient_half"] != atlas["E_sym"]["diagram_half_mirror"]
        and atlas["sinh_L"]["coefficient_half"]
        != atlas["E_asym"]["diagram_half_mirror"]
    )

    # THE CENTRAL RESULT: under the FULL involution both channels are odd,
    # so the words do not separate them there.
    checks["full_bar_makes_E_sym_odd"] = (
        atlas["E_sym"]["full_bar_involution"] == "odd"
    )
    checks["full_bar_makes_E_asym_odd"] = (
        atlas["E_asym"]["full_bar_involution"] == "odd"
    )
    checks["full_bar_does_not_separate_channels"] = (
        atlas["E_sym"]["full_bar_involution"]
        == atlas["E_asym"]["full_bar_involution"]
        == "odd"
    )
    checks["full_bar_negates_e_cross"] = sp.simplify(full(e_cross) + e_cross) == 0

    # --- Grading D: the spin involution on the sym/alt Hecke block. ------
    # electroweak-triplet-charge-spin-from-involution-proof.md:3 states the
    # spin involution acts on this block as the eigenvalue swap
    # q^{2k} <-> q^{-2k}, i.e. "precisely the bar involution".  Verify that
    # its sectors are the coefficient-half parity eigenspaces, hence the SAME
    # grading as A's weights.
    a_plus = (q ** (2 * k) + q ** (-2 * k)) / 2
    a_minus = (q ** (2 * k) - q ** (-2 * k)) / 2
    checks["D_swap_is_the_coefficient_half"] = (
        sp.simplify(coef(q ** (2 * k)) - q ** (-2 * k)) == 0
    )
    checks["D_A_plus_is_coefficient_even"] = parity(coef, a_plus) == "even"
    checks["D_A_minus_is_coefficient_odd"] = parity(coef, a_minus) == "odd"
    # ...and they are literally cosh / sinh at argument 2k*lambda.
    lam = sp.log(q)
    checks["D_A_plus_is_cosh"] = sp.simplify(a_plus - sp.cosh(2 * k * lam)) == 0
    checks["D_A_minus_is_sinh"] = sp.simplify(a_minus - sp.sinh(2 * k * lam)) == 0
    checks["A_and_D_are_the_same_grading"] = (
        checks["D_A_plus_is_coefficient_even"]
        and checks["D_A_minus_is_coefficient_odd"]
        and checks["A_cosh_is_coefficient_even"]
        and checks["A_sinh_is_coefficient_odd"]
    )

    # --- Grading B: the Hecke eigen-split is FIXED, not graded. ----------
    # Worked in the 2-dimensional seminormal block, sigma = diag(q, -1/q).
    # Applying the full involution to the *expressions* for the idempotents
    # (q -> 1/q AND sigma -> sigma^{-1}) leaves each one where it was.
    ident = sp.eye(2)
    sigma = sp.diag(q, -1 / q)
    sigma_inv = sigma.inv()
    b2 = q + 1 / q  # [2]_q, itself coefficient-even
    e_minus = sp.simplify((q * ident - sigma) / b2)
    e_plus = sp.simplify((sigma + ident / q) / b2)
    checks["B_idempotents_resolve_identity"] = (
        sp.simplify(e_plus + e_minus - ident) == sp.zeros(2, 2)
    )
    bar_e_minus = sp.simplify(((1 / q) * ident - sigma_inv) / coef(b2))
    bar_e_plus = sp.simplify((sigma_inv + ident * q) / coef(b2))
    checks["B_e_minus_is_bar_fixed"] = (
        sp.simplify(bar_e_minus - e_minus) == sp.zeros(2, 2)
    )
    checks["B_e_plus_is_bar_fixed"] = (
        sp.simplify(bar_e_plus - e_plus) == sp.zeros(2, 2)
    )
    # Hence the full involution does NOT exchange the two eigenchannels: it
    # fixes both, so both are "bar-even" and the words separate nothing here
    # either.  (This contradicts a corpus statement -- see the caveat.)
    checks["B_full_bar_does_not_exchange_channels"] = (
        checks["B_e_minus_is_bar_fixed"] and checks["B_e_plus_is_bar_fixed"]
    )
    # The coefficient half ALONE moves sigma's spectrum off itself, onto the
    # spectrum of sigma^{-1}: it does not act on the eigenchannels at all
    # without the diagram half.
    checks["B_coefficient_half_alone_leaves_the_spectrum"] = all(
        sp.simplify(coef(e) - e) != 0 for e in (q, -1 / q)
    )

    # --- Numerics at the experimental (proton) pin. ----------------------
    q0 = sp.Float(Q_50_DIGIT_STR, DPS)
    num = {
        "q_0": str(sp.N(q0, 30)),
        "cosh_lambda": str(sp.N(cosh_L.subs(q, q0), 30)),
        "sinh_lambda": str(sp.N(sinh_L.subs(q, q0), 30)),
    }

    all_pass = all(checks.values())

    wb.add_parameter("q_0_pin", "experimental/proton")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("dps", DPS)
    wb.add_data("checks", {k_: bool(v) for k_, v in checks.items()})
    wb.add_data("parity_atlas", atlas)
    wb.add_data("numerics_at_q0", num)
    wb.add_data(
        "involutions",
        {
            "coefficient_half": "q -> q^{-1}, diagram fixed",
            "diagram_half_mirror": "sigma_i -> sigma_i^{-1}, i.e. p <-> m",
            "full_bar_involution": (
                "def:bar-involution = both halves; bar(sigma_i)=sigma_i^{-1} "
                "and bar(q)=q^{-1}"
            ),
        },
    )
    wb.add_data(
        "grading_to_half",
        {
            "A_crossing_energy_weights": "coefficient half",
            "B_hecke_eigen_split": (
                "not a grading -- the full involution FIXES both e_+ and e_-"
            ),
            "C_knot_mirror_channel_totals": "diagram half",
            "D_spin_involution_sectors": "coefficient half",
        },
    )

    wb.add_assertion(
        "checks_failed", sum(1 for v in checks.values() if not v), 0,
        source="sympy exact",
    )
    wb.add_assertion(
        "n_channels_odd_under_full_bar",
        sum(
            1
            for c in ("E_sym", "E_asym")
            if atlas[c]["full_bar_involution"] == "odd"
        ),
        2,
        source="sympy exact",
    )
    # Was add_assertion(name, X, X) -- both slots the same literal, so `x == x`:
    # it renders as "passed": true beside real checks, which reads as machine-
    # verified. This is a DECLARATION the code cannot verify about itself, so it is
    # a parameter. The statement is unchanged; only the false badge is removed.
    # Bean qou-ploj (LITERAL class).
    # NOT converted to a real check: I could not establish from this file what the
    # "four gradings" are indexed over, and fabricating a count I do not understand
    # would be worse than recording the claim honestly. A real check is available to
    # someone who knows the intended indexing.
    wb.add_parameter(
        "n_distinct_involutions_behind_the_four_gradings",
        "1 (DECLARED, not counted. The source field read 'sympy exact; the halves are "
        "halves of def:bar-involution' -- but no count was performed here.)")

    wb.add_data(
        "interpretation",
        {
            "one_involution_two_halves": (
                "A, C and D are not three involutions. They are "
                "def:bar-involution applied by halves: A and D by the "
                "coefficient half q -> 1/q, C by the diagram half (mirror). "
                "B is the Hecke eigen-split, which the full involution "
                "fixes rather than grades."
            ),
            "the_words_separate_nothing_under_the_full_involution": (
                "Under def:bar-involution itself: both crossing-energy "
                "channels are odd, and both Hecke idempotents are fixed. So "
                "on every one of the four gradings the parity words fail to "
                "distinguish the two summands when read against the full "
                "involution. They distinguish them only against a named half."
            ),
            "why_the_names_are_safe_to_keep": (
                "A and D carry the SAME grading -- coefficient-half parity -- "
                "with the same assignment (cosh/A_+ even, sinh/A_- odd), so "
                "'bar-even/bar-odd' is consistent between them. The only "
                "cross-wiring is C, which grades the channel TOTALS by the "
                "other half and so anti-correlates."
            ),
            "the_full_involution_separates_nothing": (
                "Under def:bar-involution itself both channels are odd and "
                "E_cross is negated. So the parity words separate the "
                "channels only when read against the coefficient half; the "
                "notation register must say which half is meant."
            ),
            "the_double_inversion_is_not_an_error": (
                "cosh L is coefficient-EVEN while its channel total "
                "E_sym = (p-m) cosh L is diagram-ODD, because the mirror "
                "flips the multiplicity as well as the weight. Both "
                "statements hold of the same summand; only the involution "
                "differs."
            ),
        },
    )

    wb.add_caveat(
        "This is a statement about which involution each label is computed "
        "against, not a claim that any block is wrong. Every parity assertion "
        "checked here is true against the half its own block uses."
    )
    wb.add_caveat(
        "DISCREPANCY FLAGGED, NOT EDITED. eigenbasis-structural-lemmas.md:2 "
        "states 'the bar involution q -> q^{-1} swaps the seminormal "
        "eigenvalues q <-> -q^{-1}'. Computed here, neither half nor the "
        "full involution produces that swap: the coefficient half sends "
        "{q, -1/q} to the spectrum of sigma^{-1}, and the full involution "
        "FIXES both idempotents pointwise. The standard operation that does "
        "exchange the symmetric and alternating channels is the "
        "Iwahori-Matsumoto involution, not the bar involution. Scope (a): "
        "this tests the eigenvalue-swap sentence only. It does not test the "
        "conjugate-character identity chi_lambda(1/q) = eps * "
        "chi_{lambda'}(q) that the block draws from it, which may hold on "
        "other grounds. Author's call."
    )
    wb.add_caveat(
        "Grading D is verified on the sym/alt Hecke block only, where "
        "electroweak-triplet-charge-spin-from-involution-proof.md:3 states "
        "the spin involution acts as the eigenvalue swap. The spin involution "
        "of def:spin-involution is defined on a general Frobenius *-algebra; "
        "that it coincides with the bar involution elsewhere is not checked "
        "here."
    )

    path = wb.save()

    print("=" * 72)
    print("bar-parity involution atlas        (proton pin, %d dps)" % DPS)
    print("=" * 72)
    print()
    print("  one involution, applied by halves:")
    print("    coefficient half   q -> 1/q          (diagram fixed)")
    print("    diagram half       sigma -> sigma^-1 (mirror, p <-> m)")
    print("    FULL = both        <- def:bar-involution")
    print()
    print(f"  {'object':10s} {'coef half':>10s} {'mirror':>10s} {'FULL bar':>10s}")
    for name, row in atlas.items():
        print(
            f"  {name:10s} {row['coefficient_half']:>10s} "
            f"{row['diagram_half_mirror']:>10s} "
            f"{row['full_bar_involution']:>10s}"
        )
    print()
    print("  A (weights) and D (spin sectors): SAME grading, coefficient half")
    print("  C (mirror totals): other half -> anti-correlated with A")
    print("  B (Hecke e_+/e_-): both FIXED by the full involution, not graded")
    print()
    for k_, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k_}")
    print()
    print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'}")
    print(f"  witness -> {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
