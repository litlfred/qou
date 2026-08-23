"""RT-route level scan at root-of-unity q — settle action #4 empirically.

Per `docs/audits/2026-05-24-rt-level-selection-bring-genus-or-embedding-max.md`:
the substrate-natural RT level $k$ is undetermined. Three candidates:

  (a) k = 4 (Bring genus)
  (b) k = 9 (max-embedded-twist)
  (c) k(q_0) (substrate-derived; unknown map)

This probe scans the cross-particle ratios W : Z : H at
$q = \exp(\pi i / (k+2))$ for $k \in \{4, 6, 9, 12, 16, 20\}$ and finds
which level gives ratios closest to the SM measurements:

  m_W : m_Z : m_H = 0.882 : 1.000 : 1.373   (cos θ_W : 1 : m_H/m_Z)

If a clear minimum-deviation $k$ emerges, that's the substrate-natural
level for the torus chain. If no level matches, the RT chain itself
needs additional categorical structure.

Status: EXPLORATORY.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpc, mpf

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

# Constants — m_e from canonical source (CAL-1)
from codata_constants import M_E_MEV  # noqa: E402  # CODATA validation constant
M_W_MEV = mpf("80379.0")      # PDG validation target (not a calibration input)
M_Z_MEV = mpf("91187.6")      # PDG validation target (not a calibration input)
M_H_MEV = mpf("125100.0")     # PDG validation target (not a calibration input)
RATIO_W_Z_EXP = M_W_MEV / M_Z_MEV
RATIO_Z_H_EXP = M_Z_MEV / M_H_MEV
RATIO_W_H_EXP = M_W_MEV / M_H_MEV

SM_TORUS_MAP = {
    "W±": {"n": 4, "mass_MeV": M_W_MEV},
    "Z":  {"n": 6, "mass_MeV": M_Z_MEV},
    "H":  {"n": 8, "mass_MeV": M_H_MEV},
}


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


def scan_level(k: int) -> dict:
    """For RT level k, compute |J_N(T(2, n))| at q = exp(πi/(k+2)) for
    each SM torus particle (W, Z, H) at N = 2..min(k+1, 8).

    Returns ratio comparisons + best-N for this k.
    """
    q = mp.exp(mpc(0, mp.pi / (k + 2)))
    # N can go from 2 to k+1 (RT cutoff)
    N_max = min(k + 1, 10)
    per_N = []
    for N in range(2, N_max + 1):
        per_particle = {}
        for particle, info in SM_TORUS_MAP.items():
            J = colored_jones_T2n(N, info["n"], q)
            mag = abs(J)
            per_particle[particle] = float(mag)
        per_N.append({
            "N": N,
            "magnitudes": per_particle,
            "ratios": (
                {
                    "W_over_Z": per_particle["W±"] / per_particle["Z"]
                                if per_particle["Z"] > 0 else None,
                    "Z_over_H": per_particle["Z"] / per_particle["H"]
                                if per_particle["H"] > 0 else None,
                    "W_over_H": per_particle["W±"] / per_particle["H"]
                                if per_particle["H"] > 0 else None,
                }
            ),
        })

    # Best N for this k by total |deviation| from SM ratios
    best_N = None
    best_dev = mpf("inf")
    for n_data in per_N:
        r = n_data["ratios"]
        if r["W_over_Z"] is None or r["Z_over_H"] is None or r["W_over_H"] is None:
            continue
        d_wz = abs(mpf(str(r["W_over_Z"])) - RATIO_W_Z_EXP) / RATIO_W_Z_EXP
        d_zh = abs(mpf(str(r["Z_over_H"])) - RATIO_Z_H_EXP) / RATIO_Z_H_EXP
        d_wh = abs(mpf(str(r["W_over_H"])) - RATIO_W_H_EXP) / RATIO_W_H_EXP
        total = float((d_wz + d_zh + d_wh) * 100)
        if total < float(best_dev):
            best_dev = mpf(total)
            best_N = n_data["N"]
            best_data = n_data
    return {
        "k": k,
        "q_root_of_unity": f"exp(πi/{k+2})",
        "q_arg_radians": float(mp.pi / (k + 2)),
        "N_max_at_this_level": N_max,
        "per_N_data": per_N,
        "best_N": best_N,
        "best_N_total_dev_pct": float(best_dev),
        "best_N_data": best_data if best_N else None,
    }


def main():
    print("RT level scan: cross-particle W:Z:H ratios at root-of-unity q")
    print(f"Testing levels k ∈ {{4, 6, 9, 12, 16, 20}}")
    print(f"50-dps mpmath; SM ratios: W/Z = {float(RATIO_W_Z_EXP):.4f}, "
          f"Z/H = {float(RATIO_Z_H_EXP):.4f}, W/H = {float(RATIO_W_H_EXP):.4f}")
    print("=" * 80)

    k_values = [4, 6, 9, 12, 16, 20]
    results = []
    for k in k_values:
        try:
            r = scan_level(k)
            results.append(r)
            print(f"\nLevel k = {k}  (q = {r['q_root_of_unity']}, N_max = {r['N_max_at_this_level']})")
            print(f"  Best N: {r['best_N']}, total |dev| = {r['best_N_total_dev_pct']:.2f}%")
            if r["best_N_data"]:
                ratios = r["best_N_data"]["ratios"]
                print(f"    W/Z = {ratios['W_over_Z']:.4f}  (exp {float(RATIO_W_Z_EXP):.4f})")
                print(f"    Z/H = {ratios['Z_over_H']:.4f}  (exp {float(RATIO_Z_H_EXP):.4f})")
                print(f"    W/H = {ratios['W_over_H']:.4f}  (exp {float(RATIO_W_H_EXP):.4f})")
        except Exception as e:
            print(f"\nLevel k = {k}: FAILED ({e})")
            results.append({"k": k, "error": str(e)})

    # Best level overall
    valid = [r for r in results if "best_N_total_dev_pct" in r]
    if valid:
        best = min(valid, key=lambda r: r["best_N_total_dev_pct"])
        print("\n" + "=" * 80)
        print("VERDICT")
        print("=" * 80)
        print(f"Best level: k = {best['k']}, N = {best['best_N']}")
        print(f"  total |dev| across 3 ratios: {best['best_N_total_dev_pct']:.2f}%")
        if best['best_N_total_dev_pct'] < 5:
            print("  → STRONG validation of RT-chain SM mapping at this level")
        elif best['best_N_total_dev_pct'] < 20:
            print("  → moderate validation; partial signal at this level")
        else:
            print("  → weak signal across all tested levels; RT chain needs more structure")

    # Witness
    witness = {
        "compute": "rt_route_root_of_unity_level_scan",
        "description": (
            "Action item #4 from docs/audits/2026-05-24-rt-level-selection-"
            "bring-genus-or-embedding-max.md. Scans cross-particle "
            "W:Z:H ratios at q = exp(πi/(k+2)) for k ∈ {4, 6, 9, 12, "
            "16, 20}. Tests whether Bring genus 4, embedding-max 9, "
            "or some other level gives ratios matching SM measurements. "
            "Complements rt_route_cross_particle_ratio_quantum_dim.py "
            "which used real q_0 instead of root-of-unity q."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "levels_tested": k_values,
            "SM_torus_map": {
                p: {"n": info["n"], "mass_MeV": str(info["mass_MeV"])}
                for p, info in SM_TORUS_MAP.items()
            },
            "experimental_ratios": {
                "W_over_Z": float(RATIO_W_Z_EXP),
                "Z_over_H": float(RATIO_Z_H_EXP),
                "W_over_H": float(RATIO_W_H_EXP),
            },
        },
        "results_per_level": results,
        "best_level": best if valid else None,
        "interpretation": (
            "Best (k, N) combination by total |deviation| across 3 SM "
            "ratios. A clear minimum at one k indicates the substrate-"
            "natural RT level for the torus chain. If multiple k give "
            "similar low deviation, the level is degenerate / determined "
            "by additional structure. If no k matches, the RT chain "
            "needs structural enrichment (Pentagon-coherent state-sum, "
            "Chern-Simons partition function on Seifert-fibered "
            "manifold, etc.)."
        ),
        "status": "exploratory",
        "tags": [
            "rt-route",
            "level-selection",
            "root-of-unity",
            "cross-particle-ratios",
            "bring-genus",
            "electroweak",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "rt-route-root-of-unity-level-scan.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
