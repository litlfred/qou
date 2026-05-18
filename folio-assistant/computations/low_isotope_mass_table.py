#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
═══════════════════════════════════════════════════════════════

Low-isotope mass + Q-value table — derived predictions vs AME2020.

Per branch `claude/ppb-math-infrastructure-p3oQQ` (1 ppb gate): this
table distinguishes **derived** values (rooted in q₀ via the
categorical derivation chain) from **reference-only** values (CODATA /
AME constants kept for comparison) and **derivation-pending** rows
(no fit-free chain available yet). No fits, no numerology, no
empirical calibration is permitted in the predicted column.

Sources of each predicted quantity (status as of this commit):

    m_p   — DERIVATION_PENDING. The producer
            `build_proton_mass_50dps_chain.py` was honesty-rewritten
            on 2026-05-11 to expose the unclosed T1+T4 mass-
            endomorphism tower assembly: it now reports
            m_p_pred = 0.5974 MeV, off by 9 orders of magnitude
            (999 M ppb) from CODATA. The chain's own derivation.json
            self-documents the SCRIPT_CITED frontier. Until the
            T1+T4 assembly closes, this table refuses to consume
            m_p as a derived input — see M_P_DERIVED_MAX_REL_DIFF
            below for the sanity-check threshold.
    m_n   — DERIVATION_PENDING. The Markov-trace neutron chain
            (`build_markov_trace_assembly_neutron_chain.py`) emits a
            dimensionless tr_M only; the MeV scale conversion awaits
            the Phase A tower-lift. Until then: NO predicted m_n.
    B(⁴He) — DERIVATION_PENDING. The magic-A specialization
            `magic_A_formula.magic_A_binding(2,2)` is a deprecation
            candidate (PR #554) and uses ρ_F=2 from
            `binding_ladder_catalog`, which is not chain-validated.
            Canonical tr_M(H_12) compute is the open frontier.
    B(D, T, ³He) — DERIVED via strategy A of
            `low_isotope_binding_sweep.py` (census-knot volumes only;
            pure m_e × Vol(K) — no fits at strategy A). Strategies B
            and C of that file ARE fit-contaminated and are NOT
            consumed here.
    B(A ≥ 4) — DERIVATION_PENDING. Strategies B and C in the sweep
            file use B_4HE_MEV (AME anchor) and a c_αα fit from ¹²C;
            both are excluded under the no-calibration rule.
    Q_β    — CAL-3 input. Available as two sources:
              · `codata` (default): CODATA neutron Q-value (calibrated)
              · `form_a_cos` (substrate, PR #655 + #661 + #662):
                Q_A · cos((z-1)·h/2) with c_2 = b² Kashiwara correction
                from V_(2,1) Hoefsmit (categorical, no fit). Residual
                vs CODATA: ~306 ppm (5.49× tighter than bare Form A).

The `row_derivation_status` field on every emitted row records which
bucket it falls into. Total mass M(Z, N) = A·u + Δ(Z, N) is reported
ONLY for rows where every input (m_p, m_n, B) is derived; otherwise
M_pred_MeV is null and a status string explains the gap.

Anti-staleness infra: every consumed witness is hash-recorded in
`derivation_inputs.upstream_witness_hashes` (sha256 of bytes +
commitSha/scriptCommitSha pulled from the witness body). A future
validator (`witness_dependency_drift.py`, planned in the audit doc
docs/audits/2026-05-16-stale-witness-infra-gap.md) compares these
recorded hashes to the current files on disk; a mismatch means a
consumed upstream changed without this table being regenerated.

Outputs:
    low-isotope-mass-table.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from low_isotope_binding_sweep import (  # noqa: E402
    AME, M_E_MEV, Q0, strategy_A_census,
)
from paper_six_term_isotope_sweep import (  # noqa: E402
    q_beta_for_source, q_beta_substrate_cos_tightened_MeV,
)
from witness_base import load_and_hash_upstream  # noqa: E402

HERE = Path(__file__).parent

# ── Reference constants (CODATA / AME, comparison only) ─────────
# These are NOT consumed as predictions. Kept so the witness can
# report observed mass excesses next to derived predictions.
U_MEV         = 931.49410372      # atomic mass unit, CODATA
# Comparison references (P31-triage Phase B): sourced from codata_constants
# `_VALIDATION` aliases — runtime values identical to the literal CODATA
# digits, but the import name announces validation-only semantics
# (never a prediction input).
from codata_constants import (
    M_P_MEV_VALIDATION as _M_P_REF_MEV_raw,
    M_N_MEV_VALIDATION as _M_N_REF_MEV_raw,
)
# Cast to float for JSON serialization (codata_constants returns mpf).
M_P_REF_MEV = float(_M_P_REF_MEV_raw)
M_N_REF_MEV = float(_M_N_REF_MEV_raw)

# ── m_p sanity-check threshold (anti-tautology + framework-precision gate) ──
# Per the three-calibration discipline, m_p is a PREDICTION, not an
# input. The threshold below is the framework's **real target**:
# CAL-1/2/3 closure to 1 ppb (1e-9), within CODATA experimental
# measurement error.  Reasoning (owner directive 2026-05-16):
#   "tighten to 1 ppb compute infra and within measurement error.
#    this is our real goal."
# CODATA m_p uncertainty is ~50 eV / 938 MeV ≈ 5e-11 (sub-ppb), so
# 1 ppb sits comfortably above the experimental floor.
#
# Threshold history:
#   - 0.01  (1 %)    PR #663 initial guard. Rejected Path A T1+T4
#                    truncation (m_p_pred = 0.597 MeV, 9 orders off).
#   - 0.02  (2 %)    Lifted briefly to admit the 1.63 % full-tower
#                    closure as "derived" on 2026-05-16; reverted on
#                    same date per owner: "tighten to 1 ppb".
#   - 1e-9  (1 ppb)  Current.  The framework's actual closure target.
#                    Every row currently >> threshold → all rows
#                    correctly classified `derivation_pending`.
M_P_DERIVED_MAX_REL_DIFF = 1e-9

# ── Derived inputs ─────────────────────────────────────────────
# m_p comes from the categorical derivation chain at 50 dps.  We
# prefer the full mass-endomorphism tower witness
# (proton-mass-full-tower-50dps.witness.json, T1+T2+T3+T4 sum) over
# the legacy Path A partial witness (proton-mass-codata-50dps.witness.json,
# T1+T4 only); falling back to Path A when the full-tower witness is
# absent.  Either witness may produce an unclosed value above the
# threshold — the sanity guard below catches both cases identically.
_FULL_TOWER_WITNESS = HERE / "proton-mass-full-tower-50dps.witness.json"
_PATH_A_WITNESS     = HERE / "proton-mass-codata-50dps.witness.json"
if _FULL_TOWER_WITNESS.exists():
    _PROTON_WITNESS = _FULL_TOWER_WITNESS
    _proton_w, _proton_hash = load_and_hash_upstream(_PROTON_WITNESS)
    # Full-tower witness schema: data.predictions_MeV.m_p_pred_50dps
    _m_p_pred_raw = float(
        _proton_w["data"]["predictions_MeV"]["m_p_pred_50dps"]
    )
    _m_p_rel_diff = float(
        _proton_w["data"]["comparisons"]["rel_diff_p"]
    )
    _m_p_source_kind = "full_tower_T1_T2_T3_T4_T5_at_A_categorical_max_GS_grade"
else:
    _PROTON_WITNESS = _PATH_A_WITNESS
    _proton_w, _proton_hash = load_and_hash_upstream(_PROTON_WITNESS)
    _m_p_pred_raw = float(_proton_w["data"]["m_p_pred_MeV"])
    _m_p_rel_diff = float(_proton_w["data"]["rel_diff"])
    _m_p_source_kind = "path_a_T1_plus_T4_only"

if abs(_m_p_rel_diff) > M_P_DERIVED_MAX_REL_DIFF:
    # The chain hasn't closed under the current threshold. Treat
    # m_p as pending; do not consume.
    M_P_DERIVED_MEV: float | None = None
    M_P_DERIVED_REL_DIFF: float | None = _m_p_rel_diff
    M_P_DERIVATION_STATUS = (
        f"pending: m_p_pred = {_m_p_pred_raw:.6f} MeV (rel_diff vs CODATA "
        f"= {_m_p_rel_diff:.3e}, above {M_P_DERIVED_MAX_REL_DIFF:.0e} "
        f"chain-closed threshold). Source: {_m_p_source_kind}. The "
        f"mass-endomorphism tower closure path is documented in "
        f"docs/audits/2026-05-16-t1-t4-tower-closure-plan.md."
    )
else:
    M_P_DERIVED_MEV = _m_p_pred_raw
    M_P_DERIVED_REL_DIFF = _m_p_rel_diff
    M_P_DERIVATION_STATUS = (
        f"derived: m_p_pred = {_m_p_pred_raw:.6f} MeV "
        f"(rel_diff vs CODATA = {_m_p_rel_diff:.3e}). "
        f"Source: {_m_p_source_kind}."
    )
M_P_DERIVED_SOURCE = _PROTON_WITNESS.name

# m_n: no fit-free derivation chain yet.
M_N_DERIVED_MEV: float | None = None
M_N_DERIVATION_STATUS = (
    "pending: tr_M(n, q_0) chain emits dimensionless trace only; "
    "MeV scale conversion (build_markov_trace_assembly_neutron_chain.py) "
    "awaits Phase A tower-lift"
)

# B(⁴He): see header docstring; magic_A is deprecation-flagged.
B_4HE_DERIVED_MEV: float | None = None
B_4HE_DERIVATION_STATUS = (
    "pending: magic_A_formula is deprecation-candidate (PR #554, "
    "ρ_F=2 not chain-validated); canonical tr_M(H_12) compute "
    "(canonical_tr_m_helium4_stub.py) is the open frontier"
)

# Substrate Q_β (CAL-2-only).  As of 2026-05-17, uses the full N=4
# categorical chain (PRs #661, #664, #665 + prop:kashiwara-jones-c4-
# categorical) cherry-picked from PR #664 — residual ~0.30 ppm vs
# CODATA (≈ 1000× tighter than the form_a_cos baseline at +306 ppm).
# Available as a CAL-3 alternative; not consumed in the predicted
# column directly (the m_p / m_n chains have their own Q_β handling).
Q_BETA_CODATA_MEV          = float(q_beta_for_source("codata"))
Q_BETA_SUBSTRATE_MEV       = float(q_beta_for_source("full_chain_n4"))
Q_BETA_SUBSTRATE_PPM       = float(
    1e6 * (Q_BETA_SUBSTRATE_MEV - Q_BETA_CODATA_MEV) / Q_BETA_CODATA_MEV
)
# Retain the form_a_cos value too for the witness — useful audit trail
# showing the tightening between forms.
Q_BETA_FORM_A_COS_MEV      = float(q_beta_substrate_cos_tightened_MeV())
Q_BETA_FORM_A_COS_PPM      = float(
    1e6 * (Q_BETA_FORM_A_COS_MEV - Q_BETA_CODATA_MEV) / Q_BETA_CODATA_MEV
)

# Mass excesses computed only from derived inputs. ¹H is no longer
# derivable here because m_p is pending under the rel_diff threshold.
DELTA_H_DERIVED: float | None = (
    M_P_DERIVED_MEV + M_E_MEV - U_MEV if M_P_DERIVED_MEV is not None else None
)
DELTA_N_DERIVED: float | None = None                  # pending m_n


def _derived_binding(symbol: str, Z: int, N: int) -> tuple[float | None, str]:
    """Return (B_pred, derivation_status) using ONLY fit-free derivations.

    Strategy A of low_isotope_binding_sweep (census-knot volumes,
    B = ρ · m_e · Vol(K)) is the only sweep strategy admitted here:
    strategies B and C use AME-anchored B(⁴He) and the c_αα fit
    from ¹²C respectively, which both fail the no-calibration rule.

    Returns (None, status_string) for any row where strategy A does
    not fire (i.e. Z=1,N=0 proton; Z+N≥4 multi-α atoms).
    """
    if Z == 1 and N == 0:
        # ¹H atomic mass = m_p + m_e; B = 0 by definition. But "derived"
        # at the row level only fires when m_p itself is derived; the
        # caller gates on M_P_DERIVED_MEV before propagating.
        return 0.0, "derived: ¹H is a free proton (B = 0 by definition)"
    B_pred, tag = strategy_A_census(symbol, Z, N)
    if B_pred is not None:
        return float(B_pred), f"derived:strategy-A:{tag}"
    return None, (
        "pending: strategy A (census-knot volume) does not cover this "
        "(Z,N); strategies B/C in the sweep are fit-contaminated and "
        "are not consumed under the no-calibration rule"
    )


# ── AME2020 observed mass excesses (MeV, atomic) ────────────────
AME_DELTA = {
    "1H":     7.28897,
    "2H":    13.13572,
    "3H":    14.9498,
    "3He":   14.9312,
    "4He":    2.42492,
    "6Li":   14.0869,
    "7Li":   14.9081,
    "8Be":    4.94167,
    "9Be":   11.3484,
    "10Be":  12.6070,
    "10B":   12.0507,
    "11B":    8.6680,
    "12C":    0.00000,   # AME definition
    "13C":    3.1250,
    "14N":    2.8634,
    "15N":    0.10144,
    "16O":   -4.73700,
    "17O":   -0.80931,
    "18O":   -0.78196,
    "19F":   -1.48740,
    "20Ne":  -7.04193,
    "21Ne":  -5.73175,
    "22Ne":  -8.02466,
}


def predict_row(symbol: str, Z: int, N: int) -> dict:
    """Build one mass-table row from derived inputs only.

    For each row we compute:
      * B_pred_MeV       — derived binding (strategy A only) or None.
      * delta_pred_MeV   — derived Δ = Z·Δ_H + N·Δ_n - B; emitted ONLY
                           when m_n is derived AND B_pred is derived.
                           m_n is currently pending so Δ_pred is null
                           for every row with N > 0.
      * M_pred_MeV       — derived total mass; same gating as Δ_pred.
      * row_derivation_status — string describing which inputs were
                                derived vs pending for this row.
    """
    A = Z + N
    B_pred, b_status = _derived_binding(symbol, Z, N)

    # Δ requires m_p (derived), m_e (CODATA scale, derived chain),
    # m_n (pending), B_pred (derived for ¹H, D, T, ³He only).
    # Under the rel_diff threshold (M_P_DERIVED_MAX_REL_DIFF), m_p is
    # itself pending — so every row's Δ_pred is pending too, even ¹H.
    if N == 0 and B_pred is not None and DELTA_H_DERIVED is not None:
        delta_pred = Z * DELTA_H_DERIVED - B_pred
        m_pred = A * U_MEV + delta_pred
        delta_status = "derived (proton-only atom; no neutron dependency)"
    else:
        delta_pred = None
        m_pred = None
        if N == 0 and B_pred is not None and DELTA_H_DERIVED is None:
            delta_status = (
                "pending: B is derived but Δ requires m_p; m_p is "
                "derivation-pending — see derivation_inputs."
                "m_p_derivation_status"
            )
        elif N > 0 and B_pred is not None:
            delta_status = (
                "pending: B is derived (strategy A) but Δ requires m_n "
                "(and m_p); both are derivation-pending"
            )
        else:
            delta_status = (
                "pending: B is derivation-pending — see B_derivation_status"
            )

    if B_pred is None or delta_pred is None:
        row_status = "derivation_pending"
    else:
        row_status = "derived"

    return {
        "symbol": symbol,
        "Z": Z,
        "N": N,
        "A": A,
        "B_AME_MeV_ref": None,  # filled by caller from sweep table
        "B_pred_MeV": B_pred,
        "B_derivation_status": b_status,
        "delta_pred_MeV": delta_pred,
        "delta_derivation_status": delta_status,
        "M_pred_MeV": m_pred,
        "row_derivation_status": row_status,
    }


def main() -> int:
    print(f"\n  Substrate q_0 = {Q0:.6f}")
    print(f"  u = {U_MEV:.4f} MeV (CODATA, comparison ref)")
    if M_P_DERIVED_MEV is None:
        print(f"  m_p_derived = PENDING "
              f"(upstream rel_diff = {M_P_DERIVED_REL_DIFF:.3e} > "
              f"{M_P_DERIVED_MAX_REL_DIFF:.0e} chain-closed threshold)")
        print(f"    -> {M_P_DERIVATION_STATUS}")
    else:
        print(f"  m_p_derived = {M_P_DERIVED_MEV:.6f} MeV "
              f"(rel_diff vs CODATA = {M_P_DERIVED_REL_DIFF:.3e})")
    print(f"  m_n_derived = PENDING ({M_N_DERIVATION_STATUS[:60]}...)")
    delta_H_str = (
        f"{DELTA_H_DERIVED:.4f} MeV" if DELTA_H_DERIVED is not None
        else "PENDING (m_p pending)"
    )
    print(f"  Δ_H_derived = {delta_H_str},  Δ_n_derived = PENDING")
    print(f"  Q_β (codata)     = {Q_BETA_CODATA_MEV:.6f} MeV (CAL-3 default)")
    print(f"  Q_β (substrate)  = {Q_BETA_SUBSTRATE_MEV:.6f} MeV "
          f"(form_a_cos, residual {Q_BETA_SUBSTRATE_PPM:+.1f} ppm)\n")

    header = (
        f"  {'atom':>6} {'A':>3} "
        f"{'Δ_obs':>9} {'Δ_pred':>9} {'ΔΔ':>8}  "
        f"{'M_obs':>11} {'M_pred':>11}  status"
    )
    print(header)
    print("  " + "-" * (len(header) - 2))

    rows = []
    for symbol, Z, N, B_ame in AME:
        A = Z + N
        delta_obs = AME_DELTA.get(symbol)
        if delta_obs is None:
            continue

        row = predict_row(symbol, Z, N)
        row["B_AME_MeV_ref"] = float(B_ame)
        row["delta_obs_MeV_ref"] = float(delta_obs)

        # Reference-only total mass (AME, comparison anchor).
        M_obs = A * U_MEV + delta_obs
        row["M_obs_MeV_ref"] = M_obs

        # Residuals only when prediction exists.
        delta_pred = row["delta_pred_MeV"]
        if delta_pred is not None:
            ddelta = delta_pred - delta_obs
            row["delta_residual_MeV"] = ddelta
            M_pred = row["M_pred_MeV"]
            row["M_err_ppm"] = 1e6 * (M_pred - M_obs) / M_obs if M_obs > 0 else 0.0
            ddelta_str = f"{ddelta:>+8.3f}"
            mpred_str = f"{M_pred:>11.3f}"
        else:
            row["delta_residual_MeV"] = None
            row["M_err_ppm"] = None
            ddelta_str = f"{'pend':>8}"
            mpred_str = f"{'pending':>11}"

        delta_pred_str = (
            f"{delta_pred:>+9.3f}" if delta_pred is not None else f"{'pend':>9}"
        )
        print(
            f"  {symbol:>6} {A:>3} "
            f"{delta_obs:>+9.3f} {delta_pred_str} "
            f"{ddelta_str}  "
            f"{M_obs:>11.3f} {mpred_str}  {row['row_derivation_status']}"
        )

        rows.append(row)

    # Stats on Δ (mass excess) — derived rows only.
    derived_rows = [r for r in rows if r["row_derivation_status"] == "derived"]
    pending_rows = [r for r in rows if r["row_derivation_status"] != "derived"]

    delta_errs = [
        abs(r["delta_residual_MeV"])
        for r in derived_rows
        if r["delta_residual_MeV"] is not None and r["delta_obs_MeV_ref"] != 0
    ]
    mean_abs = sum(delta_errs) / len(delta_errs) if delta_errs else 0.0
    max_abs = max(delta_errs) if delta_errs else 0.0
    m_ppms = [
        abs(r["M_err_ppm"])
        for r in derived_rows
        if r["M_err_ppm"] is not None and r["M_obs_MeV_ref"] > 0
    ]
    print(
        f"\n  Δ (mass excess) stats over {len(derived_rows)} derived rows: "
        f"mean|ΔΔ|={mean_abs:.3f} MeV, max|ΔΔ|={max_abs:.3f} MeV"
    )
    if m_ppms:
        print(
            f"  M (total mass) stats:  mean|δM|={sum(m_ppms)/len(m_ppms):.1f} ppm, "
            f"max|δM|={max(m_ppms):.1f} ppm"
        )
    print(
        f"  {len(pending_rows)} rows DERIVATION_PENDING (m_n / B(⁴He+) "
        f"chains not yet fit-free)"
    )

    witness = {
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "name": "low-isotope-mass-table",
        "description": (
            "Low-isotope mass + mass-excess table (Z ≤ 10) from the "
            "categorical derivation chain. Predicted columns are emitted "
            "ONLY for rows whose every input (m_p, m_n, B) traces to a "
            "fit-free derivation rooted in q₀. Rows lacking such a chain "
            "(m_n MeV scale; B(⁴He) and beyond) are emitted with "
            "row_derivation_status='derivation_pending' and predicted "
            "values set to null. The framework consumes a small set of "
            "scale/unit CODATA constants (m_e MeV scale, atomic mass unit "
            "u) — these live in derivation_inputs.scale_constants. CODATA "
            "/ AME values used purely as comparison anchors (M_P_REF, "
            "M_N_REF, AME binding energies, AME mass excesses) live in "
            "comparison_only_constants and are never consumed in the "
            "predicted column."
        ),
        "auditOnly": "docs/audits/categorical-vs-fitted-q-decay-ba.md",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "derivation_inputs": {
            "m_p_derived_MeV": M_P_DERIVED_MEV,
            "m_p_derived_source": M_P_DERIVED_SOURCE,
            "m_p_derived_rel_diff_vs_codata": M_P_DERIVED_REL_DIFF,
            "m_p_derivation_status": M_P_DERIVATION_STATUS,
            "m_p_derived_max_rel_diff_threshold": M_P_DERIVED_MAX_REL_DIFF,
            "m_n_derivation_status": M_N_DERIVATION_STATUS,
            "B_4He_derivation_status": B_4HE_DERIVATION_STATUS,
            "delta_H_derived_MeV": DELTA_H_DERIVED,
            "delta_N_derivation_status": (
                "pending: requires derived m_n"
            ),
            "Q_beta_codata_MeV": Q_BETA_CODATA_MEV,
            "Q_beta_substrate_MeV": Q_BETA_SUBSTRATE_MEV,
            "Q_beta_substrate_source":
                "full_chain_n4 (PRs #661, #664, #665 + "
                "prop:kashiwara-jones-c4-categorical): "
                "Q_A · cos(α_N1) · (1−b²ℏ_q⁴) · (1−2b³ℏ_q⁶) · "
                "(1+(b²+½)b⁴ℏ_q⁸) — c_2, c_3, c_4 all categorical, "
                "cherry-picked from PR #664 (2026-05-17)",
            "Q_beta_substrate_residual_ppm_vs_codata":
                Q_BETA_SUBSTRATE_PPM,
            "Q_beta_form_a_cos_MeV":
                Q_BETA_FORM_A_COS_MEV,
            "Q_beta_form_a_cos_residual_ppm_vs_codata":
                Q_BETA_FORM_A_COS_PPM,
            "Q_beta_substrate_tightening_vs_form_a_cos":
                abs(Q_BETA_FORM_A_COS_PPM) / max(abs(Q_BETA_SUBSTRATE_PPM), 1e-12),
            "scale_constants": {
                # Scale / unit inputs consumed by the framework
                # (the same single CODATA-bounded constant the proton
                # derivation chain consumes — see
                # build_proton_mass_50dps_chain.py step 6 — plus the
                # atomic mass unit u for total-mass assembly).
                "M_E_MEV": M_E_MEV,
                "U_MEV": U_MEV,
                "q_0": Q0,
            },
            "upstream_witness_hashes": [
                # Anti-staleness infra: every upstream witness this
                # script consumed gets its sha256 + producer commit
                # recorded here. Future drift validator compares
                # current on-disk files to these recorded hashes.
                _proton_hash,
            ],
        },
        "comparison_only_constants": {
            "M_P_REF_MEV_codata": M_P_REF_MEV,
            "M_N_REF_MEV_codata": M_N_REF_MEV,
        },
        "rows": rows,
        "stats": {
            "n_rows_total": len(rows),
            "n_rows_derived": len(derived_rows),
            "n_rows_pending": len(pending_rows),
            "delta_mean_abs_MeV": mean_abs,
            "delta_max_abs_MeV": max_abs,
            "M_mean_abs_ppm": sum(m_ppms)/len(m_ppms) if m_ppms else None,
            "M_max_abs_ppm": max(m_ppms) if m_ppms else None,
        },
        "framework_refs": [
            "conj:mass-volume-factorization",
            "conj:crossing-graded-mass-expansion",
            "conj:lifted-crossing-locality",
        ],
        "dual_witness_refs": [
            "rho-k-h3a-lp-dual.witness.json",
            "rho-k-h3a-gg-trajectory.witness.json",
            "binding-k-solver.witness.json",
        ],
    }

    out_path = Path(__file__).parent / "low-isotope-mass-table.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\n  Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
