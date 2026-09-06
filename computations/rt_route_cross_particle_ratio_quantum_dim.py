"""RT-route follow-up: cross-particle ratio test + quantum-dim normalization.

Per `docs/audits/2026-05-24-sm-particle-categorical-map-rt-route.md` §9:
action items #2 + #3 batched. Tests two structural variants on the
prior Q2 finding (|J_8(T(2,8))| · 8 · m_e ≈ 1.96 × m_H):

**#3 Quantum-dimension normalization.** Replace naive `N` factor with
quantum dimension `[N]_q` in the mass-scale formula. The quantum
dimension is the natural categorical factor in RT theory (it's the
"true" dimension of the irrep in the modular tensor category). Tests:

  |J_N| · [N]_q · m_e   vs   |J_N| · N · m_e

at the same (N, q_0) settings. Whether this resolves the factor-of-2
offset is the empirical question.

**#2 Cross-particle ratio test.** Compute |J_N(T(2, k))| for
k = 4 (W±), 6 (Z), 8 (H) at fixed (N, q_0). If the RT chain is
correct (regardless of the absolute mass formula), the RATIOS
should match the SM ratios:

  m_W / m_Z ≈ 0.882  (cos θ_W; experimentally measured)
  m_Z / m_H ≈ 0.729  (m_Z = 91.2 GeV, m_H = 125.1 GeV)
  m_W / m_H ≈ 0.643

This is a CHEAP cross-validation: even if the absolute |J_N|·N·m_e
formula is off by a structural factor, the RATIOS should be correct
IF the RT-chain identification (W=T(2,4), Z=T(2,6), H=T(2,8)) is
right. Mismatching ratios would falsify the chain; matching ratios
within ~5% would strongly validate it.

Status: EXPLORATORY (per `local/production-vs-exploratory-discipline`).
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpc, mpf

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

# Constants
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
from codata_constants import M_E_MEV  # noqa: E402 — CODATA-2022 full precision (no literal)

# SM mass measurements (PDG 2022)
M_W_GEV = mpf("80.379")
M_Z_GEV = mpf("91.1876")
M_HIGGS_GEV = mpf("125.10")

# Convert to MeV
M_W_MEV = M_W_GEV * 1000
M_Z_MEV = M_Z_GEV * 1000
M_H_MEV = M_HIGGS_GEV * 1000

# Ratios (experimental)
RATIO_W_Z_EXP = M_W_MEV / M_Z_MEV  # ≈ 0.8819 (= cos θ_W)
RATIO_Z_H_EXP = M_Z_MEV / M_H_MEV  # ≈ 0.7290
RATIO_W_H_EXP = M_W_MEV / M_H_MEV  # ≈ 0.6425

# Torus-link identifications per electroweak-higgs-torus-link-triplet.md
SM_TORUS_MAP = {
    "W±": {"n": 4, "mass_MeV": M_W_MEV, "label": "T(2,4)"},
    "Z":  {"n": 6, "mass_MeV": M_Z_MEV, "label": "T(2,6)"},
    "H":  {"n": 8, "mass_MeV": M_H_MEV, "label": "T(2,8)"},
}


def quantum_integer(N: int, q):
    """[N]_q = (q^{N/2} - q^{-N/2}) / (q^{1/2} - q^{-1/2})."""
    sq = mp.sqrt(q)
    sqi = mpf(1) / sq
    return (sq ** N - sqi ** N) / (sq - sqi)


def colored_jones_T2n(N: int, n: int, q) -> mpc:
    """Unnormalized colored Jones J_N(T(2, n), q)."""
    bracket_N = quantum_integer(N, q)
    if bracket_N == 0:
        return mp.nan
    total = mpc(0)
    for j in range(N):
        exponent = mpf(n) * (N - 1 - 2 * j) * (N + 1 - 2 * j) / 4
        sign = (-1) ** j
        total += sign * q ** exponent
    return total / bracket_N


def compute_mass_candidates(n: int, N: int, q) -> dict:
    """For T(2,n) at color N, compute multiple mass-scale candidates."""
    J_N = colored_jones_T2n(N, n, q)
    mag = abs(J_N)
    bracket_N_q = quantum_integer(N, q)
    bracket_n_q = quantum_integer(n, q)

    # `_mp` carries the mpf each field was computed as. It exists because the
    # ratio and deviation stages downstream consume these values, and reading
    # them back out of a `float(...)` field truncated the comparison against
    # the experimental ratios to binary64 -- three times over, in a chain
    # ending at a PDG comparison. It is working state, stripped before the
    # witness is written; the string fields carry the same numbers via `fmt`.
    exact = {
        "|J_N|": mag,
        "[N]_q": abs(bracket_N_q),
        "[n]_q": abs(bracket_n_q),
        "|J_N|·N·m_e (MeV)": mag * N * M_E_MEV,
        "|J_N|·[N]_q·m_e (MeV)": mag * abs(bracket_N_q) * M_E_MEV,
        "|J_N|·[n]_q·m_e (MeV)": mag * abs(bracket_n_q) * M_E_MEV,
        "|J_N|·n·m_e (MeV)": mag * n * M_E_MEV,
        "|J_N|·m_e (MeV)": mag * M_E_MEV,
    }
    out = {"n_torus": n, "N_color": N}
    out.update({k: fmt(v) for k, v in exact.items()})
    out["_mp"] = exact
    return out


def cross_particle_ratios(candidates: dict) -> dict:
    """Compute W:Z:H ratios for each formula; compare to experimental."""
    formulas = [
        "|J_N|·N·m_e (MeV)",
        "|J_N|·[N]_q·m_e (MeV)",
        "|J_N|·[n]_q·m_e (MeV)",
        "|J_N|·n·m_e (MeV)",
        "|J_N|·m_e (MeV)",
    ]
    results = {}
    for formula in formulas:
        w_val = candidates["W±"]["_mp"][formula]
        z_val = candidates["Z"]["_mp"][formula]
        h_val = candidates["H"]["_mp"][formula]
        if z_val == 0 or h_val == 0:
            results[formula] = None
            continue
        r_wz_pred = w_val / z_val
        r_zh_pred = z_val / h_val
        r_wh_pred = w_val / h_val
        dev = {
            "deviation_W_over_Z_pct":
                (r_wz_pred - RATIO_W_Z_EXP) / RATIO_W_Z_EXP * 100,
            "deviation_Z_over_H_pct":
                (r_zh_pred - RATIO_Z_H_EXP) / RATIO_Z_H_EXP * 100,
            "deviation_W_over_H_pct":
                (r_wh_pred - RATIO_W_H_EXP) / RATIO_W_H_EXP * 100,
        }
        results[formula] = {
            "predicted_W_over_Z": fmt(r_wz_pred),
            "predicted_Z_over_H": fmt(r_zh_pred),
            "predicted_W_over_H": fmt(r_wh_pred),
            "experimental_W_over_Z": fmt(RATIO_W_Z_EXP),
            "experimental_Z_over_H": fmt(RATIO_Z_H_EXP),
            "experimental_W_over_H": fmt(RATIO_W_H_EXP),
            **{k: fmt(v) for k, v in dev.items()},
            "_mp": {
                "predicted_W_over_Z": r_wz_pred,
                "predicted_Z_over_H": r_zh_pred,
                "predicted_W_over_H": r_wh_pred,
                **dev,
            },
        }
    return results


def main():
    print("RT-route follow-up: cross-particle ratios + quantum-dim normalization")
    print(f"50-dps mpmath; q_0 = {Q_0}")
    print("=" * 80)

    print(f"\nExperimental mass ratios:")
    print(f"  m_W / m_Z = {float(RATIO_W_Z_EXP):.6f}  (cos θ_W)")
    print(f"  m_Z / m_H = {float(RATIO_Z_H_EXP):.6f}")
    print(f"  m_W / m_H = {float(RATIO_W_H_EXP):.6f}")

    # Test multiple N values; pick the most informative ones
    N_test_values = [2, 4, 6, 8, 10, 12]

    all_results = {}
    for N in N_test_values:
        print(f"\n{'=' * 80}")
        print(f"Color dimension N = {N}")
        print(f"{'=' * 80}")

        candidates = {}
        for particle, info in SM_TORUS_MAP.items():
            cands = compute_mass_candidates(info["n"], N, Q_0)
            candidates[particle] = cands
            e = cands["_mp"]
            print(f"\n  {particle} = {info['label']}:  |J_{N}| = {float(e['|J_N|']):.4f}")
            print(f"    |J|·N·m_e        = {float(e['|J_N|·N·m_e (MeV)']):>14.2f} MeV  (act: {float(info['mass_MeV']):>10.2f})")
            print(f"    |J|·[N]_q·m_e    = {float(e['|J_N|·[N]_q·m_e (MeV)']):>14.2f} MeV")
            print(f"    |J|·[n]_q·m_e    = {float(e['|J_N|·[n]_q·m_e (MeV)']):>14.2f} MeV")
            print(f"    |J|·n·m_e        = {float(e['|J_N|·n·m_e (MeV)']):>14.2f} MeV")

        # Compute cross-particle ratios
        ratios = cross_particle_ratios(candidates)
        print(f"\n  Cross-particle ratios at N={N}:")
        print(f"  {'formula':<32} {'W/Z (pred)':>10} {'W/Z (exp)':>10} {'dev %':>8} {'Z/H (pred)':>11} {'dev %':>8}")
        print(f"  {'-'*82}")
        for formula, r in ratios.items():
            if r is None:
                continue
            e = r["_mp"]
            print(f"  {formula:<32} {float(e['predicted_W_over_Z']):>10.4f} "
                  f"{float(RATIO_W_Z_EXP):>10.4f} "
                  f"{float(e['deviation_W_over_Z_pct']):>+8.2f}  "
                  f"{float(e['predicted_Z_over_H']):>11.4f} "
                  f"{float(e['deviation_Z_over_H_pct']):>+8.2f}")

        all_results[f"N={N}"] = {
            "candidates": candidates,
            "ratios": ratios,
        }

    # Identify best (N, formula) combination by sum of |deviations|
    print(f"\n{'=' * 80}")
    print("BEST (N, formula) combinations by total |deviation| across 3 ratios")
    print(f"{'=' * 80}")
    best_results = []
    for N_key, data in all_results.items():
        for formula, r in data["ratios"].items():
            if r is None:
                continue
            e = r["_mp"]
            total_dev = (abs(e["deviation_W_over_Z_pct"])
                         + abs(e["deviation_Z_over_H_pct"])
                         + abs(e["deviation_W_over_H_pct"]))
            best_results.append({
                "N_key": N_key,
                "formula": formula,
                "total_deviation_pct": fmt(total_dev),
                "W_over_Z_dev_pct": fmt(e["deviation_W_over_Z_pct"]),
                "Z_over_H_dev_pct": fmt(e["deviation_Z_over_H_pct"]),
                "W_over_H_dev_pct": fmt(e["deviation_W_over_H_pct"]),
                "_mp": {
                    "total_deviation_pct": total_dev,
                    "W_over_Z_dev_pct": e["deviation_W_over_Z_pct"],
                    "Z_over_H_dev_pct": e["deviation_Z_over_H_pct"],
                    "W_over_H_dev_pct": e["deviation_W_over_H_pct"],
                },
            })

    best_results.sort(key=lambda x: x["_mp"]["total_deviation_pct"])
    print(f"  {'rank':<5} {'N':<6} {'formula':<32} {'total |dev| (%)':>16} {'W/Z dev':>10} {'Z/H dev':>10} {'W/H dev':>10}")
    print(f"  {'-' * 95}")
    for i, b in enumerate(best_results[:10]):
        marker = "  ← BEST" if i == 0 else ""
        e = b["_mp"]
        print(f"  {i+1:<5} {b['N_key']:<6} {b['formula']:<32} {float(e['total_deviation_pct']):>16.2f}  "
              f"{float(e['W_over_Z_dev_pct']):>+10.2f} {float(e['Z_over_H_dev_pct']):>+10.2f} "
              f"{float(e['W_over_H_dev_pct']):>+10.2f}{marker}")

    # Verdict
    print(f"\n{'=' * 80}")
    print("VERDICT")
    print(f"{'=' * 80}")
    if best_results:
        best = best_results[0]
        best_total = best["_mp"]["total_deviation_pct"]
        print(f"Best match: {best['N_key']}, {best['formula']}")
        print(f"  total |dev| across 3 ratios: {float(best_total):.2f}%")
        if best_total < 5:
            print(f"  → STRONG validation of RT-chain SM mapping (within 5% on all ratios)")
        elif best_total < 20:
            print(f"  → moderate validation; structural pattern present but quantitative offset")
        elif best_total < 100:
            print(f"  → weak signal; ratios are in same order-of-magnitude but not quantitative")
        else:
            print(f"  → no quantitative match across any (N, formula); chain needs more structure")

    # `_mp` is working state -- the mpf values every ratio, deviation and rank
    # above was computed from. Drop it before serialization; each one already
    # has a lossless string twin written by `fmt`.
    for data in all_results.values():
        for cands in data["candidates"].values():
            cands.pop("_mp", None)
        for r in data["ratios"].values():
            if r is not None:
                r.pop("_mp", None)
    for b in best_results:
        b.pop("_mp", None)

    # Witness
    witness = {
        "compute": "rt_route_cross_particle_ratio_quantum_dim",
        "description": (
            "Action items #2 (cross-particle ratio test) + #3 "
            "(quantum-dim normalization) from "
            "docs/audits/2026-05-24-sm-particle-categorical-map-rt-route.md §9. "
            "Tests whether |J_N(T(2,k))| ratios for k ∈ {4, 6, 8} at "
            "fixed (N, q_0) match the experimental m_W:m_Z:m_H ratios. "
            "Cheap (~3-min compute) cross-validation: matching ratios "
            "validates the RT-chain SM identification; mismatching ratios "
            "falsify it. Also tests quantum-dim [N]_q vs naive-dim N "
            "normalization."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "N_test_values": N_test_values,
            "experimental_masses": {
                "W": str(M_W_MEV),
                "Z": str(M_Z_MEV),
                "H": str(M_H_MEV),
            },
            "experimental_ratios": {
                "W_over_Z": fmt(RATIO_W_Z_EXP),
                "Z_over_H": fmt(RATIO_Z_H_EXP),
                "W_over_H": fmt(RATIO_W_H_EXP),
            },
        },
        "all_results": all_results,
        "best_combinations": best_results[:20],
        "interpretation": (
            "Cross-particle ratio test on the RT-chain SM identification. "
            "If the W:Z:H assignments to T(2,4):T(2,6):T(2,8) are correct, "
            "the |J_N| ratios should match m_W:m_Z:m_H regardless of "
            "absolute normalization. Best (N, formula) combination by "
            "total deviation reported. Quantum-dim [N]_q normalization "
            "tested alongside naive N for the factor-of-2 resolution "
            "from Q2 (PR #1116 Higgs probe finding)."
        ),
        "status": "exploratory",
        "tags": [
            "rt-route",
            "cross-particle-ratios",
            "quantum-dimension",
            "higgs",
            "electroweak",
            "W-Z-H-ratios",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out_path = WitnessBuilder.wrap_legacy(
        "rt-route-cross-particle-ratio-quantum-dim", witness,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
