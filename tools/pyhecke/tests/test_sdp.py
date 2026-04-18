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
    """Only level 3 is fully implemented today."""
    assert sdp.implemented_levels() == [3]
    assert sdp.pending_levels() == [4, 5, 6, 7]


@pytest.mark.parametrize("level", [4, 5, 6, 7])
def test_pending_levels_report_not_implemented(level):
    result = sdp.multi_level_sdp(level)
    assert result.status == "not_implemented"
    assert any("Track C" in c or "audit" in c.lower() for c in result.caveats)


def test_sdp_result_dataclass():
    r = sdp.SDPResult(level=3, status="optimal", objective=1.5)
    assert r.level == 3
    assert r.status == "optimal"
    assert r.objective == 1.5
    assert r.psd_blocks == []
    assert r.caveats == []
