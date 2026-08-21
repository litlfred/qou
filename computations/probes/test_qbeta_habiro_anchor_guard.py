#!/usr/bin/env python3
"""The anchor-straddle guard must fire on a layer swap, and only on one.

The probe announced "CANONICAL q0 (live, proton-pinned)" while computing at the
MUON value 11.54 ppb away, because `calibration_inputs.anchor` says `m_p/m_e`
(the derivation ROUTE) while `derived_50_digit.q` holds the muon literal (the
ideal_muon override means the Newton solve never runs). Bean `qou-m9xp`.

The first version of the guard could not fire: its threshold was 1.2e-8, ABOVE
the 1.15e-8 separation it exists to detect, so a synthetic straddle passed with
room to spare. A threshold set at the size of the thing being detected detects
nothing. These tests pin both directions.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
for p in (HERE, HERE.parent, HERE.parent / "substrate",
          HERE.parents[1] / "tools" / "qou-substrate" / "python"):
    sys.path.insert(0, str(p))

import pytest  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

# The comparisons below construct mpf values from 50-digit decimal strings; at
# mpmath's default 15 dps they would be truncated before the guard ever saw
# them, and a test that cannot represent the difference it asserts on is not a
# test. Idempotent, module scope, per the never-raises-dps ratchet.
set_compute_dps()

from qbeta_habiro_residual_probe import (  # noqa: E402
    _STRADDLE_TOL,
    _assert_anchor_matches_value,
    _assert_uses_proton_pin,
)

PIN = HERE.parents[1] / "computations" / "q-pinning-50-digit.witness.json"
PROTON_50 = "1.1099785827513808075916690956107688798744991218736"


def _pin():
    return json.loads(PIN.read_text())


def test_threshold_is_below_the_separation_it_detects():
    """1.15e-8 is the mu-p gap. The tolerance must be strictly under it."""
    assert _STRADDLE_TOL < 1.15e-8, (
        "threshold at or above the separation cannot fire on a layer swap"
    )
    # ...and not so tight that re-serialising a 50-dps decimal trips it.
    assert _STRADDLE_TOL > 1e-40


def test_the_committed_pin_is_not_a_straddle():
    """The restored file must pass -- otherwise the guard blocks correct work."""
    _assert_anchor_matches_value(_pin())


def test_proton_value_under_a_muon_label_fires():
    """The exact shape that 9a9c6b31c produced on main."""
    d = _pin()
    assert d["q0Anchor"] == "muon", "fixture assumes the restored muon pin"
    d["derived_50_digit"]["q"] = PROTON_50
    with pytest.raises(SystemExit, match="ANCHOR STRADDLE"):
        _assert_anchor_matches_value(d)


def test_truncated_five_digit_literal_fires():
    """1.10998 is 1277 ppb off -- the truncated-muon class (qou-8q0u)."""
    d = _pin()
    d["derived_50_digit"]["q"] = "1.10998"
    with pytest.raises(SystemExit, match="ANCHOR STRADDLE"):
        _assert_anchor_matches_value(d)


def test_the_message_formats(capsys):
    """A guard that raises TypeError instead of its diagnosis is half-broken.

    `rel` is an mpf and `f"{rel:.3e}"` throws; the first version did exactly
    that, so the straddle surfaced as a formatting crash rather than a reason.
    """
    d = _pin()
    d["derived_50_digit"]["q"] = PROTON_50
    with pytest.raises(SystemExit) as e:
        _assert_anchor_matches_value(d)
    assert "1.154e-08" in str(e.value)
    assert "qou-m9xp" in str(e.value)


def test_no_claimed_layer_is_not_an_error():
    """A witness that claims nothing cannot contradict itself."""
    d = _pin()
    d.pop("q0Anchor", None)
    _assert_anchor_matches_value(d)


def test_the_probe_is_declared_proton_and_uses_it():
    """Owner ruling 2026-08-21: this probe is PROTON.

    The guard that matters after the ruling is not "is the pin witness
    self-consistent" but "is the number THIS probe computes with the layer it
    claims". The witness guard is kept (still exercised above) because the
    witness's own consistency is a separate fact worth holding.
    """
    import mpmath as mp
    from qou_substrate.constants import Q_50_DIGIT_STR

    _assert_uses_proton_pin(mp.mpf(Q_50_DIGIT_STR))


def test_the_muon_pin_is_rejected_now():
    """The exact value this probe used to compute at, before the ruling."""
    import mpmath as mp
    import pytest as _pt

    muon = mp.mpf("1.1099785955573347198997632204832250266562084087801536866079")
    with _pt.raises(SystemExit, match="ANCHOR STRADDLE"):
        _assert_uses_proton_pin(muon)


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
