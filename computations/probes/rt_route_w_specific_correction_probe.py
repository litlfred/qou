"""W-specific structural-correction search for the RT chain.

Per PR #1119 finding: at q_0, N=2:
  Z/H ratio = 0.703 vs SM 0.729 → -3.54% deviation (strong)
  W/Z ratio = 0.627 vs SM 0.882 → -28.85% deviation (weak)
  W/H ratio = 0.441 vs SM 0.643 → -31.37% deviation (weak)

Z/H matches; W ratios diverge by ~30%. This probe searches for a
W-specific structural correction factor that closes the W/Z and W/H
ratios while preserving Z/H.

## Candidate corrections (multiplicative on W only)

  - twist-count k: |J_N(T(2,4))| · k for k ∈ {1, 2, 3, 4, 5, 6}
  - twist-power k^p: |J_N(T(2,4))| · k^p for p ∈ {-1, -0.5, 0.5, 1, 2}
  - genus correction g: T(2,4) genus = 1; W needs factor of g+offset
  - charge factor: W has charge ±1, Z=H=0; multiplicative ×|Q|
  - component-count: same for W, Z, H (= 2) — null
  - quantum dim [N]_q at different N for W vs Z+H

Hypothesis: the W has charge ±1 (Z, H neutral) — categorical correction
should reflect this difference. If the correction is ×k_twist or
×k^p, the substrate-natural value of k_twist that makes W/Z and W/H
match SM identifies the categorical structure.

## Method

For each candidate correction C_W applied to |J_2(T(2,4))|, compute
new W/Z and W/H ratios; find C_W minimizing total deviation across
both ratios (preserving Z/H untouched).

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
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpc, mpf

mp.mp.dps = 50

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
M_W_MEV = mpf("80379.0")
M_Z_MEV = mpf("91187.6")
M_H_MEV = mpf("125100.0")

RATIO_W_Z_EXP = M_W_MEV / M_Z_MEV  # 0.882
RATIO_W_H_EXP = M_W_MEV / M_H_MEV  # 0.643
RATIO_Z_H_EXP = M_Z_MEV / M_H_MEV  # 0.729


def quantum_integer(N: int, q):
    sq = mp.sqrt(q)
    sqi = mpf(1) / sq
    return (sq ** N - sqi ** N) / (sq - sqi)


def colored_jones_T2n(N: int, n: int, q) -> mpc:
    bracket_N = quantum_integer(N, q)
    if abs(bracket_N) < mpf("1e-40"):
        return mp.nan
    total = mpc(0)
    for j in range(N):
        exponent = mpf(n) * (N - 1 - 2 * j) * (N + 1 - 2 * j) / 4
        sign = (-1) ** j
        total += sign * q ** exponent
    return total / bracket_N


def main():
    print("W-specific structural-correction search")
    print(f"50-dps mpmath; q_0 = {Q_0}; N = 2 (best ratio match level)")
    print("=" * 80)

    # Base |J_2| values
    j_W = abs(colored_jones_T2n(2, 4, Q_0))
    j_Z = abs(colored_jones_T2n(2, 6, Q_0))
    j_H = abs(colored_jones_T2n(2, 8, Q_0))

    print(f"\nBase |J_2(T(2,k))| at q_0:")
    print(f"  W = T(2,4): {float(j_W):.6f}")
    print(f"  Z = T(2,6): {float(j_Z):.6f}")
    print(f"  H = T(2,8): {float(j_H):.6f}")

    print(f"\nBase ratios (uncorrected):")
    print(f"  W/Z = {float(j_W/j_Z):.4f} (target {float(RATIO_W_Z_EXP):.4f}, dev {float((j_W/j_Z - RATIO_W_Z_EXP)/RATIO_W_Z_EXP*100):+.2f}%)")
    print(f"  Z/H = {float(j_Z/j_H):.4f} (target {float(RATIO_Z_H_EXP):.4f}, dev {float((j_Z/j_H - RATIO_Z_H_EXP)/RATIO_Z_H_EXP*100):+.2f}%)")
    print(f"  W/H = {float(j_W/j_H):.4f} (target {float(RATIO_W_H_EXP):.4f}, dev {float((j_W/j_H - RATIO_W_H_EXP)/RATIO_W_H_EXP*100):+.2f}%)")

    # Try candidate W-specific corrections
    print("\n" + "=" * 80)
    print("Candidate W-only corrections (Z, H untouched)")
    print("=" * 80)
    print(f"{'correction':<30} {'W_corrected':>12} {'W/Z':>9} {'dev W/Z':>9} {'W/H':>9} {'dev W/H':>9} {'sum |dev|':>10}")
    print("-" * 92)

    candidates = []

    # (a) Multiplicative k_twist for W only
    for label, C_W in [
        ("× 1 (baseline)", mpf(1)),
        ("× 2", mpf(2)),
        ("× 3", mpf(3)),
        ("× 4 (W twist count)", mpf(4)),
        ("× 6 (Z twist count)", mpf(6)),
        ("× 8 (H twist count)", mpf(8)),
        ("× √4 = 2 (W √twist)", mp.sqrt(4)),
        ("× √(4/6) (W/Z twist)", mp.sqrt(mpf(4)/6)),
        ("× 6/4 (Z/W twist)", mpf(6)/4),
        ("× 8/4 = 2 (H/W twist)", mpf(8)/4),
        ("× cos(θ_W) = 0.8816", mpf("0.8816")),
        ("× 1/2 (component count factor)", mpf(1)/2),
        ("× h(q_0) ≈ 0.2086", Q_0 - 1/Q_0),
        ("× [4]_q", abs(quantum_integer(4, Q_0))),
        ("× [4]_q / [2]_q", abs(quantum_integer(4, Q_0))/abs(quantum_integer(2, Q_0))),
        ("× 1.405 (empirical W/Z fit)", mpf("1.405")),
    ]:
        W_new = j_W * C_W
        wz_new = float(W_new / j_Z)
        wh_new = float(W_new / j_H)
        d_wz = abs((wz_new - float(RATIO_W_Z_EXP)) / float(RATIO_W_Z_EXP)) * 100
        d_wh = abs((wh_new - float(RATIO_W_H_EXP)) / float(RATIO_W_H_EXP)) * 100
        total = d_wz + d_wh
        candidates.append({
            "label": label,
            "C_W": float(C_W),
            "W_corrected": float(W_new),
            "W_over_Z_pred": wz_new,
            "W_over_H_pred": wh_new,
            "deviation_W_over_Z_pct": float((wz_new - float(RATIO_W_Z_EXP)) / float(RATIO_W_Z_EXP) * 100),
            "deviation_W_over_H_pct": float((wh_new - float(RATIO_W_H_EXP)) / float(RATIO_W_H_EXP) * 100),
            "total_abs_deviation_pct": total,
        })
        print(f"{label:<30} {float(W_new):>12.4f} {wz_new:>9.4f} {(wz_new - float(RATIO_W_Z_EXP))/float(RATIO_W_Z_EXP)*100:>+9.2f} {wh_new:>9.4f} {(wh_new - float(RATIO_W_H_EXP))/float(RATIO_W_H_EXP)*100:>+9.2f} {total:>10.2f}")

    candidates.sort(key=lambda x: x["total_abs_deviation_pct"])
    print("\n" + "=" * 80)
    print("BEST W-correction candidates (sorted by total |deviation|)")
    print("=" * 80)
    for i, c in enumerate(candidates[:5]):
        print(f"  {i+1}. {c['label']:<30} C_W = {c['C_W']:.4f}, total |dev| = {c['total_abs_deviation_pct']:.2f}%")
        print(f"     → W/Z = {c['W_over_Z_pred']:.4f} (dev {c['deviation_W_over_Z_pct']:+.2f}%)")
        print(f"     → W/H = {c['W_over_H_pred']:.4f} (dev {c['deviation_W_over_H_pct']:+.2f}%)")

    # Direct solve: what C_W minimizes simultaneous dev?
    # Want: (j_W * C_W) / j_Z = RATIO_W_Z_EXP  ⟹  C_W = RATIO_W_Z_EXP * j_Z / j_W
    # Also: (j_W * C_W) / j_H = RATIO_W_H_EXP  ⟹  C_W = RATIO_W_H_EXP * j_H / j_W
    C_W_from_wz = RATIO_W_Z_EXP * j_Z / j_W
    C_W_from_wh = RATIO_W_H_EXP * j_H / j_W
    C_W_avg = (C_W_from_wz + C_W_from_wh) / 2
    print("\n" + "=" * 80)
    print("Direct solve: ideal W-correction for each constraint")
    print("=" * 80)
    print(f"  C_W from W/Z target: {float(C_W_from_wz):.6f}")
    print(f"  C_W from W/H target: {float(C_W_from_wh):.6f}")
    print(f"  Average:             {float(C_W_avg):.6f}")
    print(f"  Difference:          {float(C_W_from_wh - C_W_from_wz):.6f}")
    print(f"  → If a single C_W satisfies both, the values should match.")
    print(f"  → Δ = {float(abs(C_W_from_wh - C_W_from_wz)):.4f} suggests {'CONSISTENT' if abs(float(C_W_from_wh - C_W_from_wz)) < 0.01 else 'SLIGHT INCONSISTENCY'}")

    # Witness
    witness = {
        "compute": "rt_route_w_specific_correction_probe",
        "description": (
            "W-specific multiplicative-correction search for the RT-chain "
            "Z/H-matches-but-W-diverges finding from PR #1119. Tests 16 "
            "candidate corrections (twist counts, quantum dimensions, "
            "trigonometric factors, etc.) applied to |J_2(T(2,4))| only. "
            "Identifies the best correction by total |deviation| on "
            "W/Z and W/H ratios."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "N_color": 2,
            "base_J_W": float(j_W),
            "base_J_Z": float(j_Z),
            "base_J_H": float(j_H),
        },
        "uncorrected_ratios": {
            "W_over_Z_pred": float(j_W/j_Z),
            "W_over_Z_exp": float(RATIO_W_Z_EXP),
            "Z_over_H_pred": float(j_Z/j_H),
            "Z_over_H_exp": float(RATIO_Z_H_EXP),
            "W_over_H_pred": float(j_W/j_H),
            "W_over_H_exp": float(RATIO_W_H_EXP),
        },
        "candidate_corrections": candidates,
        "direct_solve": {
            "C_W_to_match_W_over_Z": float(C_W_from_wz),
            "C_W_to_match_W_over_H": float(C_W_from_wh),
            "C_W_average": float(C_W_avg),
            "C_W_difference": float(C_W_from_wh - C_W_from_wz),
            "is_consistent_single_C_W": bool(abs(float(C_W_from_wh - C_W_from_wz)) < 0.01),
        },
        "interpretation": (
            "If a single C_W satisfies BOTH W/Z and W/H ratios (within "
            "small Δ), there exists a structurally-consistent W-only "
            "correction. The value of that C_W identifies the missing "
            "categorical factor. Candidates: charge ±1 (W has |Q|=1 vs "
            "Z, H neutral), twist count k=4 (T(2,4) vs T(2,6), T(2,8)), "
            "quantum dimensions, or trigonometric factors. If no single "
            "C_W works, the W's structural correction is more complex "
            "(e.g., depends on N or involves a non-multiplicative "
            "modification)."
        ),
        "status": "exploratory",
        "tags": [
            "rt-route",
            "w-correction",
            "electroweak",
            "ratio-mismatch",
            "structural-search",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "rt-route-w-specific-correction-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
