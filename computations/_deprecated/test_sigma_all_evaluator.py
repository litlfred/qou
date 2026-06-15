"""
Tests for the Σ_all closed-form evaluator.

Verifies:
  1. The evaluator matches the symbolic-table reference values for
     A=1..6 at q_0 to f64 floor (~1e-14 relative).
  2. The two-step ratio identity Σ_all(A+2) / Σ_all(A) = 3(q⁴-1)²/(8q⁴)
     holds exactly (no floating-point error) at the working precision.
  3. The decay rate γ(q_0) matches the audit-doc prediction (≈ 1.357).
  4. The Frobenius-filter-required threshold reproduces the precision
     schedule from the audit doc (A ≤ 27 safe at f64; A=84 needs 50 dps).
"""
from __future__ import annotations

import math
import pathlib
import sys

import mpmath as mp
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from sigma_all_evaluator import (  # noqa: E402
    a_exponent,
    d_exponent,
    frob_filter_required,
    sigma_all_closed,
    sigma_all_decay_rate,
    sigma_all_ratio,
)
from q_parameter import q_at  # noqa: E402


# Reference values from `sigma_all_symbolic_decay.py` symbolic compute,
# evaluated at q_0 (audit doc table, lines 690-697).
SYMBOLIC_TABLE_AT_Q0 = {
    1:  0.5295037320168715,
    2: -0.3357233125749398,
    3:  0.035093211913212914,
    4: -0.022250285767622852,
    5:  0.002325825953473032,
    6: -0.001474652483748414,
}


@pytest.fixture(scope="module")
def q0():
    """Substrate parameter q_0 at 50 decimal digits of precision."""
    return q_at(50)


def test_a_exponent_table():
    """a(A) for A=1..6 must be {2, 4, 5, 7, 8, 10}."""
    expected = [2, 4, 5, 7, 8, 10]
    for A, want in zip(range(1, 7), expected):
        assert a_exponent(A) == want, f"a({A}) = {a_exponent(A)}, want {want}"


def test_d_exponent_table():
    """d(A) for A=1..6 must be {3, 6, 7, 10, 11, 14}."""
    expected = [3, 6, 7, 10, 11, 14]
    for A, want in zip(range(1, 7), expected):
        assert d_exponent(A) == want, f"d({A}) = {d_exponent(A)}, want {want}"


def test_matches_symbolic_table_A_1_to_6(q0):
    """sigma_all_closed must match the symbolic table at q_0 to ~f64 floor.

    Tolerance 1e-14 relative — symbolic-table values are f64 truncations
    of higher-precision computations, so floor agreement is bounded by
    f64 rounding noise (≈ 13 × 2^-52 ≈ 3e-15) when the mpmath result
    is cast back to float for comparison.
    """
    for A, expected in SYMBOLIC_TABLE_AT_Q0.items():
        got = float(sigma_all_closed(A, q0))
        rel = abs(got - expected) / abs(expected)
        assert rel < 1e-14, f"A={A}: got {got}, expected {expected}, rel={rel:.2e}"


def test_two_step_ratio_invariant(q0):
    """Σ_all(A+2) / Σ_all(A) = 3 (q⁴-1)² / (8 q⁴) exactly.

    Verified at A ∈ {1, 2, 3, 4} at q_0 to 1e-15 relative precision.
    Because the closed form contains the same (q-1)^A · (q+1)^A factors
    on both sides of the ratio, the algebraic cancellation is exact in
    finite precision; we expect rel err = 0 at any working precision.
    """
    expected = 3 * (q0 ** 4 - 1) ** 2 / (8 * q0 ** 4)
    for A in (1, 2, 3, 4):
        got = sigma_all_closed(A + 2, q0) / sigma_all_closed(A, q0)
        rel = abs(got - expected) / abs(expected)
        assert float(rel) < 1e-15, (
            f"A={A}→{A+2}: ratio {mp.nstr(got, 15)} != "
            f"{mp.nstr(expected, 15)} (rel {float(rel):.2e})"
        )


def test_two_step_ratio_via_sigma_all_ratio(q0):
    """sigma_all_ratio uses the exact identity for even ΔA."""
    expected = 3 * (q0 ** 4 - 1) ** 2 / (8 * q0 ** 4)
    got = sigma_all_ratio(1, 3, q0)
    rel = abs(got - expected) / abs(expected)
    assert float(rel) < 1e-15

    # Two steps of two = ratio squared
    got2 = sigma_all_ratio(1, 5, q0)
    expected2 = expected ** 2
    rel2 = abs(got2 - expected2) / abs(expected2)
    assert float(rel2) < 1e-15


