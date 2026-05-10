#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only Phase 1 mass-table wiring.
"""
Phase 1 of the 1 ppb workplan
([`docs/audits/2026-05-10-1ppb-workplan-update.md §Phase 1`](../../docs/audits/2026-05-10-1ppb-workplan-update.md))
— **wire `AppliedDeuteron/Tritium/Helium3Uniqueness` into mass-table
predictions** by consuming the canonical `tr_M(β_K, q_0)` values pinned
in `markov-trace-assembly-*.derivation.json` and applying the
`categoricalMass` formula proved in
[`QOU.BraidKnot.MassFormulaCategorical`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MassFormulaCategorical.lean):

    M(K) = ρ(K) · m_e · |tr_M(T_w(K))|        (cat units)
    M(K)_MeV = M(K)_cat · M_E_MEV_CODATA       (Lean theorem)

Subtle point — the `m_e` factor in the Lean formula is the **Hecke-
encoded** electron mass `m_e_Hecke`, not `M_E_MEV_CODATA`.  The
conversion to MeV via `M_E_MEV_CODATA` only makes sense if the formula
is rewritten as a **ratio**:

    m_K_predicted_MeV = (m_K_Hecke / m_e_Hecke) · M_E_MEV_CODATA
                      = (ρ_K · |tr_M(β_K)| / |tr_M(β_e)|) · M_E_MEV_CODATA
                                 ──────────────  ↑ assumes ρ_e = 1
                                 ratio of |tr_M|

Currently `m_e_Hecke` and the proton-side `m_p_Hecke` are placeholder
literals in `derivation_chain.M_HECKE_PIPELINE_AT_Q0` (the 544k ppb
defect — Phase 2 of the workplan).  This script therefore reports the
**categorical-formula prediction with the current placeholders**, and
exposes the gap vs CODATA / AME so Phase 2's substitution is auditable.

Output: `applied-uniqueness-mass-table.witness.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

mp.mp.dps = 50

from codata_constants import M_E_MEV as _M_E_MP, M_P_MEV as _M_P_MP, M_N_MEV as _M_N_MP
from witness_base import WitnessBuilder

M_E_MEV = _M_E_MP
M_P_MEV = _M_P_MP
M_N_MEV = _M_N_MP

ASSEMBLY_DIR = Path(__file__).parent

# ─── Canonical Wenzl-bridge |tr_M(β_K, q_0)| values ────────────────────
#
# Pinned in `markov-trace-assembly-{atom}.derivation.json` (target_value).
# These are the **canonical** values per `prop:y-lambda-closed-form-
# wenzl-bridge` — the legacy 2-variable Schur weight (which vanishes
# for ℓ(λ) > 2) was replaced in PR #621 + #630.
#
# T (³H) and ³He are not yet in the assembly-derivation chain (chi
# cache `chi-tritium-h9.witness.json` is partial: 2/30 partitions; ³He
# has no chi cache yet).  Phase 1.2/1.3 of the workplan wires those in
# once the cached witnesses complete.
PINNED_TR_M_Q0 = {
    "proton":   "1.0653062285923893",
    "neutron":  "0.9232332971695838",
    "deuteron": "0.3882864715477134",
}

PENDING_ATOMS = {
    "tritium": {
        "Z": 1, "N": 2, "A": 3,
        "blocker": "chi-tritium-h9.witness.json partial (2/30 partitions)",
        "next_step": "Run habiro_coefficients_atomic.py --atom T to "
                     "completion (~hours at H_9 with full Wenzl-bridge "
                     "y_λ); pin the result into "
                     "markov-trace-assembly-tritium.derivation.json.",
    },
    "helium3": {
        "Z": 2, "N": 1, "A": 3,
        "blocker": "no chi-helium3-h9.witness.json cache exists",
        "next_step": "Generate chi-helium3-h9.witness.json via "
                     "hecke_character_symbolic with σ⁻¹-aware character "
                     "chain; pin result into "
                     "markov-trace-assembly-helium3.derivation.json.",
    },
}

# Per-atom SDP multiplicities ρ(K), per `conj:rho-prefactor-structural`
# and the AppliedX-Uniqueness theorems.  Currently inherited from the
# legacy `mass_table_ppb.py` rho_factor field; matches the
# `bindingKUniqueness` proposition's rho fixture.
RHO = {
    "proton":   1,
    "neutron":  1,
    "deuteron": 1,
    "tritium":  2,
    "helium3":  2,
}

# AME baselines for binding-energy comparison (MeV).  Per
# `mass-table-ppb.witness.json`.
B_AME_MEV = {
    "deuteron": mp.mpf("2.22456612"),
    "tritium":  mp.mpf("8.4817984"),
    "helium3":  mp.mpf("7.7180375"),
    "helium4":  mp.mpf("28.2956912"),
}

# AME nucleus masses (MeV).  Computed below from
# m(K) = Z·m_p + N·m_n - B(K) where Z, N count protons + neutrons.
def ame_nucleus_mass_mev(Z: int, N: int, B_AME_MeV: mp.mpf) -> mp.mpf:
    """AME nucleus mass via mass-deficit identity."""
    return Z * M_P_MEV + N * M_N_MEV - B_AME_MeV


def categorical_mass_via_ratio(
    atom: str, tr_M_q0: mp.mpf, m_p_via_ratio: bool = True
) -> mp.mpf | None:
    """Apply the categorical mass formula at the level of ratios.

    `M(K)_MeV = (ρ_K · |tr_M(β_K)|) / (ρ_e · |tr_M(β_e)|) · M_E_MEV_CODATA`

    The electron-side ratio `ρ_e · |tr_M(β_e)|` is itself a derived
    quantity (Phase 2 of the workplan); currently we proxy it via the
    placeholder literal `M_HECKE_PIPELINE_AT_Q0['e']` so the formula's
    structure is exposed.  When that placeholder is replaced with the
    Path A 50-dps derivation of `m_e_Hecke` (Phase 2), the prediction
    will tighten by ~5 orders of magnitude.

    Returns `None` if the placeholder is not configured for the atom.
    """
    try:
        from derivation_chain import M_HECKE_PIPELINE_AT_Q0
    except ImportError:
        return None

    m_e_hecke_placeholder = mp.mpf(str(M_HECKE_PIPELINE_AT_Q0.get("e", 0)))
    if m_e_hecke_placeholder == 0:
        return None

    ratio = (RHO[atom] * tr_M_q0) / m_e_hecke_placeholder
    return ratio * M_E_MEV


def main() -> int:
    # WitnessBuilder up-front so durationMs reflects end-to-end runtime.
    w = WitnessBuilder("applied-uniqueness-mass-table", engine="mpmath")
    w.set_description(
        "Phase 1 of the 1 ppb workplan — wires AppliedDeuteron/Tritium/"
        "Helium3Uniqueness theorems into mass-table predictions by "
        "applying the categorical mass formula M(K) = ρ · m_e · |tr_M| "
        "from QOU.BraidKnot.MassFormulaCategorical to the canonical "
        "|tr_M(β_K, q_0)| values pinned in "
        "markov-trace-assembly-*.derivation.json.  Currently uses "
        "placeholder m_e_Hecke literal (Phase 2 of the workplan replaces "
        "it with the Path A 50-dps derivation, expected to tighten "
        "predictions by ~5 orders of magnitude)."
    )
    w.set_content_block("prop:atom-knot-mass-derivation")

    # Load pinned tr_M values + assembly metadata.
    tr_M = {}
    sources = {}
    for atom, val_str in PINNED_TR_M_Q0.items():
        path = ASSEMBLY_DIR / f"markov-trace-assembly-{atom}.derivation.json"
        if path.exists():
            d = json.loads(path.read_text())
            sources[atom] = {
                "path": str(path.relative_to(ASSEMBLY_DIR.parent.parent)),
                "target": d.get("target", ""),
                "target_value": d.get("target_value", val_str),
            }
            tr_M[atom] = mp.mpf(str(d.get("target_value", val_str)))
        else:
            sources[atom] = {"path": None, "fallback": val_str}
            tr_M[atom] = mp.mpf(val_str)

    print("=" * 80)
    print("PHASE 1 — APPLIED UNIQUENESS MASS TABLE")
    print("Categorical formula M(K) = ρ · m_e · |tr_M(β_K)| applied to")
    print("canonical Wenzl-bridge |tr_M(β_K, q_0)| values.")
    print("=" * 80)
    print()
    print(f"  m_e (CODATA, 50 dps) = {mp.nstr(M_E_MEV, 12)} MeV")
    print(f"  m_p (CODATA, 50 dps) = {mp.nstr(M_P_MEV, 12)} MeV")
    print(f"  m_n (CODATA, 50 dps) = {mp.nstr(M_N_MEV, 12)} MeV")
    print()

    print(f"{'atom':>10} {'ρ':>3}  {'|tr_M(β_K, q_0)|':>22}  source")
    for atom, val in tr_M.items():
        src = sources[atom].get("path", "fallback") or "fallback"
        src_short = Path(src).name if src != "fallback" else src
        print(f"  {atom:>8} {RHO[atom]:>3}  {mp.nstr(val, 18):>22}  {src_short}")
    print()

    # Apply the categorical mass formula via ratios; report m_K_predicted
    # vs CODATA / AME m_K.
    print(f"{'atom':>10}  {'m_K_pred (MeV)':>16}  {'m_K_AME (MeV)':>16}  "
          f"{'err_ppb':>14}  formula")
    rows = []
    for atom in ("proton", "neutron", "deuteron"):
        m_pred = categorical_mass_via_ratio(atom, tr_M[atom])
        if atom == "proton":
            m_ref = M_P_MEV
            ame_label = "CODATA m_p"
        elif atom == "neutron":
            m_ref = M_N_MEV
            ame_label = "CODATA m_n"
        else:  # deuteron
            m_ref = ame_nucleus_mass_mev(1, 1, B_AME_MEV["deuteron"])
            ame_label = "AME m_D"
        if m_pred is None:
            print(f"  {atom:>8}  (placeholder m_e_Hecke missing)")
            continue
        err_ppb = float((m_pred - m_ref) / m_ref * mp.mpf("1e9"))
        formula = f"ρ_{atom[0]} · |tr_M(β_{atom[0]})| / m_e_Hecke_placeholder · M_E_MEV"
        rows.append({
            "atom": atom,
            "Z": {"proton": 1, "neutron": 0, "deuteron": 1}[atom],
            "N": {"proton": 0, "neutron": 1, "deuteron": 1}[atom],
            "rho": RHO[atom],
            "tr_M_q0": str(tr_M[atom]),
            "m_K_predicted_MeV": str(m_pred),
            "m_K_reference_MeV": str(m_ref),
            "reference_label": ame_label,
            "err_ppb": err_ppb,
            "formula": formula,
            "status": "categorical_via_placeholder_m_e_Hecke",
        })
        print(f"  {atom:>8}  {mp.nstr(m_pred, 12):>16}  "
              f"{mp.nstr(m_ref, 12):>16}  {err_ppb:>+14.2e}  "
              f"{formula}")

    print()
    print("PENDING (Phase 1.2 / 1.3):")
    for atom, info in PENDING_ATOMS.items():
        print(f"  {atom}: {info['blocker']}")
        rows.append({
            "atom": atom,
            "Z": info["Z"], "N": info["N"], "A": info["A"],
            "rho": RHO[atom],
            "tr_M_q0": None,
            "status": "pending",
            "blocker": info["blocker"],
            "next_step": info["next_step"],
        })

    # Binding-energy translation for the deuteron — diff vs AME baseline.
    if rows and rows[0]["atom"] == "proton":
        # Need predicted m_p, m_n, m_D to compute B(D)_pred.
        try:
            m_p_pred = mp.mpf(rows[0]["m_K_predicted_MeV"])
            m_n_pred = mp.mpf(rows[1]["m_K_predicted_MeV"])
            m_D_pred = mp.mpf(rows[2]["m_K_predicted_MeV"])
            B_D_pred = m_p_pred + m_n_pred - m_D_pred
            B_D_ame = B_AME_MEV["deuteron"]
            B_D_err_ppb = float((B_D_pred - B_D_ame) / B_D_ame * mp.mpf("1e9"))
            print()
            print(f"{'B(D) translated':>18}: {mp.nstr(B_D_pred, 12)} MeV  "
                  f"(AME: {mp.nstr(B_D_ame, 12)} MeV, err: {B_D_err_ppb:+.2e} ppb)")
            rows.append({
                "atom": "deuteron-binding",
                "B_predicted_MeV": str(B_D_pred),
                "B_AME_MeV": str(B_D_ame),
                "err_ppb": B_D_err_ppb,
                "formula": "m_p_pred + m_n_pred - m_D_pred",
                "status": "categorical_via_placeholder_m_e_Hecke",
            })
        except (IndexError, KeyError, ValueError):
            pass

    w.add_parameter("M_E_MEV_CODATA", str(M_E_MEV))
    w.add_parameter("M_P_MEV_CODATA", str(M_P_MEV))
    w.add_parameter("M_N_MEV_CODATA", str(M_N_MEV))
    w.add_parameter("rho_table", RHO)
    w.add_data("pinned_tr_M_q0", PINNED_TR_M_Q0)
    w.add_data("sources", sources)
    w.add_data("rows", rows)
    w.add_data("pending_atoms", PENDING_ATOMS)
    w.add_data("phase", "Phase 1 of 1ppb workplan (2026-05-10)")
    w.add_data("workplan_doc", "docs/audits/2026-05-10-1ppb-workplan-update.md")
    w.add_data("lean_theorem", "QOU.BraidKnot.MassFormulaCategorical.categoricalMassMeV")
    w.add_data("formula_in_lean",
               "categoricalMass rho m_e T_w := rho * m_e * absMarkovTrace n T_w")
    w.add_data("phase_2_note",
               "Predictions consume placeholder m_e_Hecke literal "
               "(M_HECKE_PIPELINE_AT_Q0['e'] in derivation_chain.py); "
               "Phase 2 replaces this with Path A 50-dps derivation, "
               "expected to tighten by ~5 orders of magnitude.")

    # Schematic assertions: predictions are all finite + non-negative.
    finite = all(
        r.get("m_K_predicted_MeV") is None or
        mp.isfinite(mp.mpf(r["m_K_predicted_MeV"]))
        for r in rows
    )
    w.add_assertion("all_predictions_finite", computed=finite, expected=True)
    nonneg = all(
        r.get("m_K_predicted_MeV") is None or
        mp.mpf(r["m_K_predicted_MeV"]) >= 0
        for r in rows
    )
    w.add_assertion("all_predictions_nonneg", computed=nonneg, expected=True)

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
