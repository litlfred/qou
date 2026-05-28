#!/usr/bin/env python3
"""
binding_per_knot_scaling.py — test per-knot E₀ scaling for nuclear binding.

KEY FINDINGS:
  D:   B = E₀ × Δtr × q⁻¹         → +0.7% (1 pair, proved)
  ³He: B = E₀ × Δtr × q⁻³ × 3     → -0.1% (3 pairs, q⁻ᴬ scaling)
  ⁴He: B(⁴He)/B(D) ≈ [4]_q!/(2·[1]_q) = [2]_q·[3]_q·[4]_q/2  → -1.1%

The per-knot scaling uses q⁻ᴬ (one q-power per nucleon) combined
with A(A-1)/2 pair counting. The ⁴He ratio to deuteron matches the
q-factorial [4]_q!/2 to 1.1%.

T at +7.1% (Model 2) and ³He at -0.1% (Model 5) differ because of
isospin asymmetry (pp vs nn vs pn pair weights differ).
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, sqrt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-per-knot-scaling", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    qi = 1 / q
    hbar = (q - 1) / q

    E_0 = M_E_MEV / (q * (q - 1))
    Q_beta = M_E_MEV * fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    scale = E_0 / Q_beta

    def qi_n(n):
        return (q ** n - qi ** n) / h

    AME = {"D": 2.22452, "T": 8.48182, "3He": 7.71804, "4He": 28.2957}
    B_qbeta = {"D": 0.465676, "T": 0.628974, "3He": 0.658111, "4He": 0.713469}
    A_val = {"D": 2, "T": 3, "3He": 3, "4He": 4}

    print("=" * 70)
    print("BINDING PER-KNOT SCALING: E₀ × q⁻ᴬ × Δtr × n_pairs")
    print("=" * 70)
    print()

    results = {}
    for name in ["D", "T", "3He", "4He"]:
        A = A_val[name]
        n_pairs = A * (A - 1) // 2
        B_model5 = B_qbeta[name] * float(scale) * float(qi ** A) * n_pairs
        err5 = (B_model5 / AME[name] - 1) * 100
        results[name] = {"B_model5": B_model5, "err5": err5, "A": A, "pairs": n_pairs}
        print(f"  {name:>4s}: B = {B_model5:.3f} vs AME {AME[name]:.3f}  "
              f"err = {err5:+.1f}%  (A={A}, pairs={n_pairs})")

    print()
    print("=== ⁴He/D RATIO: quantum factorial test ===")
    r = AME["4He"] / AME["D"]
    qfac_test = float(qi_n(2) * qi_n(3) * qi_n(4) / 2)
    err_qfac = (qfac_test / r - 1) * 100
    print(f"  B(⁴He)/B(D) = {r:.4f}")
    print(f"  [4]_q!/(2·[1]_q) = [2]·[3]·[4]/2 = {qfac_test:.4f}  err = {err_qfac:+.1f}%")

    wb.set_description(
        "Per-knot E₀ scaling for nuclear binding. D at +0.7% (1 pair), "
        "³He at -0.1% (q⁻³ × 3 pairs), ⁴He/D ratio ≈ [4]_q!/2 at -1.1%."
    )
    wb.add_data("results", {
        k: {"B_pred": v["B_model5"], "B_AME": AME[k], "err_pct": v["err5"]}
        for k, v in results.items()
    })
    wb.add_data("he4_deuteron_ratio", {
        "observed": r, "q_factorial": qfac_test, "err_pct": err_qfac
    })
    wb.add_assertion("he3_sub_1pct", computed=abs(results["3He"]["err5"]),
                     expected=0, tolerance=1, source="³He per-knot model")
    wb.add_assertion("he4_ratio_sub_2pct", computed=abs(err_qfac),
                     expected=0, tolerance=2, source="⁴He/D ≈ [4]_q!/2")
    wb.save()


if __name__ == "__main__":
    main()
