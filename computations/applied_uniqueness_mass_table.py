#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only Phase 1 mass-table wiring.
"""
CLASS-A acknowledged-anchor (Workplan-0b): M_P/M_N_MEV_VALIDATION here build
the AME comparison REFERENCE (`ame_nucleus_mass_mev = Z·m_p + N·m_n − B_AME`
and the `m_ref` CODATA targets), never a prediction input. Verified
2026-06-17 (I11 adjudication).

═══════════════════════════════════════════════════════════════════
PARALLEL CHAIN (2026-05-23): not a consumer of the substrate
flavor-split.

This script predicts m_p AND m_n INDEPENDENTLY via the per-particle
`categoricalMass` formula `M(K) = ρ(K) · m_e · |tr_M(T_w(K))|`,
with each particle's prediction from its OWN ρ and |tr_M(β)|.
The proton-neutron mass difference falls out as a *side-effect*
of the independent ρ values + per-particle Markov traces; it is
NOT derived from a substrate flavor-split.

The substrate-pure flavor-split production chain (PR #942) uses:
  - `m_p_borromean_verification_50dps.py`   (production)
  - `_li_2_q_util.flavor_split_subleading`  (PR #690 / #942)

Cross-comparison between the two chains is a research-grade audit;
this script's per-particle approach is complementary to (not
replaced by) the borromean-tower + flavor-split production
prediction.
═══════════════════════════════════════════════════════════════════

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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

from _precision import set_compute_dps, fmt
set_compute_dps()  # mp.mp.dps via QOU_COMPUTE_DPS (default 50)
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION  # noqa: E402
from witness_base import WitnessBuilder

ASSEMBLY_DIR = Path(__file__).parent

# ─── Canonical Wenzl-bridge |tr_M(β_K, q_0)| values ────────────────────
#
# Imported from `derivation_chain.TR_M_AT_Q0` — the single source of
# truth for these literals (per Copilot review on PR #631; keeps JSON
# outputs bit-stable across consumers).
#
# Per `prop:y-lambda-closed-form-wenzl-bridge`, these are the canonical
# values; the legacy 2-variable Schur weight (which vanishes for
# ℓ(λ) > 2) was replaced in PR #621 + #630.
#
# T (³H) and ³He are not yet in `TR_M_AT_Q0` upstream — chi cache
# `chi-tritium-h9.witness.json` is partial (2/30 partitions); ³He has
# no chi cache yet.  Phase 1.2/1.3 of the workplan wires those in once
# the caches complete.
from derivation_chain import TR_M_AT_Q0  # canonical Wenzl-bridge values

# Local map: full atom name → 1-letter key used in TR_M_AT_Q0.
_ATOM_KEY = {"proton": "p", "neutron": "n", "deuteron": "D"}

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
        "blocker": "chi-helium-3-h9.witness.json partial (3/30 partitions)",
        "next_step": "Resume hecke_character_symbolic on the σ⁻¹-aware "
                     "helium-3 braid (uud) to complete the chi cache; "
                     "pin result into markov-trace-assembly-helium3.derivation.json.",
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
    "deuteron": AME_B_DEUTERON_MEV_VALIDATION,
    "tritium":  AME_B_TRITIUM_MEV_VALIDATION,
    "helium3":  AME_B_HE3_MEV_VALIDATION,
    "helium4":  AME_B_HE4_MEV_VALIDATION,
}

# AME nucleus masses (MeV).  Computed below from
# m(K) = Z·m_p + N·m_n - B(K) where Z, N count protons + neutrons.
def ame_nucleus_mass_mev(Z: int, N: int, B_AME_MeV: mp.mpf) -> mp.mpf:
    """AME nucleus mass via mass-deficit identity."""
    return Z * M_P_MEV_VALIDATION + N * M_N_MEV_VALIDATION - B_AME_MeV


def categorical_mass_via_ratio(
    atom: str, tr_M_q0: mp.mpf
) -> mp.mpf | None:
    """Apply the categorical mass formula `M(K) = ρ · m_e · |tr_M(T_w(K))|`
    proved in `QOU.BraidKnot.MassFormulaCategorical`, expressed at the
    level of ratios so the cat-units `m_e_Hecke` cancels with itself:

        m_K_MeV = (ρ_K · |tr_M(β_K)|) / m_e_Hecke · M_E_MEV_CODATA

    The denominator `m_e_Hecke` is the Hecke-encoded electron mass; in
    the Lean theorem it is the `m_e` factor multiplying `absMarkovTrace`.
    For the proton/neutron/deuteron-side ratio numerator, the same factor
    of `m_e_Hecke` would appear and cancel; we therefore divide by it
    once on the denominator and consume `M_E_MEV_CODATA` once on the
    numerator side, matching the cat-units → MeV conversion in
    `categoricalMassMeV` from the Lean module.

    The denominator is currently the **placeholder literal**
    `M_HECKE_PIPELINE_AT_Q0['e']` from `derivation_chain.py` (marked
    DEPRECATED there); Phase 2 of the workplan replaces it with the
    Path A 50-dps derivation of `m_e_Hecke`, expected to tighten the
    predictions by ~5 orders of magnitude.

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
    # Audit-only: consumes `derivation_chain.M_HECKE_PIPELINE_AT_Q0['e']`
    # which is marked DEPRECATED upstream ("DO NOT ADD NEW PRODUCTION
    # CONSUMERS").  Phase 2 of the workplan removes the placeholder
    # dependency; until then this script is a Phase 1 scaffolding
    # diagnostic, not a production prediction.  Per Copilot review on
    # PR #631.
    w.set_audit_only("docs/audits/2026-05-10-1ppb-workplan-update.md")
    w.set_description(
        "Phase 1 of the 1 ppb workplan — wires AppliedDeuteron/Tritium/"
        "Helium3Uniqueness theorems into mass-table predictions by "
        "applying the categorical mass formula M(K) = ρ · m_e · |tr_M| "
        "from QOU.BraidKnot.MassFormulaCategorical to the canonical "
        "|tr_M(β_K, q_0)| values from derivation_chain.TR_M_AT_Q0.  "
        "Currently uses placeholder m_e_Hecke literal (DEPRECATED in "
        "derivation_chain.py); Phase 2 of the workplan replaces it "
        "with the Path A 50-dps derivation, expected to tighten "
        "predictions by ~5 orders of magnitude.  AUDIT-ONLY scaffolding."
    )
    w.set_content_block("prop:atom-knot-mass-derivation")

    # Load canonical tr_M values from derivation_chain.TR_M_AT_Q0
    # (the single source of truth) + per-atom assembly metadata.
    tr_M = {}
    sources = {}
    for atom, key in _ATOM_KEY.items():
        if key not in TR_M_AT_Q0:
            continue
        canonical_val = mp.mpf(str(TR_M_AT_Q0[key]))
        path = ASSEMBLY_DIR / f"markov-trace-assembly-{atom}.derivation.json"
        if path.exists():
            d = json.loads(path.read_text())
            sources[atom] = {
                "path": str(path.relative_to(ASSEMBLY_DIR.parent.parent)),
                "target": d.get("target", ""),
                "target_value": d.get("target_value", str(canonical_val)),
                "canonical_source": "derivation_chain.TR_M_AT_Q0",
            }
            tr_M[atom] = mp.mpf(str(d.get("target_value", canonical_val)))
        else:
            sources[atom] = {
                "path": None,
                "canonical_source": "derivation_chain.TR_M_AT_Q0",
            }
            tr_M[atom] = canonical_val

    print("=" * 80)
    print("PHASE 1 — APPLIED UNIQUENESS MASS TABLE")
    print("Categorical formula M(K) = ρ · m_e · |tr_M(β_K)| applied to")
    print("canonical Wenzl-bridge |tr_M(β_K, q_0)| values.")
    print("=" * 80)
    print()
    print(f"  m_e (CODATA, 50 dps) = {mp.nstr(M_E_MEV, 12)} MeV")
    print(f"  m_p (CODATA, 50 dps) = {mp.nstr(M_P_MEV_VALIDATION, 12)} MeV")
    print(f"  m_n (CODATA, 50 dps) = {mp.nstr(M_N_MEV_VALIDATION, 12)} MeV")
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
            m_ref = M_P_MEV_VALIDATION
            ame_label = "CODATA m_p"
        elif atom == "neutron":
            m_ref = M_N_MEV_VALIDATION
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
            "tr_M_q0": fmt(tr_M[atom]),
            "m_K_predicted_MeV": fmt(m_pred),
            "m_K_reference_MeV": fmt(m_ref),
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

    # Binding-energy translation for the deuteron — diff vs AME
    # baseline.  Index by atom name (per Copilot review on PR #631);
    # robust against loop-order changes or pending/skipped rows.
    rows_by_atom = {r["atom"]: r for r in rows if "atom" in r}
    needed = ("proton", "neutron", "deuteron")
    if all(a in rows_by_atom and "m_K_predicted_MeV" in rows_by_atom[a]
           for a in needed):
        m_p_pred = mp.mpf(rows_by_atom["proton"]["m_K_predicted_MeV"])
        m_n_pred = mp.mpf(rows_by_atom["neutron"]["m_K_predicted_MeV"])
        m_D_pred = mp.mpf(rows_by_atom["deuteron"]["m_K_predicted_MeV"])
        B_D_pred = m_p_pred + m_n_pred - m_D_pred
        B_D_ame = B_AME_MEV["deuteron"]
        B_D_err_ppb = float((B_D_pred - B_D_ame) / B_D_ame * mp.mpf("1e9"))
        print()
        print(f"{'B(D) translated':>18}: {mp.nstr(B_D_pred, 12)} MeV  "
              f"(AME: {mp.nstr(B_D_ame, 12)} MeV, err: {B_D_err_ppb:+.2e} ppb)")
        rows.append({
            "atom": "deuteron-binding",
            "B_predicted_MeV": fmt(B_D_pred),
            "B_AME_MeV": fmt(B_D_ame),
            "err_ppb": B_D_err_ppb,
            "formula": "m_p_pred + m_n_pred - m_D_pred",
            "status": "categorical_via_placeholder_m_e_Hecke",
        })

    w.add_parameter("M_E_MEV_CODATA", str(M_E_MEV))
    w.add_parameter("M_P_MEV_CODATA", str(M_P_MEV_VALIDATION))
    w.add_parameter("M_N_MEV_CODATA", str(M_N_MEV_VALIDATION))
    w.add_parameter("rho_table", RHO)
    w.add_data("canonical_tr_M_q0_source", "derivation_chain.TR_M_AT_Q0")
    w.add_data("canonical_tr_M_q0_values",
               {atom: str(tr_M[atom]) for atom in tr_M})
    w.add_data("sources", sources)
    w.add_data("rows", rows)
    w.add_data("pending_atoms", PENDING_ATOMS)
    w.add_data("phase", "Phase 1 of 1ppb workplan (2026-05-10)")
    w.add_data("workplan_doc", "docs/audits/2026-05-10-1ppb-workplan-update.md")
    w.add_data("lean_theorem",
               "QOU.BraidKnot.MassFormulaCategorical.categoricalMassMeV")
    w.add_data("formula_in_lean",
               "categoricalMass rho m_e T_w := rho * m_e * absMarkovTrace n T_w")
    w.add_data("formula_used_here",
               "M(K)_MeV = (ρ_K · |tr_M(β_K, q_0)|) / m_e_Hecke_placeholder "
               "· M_E_MEV_CODATA — ratio form so cat-units m_e cancels; "
               "the numerator's (m_e * |tr_M|) is implicit in the |tr_M|·"
               "(M_E_MEV/m_e_Hecke) reshuffle.")
    w.add_data("phase_2_note",
               "Predictions consume placeholder m_e_Hecke literal "
               "(M_HECKE_PIPELINE_AT_Q0['e'] in derivation_chain.py, "
               "marked DEPRECATED upstream).  Phase 2 replaces this with "
               "Path A 50-dps derivation; expected to tighten by ~5 "
               "orders of magnitude.  This script is set_audit_only "
               "until that substitution lands.")

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
