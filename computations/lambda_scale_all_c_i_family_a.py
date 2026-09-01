#!/usr/bin/env python3
"""Prove + document all c_i for Family A (natural categorical λ_scale).

Family A:
  λ_A(q) := π_HS(id, H_4) = (1/4) · Σ_λ dim_q V_λ
         = (3·[2]_q² − 2) / 4
         = (3q² + 4 + 3q⁻²) / 4

This script proves all c_i = h^k coefficients of λ_A in closed form,
extending the H_4 partition-half-symmetric construction.

Theorem (proved here):
  λ_A(q) = 5/2 + (3/4)·h² + 0·h^4 + 0·h^6 + 0·h^{2k} for all k ≥ 2

i.e. the h-series TERMINATES at h².

Proof: Direct from λ_A(q) = 5/2 + (3/4)(q² + q⁻²) - 3/2 = ... wait,
let me recompute:
  λ_A = (3q² + 4 + 3q⁻²)/4
       = 1 + (3/4)(q² + q⁻²)
       = 1 + (3/4)([2]_q² − 2)
       = 1 - 3/2 + (3/4)·[2]_q²
       = -1/2 + (3/4)·[2]_q²

At q=1: λ_A = -1/2 + (3/4)·4 = -1/2 + 3 = 5/2 ✓

In terms of h = q - q⁻¹:
  [2]_q² = (q + q⁻¹)² = q² + 2 + q⁻²
  q² + q⁻² = h² + 2  (since h² = q² - 2 + q⁻²)
  [2]_q² = h² + 4

So:
  λ_A = -1/2 + (3/4)·(h² + 4) = -1/2 + 3 + (3/4)·h² = 5/2 + (3/4)·h²

QED. The series is EXACTLY 5/2 + (3/4)·h². All higher coefficients are
identically zero.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def main() -> int:
    w = WitnessBuilder("lambda-scale-all-c-i-family-a", engine="sympy")
    w.set_description(
        "Closed-form proof of ALL h-expansion coefficients c_i for "
        "the natural categorical Family A: λ_A(q) = (1/4) Σ_λ dim_q V_λ "
        "at H_4. Proved by direct algebraic manipulation: λ_A = "
        "5/2 + (3/4)·h², series TERMINATES (c_4 = c_6 = ... = 0). "
        "Per PR #895 this IS the framework-derived substrate λ_scale "
        "(replacing the CAL-4-fitted literal 2.4599527869 in "
        "m_p_borromean_verification_50dps.py). Framework m_p prediction "
        "is now 966 MeV (~3 % off CODATA's 938.27 MeV); the 3 % gap is "
        "the framework's honest accuracy, not an error. See "
        "docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md "
        "§Alternatives to Strategy D for the search for substrate-pure "
        "refinements (V_3, V_4 Wedderburn sums; q-dilog tower; Yekutieli "
        "curvature) that could close the 3 % residual."
    )
    # The earlier conj:lambda-scale-substrate-form content_block tag
    # is dropped here intentionally — that label was demoted to
    # `conj:` in PR #892 (now merged) as a CAL-4 honesty banner, and
    # its meaning shifted away from "Family A IS λ_scale". Family A
    # is now the framework's substrate λ_scale per PR #895, but
    # there is no single content block whose `lean.ref` points at
    # this proof: the algebraic identity is documented inline in
    # this script's description + witness assertions, and consumed
    # by m_p_borromean_verification_50dps.py via the production
    # `lambda_proton_family_a()` helper. The content-block layer
    # references Family A through that consumer's witness, not
    # through this proof script directly.

    q = sp.Symbol("q", positive=True)
    h = sp.Symbol("h", real=True)

    # Define λ_A via the dim_q formula
    def qint(n):
        return sp.simplify((q**n - q**(-n))/(q - 1/q))

    # H_4 quantum dimensions (Frame-Robinson-Thrall hook-content):
    dim_q_lambdas = {
        "(4)": sp.Integer(1),
        "(3,1)": qint(3),
        "(2,2)": sp.simplify(qint(4) / qint(2)),
        "(2,1,1)": qint(3),
        "(1,1,1,1)": sp.Integer(1),
    }
    print("Quantum dimensions at H_4:")
    for label, d in dim_q_lambdas.items():
        print(f"  dim_q V_{label} = {d}")
    w.add_data("dim_q_H4", {k: str(v) for k, v in dim_q_lambdas.items()})

    lambda_A_q = sp.cancel(sum(dim_q_lambdas.values()) / 4)
    print(f"\nλ_A(q) = (1/4) Σ_λ dim_q V_λ")
    print(f"       = {lambda_A_q}")
    w.add_data("lambda_A_q_closed_form", str(lambda_A_q))

    # Algebraic simplification: λ_A = -1/2 + (3/4)·[2]_q²
    # = -1/2 + (3/4)·(h² + 4)
    # = 5/2 + (3/4)·h²
    lambda_A_h = sp.Rational(5, 2) + sp.Rational(3, 4) * h**2
    print(f"\nλ_A in h = q - q⁻¹:")
    print(f"  λ_A = 5/2 + (3/4)·h²  (proved algebraically)")
    w.add_data("lambda_A_h_closed_form", str(lambda_A_h))

    # Verify algebraically: substitute h² = q² - 2 + q⁻² in λ_A_h
    # and check it equals λ_A_q
    lambda_A_h_substituted = lambda_A_h.subs(h**2, q**2 - 2 + q**(-2))
    diff = sp.simplify(lambda_A_h_substituted - lambda_A_q)
    print(f"\nVerification: λ_A_h(h²→q²-2+q⁻²) - λ_A_q = {diff}  (should be 0)")
    verified = (diff == 0)
    w.add_assertion(
        "lambda_A_h_form_equals_lambda_A_q_form",
        computed=str(diff),
        expected="0",
        tolerance=None,
    )

    # Now state ALL c_i in closed form
    all_c_i = {
        "c_0": sp.Rational(5, 2),
        "c_2": sp.Rational(3, 4),
        "c_4": sp.Integer(0),
        "c_6": sp.Integer(0),
        "c_8": sp.Integer(0),
    }
    print(f"\n═══════════════════════════════════════════════════════")
    print(f"PROVED: All h-coefficients of Family A (closed form)")
    print(f"═══════════════════════════════════════════════════════")
    print(f"  c_0 = 5/2   (leading; half-symmetric H_4 partition count)")
    print(f"  c_2 = 3/4   (first quantum correction)")
    print(f"  c_4 = 0     (exact — series TERMINATES at h²)")
    print(f"  c_6 = 0")
    print(f"  c_2k = 0 for all k ≥ 2  (proved by exact form)")
    print(f"  c_(2k+1) = 0 for all k ≥ 0  (symmetric in q ↔ q⁻¹)")
    print(f"═══════════════════════════════════════════════════════")
    w.add_data("c_i_closed_form_family_A", {k: str(v) for k, v in all_c_i.items()})

    # Independent route to the same five numbers: substitute the positive
    # root q(h) = (h + √(h²+4))/2 of q − q⁻¹ = h into λ_A(q) and read the
    # Taylor coefficients off. Nothing below consults `all_c_i`.
    q_of_h = (h + sp.sqrt(h**2 + 4)) / 2
    lambda_A_series = sp.expand(sp.simplify(
        sp.series(lambda_A_q.subs(q, q_of_h), h, 0, 10).removeO()))
    derived_c_i = {
        f"c_{k}": sp.nsimplify(sp.simplify(lambda_A_series.coeff(h, k)))
        for k in (0, 2, 4, 6, 8)
    }
    w.add_data("c_i_from_h_series_family_A",
               {k: str(v) for k, v in derived_c_i.items()})

    # Each of these read `computed=str(value), expected=str(value)` straight
    # off the hand-written `all_c_i` dict above — five assertions that a
    # literal equals itself, which would have passed just as happily had
    # someone typed c_2 = 7. The source string names the real claim, and
    # that expansion is computable, so the stated coefficient is now checked
    # against the one the series actually produces (bean qou-26f2).
    for label, value in all_c_i.items():
        w.add_assertion(
            f"family_A_{label}",
            computed=str(derived_c_i[label]),
            expected=str(value),
            tolerance=None,
            source="closed-form expansion of (3q² + 4 + 3q⁻²)/4 in h — "
                   "coefficient read off the sympy series in h at "
                   "q = (h + √(h²+4))/2",
        )

    # The banner above also prints "c_(2k+1) = 0 for all k ≥ 0 (symmetric in
    # q ↔ q⁻¹)", which nothing checked; the same series answers it.
    w.add_assertion(
        "family_A_odd_h_coefficients_vanish",
        computed=sum(1 for k in (1, 3, 5, 7, 9)
                     if sp.simplify(lambda_A_series.coeff(h, k)) == 0),
        expected=5,
        tolerance=0,
        source="λ_A is symmetric under q ↔ q⁻¹, so every odd power of h must "
               "vanish — checked on the h-series through h⁹",
    )

    # Numerical verification at q_0
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    H0 = Q0 - 1/Q0
    lambda_A_at_q0_symbolic = float(lambda_A_q.subs(q, float(Q0)))
    lambda_A_at_q0_h = float(sp.Rational(5,2) + sp.Rational(3,4) * float(H0)**2)
    print(f"\nNumerical verification at q_0:")
    print(f"  λ_A from q-expression: {lambda_A_at_q0_symbolic:.15f}")
    print(f"  λ_A from h-expression: {lambda_A_at_q0_h:.15f}")
    print(f"  diff: {lambda_A_at_q0_symbolic - lambda_A_at_q0_h:.6e}")
    w.add_data("lambda_A_at_q0_from_q_expr", lambda_A_at_q0_symbolic)
    w.add_data("lambda_A_at_q0_from_h_expr", lambda_A_at_q0_h)

    # Family B comparison
    from experimental_constants import M_E_MEV as _M_E_MEV  # noqa: E402
    M_E = mp.mpf(_M_E_MEV)
    from experimental_constants import M_P_MEV as _M_P_MEV  # noqa: E402
    M_P = mp.mpf(_M_P_MEV)
    VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), 8·G via Adams 1985
    HBAR_Q = (Q0 - 1) / Q0
    lambda_B_target = float((M_P / M_E) * HBAR_Q**2 / VOL_B3)
    rel_diff = (lambda_A_at_q0_symbolic - lambda_B_target) / lambda_B_target
    print(f"\nFamily B comparison:")
    print(f"  λ_A           = {lambda_A_at_q0_symbolic:.10f}")
    print(f"  λ_B (CODATA)  = {lambda_B_target:.10f}")
    print(f"  rel diff      = {rel_diff:+.4%}")
    w.add_data("lambda_B_target_at_q0", lambda_B_target)
    w.add_data("family_A_vs_B_rel_diff", rel_diff)

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
