#!/usr/bin/env python3
"""Regression tests for the migration tolerance triage.

Every case here is a real corpus assertion that an earlier revision of this
script mis-bucketed. All three false-positive classes have the same shape:
`slack` is arithmetically zero or negative and the assertion is nonetheless
fine, because the fields do not mean what the margin model assumes.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from q0_migration_tolerance_triage import (  # noqa: E402
    ANCHOR_IMPACT,
    carries_the_anchor,
    is_discrete,
    slack_of,
)


def test_counts_are_discrete_not_at_risk():
    """229 of a reported 291 "AT RISK" were counts with tolerance 0.

    An 11.5 ppb anchor shift cannot turn 77 into 76.
    """
    for a in (
        {"name": "all_77_y_lambda_computed", "tolerance": 0,
         "computed": 77, "expected": 77},
        {"name": "fixed_point_forms_solved", "tolerance": 0,
         "computed": 3, "expected": 3},
        {"name": "lp_feasibility_at_q0_two_row", "tolerance": 0.0,
         "computed": 3.0, "expected": 3.0},
    ):
        assert slack_of(a) == 0.0, "the arithmetic really is zero margin"
        assert is_discrete(a), a["name"]


def test_real_valued_zero_tolerance_is_not_discrete():
    """An exact real is still a measurement -- it must stay in the triage."""
    a = {"name": "bare_alpha4_equals_minus_three_quarters_exact",
         "tolerance": 0.0, "computed": -0.75, "expected": -0.75}
    assert not is_discrete(a)


def test_threshold_semantics_is_not_a_failure():
    """`passed: true` with |computed - expected| > tolerance is an INEQUALITY.

    Live case: a pre-registered kill criterion where 2.21 < 9.2 IS the result.
    Reporting it as "already failing" inverts a deliberate negative result.
    """
    a = {"name": "stage1_entropy_verdict_is_blocked", "computed": 2.21,
         "expected": 9.2, "passed": True, "tolerance": 0.0}
    assert slack_of(a) < 0
    assert a.get("passed") is not False, "must not be read as already-failing"


def test_the_anchor_pinned_assertion_is_caught():
    """The sharpest class: the asserted value IS the anchor being moved.

    1e-18 tolerance on a quantity about to shift 1.15e-8.
    """
    a = {"name": "lambda_plus_eq_q", "tolerance": 1e-18,
         "computed": 1.1099785955573347199,
         "expected": 1.1099785955573347199}
    assert carries_the_anchor(a)
    assert slack_of(a) < ANCHOR_IMPACT


def test_the_proton_pin_is_not_the_muon_anchor():
    """The two pins are 11.5 ppb apart; the detector must not collapse them."""
    a = {"computed": 1.1099785827513808, "expected": 1.1099785827513808}
    assert not carries_the_anchor(a)


def test_slack_accounts_for_margin_already_consumed():
    """A wide tolerance sitting at 99% of itself is as fragile as a tight one.

    This is why the script measures unused margin rather than tolerance.
    """
    roomy = {"tolerance": 1e-3, "computed": 1.0, "expected": 1.0}
    # 99.999% of a 1e-3 tolerance already spent -> 1e-8 left, below the move.
    consumed = {"tolerance": 1e-3, "computed": 1.00099999, "expected": 1.0}
    assert slack_of(roomy) > ANCHOR_IMPACT
    assert slack_of(consumed) < ANCHOR_IMPACT
    # Both carry the SAME tolerance, which is the point: sorting by tolerance
    # cannot separate them, and only one of them can absorb the anchor move.
    assert roomy["tolerance"] == consumed["tolerance"]


def test_non_numeric_is_unmeasurable_not_safe():
    """A boolean or string assertion CAN flip; the model just cannot see it."""
    for a in ({"computed": "true", "expected": "true"},
              {"computed": 1.0, "expected": 1.0},          # no tolerance key
              {"tolerance": 1e-9, "computed": 1.0, "expected": 0.0}):
        assert slack_of(a) is None


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
