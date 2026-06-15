#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical diagnostic only.
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

Neutron −8.3% error decomposition (Phase 1.7 / Strategy-3 frontier).

Per audit `docs/audits/2026-05-09-proton-m_e-anomaly.md §9.5`,
Strategy-3 (`atomic_braid_mass_table.py`) calibrates E_0 against the
proton (M_pred[p] = CODATA[p] by construction) and predicts the
neutron at M_pred[n] = 861.3 MeV vs CODATA 939.6 — an −8.325% gap.

This script decomposes the gap component-by-component to localise its
structural origin.

Findings (from `atomic-braid-mass-table.witness.json`):

  Component (cat units)        | proton    | neutron   | diff
  ─────────────────────────────|───────────|───────────|──────
  T1 = |tr_M_atomic|           | 1.6332    | 1.2483    | -0.3849 (-23.6%)
  T1 factor: a(Z,N) Δ_I        | 1.0       | 1.0       | (none)
  T1 factor: full-twist Δ_n²   | 1.0       | 1.0       | (none)
  T2 = z² · brane (single)     | 0.4986    | 0.4986    | identical
  T3 = z⁴ · brane (pair)       | 0.0622    | 0.0622    | identical
  T4 = Frobenius co-Casimir    | 2.4973    | 2.4973    | identical
  T6 = cyclotomic tail (MeV)   | 0.6807    | 0.6807    | identical
  total_hecke = T1+T2+T3+T4    | 4.6912    | 4.3063    | -0.3849

  E_0 (proton-calibrated)        = 199.86 MeV/cat-unit
  M_pred[p] = E_0·4.6912 + 0.6807 = 938.272 MeV  (= CODATA, by construction)
  M_pred[n] = E_0·4.3063 + 0.6807 = 861.345 MeV  (CODATA: 939.565)
  gap                            = -78.22 MeV   (8.325%)

The −8.3% neutron error is therefore localised **entirely to the
T1 factor `|tr_M_atomic|`**.  All other Strategy-3 components
(T2, T3, T4, T6, a(Z,N), Δ_n²) are identical between proton and
neutron at A=1.

Root cause:

  proton (uud) braid encoding:
    gen 0: 3·σ₀ (B₃) + 1·σ₀ (uu pair) + ½(σ₀+σ₀⁻¹) (ud pair) + 2·σ₀ (gluon)
    gen 1: 3·σ₁⁻¹ (B₃) + ½(σ₁+σ₁⁻¹) (ud pair)

  neutron (udd) braid encoding:
    gen 0: 3·σ₀ (B₃) + ½(σ₀+σ₀⁻¹) × 2 (ud pairs) + 2·σ₀ (gluon)
    gen 1: 3·σ₁⁻¹ (B₃) + 1·σ₁⁻¹ (dd pair)

The asymmetry: proton has `uu → σ` on gen 0 and `ud → ½(σ+σ⁻¹)` on
gen 1; neutron has `dd → σ⁻¹` on gen 1 and `ud → ½(σ+σ⁻¹)` × 2 on
gen 0.  The σ vs σ⁻¹ asymmetry at q ≠ 1 (eigenvalues {q, −q⁻¹} vs
{q⁻¹, −q}) produces a per-swap trace ratio of order q² / q⁻² ≈ q⁴
≈ 1.52 at q₀ ≈ 1.11.  Compounded across the multiple σ↔σ⁻¹ swaps
between the two encodings, this yields the observed 30% trace gap.

But the **physical** m_n − m_p splitting is only **1.293 MeV**
(0.14% of m_p), comprising:
  · Electromagnetic self-energy:  ≈ +0.76 MeV (proton has charge)
  · Quark mass difference:        ≈ +2.05 MeV (m_d − m_u ≈ 2.5 MeV)
  · Net (with sign cancellations): +1.29 MeV

So the framework's encoding over-predicts the proton-neutron mass
splitting by a factor of **~60**.  The encoding would need either:

  (a) A symmetry constraint that makes ud and du encodings produce
      the same trace contribution, AND uu / dd encodings differ only
      by a small isospin-symmetry-breaking term;

  (b) Separate the strong-force (large, isospin-symmetric) and
      isospin-symmetry-breaking (small) contributions, and only use
      the latter to predict the m_n − m_p splitting; OR

  (c) A different braid-encoding scheme where the proton vs neutron
      trace ratio is structurally bounded by ~0.14% rather than
      determined by σ↔σ⁻¹ count.

This diagnostic does NOT propose a fix; it documents the structural
origin of the 8.3% neutron error so the next agent has a clear target.

