"""`matches_live_q0` compares at the coarser of the two stated precisions.

The 2026-11-24 compute refresh (PR #9395) found 34 witnesses that record q0 to
60-70 digits flagged stale by `run_pipeline` against the ~50-significant-digit
`Q_50_DIGIT_STR`: at the recorded value's own 1e-70 ulp, the live string's own
rounding read as drift. These tests pin the fix and the two properties it must
not lose: a genuine pin flip is still stale, and a short serialization of the
live pin is still fresh.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "computations" / "substrate", ROOT / "computations",
          ROOT / "tools" / "qou-substrate" / "python"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from witness_constant_staleness import matches_live_q0  # noqa: E402


def _live_at(digits: int) -> str:
    """The live pin, re-derived at `digits` significant digits from its own
    string (what a full-precision producer serialises)."""
    with mp.workdps(digits + 10):
        return mp.nstr(mp.mpf(Q_50_DIGIT_STR), digits, strip_zeros=False)


def test_full_precision_record_of_live_pin_is_fresh():
    # 70 digits: agrees with the live string to every digit it carries.
    rec = _live_at(70)
    assert len(rec) > len(Q_50_DIGIT_STR)
    assert matches_live_q0(rec)


def test_full_precision_record_differing_past_live_precision_is_fresh():
    # Digits past the live string's last place are unknowable from it.
    rec = Q_50_DIGIT_STR + "4" * 20
    assert matches_live_q0(rec)


def test_short_record_of_live_pin_is_fresh():
    assert matches_live_q0(Q_50_DIGIT_STR[:13])


def test_muon_pin_is_still_stale_at_full_precision():
    # The CODATA-2022 muon anchor, ~11.6 ppb from the proton pin.
    muon = "1.109978595642739046681795129380001752700065561029011556974045769999095"
    assert not matches_live_q0(muon)


def test_one_live_ulp_off_at_full_precision_is_stale():
    # Two units in the live string's last place is drift, whatever the width.
    with mp.workdps(90):
        live = mp.mpf(Q_50_DIGIT_STR)
        frac = Q_50_DIGIT_STR.split(".", 1)[1]
        bumped = live + 2 * mp.mpf(10) ** (-len(frac))
        rec = mp.nstr(bumped, 70, strip_zeros=False)
    assert not matches_live_q0(rec)
