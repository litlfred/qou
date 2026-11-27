#!/usr/bin/env python3
"""qbeta_c3_v9_style_probe.py — Q_β c_3 with V9-style Habiro pattern.

The m_μ R9+V9 closure (PR #1781) revealed a Habiro-like structure:
  δ_total = (leading rung) × (1 + ℏ_q² × [3]_q / 5)

Apply the same structure to the Q_β c_3 problem (residue A; 34-
candidate NEGATIVE bracket per PR #1773):

  c_3 = J_Hopf × (1 + r(q) × Habiro_correction(q) / N^k)

where:
  - J_Hopf(q=1) = -2 is the categorical leading factor
  - Habiro correction has scale 0.0347 = (c_3/J_Hopf - 1)
  - N is the categorical denominator (5 for cinquefoil; 6 for Borromean?)

12 V9-style candidates for c_3 at proton-pinned q₀:

  Q1. -2 × (1 + ℏ_q × q / 5)
  Q2. -2 × (1 + ℏ_q × q / 6)
  Q3. -2 × (1 + ℏ_q × [3]_q / 25)
  Q4. -2 × (1 + ℏ_q² × q / 5)
  Q5. -2 × (1 + ℏ_q² × [4]_q / 1)
  Q6. -2 × (1 + h × q / 6)     (h = q - q⁻¹)
  Q7. -2 × (1 + h × [3]_q / 25)
  Q8. -(q² + q⁻²) × (1 + ℏ_q² × q / 5)   (start from best 15-cand re-run)
  Q9. -(q² + q⁻²) × (1 + ℏ_q × [3]_q / 25)
  Q10. -2 × (1 + ℏ_q × b × q / 5)        (Hoefsmit-modulated)
  Q11. -2 × (1 + ℏ_q² × J_Hopf'(q₀))     (q-deformed Hopf derivative)
  Q12. -2 + ℏ_q² × b × q²                (additive, not multiplicative)

Target: c_3 ≈ -2.06934 (cal-anchored).
Tolerance: 10 ppm (closes Q_β c_3 to derived tier).

If any PASS: would suggest Q_β residue A IS structurally analogous to
m_μ V9 closure — closing both observables via the same Habiro
framework.
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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def quantum_int(n: int, q: mpf) -> mpf:
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-c3-v9-style-probe", engine="mpmath")

    q_mp = Q_MP
    target_c3 = mpf("-2.06934257711516783787971951725")
    j_hopf = mpf(-2)

    def q1(q):
        hb = (q - 1) / q
        return j_hopf * (1 + hb * q / 5)

    def q2(q):
        hb = (q - 1) / q
        return j_hopf * (1 + hb * q / 6)

    def q3(q):
        hb = (q - 1) / q
        return j_hopf * (1 + hb * quantum_int(3, q) / 25)

    def q4(q):
        hb = (q - 1) / q
        return j_hopf * (1 + hb ** 2 * q / 5)

    def q5(q):
        hb = (q - 1) / q
        return j_hopf * (1 + hb ** 2 * quantum_int(4, q))

    def q6(q):
        hh = q - 1 / q
        return j_hopf * (1 + hh * q / 6)

    def q7(q):
        hh = q - 1 / q
        return j_hopf * (1 + hh * quantum_int(3, q) / 25)

    def q8(q):
        hb = (q - 1) / q
        return -(q ** 2 + q ** -2) * (1 + hb ** 2 * q / 5)

    def q9(q):
        hb = (q - 1) / q
        return -(q ** 2 + q ** -2) * (1 + hb * quantum_int(3, q) / 25)

    def q10(q):
        hb = (q - 1) / q
        return j_hopf * (1 + hb * hoefsmit_b(q) * q / 5)

    def q11(q):
        hb = (q - 1) / q
        # J_Hopf'(q) at q=1: derivative of (-(q^(1/2)+q^(-1/2))(q^(3/2)+q^(-3/2)))
        # = -d/dq[(q^(1/2)+q^(-1/2))(q^(3/2)+q^(-3/2))]
        # Approximate numerically as (J_Hopf(q+eps) - J_Hopf(q-eps))/(2eps)
        eps = mpf("1e-15")

        def jh(qx):
            return -(qx ** mpf("0.5") + qx ** mpf("-0.5")) * (qx ** mpf("1.5") + qx ** mpf("-1.5"))

        j_prime = (jh(q + eps) - jh(q - eps)) / (2 * eps)
        return j_hopf * (1 + hb ** 2 * j_prime)

    def q12(q):
        hb = (q - 1) / q
        return -mpf(2) + hb ** 2 * hoefsmit_b(q) * q ** 2

    candidates = {
        "Q1.  -2 × (1 + ℏ_q × q / 5)": q1,
        "Q2.  -2 × (1 + ℏ_q × q / 6)": q2,
        "Q3.  -2 × (1 + ℏ_q × [3]_q / 25)": q3,
        "Q4.  -2 × (1 + ℏ_q² × q / 5)": q4,
        "Q5.  -2 × (1 + ℏ_q² × [4]_q)": q5,
        "Q6.  -2 × (1 + h × q / 6)": q6,
        "Q7.  -2 × (1 + h × [3]_q / 25)": q7,
        "Q8.  -(q² + q⁻²) × (1 + ℏ_q² × q / 5)": q8,
        "Q9.  -(q² + q⁻²) × (1 + ℏ_q × [3]_q / 25)": q9,
        "Q10. -2 × (1 + ℏ_q × b × q / 5)": q10,
        "Q11. -2 × (1 + ℏ_q² × J_Hopf'(q))": q11,
        "Q12. -2 + ℏ_q² × b × q²  (additive)": q12,
    }

    print("=" * 76)
    print(" Q_β c_3 V9-style probe — Habiro pattern from m_μ closure")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  target c_3 = {mp.nstr(target_c3, 14)}")
    print(f"  Best in 34-cand bracket so far: -(q²+q⁻²) at 9,109 ppm m_p-pin")
    print()

    results = {}
    any_pass = False
    best_err_ppm = float("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            value = formula(q_mp)
            err_ppm = float(abs(value - target_c3) / abs(target_c3) * 1e6)
            ok = err_ppm <= 10.0
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            value = mpf("nan")
            err_ppm = float("inf")
            ok = False
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     pred = {mp.nstr(value, 12):>22}  miss: {err_ppm:>14.2f} ppm  {status}")

        results[name] = {
            "computed": mp.nstr(value, 30) if not mp.isnan(value) else "nan",
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
    print()
    if any_pass:
        print("  ★ POSITIVE — V9-style Habiro pattern closes Q_β c_3!")
        print("  This would link m_μ closure (PR #1781) with Q_β residue A closure.")
    else:
        print("  NEGATIVE — V9-style structure does NOT close Q_β c_3.")
        print(f"  Best is {best_err_ppm:.0f} ppm vs 9,109 ppm prior best.")
        print()
        print("  Implication: the m_μ V9 closure pattern is observable-specific,")
        print("  NOT a universal Habiro template. Q_β residue A genuinely requires")
        print("  its own categorical search (or upstream-infra path per PR #1770).")

    wb.add_assertion(
        "qbeta_c3_v9_style_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="12 V9-style Habiro candidates for c_3. PASS would link m_μ closure "
               "and Q_β residue A via a universal Habiro template.",
    )

    wb.add_data("target_c_3", mp.nstr(target_c3, 30))
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
