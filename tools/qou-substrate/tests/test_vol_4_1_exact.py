#!/usr/bin/env python3
"""Vol(4_1) must be COMPUTED, and must not move the substrate pin.

Until 2026-08-21 this constant was the hand-typed literal
`2.029883212819307`, which is not merely f64-truncated -- it is not even the
correctly-rounded f64 of 2*Cl_2(pi/3) (`2.0298832128193074`). A decimal
literal cannot be checked by reading it, and the module already had
`vol_4_1_at()` computing the same quantity, so one of the two was free to be
wrong. It was the one every f64 path used.
"""
import mpmath as mp
import pytest

from qou_substrate import constants as C


def _exact():
    with mp.workdps(60):
        return 2 * mp.clsin(2, mp.pi / 3)


def test_the_f64_is_correctly_rounded_not_truncated():
    assert C.VOL_FIGURE_EIGHT == float(_exact())
    # The old literal is specifically excluded: it differs in the last bits.
    assert C.VOL_FIGURE_EIGHT != 2.029883212819307


def test_the_50_digit_string_agrees_with_the_computation():
    with mp.workdps(60):
        s = mp.mpf(C.VOL_FIGURE_EIGHT_50_STR)
        assert abs(s - _exact()) / _exact() < mp.mpf("1e-49")


def test_it_agrees_with_the_modules_own_high_precision_function():
    """Two spellings of one constant must not be free to disagree."""
    with mp.workdps(60):
        assert abs(C.vol_4_1_at(50) - _exact()) / _exact() < mp.mpf("1e-49")
        assert float(C.vol_4_1_at(50)) == C.VOL_FIGURE_EIGHT


def test_the_substrate_pin_does_not_move():
    """The correction must NOT shift q_0.

    Measured before making the change: the f64 Newton solve returns identical
    bits either way, because 1.23e-16 is below what it resolves. If this ever
    fails, the correction has become a re-pin and needs owner sign-off.
    """
    assert C.Q == 1.1099785827513808
    assert C._solve_q_proton_f64(C.MASS_RATIO_P_E, 2.029883212819307) == C.Q


@pytest.mark.parametrize("dps", [15, 30, 50])
def test_vol_4_1_at_is_stable_across_precisions(dps):
    with mp.workdps(60):
        assert abs(C.vol_4_1_at(dps) - _exact()) / _exact() < mp.mpf(f"1e-{dps - 2}")
