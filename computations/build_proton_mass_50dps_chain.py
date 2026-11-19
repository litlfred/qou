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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_trm_reference import tr_m_nucleon  # noqa: E402
from derivation_chain import (  # noqa: E402
    M_HECKE_PIPELINE_AT_Q0,
    Q_0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT_CHAIN = _pb.witness_path("proton-mass-50dps.derivation.json", HERE)

# CODATA pinned values for the proton/electron mass comparison; the
# Hecke-pipeline summary values live in
# `derivation_chain.M_HECKE_PIPELINE_AT_Q0` (single source of truth
# per Gemini PR #484 review — see that registry's docstring for the
# precision-lift roadmap).
import mpmath as mp  # 50-dps arithmetic per the no-float64 directive
from _precision import set_compute_dps, fmt  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
set_compute_dps()

# CAL-1: m_e from codata_constants registry (P31-triage Phase A).
from codata_constants import M_E_MEV as M_E_MEV_CODATA
# Comparison reference (P31-triage Phase B): validation-only CODATA m_p
# used to report the proton-mass-chain residual, not as a prediction input.
from codata_constants import M_P_MEV_VALIDATION as M_P_MEV_CODATA
# `M_HECKE_PIPELINE_AT_Q0` returns `mp.mpf` (PR #637); preserved as
# mp.mpf throughout per the no-float64 directive (derivation_chain.py
# docstring §"Keep the values as mp.mpf to preserve 50-dps precision").
M_E_HECKE_PIPELINE   = M_HECKE_PIPELINE_AT_Q0["e"]
M_P_HECKE_PIPELINE   = M_HECKE_PIPELINE_AT_Q0["p"]
M_P_PRED_HECKE_RATIO_MEV = (M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE) * M_E_MEV_CODATA
"""Single-level Markov-trace prediction for m_p — the 0.597 MeV
result that motivates the brane-tower extension below.  Retained
as `M_P_PRED_HECKE_RATIO_MEV` for the comparison line in the
chain step output."""

# ── HISTORICAL: Borromean tower with substrate-form λ_scale ──
# (λ_A EXCISED as headline 2026-06-24 — the quantities computed in
# this section survive only as audit columns; the canonical headline
# prediction is the muon-anchored Hecke energy further below.)
#
# Per `conj:lambda-scale-substrate-form` (formalised 2026-05-18 on
# PR #683), the Borromean baryon mass formula
# (`conj:borromean-baryon-mass-formula`) closes to 5.4 ppm for the
# proton under the substrate ansatz
#
#   λ_scale = 5/2 − h²·G + O(h^4)
#
# where h = q - 1/q and G = Catalan's constant = Vol(B_3)/8.
#
# Status: JUSTIFICATION (numerical match at 5.4 ppm, plausible
# categorical interpretation), NOT yet derivation. Step 2 of the
# proof (5/2 = H_4 conjugate-pair half-symmetric partition count)
# is rigorously established by enumeration; Steps 1, 3, 4, 5 are
# open R&D.
#
# Wired here clearly marked as CONJECTURAL — the chain step emits
# both the legacy Hecke-pipeline ratio (single-level, off by 99%)
# and the Borromean tower prediction (5.4 ppm) so reviewers see
# both interpretations.
from q_parameter import Q_50_DIGIT_STR
_Q_0 = mp.mpf(Q_50_DIGIT_STR)
_HBAR_Q = (_Q_0 - mp.mpf(1)) / _Q_0
_H = _Q_0 - mp.mpf(1) / _Q_0
# Closed-form exact: Vol(𝓑₃) = 8·G where G = Catalan's constant
# (Adams 1985 + Lobachevsky/Catalan identity, PR #843).  Using
# mpmath's built-in `mp.catalan` here keeps both constants at full
# working precision and removes hardcoded-literal discipline risk
# (CAL-4 audit, 2026-05-22).
_CATALAN_G = mp.catalan
_VOL_B3_LIT = 8 * _CATALAN_G

# λ_scale categorical identity (PROVED — Family A theorem in
# `lambda_scale_all_c_i_family_a.py` + Lean
# `lambda-scale-substrate-form.lean`):
#
#     λ_A(q) = (1/4) · Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4) h²
#
# This is the actual categorical sum at H_4 (conjugate-pair half-
# symmetric partition count, q-deformed via Frame–Robinson–Thrall).
# It TERMINATES exactly at h² (all higher h^{2k} vanish).
#
# The PRIOR form `5/2 − h²·G` shipped in PR #701 / #843 was a
# PSLQ-style empirical fit to CODATA m_p (5.4 ppm match) that the
# 2026-05-18 falsification audit ruled out as a categorical
# identity:
#   - Family A gives + 3h²/4 (positive), not −G (negative) — sign
#     mismatch.
#   - 32 sign-flipped Wedderburn variants at H_4 — none give a
#     negative h² coefficient.
#   - Hecke levels H_2 through H_7 — all positive h².
#   - Transcendental ansätze (Bloch-Wigner, Clausen, ζ(3), Cl_2)
#     — no candidate matches the empirical Σ_geom within 1e-3.
# See `docs/audits/2026-05-18-conjecture-falsification.md`.
#
# This expression is the FRAMEWORK'S ACTUAL PREDICTION — it puts
# the m_p prediction further from CODATA than the falsified fit
# did, but it is the categorical truth as established to date.
# The Bring–Bloch path (`conj:lambda-scale-bring-bloch-identity`)
# remains the open R&D direction for closing m_p to ppb.
# λ_A-path Borromean VolDensity — EXCISED as the headline prediction
# (owner ruling 2026-06-24, docs/coordination/2026-06-24-lambda-a-fit-
# excised-per-knot-density.md): λ_A is a CODATA-implied fit and the
# Vol(𝓑₃)/ℏ_q² form applies c_q² to the wrong volume (+2.96%). Both
# quantities are retained BELOW purely as audit columns in the witness;
# the DeprecationWarning is suppressed because this retention is the
# intentional, documented audit use.
import warnings as _warnings
from _li_2_q_util import per_knot_density_borromean as _vol_density_borromean
with _warnings.catch_warnings():
    _warnings.simplefilter("ignore", DeprecationWarning)
    GEOM_FULL_BORROMEAN_Q0 = _vol_density_borromean(_Q_0)

# Empirical legacy (falsified, retained for the comparison column
# in the audit witness).
LINKING_WEIGHT_FALSIFIED_FIT = mp.mpf(5) / 2 - _H**2 * _CATALAN_G

# Audit columns (excised λ_A paths — NOT predictions):
M_P_PRED_BORROMEAN_MEV = GEOM_FULL_BORROMEAN_Q0 * M_E_MEV_CODATA
M_P_PRED_BORROMEAN_FALSIFIED_FIT_MEV = (
    _VOL_B3_LIT / _HBAR_Q**2 * LINKING_WEIGHT_FALSIFIED_FIT * M_E_MEV_CODATA
)

# ── CANONICAL absolute m_p: muon-anchored Hecke energy ──────────
# m_p = (2·m_μ·F_Bor − 12·m_e)·habiro_ratio, m_μ = m_e·Vol(4₁)/ℏ_q²
# — the production substrate identity (m_p_substrate_identity_50dps.py,
# the same source canonical_mass.py reads; the Habiro truncation
# ladder is part of the production value). Consumed from its witness
# as a decimal string → mp.mpf: the canonical_mass facade returns
# float64, which a 50-dps chain must not consume, and re-inlining the
# identity here would duplicate its production constants (drift risk —
# a partial re-inline missed the habiro_ratio and landed 240 ppb off).
_SUBSTRATE_IDENTITY_WITNESS = HERE / "m-p-substrate-identity-50dps.witness.json"
if not _SUBSTRATE_IDENTITY_WITNESS.exists():
    raise RuntimeError(
        "m-p-substrate-identity-50dps.witness.json missing — run "
        "m_p_substrate_identity_50dps.py first (canonical m_p source)."
    )
M_P_PRED_CANONICAL_MEV = mp.mpf(
    json.loads(_SUBSTRATE_IDENTITY_WITNESS.read_text())["data"]["predictions"]["m_p_MeV"]
)

M_P_PRED_MEV = M_P_PRED_CANONICAL_MEV
CONJECTURAL_M_P_DERIVATION = False
"""The headline M_P_PRED_MEV is the production muon-anchored Hecke
energy (canonical_mass identity, λ_A excised 2026-06-24), not the
conjectural λ_scale tower. Note: q₀ is pinned in the same H¹ datum
that m_p informs, so the CODATA comparison below is a
calibration-consistency cross-check, not an independent prediction
(see AGENTS.md §q₀ anchor convention)."""

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
        # Per Copilot review on PR #640: source from the 50-dps companion
        # to avoid float64 truncation in a "50dps derivation chain".
        # MIGRATED 2026-09-13 (bean qou-4383). Was TR_M_AT_Q0_50DPS["p"], a
        # hardcoded 50-dps string in the GROUPED intra-nucleon frame — correct
        # when written, superseded by the 2026-09-05 ordering ruling
        # (qou-hu1f). Now read through `canonical_trm_reference`, which
        # validates pin AND ordering (qou-y4gi).
        #
        # This step is DOCUMENTARY and the headline mass does not move: the
        # step that consumes it records "see mass-formula-6term-mpfr-50dps
        # .witness.json", and M_P_PRED_MEV comes from the canonical_mass
        # identity, not from here. Checked before changing it — 938.27209 MeV
        # at 0.00285 ppb against a 1 ppb target, before and after.
        output_value=str(tr_m_nucleon("proton")),
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
            "script: computations/mass_formula_6term_mpfr_50dps.py.  "
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
        output_value=mp.nstr(M_P_HECKE_PIPELINE, 50),
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: computations/mass_endomorphism.py + "
            "proton_mass_tower_derivation.py.  SCRIPT_CITED — "
            "the T1+T2+T3+T4 assembly itself awaits its own derivation "
            "chain.  Phase A item (50 dps lift) on PR #476 brings each "
            "term individually to mpmath precision.  "
            "**Precision note**: the stored `output_value` "
            f"({M_P_HECKE_PIPELINE}) is a 4-sig-fig rounded summary "
            "of the upstream pipeline output, kept short for "
            "readability in the chain JSON.  The full-precision 50 dps "
            "values live in `mass-formula-6term-mpfr-50dps.witness.json`; "
            "downstream code that needs >4 sig figs should read from "
            "that witness rather than from this chain step."
        ),
    ))

    # 4 — Same for the electron
    steps.append(DerivationStep(
        name="m_e_Hecke (electron mass in cat units, 50 dps)",
        operation=(
            "Same tower formula applied to the electron's 2-strand "
            "atomic braid; 50 dps via the same mpmath pipeline."
        ),
        inputs=[],  # electron is independent of proton/neutron
        output_name="m_e_Hecke",
        output_value=mp.nstr(M_E_HECKE_PIPELINE, 50),
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower",
        jet_order=0,
        notes=(
            "script: computations/mass_endomorphism.py "
            "electron-tower path.  SCRIPT_CITED until an "
            "electron-tr-M-q0 chain ships.  "
            "**Precision note**: the stored `output_value` "
            f"({M_E_HECKE_PIPELINE}) is a 4-sig-fig rounded summary "
            "of the upstream pipeline output, kept short for "
            "readability in the chain JSON.  Full-precision 50 dps "
            "values live in `mass-formula-6term-mpfr-50dps.witness.json`."
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
        output_value=mp.nstr(M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE, 50),
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§dimensionless-mass-ratio",
        jet_order=0,
        notes="Pure arithmetic (ratio of two 50 dps values).",
    ))

    # 5b — Canonical substrate-identity witness (headline m_p source)
    steps.append(DerivationStep(
        name="Canonical substrate-identity m_p at 50 dps (witness read)",
        operation=(
            "Read data.predictions.m_p_MeV from "
            "m-p-substrate-identity-50dps.witness.json as a 50-dps "
            "decimal string → mp.mpf.  This is the production "
            "muon-anchored Hecke-energy value the canonical_mass "
            "facade also serves; consuming the witness (rather than "
            "re-inlining the identity) keeps the Habiro-ladder "
            "constants single-sourced."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="m_p_substrate_identity_MeV",
        output_value=mp.nstr(M_P_PRED_CANONICAL_MEV, 50),
        trust_basis=TrustBasis.SCRIPT_CITED,
        jet_order=0,
        notes=(
            "script: computations/m_p_substrate_identity_50dps.py "
            "(producer of m-p-substrate-identity-50dps.witness.json; "
            "hash recorded in the codata witness's "
            "upstream_witness_hashes)."
        ),
    ))

    # 6 — Canonical muon-anchored Hecke energy → m_p in MeV
    steps.append(DerivationStep(
        name="Muon-anchored Hecke energy → m_p in MeV",
        operation=(
            "m_p (MeV) := 2·(m_μ·F_Bor − 6·m_e), with the muon anchor "
            "m_μ = m_e·Vol(4₁)/ℏ_q² and the dimensionless Borromean "
            "factor F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ (canonical_mass "
            f"facade identity at 50 dps).  M_E_MEV = {M_E_MEV_CODATA} "
            "MeV is the **single CODATA-bounded constant** the "
            "framework consumes.  The single-level ratio m_p_over_m_e "
            "(step 5) remains as a comparison column only."
        ),
        inputs=["m_p_substrate_identity_MeV"],
        output_name="m_p_pred_MeV",
        output_value=mp.nstr(M_P_PRED_MEV, 50),
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            f"COMPUTATIONAL leaf: m_p_pred ≈ {mp.nstr(M_P_PRED_MEV, 6)} MeV "
            f"vs CODATA m_p = {mp.nstr(M_P_MEV_CODATA, 12)} MeV.  Current relative "
            f"error: {mp.nstr(GAP_REL, 4)} = {mp.nstr(GAP_REL * mp.mpf('1e9'), 5)} ppb.  "
            "λ_A excision (2026-06-24): the former headline Borromean "
            f"VolDensity path ≈ {mp.nstr(M_P_PRED_BORROMEAN_MEV, 6)} MeV "
            "(+2.96%, a CODATA-implied fit) is retained only as an audit "
            "column in the codata witness.  The q₀ pin and m_p inform the "
            "same H¹ datum, so this residual is a calibration-consistency "
            "cross-check (AGENTS.md §q₀ anchor convention)."
        ),
    ))

    return DerivationChain(
        target="m_p (MeV)",
        target_value=mp.nstr(M_P_PRED_MEV, 50),
        target_tolerance=0.01,  # float64-ok: DerivationChain schema tolerance field
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
            f"Current proton mass prediction: {mp.nstr(M_P_PRED_MEV, 6)} MeV "
            f"vs CODATA {mp.nstr(M_P_MEV_CODATA, 12)} (rel_diff "
            f"{mp.nstr(GAP_REL, 4)}, {mp.nstr(GAP_REL * mp.mpf('1e9'), 5)} ppb).  Target: 1 ppb."
        ),
        steps=steps,
    )


