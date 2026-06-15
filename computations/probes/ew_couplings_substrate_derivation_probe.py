"""Systematic candidate-formula search for SM electroweak parameters from substrate.

Per user direction (2026-05-24): three research-grade tasks
1. Categorical derivation of g, g' from substrate
2. Investigation of v_framework / v_SM ≈ 1.78 factor
3. Cross-particle-class ratio 171/143 ≈ 1.196 categorical origin

This probe tests dozens of candidate substrate-functions for each
target and identifies the cleanest empirical matches. NOT a derivation
— this generates HYPOTHESES that may motivate categorical investigation.

## SM target values

  g  = 0.6535 (SU(2)_L coupling at Z scale)
  g' = 0.3504 (U(1)_Y coupling at Z scale)
  g/g' = 1.865
  v = 246 GeV (Higgs VEV)
  cos θ_W = g/√(g²+g'²) = 0.8815
  v_framework / v_SM ≈ 1.78
  gauge_mass_factor = 143
  scalar_mass_factor = 171
  scalar/gauge = 1.196

## Substrate quantities at q_0 ≈ 1.1097

  q_0:    1.1097
  q_0^-1: 0.9011
  h_0 = q_0 - q_0^-1: 0.2086
  ℏ_q = (q-1)/q: 0.0989
  Vol(B_3) = 8G: 7.328
  Catalan G: 0.9160
  π: 3.1416
  e: 2.7183
  φ (golden): 1.6180

Status: EXPLORATORY (per local/production-vs-exploratory-discipline).
"""

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import subprocess
import sys
from math import comb
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

mp.mp.dps = 50

# Substrate
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0          # ≈ 0.2086
HBAR_Q = (Q_0 - 1) / Q_0          # ≈ 0.0989
VOL_B3 = 8 * mp.catalan           # ≈ 7.328
G_CATALAN = mp.catalan            # ≈ 0.9160
GOLDEN_PHI = (mp.sqrt(5) + 1) / 2 # ≈ 1.618

# SM targets
SM_g = mpf("0.6535")
SM_g_prime = mpf("0.3504")
SM_v_GeV = mpf("246.0")
SM_cos_theta_W = mpf("0.8815")
SM_tan_theta_W = SM_g_prime / SM_g
SM_v_framework = mpf("443.0")  # from PR #1137 audit
SM_v_ratio = SM_v_framework / SM_v_GeV  # ≈ 1.78
GAUGE_FACTOR = mpf("143.0")
SCALAR_FACTOR = mpf("171.0")
SCALAR_GAUGE_RATIO = SCALAR_FACTOR / GAUGE_FACTOR  # ≈ 1.196


def report_match(label: str, predicted, target, tolerance_pct: float = 5.0):
    """Standard reporting + match-marker."""
    p = float(predicted)
    t = float(target)
    if t == 0:
        return f"  {label:<60} pred={p:+.6f}  target=0      (skip)"
    dev = (p - t) / t * 100
    marker = "  ✓ MATCH" if abs(dev) < tolerance_pct else "  ~ close" if abs(dev) < 20 else ""
    return f"  {label:<60} pred={p:+.6f}  target={t:+.6f}  dev={dev:+.2f}%{marker}"


