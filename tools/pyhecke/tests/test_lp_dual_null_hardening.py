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


def test_empty_active_set_with_nonzero_y_star_fails(tmp_path):
    """An empty active set CONTRADICTING a nonzero y_star must fail.

    Renamed from `test_empty_active_set_fails`, which asserted the wrong
    reason and had been red against the implementation for as long as both
    existed. Emptiness alone is not the defect — `_FULL` carries
    `y_star = [0.0, 0.3]`, so constraint 1 IS tight and the active set
    should be `[1]`. The two fields contradict each other, because the
    active set is *defined* as `{i : y_star[i] > 0}`.

    The failure is therefore reported under `inconsistent`, not `missing`:
    nothing is absent here, the present values disagree."""
    payload = dict(_FULL, active_set=[])
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    assert r["missing"] == [], r["missing"]
    assert len(r["inconsistent"]) == 1, r["inconsistent"]
    assert "active_set is empty but y_star" in r["inconsistent"][0]


def test_empty_active_set_with_zero_y_star_passes(tmp_path):
    """An interior optimum — no tight constraint — is legitimate.

    This is the case the corpus actually contains. Of 3096 witnesses, 14
    carry an empty active set and ALL 14 pair it with an absent or all-zero
    `y_star` (e.g. `wedderburn-lp-ew-wiring`, `duality_gap = 0.0`,
    `y0_star = 5.2e-06`). Failing emptiness outright would have rejected
    every one of them, which is why the implementation carved it out —
    it was right about this half."""
    payload = dict(_FULL, active_set=[], y_star=[0.0, 0.0])
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is True, (r["missing"], r["inconsistent"])


def test_consistent_nonempty_active_set_passes(tmp_path):
    """The ordinary case: active set matches the tight constraint."""
    payload = dict(_FULL, active_set=[1], y_star=[0.0, 0.3])
    assert verify_dual_present(_write(tmp_path, payload))["ok"] is True


def test_inconsistency_is_found_in_nested_records(tmp_path):
    """Real witnesses nest the dual under `data.…[i]`, not at the root, so
    the check has to pair the two fields at the SAME object level.

    A flat 'is this key anywhere in the file' scan cannot do that — it was
    how an earlier census of mine mis-answered this exact question, pairing
    an empty active set against a `y_star` belonging to a different LP."""
    payload = {
        **_FULL,
        "data": {"per_atom": [{"lp_dual": dict(_FULL, active_set=[])}]},
    }
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    assert "data.per_atom[0].lp_dual" in r["inconsistent"][0], r["inconsistent"]


def test_empty_y_star_fails(tmp_path):
    payload = dict(_FULL, y_star=[])
    r = verify_dual_present(_write(tmp_path, payload))
    assert r["ok"] is False
    assert "y_star" in r["missing"]
