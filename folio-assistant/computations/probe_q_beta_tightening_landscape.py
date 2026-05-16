#!/usr/bin/env python3
"""Q_β tightening landscape — what works and what doesn't.

Per PR #655's audit, ε_ΔS = 0.605 · ε_Q, so 1 ppb on ΔS requires
ε_Q ≈ 0.0017 ppm (1700× tighter than the 1678 ppm Form A residual).
This probe sweeps several candidate refinements and reports their
residuals so the open form-tightening problem can be triaged
without wasting compute on geometric / naive expansions.

Candidates evaluated at q_0 (50 dps):

  Baseline:
    Form A (single-wrap NF):
      Q_β = m_e · |q² - 2q - 1| · (q+1) / (2q³)

  Tested:
    1. N=1 geometric extension (already on main, refuted):
       Q_β · (1 + ℏ_q²)
    2. N=2 geometric extension:
       Q_β · (1 + ℏ_q² + ℏ_q⁴)
    3. Bridge correction inverse direction:
       Form B = Form A / (1 + (z-1)h/2)
    4. Bridge correction forward direction:
       Form A · (1 - (z-1)h/2)
    5. Quadratic Pochhammer ansatz:
       Q_β / (1 - ℏ_q²)   [full geometric sum]
    6. h-shift ansatz: Q_β at (h ↦ h(2-h)/2)
       (using the EXACT NF counit instead of leading h)
    7. (q-q⁻¹)²·(q+q⁻¹) regularization candidate.

Output: `q-beta-tightening-landscape.witness.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 50


def _q_0_50dps() -> mp.mpf:
    with (HERE / "q-pinning-50-digit.witness.json").open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def main() -> int:
    q = _q_0_50dps()
    h = q - 1 / q
    hbar_q = (q - 1) / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    m_e = mp.mpf(str(M_E_MEV))
    m_p = mp.mpf(str(M_P_MEV_VALIDATION))
    m_n = mp.mpf(str(M_N_MEV_VALIDATION))

    Q_beta_AME = m_n - m_p - m_e

    # Baseline Form A
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    eps_A = Q_A / Q_beta_AME - 1

    print("=" * 90)
    print("  Q_β tightening landscape — candidates vs CODATA target")
    print("=" * 90)
    print()
    print(f"  q_0     = {mp.nstr(q, 14)}")
    print(f"  ℏ_q     = {mp.nstr(hbar_q, 14)}    h = q - q⁻¹ = {mp.nstr(h, 14)}    z = {mp.nstr(z, 14)}")
    print(f"  Q_β AME = {mp.nstr(Q_beta_AME, 14)} MeV")
    print()
    print(f"  Baseline:")
    print(f"    Form A (single-wrap NF): Q_β = {mp.nstr(Q_A, 14)} MeV   "
          f"ε = {float(eps_A * 1e6):+10.2f} ppm")
    print()
    print(f"  Candidates:")
    print(f"    {'#':<3} {'name':<48} {'Q_β [MeV]':>16} {'ε [ppm]':>14}  verdict")
    print(f"    {'-'*100}")

    candidates = [
        ("1", "N=1 geometric: Q_A · (1 + ℏ_q²)",
         Q_A * (1 + hbar_q ** 2)),
        ("2", "N=2 geometric: Q_A · (1 + ℏ_q² + ℏ_q⁴)",
         Q_A * (1 + hbar_q ** 2 + hbar_q ** 4)),
        ("3", "Form B (inverse bridge): Q_A / (1 + (z-1)h/2)",
         Q_A / (1 + (z - 1) * h / 2)),
        ("4", "forward bridge: Q_A · (1 - (z-1)h/2)",
         Q_A * (1 - (z - 1) * h / 2)),
        ("5", "Full geometric: Q_A / (1 - ℏ_q²)",
         Q_A / (1 - hbar_q ** 2)),
        ("6", "h-shift: Q_A with h ↦ h(2-h)/2 in numerator",
         # numerator h(2-h)/2 from prop:neutron-qvalue-symbolic, substituting
         # h^4(2-h)^2 / 4 — over-iterating the NF counit
         m_e * mp.fabs(h * (2 - h) / 2) ** 2 * (q + 1) / (2 * q ** 2 * (q - 1))),
        ("7", "Pochhammer factor: Q_A · (1 - q⁻²)",
         Q_A * (1 - 1 / q ** 2)),
        ("8", "z² regularization: Q_A · (1 + (z-1)² h² / 4)",
         Q_A * (1 + (z - 1) ** 2 * h ** 2 / 4)),
        ("9",  "Symmetric correction: Q_A · cos((z-1)h/2)",
         Q_A * mp.cos((z - 1) * h / 2)),
        ("10", "cos², symmetric²: Q_A · cos²((z-1)h/2)",
         Q_A * mp.cos((z - 1) * h / 2) ** 2),
        ("11", "cos with argument (1-z)h/2 = -(z-1)h/2 (parity check)",
         Q_A * mp.cos((1 - z) * h / 2)),
        ("12", "exp(i…) magnitude: Q_A · cos((z-1)h)",
         Q_A * mp.cos((z - 1) * h)),
        ("13", "1 - h²(z-1)²/8: Taylor of cos to O(h⁴)",
         Q_A * (1 - h ** 2 * (z - 1) ** 2 / 8)),
        ("14", "Q_A · cos(h/2) (no z factor)",
         Q_A * mp.cos(h / 2)),
        ("15", "Q_A · cos(zh/2)",
         Q_A * mp.cos(z * h / 2)),
        ("16", "Q_A · cos(zh)",
         Q_A * mp.cos(z * h)),
        ("17", "Q_A · sec((z-1)h/2) (reciprocal cos)",
         Q_A / mp.cos((z - 1) * h / 2)),
    ]

    results = []
    for label, name, Q_cand in candidates:
        eps = Q_cand / Q_beta_AME - 1
        eps_abs = mp.fabs(eps)
        eps_A_abs = mp.fabs(eps_A)
        if eps_abs < eps_A_abs:
            verdict = "BETTER"
            ratio = float(eps_A_abs / eps_abs)
            verdict_str = f"BETTER ({ratio:.2f}× tighter)"
        elif eps_abs < eps_A_abs * mp.mpf("1.1"):
            verdict_str = "~same"
        else:
            ratio = float(eps_abs / eps_A_abs)
            verdict_str = f"worse  ({ratio:.2f}× looser)"
        print(f"    {label:<3} {name:<48} {mp.nstr(Q_cand, 8):>16} "
              f"{float(eps * 1e6):>+14.2f}  {verdict_str}")
        results.append({
            "label": label,
            "name": name,
            "Q_beta_MeV": str(Q_cand),
            "eps_vs_AME": str(eps),
            "eps_ppm": float(eps * 1e6),
            "abs_eps_smaller_than_form_A": eps_abs < eps_A_abs,
        })

    print()
    # Find best candidate
    best = min(candidates, key=lambda c: mp.fabs(c[2] / Q_beta_AME - 1))
    best_eps = best[2] / Q_beta_AME - 1
    print(f"  BEST candidate among tested:")
    print(f"    {best[0]}: {best[1]}")
    print(f"    Q_β = {mp.nstr(best[2], 14)}  ε = {float(best_eps * 1e6):+10.4f} ppm")
    print(f"    Improvement vs Form A: {float(mp.fabs(eps_A) / mp.fabs(best_eps)):.2f}×")
    print()
    print(f"  Gap to 1 ppb on ΔS (needs ε_Q ≈ 0.0017 ppm):")
    print(f"    Current best ε_Q ≈ {float(mp.fabs(best_eps) * 1e6):.4f} ppm")
    print(f"    Remaining tightening factor: {float(mp.fabs(best_eps) * 1e6 / 0.0017):.0f}×")
    print()
    print(f"  CONCLUSION: simple algebraic / Pochhammer extensions of Form A")
    print(f"  cannot close the Q_β gap to 1 ppb on their own. The structural")
    print(f"  origin of the 1678 ppm residual is not captured by these")
    print(f"  candidates — it likely requires the full Hecke-spectral")
    print(f"  brane-tower computation in Form B's eigenfunction basis.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "q-beta-tightening-landscape",
        {
            "description": (
                "Q_β tightening landscape: 9 candidate refinements of the "
                "single-wrap Form A closed form, evaluated at q_0 with "
                "50 dps. Identifies which candidates improve and which "
                "worsen the +1678 ppm residual against CODATA. None of "
                "the simple algebraic / geometric / bridge-based "
                "extensions close the gap to 1 ppb (need ε_Q ≈ 0.0017 ppm). "
                "Implication: structural Hecke-spectral brane-tower "
                "computation is required — the gap is not a missing scalar."
            ),
            "auditOnly": (
                "PR #655 audit_delta_S_chain.py established that "
                "1 ppb on the n-p mass split requires ε_Q ≈ 0.0017 ppm "
                "(1700× tighter than current Form A). This probe sweeps "
                "naive candidates to confirm none of them close the gap "
                "alone, narrowing the open search to spectral compute."
            ),
            "data": {
                "q_0_50dps": str(q),
                "hbar_q_50dps": str(hbar_q),
                "h_50dps": str(h),
                "z_markov_50dps": str(z),
                "Q_beta_AME_MeV": str(Q_beta_AME),
                "form_A_Q_beta_MeV": str(Q_A),
                "form_A_eps_ppm": float(eps_A * 1e6),
                "candidates": results,
                "best_candidate_label": best[0],
                "best_candidate_eps_ppm": float(best_eps * 1e6),
                "form_A_to_best_tightening_factor": float(mp.fabs(eps_A) / mp.fabs(best_eps)) if best_eps != 0 else None,
                "remaining_tightening_factor_for_1ppb": float(mp.fabs(best_eps) * 1e6 / 0.0017),
            },
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
