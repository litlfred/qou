"""The `environment` block must be monotonic — repairable, never silently degraded.

Bean `qou-dc0n`. `environment` is one of `_EPHEMERAL_META_FIELDS`, so a witness
differing ONLY in that block counts as substantively equal and takes `save()`'s
preserve branch. That branch used to `return` above
`_check_environment_regression`, which made the block sticky in both directions:
a degraded copy could not be repaired by re-running with the libraries restored
(the fresh, complete block was discarded), and no warning was emitted, so the
record went silent at exactly the moment it was wrong.

Measured on `reeb-g-structural-identity.witness.json`, 2026-08-23:

    payload changed, container missing clarabel/numpy/scipy  -> degraded, warns
    pip install the recorded libs, re-run                    -> STILL degraded, SILENT
    rm the witness, re-run                                   -> full block restored

These tests pin the fixed behaviour of all three steps.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    _environment_delta,
    _environment_is_repair,
)

FULL = {"python": "3.11.15", "numpy": "2.4.6", "scipy": "1.17.1",
        "mpmath": "1.4.1", "clarabel": "0.11.1"}
WEAK = {"python": "3.11.15", "mpmath": "1.3.0"}


def _write(tmp_path, env, payload=("x", 1)):
    """Save a witness with a forced `environment` block; return the file body."""
    wb = WitnessBuilder("env-monotonic-probe", output_dir=str(tmp_path))
    wb.add_data(payload[0], payload[1])
    out = wb.save(extra={"environment": dict(env)})
    return json.loads(Path(out).read_text(encoding="utf-8"))


# --- the pure comparison ----------------------------------------------------

def test_delta_reports_all_four_directions():
    d = _environment_delta(FULL, WEAK)
    assert set(d["stripped"]) == {"numpy", "scipy", "clarabel"}
    assert d["downgraded"] == ["mpmath 1.4.1 -> 1.3.0"]
    assert d["added"] == [] and d["upgraded"] == []

    d = _environment_delta(WEAK, FULL)
    assert set(d["added"]) == {"numpy", "scipy", "clarabel"}
    assert d["upgraded"] == ["mpmath 1.3.0 -> 1.4.1"]
    assert d["stripped"] == [] and d["downgraded"] == []


def test_repair_requires_strictly_stronger():
    assert _environment_is_repair(WEAK, FULL) is True
    assert _environment_is_repair(FULL, WEAK) is False
    # lateral: identical -> nothing to repair, must not write
    assert _environment_is_repair(FULL, FULL) is False
    # mixed (drops one, adds another) is a REGRESSION, not a repair:
    # losing a recorded library is provenance damage whatever came with it.
    mixed = {"python": "3.11.15", "mpmath": "1.4.1", "numpy": "2.4.6",
             "scipy": "1.17.1", "sympy": "1.14.0"}   # clarabel dropped
    assert _environment_is_repair(FULL, mixed) is False


# --- the save() behaviour that was broken -----------------------------------

def test_degraded_block_is_repaired_by_rerunning(tmp_path):
    """The step that used to be a no-op: re-run with the libraries restored."""
    _write(tmp_path, WEAK)
    body = _write(tmp_path, FULL)
    assert body["environment"] == FULL, (
        "re-running with the libraries installed must REPAIR the block; "
        "this is the exact step that silently did nothing before"
    )


def test_weaker_environment_never_degrades_a_preserved_file(tmp_path, capsys):
    """A degraded container must not weaken a file it is not otherwise rewriting."""
    _write(tmp_path, FULL)
    capsys.readouterr()
    body = _write(tmp_path, WEAK)
    assert body["environment"] == FULL, "the stronger on-disk block must be kept"

    err = capsys.readouterr().err
    assert "environment" in err, "the regression must no longer be silent"
    assert "NOT modified" in err, (
        "on the preserve path the message must not tell the agent to avoid "
        "committing a write that never happened"
    )


def test_payload_unchanged_by_a_repair_write(tmp_path):
    """A repair rewrites provenance only — never a number."""
    first = _write(tmp_path, WEAK, payload=("value", "7.2445e-71"))
    second = _write(tmp_path, FULL, payload=("value", "7.2445e-71"))
    assert first["data"] == second["data"]
    assert first["assertions"] == second["assertions"]


def test_repair_is_idempotent_so_two_containers_cannot_ping_pong(tmp_path):
    """Monotonicity: only upward moves write, so alternating runs converge.

    This is what keeps the fix from reintroducing the CI drift loop that
    masking `environment` was introduced to prevent.
    """
    _write(tmp_path, WEAK)
    repaired = _write(tmp_path, FULL)
    mtime_after_repair = (tmp_path / "env-monotonic-probe.witness.json").stat().st_mtime_ns

    # the weak container runs again: must NOT write
    _write(tmp_path, WEAK)
    assert (tmp_path / "env-monotonic-probe.witness.json").stat().st_mtime_ns == mtime_after_repair
    # and the strong one re-running is now a no-op too
    _write(tmp_path, FULL)
    assert (tmp_path / "env-monotonic-probe.witness.json").stat().st_mtime_ns == mtime_after_repair
    assert json.loads(
        (tmp_path / "env-monotonic-probe.witness.json").read_text(encoding="utf-8")
    )["environment"] == repaired["environment"]
