"""A witness-less dependency propagates staleness only when its own source
changed after the dependent's witness was computed (owner ruling 2026-11-25).

`_path_bridge.py` writes no witness, so `_is_stale` reports it "no witness
file"; that verdict used to cascade to every importer (591 producers). These
tests pin the new rule on the decision function, with git stubbed out.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "computations", ROOT / "tools" / "qou-substrate" / "python"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import run_pipeline as rp  # noqa: E402


def _stub(monkeypatch, *, commit, computed, dirty=False, floor=None):
    monkeypatch.setattr(rp, "_module_last_commit", lambda name: commit)
    monkeypatch.setattr(rp, "_witness_computed_at", lambda script: computed)
    monkeypatch.setattr(rp, "_module_dirty", lambda name: dirty)
    monkeypatch.setattr(rp, "_shallow_floor", lambda: floor)


def test_unchanged_since_witness_does_not_propagate(monkeypatch):
    _stub(monkeypatch, commit=1_000.0, computed=2_000.0)
    assert rp._witnessless_dep_changed("_path_bridge.py", "p.py") is None


def test_changed_after_witness_propagates(monkeypatch):
    _stub(monkeypatch, commit=3_000.0, computed=2_000.0)
    assert "changed after" in rp._witnessless_dep_changed("_path_bridge.py", "p.py")


def test_uncommitted_edit_propagates(monkeypatch):
    _stub(monkeypatch, commit=1_000.0, computed=2_000.0, dirty=True)
    assert "uncommitted" in rp._witnessless_dep_changed("_path_bridge.py", "p.py")


def test_undatable_in_shallow_clone_is_conservative(monkeypatch):
    # Last commit is past the shallow boundary; witness is older than it.
    _stub(monkeypatch, commit=None, computed=500.0, floor=1_000.0)
    assert "undecidable" in rp._witnessless_dep_changed("_path_bridge.py", "p.py")
    # Witness newer than the boundary: the module cannot have changed since.
    _stub(monkeypatch, commit=None, computed=1_500.0, floor=1_000.0)
    assert rp._witnessless_dep_changed("_path_bridge.py", "p.py") is None