def main():
    print("Systematic candidate-formula search: SM EW parameters from substrate")
    print(f"50-dps mpmath; q_0 = {Q_0}; h_0 = {float(H_0):.6f}; ℏ_q = {float(HBAR_Q):.6f}")
    print(f"Vol(B_3) = {float(VOL_B3):.6f}; Catalan G = {float(G_CATALAN):.6f}")
    print("=" * 90)

    all_hypotheses = []

    # ===== Task 1: g, g' candidates =====
    print("\n" + "=" * 90)
    print("TASK 1: Candidate substrate formulas for g (SM 0.6535)")
    print("=" * 90)
    g_candidates = {
        "√(2h_0)":             mp.sqrt(2 * H_0),
        "√(2ℏ_q)":             mp.sqrt(2 * HBAR_Q),
        "√(h_0 · 2 · G)":      mp.sqrt(H_0 * 2 * G_CATALAN),
        "h_0 · π":             H_0 * mp.pi,
        "√h_0 · √π":           mp.sqrt(H_0) * mp.sqrt(mp.pi),
        "h_0 · φ²":            H_0 * GOLDEN_PHI ** 2,
        "√(2 G · h_0)":        mp.sqrt(2 * G_CATALAN * H_0),
        "√(Vol/π²)/√π":        mp.sqrt(VOL_B3 / mp.pi ** 2) / mp.sqrt(mp.pi),
        "√(h_0 · √(2π))":      mp.sqrt(H_0 * mp.sqrt(2 * mp.pi)),
        "2·sin(θ_W)·cos(θ_W) = sin(2θ_W)": 2 * mp.sin(mp.acos(SM_cos_theta_W)) * SM_cos_theta_W,
        "√(2h_0(1+h_0²/2))":   mp.sqrt(2 * H_0 * (1 + H_0 ** 2 / 2)),
    }
    g_results = []
    for label, val in g_candidates.items():
        print(report_match(label, val, SM_g))
        g_results.append({
            "label": label, "value": float(val), "target": float(SM_g),
            "deviation_pct": float((val - SM_g) / SM_g * 100),
        })

    print("\n" + "=" * 90)
    print("TASK 1 cont: Candidate substrate formulas for g' (SM 0.3504)")
    print("=" * 90)
    # Note: g' typically smaller than g
    g_prime_candidates = {
        "√h_0":                 mp.sqrt(H_0),
        "h_0 · √π":             H_0 * mp.sqrt(mp.pi),
        "h_0 · φ":              H_0 * GOLDEN_PHI,
        "√(h_0 · G)":           mp.sqrt(H_0 * G_CATALAN),
        "√(ℏ_q · π)":           mp.sqrt(HBAR_Q * mp.pi),
        "√(2h_0) · tan(θ_W)":   mp.sqrt(2 * H_0) * SM_tan_theta_W,
        "h_0 / (h_0 + ℏ_q)":    H_0 / (H_0 + HBAR_Q),
        "√(2h_0)/φ":            mp.sqrt(2 * H_0) / GOLDEN_PHI,
        "(g_predicted)·tan(θ_W) [where g=√(2h_0)]": mp.sqrt(2 * H_0) * SM_tan_theta_W,
    }
    g_prime_results = []
    for label, val in g_prime_candidates.items():
        print(report_match(label, val, SM_g_prime))
        g_prime_results.append({
            "label": label, "value": float(val), "target": float(SM_g_prime),
            "deviation_pct": float((val - SM_g_prime) / SM_g_prime * 100),
        })

    print("\n" + "=" * 90)
    print("TASK 1 cont: Candidate substrate formulas for g/g' ratio (SM 1.865)")
    print("=" * 90)
    g_over_g_prime_candidates = {
        "φ (golden ratio)":      GOLDEN_PHI,
        "√(π·G)/√(2-1)":         mp.sqrt(mp.pi * G_CATALAN),
        "1/√(1-cos²θ_W)/cos θ_W = sec(θ_W)/tan(θ_W) - 1 + 1": mpf(1) / SM_tan_theta_W,
        "2 - h_0":               2 - H_0,
        "1 + √h_0":              1 + mp.sqrt(H_0),
        "√(π/√G)":               mp.sqrt(mp.pi / mp.sqrt(G_CATALAN)),
        "φ + h_0":               GOLDEN_PHI + H_0,
        "1/h_0 · ℏ_q · √π":      (1/H_0) * HBAR_Q * mp.sqrt(mp.pi),
    }
    ratio_results = []
    sm_g_over_g_prime = SM_g / SM_g_prime
    for label, val in g_over_g_prime_candidates.items():
        print(report_match(label, val, sm_g_over_g_prime))
        ratio_results.append({
            "label": label, "value": float(val), "target": float(sm_g_over_g_prime),
            "deviation_pct": float((val - sm_g_over_g_prime) / sm_g_over_g_prime * 100),
        })

    # ===== Task 2: v_framework / v_SM ≈ 1.78 =====
    print("\n" + "=" * 90)
    print("TASK 2: Candidate categorical formulas for v_framework/v_SM (≈1.78)")
    print("=" * 90)
    v_ratio_candidates = {
        "√π":                  mp.sqrt(mp.pi),
        "√3":                  mp.sqrt(3),
        "log(6)":              mp.log(6),
        "4/√5":                mpf(4) / mp.sqrt(5),
        "π/√3":                mp.pi / mp.sqrt(3),
        "√(π+G)":              mp.sqrt(mp.pi + G_CATALAN),
        "2·G - 1·h_0":         2 * G_CATALAN - H_0,
        "(φ-1)·π":             (GOLDEN_PHI - 1) * mp.pi,
        "exp(1/(1+e))":        mp.exp(1 / (1 + mp.e)),
        "1 + 1/cos θ_W - h_0": 1 + 1/SM_cos_theta_W - H_0,
        "√(π · cos θ_W)":      mp.sqrt(mp.pi * SM_cos_theta_W),
        "2·sin(45°) + h_0":    2 * mp.sin(mp.pi/4) + H_0,
        "1.78 (exact)":        mpf("1.78"),  # baseline
    }
    v_ratio_results = []
    for label, val in v_ratio_candidates.items():
        print(report_match(label, val, SM_v_ratio))
        v_ratio_results.append({
            "label": label, "value": float(val), "target": float(SM_v_ratio),
            "deviation_pct": float((val - SM_v_ratio) / SM_v_ratio * 100),
        })

    # ===== Task 3: 171/143 ≈ 1.196 =====
    print("\n" + "=" * 90)
    print("TASK 3: Candidate categorical formulas for scalar/gauge ratio (≈1.196)")
    print("=" * 90)
    sg_ratio_candidates = {
        "6/5":                 mpf(6) / 5,
        "Vol/(h_0² · gauge)":  VOL_B3 / (H_0 ** 2 * GAUGE_FACTOR),
        "1 + √h_0 - h_0":      1 + mp.sqrt(H_0) - H_0,
        "√(φ)":                mp.sqrt(GOLDEN_PHI),  # √φ ≈ 1.272 — too high
        "√(√2)":               mp.sqrt(mp.sqrt(2)),  # ≈ 1.189 — close!
        "(1+h_0)^√3":          (1 + H_0) ** mp.sqrt(3),
        "(1 + h_0/2)·(1 + h_0²)": (1 + H_0 / 2) * (1 + H_0 ** 2),
        "1 + h_0 · √π":        1 + H_0 * mp.sqrt(mp.pi),
        "cos(θ_W) + h_0":      SM_cos_theta_W + H_0,
        "5/4 - h_0":           mpf(5) / 4 - H_0,
        "tanh(1+h_0)":         mp.tanh(1 + H_0),
        "e^h_0 ":              mp.exp(H_0),
    }
    sg_ratio_results = []
    for label, val in sg_ratio_candidates.items():
        print(report_match(label, val, SCALAR_GAUGE_RATIO))
        sg_ratio_results.append({
            "label": label, "value": float(val), "target": float(SCALAR_GAUGE_RATIO),
            "deviation_pct": float((val - SCALAR_GAUGE_RATIO) / SCALAR_GAUGE_RATIO * 100),
        })

    # ===== Summary: cleanest matches =====
    print("\n" + "=" * 90)
    print("SUMMARY: cleanest matches (within 5%)")
    print("=" * 90)
    all_results = [
        ("g (0.6535)", g_results),
        ("g' (0.3504)", g_prime_results),
        ("g/g' (1.865)", ratio_results),
        ("v_ratio (1.78)", v_ratio_results),
        ("scalar/gauge (1.196)", sg_ratio_results),
    ]
    for category, results in all_results:
        best = sorted(results, key=lambda r: abs(r["deviation_pct"]))
        print(f"\n{category}:")
        for r in best[:3]:
            marker = "  ← BEST" if r == best[0] else ""
            print(f"  dev {r['deviation_pct']:+6.2f}%   {r['label']:<55}  {r['value']:.4f}{marker}")

    # Witness
    witness = {
        "compute": "ew_couplings_substrate_derivation_probe",
        "description": (
            "Systematic candidate-formula search for SM EW parameters "
            "(g, g', g/g', v_ratio, scalar/gauge) from substrate "
            "(q_0, h_0, ℏ_q, Vol(B_3), Catalan, π, e, φ). Identifies "
            "cleanest empirical matches; generates hypotheses for "
            "categorical investigation. NOT a derivation."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "HBAR_Q": str(HBAR_Q),
            "VOL_B3": str(VOL_B3),
            "G_CATALAN": str(G_CATALAN),
            "GOLDEN_PHI": str(GOLDEN_PHI),
            "SM_g": float(SM_g),
            "SM_g_prime": float(SM_g_prime),
            "SM_v_ratio": float(SM_v_ratio),
            "SCALAR_GAUGE_RATIO": float(SCALAR_GAUGE_RATIO),
        },
        "results": {
            "g_candidates": g_results,
            "g_prime_candidates": g_prime_results,
            "g_over_g_prime_candidates": ratio_results,
            "v_ratio_candidates": v_ratio_results,
            "scalar_gauge_ratio_candidates": sg_ratio_results,
        },
        "best_matches": {
            cat: sorted(rs, key=lambda r: abs(r["deviation_pct"]))[0]
            for cat, rs in all_results
        },
        "interpretation": (
            "These empirical matches are HYPOTHESES — clean numerical "
            "relations between substrate quantities and SM EW parameters "
            "that suggest possible categorical derivations. NONE of these "
            "constitute a proof; they generate candidate categorical "
            "structures for future investigation. Be cautious of "
            "numerology — many 'clean' matches at the few-% level are "
            "coincidental given the small number of substrate quantities "
            "and the many ways to combine them."
        ),
        "status": "exploratory",
        "tags": [
            "ew-substrate-derivation",
            "g-g-prime",
            "v-framework-ratio",
            "scalar-gauge-ratio",
            "hypothesis-generation",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "ew-couplings-substrate-derivation-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
