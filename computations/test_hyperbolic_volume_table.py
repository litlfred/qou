#!/usr/bin/env python3
"""The hyperbolic-volume table in `lambda_scale_rd4_k_p_search.py` is correct.

## Why this test exists

Every hand-typed volume in that table was wrong. Six of seven decimal
literals disagreed with the SnapPy census, one by a factor of two, and one
carried the wrong knot's name:

    entry   was                    true                     rel err
    4_1     4.0597664256386145     2.0298832128193073       1.0     (2x)
    5_2     2.82812208833          2.8281220883307832       2.8e-13 (ok)
    6_1     3.16396322648          3.1639632288831440       7.6e-10
    6_2     4.40083251217          4.4008325161230461       9.0e-10
    6_3     5.69302109614          5.6930210912813008       8.5e-10
    7_4     5.13794120982          5.1379412018734178       1.5e-9
    8_1     3.42720252426          3.4272052462740162       7.9e-7

The two entries that were RIGHT (`V_OCT`, `VOL_B3`) are the two that were
computed from a closed form rather than transcribed. A decimal literal
cannot be checked by reading it; that is what this test is for.

The `4_1` case was not a precision defect at all. `V_TET` was defined as
`2*Cl_2(pi/3)` while its own comment said "≈ 1.0149" (which is
`Cl_2(pi/3)`), and the next line then took `VOL_4_1 = 2 * V_TET` -- so the
factor of two was applied twice. The prose conclusion in the same file
quotes `9*Vol(4_1) = 18.27`, i.e. the CORRECT value, so the narrative and
the code had disagreed for as long as both existed.

## Two tiers

Closed-form entries are checked unconditionally -- no external data needed,
so these can never silently stop running. Census entries need SnapPy, and
skip without it, which is why the closed-form tier carries the load: it
independently pins `4_1`, the one entry that was catastrophically wrong.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp
import pytest

HERE = Path(__file__).resolve().parent


def _load_table():
    """Import the search module for its constants without running main()."""
    sys.path.insert(0, str(HERE))
    spec = importlib.util.spec_from_file_location(
        "lambda_scale_rd4_k_p_search", HERE / "lambda_scale_rd4_k_p_search.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Tier 1 -- closed forms. No SnapPy, no census, no transcription.
# ---------------------------------------------------------------------------

def test_v_tet_is_one_ideal_tetrahedron():
    """`V_TET` must be ONE tetrahedron, not two.

    This is the assertion the old code failed: it held `2*Cl_2(pi/3)`, which
    is the figure-eight volume, under a name and a comment that both said
    tetrahedron.
    """
    m = _load_table()
    with mp.workdps(50):
        assert abs(m.V_TET - mp.clsin(2, mp.pi / 3)) < mp.mpf("1e-45")
        # And it is NOT the figure-eight, which is what it used to be.
        assert abs(m.V_TET - 2 * mp.clsin(2, mp.pi / 3)) > mp.mpf("1")


def test_figure_eight_is_two_tetrahedra():
    """Vol(4_1) = 2*Cl_2(pi/3) ≈ 2.0299 -- the AGENTS.md Λ-vs-Cl_2 guard.

    `2Λ(π/3) ≈ 0.6766` and `3·Cl_2(π/3) ≈ 3.0448` are both wrong, and so is
    the doubled `4.0598` this file used to carry.
    """
    m = _load_table()
    with mp.workdps(50):
        assert abs(m.VOL_4_1 - 2 * mp.clsin(2, mp.pi / 3)) < mp.mpf("1e-45")
        assert abs(m.VOL_4_1 - mp.mpf("2.0298832128193072500424051085")) < mp.mpf("1e-25")


def test_octahedron_whitehead_and_borromean_are_consistent():
    """Whitehead is ONE ideal octahedron; Borromean is TWO.

    The old table listed `Vol(L_Whitehead) = 3.4272...` while separately
    listing `V_octahedron = 3.6639...` -- i.e. it carried the Whitehead
    volume twice, once under the right number and once under the right name,
    and they were different rows.
    """
    m = _load_table()
    with mp.workdps(50):
        assert abs(m.V_OCT - 4 * mp.catalan) < mp.mpf("1e-45")
        assert m.VOL_WHITEHEAD == m.V_OCT
        assert abs(m.VOL_B3 - 2 * m.V_OCT) < mp.mpf("1e-45")
        # 8_1 is a different manifold from the Whitehead link.
        assert abs(m.VOL_8_1 - m.VOL_WHITEHEAD) > mp.mpf("0.2")


# ---------------------------------------------------------------------------
# Tier 2 -- census values, verified against SnapPy when it is installed.
# ---------------------------------------------------------------------------

CENSUS = {
    "4_1": "VOL_4_1",
    "5_2": "VOL_5_2",
    "6_1": "VOL_6_1",
    "6_2": "VOL_6_2",
    "6_3": "VOL_6_3",
    "7_4": "VOL_7_4",
    "8_1": "VOL_8_1",
}


@pytest.mark.parametrize("knot,const", sorted(CENSUS.items()))
def test_matches_snappy_census(knot, const):
    snappy = pytest.importorskip("snappy", reason="SnapPy not installed")
    m = _load_table()
    with mp.workdps(50):
        true = mp.mpf(str(snappy.Manifold(knot).high_precision().volume()))
        got = getattr(m, const)
        rel = abs(got - true) / true
        assert rel < mp.mpf("1e-25"), (
            f"{const} = {mp.nstr(got, 30)} but Vol({knot}) = {mp.nstr(true, 30)} "
            f"(rel {mp.nstr(rel, 4)})"
        )


def test_snappy_and_the_closed_form_agree_on_the_figure_eight():
    """Cross-check the two independent sources against each other.

    If SnapPy's census and `2*Cl_2(pi/3)` ever disagreed, one of the two
    tiers above would be measuring the wrong thing, and neither tier alone
    could tell you which.
    """
    snappy = pytest.importorskip("snappy", reason="SnapPy not installed")
    with mp.workdps(50):
        census = mp.mpf(str(snappy.Manifold("4_1").high_precision().volume()))
        closed = 2 * mp.clsin(2, mp.pi / 3)
        assert abs(census - closed) / closed < mp.mpf("1e-25")
