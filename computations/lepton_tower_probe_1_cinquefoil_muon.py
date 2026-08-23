#!/usr/bin/env python3
"""
Probe 1 from docs/audits/2026-05-25-lepton-tower-structure.md.

Direct closed-form computation of |tr_M(σ_1^(2m+1))| at q_0 for the
T(2, 2m+1) torus-knot lepton-tower candidate at m = 1 (electron),
m = 2 (cinquefoil-as-muon hypothesis), m = 3 (septafoil = tau).

Uses the algebraic recursion proved in Lean
`lepton-mass-tower-canonical.lean:torus_knot_odd_reduction_exists`:
  σ^(2m+1) = P_m · σ + Q_m
  P_{m+1} = h² P_m + P_m + h Q_m
  Q_{m+1} = h P_m + Q_m
  P_0 = 1, Q_0 = 0

Then computes:
  |tr_M(σ^(2m+1))| at q_0 (Markov convention A: tr_M(1) = 1)
  ratio m=2/m=1 (cinquefoil/trefoil) vs CODATA m_μ/m_e
  ratio m=3/m=1 (septafoil/trefoil) vs CODATA m_τ/m_e
  required ξ_m prefactor to close

This tests the "muon = T(2, 5) instead of 4_1" hypothesis from
docs/audits/2026-05-24-muon-knot-id-conflict.md.

Outcome predicts whether the T(2, 2m+1) tower is uniform for leptons
or whether muon = 4_1 (different knot type) is the correct
identification per `prop:skein-mass-relation` (canonical paper).

Audit-only; no production wiring.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()

    # Constants (CODATA 2022)
    cal2_target = M_MU_OVER_M_E           # m_μ / m_e
    cal_tau_e   = mp.mpf("3477.23")               # m_τ / m_e

    # Substrate q_0 from CAL-2 (Skein LO, same as q_pinning_50_digit)
    # Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 53 digits, correct to 19 (qou-ckbv)
    Vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)

    h = q0 - 1 / q0                                # Hecke amplitude
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))  # Markov parameter

    print("=== Substrate at q_0 ===")
    print(f"  q_0    = {float(q0):.15f}")
    print(f"  h      = q - q⁻¹ = {float(h):.10f}")
    print(f"  z      = 1/(q^½ + q^{{-½}}) = {float(z):.10f}")
    print(f"  ℏ_q²   = {float(hbar_q_sq):.10f}")
    print(f"  1/ℏ_q² = {float(1/hbar_q_sq):.6f}")
    print()

    # Recurrence: P_0 = 1, Q_0 = 0; P_{m+1} = h² P_m + P_m + h Q_m; Q_{m+1} = h P_m + Q_m
    print("=== T(2, 2m+1) torus-knot tower: σ^(2m+1) = P_m σ + Q_m ===")
    rows = []
    P_m, Q_m = mp.mpf(1), mp.mpf(0)
    for m in range(0, 5):
        # tr_M (conv A: tr_M(1) = 1, tr_M(σ) = z)
        tr_M_A = P_m * z + Q_m
        # tr_M (conv B: tr_M(1) = z, Markov-normalized)
        tr_M_B = P_m * z + Q_m * z
        rows.append({
            "m": m,
            "knot": f"T(2, {2*m+1})",
            "label": {1: "trefoil (electron)", 2: "cinquefoil", 3: "septafoil (tau?)", 4: "T(2,9)"}.get(m, "—") if m >= 1 else "trivial",
            "P_m": str(P_m),
            "Q_m": str(Q_m),
            "tr_M_conv_A": str(tr_M_A),
            "tr_M_conv_B": str(tr_M_B),
            "abs_tr_M_A": mp.fabs(tr_M_A),
            "abs_tr_M_B": mp.fabs(tr_M_B),
        })
        print(f"  m={m}  T(2,{2*m+1:2d})  P_m = {float(P_m):.8f}  Q_m = {float(Q_m):.8f}  |tr_M(A)| = {float(mp.fabs(tr_M_A)):.6f}")
        # Step
        P_next = h*h*P_m + P_m + h*Q_m
        Q_next = h*P_m + Q_m
        P_m, Q_m = P_next, Q_next
    print()

    # Probe 1: m=2 (cinquefoil)-as-muon hypothesis
    print("=== Probe 1: cinquefoil-as-muon hypothesis ===")
    tr_M_e = mp.mpf(rows[1]["tr_M_conv_A"])   # m=1 trefoil
    tr_M_mu_cinquefoil = mp.mpf(rows[2]["tr_M_conv_A"])   # m=2 cinquefoil
    tr_M_tau = mp.mpf(rows[3]["tr_M_conv_A"])   # m=3 septafoil

    ratio_mu_cinquefoil = mp.fabs(tr_M_mu_cinquefoil) / mp.fabs(tr_M_e)
    ratio_tau           = mp.fabs(tr_M_tau)           / mp.fabs(tr_M_e)

    print(f"  Direct ratios (Markov conv A):")
    print(f"    |tr_M(T(2,5))| / |tr_M(trefoil)| = {float(ratio_mu_cinquefoil):.6f}  (vs CODATA m_μ/m_e = {float(cal2_target):.4f})")
    print(f"    |tr_M(T(2,7))| / |tr_M(trefoil)| = {float(ratio_tau):.6f}  (vs CODATA m_τ/m_e = {float(cal_tau_e):.4f})")
    print()

    # Required ξ_m prefactor to close
    xi_2 = cal2_target / ratio_mu_cinquefoil
    xi_3 = cal_tau_e / ratio_tau
    xi_ratio_3_2 = xi_3 / xi_2
    codata_tau_mu = cal_tau_e / cal2_target

    print(f"  Required ξ_m prefactor (ratio = CODATA / direct):")
    print(f"    ξ_2 (cinquefoil-as-muon) = {float(xi_2):.6f}  (compare to 1/ℏ_q² = {float(1/hbar_q_sq):.6f}; ratio = {float(xi_2 * hbar_q_sq):.4f})")
    print(f"    ξ_3 (septafoil-as-tau)   = {float(xi_3):.6f}  (compare to 1/ℏ_q² = {float(1/hbar_q_sq):.6f}; ratio = {float(xi_3 * hbar_q_sq):.4f})")
    print(f"    ξ_3 / ξ_2                = {float(xi_ratio_3_2):.4f}  (compare to CODATA m_τ/m_μ = {float(codata_tau_mu):.4f})")
    print()

    if mp.fabs(xi_ratio_3_2 - codata_tau_mu) / codata_tau_mu < mp.mpf("0.05"):
        verdict_cinquefoil = "SUPPORTED — ξ_3/ξ_2 ≈ m_τ/m_μ within 5%, consistent with uniform ξ_m·common structure"
    elif mp.fabs(xi_ratio_3_2 - codata_tau_mu) / codata_tau_mu < mp.mpf("0.20"):
        verdict_cinquefoil = "PARTIAL — ξ_3/ξ_2 close to m_τ/m_μ but off by 5-20%; structural improvement over flat ξ but not exact"
    else:
        verdict_cinquefoil = "REFUTED — ξ_3/ξ_2 ≠ m_τ/m_μ, simple T(2,2m+1) tower does not close lepton mass ratios"

    print(f"  Verdict (cinquefoil-as-muon under simple ξ_m tower): {verdict_cinquefoil}")
    print()

    # Compare to muon = 4_1 (current canonical paper identification)
    # tr_M(4_1) = z² (1 - h + h³) per Phase 3 audit
    tr_M_4_1 = z**2 * (1 - h + h**3)
    ratio_4_1 = mp.fabs(tr_M_4_1) / mp.fabs(tr_M_e)
    xi_4_1 = cal2_target / ratio_4_1
    print(f"=== Cross-check: muon = 4_1 (canonical paper) ===")
    print(f"  |tr_M(4_1)| = z²(1 - h + h³) = {float(mp.fabs(tr_M_4_1)):.6f}")
    print(f"  |tr_M(4_1)| / |tr_M(trefoil)| = {float(ratio_4_1):.6f}")
    print(f"  Required ξ_(4_1) = {float(xi_4_1):.6f}")
    print(f"  Compare ξ_2 (T(2,5)) = {float(xi_2):.6f}; ratio = {float(xi_4_1/xi_2):.4f}")
    print()

    # Witness
    witness = {
        "description": "Probe 1 — cinquefoil-as-muon T(2,2m+1) lepton-tower hypothesis test",
        "computation": "lepton_tower_probe_1_cinquefoil_muon",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "source_audit": "docs/audits/2026-05-25-lepton-tower-structure.md",
            "lean_theorem": "qou:QOU.BraidKnot.LeptonMassTowerCanonical.torus_knot_odd_reduction_exists",
            "method": "Algebraic closed-form via Hecke recursion P_{m+1} = h²P_m + P_m + hQ_m; Q_{m+1} = hP_m + Q_m",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z_markov": str(z),
            "hbar_q_sq": str(hbar_q_sq),
            "inv_hbar_q_sq": str(1/hbar_q_sq),
            "cal2_target_m_mu_over_m_e": str(cal2_target),
            "cal_tau_e_codata": str(cal_tau_e),
        },
        "tower_table": rows,
        "ratios": {
            "trM_cinquefoil_over_trefoil": str(ratio_mu_cinquefoil),
            "trM_septafoil_over_trefoil": str(ratio_tau),
            "trM_4_1_over_trefoil": str(ratio_4_1),
            "codata_m_mu_over_m_e": str(cal2_target),
            "codata_m_tau_over_m_e": str(cal_tau_e),
            "codata_m_tau_over_m_mu": str(codata_tau_mu),
        },
        "required_xi_prefactors": {
            "xi_2_cinquefoil_muon_hypothesis": str(xi_2),
            "xi_3_septafoil_tau": str(xi_3),
            "xi_3_over_xi_2": str(xi_ratio_3_2),
            "xi_4_1_canonical_muon": str(xi_4_1),
        },
        "verdict": {
            "cinquefoil_as_muon_uniform_xi_tower": verdict_cinquefoil,
            "ratio_xi_3_xi_2_match_codata_tau_mu": float(xi_ratio_3_2),
            "expected_if_uniform": float(codata_tau_mu),
            # mp.nstr preserves substrate precision in the JSON emit.
            "relative_diff_percent": mp.nstr(
                mp.fabs(xi_ratio_3_2 - codata_tau_mu) / codata_tau_mu * 100, 12),
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    here = Path(__file__).resolve().parent
    out = here / "lepton-tower-probe-1-cinquefoil-muon.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
