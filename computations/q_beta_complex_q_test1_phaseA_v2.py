#!/usr/bin/env python3
"""
Phase A v2 of Test 1 from PR #1127 — Apollonius parametrization.

CAL-2 (|m_μ/m_e|) constrains q to an APOLLONIUS CIRCLE in ℂ:
  Vol(4_1) · |q|² / |q-1|² = 206.7682830  # noqa: P31 — docstring; Apollonius-circle target statement
  =>  |q-1| / |q| = √(Vol_4_1 / cal2_target)

The Apollonius locus {q : |q-1|/|q| = k} for 0 < k ≠ 1 is a circle
in the complex plane with:
  center = 1 / (1 - k²)  on the real axis
  radius = k / |1 - k²|

Parametrize q(θ) = center + radius · e^(iθ); CAL-2 holds for all θ.
Then CAL-3 becomes a 1D problem in θ:
  g(θ) := |Q_β(q(θ))| - 0.78233341 MeV
  Q_β(q) = m_e · |(q² − 2q − 1)(q+1) / (2q³)|   (ansatz, full modulus)

Scan θ ∈ [0, 2π], locate zeros of g(θ). The real solution is at θ ≈ 0
(or θ = π if q maps to negative real axis); complex solutions at
other θ values are the Schrödinger-moment candidates.

Audit-only; ansatz-dependent per PR #1127 fitting-finding audit.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402


def main() -> int:
    mp.mp.dps = 50

    # Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 53 digits, correct to 19 (qou-ckbv)
    Vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    cal2_target = M_MU_OVER_M_E
    cal3_target = mp.mpf("0.78233341")
    m_e = mp.mpf("0.51099895000")

    # Apollonius circle from CAL-2
    k_sq = Vol_4_1 / cal2_target           # = (|q-1| / |q|)²
    k = mp.sqrt(k_sq)
    one_minus_k_sq = 1 - k_sq
    center = 1 / one_minus_k_sq
    radius = k / mp.fabs(one_minus_k_sq)

    print("=== Apollonius circle from CAL-2 ===")
    print(f"  k² = Vol(4_1) / 206.7682830  = {float(k_sq):.10f}")  # noqa: P31 — descriptive print of CAL-2 target in Apollonius diagnostic
    print(f"  k  = |q-1| / |q|             = {float(k):.10f}")
    print(f"  Circle center (real axis)    = {float(center):.10f}")
    print(f"  Circle radius                = {float(radius):.10f}")
    print(f"  Real-axis intercepts:")
    print(f"     q_+ = center + radius     = {float(center + radius):.10f}")
    print(f"     q_- = center - radius     = {float(center - radius):.10f}")
    print()

    # Verify Apollonius parametrization
    def q_on_circle(theta_mpf):
        return mp.mpc(center, 0) + radius * mp.exp(mp.mpc(0, 1) * theta_mpf)

    # Verify at θ=0: should give canonical q_0
    q0_check = q_on_circle(mp.mpf("0"))
    cal2_q0 = Vol_4_1 * mp.fabs(q0_check)**2 / mp.fabs(q0_check - 1)**2
    print(f"  Verification at θ=0: q={complex(q0_check)}, CAL-2 = {float(cal2_q0):.10f} (target {float(cal2_target):.10f}, diff {float(cal2_q0 - cal2_target):+.2e})")
    print()

    # CAL-3 residual on the circle: g(θ) = |Q_β(q(θ))| - cal3_target
    def cal3_residual(theta_mpf):
        q = q_on_circle(theta_mpf)
        num = (q*q - 2*q - 1) * (q + 1)
        den = 2 * q**3
        q_beta = m_e * mp.fabs(num / den)
        return q_beta - cal3_target

    # Scan θ ∈ [0, 2π] with N points; locate sign changes
    print("=== CAL-3 residual scan on Apollonius circle ===")
    N = 360                                  # 1-degree resolution for sign-change scan
    thetas = [mp.mpf(i) * 2 * mp.pi / N for i in range(N + 1)]
    residuals = []
    for theta in thetas:
        try:
            r = cal3_residual(theta)
            residuals.append((theta, r, float(r)))
        except Exception:
            residuals.append((theta, None, None))

    # Print every 30th sample for the verbose user
    print(f"  θ (deg)     q (complex)                                |Q_β| (MeV)     residual (MeV)")
    for i in range(0, N + 1, 30):
        theta, r, rf = residuals[i]
        q = q_on_circle(theta)
        deg = float(theta) * 180 / 3.141592653589793
        print(f"  {deg:7.1f}    {float(q.real):+.8f} {float(q.imag):+.8f}j     {float(cal3_target + r):.8f}      {rf:+.6e}")

    # Locate sign changes (= zeros of g(θ))
    print()
    print("=== Sign changes of g(θ) on the circle ===")
    sign_changes = []
    for i in range(N):
        _, r1, rf1 = residuals[i]
        _, r2, rf2 = residuals[i + 1]
        if rf1 is None or rf2 is None:
            continue
        if rf1 * rf2 < 0:
            sign_changes.append((i, thetas[i], thetas[i + 1], rf1, rf2))
            deg1 = float(thetas[i]) * 180 / 3.141592653589793
            deg2 = float(thetas[i + 1]) * 180 / 3.141592653589793
            print(f"  sign change between θ={deg1:.2f}° and θ={deg2:.2f}° (residuals {rf1:+.2e} → {rf2:+.2e})")

    if not sign_changes:
        print(f"  NO SIGN CHANGES found in {N} samples — g(θ) has constant sign on the circle.")
        # Show min |residual|
        min_idx = min(range(N + 1), key=lambda i: abs(residuals[i][2]) if residuals[i][2] is not None else float('inf'))
        theta_min = thetas[min_idx]
        r_min = residuals[min_idx][2]
        deg_min = float(theta_min) * 180 / 3.141592653589793
        print(f"  Closest approach at θ={deg_min:.2f}°: residual = {r_min:+.6e} MeV")

    # Refine each sign change to high precision
    print()
    print("=== Refined zeros (mpmath findroot, 50 dps) ===")
    refined = []
    for idx, t1, t2, _, _ in sign_changes:
        try:
            theta_zero = mp.findroot(lambda t: cal3_residual(t), (t1 + t2) / 2, tol=mp.mpf("1e-40"))
            q_zero = q_on_circle(theta_zero)
            r_check = cal3_residual(theta_zero)
            cal2_check = Vol_4_1 * mp.fabs(q_zero)**2 / mp.fabs(q_zero - 1)**2 - cal2_target
            refined.append({
                "theta": str(theta_zero),
                "theta_deg": float(theta_zero) * 180 / 3.141592653589793,
                "q_real": str(q_zero.real),
                "q_imag": str(q_zero.imag),
                "cal2_residual": str(cal2_check),
                "cal3_residual_MeV": str(r_check),
                "abs_q": str(mp.fabs(q_zero)),
                "is_real_axis": float(mp.fabs(q_zero.imag)) < 1e-15,
            })
            deg = float(theta_zero) * 180 / 3.141592653589793
            print(f"  θ = {deg:+.6f}°  =>  q = {float(q_zero.real):+.10f} + {float(q_zero.imag):+.10f}i")
            print(f"     CAL-2 residual = {float(cal2_check):+.4e}   CAL-3 residual = {float(r_check):+.4e} MeV")
            print(f"     |q| = {float(mp.fabs(q_zero)):.10f}, on-axis = {float(mp.fabs(q_zero.imag)) < 1e-15}")
        except Exception as e:
            print(f"  refinement failed at θ ∈ [{float(t1)}, {float(t2)}]: {e}")

    # Classify
    n_real = sum(1 for r in refined if r["is_real_axis"])
    n_complex = sum(1 for r in refined if not r["is_real_axis"])

    print()
    print(f"=== Outcome ===")
    print(f"  Real-axis solutions:   {n_real}")
    print(f"  Complex solutions:     {n_complex}")
    if n_real == 0 and n_complex == 0:
        outcome = "d"
        outcome_msg = "NO joint solution found anywhere on the Apollonius circle — ansatz cannot simultaneously fit CAL-2 + CAL-3 for ANY complex q"
    elif n_real >= 1 and n_complex == 0:
        outcome = "a"
        outcome_msg = "Only real-axis solution(s); no complex q closes both CAL-2 + CAL-3 under this ansatz"
    elif n_complex >= 1 and n_real == 0:
        outcome = "c"
        outcome_msg = "ONLY complex solution(s) — Schrödinger-moment candidate"
    elif n_real >= 1 and n_complex >= 1:
        outcome = "(a)+(c)"
        outcome_msg = "Both real and complex solutions — ansatz UNDER-determines q"
    else:
        outcome = "b"
        outcome_msg = "Multiple real solutions, no complex — degenerate"

    print(f"  Outcome class: ({outcome})")
    print(f"  {outcome_msg}")

    witness = {
        "description": "Test 1 Phase A v2 — Apollonius parametrization on (CAL-2, CAL-3) for complex q under Q_β ansatz",
        "computation": "q_beta_complex_q_test1_phaseA_v2",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "method": "1D parametrization on CAL-2 Apollonius circle; CAL-3 residual scanned on the circle then refined at sign changes",
            "source_audits": [
                "docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md",
                "docs/audits/2026-05-24-complex-q-historical-trajectory.md",
            ],
            "ansatz_form": "Q_β(q) = m_e · |(q²−2q−1)(q+1)/(2q³)|",
            "ansatz_status": "ANSATZ (per pre-archimedean-derivation-chain.md:391 'by construction')",
        },
        "constants": {
            "Vol_4_1": str(Vol_4_1),
            "cal2_target_m_mu_over_m_e": str(cal2_target),
            "cal3_target_Q_beta_MeV": str(cal3_target),
            "m_e_MeV": str(m_e),
        },
        "apollonius_circle": {
            "k_squared": str(k_sq),
            "k": str(k),
            "center_real": str(center),
            "radius": str(radius),
            "real_axis_intercepts": [str(center + radius), str(center - radius)],
        },
        "scan": {
            "N_samples": N,
            "n_sign_changes": len(sign_changes),
        },
        "refined_zeros": refined,
        "summary": {
            "n_real": n_real,
            "n_complex": n_complex,
            "outcome_class": outcome,
            "outcome_description": outcome_msg,
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "q-beta-complex-q-test1-phasea-v2", witness,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\nWitness: {out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