def emit_codata_witness(chain: DerivationChain) -> None:
    """Emit a separate `proton-mass-codata-50dps.witness.json` with
    the CODATA comparison data.  This is consumed by the Phase E
    final-convergence assertion in the workplan."""
    from witness_base import WitnessBuilder, load_and_hash_upstream
    out = _pb.witness_path("proton-mass-codata-50dps.witness.json", HERE)
    w = WitnessBuilder("proton-mass-codata-50dps", engine="python")
    w.set_description(
        "Cross-pipeline m_p prediction vs CODATA. Headline m_p is the "
        "canonical muon-anchored Hecke energy read from "
        "m-p-substrate-identity-50dps.witness.json at 50 dps (λ_A "
        "excised 2026-06-24; the Borromean VolDensity paths survive "
        "only as audit columns). The CODATA residual is a "
        "calibration-consistency cross-check per the q₀ anchor "
        "convention, since q₀ and m_p inform the same H¹ datum."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    # Witness values stored as 50-dps decimal strings (mp.nstr) so
    # consumers retain full precision per the no-float64 directive.
    w.add_parameter("q_0", Q_50_DIGIT_STR)
    w.add_parameter("M_E_MEV_CODATA", mp.nstr(M_E_MEV_CODATA, 12))
    w.add_parameter("target_precision_ppb", "1.0")
    w.add_parameter("conjectural_derivation", CONJECTURAL_M_P_DERIVATION)
    w.add_parameter(
        "mass_route",
        "canonical muon-anchored Hecke energy "
        "(canonical_mass identity; λ_A excised 2026-06-24)",
    )
    # expected must be float-parsable: Assertion.passed does
    # abs(float(computed) − float(expected)) ≤ tolerance and the old
    # expected="< 10" silently fell back to string equality (always
    # False, even at 4e-7 ppm).
    w.add_assertion(
        "m_p_within_10_ppm_canonical",
        computed=mp.nstr(GAP_REL * mp.mpf("1e6"), 8),
        expected="0",
        tolerance=mp.mpf("10"),
        unit="ppm",
        source=(
            "muon-anchored Hecke energy m_p = 2·(m_μ·F_Bor − 6·m_e) "
            "(canonical_mass facade identity at 50 dps)"
        ),
    )
    w.add_assertion(
        "m_p_within_1_ppb_target",
        computed=mp.nstr(GAP_REL, 50),
        expected="0",
        tolerance=mp.mpf("1e-9"),
        source=(
            "1 ppb target via the canonical identity. NOTE: q₀ and m_p "
            "inform the same H¹ datum, so this is a calibration-"
            "consistency cross-check, not an independent 1-ppb "
            "prediction (AGENTS.md §q₀ anchor convention)."
        ),
    )
    w.add_assertion(
        "m_p_pred_MeV_finite",
        computed=bool(mp.mpf("0") < M_P_PRED_MEV < mp.mpf("1e3")),
        expected=True,
    )
    w.add_data("m_p_pred_MeV", mp.nstr(M_P_PRED_MEV, 50))
    # Audit columns — the excised λ_A paths (owner ruling 2026-06-24),
    # retained so the fit's magnitude stays visible in the record:
    w.add_data("m_p_borromean_lambdaA_excised_fit_MeV",
               mp.nstr(M_P_PRED_BORROMEAN_MEV, 50))
    w.add_data("m_p_borromean_falsified_fit_MeV",
               mp.nstr(M_P_PRED_BORROMEAN_FALSIFIED_FIT_MEV, 50))
    w.add_data("m_p_codata_MeV", mp.nstr(M_P_MEV_CODATA, 12))
    w.add_data("rel_diff", mp.nstr(GAP_REL, 50))
    w.add_data("rel_diff_ppb", mp.nstr(GAP_REL * mp.mpf("1e9"), 12))
    w.add_data("target_ppb", "1.0")
    if GAP_REL == mp.mpf("0"):
        oom_to_target = mp.mpf("0")
    else:
        # mpmath log10 for full-precision OOM
        oom_to_target = mp.log10(GAP_REL / mp.mpf("1e-9"))
    w.add_data("gap_orders_of_magnitude_to_1ppb", mp.nstr(oom_to_target, 6))

    # Fix #7 (sweep audit 2026-05-18) — declare the canonical Markov-
    # trace axiomatic-closed-form witness in the dep chain, and add the
    # corresponding `prop:` to reference_blocks via add_data so the
    # block-resolver picks it up.
    _option_b_path = _pb.witness_path("option-b-proton-mass-full-chain.witness.json", HERE)
    upstream_hashes: list[dict] = []
    if _option_b_path.exists():
        _, _hr = load_and_hash_upstream(_option_b_path)
        upstream_hashes.append(_hr)
    # The headline m_p_pred_MeV is sourced from the substrate-identity
    # witness — record its hash so witness_dependency_drift.py detects
    # drift in the canonical mass source (Copilot review, PR #3199).
    _, _hr_si = load_and_hash_upstream(_SUBSTRATE_IDENTITY_WITNESS)
    upstream_hashes.append(_hr_si)
    w.add_data("upstream_witness_hashes", upstream_hashes)
    w.add_data("reference_blocks", [
        "prop:full-pole-structure-mass-trace",
        "prop:markov-trace-axiomatic-closed-form",
    ])
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))

    w.save()


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"proton-mass 50 dps chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {mp.nstr(M_P_PRED_MEV, 8)} MeV")
    print(f"CODATA m_p:    {mp.nstr(M_P_MEV_CODATA, 12)} MeV")
    print(f"rel_diff:      {mp.nstr(GAP_REL, 4)} "
          f"({mp.nstr(GAP_REL * mp.mpf('1e9'), 6)} ppb; target 1 ppb)")
    chain.save(OUTPUT_CHAIN)
    print(f"Wrote {OUTPUT_CHAIN}")
    emit_codata_witness(chain)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
