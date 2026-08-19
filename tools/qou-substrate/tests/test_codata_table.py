"""The CODATA table reader, and the guard against the vendored copy drifting.

`qou_substrate/data/allascii.txt` is a copy of the repo-root
`library/allascii.txt` (NIST's *Complete Listing*, 2022 CODATA adjustment, as
downloaded). A copy that nothing compares is a copy that drifts — the failure
mode AGENTS.md records for `qou-mass/_internal/`, where all 14 vendored
modules had diverged and the drift masked a live defect. So the byte-identity
is asserted here, not assumed.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import mpmath as mp
import pytest

from qou_substrate import constants
from qou_substrate.codata import codata, table

_REPO = Path(__file__).resolve().parents[3]
_UPLOADED = _REPO / "uploads" / "allascii.txt"
_VENDORED = Path(constants.__file__).resolve().parent / "data" / "allascii.txt"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_vendored_table_matches_upload():
    """The package copy must be byte-identical to the committed upload."""
    if not _UPLOADED.exists():
        pytest.skip(f"{_UPLOADED} absent (package checked out standalone)")
    assert _sha(_VENDORED) == _sha(_UPLOADED), (
        "qou_substrate/data/allascii.txt has drifted from library/allascii.txt "
        "The upload is the artifact of record; re-copy it rather than editing "
        "either in place."
    )


def test_table_parses():
    entries = table()
    # The 2022 listing carries a few hundred rows; a parser that silently
    # matched almost nothing would still 'work' without this floor.
    assert len(entries) > 250, f"only {len(entries)} entries parsed"


def test_it_is_the_2022_adjustment():
    """Guard the edition itself — the whole point of the module."""
    header = _VENDORED.read_text(encoding="utf-8", errors="replace")[:400]
    assert "2022 CODATA adjustment" in header


@pytest.mark.parametrize(
    ("quantity", "value", "uncertainty"),
    [
        ("muon-electron mass ratio", "206.7682827", "0.0000046"),
        ("proton-electron mass ratio", "1836.152673426", "0.000000032"),
        ("electron mass energy equivalent in MeV", "0.51099895069", "0.00000000016"),
        ("proton mass energy equivalent in MeV", "938.27208943", "0.00000029"),
        ("neutron mass energy equivalent in MeV", "939.56542194", "0.00000048"),
    ],
)
def test_known_rows(quantity, value, uncertainty):
    """Digit strings are returned exactly as NIST prints them."""
    entry = codata(quantity)
    assert entry.value_str == value
    assert entry.uncertainty_str == uncertainty
    assert entry.value == mp.mpf(value)


def test_digit_grouping_is_stripped():
    """NIST groups digits in threes; that is presentation, not precision."""
    assert " " not in codata("proton-electron mass ratio").value_str


def test_unknown_quantity_raises_rather_than_defaulting():
    """A silently-wrong constant is the failure mode this module removes."""
    with pytest.raises(KeyError):
        codata("muon-electron mass ration")  # typo


def test_constants_are_read_from_the_table_not_transcribed():
    """The two substrate mass ratios must equal the table, digit for digit.

    Regression guard for the edition straddle removed on 2026-08-15:
    MASS_RATIO_MU_E_STR was the CODATA-2018 value 206.7682830 under a
    'CODATA 2022' comment, and MASS_RATIO_P_E_ERR was the CODATA-2018
    uncertainty 1.1e-7 against a value that prints the same in both editions
    (so a value-only check passed).
    """
    mu_e = codata("muon-electron mass ratio")
    p_e = codata("proton-electron mass ratio")

    assert constants.MASS_RATIO_MU_E_STR == mu_e.value_str
    assert constants.MASS_RATIO_P_E_STR == p_e.value_str
    assert constants.MASS_RATIO_MU_E == float(mu_e.value)
    assert constants.MASS_RATIO_P_E == float(p_e.value)
    assert constants.MASS_RATIO_MU_E_ERR == float(mu_e.uncertainty)
    assert constants.MASS_RATIO_P_E_ERR == float(p_e.uncertainty)


def test_production_q_is_unchanged_by_the_correction():
    """The proton pin must not move — witnesses depend on it.

    m_p/m_e prints identically in CODATA-2018 and -2022, so repointing the
    registry at the table changed the muon cross-check and the error bars but
    NOT q0 itself. If this value ever moves, ~840 committed witnesses need
    regeneration and that must be a deliberate, announced act.
    """
    assert repr(constants.Q) == "1.1099785827513808"
