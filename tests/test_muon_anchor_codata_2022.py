"""The muon anchor must be DERIVED, and must keep matching what it declares.

`computations/substrate/q_parameter.py` names this file.  It used to carry an
import-time guard asserting the anchor witness's prefix; the guard was removed
because the anchor is now derived from `q_muon_at()` rather than read back out
of the witness, and an import-time raise would deadlock regeneration — the
producer needs that module in order to run.

The guard had to go somewhere, and until this file existed it had gone nowhere:
the comment in `q_parameter.py` said the artifact "is checked against this
derivation by tests/test_muon_anchor_codata_2022.py", and no such file was in
the tree.  A claim of verification with nothing behind it is worse than no
claim, so these are the checks it was promising.

Why the anchor was wrong before the 2026-08-22 owner ruling ("A --> CODATA
2022"): the witness is written by `q_pinning_50_digit.py`, which is itself
listed `ideal_muon`, so `q_parameter` rebound `q_at` for that very producer and
it wrote back the value it had just read.  The anchor certified itself.  The
stored value inverted to m_mu/m_e = 206.768282989315, matching no published
CODATA and disagreeing by 1.4 ppb with the ratio the same witness DECLARES.

Test 1 is the one that would have caught that, and it is deliberately
independent of `q_muon_at`: it inverts the stored q back to a mass ratio and
compares against the witness's own `calibration_inputs`.  A witness that
disagrees with its own declared input is self-inconsistent no matter which
closed form produced it.
"""

from __future__ import annotations

import json
import pathlib

import pytest

mpmath = pytest.importorskip("mpmath")
from mpmath import mp, mpf  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PIN = ROOT / "computations" / "q-pinning-50-digit.witness.json"


def _witness() -> dict:
    if not PIN.exists():                                    # pragma: no cover
        pytest.skip(f"anchor witness not present: {PIN}")
    return json.loads(PIN.read_text(encoding="utf-8"))


def _stored_q() -> mpf:
    return mpf(_witness()["derived_50_digit"]["q"])


def _declared_ratio() -> str:
    """The m_mu/m_e the witness itself declares as its input."""
    ci = _witness().get("calibration_inputs") or {}
    for k, v in ci.items():
        if "mu" in k.lower() and ("e" in k.lower() or "ratio" in k.lower()):
            return str(v.get("value", v) if isinstance(v, dict) else v)
    pytest.skip("witness declares no m_mu/m_e in calibration_inputs")


def test_stored_q_implies_the_ratio_the_witness_declares():
    """The anchor must not contradict its own stated input.

    Invert q -> hbar_q = 1 - 1/q -> m_mu/m_e = Vol(4_1)/hbar_q^2, and compare
    with the ratio the witness declares.  This is the self-consistency check
    the self-certifying loop defeated; it uses no closed form from the code
    under test, so it stays honest if that code changes.
    """
    with mp.workdps(80):
        q = _stored_q()
        hbar = mpf(1) - mpf(1) / q
        vol = 2 * mp.clsin(2, mp.pi / 3)          # Vol(4_1) = 2*Cl_2(pi/3)
        implied = vol / hbar ** 2
        declared = mpf(_declared_ratio())
        ppb = abs(implied - declared) / declared * mpf(10) ** 9
    # The declared ratio is quoted to ~10 significant figures, so agreement is
    # limited by that quotation, not by the arithmetic. 1 ppb is far tighter
    # than the 1.4 ppb contradiction this exists to catch, and far looser than
    # the quotation floor.
    assert ppb < 1, (
        f"anchor contradicts its own declared m_mu/m_e by {mp.nstr(ppb, 5)} ppb: "
        f"stored q implies {mp.nstr(implied, 16)}, witness declares {declared}"
    )


def test_stored_q_reproduces_the_live_muon_derivation():
    """The committed artifact must equal what q_muon_at() derives.

    This is the removed import-time guard, relocated.  It is the check that
    the anchor is DERIVED rather than frozen: it fails the moment someone
    hand-edits the witness, and it follows the next CODATA revision without
    anyone editing a digit here.
    """
    constants = pytest.importorskip("qou_substrate.constants")
    if not hasattr(constants, "q_muon_at"):                 # pragma: no cover
        pytest.skip("qou_substrate.constants has no q_muon_at")
    with mp.workdps(90):
        derived = constants.q_muon_at(70)
        stored = _stored_q()
        rel = abs(stored - derived) / derived
    assert rel < mpf(10) ** -40, (
        f"committed anchor differs from the live derivation by {mp.nstr(rel, 5)} "
        f"relative.\n  stored  {mp.nstr(stored, 30)}\n  derived {mp.nstr(derived, 30)}\n"
        "Fix by re-running computations/q_pinning_50_digit.py — never by editing "
        "the witness."
    )


def test_anchor_is_not_the_superseded_codata_2018_value():
    """B is a THIRD population, not the same defect as A.

    B = 1.109978595554180... is the CODATA-2018 muon value.  It agrees with A
    to 11 digits, so a short-prefix grep sums the two silently; this pins the
    anchor away from it explicitly rather than relying on a prefix scan.
    """
    q = str(_stored_q())
    assert not q.startswith("1.109978595554"), (
        "anchor carries the superseded CODATA-2018 muon value (B). "
        "The ruling of 2026-08-22 is CODATA 2022."
    )