def test_sigma_all_ratio_odd_delta(q0):
    """Odd Δ falls back to ratio of two evaluations and must match
    the direct quotient sigma_all_closed(A2) / sigma_all_closed(A1)."""
    direct = sigma_all_closed(4, q0) / sigma_all_closed(3, q0)
    via_ratio = sigma_all_ratio(3, 4, q0)
    rel = abs(direct - via_ratio) / abs(direct)
    assert float(rel) < 1e-15


def test_decay_rate_at_q0(q0):
    """γ(q_0) = ½ log(8 q_0⁴ / (3 (q_0⁴-1)²)) ≈ 1.357 (audit line 734)."""
    gamma = sigma_all_decay_rate(q0)
    # Audit predicts ~1.357; allow 0.001 absolute tolerance to be robust
    # against the audit's own truncation.
    assert abs(float(gamma) - 1.357) < 0.001, f"γ(q_0) = {float(gamma)}"


def test_frob_filter_threshold_f64(q0):
    """Per audit precision schedule: at f64 (1e-16 target), A ≤ 27 safe.

    A=10 must be safe; A=84 must require the closed form.
    """
    assert frob_filter_required(84, q0, 1e-15) is True
    assert frob_filter_required(10, q0, 1e-15) is False


def test_frob_filter_threshold_50dps(q0):
    """Per audit: at 50 dps (1e-50 target), A ≤ 84 safe; A ≥ 85 needs
    closed form."""
    # A=240 (heaviest stable nuclei) is far past the 50-dps safe
    # boundary — closed form is required.
    assert frob_filter_required(240, q0, 1e-50) is True
    # A=10 is far inside the safe zone for 50 dps.
    assert frob_filter_required(10, q0, 1e-50) is False


def test_frob_filter_audit_max_A_boundary(q0):
    """The audit table says A ≤ 27 / 42 / 84 / 169 / 338 are SAFE at
    their respective working precisions.  Lock in that
    `frob_filter_required` returns False *at* the boundary and True one
    step past it.

    See docs/audits/2026-05-02-nv-frob-filter-conjectures.md lines
    746–761 — Gemini PR #525 review caught a +1 floor that made these
    boundary values flip incorrectly.
    """
    # (max_A_safe, first_A_past_floor, target) — first_A_past_floor is
    # the smallest A for which ceil(A · 0.589) strictly exceeds
    # log10(1/target), i.e. where the closed form becomes mandatory.
    # For most rows this is max_A_safe + 1, but at 200 dps a second
    # ceiling step lands at A=340 because A=339 still rounds to 200.
    boundaries = [
        (27, 28, 1e-16),
        (42, 43, 1e-25),
        (84, 85, 1e-50),
        (169, 170, 1e-100),
        (338, 340, 1e-200),
    ]
    for A_max_safe, A_past_floor, target in boundaries:
        assert frob_filter_required(A_max_safe, q0, target) is False, (
            f"A={A_max_safe} at target={target:g} should be SAFE per audit table"
        )
        assert frob_filter_required(A_past_floor, q0, target) is True, (
            f"A={A_past_floor} at target={target:g} should require closed form"
        )


def test_sign_pattern(q0):
    """Σ_all(A) sign alternates: +, -, +, -, +, -, ..."""
    for A in range(1, 9):
        val = sigma_all_closed(A, q0)
        expected_positive = (A % 2 == 1)
        if expected_positive:
            assert val > 0, f"Σ_all({A}) should be > 0, got {float(val)}"
        else:
            assert val < 0, f"Σ_all({A}) should be < 0, got {float(val)}"


def test_high_precision_evaluation(q0):
    """The evaluator can compute Σ_all at A=240 (full β-decay table)
    in constant time at 200 dps — no cancellation, no precision loss."""
    q_hi = q_at(200)
    with mp.workdps(200):
        val = sigma_all_closed(240, q_hi, dps=200)
        # Must be a finite, non-zero result. Magnitude ~ 0.2575^240 ≈ 1e-141.
        assert mp.isfinite(val)
        assert val != 0
        log10_abs = float(mp.log10(abs(val)))
        # Audit asymptotic: log10 |Σ_all| / A → -0.589, so at A=240
        # we expect log10 |Σ_all(240)| ≈ -141.
        assert -150 < log10_abs < -130, f"log10|Σ_all(240)| = {log10_abs}"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
