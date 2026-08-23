"""h⁴ probe for the linking weight inside `VolDensity(𝓑₃, q)`.

Two empirical questions, both targeted at the post-Yekutieli-purge
architectural finding (`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`):

1. **Solve-for-c_4**: assume the structurally-correct linking weight
   has form `5/2 + c_4·h⁴` (h² coefficient = 0, per the exact
   Borromean Markov trace closed form). Solve for c_4 such that the
   q-locality slope at q_0 → 0. Cross-check whether c_4 matches a
   natural categorical value:
     - `-3/4 · 5/2 = -15/8 = -1.875` (Markov trace's h⁴ × Wedderburn 5/2)
     - `-2G ≈ -1.832` (Yekutieli k=2 doubled-cell prediction)
     - `-G ≈ -0.916` (Yekutieli k=1 single-cell scaled to h⁴)
     - `-3/4 ≈ -0.75` (bare Markov trace h⁴ unscaled)

2. **Structural-trace**: test the candidate
   `linking_weight = 5/2 · (4 + h² − 3h⁴ − h⁶) / (h² + 4)` directly
   (i.e., Markov trace × 5/2). Compute slope; report gap.

Both probes use the canonical infrastructure (50-dps mpmath,
`geom_leading = Vol(𝓑₃)/ℏ_q²`, the q-locality slope discipline).

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
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

sys.path.insert(0, str(Path(__file__).parent))

# Constants
# CAL-1 from the registry, not re-typed: the literal here was
# "0.510998950", CODATA truncated to 9 s.f. (canonical 0.51099895069).
from codata_constants import M_E_MEV  # noqa: E402
M_P_CODATA_MEV = mpf(M_P_MEV_VALIDATION)
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
VOL_B3 = 8 * mp.catalan
G_CATALAN = mp.catalan

SWEEP_DELTAS = [mpf("0.001"), mpf("0.01"), mpf("0.05")]
TOLERANCE_PPM_PER_Q = mpf("1e5")


def hbar_q(q: mpf) -> mpf:
    return (q - 1) / q


def h_of_q(q: mpf) -> mpf:
    """h = q − q⁻¹ — the substrate expansion parameter."""
    return q - mpf(1) / q


def geom_leading(q: mpf) -> mpf:
    return VOL_B3 / hbar_q(q) ** 2


def lambda_p_codata(q: mpf) -> mpf:
    """Target linking weight: m_p_CODATA · ℏ_q² / (m_e · Vol)."""
    return M_P_CODATA_MEV * hbar_q(q) ** 2 / (M_E_MEV * VOL_B3)


def slope_ppm_per_q(linking_weight_fn, q_center: mpf, delta: mpf) -> mpf:
    qp, qm = q_center + delta, q_center - delta
    diff_p = linking_weight_fn(qp) - lambda_p_codata(qp)
    diff_m = linking_weight_fn(qm) - lambda_p_codata(qm)
    slope_abs = (diff_p - diff_m) / (2 * delta)
    return mpf("1e6") * slope_abs / linking_weight_fn(q_center)


# --- Candidate linking-weight forms ----------------------------------

def candidate_h2_only_no_h4(q: mpf) -> mpf:
    """Family A baseline: 5/2 + (3/4)·h² (current production)."""
    h = h_of_q(q)
    return mpf("5") / 2 + mpf("3") * h ** 2 / 4


def candidate_h4_param(q: mpf, c_4: mpf) -> mpf:
    """Test form: 5/2 + 0·h² + c_4·h⁴ (h² = 0 per exact Markov trace)."""
    h = h_of_q(q)
    return mpf("5") / 2 + c_4 * h ** 4


def candidate_structural_markov_trace(q: mpf) -> mpf:
    """5/2 × tr_M(β_Bor, q) where tr_M = (4+h²-3h⁴-h⁶)/(h²+4) exactly.

    This treats the exact Markov-trace closed form (which has h² = 0
    by non-trivial cancellation) as the structural linking weight,
    scaled by the half-symmetric Wedderburn 5/2 factor.
    """
    h = h_of_q(q)
    h2 = h ** 2
    h4 = h ** 4
    h6 = h ** 6
    trace = (4 + h2 - 3 * h4 - h6) / (h2 + 4)
    return mpf("5") / 2 * trace


# --- Probe 1: solve for c_4 ------------------------------------------

def solve_c_4_q_local(delta: mpf = mpf("0.01")) -> mpf:
    """Find c_4 such that the q-locality slope at q_0 vanishes.

    The candidate is `5/2 + c_4·h⁴`; the slope is linear in c_4
    (since c_4 enters linearly into linking_weight, and the slope
    is linear in linking_weight). So one solve = one bisection /
    Newton step.
    """
    # Sample at c_4 = 0 and c_4 = 1 to get the slope's linear response
    def lw(q, c):
        return candidate_h4_param(q, c)

    s0 = slope_ppm_per_q(lambda q: lw(q, mpf(0)), Q_0, delta)
    s1 = slope_ppm_per_q(lambda q: lw(q, mpf(1)), Q_0, delta)
    # slope(c) = s0 + (s1 − s0)·c; solve slope(c) = 0
    return -s0 / (s1 - s0)


def main() -> None:
    print(f"h⁴ probe for the Borromean linking weight inside VolDensity(𝓑₃, q)")
    print(f"50-dps mpmath; Q_0 = {Q_0}; h(Q_0) = {float(h_of_q(Q_0)):.10f}")
    print("---")

    # ===== Probe 1: solve-for-c_4 =====
    print("PROBE 1: solve-for-c_4 q-locality")
    print("Candidate: 5/2 + 0·h² + c_4·h⁴")
    print("---")
    c_4_solved = solve_c_4_q_local()
    print(f"c_4 solved (slope → 0 at δ = 0.01):  c_4 = {float(c_4_solved):.10f}")

    # Cross-check against natural categorical values
    natural_values = {
        "−3/4 · 5/2 = −15/8  (Markov trace h⁴ scaled by 5/2)": -mpf("15") / 8,
        "−2G  (Yekutieli k=2 doubled-cell)": -2 * G_CATALAN,
        "−G   (Yekutieli k=1 scaled to h⁴)": -G_CATALAN,
        "−3/4 (bare Markov trace h⁴ unscaled)": -mpf("3") / 4,
        "−G/2 (Yekutieli k=1 halved)": -G_CATALAN / 2,
        "+3/4 (Family A's h² coefficient, lifted to h⁴ slot)": mpf("3") / 4,
    }
    print("\nCross-check vs natural categorical values:")
    closest_match = None
    closest_diff = mpf("inf")
    for label, val in natural_values.items():
        diff = c_4_solved - val
        rel_diff = abs(diff) / abs(val) if val != 0 else abs(diff)
        marker = ""
        if abs(rel_diff) < closest_diff:
            closest_diff = abs(rel_diff)
            closest_match = label
        print(f"  {label}")
        print(f"      val = {float(val):+.6f}, diff = {float(diff):+.6f}, rel = {float(rel_diff)*100:+.2f}%")

    print(f"\nCLOSEST: {closest_match}  (rel diff {float(closest_diff)*100:.2f}%)")

    # Verify slope at solved c_4
    print("\nSlope verification at solved c_4:")
    slopes_at_solved = []
    for delta in SWEEP_DELTAS:
        s = slope_ppm_per_q(lambda q: candidate_h4_param(q, c_4_solved), Q_0, delta)
        print(f"  δ = {float(delta):.4f}: slope = {float(s):+.3e} ppm/q")
        slopes_at_solved.append({"delta": float(delta), "slope_ppm_per_q": float(s)})

    # Predicted m_p at q_0 with solved c_4
    lw_at_q0 = candidate_h4_param(Q_0, c_4_solved)
    m_p_pred_solved = M_E_MEV * geom_leading(Q_0) * lw_at_q0
    gap_pct_solved = (m_p_pred_solved - M_P_CODATA_MEV) / M_P_CODATA_MEV * 100
    print(f"\nWith solved c_4:")
    print(f"  linking_weight(q_0) = {float(lw_at_q0):.6f}")
    print(f"  m_p_pred           = {float(m_p_pred_solved):.4f} MeV")
    print(f"  gap vs CODATA      = {float(gap_pct_solved):+.3f}%")

    # ===== Probe 2: structural Markov-trace candidate =====
    print("\n" + "=" * 60)
    print("PROBE 2: structural linking weight = 5/2 · tr_M(β_Bor, q)")
    print("(exact closed form: tr_M = (4+h²-3h⁴-h⁶)/(h²+4))")
    print("---")

    lw_struct_q0 = candidate_structural_markov_trace(Q_0)
    m_p_pred_struct = M_E_MEV * geom_leading(Q_0) * lw_struct_q0
    gap_pct_struct = (m_p_pred_struct - M_P_CODATA_MEV) / M_P_CODATA_MEV * 100
    print(f"  linking_weight(q_0) = {float(lw_struct_q0):.6f}")
    print(f"  m_p_pred           = {float(m_p_pred_struct):.4f} MeV")
    print(f"  gap vs CODATA      = {float(gap_pct_struct):+.3f}%")
    print("\nq-locality slopes:")
    slopes_struct = []
    for delta in SWEEP_DELTAS:
        s = slope_ppm_per_q(candidate_structural_markov_trace, Q_0, delta)
        verdict = "PASS" if abs(s) < TOLERANCE_PPM_PER_Q else "FAIL"
        print(f"  δ = {float(delta):.4f}: slope = {float(s):+.3e} ppm/q  [{verdict}]")
        slopes_struct.append({
            "delta": float(delta),
            "slope_ppm_per_q": float(s),
            "pass_q_locality": bool(abs(s) < TOLERANCE_PPM_PER_Q),
        })

    # ===== Probe 3: baseline Family A for comparison =====
    print("\n" + "=" * 60)
    print("BASELINE: Family A = 5/2 + (3/4)·h² (current production)")
    print("---")
    lw_fa_q0 = candidate_h2_only_no_h4(Q_0)
    m_p_pred_fa = M_E_MEV * geom_leading(Q_0) * lw_fa_q0
    gap_pct_fa = (m_p_pred_fa - M_P_CODATA_MEV) / M_P_CODATA_MEV * 100
    print(f"  linking_weight(q_0) = {float(lw_fa_q0):.6f}")
    print(f"  m_p_pred           = {float(m_p_pred_fa):.4f} MeV")
    print(f"  gap vs CODATA      = {float(gap_pct_fa):+.3f}%")

    # Write witness
    witness = {
        "compute": "vol_density_borromean_h4_probe",
        "description": (
            "h⁴ probe for Borromean linking weight. Per "
            "docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md, "
            "the exact Markov trace closed form has h² = 0 and h⁴ = −3/4. "
            "This probe (1) solves c_4 such that 5/2 + c_4·h⁴ is q-local "
            "at q_0, and (2) tests the structural candidate "
            "5/2 · tr_M(β_Bor, q) directly."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "M_E_MEV": str(M_E_MEV),
            "M_P_CODATA_MEV": str(M_P_CODATA_MEV),
            "G_catalan": str(G_CATALAN),
            "sweep_deltas": [float(d) for d in SWEEP_DELTAS],
            "tolerance_ppm_per_q": float(TOLERANCE_PPM_PER_Q),
        },
        "probe_1_solve_for_c_4": {
            "candidate": "5/2 + 0·h² + c_4·h⁴",
            "c_4_solved": float(c_4_solved),
            "closest_natural_value": closest_match,
            "closest_relative_difference_pct": float(closest_diff * 100),
            "natural_values_cross_check": {
                k: {"value": float(v), "abs_diff": float(c_4_solved - v),
                    "relative_diff_pct": float(abs(c_4_solved - v) / abs(v) * 100)
                                          if v != 0 else None}
                for k, v in natural_values.items()
            },
            "verification_slopes_at_solved_c_4": slopes_at_solved,
            "linking_weight_at_q0": float(lw_at_q0),
            "m_p_pred_MeV": float(m_p_pred_solved),
            "gap_vs_codata_pct": float(gap_pct_solved),
        },
        "probe_2_structural_markov_trace": {
            "candidate": "5/2 · (4 + h² − 3h⁴ − h⁶) / (h² + 4)",
            "linking_weight_at_q0": float(lw_struct_q0),
            "m_p_pred_MeV": float(m_p_pred_struct),
            "gap_vs_codata_pct": float(gap_pct_struct),
            "q_locality_slopes": slopes_struct,
        },
        "baseline_family_a": {
            "candidate": "5/2 + (3/4)·h²",
            "linking_weight_at_q0": float(lw_fa_q0),
            "m_p_pred_MeV": float(m_p_pred_fa),
            "gap_vs_codata_pct": float(gap_pct_fa),
        },
        "status": "exploratory",
        "tags": [
            "h4-coefficient",
            "q-locality",
            "vol-density-refinement",
            "borromean",
            "so3-lift",
            "yekutieli-mi-k2",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }

    out_path = Path(__file__).parent / "vol-density-borromean-h4-probe.witness.json"
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
