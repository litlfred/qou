"""Q5/§5#2: W = √[2]_q probe — does the quantum-dim spinor norm close W's gap?

Per `docs/audits/2026-05-24-rt-route-research-frontiers-w-correction-habiro-heegaard.md`
§1, the empirical W-correction is ≈ 1.43 (close to √2 = 1.414). The
categorical candidate origin is $\sqrt{[2]_q}$ at $q_0$ — the quantum
dimension of the SU_q(2) fundamental rep, which couples to the W's
charge ±1.

This probe:

1. Computes $\sqrt{[2]_q}$ at substrate $q_0$
2. Applies it as a multiplicative correction to W's |J_N| at multiple N
3. Reports the corrected W absolute mass + W/Z, W/H ratios
4. Verifies whether this single categorical factor closes W's gap

If $\sqrt{[2]_{q_0}}$ gives W ratios within 5% (matching the existing
Z/H precision), the categorical W correction is identified.
Otherwise, a different categorical origin is needed.

Status: EXPLORATORY.
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
M_E_MEV = mpf("0.510998950")
M_W_MEV = mpf("80379.0")
M_Z_MEV = mpf("91187.6")
M_H_MEV = mpf("125100.0")

RATIO_W_Z_EXP = M_W_MEV / M_Z_MEV
RATIO_W_H_EXP = M_W_MEV / M_H_MEV
RATIO_Z_H_EXP = M_Z_MEV / M_H_MEV


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
    print("W = √[2]_q quantum-spinor correction probe")
    print(f"50-dps mpmath; q_0 = {Q_0}")
    print("=" * 80)

    # The conjectured correction factor
    bracket_2_q0 = abs(quantum_integer(2, Q_0))
    sqrt_bracket_2 = mp.sqrt(bracket_2_q0)
    print(f"\n[2]_q at q_0 = {float(bracket_2_q0):.8f}")
    print(f"√[2]_q at q_0 = {float(sqrt_bracket_2):.8f}")
    print(f"√2 (pure)    = {float(mp.sqrt(2)):.8f}")
    print(f"Δ (sqrt[2]_q - √2) = {float(sqrt_bracket_2 - mp.sqrt(2)):+.8f}")

    # Test at multiple N
    N_values = [2, 3, 4, 5, 6]
    print(f"\nTesting correction factor C_W = √[2]_q ≈ {float(sqrt_bracket_2):.4f} on W only")
    print("=" * 80)

    results = []
    for N in N_values:
        j_W = abs(colored_jones_T2n(N, 4, Q_0))
        j_Z = abs(colored_jones_T2n(N, 6, Q_0))
        j_H = abs(colored_jones_T2n(N, 8, Q_0))

        # Apply correction to W only
        j_W_corrected = j_W * sqrt_bracket_2

        # Ratios with correction
        wz_corr = float(j_W_corrected / j_Z)
        zh_corr = float(j_Z / j_H)
        wh_corr = float(j_W_corrected / j_H)

        d_wz = (wz_corr - float(RATIO_W_Z_EXP)) / float(RATIO_W_Z_EXP) * 100
        d_zh = (zh_corr - float(RATIO_Z_H_EXP)) / float(RATIO_Z_H_EXP) * 100
        d_wh = (wh_corr - float(RATIO_W_H_EXP)) / float(RATIO_W_H_EXP) * 100
        total_dev = abs(d_wz) + abs(d_zh) + abs(d_wh)

        print(f"\nN = {N}")
        print(f"  Uncorrected |J_W| = {float(j_W):.4f}")
        print(f"  Corrected   |J_W|·√[2]_q = {float(j_W_corrected):.4f}")
        print(f"  W/Z = {wz_corr:.4f} (target {float(RATIO_W_Z_EXP):.4f}, dev {d_wz:+.2f}%)")
        print(f"  Z/H = {zh_corr:.4f} (target {float(RATIO_Z_H_EXP):.4f}, dev {d_zh:+.2f}%)")
        print(f"  W/H = {wh_corr:.4f} (target {float(RATIO_W_H_EXP):.4f}, dev {d_wh:+.2f}%)")
        print(f"  Total |dev| = {total_dev:.2f}%")

        # Absolute m_W prediction at this N: m_e · |J_W_corrected| · X for various X
        # Take same N factor as for Higgs at N=8: |J|·N·m_e or |J|·N²·m_e
        m_W_pred_JN = float(j_W_corrected * N * M_E_MEV)
        m_W_pred_JN2 = float(j_W_corrected * N ** 2 * M_E_MEV)
        m_W_pred_J = float(j_W_corrected * M_E_MEV)

        ratio_JN = m_W_pred_JN / float(M_W_MEV)
        ratio_JN2 = m_W_pred_JN2 / float(M_W_MEV)
        ratio_J = m_W_pred_J / float(M_W_MEV)
        print(f"  Absolute m_W pred:")
        print(f"    |J|·m_e        = {m_W_pred_J:.2f} MeV  (ratio {ratio_J:.4f} × m_W)")
        print(f"    |J|·N·m_e      = {m_W_pred_JN:.2f} MeV  (ratio {ratio_JN:.4f} × m_W)")
        print(f"    |J|·N²·m_e     = {m_W_pred_JN2:.2f} MeV  (ratio {ratio_JN2:.4f} × m_W)")

        results.append({
            "N": N,
            "J_W_uncorrected": float(j_W),
            "J_W_corrected": float(j_W_corrected),
            "J_Z": float(j_Z),
            "J_H": float(j_H),
            "ratio_W_over_Z_pred": wz_corr,
            "ratio_W_over_Z_exp": float(RATIO_W_Z_EXP),
            "ratio_Z_over_H_pred": zh_corr,
            "ratio_Z_over_H_exp": float(RATIO_Z_H_EXP),
            "ratio_W_over_H_pred": wh_corr,
            "ratio_W_over_H_exp": float(RATIO_W_H_EXP),
            "deviation_W_over_Z_pct": d_wz,
            "deviation_Z_over_H_pct": d_zh,
            "deviation_W_over_H_pct": d_wh,
            "total_abs_deviation_pct": total_dev,
            "m_W_pred_J_m_e_MeV": m_W_pred_J,
            "m_W_pred_J_N_m_e_MeV": m_W_pred_JN,
            "m_W_pred_J_N2_m_e_MeV": m_W_pred_JN2,
        })

    # Best N
    best = min(results, key=lambda r: r["total_abs_deviation_pct"])
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    print(f"Best N with √[2]_q correction: N = {best['N']}, total |dev| = {best['total_abs_deviation_pct']:.2f}%")
    print(f"  W/Z = {best['ratio_W_over_Z_pred']:.4f} (dev {best['deviation_W_over_Z_pct']:+.2f}%)")
    print(f"  Z/H = {best['ratio_Z_over_H_pred']:.4f} (dev {best['deviation_Z_over_H_pct']:+.2f}%)")
    print(f"  W/H = {best['ratio_W_over_H_pred']:.4f} (dev {best['deviation_W_over_H_pct']:+.2f}%)")

    if best["total_abs_deviation_pct"] < 10:
        print(f"\n→ STRONG: √[2]_q correction closes W's gap within 10% on all ratios.")
        print(f"  Categorical W-correction identified as √[2]_q (= quantum spinor norm).")
    elif best["total_abs_deviation_pct"] < 25:
        print(f"\n→ MODERATE: partial closure; structural pattern present but quantitative")
        print(f"  offset remains. The √[2]_q candidate is suggestive but incomplete.")
    else:
        print(f"\n→ WEAK: √[2]_q correction doesn't close W's gap. Different categorical")
        print(f"  origin needed (charge-coupling, spinor structure with additional q-factor).")

    # Witness
    witness = {
        "compute": "rt_w_sqrt_quantum_two_probe",
        "description": (
            "Tests whether √[2]_q at q_0 (quantum dim of SU_q(2) "
            "fundamental rep, coupling to W's charge ±1) is the "
            "structural origin of the empirical W-correction ≈ 1.43 "
            "found in rt_route_w_specific_correction_probe.py. Applies "
            "this single multiplicative factor to W's |J_N| for "
            "N = 2..6 and checks whether ratios match SM within 10%."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "bracket_2_q0": float(bracket_2_q0),
            "sqrt_bracket_2_q0": float(sqrt_bracket_2),
            "sqrt_2_pure": float(mp.sqrt(2)),
            "N_values_tested": N_values,
        },
        "results_per_N": results,
        "best": best,
        "interpretation": (
            "If √[2]_q correction gives total |dev| < 10%, the "
            "categorical W-correction is identified as the quantum "
            "spinor norm. This would provide a categorical derivation "
            "matching the SM ratios (modulo the absolute mass scale, "
            "which remains an open structural question for the RT "
            "chain)."
        ),
        "status": "exploratory",
        "tags": [
            "rt-route",
            "w-correction",
            "sqrt-quantum-two",
            "categorical-spinor-norm",
            "electroweak",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "rt-w-sqrt-quantum-two-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
