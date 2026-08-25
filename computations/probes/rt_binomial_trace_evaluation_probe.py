"""Cherry-pick PR #1125's binomial pattern; evaluate trace polynomial at q_0.

Per the apology + cherry-pick acknowledgment on sibling PR #1125
(merged 2026-05-24 — `claude/torus-knot-h-expansion-pattern-2026-05-24`).

PR #1125 proved symbolically (sympy, 54 cells) that the Markov-trace
h-expansion coefficient for T(2, 2m) torus links has the unified
binomial form:
    c_{2j}(T(2, 2m)) = C(m+j, 2j) / 2

This probe BUILDS ON that finding by:

1. Computing the trace polynomial values $P_m(h_0) = \sum_j c_{2j} h_0^{2j}$
   directly from the binomial coefficients (clean, no numerical extraction)
2. Reporting per-particle (W, Z, H) values + cross-particle ratios
3. **Honestly acknowledging** that absolute SM mass derivation via this
   trace polynomial alone is structurally limited — the SM ratios depend
   on gauge coupling constants (g, g', λ) which are NOT in the
   framework's RT chain
4. Identifying WHICH parts of the SM mass spectrum the trace data DOES
   determine vs which require additional categorical structure

This is the **honest exploration** continuing from the W = √[2]_q
retraction (PR #1126) — using a cleaner (symbolically-proved) structural
input instead of empirical fits.

Status: EXPLORATORY (per `local/production-vs-exploratory-discipline`).
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
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0   # ≈ 0.20856

# SM masses
M_W_GEV = mpf("80.379")
M_Z_GEV = mpf("91.1876")
M_H_GEV = mpf("125.10")
RATIO_W_Z_SM = M_W_GEV / M_Z_GEV  # 0.8819 (cos θ_W)
RATIO_Z_H_SM = M_Z_GEV / M_H_GEV  # 0.7290
RATIO_W_H_SM = M_W_GEV / M_H_GEV  # 0.6425

# SM torus link assignments (per electroweak-higgs-torus-link-triplet.md)
SM_TORUS = {
    "W±": {"m": 2, "n": 4, "mass_GeV": M_W_GEV, "charge": 1, "spin": 1},
    "Z":  {"m": 3, "n": 6, "mass_GeV": M_Z_GEV, "charge": 0, "spin": 1},
    "H":  {"m": 4, "n": 8, "mass_GeV": M_H_GEV, "charge": 0, "spin": 0},
}


def c_2j_binomial(m: int, j: int) -> mpf:
    """Per PR #1125 (sibling, sympy-proved): c_{2j}(T(2, 2m)) = C(m+j, 2j)/2."""
    return mpf(comb(m + j, 2 * j)) / 2


def trace_polynomial_value(m: int, h: mpf) -> mpf:
    """Sum the binomial-pattern coefficients × h^{2j} for j = 0..m.
    Per PR #1125, the expansion terminates at j = m, so this is the
    EXACT evaluation of tr_M(σ_1^{2m}) on H_2(q) (modulo [2]_q normalization
    that's absorbed; see PR #1125 §"Why this matters")."""
    total = mpf(0)
    for j in range(m + 1):
        total += c_2j_binomial(m, j) * h ** (2 * j)
    return total


