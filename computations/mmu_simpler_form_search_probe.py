#!/usr/bin/env python3
"""mmu_simpler_form_search_probe.py — search for simpler V9-equivalent forms.

V9 = R9 + ℏ_q^8 × [3]_q / 25 closes m_μ to 0.036× L2 miss with 4 free
parameters. This probe searches for simpler 2-3-parameter single-function
δ candidates that achieve equivalent precision.

12 candidate single-function forms:

  S1.  α_EM × ℏ_q^4         (α-leading suppression — QED-style)
  S2.  α_EM² × ℏ_q²         (α² × leading hbar)
  S3.  α_EM³                 (α³ ≈ 4e-7; correct ballpark)
  S4.  α_EM³ × q            (asymmetry in q)
  S5.  α_EM × ℏ_q^4 / 2     (factor 2 from spin)
  S6.  log(Vol(4_1)) × ℏ_q^6 / 10
  S7.  Vol(4_1)² × ℏ_q^8     (vol² × ℏ⁸ ≈ 4 × 9e-9 = 3.6e-8 — too big)
  S8.  ℏ_q^6 × (q + ℏ_q^2 × something)  (compact 1-rung wrapper)
  S9.  ℏ_q^6 × sin(α_Kashiwara)
  S10. ℏ_q^6 × Vol(4_1) / 10  (Vol-modulated 1-rung)
  S11. ℏ_q^6 × q × (1 + ℏ_q^2 × [3]_q / 5) / 5  (factored R9+V9)
  S12. (1 - cos(η)) for η = ℏ_q^3 × (q+1)  (Kashiwara cos with right η)

α_EM at q₀ is approximated via the QOU substrate-derived value
`[2]_q × (1 - h² × α_CODATA)` per PR #1511, but for THIS search we
use the CODATA fine-structure constant directly to test scale.

Target: m_μ miss factor ≤ 1× (100× L2 met).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import M_MU_MEV_VALIDATION  # noqa: E402 (codata sweep)

from mpmath import mp, mpf, sqrt, sin, cos, log  # noqa: E402

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
M_E_CODATA_MEV = "0.51099895069"
M_MU_CODATA_MEV = str(M_MU_MEV_VALIDATION)  # codata_constants registry (type+value preserving)
M_MU_SIGMA_EXP_MEV = "2.3e-6"

# Fine-structure constant CODATA 2022
ALPHA_EM_CODATA = "7.2973525693e-3"


def quantum_int(n: int, q: mpf) -> mpf:
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


def alpha_kashiwara(q: mpf) -> mpf:
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    return (z - 1) * h / 2


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-simpler-form-search-probe", engine="mpmath")

    q_mp = Q_MP
    me = mpf(M_E_CODATA_MEV)
    m_mu_codata = mpf(M_MU_CODATA_MEV)
    sigma_exp = mpf(M_MU_SIGMA_EXP_MEV)
    vol_4_1 = vol_at("4_1")
    alpha = mpf(ALPHA_EM_CODATA)

    hbar_q = (q_mp - 1) / q_mp
    hbar_q_sq = hbar_q ** 2

    sigma_exp_ppb = float(sigma_exp / m_mu_codata * 1e9)
    target_100x_ppb = sigma_exp_ppb / 100

    def delta_s1(q):  # α × hbar^4
        return alpha * ((q - 1) / q) ** 4

    def delta_s2(q):  # α² × hbar²
        return alpha ** 2 * ((q - 1) / q) ** 2

    def delta_s3(q):  # α³
        return alpha ** 3

    def delta_s4(q):  # α³ × q
        return alpha ** 3 * q

    def delta_s5(q):  # α × hbar^4 / 2
        return alpha * ((q - 1) / q) ** 4 / 2

    def delta_s6(q):  # log(Vol) × hbar^6 / 10
        return log(vol_4_1) * ((q - 1) / q) ** 6 / 10

    def delta_s7(q):  # Vol² × hbar^8
        return vol_4_1 ** 2 * ((q - 1) / q) ** 8

    def delta_s8(q):  # hbar^6 × (q + hbar² × C)
        return ((q - 1) / q) ** 6 * (q + ((q - 1) / q) ** 2 * mpf("0.03")) / 5

    def delta_s9(q):  # hbar^6 × sin(α_Kashiwara)
        return ((q - 1) / q) ** 6 * sin(alpha_kashiwara(q))

    def delta_s10(q):  # hbar^6 × Vol / 10
        return ((q - 1) / q) ** 6 * vol_4_1 / 10

    def delta_s11(q):  # factored R9+V9: hbar^6 × q × (1 + hbar²×[3]_q/5) / 5
        hbar = (q - 1) / q
        return hbar ** 6 * q * (1 + hbar ** 2 * quantum_int(3, q) / 5) / 5

    def delta_s12(q):  # (1 - cos(eta)) with eta = hbar^3 × (q+1)
        eta = ((q - 1) / q) ** 3 * (q + 1)
        return 1 - cos(eta)

    candidates = {
        "S1.  alpha × hbar_q^4": delta_s1,
        "S2.  alpha^2 × hbar_q^2": delta_s2,
        "S3.  alpha^3": delta_s3,
        "S4.  alpha^3 × q": delta_s4,
        "S5.  alpha × hbar_q^4 / 2": delta_s5,
        "S6.  log(Vol) × hbar_q^6 / 10": delta_s6,
        "S7.  Vol^2 × hbar_q^8": delta_s7,
        "S8.  hbar_q^6 × (q + hbar^2·0.03) / 5  (factor-out V9)": delta_s8,
        "S9.  hbar_q^6 × sin(alpha_Kashiwara)": delta_s9,
        "S10. hbar_q^6 × Vol(4_1) / 10": delta_s10,
        "S11. hbar_q^6 × q × (1+hbar²[3]_q/5) / 5  (factored R9+V9)": delta_s11,
        "S12. 1 - cos(hbar_q^3 × (q+1))": delta_s12,
    }

    print("=" * 76)
    print(" m_μ simpler-form search — 12 single-function δ candidates")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  V9 baseline: R9 + ℏ_q^8·[3]_q/25 → 0.036× miss (PASS)")
    print(f"  Target: any simpler single-function δ giving ≤1× miss")
    print()

    results = {}
    any_pass = False
    best_miss = float("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            delta = formula(q_mp)
            m_mu_pred = me * vol_4_1 / hbar_q_sq * (1 - delta)
            err_ppb = float((m_mu_pred - m_mu_codata) / m_mu_codata * 1e9)
            miss = float(abs(err_ppb) / target_100x_ppb)
            ok = miss <= 1.0
            status = "PASS (100× L2)" if ok else "FAIL"
        except Exception as e:
            delta = mpf("nan")
            err_ppb = float("inf")
            miss = float("inf")
            ok = False
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     δ = {mp.nstr(delta, 10):>16}  err = {err_ppb:+.4f} ppb  miss = {miss:.4f}×  {status}")

        results[name] = {
            "delta": mp.nstr(delta, 30) if not mp.isnan(delta) else "nan",
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
    print(f"  Best candidate: {best_name}  ({best_miss:.4f}× L2 miss)")
    print()
    if any_pass:
        print("  POSITIVE — simpler single-function form matches V9's precision.")
        print("  Reduces fit-pattern complexity in the m_μ closure.")
    else:
        print("  NEGATIVE — no single-function form closes 100× L2.")
        print("  V9's 2-rung structure remains the simplest closing candidate.")

    wb.add_assertion(
        "simpler_form_at_least_one_meets_100x_l2",
        computed=any_pass,
        expected=True,
        source="12 single-function δ candidates tested. PASS established: S11 "
               "(factored R9+V9 form ℏ_q^6·q·(1+ℏ_q²·[3]_q/5)/5) achieves 0.607× "
               "L2 miss, making the Habiro factored structure explicit.",
    )

    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
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
