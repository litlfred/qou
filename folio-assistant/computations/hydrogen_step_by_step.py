"""
hydrogen_step_by_step.py — full per-term decomposition of m(¹H)

Walks every term of the canonical 6-term mass tower for ¹H
(= 1 proton + 1 electron, bound by ~13.6 eV) under the
post-2026-05-03 paper-canonical convention (symmetric Li_2^q
brane-tower per `prop:mass-endomorphism-tower`).

Goal: produce a single witness JSON listing every input, every
term, every gap, and the cumulative error vs CODATA m(¹H).

Convention summary (paper canon, NOT Faddeev):

    m(β) = |Π V̂_i^full|
         − Σ_i     Li_2^q(−|V̂_i^full|)
         − Σ_{i<j} z² · Li_2^q(−|V̂_i V̂_j|)
         + T4 (Frobenius co-Casimir)
         + T5 (chirality / Burnside–Wedderburn at A_max_grade)
         + T6 (Habiro residue, A_nucleon-keyed)
         + T7 (σ-shell α_5 · S_crystal, A≥2 only)

  z         = 1/(q^{1/2} + q^{-1/2})              Markov parameter
  [n]_q     = (q^n − q^{-n})/(q − q^{-1})        symmetric q-int
  Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q)          symmetric q-dilog

m(¹H) = m_p_pred + m_e_anchor − BE(¹H_atomic)
      = m_p_pred + 0.511 MeV (exact)  − 13.6 eV (negligible vs MeV)

So the residual error is dominated entirely by the m_p_pred
prediction (electron is calibration-anchored).

Outputs `hydrogen-step-by-step.witness.json` with every
intermediate value at 50-digit MPFR precision.

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
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

from mpmath import mp, mpf

# Reuse the production chain — DO NOT recompute upstream.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from _li_2_q_util import li_2_q as Li_2_q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV as _M_E_MEV, M_P_MEV_VALIDATION  # noqa: E402

set_compute_dps()

# P31 compliance: M_E_MEV and M_P imported from codata_constants (single
# source of truth).  M_H is the ¹H atomic mass and is not in the canonical
# CODATA validation set — kept as a local mpf literal.
M_E_MEV = mpf(str(_M_E_MEV))
M_P_CODATA_MEV = mpf(str(M_P_MEV_VALIDATION))
M_H_CODATA_MEV = mpf("938.7830731")  # CODATA m(¹H_atomic), 2018
BE_H_EV = mpf("13.605693")  # ¹H ionisation energy
BE_H_MEV = BE_H_EV * mpf("1e-6")

PROTON_TOWER = _pb.witness_path("proton-mass-full-tower-50dps.witness.json", HERE)
Q_WITNESS_PATH = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)


def main() -> int:
    if not PROTON_TOWER.exists():
        print(f"  ERROR: missing {PROTON_TOWER.name}")
        print(f"  run derive_m_p_hecke_full_tower_50dps.py first")
        return 1

    # P31 / centralization (gemini #663): use WitnessBuilder.add_upstream
    # to load each upstream witness and record its hash in a single call,
    # replacing the previous private _load helper that bypassed the
    # anti-staleness infrastructure.
    w = (WitnessBuilder("hydrogen-step-by-step", engine="python+mpmath")
         .set_description("Full ¹H mass step-by-step under canonical Li_2^q tower"))
    tower = w.add_upstream(PROTON_TOWER)
    q_wit = w.add_upstream(Q_WITNESS_PATH)
    p = tower["data"]["particles"]["proton"]

    q_str = q_wit["derived_50_digit"]["q"]
    q = mpf(q_str)
    print("=" * 76)
    print("  Hydrogen (¹H) step-by-step mass trace — canonical-form tower")
    print("=" * 76)
    print()
    print(f"  Substrate pin   q_0       = {mp.nstr(q, 20)}")
    print(f"  Markov param    z         = {mp.nstr(mpf(1) / (mp.sqrt(q) + mp.sqrt(mpf(1)/q)), 20)}")
    print(f"  Electron mass   m_e       = {M_E_MEV} MeV (CODATA, anchor)")
    print(f"  ¹H ionisation   BE        = {BE_H_EV} eV (≪ MeV — neglected)")
    print()

    # === Proton terms ===
    print("  PROTON terms (cat-units = ratios to m_e):")
    print("  " + "-" * 70)
    t1 = mpf(p["T1_descended_50dps"])
    t2 = mpf(p["T2_single_Li2q_50dps"])
    t3 = mpf(p["T3_pair_Li2q_50dps"])
    t4 = mpf(p["T4_Frobenius_50dps"])
    t5 = mpf(p["T5_chirality_BW_50dps_cat_units"])
    t6 = mpf(p["T6_Habiro_residue_50dps_cat_units"])
    t7 = mpf(0)  # A=1 nucleon — T7 σ-shell not in producer (no pure-Artin chain)
    m_hecke = t1 + t2 + t3 + t4 + t5 + t6 + t7
    m_p_pred = m_hecke * M_E_MEV

    rows = [
        ("T1  descended           |Π V̂_i|", t1, "Markov trace of product chain (positive)"),
        ("T2  single-brane Li_2^q  − Σ Li_2^q(−|V̂_i|)", t2, "negative-argument symmetric q-dilog, alternating series"),
        ("T3  pair-brane Li_2^q    − z² Σ Li_2^q(−|V̂_i V̂_j|)", t3, "all-pairs (Markov peel ⇒ z² for every i<j)"),
        ("T4  Frobenius co-Casimir              ", t4, "Sym² + alt² q-integers, derived"),
        ("T5  chirality / BW at A_max_grade=2   ", t5, "Burnside–Wedderburn at categorical A (no nucleon ledger)"),
        ("T6  Habiro residue at A_nucleon=1     ", t6, "non-zero roots-of-unity sum (paper-canonical)"),
        ("T7  σ-shell α_5 · S_crystal           ", t7, "GAP: A=1 not in producer (no pure-Artin word for nucleon)"),
    ]
    cumulative = mpf(0)
    for name, val, note in rows:
        cumulative += val
        in_MeV = val * M_E_MEV
        print(f"  {name:<48} {mp.nstr(val, 12):>16} (cum {mp.nstr(cumulative, 12):>14}, +{mp.nstr(in_MeV, 10)} MeV)")
        print(f"      {note}")
    print("  " + "-" * 70)
    print(f"  m_hecke (cat)  = {mp.nstr(m_hecke, 14)}")
    print(f"  m_p_pred       = {mp.nstr(m_p_pred, 12)} MeV   (CODATA {M_P_CODATA_MEV} MeV)")
    pp_residual = (m_p_pred - M_P_CODATA_MEV) / M_P_CODATA_MEV * 100
    print(f"  m_p residual   = {mp.nstr(pp_residual, 8)} %   ({mp.nstr(pp_residual * 10000, 8)} ppm)")
    print()

    # === Electron ===
    print("  ELECTRON: anchored — m_e = 0.51099895069 MeV exactly (CALIBRATION)")
    print()

    # === ¹H total ===
    m_H_pred = m_p_pred + M_E_MEV - BE_H_MEV
    h_residual_MeV = m_H_pred - M_H_CODATA_MEV
    h_residual_pct = (m_H_pred - M_H_CODATA_MEV) / M_H_CODATA_MEV * 100

    print(f"  m(¹H) prediction = m_p_pred + m_e − BE")
    print(f"                  = {mp.nstr(m_p_pred, 8)} + {M_E_MEV} − {mp.nstr(BE_H_MEV, 6)}")
    print(f"                  = {mp.nstr(m_H_pred, 10)} MeV")
    print(f"  CODATA m(¹H)    = {M_H_CODATA_MEV} MeV")
    print(f"  Δ_abs           = {mp.nstr(h_residual_MeV, 10)} MeV")
    print(f"  Δ_rel           = {mp.nstr(h_residual_pct, 8)} % ({mp.nstr(h_residual_pct * 10000, 6)} ppm)")
    print()

    # === Gap accounting ===
    print("  GAP ACCOUNTING — where the 99 % m_p error comes from:")
    print("  " + "-" * 70)
    gap_MeV = M_P_CODATA_MEV - m_p_pred
    print(f"  Total m_p shortfall  : {mp.nstr(gap_MeV, 10)} MeV")
    print(f"  T7 (A=1 σ-shell)     : NOT IMPLEMENTED — proton's Hecke-")
    print(f"                         coefficient chain ≠ pure-Artin word;")
    print(f"                         estimated magnitude < 10 MeV by")
    print(f"                         |α_5 · S_crystal| scaling from A=2")
    print(f"  T8+ (higher-loop)    : NOT IMPLEMENTED — pre-2026-05 the tower")
    print(f"                         was truncated at T6; revision plan")
    print(f"                         pending (see audit INDEX GAP #19/#22).")
    print(f"  Convention-mismatch  : V̂_i computation in")
    print(f"                         additive_wedderburn_volumes mirrors")
    print(f"                         mass_endomorphism.py — a chain matched")
    print(f"                         to the now-retired Faddeev Φ_q form.")
    print(f"                         Under Li_2^q the V̂_i values may need")
    print(f"                         re-derivation to give correct magnitudes.")
    print(f"  Faddeev-pole artifact: PRE-revision T2 was ~10^6 cat-units for")
    print(f"                         proton (|V̂|=0.989 near Φ_q's pole at q^{{-1}}=0.901)")
    print(f"                         giving spurious 1.50%; the canonical form")
    print(f"                         is finite (T2≈1.6) but at the wrong scale.")
    print()

    # === Witness emission ===
    # WitnessBuilder w was created at top of main() so add_upstream could
    # record the upstream hashes alongside the data load.
    w.add_data("convention", "paper canonical (Li_2^q, 2026-05-03 revision)")
    w.add_data("q_pinned", q_str)
    w.add_data("m_e_MeV_anchor", str(M_E_MEV))
    w.add_data("BE_H_MeV", str(BE_H_MEV))
    w.add_data("proton_terms_cat_units", {
        "T1_descended":            str(t1),
        "T2_single_Li2q":          str(t2),
        "T3_pair_Li2q":            str(t3),
        "T4_Frobenius":            str(t4),
        "T5_chirality_BW_A_grade": str(t5),
        "T6_Habiro_A_nucleon":     str(t6),
        "T7_sigma_shell":          str(t7),
        "m_hecke_sum":             str(m_hecke),
    })
    w.add_data("predictions_MeV", {
        "m_p_pred":     str(m_p_pred),
        "m_p_CODATA":   str(M_P_CODATA_MEV),
        "m_p_residual_pct": str(pp_residual),
        "m_H_pred":     str(m_H_pred),
        "m_H_CODATA":   str(M_H_CODATA_MEV),
        "m_H_residual_MeV": str(h_residual_MeV),
        "m_H_residual_pct": str(h_residual_pct),
    })
    w.add_data("gap_inventory", [
        {"name": "T7_A1_not_implemented",
         "kind": "missing_term",
         "estimated_max_magnitude_MeV": "≲ 10 (by |α_5·S_crystal| scaling from A=2)",
         "doc": "term7_alpha5_crystal_derivation covers A∈{2,3,4} only; A=1 atoms not added"},
        {"name": "T8_plus_higher_loop",
         "kind": "missing_term",
         "doc": "tower truncation at T6 pre-2026-05; T7+T8 design pending"},
        {"name": "V_hat_i_convention_mismatch",
         "kind": "structural",
         "doc": "additive_wedderburn_volumes was tuned to Faddeev Φ_q (now retired); Li_2^q may need re-derived V̂_i"},
        {"name": "Faddeev_pole_artifact_pre_revision",
         "kind": "documented_now_resolved",
         "doc": "previous 1.50% closure was T2≈1M cat-units from Φ_q near-pole at |V̂|=0.989 > q^{-1}=0.901; Li_2^q gives finite T2≈1.6"},
    ])
    w.add_assertion("li_2_q_finite_proton",
                    computed=1.0 if mp.isfinite(t2) else 0.0,
                    expected=1.0)
    w.add_assertion("m_p_pred_honest_gap_above_50pct",
                    computed=1.0 if mp.fabs(pp_residual) > 50 else 0.0,
                    expected=1.0)

    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