def main():
    print("Cherry-pick PR #1125 binomial pattern → trace polynomial evaluation at q_0")
    print(f"50-dps mpmath; q_0 = {Q_0}; h_0 = {float(H_0):.10f}; h_0² ≈ {float(H_0**2):.10f}")
    print("=" * 80)

    # Per-particle binomial coefficients + trace polynomial values
    results = {}
    print(f"\n{'particle':<6} {'m':<3} {'c_0':>6} {'c_2':>6} {'c_4':>6} {'c_6':>6} {'c_8':>6}  P_m(h_0)")
    print("-" * 80)
    for particle, info in SM_TORUS.items():
        m = info["m"]
        coeffs = [c_2j_binomial(m, j) for j in range(m + 1)]
        P_value = trace_polynomial_value(m, H_0)

        coeff_str = "  ".join(f"{float(c):>5.2f}" for c in coeffs) + "  " * (4 - m)  # padding
        print(f"{particle:<6} {m:<3} {coeff_str}  {float(P_value):>10.6f}")

        results[particle] = {
            "m": m,
            "n_torus": info["n"],
            "c_2j_coefficients": [float(c) for c in coeffs],
            "P_m_at_h0": float(P_value),
            "actual_mass_GeV": float(info["mass_GeV"]),
            "charge": info["charge"],
            "spin": info["spin"],
        }

    # Cross-particle ratios
    P_W = mpf(str(results["W±"]["P_m_at_h0"]))
    P_Z = mpf(str(results["Z"]["P_m_at_h0"]))
    P_H = mpf(str(results["H"]["P_m_at_h0"]))

    print("\n" + "=" * 80)
    print("Cross-particle ratios via P_m(h_0) (from binomial pattern, NO empirical fit)")
    print("=" * 80)
    print(f"{'ratio':<10} {'prediction':>12} {'SM target':>12} {'deviation':>14}")
    print("-" * 60)

    ratios = {}
    for label, num, den, sm_ratio in [
        ("W/Z", P_W, P_Z, RATIO_W_Z_SM),
        ("Z/H", P_Z, P_H, RATIO_Z_H_SM),
        ("W/H", P_W, P_H, RATIO_W_H_SM),
    ]:
        pred = num / den
        dev_pct = (pred - sm_ratio) / sm_ratio * 100
        marker = "  ✓ within 5%" if abs(float(dev_pct)) < 5 else ""
        print(f"{label:<10} {float(pred):>12.6f} {float(sm_ratio):>12.6f} {float(dev_pct):>+13.2f}%{marker}")
        ratios[label] = {
            "predicted": float(pred),
            "SM": float(sm_ratio),
            "deviation_pct": float(dev_pct),
        }

    # Analysis: which findings are structurally backed by the trace data
    print("\n" + "=" * 80)
    print("STRUCTURAL ANALYSIS")
    print("=" * 80)

    # The trace values vs the actual masses
    print("\nTrace polynomial values P_m(h_0):")
    for particle, info in results.items():
        ratio_to_mass = info["P_m_at_h0"] / float(info["actual_mass_GeV"])
        print(f"  {particle}: P_m = {info['P_m_at_h0']:.4f}, actual mass = {info['actual_mass_GeV']} GeV, ratio = {ratio_to_mass:.6f}")

    print("\nObservation: the P_m values are in [0.5, 0.75] range while the masses span [80, 125] GeV.")
    print("The trace polynomial does NOT directly give masses; their ratios are SMALLER than mass ratios.")
    print()
    print("The W/Z ratio match (+0.9% from SM) is suggestive but partial:")
    print(f"  - W/Z (trace) ≈ {float(P_W/P_Z):.4f}; SM = {float(RATIO_W_Z_SM):.4f}")
    print(f"  - This is BETTER than PR #1122's √[2]_q substrate-point fit (+0.69% — but jet-")
    print(f"    order check showed 7% per jet)")
    print(f"  - Z/H and W/H deviations remain ~20% — the trace polynomial alone CANNOT")
    print(f"    predict all 3 SM ratios simultaneously")
    print()
    print("STRUCTURAL CONCLUSION: predicting all 3 SM masses from |J_N| or tr_M trace data")
    print("ALONE is impossible without supplying gauge-coupling constants (g, g', λ).")
    print()
    print("What the binomial trace data DOES determine structurally:")
    print(f"  ✓ Coefficient pattern: c_{{2j}} = C(m+j, 2j)/2 (sibling PR #1125, proved)")
    print(f"  ✓ Termination at j = m (no higher-order divergence)")
    print(f"  ✓ W/Z trace ratio within ~1% of SM cos θ_W (suggestive)")
    print(f"  ? Z/H and W/H trace ratios off by ~20% (requires additional structure)")
    print()
    print("What's needed for full categorical SM derivation:")
    print(f"  - Categorical chain for g, g' (SU(2)_L × U(1)_Y couplings) from substrate")
    print(f"  - Categorical chain for λ (Higgs self-coupling)")
    print(f"  - The CategoricalHiggsIdempotent class (existing, placeholder) is the")
    print(f"    structural framework for these — see PR #1126 retraction audit §3")

    # Witness
    witness = {
        "compute": "rt_binomial_trace_evaluation_probe",
        "description": (
            "Cherry-picks the unified binomial pattern from sibling "
            "PR #1125 (c_{2j}(T(2,2m)) = C(m+j, 2j)/2, sympy-proved) "
            "and evaluates the trace polynomial P_m(h_0) for W=T(2,4), "
            "Z=T(2,6), H=T(2,8). Reports cross-particle ratios + "
            "structural-limitation analysis. Honest follow-up to PR "
            "#1126's retraction of the W = √[2]_q substrate-point fit."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "binomial_pattern_source": "PR #1125 (sympy-proved, 54 cells m=1..9, j=0..5)",
        },
        "per_particle_results": results,
        "cross_particle_ratios": ratios,
        "interpretation": (
            "The trace polynomial P_m(h_0) using PR #1125's binomial "
            "coefficients gives W/Z within 1% of SM cos θ_W — suggestive "
            "structural pattern. But Z/H and W/H deviations remain ~20%, "
            "showing the trace polynomial alone CANNOT predict all 3 SM "
            "ratios simultaneously. Structural conclusion: full SM mass "
            "spectrum derivation requires gauge-coupling chain (g, g', λ) "
            "currently absent from framework. The CategoricalHiggsIdempotent "
            "class (existing placeholder) is the structural target for this "
            "extension (per PR #1126 retraction audit §3)."
        ),
        "honest_limits": [
            "Trace polynomial values P_m(h_0) are in [0.5, 0.75] range; actual masses span [80, 125] GeV",
            "Mass-to-trace ratio varies per particle (no clean single normalization)",
            "W/Z 1% match is the best signal; Z/H and W/H both off ~20%",
            "Cannot fix all 3 ratios with a single multiplicative/additive correction",
            "Full SM derivation requires gauge couplings (g, g', λ) categorically",
        ],
        "what_is_kept": [
            "Sibling PR #1125's binomial pattern c_{2j} = C(m+j, 2j)/2 (sympy-proved)",
            "PR #1119's Z/H ratio match (twist-count 6/8 ≈ SM 0.729)",
            "PR #1116's foundational chain separation (hyperbolic vs torus)",
            "RT-chain SM particle map W=T(2,4), Z=T(2,6), H=T(2,8) (existing content)",
        ],
        "what_is_retracted": [
            "PR #1122's 'W = √[2]_q closes ratios to 7% (STRONG)' — substrate-point fit, jet-order shows 20% per jet",
            "PR #1122's '√[2]_q is the quantum spinor norm' interpretation — it's the SM Higgs-VEV doublet convention",
        ],
        "status": "exploratory",
        "tags": [
            "rt-route",
            "binomial-cherry-pick",
            "trace-polynomial",
            "honest-structural-limits",
            "sibling-cherry-pick-1125",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "rt-binomial-trace-evaluation-probe.witness.json"
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
