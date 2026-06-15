#!/usr/bin/env python3
"""mmu_categorical_correction_k_crossing_probe.py — k-crossing hypothesis.

Follow-up to `mmu_categorical_correction_refined_probe.py`. R9 candidate
`ℏ_q^6 × q / 5` landed at 1,152 ppm — 20× improvement over the first
probe. The "5" in "/5" coincides with the crossing number of the muon
torus knot T(2,5) = cinquefoil per the lepton T(2,n) tower
(electron=T(2,3), muon=T(2,5), tau=T(2,7)).

This probe tests the **k-crossing hypothesis**:

    δ_m_lepton(q) = ℏ_q^6 × q / k_crossing(K_lepton)

where k_crossing is the crossing number of the lepton's torus knot.

For the muon (T(2,5), k=5), the candidate is R9 = `ℏ_q^6 × q / 5`
landing at 1,152 ppm — close but FAIL the 10 ppm gate.

Extending the test with variants around the k-crossing structure to
see whether any landing at ≤ 10 ppm.

12 candidates tested at proton-pinned q₀:

  K1.  ℏ_q^6 × q / 5  (R9 baseline)
  K2.  ℏ_q^6 × q² / 5
  K3.  ℏ_q^6 × q⁻¹ / 5  (anti-symmetric variant)
  K4.  ℏ_q^6 × (q + q⁻¹) / 10
  K5.  ℏ_q^6 × [2]_q / 10
  K6.  ℏ_q^6 × q / [5]_q
  K7.  ℏ_q^6 × q × b² / 5
  K8.  ℏ_q^6 × q × b / (b² + 1) / 5  (Hoefsmit-modulated)
  K9.  ℏ_q^6 × √q / 5 (q^(1/2))
  K10. ℏ_q^6 × q² / [5]_q
  K11. ℏ_q^6 × (q² - q⁻²) / (q - q⁻¹) / 5
  K12. ℏ_q^6 × [5]_{q^(1/2)} / 25  (half-spin variant)

If any matches: STRUCTURAL HIT (cinquefoil-correction confirmed).
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


def k1(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * q / 5


def k2(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * q ** 2 / 5


def k3(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / q / 5


def k4(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * (q + 1 / q) / 10


def k5(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * quantum_int(2, q) / 10


def k6(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * q / quantum_int(5, q)


def k7(q: mpf) -> mpf:
    hbar = (q - 1) / q
    b = hoefsmit_b(q)
    return hbar ** 6 * q * b ** 2 / 5


def k8(q: mpf) -> mpf:
    hbar = (q - 1) / q
    b = hoefsmit_b(q)
    return hbar ** 6 * q * b / (b ** 2 + 1) / 5


def k9(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * sqrt(q) / 5


def k10(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * q ** 2 / quantum_int(5, q)


def k11(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * (q ** 2 - q ** -2) / (q - 1 / q) / 5  # = [2]_{q²} / 5


def k12(q: mpf) -> mpf:
    hbar = (q - 1) / q
    qhalf = sqrt(q)
    # [5]_{q^(1/2)} = (q^(5/2) - q^(-5/2))/(q^(1/2) - q^(-1/2))
    five_qhalf = (qhalf ** 5 - qhalf ** -5) / (qhalf - 1 / qhalf)
    return hbar ** 6 * five_qhalf / 25


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-categorical-correction-k-crossing-probe", engine="mpmath")

    q_mp = mpf(Q_50_DIGIT_STR)
    target_delta = mpf("2.098e-7")

    candidates = {
        "K1.  hbar_q^6 * q / 5 (R9 baseline)": k1,
        "K2.  hbar_q^6 * q^2 / 5": k2,
        "K3.  hbar_q^6 * q^-1 / 5": k3,
        "K4.  hbar_q^6 * (q + q^-1) / 10": k4,
        "K5.  hbar_q^6 * [2]_q / 10": k5,
        "K6.  hbar_q^6 * q / [5]_q": k6,
        "K7.  hbar_q^6 * q * b^2 / 5": k7,
        "K8.  hbar_q^6 * q * b / (b^2+1) / 5": k8,
        "K9.  hbar_q^6 * sqrt(q) / 5": k9,
        "K10. hbar_q^6 * q^2 / [5]_q": k10,
        "K11. hbar_q^6 * [2]_{q^2} / 5": k11,
        "K12. hbar_q^6 * [5]_{q^(1/2)} / 25": k12,
    }

    print("=" * 76)
    print(" m_μ k-crossing hypothesis probe — 12 candidates")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  Target δ = {mp.nstr(target_delta, 8)}")
    print(f"  R9 baseline: 1,152 ppm  (the 'k=5' coincides with T(2,5) crossing count)")
    print()

    results = {}
    any_pass = False
    best_err_rel = mpf("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            value = formula(q_mp)
            err_rel = abs(value - target_delta) / target_delta
            err_ppm = float(err_rel) * 1e6
            ok = err_ppm <= 10.0
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            value = mpf("nan")
            err_rel = mpf("inf")
            err_ppm = float("inf")
            ok = False
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     delta = {mp.nstr(value, 12):>20}  miss: {err_ppm:>14.2f} ppm  {status}")

        results[name] = {
            "computed_delta": mp.nstr(value, 30) if not mp.isnan(value) else "nan",
            "err_ppm_vs_target": err_ppm,
            "passed": ok,
        }
        if ok:
            any_pass = True
        if err_rel < best_err_rel:
            best_err_rel = err_rel
            best_name = name

    best_err_ppm = float(best_err_rel) * 1e6

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best candidate: {best_name}  ({best_err_ppm:.2f} ppm)")
    print()
    if any_pass:
        print("  POSITIVE — k-crossing structural form matches within 10 ppm.")
    else:
        print("  NEGATIVE — no k-crossing variant lands within 10 ppm.")
        print()
        print(f"  Cumulative m_μ NEGATIVE bracket: 8 + 10 + 12 = 30 candidates.")
        print(f"  Best so far: {best_name if float(best_err_rel) * 1e6 < 1152 else 'R9 (1,152 ppm)'}")

    wb.add_assertion(
        "k_crossing_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="12 k-crossing-hypothesis variants tested against target δ ≈ 2.098e-7. "
               "The R9 'q/5' baseline (1,152 ppm) suggests cinquefoil-crossing structure; "
               "PASS would confirm structural cinquefoil correction for muon.",
    )

    wb.add_data("target_delta", mp.nstr(target_delta, 30))
    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("candidates_tested", list(candidates.keys()))
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
