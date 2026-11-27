#!/usr/bin/env python3
"""mmu_categorical_correction_refined_probe.py — m_μ refined δ search.

Follow-up to `mmu_categorical_correction_first_probe.py` (PR #1781).
The first probe's best candidate D2 = `ℏ_q^6 × b / 4` lands at 2.05e-7
vs target 2.10e-7 (2.2% off). The `1/4` factor is ad-hoc.

This refined probe tests the natural family `ℏ_q^6 / X(q)` where X(q) is
a canonical categorical denominator (quantum integer [k]_q, hook-length
products, Wedderburn-block dimension sums, etc.). The ℏ_q^6 numerator
is the natural categorical scale at the right order of magnitude
(~9.4e-7 at q₀). The denominator family is principled:

Candidates tested at proton-pinned q₀:

  R1.  ℏ_q^6 / [2]_q
  R2.  ℏ_q^6 / [3]_q
  R3.  ℏ_q^6 / [4]_q  (closest to ad-hoc 1/4 from D2)
  R4.  ℏ_q^6 / [5]_q
  R5.  ℏ_q^6 / (q + q⁻¹ + 1)  (Hopf-symmetric 3-sum)
  R6.  ℏ_q^6 × b / (q + 1)  (Hoefsmit-modulated 2-sum)
  R7.  ℏ_q^6 / ([2]_q · [3]_q)  (product of quantum integers)
  R8.  ℏ_q^6 / Vol(4_1)  (the production formula's own constant)
  R9.  ℏ_q^6 × q  (next h-order shift)
  R10. ℏ_q^4 × ℏ_q²/(q+q⁻¹)  (mixed)

Target δ = 2.098e-7. Tolerance: 10 ppm.

The probe extends the m_μ search bracket. Δ_λ-gate compliant.
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
from knot_volumes import vol_at  # noqa: E402 — canonical volume registry

# Vol(4_1) is EXCISED, not corrected (bean qou-ckbv, 2026-08-30).
# This file carried VOL_4_1_STR = "2.0298832128193072500115970029" -- 29
# digits printed, 19 correct, the same 20-digit carrier bean qou-f8lit
# tracks. Vol(4_1) has a closed form, 2*Cl_2(pi/3); a literal for it can
# only ever be a truncation of something the machine can compute exactly,
# so the fix is deletion rather than re-transcription.


def quantum_int(n: int, q: mpf) -> mpf:
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


# Candidate δ(q) refinements
def r1(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / quantum_int(2, q)


def r2(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / quantum_int(3, q)


def r3(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / quantum_int(4, q)


def r4(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / quantum_int(5, q)


def r5(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / (q + 1 / q + 1)


def r6(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * hoefsmit_b(q) / (q + 1)


def r7(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / (quantum_int(2, q) * quantum_int(3, q))


def r8(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / vol_at("4_1")


def r9(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * q / 5


def r10(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 4 * hbar ** 2 / (q + 1 / q)


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-categorical-correction-refined-probe", engine="mpmath")

    q_mp = Q_MP
    target_delta = mpf("2.098e-7")

    candidates = {
        "R1. hbar^6 / [2]_q": r1,
        "R2. hbar^6 / [3]_q": r2,
        "R3. hbar^6 / [4]_q": r3,
        "R4. hbar^6 / [5]_q": r4,
        "R5. hbar^6 / (q + q^-1 + 1)": r5,
        "R6. hbar^6 * b / (q + 1)": r6,
        "R7. hbar^6 / ([2]_q * [3]_q)": r7,
        "R8. hbar^6 / Vol(4_1)": r8,
        "R9. hbar^6 * q / 5": r9,
        "R10. hbar^4 * hbar^2 / (q + q^-1)": r10,
    }

    print("=" * 76)
    print(" m_μ refined δ probe — 10 hbar_q^6 / X(q) candidates")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  Target δ = {mp.nstr(target_delta, 8)}")
    print(f"  Tolerance: 10 ppm (closes m_μ to ≤10 ppb)")
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
        print(f"     δ_pred = {mp.nstr(value, 12):>22}  miss: {err_ppm:>12.2f} ppm  {status}")

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
        print("  POSITIVE — natural categorical denominator family identifies a")
        print("  candidate δ within 10 ppm of target. This closes m_μ to ≤10 ppb.")
    else:
        print("  NEGATIVE — no ℏ_q^6 / [k]_q family member matches within 10 ppm.")
        print("  The best refinement narrows the gap but doesn't close it.")
        print("  Cumulative m_μ NEGATIVE bracket: 8 (first-probe) + 10 (refined) = 18.")

    wb.add_assertion(
        "mmu_refined_correction_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="10 ℏ_q^6 / X(q) candidates tested where X is a canonical "
               "categorical denominator (quantum integer, Hopf-sum, etc.). "
               "PASS would identify a structurally-derived m_μ correction.",
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
