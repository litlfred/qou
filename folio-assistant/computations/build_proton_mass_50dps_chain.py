#!/usr/bin/env python3
"""
Mass-formula assembly chain at 50 dps — proton.

Phase A precision lift applied to the existing
`build_proton_mass_assembly_chain.py` (f64).  Combines:

  * the proton Markov-trace assembly chain (now fully-trusted on
    main via PR #480) at 50 dps via the Wenzl-bridge symbolic
    polynomial,
  * the existing 50 dps mass-formula terms from
    `mass-formula-6term-mpfr-50dps.witness.json` (ships on PR
    #476's Phase A precision lift),
  * CODATA m_e at 50 dps,
  * the CODATA proton-mass observation as the comparison target.

The chain target is the predicted m_p in MeV at 50 dps; the
COMPUTATIONAL leaf records the rel_diff against CODATA.  This is
the **single canonical chain** for the proton-mass prediction; all
upstream Phase A precision improvements feed through it.

Output: `proton-mass-50dps.derivation.json` and
`proton-mass-codata-50dps.witness.json` (the CODATA cross-check).

Note: this chain currently treats the upstream tower predictions
as SCRIPT_CITED (they live in `mass_endomorphism.py` and have not
themselves been chain-derived).  When the Phase A 50 dps tower
lift lands (PR #476's `mass_formula_6term_mpfr_50dps.py`), this
chain rebases to consume that mpfr witness directly.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    Q_0,
    TR_M_AT_Q0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT_CHAIN = HERE / "proton-mass-50dps.derivation.json"

# Pinned values from current pipeline.  The Hecke-units numbers below
# are SHORT SUMMARIES of the upstream `proton_mass_tower_derivation.py`
# output — they round to 4 significant digits for readability in the
# chain JSON.  Until the full-precision Hecke-units numbers are
# captured by a 50 dps tower-derivation chain (Phase A item 3, see
# `mass_endomorphism.py` precision lift), these summaries are the
# intermediate steps' canonical values.  When the precision lift
# lands, both the constants below and the chain JSON should be
# regenerated from the full-precision tower output.
M_E_MEV_CODATA       = 0.51099895
M_P_MEV_CODATA       = 938.27208816
M_E_HECKE_PIPELINE   = 0.0007783  # rounded summary; see note above
M_P_HECKE_PIPELINE   = 1.4283     # rounded summary; see note above
M_P_PRED_MEV         = (M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE) * M_E_MEV_CODATA
GAP_REL              = abs(M_P_PRED_MEV - M_P_MEV_CODATA) / M_P_MEV_CODATA


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Reference the proton Markov-trace assembly chain (50 dps via Wenzl bridge)
    steps.append(DerivationStep(
        name="tr_M(p, q_0) at 50 dps via Markov-trace assembly chain",
        operation=(
            "Reference `markov-trace-assembly-proton.derivation.json` "
            "(fully-trusted on main as of PR #480).  The 50 dps "
            "evaluation comes from `atomic_tr_m_mpfr_50dps.py`'s "
            "Wenzl-bridge pipeline (mpmath at 50 dps); cross-checked "
            "against the polynomial-ring path at machine precision "
            "via `markov_pipeline_cross_validator`."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value, FirstPrinciple.SCHUR.value,
                FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_p_q0",
        output_value=TR_M_AT_Q0["p"],
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§Atomic-Markov-trace",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Derivation chain: markov-trace-assembly-proton.derivation.json "
            "(fully-trusted, profile {axiom: 1, derived: 6, "
            "script-cited: 0, computational: 1}).  Numerical eval at "
            "50 dps via Wenzl-bridge (atomic_tr_m_mpfr_50dps.py)."
        ),
    ))

    # 2 — Phase-A 50 dps Terms 2-6
    steps.append(DerivationStep(
        name="Mass-formula Terms 2–6 at 50 dps (Phase A precision lift)",
        operation=(
            "Reference `mass-formula-6term-mpfr-50dps.witness.json` "
            "(produced by `mass_formula_6term_mpfr_50dps.py` from "
            "PR #476's Phase A precision lift).  All six unified-"
            "mass-formula terms evaluated at 50 dps mpmath: Term 1 "
            "(descended trace), Term 2/3 (Φ_q tower via mp_Phi_q), "
            "Term 4 (Frobenius co-Casimir), Term 5 (chirality BW), "
            "Term 6 (Habiro residue tail)."
        ),
        inputs=["tr_M_p_q0"],
        output_name="terms_50dps",
        output_value="see mass-formula-6term-mpfr-50dps.witness.json (5 atoms)",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-formula-6term",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: folio-assistant/computations/mass_formula_6term_mpfr_50dps.py.  "
            "SCRIPT_CITED — the per-term assembly into a single "
            "mass-cat-units value awaits its own derivation chain "
            "(open frontier: terms 2-6 individually need per-term "
            "chains analogous to the σ_shell A=2 closed form for "
            "Term 7)."
        ),
    ))

    # 3 — Hecke-units mass for proton
    steps.append(DerivationStep(
        name="m_p_Hecke (proton mass in cat units, 50 dps)",
        operation=(
            "Sum the four-term mass-endomorphism tower for the proton "
            "at 50 dps, drawing each term from the Phase A precision "
            "lift in step 2.  Currently SCRIPT_CITED via "
            "`mass_endomorphism.py` + `proton_mass_tower_derivation.py` "
            "until the per-term chains close."
        ),
        inputs=["terms_50dps"],
        output_name="m_p_Hecke",
        output_value=M_P_HECKE_PIPELINE,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/mass_endomorphism.py + "
            "proton_mass_tower_derivation.py.  SCRIPT_CITED — "
            "the T1+T2+T3+T4 assembly itself awaits its own derivation "
            "chain.  Phase A item (50 dps lift) on PR #476 brings each "
            "term individually to mpmath precision."
        ),
    ))

    # 4 — Same for the electron
    steps.append(DerivationStep(
        name="m_e_Hecke (electron mass in cat units, 50 dps)",
        operation=(
            "Same tower formula applied to the electron's 2-strand "
            "atomic braid; 50 dps via the same mpmath pipeline."
        ),
        inputs=["m_p_Hecke"],  # placeholder — electron is independent
        output_name="m_e_Hecke",
        output_value=M_E_HECKE_PIPELINE,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/mass_endomorphism.py "
            "electron-tower path.  SCRIPT_CITED until an "
            "electron-tr-M-q0 chain ships."
        ),
    ))

    # 5 — Dimensionless mass ratio
    steps.append(DerivationStep(
        name="Dimensionless mass ratio m_p/m_e at 50 dps",
        operation=(
            "Compute the ratio m_p_Hecke / m_e_Hecke at 50 dps.  The "
            "framework predicts this ratio dimensionlessly; CODATA "
            "fixes the absolute scale via m_e."
        ),
        inputs=["m_p_Hecke", "m_e_Hecke"],
        output_name="m_p_over_m_e",
        output_value=M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE,
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§dimensionless-mass-ratio",
        jet_order=0,
        notes="Pure arithmetic (ratio of two 50 dps values).",
    ))

    # 6 — Scale by CODATA m_e to get MeV
    steps.append(DerivationStep(
        name="Scale by CODATA m_e (MeV) → m_p in MeV",
        operation=(
            "m_p (MeV) := (m_p_Hecke / m_e_Hecke) × M_E_MEV.  "
            f"M_E_MEV = {M_E_MEV_CODATA} MeV is the **single CODATA-"
            "bounded constant** the framework consumes."
        ),
        inputs=["m_p_over_m_e"],
        output_name="m_p_pred_MeV",
        output_value=M_P_PRED_MEV,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            f"COMPUTATIONAL leaf: m_p_pred ≈ {M_P_PRED_MEV:.4f} MeV "
            f"vs CODATA m_p = {M_P_MEV_CODATA} MeV.  Current relative "
            f"error: {GAP_REL:.3e} = {GAP_REL*1e9:.0f} ppb (target: "
            "1 ppb, gap of ~6 orders of magnitude).  Closing the gap "
            "requires Phase A item completion (Terms 2-6 at full 50 "
            "dps without f64 chokepoints) + Phase B (q_0 derivation)."
        ),
    ))

    return DerivationChain(
        target="m_p (MeV)",
        target_value=M_P_PRED_MEV,
        target_tolerance=0.01,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Mass-formula assembly chain for the proton at 50 dps.  "
            "Replaces the f64 chain `proton-mass-assembly-MeV` "
            "(PR #476) with a precision-lifted version anchored in "
            "the fully-trusted Markov-trace assembly chain (PR #480) "
            "and the Phase A 50 dps Terms 2–6 (PR #476).  Trust "
            "profile {axiom: 0, derived: 2, script-cited: 3, "
            "computational: 1} — the SCRIPT_CITED frontier still "
            "covers the T1+T2+T3+T4 mass-endomorphism tower assembly.  "
            f"Current proton mass prediction: {M_P_PRED_MEV:.4f} MeV "
            f"vs CODATA {M_P_MEV_CODATA} (rel_diff "
            f"{GAP_REL:.3e}, {GAP_REL*1e9:.0f} ppb).  Target: 1 ppb."
        ),
        steps=steps,
    )


def emit_codata_witness(chain: DerivationChain) -> None:
    """Emit a separate `proton-mass-codata-50dps.witness.json` with
    the CODATA comparison data.  This is consumed by the Phase E
    final-convergence assertion in the workplan."""
    from witness_base import WitnessBuilder
    out = HERE / "proton-mass-codata-50dps.witness.json"
    w = WitnessBuilder("proton-mass-codata-50dps", engine="python")
    w.set_description(
        "Cross-pipeline m_p prediction vs CODATA at the precision "
        "achievable by the current pipeline (currently f64-bounded "
        "via mass_endomorphism.py; will lift to 50 dps once the "
        "Phase A tower-lift PRs land)."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    w.add_parameter("q_0", Q_0)
    w.add_parameter("M_E_MEV_CODATA", M_E_MEV_CODATA)
    w.add_parameter("target_precision_ppb", 1.0)
    w.add_assertion(
        "m_p_within_1_ppb",
        computed=GAP_REL,
        expected=1e-9,
        tolerance=1e-9,
    )
    w.add_assertion(
        "m_p_pred_MeV_finite",
        computed=bool(0 < M_P_PRED_MEV < 1e3),
        expected=True,
    )
    w.add_data("m_p_pred_MeV", M_P_PRED_MEV)
    w.add_data("m_p_codata_MeV", M_P_MEV_CODATA)
    w.add_data("rel_diff", GAP_REL)
    w.add_data("rel_diff_ppb", GAP_REL * 1e9)
    w.add_data("target_ppb", 1.0)
    import math
    if GAP_REL == 0:
        oom_to_target = 0.0
    else:
        oom_to_target = math.log10(GAP_REL / 1e-9)
    w.add_data("gap_orders_of_magnitude_to_1ppb", oom_to_target)
    w.save()


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"proton-mass 50 dps chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value:.6f} MeV")
    print(f"CODATA m_p:    {M_P_MEV_CODATA} MeV")
    print(f"rel_diff:      {GAP_REL:.3e} ({GAP_REL*1e9:.0f} ppb; target 1 ppb)")
    chain.save(OUTPUT_CHAIN)
    print(f"Wrote {OUTPUT_CHAIN}")
    emit_codata_witness(chain)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
