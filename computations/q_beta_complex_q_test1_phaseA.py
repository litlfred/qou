#!/usr/bin/env python3
"""
Phase A of Test 1 from PR #1127 / Path D Hermiticity audit.

Solve simultaneously for complex `q = u + iv ∈ ℂ`:

  CAL-2: |m_μ/m_e (q)|   =  Vol(4_1) · |q|² / |q − 1|²   =  206.7682830  # noqa: P31 — docstring; CAL-2/CAL-3 target statement
  CAL-3: |Q_β(q)|        =  m_e · |(q² − 2q − 1)(q+1) / (2q³)|  =  0.78233341 MeV

The Q_β closed form is the ANSATZ extension of
`prop:neutron-qvalue-symbolic` to complex q (with the sign-fixing |·|
promoted to a full modulus per the Born / P_avg projection per
`bar-involution.md`).

Outcomes (per audit doc):
  (a) only the real solution (~1.110, 0) — ansatz unique at real axis
  (b) multiple real solutions — degenerate
  (c) only complex solution(s) with v ≠ 0 — Schrödinger-moment candidate
      for the framework's q ∈ ℂ trajectory (per the historical-trajectory
      audit)
  (d) no solution — mass formulas inconsistent at the third decimal

This is the user-prioritized "decisive next step" in PR #1127's chat
2026-05-24, per the Path D / historical-trajectory reconciliation.

Audit-only; no production wiring. Witness: q-beta-complex-q-test1-phasea.witness.json.
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
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()

    # Constants (CODATA 2022 + hyperbolic volume of figure-eight)
    Vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)  # Vol(4_1) EXACT = 2*Cl_2(pi/3).
    # The literal here printed 53 digits and was correct to 20; dps is
    # raised above, so the closed form is exact (bean qou-ckbv).
    cal2_target = M_MU_OVER_M_E           # m_μ / m_e
    cal3_target = mp.mpf("0.78233341")            # Q_β(n) MeV
    m_e = mp.mpf("0.51099895000")                 # m_e MeV

    def cal2_observable(q):
        """|m_μ/m_e (q)| = Vol(4_1) · |q|² / |q-1|² under modulus projection."""
        return Vol_4_1 * mp.fabs(q)**2 / mp.fabs(q - 1)**2

    def q_beta_observable(q):
        """|Q_β(q)| as ansatz closed form, full modulus per P_avg projection.

        Q_β(q) = m_e · (q² − 2q − 1)(q + 1) / (2 q³)   (complex-valued)
        Observable = |Q_β(q)|.

        For real q ≈ 1.110, (q² − 2q − 1) ≈ −1.988 < 0, so |·| yields the
        sign-fixed real value 0.7836 MeV (+0.17% vs CODATA 0.78233).  # noqa: P31 — docstring; CODATA comparison note
        """
        num = (q*q - 2*q - 1) * (q + 1)
        den = 2 * q**3
        return m_e * mp.fabs(num / den)

    def joint_residual(u, v):
        """Returns [r_cal2(u,v), r_cal3(u,v)] for the simultaneous fit."""
        q = mp.mpc(u, v)
        return [
            cal2_observable(q) - cal2_target,
            q_beta_observable(q) - cal3_target,
        ]

    # Real-axis baseline: u ≈ 1.10998, v = 0
    print("=== Real-axis baseline (sanity check) ===")
    u0 = mp.mpf("1.10998")
    q0 = mp.mpc(u0, 0)
    print(f"  q_real = {u0} + 0i")
    print(f"  CAL-2 observable   = {float(cal2_observable(q0)):.8f}   (target {float(cal2_target):.8f})")
    print(f"  CAL-2 residual     = {float(cal2_observable(q0) - cal2_target):+.6e}")
    print(f"  CAL-3 observable   = {float(q_beta_observable(q0)):.8f} MeV   (target {float(cal3_target):.8f} MeV)")
    print(f"  CAL-3 residual     = {float(q_beta_observable(q0) - cal3_target):+.6e} MeV   (expected +0.0013, the +0.17%)")
    print()

    # Refine the real solution to match CAL-2 exactly (this gives the canonical q_0)
    def cal2_only_real(u):
        return cal2_observable(mp.mpc(u, 0)) - cal2_target
    u_real = mp.findroot(cal2_only_real, mp.mpf("1.110"), tol=mp.mpf("1e-45"))
    print(f"=== Canonical real q_0 from CAL-2 alone ===")
    print(f"  q_0 (real, CAL-2 fit)        = {u_real}")
    print(f"  CAL-3 residual at q_0 (real) = {float(q_beta_observable(mp.mpc(u_real, 0)) - cal3_target):+.6e} MeV")
    print(f"                               = {float((q_beta_observable(mp.mpc(u_real, 0)) - cal3_target) / cal3_target * 100):+.4f}%")
    print()

    # Phase A: search for complex (u, v) solutions to BOTH equations.
    # Use multi-D findroot with several starting guesses.
    print("=== Joint (CAL-2 + CAL-3) search over complex q-plane ===")

    starting_points = [
        ("real (v=0 start)",         mp.mpf("1.11"),  mp.mpf("0.0")),
        ("near-real v=+0.001",       mp.mpf("1.11"),  mp.mpf("0.001")),
        ("v=+0.01",                  mp.mpf("1.11"),  mp.mpf("0.01")),
        ("v=+0.05",                  mp.mpf("1.11"),  mp.mpf("0.05")),
        ("v=+0.1",                   mp.mpf("1.11"),  mp.mpf("0.1")),
        ("v=−0.05",                  mp.mpf("1.11"),  mp.mpf("-0.05")),
        ("u=1.05, v=+0.05",          mp.mpf("1.05"),  mp.mpf("0.05")),
        ("u=1.15, v=+0.05",          mp.mpf("1.15"),  mp.mpf("0.05")),
        ("u=1.05, v=+0.20",          mp.mpf("1.05"),  mp.mpf("0.20")),
        ("u=0.95, v=+0.20",          mp.mpf("0.95"),  mp.mpf("0.20")),
        ("u=1.20, v=+0.20",          mp.mpf("1.20"),  mp.mpf("0.20")),
        ("u=1.30, v=+0.30",          mp.mpf("1.30"),  mp.mpf("0.30")),
        ("|q|=1 region: u=0.7,v=0.7",mp.mpf("0.7"),   mp.mpf("0.7")),
    ]

    results = []
    seen = []  # solutions found (to deduplicate)

    for label, u_start, v_start in starting_points:
        try:
            sol = mp.findroot(
                lambda u, v: joint_residual(u, v),
                (u_start, v_start),
                tol=mp.mpf("1e-40"),
                maxsteps=200,
            )
            u_sol, v_sol = sol[0], sol[1]
            q_sol = mp.mpc(u_sol, v_sol)
            r1 = cal2_observable(q_sol) - cal2_target
            r2 = q_beta_observable(q_sol) - cal3_target
            r1f, r2f = float(r1), float(r2)
            converged = (abs(r1f) < 1e-30) and (abs(r2f) < 1e-30)

            # Deduplicate against already-found solutions
            is_dup = False
            for u_seen, v_seen in seen:
                if mp.fabs(u_sol - u_seen) < mp.mpf("1e-20") and mp.fabs(v_sol - v_seen) < mp.mpf("1e-20"):
                    is_dup = True
                    break

            results.append({
                "start_label": label,
                "u_start": str(u_start),
                "v_start": str(v_start),
                "u": str(u_sol),
                "v": str(v_sol),
                "cal2_residual": str(r1),
                "cal3_residual_MeV": str(r2),
                "converged": converged,
                "duplicate_of_earlier": is_dup,
            })
            if converged and not is_dup:
                seen.append((u_sol, v_sol))

            tag = "DUP" if is_dup else ("✓" if converged else "?")
            print(f"  {tag}  {label:32s}  u={float(u_sol):+.10f}  v={float(v_sol):+.10f}   (r1={r1f:+.2e}, r2={r2f:+.2e})")
        except Exception as e:
            results.append({
                "start_label": label,
                "u_start": str(u_start),
                "v_start": str(v_start),
                "error": str(e),
            })
            print(f"  ✗  {label:32s}  FAILED — {e}")

    # Classify outcome
    unique_solutions = [(u, v) for u, v in seen]
    real_solutions = [(u, v) for u, v in unique_solutions if mp.fabs(v) < mp.mpf("1e-15")]
    complex_solutions = [(u, v) for u, v in unique_solutions if mp.fabs(v) >= mp.mpf("1e-15")]

    print()
    print(f"=== Outcome classification ===")
    print(f"  Unique converged solutions:  {len(unique_solutions)}")
    print(f"    real-axis (v ≈ 0):         {len(real_solutions)}")
    print(f"    complex (|v| > 1e-15):     {len(complex_solutions)}")

    if len(unique_solutions) == 0:
        outcome = "d"
        outcome_msg = "no joint solution found — mass formulas inconsistent at third decimal under the ansatz"
    elif len(real_solutions) >= 1 and len(complex_solutions) == 0:
        outcome = "a"
        outcome_msg = "only real solution(s) — the ansatz cannot simultaneously fit CAL-2 + CAL-3 at the real axis (+0.17% residual stands); no complex q closes it under THIS ansatz"
    elif len(complex_solutions) >= 1 and len(real_solutions) == 0:
        outcome = "c"
        outcome_msg = "ONLY complex solution(s) — Schrödinger-moment candidate under the ansatz"
    elif len(real_solutions) >= 1 and len(complex_solutions) >= 1:
        outcome = "(a)+(c)"
        outcome_msg = "BOTH real and complex solutions exist — the system is genuinely under-determined; CAL-2 + CAL-3 is not enough to fix q ∈ ℂ uniquely"
    else:
        outcome = "b"
        outcome_msg = "multiple real solutions only — degenerate"

    print(f"\n  Outcome class: ({outcome})")
    print(f"  {outcome_msg}")
    print()

    if real_solutions:
        print("  Real solution(s):")
        for u, v in real_solutions:
            print(f"    q = {u} + 0i")
    if complex_solutions:
        print("  Complex solution(s):")
        for u, v in complex_solutions:
            print(f"    q = {u} + {v}i   (|q|={mp.sqrt(u*u + v*v)}, arg={mp.atan2(v, u)})")

    # Emit witness
    witness = {
        "description": "Test 1 Phase A — simultaneous (CAL-2, CAL-3) fit for complex q under the Q_β ansatz",
        "computation": "q_beta_complex_q_test1_phaseA",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "source_audits": [
                "docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md",
                "docs/audits/2026-05-24-complex-q-historical-trajectory.md",
            ],
            "coordination_ledger": "docs/coordination/2026-05-24-q-beta-fitting-and-complex-q.md",
            "pr": "https://github.com/litlfred/qou/pull/1127",
            "sibling_pr_relevant": "https://github.com/litlfred/qou/pull/1153",
            "ansatz_form": "Q_β(q) = m_e · |(q²−2q−1)(q+1)/(2q³)|  (full modulus per P_avg projection)",
            "ansatz_status": "ANSATZ (per pre-archimedean-derivation-chain.md:391 'by construction')",
            "projection_rule": "P_avg (bar-symmetric) per bar-involution.md; complex q components in P_skew are discarded by |·|",
        },
        "constants": {
            "Vol_4_1": str(Vol_4_1),
            "cal2_target_m_mu_over_m_e": str(cal2_target),
            "cal3_target_Q_beta_MeV": str(cal3_target),
            "m_e_MeV": str(m_e),
        },
        "real_axis_baseline": {
            "q_real_canonical": str(u_real),
            "cal3_residual_MeV_at_q_real": str(q_beta_observable(mp.mpc(u_real, 0)) - cal3_target),
            "cal3_residual_percent_at_q_real": str(float((q_beta_observable(mp.mpc(u_real, 0)) - cal3_target) / cal3_target * 100)),
        },
        "search_results": results,
        "unique_solutions": [
            {"u": str(u), "v": str(v), "is_complex": mp.fabs(v) >= mp.mpf("1e-15")}
            for u, v in unique_solutions
        ],
        "summary": {
            "n_unique_solutions": len(unique_solutions),
            "n_real_solutions": len(real_solutions),
            "n_complex_solutions": len(complex_solutions),
            "outcome_class": outcome,
            "outcome_description": outcome_msg,
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    here = Path(__file__).resolve().parent
    out = here / "q-beta-complex-q-test1-phasea.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
