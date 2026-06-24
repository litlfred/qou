"""Regression tests for verify_dual_present null/empty hardening.

A witness that emits the dual-certificate KEYS with null (or empty)
VALUES used to pass the presence-only check while computing no dual —
the devils-advocate class-3 / witness-hollowness pattern that left 11
LP/SDP witnesses green in CI (see
docs/audits/2026-06-24-devils-advocate-wave4.md). `verify_dual_present`
now treats a null / empty value as NOT present.

These tests inline the witness JSON so they need no on-disk fixtures and
no numpy/cvxpy (the module's heavy deps are imported lazily for the
solver paths, not for verify_dual_present).
"""

from __future__ import annotations

import json
from pathlib import Path

from pyhecke.lp_dual_solver import verify_dual_present


_FULL = {
    "y0_star": 1.5,
    "y_star": [0.0, 0.3],
    "active_set": [1],
    "primal_obj": 2.0,
    "dual_obj": 2.0,
    "duality_gap": 0.0,
}


def _write(tmp_path: Path, payload: dict) -> Path:
    p = tmp_path / "w.witness.json"
    p.write_text(json.dumps(payload))
    return p


def test_real_dual_passes(tmp_path):
    assert verify_dual_present(_write(tmp_path, _FULL))["ok"] is True


def test_all_null_dual_fails(tmp_path):
    payload = {k: None for k in _FULL}
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    # every required scalar + the active alias must be reported missing
    assert "y0_star" in r["missing"]
    assert any("active" in m for m in r["missing"])


def test_single_null_scalar_fails(tmp_path):
    payload = dict(_FULL, y0_star=None)
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    assert "y0_star" in r["missing"]


def test_empty_active_set_fails(tmp_path):
    # active_set present but empty [] is hollow.
    payload = dict(_FULL, active_set=[])
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    assert any("active" in m for m in r["missing"])


def test_empty_y_star_fails(tmp_path):
    payload = dict(_FULL, y_star=[])
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    assert "y_star" in r["missing"]
