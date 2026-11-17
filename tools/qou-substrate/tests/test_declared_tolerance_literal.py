"""A DECLARED tolerance is serialized as a literal; a COMPUTED one is not.

The discrimination is the whole point of `_tolerance_literal`, and it is the
part that would rot silently. Widening it to "stringify every tolerance" would
still drain the ratchet — while laundering exactly the values the ratchet
exists to find — and no other check in the tree would notice. So the refusal
half is asserted here as hard as the conversion half.
"""
import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

from qou_substrate.witness import (  # noqa: E402
    Assertion,
    WitnessBuilder,
    _raw_float_paths,
    _tolerance_literal,
)


# Declared thresholds: what an author types. Each must round-trip to the
# identical double, which is what makes the rewrite value-preserving.
DECLARED = [
    (1e-9, "1e-09"),
    (0.5, "0.5"),
    (1e-40, "1e-40"),
    (0.001, "0.001"),
    (0.05, "0.05"),
    (17.22, "17.22"),
    (1.3434, "1.3434"),
    (-0.25, "-0.25"),
]

# Computed tolerances -- an error budget scaled off the expected value. These
# really did lose precision and are genuine findings; converting one would hide
# a defect behind a convention.
COMPUTED = [
    1025.6028557082007,
    130.70734000000002,
    0.0222456607,
    1.3050938107994625e-12,
    4.967999999999999,
]


@pytest.mark.parametrize("value,literal", DECLARED)
def test_declared_tolerance_becomes_its_literal(value, literal):
    assert _tolerance_literal(value) == literal
    # The invariant. Bit for bit, or the rewrite was not value-preserving.
    assert float(literal) == value


@pytest.mark.parametrize("value", COMPUTED)
def test_computed_tolerance_is_refused(value):
    assert _tolerance_literal(value) is None


@pytest.mark.parametrize("value", [0.0, 1.0, -2.0])
def test_integral_tolerance_is_left_alone(value):
    """Exact in binary64, already excused by the ratchet, so not this fix's job."""
    assert _tolerance_literal(value) is None


@pytest.mark.parametrize("value", [None, 0, "1e-9", True, False,
                                   float("nan"), float("inf")])
def test_non_float_and_non_finite_are_left_alone(value):
    assert _tolerance_literal(value) is None


def test_verdict_is_unchanged_by_the_rewrite():
    """`passed` must not move: it is derived through `float(tolerance)`."""
    for computed, expected, tol in [("1.0", "1.0", 1e-9),
                                    ("1.0", "1.000000002", 1e-9),
                                    ("1.0", "1.0000000001", 1e-9)]:
        a = Assertion("x", computed=computed, expected=expected, tolerance=tol)
        b = Assertion("x", computed=computed, expected=expected,
                      tolerance=_tolerance_literal(tol))
        assert a.passed == b.passed
        assert a.to_dict()["passed"] == a.passed


def test_saved_witness_carries_no_raw_float64_for_declared_tolerances(tmp_path):
    """End to end, under the STRICTEST guard the module offers."""
    old = os.environ.get("QOU_WITNESS_STRICT_FLOAT64")
    os.environ["QOU_WITNESS_STRICT_FLOAT64"] = "1"  # raise, don't warn
    try:
        w = WitnessBuilder("declared-tolerance-test", output_dir=str(tmp_path))
        w.add_assertion("a", computed="2.0", expected="2.0", tolerance=1e-45)
        w.add_assertion("b", computed="1", expected="1", tolerance=0.5)
        doc = json.loads(Path(w.save()).read_text(encoding="utf-8"))
        assert [a["tolerance"] for a in doc["assertions"]] == ["1e-45", "0.5"]

        # ...and the refusal still trips it, so this is not a blanket stringify.
        w2 = WitnessBuilder("computed-tolerance-test", output_dir=str(tmp_path))
        w2.add_assertion("c", computed="1", expected="1",
                         tolerance=1025.6028557082007)
        with pytest.raises(ValueError, match="raw-float64"):
            w2.save()
    finally:
        if old is None:
            os.environ.pop("QOU_WITNESS_STRICT_FLOAT64", None)
        else:
            os.environ["QOU_WITNESS_STRICT_FLOAT64"] = old


def test_raw_float_locator_honors_shadow_and_carveouts(tmp_path):
    """Bean qou-7q56: _raw_float_paths must honor the *_str shadow rule,
    LP_DUAL_F64_FIELDS, runtime duration fields, and float64-integrator tier."""
    # Shadowed scalar and list: 0 raw float paths
    assert list(_raw_float_paths({
        "y0_star": 0.012246289813934,
        "y0_star_str": "1.224628981393451974336267854072680408e-2",
        "vals": [0.5, 0.25],
        "vals_str": [
            "5.000000000000000000000000000000e-1",
            "2.500000000000000000000000000000e-1",
        ],
    })) == []

    # Laundering guard: short *_str (<= 17 sig digits) or disagreeing *_str still flagged
    assert list(_raw_float_paths({"v": 0.1, "v_str": "0.1"})) == [".v"]
    assert list(_raw_float_paths({
        "primal_obj_x": 0.0,
        "primal_obj_x_str": "4.203895392974451212771188749869748393840785825629547e-44",
    })) == [".primal_obj_x"]

    # LP-dual carve-out & ephemeral duration carve-out: excused
    assert list(_raw_float_paths({
        "y_star": [0.5, 0.25],
        "duality_gap": 1.23456789e-9,
        "elapsed_sec": 43.21,
        "duration_sec": 0.75,
    })) == []

    # float64-integrator tier: excused at witness level
    assert list(_raw_float_paths({
        "data": {"precision_tier": "float64-integrator", "rk2_val": 1.23456789},
    })) == []

    # End-to-end save with shadowed float under QOU_WITNESS_STRICT_FLOAT64=1
    old = os.environ.get("QOU_WITNESS_STRICT_FLOAT64")
    os.environ["QOU_WITNESS_STRICT_FLOAT64"] = "1"
    try:
        w = WitnessBuilder("shadowed-float-test", output_dir=str(tmp_path))
        w.add_data("rows", [{
            "mass_mev": 938.27208816,
            "mass_mev_str": "938.272088160000000000000000000000000000000000000000000000000",
        }])
        w.save()
    finally:
        if old is None:
            os.environ.pop("QOU_WITNESS_STRICT_FLOAT64", None)
        else:
            os.environ["QOU_WITNESS_STRICT_FLOAT64"] = old
