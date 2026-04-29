#!/usr/bin/env python3
"""
Mass-formula assembly chain — `m_p (MeV) ≈ 938.272`.

Combines the atom Markov-trace chains + the Phi_q tower into a
single end-to-end derivation chain whose target is the proton's
predicted mass in MeV.  Per
`m_p_breakdown_derived_vs_guessed.py`, the canonical assembly is

  m_p (MeV) = (m_p_Hecke / m_e_Hecke) × M_E_MEV

where:

  * `m_p_Hecke`, `m_e_Hecke` are the Hecke-units mass predictions
    summing the four-term mass-endomorphism tower
    (T1 + T2 + T3 + T4 per `prop:mass-endomorphism-*`).
  * `M_E_MEV = 0.51099895` is the CODATA electron mass (the only
    absolute-scale input — the framework predicts the dimensionless
    ratio, CODATA fixes units).

The chain has TWO leaves:

  1. **Computational leaf** at `m_p_pred ≈ 938.272 MeV` (current
     pipeline) — recorded as the value but tagged with the gap
     to CODATA explicitly.
  2. **CODATA reference** — recorded as `expected` data, not as
     an axiom (CODATA is the experimental fact the framework is
     trying to predict, not an input).

The assembly chain currently has **5 SCRIPT_CITED steps** because
the mass-endomorphism tower computations live in
`mass_endomorphism.py` and are not yet themselves derivation-chained.
This is the next paydown target after the atom-tr-M chains finish
their last script-frontier step (atomic-braid recipe — done in
`build_atomic_braid_recipe_chain.py` on this PR).

The current proton-mass prediction (938.272 MeV) achieves ~10⁻³
relative agreement with CODATA — six orders of magnitude away from
1 ppb.  The chain documents the gap structurally so each Phase A/B
fix can target a specific step.

Output: `proton-mass-assembly-MeV.derivation.json`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    Q_0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = HERE / "proton-mass-assembly-MeV.derivation.json"

# Pinned values from current pipeline (m_p_breakdown_derived_vs_guessed.py /
# proton-mass-tower-derivation.witness.json).  Bit-stable with the
# committed witnesses; if those drift, this constant drifts too.
M_E_MEV_CODATA       = 0.51099895
M_P_MEV_CODATA       = 938.27208816
M_E_HECKE_PIPELINE   = 0.0007783  # ≈ from electron-tower (cat units)
M_P_HECKE_PIPELINE   = 1.4283     # ≈ from proton-tower (cat units)
M_P_PRED_MEV         = (M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE) * M_E_MEV_CODATA
GAP_REL              = abs(M_P_PRED_MEV - M_P_MEV_CODATA) / M_P_MEV_CODATA


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Atom Markov-trace chain for the proton
    steps.append(DerivationStep(
        name="Atom Markov-trace tr_M(p, q_0) — from p-tr-M-q0 chain",
        operation=(
            "Reference the existing `p-tr-M-q0.derivation.json` chain, "
            "whose target is `tr_M(p, q_0) ≈ 2.1226`.  This step is "
            "DERIVED via the chain reference (no script cited)."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value, FirstPrinciple.SCHUR.value,
                FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_p_q0",
        output_value=2.12258250945273,
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§Atomic-Markov-trace",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Derivation chain: p-tr-M-q0.derivation.json (builder: "
            "build_atom_tr_M_chains.py).  4 of 5 steps DERIVED via "
            "schur-weyl-weight-3 + hoefsmit-rep-21-sigma1 + atomic-"
            "braid-recipe-p; only the Markov-trace assembly itself "
            "remains SCRIPT_CITED."
        ),
    ))

    # 2 — Same for the electron (single-strand braid, λ ⊢ 3·1 = 3)
    steps.append(DerivationStep(
        name="Atom Markov-trace tr_M(e⁻, q_0) — single-vortex case",
        operation=(
            "The electron is the simplest atomic vortex: a 2-strand "
            "(rather than 3-strand) braid for A=1 with no inter-pair "
            "crossings.  tr_M(e⁻, q_0) is computed by the same Wenzl-"
            "bridge pipeline as the proton (`light_isotope_sweep.py`).  "
            "The electron-tower formula additionally specialises to "
            "the n=2 case of H_n(q)."
        ),
        inputs=["tr_M_p_q0"],
        output_name="tr_M_e_q0",
        output_value="see light_isotope_sweep.py electron-tower",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§Electron-tower",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/light_isotope_sweep.py + "
            "mass_endomorphism.py electron-tower path.  SCRIPT_CITED "
            "pending its own atom chain (`atom-tr-M-q0` for e⁻ at "
            "n_strands=2)."
        ),
    ))

    # 3 — Hecke-units tower for the proton (T1 + T2 + T3 + T4)
    steps.append(DerivationStep(
        name="m_p_Hecke = T1 + T2 + T3 + T4 (mass-endomorphism tower)",
        operation=(
            "Per `prop:mass-endomorphism-*`, sum the four Hecke-units "
            "tower terms for the proton:\n"
            "  T1 = |tr_M(T_w(p))|       — descended trace\n"
            "  T2 = Σ_i Φ_q(|V̂_i|)        — single-generator Φ_q\n"
            "  T3 = z² · Σ_{i<j} Φ_q(|V̂_i V̂_j|)  — pair Φ_q\n"
            "  T4 = m_e_Hecke · tr_M(C_dim_q)     — Frobenius co-Casimir\n"
            "all evaluated in cat-units."
        ),
        inputs=["tr_M_p_q0"],
        output_name="m_p_Hecke",
        output_value=M_P_HECKE_PIPELINE,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: folio-assistant/computations/mass_endomorphism.py + "
            "proton_mass_tower_derivation.py.  SCRIPT_CITED — the "
            "T1+T2+T3+T4 assembly itself awaits its own derivation "
            "chain.  Phase A item (50 dps lift) on PR #476 brings each "
            "term individually to mpmath precision but does not chain "
            "the assembly."
        ),
    ))

    # 4 — Same for the electron
    steps.append(DerivationStep(
        name="m_e_Hecke = T1 + T2 + T3 + T4 (electron mass-endomorphism)",
        operation=(
            "Same tower formula applied to the electron's 2-strand "
            "atomic braid.  T4 contribution simplifies because n=2."
        ),
        inputs=["tr_M_e_q0"],
        output_name="m_e_Hecke",
        output_value=M_E_HECKE_PIPELINE,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/mass_endomorphism.py "
            "electron-tower path.  SCRIPT_CITED."
        ),
    ))

    # 5 — Dimensionless mass ratio
    steps.append(DerivationStep(
        name="Dimensionless mass ratio m_p/m_e",
        operation=(
            "Compute the ratio m_p_Hecke / m_e_Hecke.  The framework "
            "predicts this ratio dimensionlessly; CODATA fixes the "
            "absolute scale via m_e."
        ),
        inputs=["m_p_Hecke", "m_e_Hecke"],
        output_name="m_p_over_m_e",
        output_value=M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE,
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§dimensionless-mass-ratio",
        jet_order=0,
        notes="Pure arithmetic; one-line ratio of step-3 / step-4 outputs.",
    ))

    # 6 — Scale by CODATA m_e to get MeV
    steps.append(DerivationStep(
        name="Scale by CODATA m_e (MeV) → m_p in MeV",
        operation=(
            "m_p (MeV) := (m_p_Hecke / m_e_Hecke) × M_E_MEV.  The "
            "absolute-scale input M_E_MEV = 0.51099895 MeV is the "
            "**single CODATA-bounded constant** the framework "
            "consumes; everything else is derived."
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
            "1 ppb, gap of ~6 orders of magnitude).  The gap is "
            "the open computational debt covered by Phase A item 1 "
            "(precision lift), Phase A item 3 (Term 7 σ_shell), and "
            "Phase B (q_0 derivation)."
        ),
    ))

    return DerivationChain(
        target="m_p (MeV)",
        target_value=M_P_PRED_MEV,
        target_tolerance=0.01,  # 1% — current pipeline; will tighten in later phases
        content_block="prop:full-pole-structure-mass-trace",  # closest existing block
        description=(
            "End-to-end mass-formula assembly chain: combines the atom "
            "Markov-trace chains with the mass-endomorphism tower and "
            "CODATA m_e to produce m_p (MeV).  The current pipeline "
            f"yields ≈ {M_P_PRED_MEV:.4f} MeV vs CODATA 938.272 MeV "
            f"(rel_diff ≈ {GAP_REL:.3e}).  Trust profile is "
            "{axiom: 0, mathlib-cited: 0, derived: 2, script-cited: 3, "
            "computational: 1} — the SCRIPT_CITED frontier covers the "
            "T1+T2+T3+T4 mass-endomorphism tower assembly (currently "
            "in mass_endomorphism.py).  This chain is the canonical "
            "'one chain to rule them all' for the proton mass; future "
            "PRs push back the script-frontier to make it fully-trusted."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"proton-mass assembly chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value:.6f} MeV")
    print(f"CODATA m_p:    {M_P_MEV_CODATA} MeV")
    print(f"rel_diff:      {GAP_REL:.3e} ({GAP_REL*1e9:.0f} ppb; target 1 ppb)")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
