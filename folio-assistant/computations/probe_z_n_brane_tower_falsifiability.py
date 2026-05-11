#!/usr/bin/env python3
"""Empirical falsifiability test of `he3_vs_tritium_shell_cancels`.

The Lean theorem `he3_vs_tritium_shell_cancels` in
`conj-magic-shell-stabilization.lean` proves:

    (B(³He) + Δ_shell(2, 1)) - (B(³H) + Δ_shell(1, 2))
      = B(³He) - B(³H)

under the Z↔N symmetry axiom `Δ_shell(Z, N) = Δ_shell(N, Z)`.

This gives a **falsifiable prediction**: if `B^⋆ = B + Δ_shell`
matches AME, then

    B(³He) - B(³H)  ≈  B^⋆(³He) - B^⋆(³H)  =  AME(³He) - AME(³H)
                                            =  -0.76374 MeV
                                            (+ Coulomb correction)

Coulomb correction for mirror nuclei: ³He has Z=2 (one p-p pair) at
~1.96 fm vs ³H has Z=1 (no p-p pair).  E_C(³He) - E_C(³H) ≈
+0.7 MeV (single proton-proton Coulomb repulsion at nuclear scale).

So the EXPECTED brane-tower mass difference under Z↔N symmetry +
Coulomb correction is

    B(³He) - B(³H)  ≈  AME(³He) - AME(³H)  −  E_C
                    ≈  −0.76  −  0.7
                    ≈  −1.46 MeV

This probe pulls `B(³He)` and `B(³H)` from each of the six probed
brane-tower conventions in PR #638 and computes the difference,
compared to the predicted −1.46 MeV.

Output: `z-n-brane-tower-falsifiability.witness.json`
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from witness_base import WitnessBuilder

AME = {"tritium": 8.481798, "he3": 7.71806}
COULOMB_HE3_MINUS_H3_MEV = 0.7  # approximate single p-p pair @ ~2 fm
EXPECTED_BRANE_DIFF_MEV = (AME["he3"] - AME["tritium"]
                              - COULOMB_HE3_MINUS_H3_MEV)


def pull_b_values(witness_path: Path, atom_extractor):
    """Apply the atom_extractor to a witness JSON to get
    (B_tritium, B_he3) values for a specific scheme."""
    if not witness_path.exists():
        return None, None
    data = json.loads(witness_path.read_text())
    return atom_extractor(data)


def main():
    HERE = Path(__file__).parent

    print("=" * 76)
    print("Z↔N brane-tower falsifiability test — B(³He) - B(³H) vs AME")
    print("=" * 76)
    print(f"  AME(³He) - AME(³H) = {AME['he3'] - AME['tritium']:+.4f} MeV")
    print(f"  Coulomb correction (³He - ³H) ≈ +{COULOMB_HE3_MINUS_H3_MEV:.2f} MeV")
    print(f"  Expected brane-tower diff under Z↔N symmetry: "
          f"{EXPECTED_BRANE_DIFF_MEV:+.4f} MeV")
    print()
    print(f"  {'scheme':<48}  {'B(³He)':>9}  {'B(³H)':>9}  {'diff':>9}")
    print("  " + "-" * 80)

    results = {}

    # Scheme 1: scalar uniform-k at k=2 absolute form.
    w = json.loads(
        (HERE / "probe-phiq-uniform-k.witness.json").read_text()
    )
    b_t = w["data"]["results"]["2"]["tritium"]["B_abs_MeV"]
    b_h = w["data"]["results"]["2"]["he3"]["B_abs_MeV"]
    diff = b_h - b_t
    results["scalar_uniform_k_2_abs"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'scalar uniform k=2 absolute':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    # Scheme 1b: scalar uniform-k subtractive at k=2.
    b_t = w["data"]["results"]["2"]["tritium"]["B_sub_MeV"]
    b_h = w["data"]["results"]["2"]["he3"]["B_sub_MeV"]
    diff = b_h - b_t
    results["scalar_uniform_k_2_subtractive"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'scalar uniform k=2 subtractive':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    # Scheme 2: ell·n_0+k rule.
    w = json.loads(
        (HERE / "probe-phiq-n-star-rule.witness.json").read_text()
    )
    b_t = w["data"]["rows"]["tritium"]["B_abs_MeV"]
    b_h = w["data"]["rows"]["he3"]["B_abs_MeV"]
    diff = b_h - b_t
    results["ell_n0_k_rule_absolute"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'ell·n_0+k rule (n_⋆_T=27, n_⋆_He3=20) abs':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    # Scheme 3: per-eigenvalue operator-valued at k=2.
    w = json.loads(
        (HERE / "probe-phiq-operator-valued.witness.json").read_text()
    )
    b_t = w["data"]["results"]["2"]["tritium"]["B_op_abs_MeV"]
    b_h = w["data"]["results"]["2"]["he3"]["B_op_abs_MeV"]
    diff = b_h - b_t
    results["operator_valued_uniform_k_2"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'operator-valued uniform k=2':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    # Scheme 3a: operator-valued at k=1 (D sweet spot — for completeness).
    b_t1 = w["data"]["results"]["1"]["tritium"]["B_op_abs_MeV"]
    b_h1 = w["data"]["results"]["1"]["he3"]["B_op_abs_MeV"]
    diff1 = b_h1 - b_t1
    results["operator_valued_uniform_k_1"] = {
        "B_tritium": b_t1, "B_he3": b_h1, "diff_he3_minus_h3": diff1,
        "discrepancy_from_expected": diff1 - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'operator-valued uniform k=1':<48}  "
          f"{b_h1:>9.3f}  {b_t1:>9.3f}  {diff1:>+9.3f}")

    # Scheme 4: multiplicity-refined R2 (per-atom n_⋆) — both scalar and op.
    w = json.loads(
        (HERE / "probe-phiq-multiplicity-refined.witness.json").read_text()
    )
    b_t = w["data"]["results"]["R2_mult_truncated"]["tritium"]["B_op_MeV"]
    b_h = w["data"]["results"]["R2_mult_truncated"]["he3"]["B_op_MeV"]
    diff = b_h - b_t
    results["multiplicity_R2_op_per_atom"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'multiplicity R2 op (n_⋆_T=2, n_⋆_He3=1)':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    # Scheme 5: pair-knot product-volume.
    w = json.loads(
        (HERE / "probe-phiq-pair-knot-magic-shell.witness.json").read_text()
    )
    b_t = w["data"]["per_atom"]["tritium"]["B_paired_MeV"]
    b_h = w["data"]["per_atom"]["he3"]["B_paired_MeV"]
    diff = b_h - b_t
    results["pair_knot_product_volume"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'pair-knot product-volume':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    # Scheme 6: pair-knot Markov-trace + LP/SDP.
    w = json.loads(
        (HERE / "probe-phiq-pair-knot-markov-trace.witness.json").read_text()
    )
    b_t = w["data"]["per_atom"]["tritium"]["B_markov_trace_MeV"]
    b_h = w["data"]["per_atom"]["he3"]["B_markov_trace_MeV"]
    diff = b_h - b_t
    results["pair_knot_markov_trace"] = {
        "B_tritium": b_t, "B_he3": b_h, "diff_he3_minus_h3": diff,
        "discrepancy_from_expected": diff - EXPECTED_BRANE_DIFF_MEV,
    }
    print(f"  {'pair-knot Markov-trace (full Gram, LP+SDP)':<48}  "
          f"{b_h:>9.3f}  {b_t:>9.3f}  {diff:>+9.3f}")

    print()
    print("  AME reference:")
    print(f"     B(³He) = {AME['he3']:.4f} MeV")
    print(f"     B(³H)  = {AME['tritium']:.4f} MeV")
    print(f"     AME(³He) - AME(³H) = {AME['he3']-AME['tritium']:+.4f} MeV")
    print(f"     Expected brane-tower diff "
          f"(AME - Coulomb): {EXPECTED_BRANE_DIFF_MEV:+.4f} MeV")
    print()
    print("  Verdict (|brane diff - expected| < 1.0 MeV "
          "≈ Z↔N symmetry plausibly holds):")
    closest = None
    closest_disc = float("inf")
    for scheme, r in results.items():
        disc = abs(r["discrepancy_from_expected"])
        verdict = "✓" if disc < 1.0 else f"✗ ({disc:.2f} MeV off)"
        if disc < closest_disc:
            closest = scheme; closest_disc = disc
        print(f"    {scheme:<48}  {r['diff_he3_minus_h3']:>+9.3f}  {verdict}")
    print()
    print(f"  Closest scheme to expected: {closest} (|Δ| = {closest_disc:.3f} MeV)")
    print()

    w = (
        WitnessBuilder(
            "z-n-brane-tower-falsifiability", engine="python"
        )
        .set_description(
            "Empirical falsifiability test of the "
            "`he3_vs_tritium_shell_cancels` Lean theorem in "
            "conj-magic-shell-stabilization.lean.  Under the Z↔N "
            "symmetry of Δ_shell, the brane-tower difference "
            "B(³He) - B(³H) should equal AME(³He) - AME(³H) modulo "
            "the proton-proton Coulomb correction (~+0.7 MeV).  "
            "Pulls B values from each of the six probed brane-tower "
            "conventions in PR #638 and reports which (if any) "
            "is closest to the expected difference under the Z↔N "
            "hypothesis."
        )
        .set_content_block("conj:magic-shell-stabilization")
        .add_parameter("ame_he3_MeV", AME["he3"])
        .add_parameter("ame_h3_MeV", AME["tritium"])
        .add_parameter("coulomb_correction_MeV", COULOMB_HE3_MINUS_H3_MEV)
        .add_parameter("expected_brane_diff_MeV", EXPECTED_BRANE_DIFF_MEV)
        .add_data("per_scheme_diff", results)
        .add_data("closest_scheme", {
            "name": closest,
            "discrepancy_MeV": closest_disc,
        })
        # Refutation expected: NO brane-tower scheme directly matches
        # the AME Z↔N + Coulomb prediction (records the refutation as
        # the passing outcome).
        .add_assertion(
            "no_brane_tower_scheme_within_1MeV_of_z_n_prediction_refuted",
            computed=0 if closest_disc < 1.0 else 1,
            expected=1,
        )
        .add_caveat(
            "Coulomb correction ~+0.7 MeV is a single-p-p-pair "
            "estimate at r ~ 2 fm; precise value depends on the ³He "
            "charge radius (1.96 fm RMS) and Coulomb-energy formula. "
            "The probe's verdict tolerance (|Δ| < 1.0 MeV) absorbs "
            "this uncertainty."
        )
        .add_caveat(
            "The brane-tower formulae overshoot AME by 50%–1000% on "
            "all atoms (per PR #638 closure).  The B(³He) - B(³H) "
            "DIFFERENCE may nonetheless reflect Z↔N symmetry even "
            "when the absolute B values are far from AME — that is "
            "the precise content of the he3_vs_tritium_shell_cancels "
            "theorem."
        )
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
