#!/usr/bin/env python3
"""
Mass-formula assembly chain at 50 dps — neutron.

Neutron-side counterpart of `build_proton_mass_50dps_chain.py`
(PR #480 + PR #476), built on the substrate-derived T1+T4 Path A
infrastructure that landed with PR #637.

Combines:

  * the neutron Markov-trace assembly chain (fully-trusted on main
    via PR #612) at 50 dps via the Wenzl-bridge symbolic polynomial;
  * the existing 50 dps mass-formula terms from
    `mass-formula-6term-mpfr-50dps.witness.json` (Phase A precision
    lift, PR #476);
  * the substrate-derived `m_n_Hecke` value from
    `derive_m_n_hecke_path_a.py` (T1+T4 partial; quarantines
    T2/T3/T5/T6 as honest open-R&D);
  * CODATA `m_e` at 50 dps for the absolute-scale conversion (CAL-1);
  * the CODATA neutron-mass observation as the comparison target
    (residual-exposure only — NOT a calibration input per the
    three-calibration discipline; see
    [`docs/audits/2026-05-11-three-calibration-discipline-violations.md`](../../docs/audits/2026-05-11-three-calibration-discipline-violations.md)).

The chain target is the predicted `m_n` in MeV at 50 dps; the
COMPUTATIONAL leaf records `rel_diff` against CODATA. The honest
residual (substrate-only, no $m_p$ / $m_n$ injection) is expected
to be **wildly off CODATA** until the T2/T3/T5/T6 R&D closes —
identical character to the proton chain on main.

Output: `neutron-mass-50dps.derivation.json` and
`neutron-mass-codata-50dps.witness.json` (the CODATA cross-check).

Ledger entry: docs/coordination/1ppb.md — adds the neutron-side
counterpart to PR #480's proton chain; closes the open scoping item
in row 40 of the ledger (PR #617). The PR #564 ρ_K LO path is not
used here — that path consumes CODATA $m_p$ and $m_n$, which
violates the three-calibration discipline (see audit doc above).
"""

from __future__ import annotations

# `json` import removed per Copilot review on PR #640 (unused).
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    M_HECKE_PIPELINE_AT_Q0,
    Q_0,
    TR_M_AT_Q0,
    TR_M_AT_Q0_50DPS,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT_CHAIN = HERE / "neutron-mass-50dps.derivation.json"

# CODATA pinned values for the neutron/electron mass comparison; the
# Hecke-pipeline summary values live in
# `derivation_chain.M_HECKE_PIPELINE_AT_Q0` (single source of truth
# per Gemini PR #484 review — see that registry's docstring for the
# precision-lift roadmap).
import mpmath as mp  # 50-dps arithmetic per no-float64 directive
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

# Per `folio-assistant/computations/README.md` and the
# three-calibration discipline (Copilot review PR #640:71):
# import CAL-1 (m_e) directly from the registry; the neutron mass
# is loaded as VALIDATION-only (residual exposure, NOT a calibration
# anchor — that would be a CAL discipline violation).
from codata_constants import M_E_MEV, M_N_MEV_VALIDATION  # noqa: E402

