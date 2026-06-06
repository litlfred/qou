#!/usr/bin/env python3
"""GAP-A-4 T15 probe — polynomial-side: χ^{(2,1)}(β_Bor) closed form in h.

Follow-up to the merged T13/T14 retrospective in PR #1925.  The audit
identified "polynomial-side mechanisms (NOT q-series expansions)" as the
first remaining open direction after 8 cross-algebra functor refutations.
T15 derives one concrete polynomial-side structural identity:

  χ^{(2,1)}(β_Bor)  =  2  −  3·h⁴  −  h⁶        (where h = q − q⁻¹)

PROOF (in this probe):

  The closed-form character from `prop:borromean-markov-trace-closed-form`:
    χ^{(2,1)}(β_Bor) = (−q^{12} + 3q^{10} − 3q^8 + 4q^6 − 3q^4 + 3q^2 − 1) / q^6

  Rewrite using X = q²:
    = (−X^6 + 3X^5 − 3X^4 + 4X^3 − 3X^2 + 3X − 1) / X^3
    = −X^3 + 3X^2 − 3X + 4 − 3/X + 3/X^2 − 1/X^3
    = −(X^3 + 1/X^3) + 3(X^2 + 1/X^2) − 3(X + 1/X) + 4

  Use u = X + 1/X = q² + q⁻² = h² + 2 (since h² = q² − 2 + q⁻²):
    X^2 + 1/X^2 = u² − 2
    X^3 + 1/X^3 = u³ − 3u

  Substitute:
    χ^{(2,1)}(β_Bor) = −(u³ − 3u) + 3(u² − 2) − 3u + 4
                     = −u³ + 3u + 3u² − 6 − 3u + 4
                     = −u³ + 3u² − 2

  Substitute u = h² + 2:
    −(h² + 2)³ + 3(h² + 2)² − 2
    = −(h^6 + 6h^4 + 12h² + 8) + 3(h^4 + 4h² + 4) − 2
    = −h^6 − 6h^4 − 12h² − 8 + 3h^4 + 12h² + 12 − 2
    = −h^6 − 3h^4 + 0·h² + 2

  ∴  χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶                          ∎

STRUCTURAL OBSERVATIONS (the probe records these as data):

  (a) The character is a POLYNOMIAL in h² of degree 3 (in h² ⇒ degree 6
      in h).  No h⁰ correction term ⇒ no q⁻¹ poles; the rational
      function (−q^{12} + ...) / q⁶ is entirely polynomial in h.

  (b) The h⁰ coefficient is exactly d_(2,1) = 2 (= dim of the standard
      S_3 irrep).  Consistent with β_Bor → id ∈ S_3 (writhe 0, image
      = identity).

  (c) The h² coefficient is exactly 0.  This is the SOURCE of the
      Borromean h² = 0 cancellation in the full tr_M: the (2,1)
      irrep already has no h² correction at the character level,
      and (3) + (1³) contributions cancel each other.

  (d) The h⁴ coefficient is exactly −3.  Multiplied by the Plancherel
      weight y_{(2,1)}(0) = 2/3 (at h = 0) and adjusted for the
      [h²+4]⁻¹ denominator factor of the full tr_M, this contributes
      part of the Borromean h⁴ = −3/4.

  (e) The h⁶ coefficient is exactly −1.

OPEN COMBINATORIAL QUESTION (NOT proposed as a derivation here):

  Do the coefficient triple (2, 0, −3, −1) at (h⁰, h², h⁴, h⁶)
  admit a combinatorial-bijection interpretation involving the (2,1)
  Young diagram (3 cells, hook lengths (3, 1, 1), 2 standard Young
  tableaux, 2 corners) and the Borromean braid combinatorics
  (β_Bor = (σ₁⁻¹σ₂)³ = 6 crossings, image id ∈ S_3, writhe 0)?

  Per CLAUDE.md "no 7th ansatz" / formalize-first discipline, the
  bijection candidate is NOT proposed here — the probe just records
  the closed form and the structural coefficient triple.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T15-character-polynomial-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from _gap_a4_qsafe import Q_0_50DPS  # noqa: E402

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent

# Tolerance constants (Gemini review #1927: centralise the 1e-40 / 1e-30
# magic values rather than re-typing them at three call sites).
TOL_50DPS = mp.mpf("1e-40")  # closed-form vs polynomial agreement
TOL_NEAR_ZERO = mp.mpf("1e-30")  # h ≈ 0 / q ≈ 1 classical-limit branch


# ── The two forms of χ^{(2,1)}(β_Bor) ─────────────────────────────


def chi_21_from_closed_form_in_q(q: mp.mpf) -> mp.mpf:
    """χ^{(2,1)}(β_Bor) via the closed form from
    `prop:borromean-markov-trace-closed-form`:
       (−q^{12} + 3q^{10} − 3q^8 + 4q^6 − 3q^4 + 3q^2 − 1) / q^6.
    """
    num = (
        -q ** 12 + 3 * q ** 10 - 3 * q ** 8
        + 4 * q ** 6 - 3 * q ** 4 + 3 * q ** 2 - 1
    )
    return num / q ** 6


def chi_21_from_polynomial_in_h(h: mp.mpf) -> mp.mpf:
    """χ^{(2,1)}(β_Bor) via the DERIVED polynomial form: 2 − 3h⁴ − h⁶."""
    return 2 - 3 * h ** 4 - h ** 6


def h_of_q(q: mp.mpf) -> mp.mpf:
    """h = q − q⁻¹."""
    return q - 1 / q


# ── Tests ─────────────────────────────────────────────────────────


def test_closed_form_agreement(q_0: mp.mpf) -> dict:
    """Verify chi_21_from_closed_form_in_q(q_0) =
    chi_21_from_polynomial_in_h(h(q_0)) to 50 dps."""
    print("=" * 78)
    print("T15a — Closed form vs polynomial form for χ^{(2,1)}(β_Bor)")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(q_0, 12)}")
    h_0 = h_of_q(q_0)
    print(f"  h_0 = q_0 − q_0⁻¹ = {mp.nstr(h_0, 12)}")
    print()
    chi_q = chi_21_from_closed_form_in_q(q_0)
    chi_h = chi_21_from_polynomial_in_h(h_0)
    print(f"  Closed form in q: χ^{{(2,1)}}(β_Bor)|_q_0 = "
          f"{mp.nstr(chi_q, 14)}")
    print(f"  Polynomial in h:  2 − 3·h_0⁴ − h_0⁶       = "
          f"{mp.nstr(chi_h, 14)}")
    diff = abs(chi_q - chi_h)
    print(f"  |diff|                                  = {mp.nstr(diff, 14)}")
    match = diff < TOL_50DPS
    print(f"  Match: {'✓ (identity proven by derivation in docstring)' if match else '✗'}")
    return {
        "q_0": str(q_0),
        "h_0": str(h_0),
        "chi_from_closed_form_q": str(chi_q),
        "chi_from_polynomial_h": str(chi_h),
        "absolute_difference": str(diff),
        "identity_verified": match,
    }


def test_h_coefficients_at_sample_h_values() -> dict:
    """Verify the polynomial form 2 − 3h⁴ − h⁶ at multiple sample h
    values via direct evaluation (sanity check the closed form)."""
    print("=" * 78)
    print("T15b — Polynomial form sanity at sample h values")
    print("=" * 78)
    samples = [mp.mpf("0.0"), mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.5")]
    rows = []
    for h_val in samples:
        # Convert h to q via the inverse of h = q − q⁻¹.
        # Standard form: q = (h + √(h²+4))/2 — numerically stable for
        # h ≥ 0.  For h < 0 the standard form has catastrophic
        # cancellation (Gemini review #1927); use the conjugate form
        # q = 2 / (−h + √(h²+4)) which is mathematically equivalent and
        # numerically stable for h < 0.
        if abs(h_val) < TOL_NEAR_ZERO:
            q_val = mp.mpf(1)
        elif h_val > 0:
            q_val = (h_val + mp.sqrt(h_val ** 2 + 4)) / 2
        else:
            q_val = 2 / (-h_val + mp.sqrt(h_val ** 2 + 4))
        chi_q = chi_21_from_closed_form_in_q(q_val)
        # Use the single-source helper rather than re-encoding the
        # polynomial inline (Copilot review #1927: avoid drift if the
        # closed form is ever updated).
        chi_h_poly = chi_21_from_polynomial_in_h(h_val)
        diff = abs(chi_q - chi_h_poly)
        match = diff < TOL_50DPS
        print(f"  h = {mp.nstr(h_val, 4):>8}: "
              f"χ_q = {mp.nstr(chi_q, 12):>16}  "
              f"poly = {mp.nstr(chi_h_poly, 12):>16}  "
              f"{'✓' if match else '✗'}")
        rows.append({
            "h": str(h_val),
            "q_from_h": str(q_val),
            "chi_from_closed_form": str(chi_q),
            "chi_from_polynomial": str(chi_h_poly),
            "match": match,
        })
    return {"samples": rows}


def test_coefficient_triple() -> dict:
    """Record the coefficient triple (h⁰, h², h⁴, h⁶) = (2, 0, −3, −1)
    as the structural data point."""
    print("=" * 78)
    print("T15c — Coefficient triple of χ^{(2,1)}(β_Bor) in h")
    print("=" * 78)
    print(f"  χ^{{(2,1)}}(β_Bor) = 2 + 0·h² + (−3)·h⁴ + (−1)·h⁶")
    print()
    print(f"  Per-order interpretation:")
    print(f"    h⁰ = +2:  d_{{(2,1)}} (dim of standard S_3 irrep)")
    print(f"               consistent with β_Bor → id ∈ S_3.")
    print(f"    h² = 0:   no h² correction at character level — this")
    print(f"               is the SOURCE of the Borromean h² = 0 in tr_M.")
    print(f"    h⁴ = −3:  the SOURCE of the Borromean h⁴ = −3/4 in tr_M")
    print(f"               (combined with Plancherel weight y_{{(2,1)}}(0)")
    print(f"               = 2/3 and the [h²+4]⁻¹ denominator).")
    print(f"    h⁶ = −1:  next-order contribution.")
    print()
    print(f"  OPEN combinatorial question (not proposed as a derivation):")
    print(f"    Do (2, 0, −3, −1) match any natural counting on the")
    print(f"    (2,1) Young diagram (3 cells, hooks (3,1,1), 2 SYT,")
    print(f"    2 corners) crossed with the Borromean braid structure")
    print(f"    (6 crossings, π = id ∈ S_3, writhe 0)?")
    return {
        "coefficient_triple_h0_h2_h4_h6": [2, 0, -3, -1],
        "polynomial_form": "χ^{(2,1)}(β_Bor) = 2 − 3·h⁴ − h⁶",
        "structural_notes": {
            "h0_equals_dim_2_1": "d_(2,1) = 2 (β_Bor → id ∈ S_3)",
            "h2_equals_zero": "no character-level h² correction "
                              "(source of Borromean h² = 0)",
            "h4_equals_minus_three": "source of Borromean h⁴ = −3/4 "
                                     "(via y_(2,1)(0) = 2/3 + denominator)",
            "h6_equals_minus_one": "next-order contribution",
        },
        "open_combinatorial_question": (
            "Do (2, 0, −3, −1) admit a counting interpretation on the "
            "(2,1) Young diagram crossed with β_Bor braid structure? "
            "Not proposed as a derivation here per formalize-first / "
            "no-7th-ansatz discipline."
        ),
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    # mp.mp.dps set by set_compute_dps() at module top (50 dps default).
    w = WitnessBuilder("gap-a4-T15-character-polynomial-probe",
                       engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-06-gap-a4-T9-T14-followup-retrospective.md"
    )
    w.set_description(
        "GAP-A-4 T15 — polynomial-side: derives the closed form "
        "χ^{(2,1)}(β_Bor) = 2 − 3·h⁴ − h⁶ in h = q − q⁻¹, verified "
        "to 50 dps against the closed form in q.  Records the "
        "coefficient triple (2, 0, −3, −1) and queues the open "
        "combinatorial-bijection question without proposing a "
        "derivation (per formalize-first / no-7th-ansatz)."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    # q_0 is recorded as the full 50-dps string via add_parameter above;
    # do NOT add a low-precision float copy (Copilot review #1927).

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    closed = test_closed_form_agreement(q_0)
    print()
    samples = test_h_coefficients_at_sample_h_values()
    print()
    coef = test_coefficient_triple()

    w.add_data("closed_form_agreement", closed)
    w.add_data("h_value_samples", samples)
    w.add_data("coefficient_triple", coef)

    # Assertions
    w.add_assertion(
        "polynomial_form_matches_closed_form_at_q0",
        computed=float(mp.mpf(closed["absolute_difference"])),
        expected=0.0,
        tolerance=float(TOL_50DPS),
        source=(
            "χ^{(2,1)}(β_Bor) = (−q^{12} + 3q^{10} − 3q^8 + 4q^6 − "
            "3q^4 + 3q^2 − 1)/q^6 = 2 − 3·h⁴ − h⁶ (where h = q − q⁻¹), "
            "derived via u = q² + q⁻² = h² + 2 substitution.  "
            "Verified to 50 dps at q_0."
        ),
    )
    # Polynomial form at h = 0 should equal d_(2,1) = 2.
    chi_at_h_zero = chi_21_from_polynomial_in_h(mp.mpf(0))
    w.add_assertion(
        "polynomial_at_h_zero_equals_dim_two_one",
        computed=float(chi_at_h_zero),
        expected=2.0,
        tolerance=float(TOL_NEAR_ZERO),
        source=(
            "At h = 0 (q = 1), χ^{(2,1)}(β_Bor)|_{q=1} = "
            "χ^{(2,1)}(id) = d_(2,1) = 2 since β_Bor → id ∈ S_3."
        ),
    )

    synthesis = (
        "T15 derives χ^{(2,1)}(β_Bor) = 2 − 3·h⁴ − h⁶ exactly via "
        "the u = q² + q⁻² = h² + 2 substitution applied to the closed "
        "form (−q^{12} + 3q^{10} − 3q^8 + 4q^6 − 3q^4 + 3q^2 − 1)/q^6 "
        "from prop:borromean-markov-trace-closed-form.  Verified to "
        "50 dps at q_0 and at 4 sample h-values.  Structural triple "
        "(h⁰, h², h⁴, h⁶) = (2, 0, −3, −1): h⁰ = 2 = d_(2,1); "
        "h² = 0 is the source of the Borromean h² = 0 cancellation "
        "at the character level (the (3) and (1³) contributions cancel "
        "each other at h² order, leaving (2,1) which already has no "
        "h² character correction); h⁴ = −3 is the structural source of "
        "the Borromean h⁴ = −3/4 in the full tr_M (combined with "
        "Plancherel weight y_(2,1)(0) = 2/3 and the [h²+4]⁻¹ "
        "denominator factor).  This closed form OPENS the polynomial-"
        "side direction in the audit doc's remaining search space, but "
        "the open combinatorial-bijection question — whether the "
        "coefficient triple admits a counting interpretation on the "
        "(2,1) Young diagram crossed with β_Bor's braid structure — "
        "is NOT proposed as a derivation per formalize-first discipline."
    )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
