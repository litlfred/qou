"""Tests for pyhecke.sdp — Track C multi-level SDP dispatcher."""

from __future__ import annotations

import pytest

from pyhecke import sdp


def test_dispatch_valid_levels():
    for lvl in (3, 4, 5, 6, 7):
        result = sdp.multi_level_sdp(lvl)
        assert isinstance(result, sdp.SDPResult)
        assert result.level == lvl


def test_dispatch_rejects_invalid_level():
    for lvl in (0, 1, 2, 8, -1):
        with pytest.raises(ValueError):
            sdp.multi_level_sdp(lvl)


def test_implemented_levels():
    """Levels 3 and 4 are implemented; 5-7 remain."""
    assert sdp.implemented_levels() == [3, 4]
    assert sdp.pending_levels() == [5, 6, 7]


@pytest.mark.parametrize("level", [5, 6, 7])
def test_pending_levels_report_not_implemented(level):
    result = sdp.multi_level_sdp(level)
    assert result.status == "not_implemented"
    assert any("Track C" in c or "audit" in c.lower() for c in result.caveats)


# ── Level 4 — shell-magic SDP ──────────────────────────────────────────

def test_level4_rejects_non_magic_count():
    """A_magic = 3 is not a magic number — solver must reject."""
    result = sdp.solve_shell_magic_sdp(a_magic=3)
    assert result.level == 4
    assert result.status == "infeasible"
    assert any("magic" in c for c in result.caveats)


@pytest.mark.parametrize("a_magic", list(sdp.MAGIC_NUMBERS))
def test_level4_accepts_each_magic_number(a_magic):
    """Every canonical magic number must pass the 2x2 PSD test."""
    try:
        result = sdp.solve_shell_magic_sdp(a_magic=a_magic)
    except ImportError:
        pytest.skip("sigma_shell_characterization not importable")
    assert result.level == 4
    # Allow "not_implemented" (upstream import failure) or "optimal".
    if result.status == "not_implemented":
        pytest.skip(f"upstream not available: {result.caveats}")
    assert result.status == "optimal"
    assert result.primal is not None
    assert result.primal["a_magic"] == a_magic
    assert result.primal["hecke_level"] == 3 * a_magic
    det = result.primal["det_2x2"]
    assert det >= -1e-12, f"det(2x2) = {det} for a_magic = {a_magic}"


def test_level4_psd_block_structure():
    """PSD-blocks output must include the 2x2 shell-closure block."""
    try:
        result = sdp.solve_shell_magic_sdp(a_magic=2)
    except ImportError:
        pytest.skip("sigma_shell_characterization not importable")
    if result.status == "not_implemented":
        pytest.skip("upstream not available")
    blocks = result.psd_blocks
    assert len(blocks) == 1
    assert blocks[0]["name"] == "shell_closure_2x2"
    assert blocks[0]["size"] == 2


def test_sdp_result_dataclass():
    r = sdp.SDPResult(level=3, status="optimal", objective=1.5)
    assert r.level == 3
    assert r.status == "optimal"
    assert r.objective == 1.5
    assert r.psd_blocks == []
    assert r.caveats == []