M_E_MEV_CODATA       = M_E_MEV  # CAL-1 (legitimate calibration input)
M_N_MEV_CODATA       = M_N_MEV_VALIDATION  # validation-only (residual target)
# `M_HECKE_PIPELINE_AT_Q0` returns `mp.mpf` post-PR #637 — preserved
# as mp.mpf throughout per the no-float64 directive
# (derivation_chain.py docstring §"Keep the values as mp.mpf to
# preserve 50-dps precision").  Use `mp.nstr()` for display, not
# Python `.4f` formatting.
M_E_HECKE_PIPELINE   = M_HECKE_PIPELINE_AT_Q0["e"]
M_N_HECKE_PIPELINE   = M_HECKE_PIPELINE_AT_Q0["n"]
M_N_PRED_MEV         = (M_N_HECKE_PIPELINE / M_E_HECKE_PIPELINE) * M_E_MEV_CODATA
GAP_REL              = abs(M_N_PRED_MEV - M_N_MEV_CODATA) / M_N_MEV_CODATA


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Reference the neutron Markov-trace assembly chain (50 dps via Wenzl bridge)
    steps.append(DerivationStep(
        name="tr_M(n, q_0) at 50 dps via Markov-trace assembly chain",
        operation=(
            "Reference `markov-trace-assembly-neutron.derivation.json` "
            "(fully-trusted on main as of PR #612).  The 50 dps "
            "evaluation comes from `atomic_tr_m_mpfr_50dps.py`'s "
            "Wenzl-bridge pipeline (mpmath at 50 dps); cross-checked "
            "against the polynomial-ring path at machine precision "
            "via `markov_pipeline_cross_validator`."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value, FirstPrinciple.SCHUR.value,
                FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_n_q0",
        # Per Copilot review on PR #640: source from the 50-dps companion
        # to avoid float64 truncation in a "50dps derivation chain".
        output_value=TR_M_AT_Q0_50DPS["n"],
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§Atomic-Markov-trace",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Derivation chain: markov-trace-assembly-neutron.derivation.json "
            "(fully-trusted after PR #612 added the "
            "`atomic-braid-recipe-n` chain; profile {axiom: 1, "
            "derived: 7, computational: 1}, no SCRIPT_CITED frontier).  "
            "Numerical eval at 50 dps via Wenzl-bridge "
            "(atomic_tr_m_mpfr_50dps.py)."
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
        inputs=["tr_M_n_q0"],
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

    # 3 — Hecke-units mass for neutron
    steps.append(DerivationStep(
        name="m_n_Hecke (neutron mass in cat units, 50 dps)",
        operation=(
            "Sum the T1+T4 trustable-subset of the mass-endomorphism "
            "tower for the neutron at 50 dps, via the substrate-only "
            "Path A derivation (`derive_m_n_hecke_path_a.py`).  "
            "T2/T3/T5/T6 quarantined per the trustable-subset analysis: "
            "T2/T3 structurally empty at A=1 under the current "
            "level-selection rule, T5 sign-indefinite, T6 small Habiro "
            "tail.  SCRIPT_CITED (per-term assembly chains still open)."
        ),
        inputs=["terms_50dps"],
        output_name="m_n_Hecke",
        output_value=mp.nstr(M_N_HECKE_PIPELINE, 50),
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/derive_m_n_hecke_path_a.py "
            "(neutron-side counterpart of derive_m_p_hecke_path_a.py).  "
            "SCRIPT_CITED — the T1+T2+T3+T4 assembly itself awaits its "
            "own derivation chain; the current value is T1+T4 only "
            "(trustable subset).  Phase A item (50 dps lift) on PR #476 "
            "brings each term individually to mpmath precision.  "
            "**Precision note**: the stored `output_value` is a "
            "50-significant-figure decimal string from `mp.nstr(..., 50)` "
            "(50-dps full precision lives in the upstream "
            "`mass-formula-6term-mpfr-50dps.witness.json`; consumers "
            "needing more than 20 sig figs should read that witness "
            "directly rather than this chain step).  "
            "**Alternative-paths cross-reference**: the PR #564 ρ_K^LO "
            "path consumes CODATA $m_p$ and $m_n$ to produce 0 ppb "
            "residuals for $\\{p, n\\}$ by construction; that path "
            "violates the three-calibration discipline (audit doc: "
            "docs/audits/2026-05-11-three-calibration-discipline-violations.md). "
            "This chain follows the discipline strictly — substrate-"
            "only T1+T4, no $m_n$ injection — so the residual is the "
            "honest open-R&D delta, not a calibration tautology."
        ),
    ))

    # 4 — Same for the electron
    steps.append(DerivationStep(
        name="m_e_Hecke (electron mass in cat units, 50 dps)",
        operation=(
            "Same tower formula applied to the electron's 2-strand "
            "atomic braid; 50 dps via the same mpmath pipeline."
        ),
        # Electron Path A derivation is independent of the neutron
        # step (per Copilot review #640:196 — was previously
        # ["m_n_Hecke"] placeholder which misrepresented the
        # dependency graph).
        inputs=[],
        output_name="m_e_Hecke",
        output_value=mp.nstr(M_E_HECKE_PIPELINE, 50),
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/derive_m_e_hecke_path_a.py "
            "(electron Path A; consumed via M_HECKE_PIPELINE_AT_Q0['e']).  "
            "SCRIPT_CITED until the electron-tr-M-q0 chain ships.  "
            "**Precision note**: the stored `output_value` is a "
            "50-significant-figure decimal string from `mp.nstr(..., 50)` "
            "(full 50-dps precision lives in the upstream "
            "`mass-formula-6term-mpfr-50dps.witness.json`)."
        ),
    ))

    # 5 — Dimensionless mass ratio
    steps.append(DerivationStep(
        name="Dimensionless mass ratio m_n/m_e at 50 dps",
        operation=(
            "Compute the ratio m_n_Hecke / m_e_Hecke at 50 dps.  The "
            "framework predicts this ratio dimensionlessly; CODATA "
            "fixes the absolute scale via m_e."
        ),
        inputs=["m_n_Hecke", "m_e_Hecke"],
        output_name="m_n_over_m_e",
        output_value=mp.nstr(M_N_HECKE_PIPELINE / M_E_HECKE_PIPELINE, 50),
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§dimensionless-mass-ratio",
        jet_order=0,
        notes="Pure arithmetic (ratio of two 50 dps values).",
    ))

    # 6 — Scale by CODATA m_e to get MeV
    steps.append(DerivationStep(
        name="Scale by CODATA m_e (MeV) → m_n in MeV",
        operation=(
            "m_n (MeV) := (m_n_Hecke / m_e_Hecke) × M_E_MEV.  "
            f"M_E_MEV = {M_E_MEV_CODATA} MeV is the **single CODATA-"
            "bounded constant** the framework consumes."
        ),
        inputs=["m_n_over_m_e"],
        output_name="m_n_pred_MeV",
        output_value=mp.nstr(M_N_PRED_MEV, 50),
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            f"COMPUTATIONAL leaf: m_n_pred ≈ {mp.nstr(M_N_PRED_MEV, 6)} MeV "
            f"vs CODATA m_n = {mp.nstr(M_N_MEV_CODATA, 12)} MeV.  Current relative "
            f"error: {mp.nstr(GAP_REL, 4)} = {mp.nstr(GAP_REL * mp.mpf('1e9'), 5)} ppb (target: "
            "1 ppb).  Closing the gap "
            "requires Phase A item completion (Terms 2-6 at full 50 "
            "dps without f64 chokepoints), rebasing onto the ρ_K "
            "canonical path (0 ppb empirically via "
            "atomic_mass_via_rho_k.py), and Phase B (q_0 derivation "
            "to clear the 780 ppb CAL-2 floor)."
        ),
    ))

    return DerivationChain(
        target="m_n (MeV)",
        target_value=mp.nstr(M_N_PRED_MEV, 50),
        target_tolerance=0.01,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Mass-formula assembly chain for the neutron at 50 dps.  "
            "Parallel to the proton chain (`build_proton_mass_50dps_chain.py`, "
            "PR #480 + PR #476).  Anchored in the fully-trusted "
            "Markov-trace assembly chain (PR #612) and the Phase A "
            "50 dps Terms 2–6 (PR #476).  Trust profile {axiom: 0, "
            "derived: 2, script-cited: 3, computational: 1} — the "
            "SCRIPT_CITED frontier still covers the T1+T2+T3+T4 "
            "mass-endomorphism tower assembly.  "
            f"Current neutron mass prediction: {mp.nstr(M_N_PRED_MEV, 6)} MeV "
            f"vs CODATA {mp.nstr(M_N_MEV_CODATA, 12)} (rel_diff "
            f"{mp.nstr(GAP_REL, 4)}, {mp.nstr(GAP_REL * mp.mpf('1e9'), 5)} ppb).  Target: 1 ppb."
        ),
        steps=steps,
    )