Output: `neutron-error-diagnostic.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from q_parameter import Q as Q0_FLOAT
# CODATA anchors via the canonical mp.mpf-string source
# (per Copilot review on PR #621 — single source of truth).
from codata_constants import (
    M_E_MEV as _M_E_MP,
    M_P_MEV_VALIDATION as _M_P_MP,
    M_N_MEV_VALIDATION as _M_N_MP,
)
M_E_MEV = float(_M_E_MP)
M_P_MEV = float(_M_P_MP)  # validation-only comparator (diagnostic script)
M_N_MEV = float(_M_N_MP)  # validation-only comparator (diagnostic script)


def main() -> int:
    # Construct WitnessBuilder up-front so durationMs reflects actual
    # end-to-end runtime (per Copilot review on PR #621).
    w = WitnessBuilder("neutron-error-diagnostic", engine="python")
    w.set_audit_only("docs/audits/2026-05-09-mass-table-1ppb-audit.md")

    # Load the legacy mass-table witness (six-term decomposition).
    # P4‴ note: this diagnostic probes the legacy E_0 single-anchor
    # calibration via its `term1_atomic_total`,
    # `term6_cyclotomic_tail_MeV`, and `total_hecke` fields
    # (term1 specifically localises the 8.3% error gap; see line 171
    # findings). All are legacy-only. Canonical mass predictions
    # are in `atomic-mass-via-rho-k.witness.json`.
    here = Path(__file__).parent
    witness_path = here / "atomic-braid-mass-table.witness.json"
    with open(witness_path) as f:
        mtw = json.load(f)

    rows = mtw["data"]["rows"]
    p_row = next(r for r in rows if r["atom"] == "p")
    n_row = next(r for r in rows if r["atom"] == "n")

    # Component-by-component diff
    components = [
        "term1_atomic_total",
        "term1_factor_disjoint_base",
        "term1_factor_a_ZN",
        "term1_factor_full_twist_delta_n2",
        "term2_markov_z2",
        "term3_markov_z4",
        "term4_frobenius_codim",
        "term6_cyclotomic_tail_MeV",
        "total_hecke",
    ]

    print("=" * 100)
    print("NEUTRON −8.3% ERROR DIAGNOSTIC — Strategy-3 component decomposition")
    print("=" * 100)
    # E_0 derived from proton row (since witness summary doesn't expose it directly)
    p_total_for_E0 = float(p_row["total_hecke"])
    p_t6_for_E0   = float(p_row["term6_cyclotomic_tail_MeV"])
    e0_proton_anchored = (M_P_MEV - p_t6_for_E0) / p_total_for_E0
    print(f"\n  q_0 = {Q0_FLOAT}")
    print(f"  E_0 (proton-calibrated) = {e0_proton_anchored:.6f} MeV/cat-unit")
    print(f"\n  CODATA m_n − m_p   = {M_N_MEV - M_P_MEV:+.4f} MeV  ({(M_N_MEV-M_P_MEV)/M_P_MEV*100:+.4f}% of m_p)")
    print(f"  Predicted Δ        = {float(p_row['M_pred_MeV']) - float(n_row['M_pred_MeV']):+.4f} MeV")
    print(f"  Predicted err on n = {float(n_row['err_pct']):+.3f}%")
    print()

    print(f"  {'component':<35} {'proton':>20} {'neutron':>20} {'diff':>20}  Identical?")
    print(f"  {'-'*35} {'-'*20} {'-'*20} {'-'*20}  ----------")
    diffs: list[dict] = []
    for c in components:
        p_v = float(p_row[c])
        n_v = float(n_row[c])
        d = n_v - p_v
        identical = abs(d) < 1e-12
        marker = "  ✓ IDENTICAL" if identical else f"  ✗ Δ = {d:+.6f}"
        print(f"  {c:<35} {p_v:>20.10f} {n_v:>20.10f} {d:>+20.6e}{marker}")
        diffs.append({"component": c, "proton": p_v, "neutron": n_v, "diff": d, "identical": identical})

    # Localise the gap
    p_total = float(p_row["total_hecke"])
    n_total = float(n_row["total_hecke"])
    p_t1 = float(p_row["term1_atomic_total"])
    n_t1 = float(n_row["term1_atomic_total"])
    print()
    print(f"  Total cat-unit gap (n − p) = {n_total - p_total:+.6f}")
    print(f"  T1 contribution (n − p)    = {n_t1 - p_t1:+.6f}")
    print(f"  T2/T3/T4 contribution      = {(n_total - p_total) - (n_t1 - p_t1):+.6f}")
    print()
    print(f"  ⇒ 100% of the cat-unit gap lives in T1 = |tr_M_atomic|.")
    print(f"  ⇒ a(Z,N) and Δ_n² are 1.0 for both at A=1, so neither contributes.")
    print(f"  ⇒ The 30% T1 trace gap reflects the σ↔σ⁻¹ asymmetry between")
    print(f"     uu→σ (proton) and dd→σ⁻¹ (neutron) at q≠1.")
    print(f"  ⇒ Physical m_n − m_p / m_p = 0.14%; framework predicts 8.3%.")
    print(f"  ⇒ Over-prediction factor: ≈60×.")

    # ── m_e accounting check ────────────────────────────────────────
    # Hypothesis: the framework's "proton braid" includes an electron
    # crossing (atomic-hydrogen braid).  If true, calibration target
    # should be M_atomic_H = M_p + M_e − Rydberg ≈ M_p + M_e.
    #
    # Test: does adjusting the calibration target by ±m_e bring the
    # neutron prediction closer to CODATA?
    print()
    print("─" * 100)
    print("m_e ACCOUNTING CHECK")
    print("─" * 100)

    p_total = float(p_row["total_hecke"])
    n_total = float(n_row["total_hecke"])
    p_t6 = float(p_row["term6_cyclotomic_tail_MeV"])
    n_t6 = float(n_row["term6_cyclotomic_tail_MeV"])

    # Hypothesis A (current state): bare proton braid, bare CODATA m_p.
    e0_A = (M_P_MEV - p_t6) / p_total
    n_pred_A = e0_A * n_total + n_t6
    err_A = (n_pred_A - M_N_MEV) / M_N_MEV * 100

    # Hypothesis B: framework's proton braid is hydrogen-atom (p + e⁻).
    # Calibration target: M_p + M_e; neutron stays bare.
    e0_B = (M_P_MEV + M_E_MEV - p_t6) / p_total
    n_pred_B = e0_B * n_total + n_t6
    err_B = (n_pred_B - M_N_MEV) / M_N_MEV * 100

    # Hypothesis C: framework's proton braid is hydrogen, AND we report
    # it as bare proton (so subtract m_e from the prediction).
    n_pred_C = e0_B * n_total + n_t6  # same as B for n (no e in neutron)
    err_C = err_B

    # Hypothesis D: m_e shifts the neutron prediction directly
    # (e.g. neutron-electron interaction missing).
    n_pred_D = n_pred_A + M_E_MEV
    err_D = (n_pred_D - M_N_MEV) / M_N_MEV * 100

    print(f"\n  Hypothesis A (current): bare braid, bare m_p calibration")
    print(f"    E_0 = (M_p_codata − T6_p) / total_hecke[p] = {e0_A:.6f} MeV/cat-unit")
    print(f"    M_pred[n] = {n_pred_A:.4f} MeV  err = {err_A:+.4f}%")
    print(f"\n  Hypothesis B: proton braid is atomic H (calibrate against m_p + m_e)")
    print(f"    E_0 = (M_p + M_e − T6_p) / total_hecke[p] = {e0_B:.6f} MeV/cat-unit")
    print(f"    M_pred[n] = {n_pred_B:.4f} MeV  err = {err_B:+.4f}%")
    print(f"\n  Hypothesis D: neutron prediction missing +m_e directly")
    print(f"    M_pred[n] = M_pred_A[n] + m_e = {n_pred_D:.4f} MeV  err = {err_D:+.4f}%")
    print(f"\n  CODATA m_n − m_p − m_e = {M_N_MEV - M_P_MEV - M_E_MEV:+.4f} MeV  (= β-decay Q)")
    print(f"  Framework's predicted (m_p − m_n) = {float(p_row['M_pred_MeV']) - n_pred_A:+.4f} MeV")
    print()
    print(f"  ⇒ m_e accounting (hypothesis B / D) shifts the neutron error by")
    print(f"     only ±{abs(M_E_MEV/M_N_MEV)*100:.4f}% = ±0.054%; the actual")
    print(f"     8.3% gap is far too large to be m_e-related.  The σ↔σ⁻¹")
    print(f"     asymmetry diagnosis stands.")

    # Witness population (builder constructed at start of main())
    w.set_description(
        "Strategy-3 component decomposition of the −8.3% neutron error.  "
        "All components except T1=|tr_M_atomic| are identical between "
        "proton and neutron at A=1; the entire gap localises to the "
        "trace ratio |tr_M(n)| / |tr_M(p)| = 0.764.  Root cause: σ↔σ⁻¹ "
        "asymmetry at q ≠ 1 in the proton-uud vs neutron-udd quark "
        "encoding (uu→σ, dd→σ⁻¹).  Physical splitting = 0.14% of m_p; "
        "framework's encoding predicts 8.3% — over-prediction factor "
        "≈60×.  This diagnostic does NOT propose a fix; it identifies "
        "the structural target for the next agent.  See "
        "docs/audits/2026-05-09-proton-m_e-anomaly.md §9.5 for the "
        "1ppb-frontier ranking."
    )
    w.set_content_block("prop:atomic-mass-gb-nf")
    w.add_parameter("q_0", float(Q0_FLOAT))
    w.add_parameter("M_p_codata_MeV", M_P_MEV)
    w.add_parameter("M_n_codata_MeV", M_N_MEV)
    w.add_parameter("M_n_minus_M_p_codata_MeV", M_N_MEV - M_P_MEV)
    w.add_parameter("M_n_minus_M_p_codata_pct", (M_N_MEV - M_P_MEV) / M_P_MEV * 100)
    w.add_data("component_diffs", diffs)
    w.add_data("M_pred_n_MeV", float(n_row["M_pred_MeV"]))
    w.add_data("M_pred_n_err_pct", float(n_row["err_pct"]))
    w.add_data("framework_n_minus_p_MeV", float(p_row["M_pred_MeV"]) - float(n_row["M_pred_MeV"]))
    w.add_data("over_prediction_factor",
               abs(float(p_row["M_pred_MeV"]) - float(n_row["M_pred_MeV"])) /
               abs(M_N_MEV - M_P_MEV))
    w.add_data("trace_ratio_n_over_p", n_t1 / p_t1)
    w.add_data("structural_origin", (
        "σ ↔ σ⁻¹ asymmetry: proton uud has uu pair → σ on gen 0, "
        "neutron udd has dd pair → σ⁻¹ on gen 1. At q ≠ 1, σ has "
        "eigenvalues {q, −q⁻¹} while σ⁻¹ has eigenvalues {q⁻¹, −q}; "
        "the per-swap trace ratio q²/q⁻² ≈ q⁴ ≈ 1.52 at q₀ ≈ 1.11, "
        "compounded across multiple swaps → 30% trace gap."
    ))
    w.add_data("recommended_paths", [
        "(a) Constrain ud/du encodings to produce equal trace contributions; "
        "uu/dd differ only by small isospin-symmetry-breaking term.",
        "(b) Decompose strong-force (isospin-symmetric, large) from "
        "isospin-symmetry-breaking (small) and use only the latter for "
        "the predicted m_n − m_p splitting.",
        "(c) Different braid-encoding scheme: trace ratio bounded by 0.14% "
        "structurally rather than determined by σ↔σ⁻¹ count.",
    ])
    w.add_assertion(
        "neutron_gap_localised_to_T1",
        computed=abs((n_total - p_total) - (n_t1 - p_t1)),
        expected=0.0,
        tolerance=1e-12,
    )
    w.add_assertion(
        "framework_overpredicts_n_minus_p_by_factor_~60",
        computed=abs(float(p_row["M_pred_MeV"]) - float(n_row["M_pred_MeV"])) / abs(M_N_MEV - M_P_MEV),
        expected=60.0,
        tolerance=20.0,   # allow 30-90× window
    )
    # m_e accounting check assertions
    w.add_data("m_e_accounting_hypotheses", {
        "hypothesis_A_bare_bare":      {"E_0": e0_A, "M_pred_n_MeV": n_pred_A, "err_pct": err_A},
        "hypothesis_B_atomic_p_calib": {"E_0": e0_B, "M_pred_n_MeV": n_pred_B, "err_pct": err_B},
        "hypothesis_D_n_plus_m_e":     {"M_pred_n_MeV": n_pred_D, "err_pct": err_D},
        "m_e_shift_max_pct": M_E_MEV / M_N_MEV * 100,
        "verdict": (
            f"m_e accounting can shift the neutron error by ±{M_E_MEV/M_N_MEV*100:.4f}% = ±0.054%; "
            "the 8.3% gap is far larger.  The neutron error is NOT m_e-related; "
            "the σ↔σ⁻¹ asymmetry diagnosis stands."
        ),
    })
    w.add_assertion(
        "m_e_accounting_does_not_explain_8pct_gap",
        computed=bool(abs(err_A) - abs(err_B) < 1.0),  # Hyp B should not improve by >1%
        expected=True,
    )
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("neutron"))

    w.save()
    print(f"\n✓ Witness: {Path('folio-assistant/computations/neutron-error-diagnostic.witness.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
