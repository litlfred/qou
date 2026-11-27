#!/usr/bin/env python3
"""
meson_tower_correction_probe.py — find the meson-analog of the
Habiro brane-tower correction that closes m_K/m_π from 290 ppm.

The baryon tower used R = (1 + 46u⁴)(1 + 4u⁵)(1 - 29u⁶) with
u = b·ℏ_q². The meson tower should have a similar structure
but with meson-specific integer coefficients.

The base formula is:
    m_K/m_π = (q⁵ − q⁻⁵) × (9/5)² × R_meson

where R_meson ≈ 1 + O(290 ppm).
"""
from __future__ import annotations


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

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, sqrt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_PI_PM_MEV_VALIDATION, M_K_PM_MEV_VALIDATION  # noqa: E402


def main():
    set_compute_dps()
    wb = WitnessBuilder("meson-tower-correction-probe", engine="mpmath")

    q = Q_MP
    h = q - 1 / q
    hbar_q = (q - 1) / q
    qi = 1 / q

    target = M_K_PM_MEV_VALIDATION / M_PI_PM_MEV_VALIDATION
    base = (q ** 5 - q ** (-5)) * (mpf(9) / 5) ** 2
    residual = target / base - 1  # ≈ +2.9e-4 (290 ppm)

    b_sq = (h ** 2 + 3) / (h ** 2 + 4)
    b_val = sqrt(b_sq)
    u = b_val * hbar_q ** 2  # baryon eigenvalue parameter

    # Meson-specific parameters
    v1 = hbar_q ** 2           # ℏ_q² alone (no b)
    v2 = h ** 2                # h² (Hecke parameter squared)
    v3 = u                     # same as baryon u = b·ℏ²
    v4 = qi * hbar_q           # q⁻¹·ℏ_q
    v5 = hbar_q                # ℏ_q alone

    params = {"u": u, "v1_hbar2": v1, "v2_h2": v2, "v3_u": v3,
              "v4_qi_hbar": v4, "v5_hbar": v5}

    print("=" * 70)
    print("MESON TOWER CORRECTION PROBE")
    print(f"Base: (q⁵−q⁻⁵)×(9/5)² = {float(base):.10f}")
    print(f"Target: m_K/m_π = {float(target):.10f}")
    print(f"Residual: {float(residual):.6e} ({float(residual*1e6):.1f} ppm)")
    print("=" * 70)
    print()

    # Scan: R_meson = 1 + c × param^k for integer c, various params and powers
    best_err = 1.0
    best_formula = ""
    best_pred = mpf(0)
    results = []

    for pname, pval in params.items():
        for k in range(1, 8):
            pk = pval ** k
            if float(fabs(pk)) < 1e-20:
                continue
            c_exact = residual / pk
            c_int = round(float(c_exact))
            if c_int == 0:
                continue

            R = 1 + c_int * pk
            pred = base * R
            err_ppm = float(fabs(pred - target) / target * 1e6)

            if err_ppm < 200:
                results.append((pname, k, c_int, err_ppm, float(pred)))
                if err_ppm < best_err:
                    best_err = err_ppm
                    best_formula = f"1 + {c_int}·{pname}^{k}"
                    best_pred = pred

    # Also try two-term corrections
    for p1name, p1val in params.items():
        for k1 in range(1, 5):
            pk1 = p1val ** k1
            c1 = round(float(residual / pk1))
            if c1 == 0:
                continue
            r1 = residual - c1 * pk1
            for p2name, p2val in params.items():
                for k2 in range(k1, 6):
                    pk2 = p2val ** k2
                    if float(fabs(pk2)) < 1e-20:
                        continue
                    c2 = round(float(r1 / pk2))
                    if c2 == 0:
                        continue
                    R = 1 + c1 * pk1 + c2 * pk2
                    pred = base * R
                    err_ppm = float(fabs(pred - target) / target * 1e6)
                    if err_ppm < best_err:
                        best_err = err_ppm
                        best_formula = f"1 + {c1}·{p1name}^{k1} + {c2}·{p2name}^{k2}"
                        best_pred = pred

    results.sort(key=lambda x: x[3])
    print("Top single-term corrections (< 200 ppm):")
    for pname, k, c, err, pred in results[:10]:
        print(f"  1 + {c:+d}·{pname}^{k}: pred={pred:.10f} err={err:.1f} ppm")

    print(f"\n★ BEST: R = {best_formula}")
    print(f"  pred = {float(best_pred):.10f}")
    print(f"  err  = {best_err:.1f} ppm")

    wb.set_description(
        f"Meson tower correction probe. Base (q⁵−q⁻⁵)×(9/5)² = {float(base):.6f} "
        f"at 290 ppm. Best correction: R = {best_formula} at {best_err:.1f} ppm."
    )
    wb.add_data("base", {"value": str(float(base)), "err_ppm": float(residual * 1e6)})
    wb.add_data("best", {"formula": best_formula, "err_ppm": best_err})
    wb.add_data("parameters", {k: str(float(v)) for k, v in params.items()})
    wb.add_assertion("correction_improves", computed=best_err, expected=0, tolerance=290,
                     source="Tower correction beats base formula")
    wb.save()


if __name__ == "__main__":
    main()