def emit_codata_witness(chain: DerivationChain) -> None:
    """Emit a separate `neutron-mass-codata-50dps.witness.json` with
    the CODATA comparison data.  Mirrors the proton counterpart."""
    from witness_base import WitnessBuilder
    out = HERE / "neutron-mass-codata-50dps.witness.json"
    w = WitnessBuilder("neutron-mass-codata-50dps", engine="python")
    w.set_description(
        "Cross-pipeline m_n prediction vs CODATA at the precision "
        "achievable by the current pipeline (currently f64-bounded "
        "via mass_endomorphism.py; will lift to 50 dps once the "
        "Phase A tower-lift PRs land, and to ~0 ppb once the chain "
        "rebases onto the ρ_K canonical path)."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    w.add_parameter("q_0", Q_0)
    # Witness values stored as 50-dps decimal strings (mp.nstr) so
    # consumers retain full precision per the no-float64 directive.
    w.add_parameter("M_E_MEV_CODATA", mp.nstr(M_E_MEV_CODATA, 12))
    w.add_parameter("target_precision_ppb", "1.0")
    w.add_assertion(
        "m_n_within_1_ppb",
        computed=mp.nstr(GAP_REL, 50),
        expected="0",
        tolerance=1e-9,
    )
    w.add_assertion(
        "m_n_pred_MeV_finite",
        computed=bool(mp.mpf("0") < M_N_PRED_MEV < mp.mpf("1e3")),
        expected=True,
    )
    w.add_data("m_n_pred_MeV", mp.nstr(M_N_PRED_MEV, 50))
    w.add_data("m_n_codata_MeV", mp.nstr(M_N_MEV_CODATA, 12))
    w.add_data("rel_diff", mp.nstr(GAP_REL, 50))
    w.add_data("rel_diff_ppb", mp.nstr(GAP_REL * mp.mpf("1e9"), 12))
    w.add_data("target_ppb", "1.0")
    if GAP_REL == mp.mpf("0"):
        oom_to_target = mp.mpf("0")
    else:
        # mpmath log10 for full-precision OOM
        oom_to_target = mp.log10(GAP_REL / mp.mpf("1e-9"))
    w.add_data("gap_orders_of_magnitude_to_1ppb", mp.nstr(oom_to_target, 6))
    w.save()


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"neutron-mass 50 dps chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {mp.nstr(M_N_PRED_MEV, 8)} MeV")
    print(f"CODATA m_n:    {mp.nstr(M_N_MEV_CODATA, 12)} MeV")
    print(f"rel_diff:      {mp.nstr(GAP_REL, 4)} "
          f"({mp.nstr(GAP_REL * mp.mpf('1e9'), 6)} ppb; target 1 ppb)")
    chain.save(OUTPUT_CHAIN)
    print(f"Wrote {OUTPUT_CHAIN}")
    emit_codata_witness(chain)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
