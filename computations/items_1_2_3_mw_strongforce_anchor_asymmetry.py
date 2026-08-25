"""Items 1-3 from prior session queue, honestly framed (derivation vs empirical).

Item 1: Construct m_W from substrate directly (not anchor-based)
Item 2: Apply formula to strong-force torus knots T(2,9), T(3,5)
Item 3: Investigate W/Z anchor asymmetry structurally

Per user correction: distinguish DERIVATION from EMPIRICAL match.

Status: EXPLORATORY (probes that EITHER derive structurally OR
report negative findings honestly).
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from math import comb
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpc, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from markov_trace_for_knot import trM_torus_2_k_mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0
HBAR_Q = (Q_0 - 1) / Q_0
G_CATALAN = mp.catalan
VOL_B3 = 8 * G_CATALAN

# CAL-1 from the registry, not re-typed: the literal here was
# "0.510998950", CODATA truncated to 9 s.f. (canonical 0.51099895069).
from codata_constants import M_E_MEV  # noqa: E402
M_W_GEV = mpf("80.379")
M_W_MEV = M_W_GEV * 1000
M_Z_GEV = mpf("91.1876")
M_Z_MEV = M_Z_GEV * 1000
M_H_GEV = mpf("125.10")


def tr_M_sym(m: int, h: mpf) -> mpf:
    """Even-n trace via DERIVED binomial pattern (PR #1174):
    c_{2j} = C(m+j, 2j)/2, so tr_M(σ_1^{2m}) (sibling norm) = sum/2."""
    return sum(mpf(comb(m + j, 2 * j)) / 2 * h ** (2 * j) for j in range(m + 1))


def tr_M_direct_hecke(n: int, q: mpf) -> mpf:
    """Direct Hecke calc: tr_M(σ_1^n) for T(2, n) torus link.

    q-Schur Plancherel convention (sibling generic infra). Standard
    normalization (NOT sibling's /2). Delegates to common infra
    `trM_torus_2_k_mpf` — keeps the H_2 closed form in one place.
    """
    return trM_torus_2_k_mpf(n, q)


def main():
    print("=" * 80)
    print("Items 1-3: m_W from substrate, strong-force torus knots, W/Z anchor asymmetry")
    print("=" * 80)
    print()
    print(f"50-dps mpmath; q_0 = {Q_0}, h_0 = {float(H_0):.10f}")
    print(f"Vol(B_3) = 8G ≈ {float(VOL_B3):.6f}, G ≈ {float(G_CATALAN):.6f}")
    print()

    # ===== Item 1: m_W from substrate =====
    print("=" * 80)
    print("ITEM 1: Can m_W be derived from substrate alone?")
    print("=" * 80)
    print()
    print("Empirical: m_W = 80.379 GeV, so m_W/m_e = 157,290")
    print()
    print("Per SM: m_W = g · v / 2 where g ≈ 0.6535 (SU(2)_L), v = 246 GeV")
    print()
    print("Per PR #1143 (empirical match): g ≈ π·h_0")
    g_predicted = mp.pi * H_0
    print(f"  Predicted g = π·h_0 = {float(g_predicted):.6f} (SM 0.6535, dev {float((g_predicted - mpf('0.6535'))/mpf('0.6535'))*100:+.2f}%)")
    print()
    print(f"To derive m_W from substrate, also need v from substrate.")
    print(f"Per PR #1143: v_framework/v_SM ≈ log(6); but v_framework itself")
    print(f"requires a substrate formula.")
    print()
    print("Honest verdict: m_W cannot be derived from substrate alone")
    print("without a derivation of v.")
    print()
    print("STRUCTURAL DERIVATION (modulo open v):")
    print(f"  m_W = (π·h_0) · v / 2")
    print(f"      = (π·h_0) · v_substrate · 0.5  ← v_substrate is the OPEN piece")
    print()
    print("Empirical inversion: if g = π·h_0 holds exactly, then:")
    print(f"  v_required = 2·m_W/(π·h_0) = 2·{float(M_W_GEV):.4f}/{float(g_predicted):.6f}")
    v_required = 2 * M_W_GEV / g_predicted
    print(f"             = {float(v_required):.4f} GeV (SM v = 246)")
    print(f"  Deviation from SM v: {float((v_required - mpf(246))/mpf(246))*100:+.2f}%")
    print()
    item1 = {
        "g_predicted": float(g_predicted),
        "v_required_GeV": float(v_required),
        "v_SM_GeV": 246.0,
        "v_deviation_pct": float((v_required - mpf(246))/mpf(246))*100,
        "verdict": (
            "m_W cannot be derived from substrate alone without v. "
            "Conditional formula: m_W = (π·h_0)·v/2, with v as the "
            "open structural quantity."
        ),
    }

    # ===== Item 2: strong-force torus knots T(2,9), T(3,5) =====
    print("=" * 80)
    print("ITEM 2: Strong-force torus knots T(2,9), T(3,5) — apply formula")
    print("=" * 80)
    print()
    print("SM: gluons are MASSLESS (mass term forbidden by SU(3) gauge symmetry)")
    print("Framework's claim: T(2,9) is strong-force EM anchor; m_T(2,9) = ?")
    print()
    print("If gluons are massless, the categorical formula should give 0 or")
    print("very small at substrate.")
    print()
    # For T(2, 9): odd n, knot (not link)
    # tr_M(σ_1^9) at q_0
    tr_T29 = tr_M_direct_hecke(9, Q_0)
    print(f"  tr_M(σ_1^9) at q_0 (standard norm) = {float(tr_T29):.6f}")
    print(f"  → NON-ZERO; if formula is m = m_e · |tr_M|, gives m ≈ {float(M_E_MEV * abs(tr_T29)):.4f} MeV")
    print(f"    That's ~0.5 MeV — much smaller than W/Z/H but NOT zero")
    print()

    # For T(3, 5): braid in B_3, n_crossings = 10. Need H_3(q) treatment.
    # T(3, n) is the (3, n) torus knot for gcd(3, n) = 1.
    # Markov trace at H_3(q) is more complex (3 partitions: (3), (2,1), (1,1,1))
    print("T(3,5) is in B_3 — H_3(q) has 3 partitions: (3), (2,1), (1,1,1)")
    print("dims 1, 2, 1; Schur elements differ. Need separate treatment.")
    print()
    print("Honest finding: applying the binomial-derived T(2,2m) formula to T(2,9)")
    print("gives non-zero value. The framework's claim that T(2,9) is gauge-massless")
    print("is NOT automatically satisfied by the trace formula — would need an")
    print("additional categorical constraint (e.g., SU(3) gauge-invariance projection).")
    print()
    item2 = {
        "T29_tr_M_at_q0": float(tr_T29),
        "T29_naive_mass_MeV": float(M_E_MEV * abs(tr_T29)),
        "expected_mass_MeV": 0.0,  # gluons massless
        "verdict": (
            "T(2,9) trace gives non-zero ≈ 0.5 MeV from naive formula. "
            "Gauge-massless gluons require a SEPARATE categorical mechanism "
            "(gauge invariance projection). Cannot be derived from trace alone."
        ),
    }

    # ===== Item 3: W/Z anchor asymmetry =====
    print("=" * 80)
    print("ITEM 3: W/Z anchor asymmetry — is the gauge_mass_factor really shared?")
    print("=" * 80)
    print()
    print("If formula is m = gauge_factor · P_m(h_0) with SAME gauge_factor for W,Z:")
    P_2 = tr_M_sym(2, H_0)
    P_3 = tr_M_sym(3, H_0)
    gauge_factor_W = M_W_GEV / P_2
    gauge_factor_Z = M_Z_GEV / P_3
    print(f"  gauge_factor from W: m_W/P_2 = {float(M_W_GEV):.4f}/{float(P_2):.6f} = {float(gauge_factor_W):.4f}")
    print(f"  gauge_factor from Z: m_Z/P_3 = {float(M_Z_GEV):.4f}/{float(P_3):.6f} = {float(gauge_factor_Z):.4f}")
    print(f"  ratio:               {float(gauge_factor_Z / gauge_factor_W):.6f}")
    print(f"  deviation:           {float((gauge_factor_Z - gauge_factor_W)/gauge_factor_W) * 100:+.4f}%")
    print()
    print("Predicted SM ratio m_W/m_Z = P_2/P_3:")
    pred_W_Z = P_2 / P_3
    sm_W_Z = M_W_GEV / M_Z_GEV
    print(f"  P_2/P_3 = {float(pred_W_Z):.6f}")
    print(f"  SM cos θ_W = m_W/m_Z = {float(sm_W_Z):.6f}")
    print(f"  Deviation from SM: {float((pred_W_Z - sm_W_Z)/sm_W_Z) * 100:+.4f}%")
    print()
    print("The 1% W/Z asymmetry SUGGESTS the gauge_factor needs a particle-")
    print("specific h-dependence. Test the form: gauge_factor(m) = base · (1 + c·h^k)")
    print(f"  W needs gauge = {float(gauge_factor_W):.4f}")
    print(f"  Z needs gauge = {float(gauge_factor_Z):.4f}")
    print(f"  Ratio Z/W = {float(gauge_factor_Z/gauge_factor_W):.6f}")
    print()
    print("Possible structural origins of 1% W/Z difference:")
    print("  (a) cos θ_W ≈ 0.882 — but P_2/P_3 already encodes ~0.89, close")
    print("  (b) W has charge ±1, Z neutral — known SM Higgs-mechanism diff")
    print("  (c) Higher-order h corrections to the trace polynomial")
    print()
    print("Honest verdict: the 1% W/Z deviation IS the SM cos θ_W vs P_2/P_3")
    print("difference. The framework's RT trace gives P_2/P_3 ≈ 0.891 (close to")
    print("SM cos θ_W ≈ 0.882). The 1% gap reflects the SM electroweak mixing")
    print("not directly visible in the H_2(q) trace alone.")
    print()
    item3 = {
        "gauge_factor_from_W": float(gauge_factor_W),
        "gauge_factor_from_Z": float(gauge_factor_Z),
        "ratio_Z_W": float(gauge_factor_Z / gauge_factor_W),
        "asymmetry_pct": float((gauge_factor_Z - gauge_factor_W)/gauge_factor_W) * 100,
        "P2_over_P3": float(pred_W_Z),
        "SM_cos_theta_W": float(sm_W_Z),
        "predicted_vs_SM_pct": float((pred_W_Z - sm_W_Z)/sm_W_Z) * 100,
        "verdict": (
            "The 1% W/Z asymmetry IS the gap between RT-chain prediction "
            "(P_2/P_3 ≈ 0.891) and SM cos θ_W (≈ 0.882). The trace formula "
            "captures the structural pattern but doesn't include the SU(2)_L "
            "× U(1)_Y mixing mechanism. Closing the 1% requires the SM "
            "electroweak symmetry breaking chain (Higgs VEV mixing g and g')."
        ),
    }

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print("Item 1 (m_W from substrate):")
    print("  STRUCTURAL: m_W = (π·h_0) · v / 2 (modulo open derivation of v)")
    print()
    print("Item 2 (T(2,9), T(3,5) strong force):")
    print("  T(2,9) trace gives ~0.5 MeV ≠ 0; gauge-massless requires SEPARATE")
    print("  categorical mechanism (gauge-invariance projection). Trace alone is")
    print("  insufficient.")
    print()
    print("Item 3 (W/Z anchor asymmetry):")
    print("  1% asymmetry is the SM electroweak mixing not in the trace formula.")
    print("  Resolution requires SU(2)_L × U(1)_Y mixing chain.")

    # Witness
    witness = {
        "compute": "items_1_2_3_mw_strongforce_anchor_asymmetry",
        "description": (
            "Items 1-3 from prior session queue: derive m_W from substrate, "
            "apply formula to T(2,9)/T(3,5) strong-force, investigate W/Z "
            "anchor asymmetry. Honestly frames each as derivation OR negative "
            "finding."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
        },
        "item_1_mw_from_substrate": item1,
        "item_2_strong_force_torus": item2,
        "item_3_wz_asymmetry": item3,
        "overall_verdict": (
            "All three items face the same structural barrier: the framework's "
            "RT trace chain on H_2(q) cannot fully derive SM electroweak masses "
            "without a categorical chain for v (Higgs VEV), g/g' mixing, and "
            "gauge-invariance projection (for massless gluons). The trace gives "
            "the SHAPE of the mass spectrum (within 1% on W/Z ratio) but the "
            "absolute scale and the W/Z 1% gap require SM-electroweak structure."
        ),
        "status": "exploratory",
        "tags": [
            "items-1-2-3",
            "m_W-derivation",
            "strong-force-torus",
            "anchor-asymmetry",
            "honest-negative",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "items-1-2-3-mw-strongforce-anchor-asymmetry.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
