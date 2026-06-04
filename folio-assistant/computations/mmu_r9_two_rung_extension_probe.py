#!/usr/bin/env python3
"""mmu_r9_two_rung_extension_probe.py — R9 + ℏ_q^8 second-rung extension.

R9 = ℏ_q^6 × q / 5 reduces m_μ miss from 970× to 5.16×. The 5.16× is
because R9 over-corrects: prediction is BELOW CODATA by 1.12 ppb (R9
subtracted 210.0 ppb from a bare 211.16 ppb excess; net residual -1.12
ppb).

To close from 5.16× to 1× (or better), need an additional correction of
~+1.12 ppb (positive shift) — i.e. reduce the magnitude of δ by ~9e-9.
This is exactly the ℏ_q^8 scale (~9.2e-9 at q₀).

A 2-rung Habiro-element-style structure:

    m_μ_pred = m_e × Vol(4_1) / ℏ_q² × (1 - δ_1 - δ_2)

where δ_1 = ℏ_q^6 × q / 5 (R9 first rung) and δ_2 is a small positive
correction at ℏ_q^8 scale that reduces over-correction.

10 candidates for the second rung δ_2 (each subtracts ~9e-9 worth of
correction from R9):

  T1.  +ℏ_q^8
  T2.  +ℏ_q^8 × b
  T3.  -ℏ_q^8 / q
  T4.  +ℏ_q^8 × q
  T5.  +ℏ_q^8 / [2]_q
  T6.  +ℏ_q^8 × q² / 5  (parallel to R9)
  T7.  +ℏ_q^8 / [3]_q
  T8.  -ℏ_q^7 × (q-1)
  T9.  +ℏ_q^6 × ℏ_q² × q / 25  (cross-product)
  T10. +ℏ_q^8 × (q + q⁻¹) / 10

For each combined δ = R9 - T_i, compute the resulting m_μ prediction
err vs CODATA. PASS if miss factor ≤ 1× (closes 100× L2 gate).
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

VOL_4_1_STR = "2.0298832128193072500115970029"
M_E_CODATA_MEV = "0.51099895069"
M_MU_CODATA_MEV = "105.6583755"
M_MU_SIGMA_EXP_MEV = "2.3e-6"


def quantum_int(n: int, q: mpf) -> mpf:
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


# Second-rung δ_2 candidates (sign carries the direction of correction)
def t1(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8


def t2(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 * hoefsmit_b(q)


def t3(q: mpf) -> mpf:
    return -((q - 1) / q) ** 8 / q


def t4(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 * q


def t5(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 / quantum_int(2, q)


def t6(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 * q ** 2 / 5


def t7(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 / quantum_int(3, q)


def t8(q: mpf) -> mpf:
    return -((q - 1) / q) ** 7 * (q - 1)


def t9(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 * q / 25


def t10(q: mpf) -> mpf:
    return ((q - 1) / q) ** 8 * (q + 1 / q) / 10


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-r9-two-rung-extension-probe", engine="mpmath")

    q_mp = mpf(Q_50_DIGIT_STR)
    me = mpf(M_E_CODATA_MEV)
    m_mu_codata = mpf(M_MU_CODATA_MEV)
    sigma_exp = mpf(M_MU_SIGMA_EXP_MEV)
    vol_4_1 = mpf(VOL_4_1_STR)

    hbar_q = (q_mp - 1) / q_mp
    hbar_q_sq = hbar_q ** 2

    delta_r9 = hbar_q ** 6 * q_mp / 5

    sigma_exp_ppb = float(sigma_exp / m_mu_codata * 1e9)
    target_100x_ppb = sigma_exp_ppb / 100

    candidates = {
        "T1.  +hbar_q^8": t1,
        "T2.  +hbar_q^8 * b": t2,
        "T3.  -hbar_q^8 / q": t3,
        "T4.  +hbar_q^8 * q": t4,
        "T5.  +hbar_q^8 / [2]_q": t5,
        "T6.  +hbar_q^8 * q^2 / 5  (R9-parallel)": t6,
        "T7.  +hbar_q^8 / [3]_q": t7,
        "T8.  -hbar_q^7 * (q-1)": t8,
        "T9.  +hbar_q^6 * hbar^2 * q / 25  (R9 * hbar^2)": t9,
        "T10. +hbar_q^8 * (q + q^-1) / 10": t10,
    }

    print("=" * 76)
    print(" m_μ R9 + ℏ_q^8 second-rung extension — 10 candidates")
    print("=" * 76)
    print(f"  q₀         = {mp.nstr(q_mp, 14)}")
    print(f"  R9 baseline: 5.16× miss (1.12 ppb residual, OVER-correcting)")
    print(f"  Target: close to ≤1× (≤0.2177 ppb residual)")
    print()

    # Baseline R9 prediction (no second rung)
    m_mu_r9 = me * vol_4_1 / hbar_q_sq * (1 - delta_r9)
    r9_err_ppb = float((m_mu_r9 - m_mu_codata) / m_mu_codata * 1e9)
    r9_miss = float(abs(r9_err_ppb) / target_100x_ppb)
    print(f"  R9-only:    err = {r9_err_ppb:+.4f} ppb  miss = {r9_miss:.2f}× (baseline)")
    print()

    results = {"r9_baseline": {"err_ppb": r9_err_ppb, "miss_factor": r9_miss}}
    any_pass = False
    best_miss = r9_miss
    best_name = "R9-only baseline"

    for name, formula in candidates.items():
        try:
            delta_2 = formula(q_mp)
            # Combined δ = R9 + δ_2: R9 alone leaves m_μ_pred 1.12 ppb ABOVE
            # CODATA (positive residual under `1 - delta_total` convention),
            # so the second-rung correction must INCREASE delta_total to
            # further suppress the prediction. Each candidate function
            # returns δ_2 with its intended sign; combine additively.
            delta_total = delta_r9 + delta_2
            m_mu_pred = me * vol_4_1 / hbar_q_sq * (1 - delta_total)
            err_ppb = float((m_mu_pred - m_mu_codata) / m_mu_codata * 1e9)
            miss = float(abs(err_ppb) / target_100x_ppb)
            ok = miss <= 1.0
            status = "PASS (100× L2 met)" if ok else "FAIL"
        except Exception as e:
            delta_2 = mpf("nan")
            err_ppb = float("inf")
            miss = float("inf")
            ok = False
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     δ_2 = {mp.nstr(delta_2, 10):>16}  err = {err_ppb:+.4f} ppb  miss = {miss:.3f}×  {status}")

        results[name] = {
            "delta_2": mp.nstr(delta_2, 30) if not mp.isnan(delta_2) else "nan",
            "err_ppb": err_ppb,
            "miss_factor": miss,
            "passed_100x_l2": ok,
        }
        if ok:
            any_pass = True
        if miss < best_miss:
            best_miss = miss
            best_name = name

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best candidate: {best_name}  ({best_miss:.3f}× L2 miss)")
    print(f"  R9-only baseline:  5.16× (from consistency check)")
    print()
    if any_pass:
        print("  POSITIVE — at least one R9 + ℏ_q^8 second-rung combination meets")
        print("  the 100× L2 target! This is the first single-form m_μ closure")
        print("  in the L2 closure campaign.")
        print()
        print("  Δ_λ-gate caveat: 4-parameter fit pattern (R9 + 2nd-rung structure).")
        print("  Promotion to derived tier requires Lean theorems for BOTH rungs +")
        print("  Lean-derived combinator.")
    else:
        print("  NEGATIVE — no second-rung extension closes 100× L2.")
        print(f"  Best is still {best_name} at {best_miss:.2f}× miss.")
        print()
        print(f"  Cumulative m_μ NEGATIVE bracket: 40 + 10 = 50 candidates.")

    wb.add_assertion(
        "two_rung_at_least_one_meets_100x_l2",
        computed=any_pass,
        expected=False,
        source="10 R9 + ℏ_q^8 second-rung candidates. PASS if any closes 100× L2 "
               "(≤0.2177 ppb residual). The ℏ_q^8 scale is matched to the residual "
               "1.12 ppb that R9 alone leaves.",
    )

    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("r9_baseline_miss_factor", r9_miss)
    wb.add_data("target_100x_ppb", target_100x_ppb)
    wb.add_data("candidates_tested", list(candidates.keys()))
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_miss_factor", best_miss)
    wb.add_data("any_meets_100x_l2", any_pass)

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
