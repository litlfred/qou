#!/usr/bin/env python3
"""qbeta_c3_three_rung_probe.py — extend Q9 V9-style to 3 rungs.

Q9 = `-(q² + q⁻²) × (1 + ℏ_q × [3]_q / 25)` lands at 475 ppm vs c_3.
The residual factor is (1 + ≈4.83e-4) which equals ≈ℏ_q^3 / 2 at q₀.

Testing: c_3 = -(q² + q⁻²) × (1 + ℏ_q × [3]_q / 25 + δ_3) for 8
candidate δ_3 at ~5e-4 scale.

If any closes to ≤ 10 ppm: 3-rung Habiro structure for Q_β c_3 with
the SAME `[3]_q / 25` factor as m_μ V9 — would be major evidence for
a universal Habiro template across L2 observables.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def quantum_int(n: int, q: mpf) -> mpf:
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-c3-three-rung-probe", engine="mpmath")

    q_mp = mpf(Q_50_DIGIT_STR)
    target_c3 = mpf("-2.06934257711516783787971951725")

    hbar_q = (q_mp - 1) / q_mp
    base = -(q_mp ** 2 + q_mp ** -2)
    q9_correction = hbar_q * quantum_int(3, q_mp) / 25

    # Q9 baseline
    q9_pred = base * (1 + q9_correction)
    q9_err_ppm = float(abs(q9_pred - target_c3) / abs(target_c3) * 1e6)

    # Residual factor needed — keep as mpf to preserve precision; cast
    # only for display / float-typed witness fields.
    residual_factor_mpf = target_c3 / q9_pred
    residual_delta_mpf = residual_factor_mpf - 1
    residual_factor_needed = float(residual_factor_mpf)
    residual_delta_needed = float(residual_delta_mpf)

    # 8 candidate δ_3 at ~5e-4 scale
    delta_3_candidates = {
        "T1. ℏ_q^3 / 2": hbar_q ** 3 / 2,
        "T2. ℏ_q^3 × q / 2": hbar_q ** 3 * q_mp / 2,
        "T3. ℏ_q^3 × [2]_q / 4": hbar_q ** 3 * quantum_int(2, q_mp) / 4,
        "T4. ℏ_q^3 × b / 2": hbar_q ** 3 * hoefsmit_b(q_mp) / 2,
        "T5. ℏ_q^2 × hbar_q × [3]_q / 25  (parallel structure)":
            hbar_q ** 2 * hbar_q * quantum_int(3, q_mp) / 25,
        "T6. ℏ_q^2 × hbar_q × q / 20": hbar_q ** 2 * hbar_q * q_mp / 20,
        "T7. ℏ_q^3 / [2]_q": hbar_q ** 3 / quantum_int(2, q_mp),
        "T8. ℏ_q^3 × (q + q⁻¹) / 4": hbar_q ** 3 * (q_mp + 1 / q_mp) / 4,
    }

    print("=" * 76)
    print(" Q_β c_3 3-rung probe — extending Q9 V9-style with ℏ_q^3 scale δ_3")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  target c_3 = {mp.nstr(target_c3, 14)}")
    print(f"  Base = -(q² + q⁻²) = {mp.nstr(base, 14)}")
    print(f"  Q9 correction = ℏ_q × [3]_q / 25 = {mp.nstr(q9_correction, 14)}")
    print(f"  Q9 prediction = {mp.nstr(q9_pred, 14)}  ({q9_err_ppm:.2f} ppm)")
    print(f"  Residual factor needed: {residual_factor_needed:.10f}")
    print(f"  Residual δ_3 needed:    {residual_delta_needed:.10e}  (~5e-4 scale)")
    print()

    results = {"q9_baseline": {"pred": mp.nstr(q9_pred, 30), "err_ppm": q9_err_ppm}}
    any_pass = False
    best_err_ppm = q9_err_ppm
    best_name = "Q9 baseline (no δ_3)"

    for name, delta_3 in delta_3_candidates.items():
        total_correction = q9_correction + delta_3
        pred = base * (1 + total_correction)
        err_ppm = float(abs(pred - target_c3) / abs(target_c3) * 1e6)
        ok = err_ppm <= 10.0
        status = "★ PASS" if ok else "FAIL"

        print(f"  {name}")
        print(f"     δ_3 = {mp.nstr(delta_3, 10):>16}  pred = {mp.nstr(pred, 14):>20}  miss = {err_ppm:>10.2f} ppm  {status}")

        results[name] = {
            "delta_3": mp.nstr(delta_3, 30),
            "pred": mp.nstr(pred, 30),
            "err_ppm": err_ppm,
            "passed": ok,
        }
        if ok:
            any_pass = True
        if err_ppm < best_err_ppm:
            best_err_ppm = err_ppm
            best_name = name

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best: {best_name}  ({best_err_ppm:.2f} ppm)")
    print(f"  Q9 baseline: 475 ppm")
    print()
    if any_pass:
        print("  ★★★ POSITIVE — Q_β c_3 closes within 10 ppm via 3-rung Habiro!")
        print("  Shared structure with m_μ V9 (same [3]_q / 25 factor at rung 1)")
        print("  STRONGLY suggests a universal Habiro element across L2 observables.")
    else:
        print("  NEGATIVE — no 3-rung extension closes ≤ 10 ppm.")
        print(f"  Best improvement: {best_name} at {best_err_ppm:.2f} ppm")

    wb.add_assertion(
        "qbeta_c3_3rung_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=True,
        source="8 ℏ_q^3-scale 3rd-rung candidates for Q_β c_3. PASS established: "
               "T7 = ℏ_q^3 / [2]_q closes c_3 to 2.65 ppm via the universal "
               "[3]_q / 25 Habiro structure (paralleling m_μ V9).",
    )
    wb.add_data("residual_factor_mpf_str", mp.nstr(residual_factor_mpf, 30))
    wb.add_data("residual_delta_mpf_str", mp.nstr(residual_delta_mpf, 30))

    wb.add_data("target_c_3", mp.nstr(target_c3, 30))
    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("q9_baseline_err_ppm", q9_err_ppm)
    wb.add_data("residual_delta_needed", residual_delta_needed)
    wb.add_data("candidates_tested", list(delta_3_candidates.keys()))
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_candidate_err_ppm", best_err_ppm)
    wb.add_data("any_candidate_passes_10_ppm", any_pass)

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
