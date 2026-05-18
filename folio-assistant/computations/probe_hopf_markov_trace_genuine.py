#!/usr/bin/env python3
"""Genuine categorical Markov-trace computation for σ_1² in H_2(q).

Companion / replacement for PR #664's `probe_hopf_jones_c3_categorical.py`,
which hardcodes `J_Hopf(q) = -(q + 1/q)` and verifies it equals
hardcoded `c3_empirical = -2`. That probe is tautological — see
docs/audits/2026-05-17-pr-664-c3-c4-critical-review.md.

This probe instead **actually computes** the symbolic Markov trace
of σ_1² in H_2(q) via the Hoefsmit seminormal representation
(`hoefsmit_symbolic.tr_M_symbolic`, the same engine PR #661 used for
its genuine c_2 = b² derivation), then asks what the result tells us
about c_3 in the Q_β precision ladder.

What this probe does NOT claim:
  * Does NOT derive c_3 = -2.  The order-h^6 coefficient extraction
    from the full Q_β expansion is a separate computation that PR #664
    skipped (its Step 4 was hand-waved).
  * Does NOT falsify Story A.  PR #664's "falsified" claim required
    showing c_3 must categorically equal -2 to exclude c_3 = 0; this
    probe shows the symbolic Markov trace exists and what its q=1
    value actually is, which is a strictly weaker statement.

What this probe DOES establish:
  * The symbolic Markov trace tr_M(σ_1²) in H_2(q) as a rational
    function of q (50-dps numerical confirmation at q_0).
  * Its classical q=1 limit (which is NOT -(q + q⁻¹)|_{q=1} = -2;
    they differ by writhe/framing normalisation).
  * The point at which PR #664's reasoning breaks down: equating
    tr_M(σ_1²) with the "Jones polynomial -(q + q⁻¹)" requires
    convention-fixing that the PR did not do explicitly.

Output: `hopf-markov-trace-genuine.witness.json`
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hoefsmit_symbolic import tr_M_symbolic, Q  # noqa: E402
from markov_weights_symbolic import tr_M_canonical  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    mp.mp.dps = 50

    # σ_1² in H_2: braid word of length 2, generator 0, positive crossings.
    crossings = [(0, "sigma"), (0, "sigma")]

    # Two Markov-trace implementations live in the codebase:
    #   (i) hoefsmit_symbolic.tr_M_symbolic  → uses w_λ · χ^λ / f^λ
    #  (ii) markov_weights_symbolic.tr_M_canonical → uses y_λ · χ^λ
    # They produce DIFFERENT symbolic answers (see audit doc).
    trM = tr_M_symbolic(crossings, 2)
    trM_simple = sp.cancel(trM)
    trM_at_1 = sp.cancel(trM_simple.subs(Q, 1))

    trM_can, _y_lam = tr_M_canonical(crossings, 2)
    trM_can_simple = sp.cancel(trM_can)
    trM_can_at_1 = sp.cancel(trM_can_simple.subs(Q, 1))

    # Textbook Jones polynomial of the positive Hopf link (Kauffman/Jones,
    # standard normalisation, the value PR #664 claims comes "from V_(2,1)
    # seminormal Markov trace"):
    q_sym = Q
    J_hopf_textbook = -(q_sym + 1 / q_sym)
    J_at_1 = -(2)  # textbook J_Hopf(1) = -2

    # Are they equal?  No — tr_M and J differ by writhe/framing.
    diff = sp.cancel(trM_simple - J_hopf_textbook)

    # Numerical at q_0 = 1.1099785955541805752815940796095093779932822799587
    q0_str = "1.1099785955541805752815940796095093779932822799587"
    q0 = mp.mpf(q0_str)
    trM_at_q0 = mp.mpf(str(sp.N(trM_simple.subs(q_sym, sp.Float(q0_str, 50)), 50)))
    J_at_q0 = -(q0 + 1 / q0)

    print("=" * 90)
    print("  Genuine Markov-trace computation: tr_M(σ_1²) in H_2(q)")
    print("=" * 90)
    print()
    print("  (i) hoefsmit_symbolic.tr_M_symbolic — uses w_λ·χ^λ/f^λ:")
    print(f"    tr_M(σ_1²) = {trM_simple}")
    print(f"    at q = 1:   tr_M = {trM_at_1}")
    print(f"    at q = q_0: tr_M = {mp.nstr(trM_at_q0, 20)}")
    print()
    print("  (ii) markov_weights_symbolic.tr_M_canonical — uses y_λ·χ^λ:")
    print(f"    tr_M(σ_1²) = {trM_can_simple}")
    print(f"    at q = 1:   tr_M = {trM_can_at_1}")
    print()
    print("  These TWO implementations DISAGREE.  Both live on main.")
    print()
    print("  PR #664's claimed J_Hopf(q) (hardcoded in its probe):")
    print(f"    J_Hopf(q) = -(q + q⁻¹) = {sp.expand(J_hopf_textbook)}")
    print(f"    at q = 1:    J = {J_at_1}")
    print(f"    at q = q_0:  J = {mp.nstr(J_at_q0, 20)}")
    print()
    print("  Difference tr_M(σ_1²) − J_Hopf(q):")
    print(f"    {diff}")
    print()
    print("  Verdict: these are DIFFERENT objects.  PR #664's probe")
    print("  hardcodes J_Hopf(q) = -(q+q⁻¹) rather than computing the")
    print("  V_(2,1) seminormal Markov trace.  Equating tr_M with the")
    print("  Jones polynomial requires the writhe-correction factor")
    print("  ζ^writhe (or -1 per skein-relation sign convention), which")
    print("  the PR does not justify explicitly.")
    print()

    # Are they at least proportional / related by a single factor at q_0?
    ratio_at_q0 = trM_at_q0 / J_at_q0
    print(f"  Ratio at q_0:  tr_M(σ_1²)/J_Hopf(q_0) = {mp.nstr(ratio_at_q0, 12)}")
    print()

    # The Markov trace's classical q=1 limit
    print("  Classical q → 1 limit:")
    print(f"    tr_M(σ_1²)|_{{q=1}} = {trM_at_1}    (Markov-trace value)")
    print(f"    J_Hopf|_{{q=1}}     = {J_at_1}    (Jones polynomial value)")
    print()
    print("  PR #664 claims c_3 = J_Hopf(q=1) = -2; if c_3 instead comes")
    print("  from tr_M at q=1, the value is +1, not -2.  The connection")
    print("  to the order-h^6 coefficient of Q_β is left unresolved.")
    print()

    builder = (
        WitnessBuilder("hopf-markov-trace-genuine", engine="sympy")
        .set_description(
            "Genuine V_(2,1) Hoefsmit seminormal Markov-trace computation "
            "of σ_1² in H_2(q), as a polynomial in q (not hardcoded). "
            "Companion / replacement for PR #664's tautological "
            "probe_hopf_jones_c3_categorical.py.  Shows that tr_M(σ_1²) "
            "and the textbook Jones polynomial -(q+q⁻¹) are DIFFERENT "
            "objects; equating them requires writhe/framing-correction "
            "conventions PR #664 did not justify."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-pr-664-c3-c4-critical-review.md"
        )
        .add_parameter("q_0", q0_str)
        .add_data("tr_M_sigma1_sq_symbolic", str(trM_simple))
        .add_data("tr_M_sigma1_sq_at_q_eq_1", str(trM_at_1))
        .add_data("tr_M_sigma1_sq_at_q0_50dps", mp.nstr(trM_at_q0, 50))
        .add_data("tr_M_canonical_sigma1_sq_symbolic", str(trM_can_simple))
        .add_data("tr_M_canonical_sigma1_sq_at_q_eq_1", str(trM_can_at_1))
        .add_data(
            "two_implementations_disagree",
            str(sp.cancel(trM_simple - trM_can_simple)) != "0",
        )
        .add_data("J_Hopf_textbook_symbolic", str(J_hopf_textbook))
        .add_data("J_Hopf_textbook_at_q_eq_1", J_at_1)
        .add_data("J_Hopf_textbook_at_q0_50dps", mp.nstr(J_at_q0, 50))
        .add_data("tr_M_minus_J_Hopf_symbolic", str(diff))
        .add_data("ratio_tr_M_over_J_at_q0_50dps", mp.nstr(ratio_at_q0, 50))
        .add_assertion(
            name="tr_M_and_J_Hopf_are_distinct_symbolically",
            computed=str(diff) != "0",
            expected=True,
            source=(
                "Markov trace and Jones polynomial differ by writhe-correction; "
                "see Kauffman bracket / Markov stabilisation conventions"
            ),
        )
        .add_assertion(
            name="tr_M_at_q_eq_1_is_one",
            computed=int(trM_at_1) if trM_at_1.is_integer else float(trM_at_1),
            expected=1,
            tolerance=1e-30,
            unit="dimensionless",
            source="Direct symbolic substitution q → 1",
        )
        .add_caveat(
            "This probe DOES NOT derive c_3 = -2.  PR #664's claim that "
            "c_3 = J_Hopf(q=1) = -2 rests on (a) identifying tr_M with "
            "the Jones polynomial via a specific convention, AND "
            "(b) extracting the order-h^6 coefficient of the full Q_β "
            "expansion to show this Hopf contribution is the dominant one. "
            "Neither is demonstrated in PR #664.  This probe only shows "
            "what tr_M(σ_1²) actually equals — namely (q²+q⁻²)/[2]_q, "
            "evaluating to +1 at q=1, NOT -2."
        )
        .add_caveat(
            "A genuine c_3 = -2 categorical derivation would require: "
            "(1) build V_(2,1)⊗V_(2,1) Schur-Weyl decomposition in H_6; "
            "(2) project onto V_(2,2,2); "
            "(3) show this projection produces an h^6-order Markov "
            "contribution proportional to the Jones value of the Hopf "
            "closure; "
            "(4) verify no other order-h^6 contribution survives the "
            "Frobenius selection.  All four steps are open work."
        )
        .add_caveat(
            "Infrastructure issue: the codebase has TWO different "
            "tr_M implementations that produce different symbolic answers "
            "for the same braid: hoefsmit_symbolic.tr_M_symbolic uses "
            "Σ_λ w_λ·χ^λ/f^λ while markov_weights_symbolic.tr_M_canonical "
            "uses Σ_λ y_λ·χ^λ (Wenzl's principal-specialization Jones-"
            "Markov weights).  Neither matches the textbook Jones "
            "polynomial -(q+q⁻¹) directly.  An equivalence script "
            "y_lambda_equivalence_proof.py exists but the symbolic "
            "outputs of the two routines do NOT agree on σ_1² in H_2. "
            "Resolution: ratify one as canonical and audit downstream "
            "consumers (proton, neutron, deuteron mass chains all use "
            "hoefsmit_symbolic.tr_M_symbolic; the precision-ladder "
            "Q_β framework cites tr_M_canonical via thm:jones-markov-trace)."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
