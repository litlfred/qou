"""Bridge dispatch tests — do not require a compiled binary to be present.

Exercises the resolver behaviour only; real subprocess tests live in M3
when the unified `hecke` binary ships.
"""

from __future__ import annotations

import os
from pathlib import Path

from pyhecke import bridge


def test_engine_dir_autodetect():
    d = bridge.engine_dir()
    assert d.name == "hecke-engine"


def test_binary_path_returns_none_for_unknown():
    assert bridge.binary_path("no-such-hecke-binary-xyz") is None


def test_bridge_refuses_divergent_native_wheel(monkeypatch):
    """When `pyhecke.gram._native_ok()` is False (e.g. a pre-2026-08-15
    convention-C wheel installed on the host), `bridge.gram_matrix_from_rust`
    and `bridge.gram_det_from_rust` must NOT call `_NATIVE` and return
    convention-C numbers; they must fall through to `gram_from_rust`."""
    import pytest
    from pyhecke import gram as pg

    class _StaleNativeStub:
        def gram_matrix(self, q):  # pragma: no cover
            raise AssertionError("stale _NATIVE.gram_matrix must not be called")

        def gram_determinant(self, q):  # pragma: no cover
            raise AssertionError("stale _NATIVE.gram_determinant must not be called")

    monkeypatch.setattr(bridge, "_NATIVE", _StaleNativeStub())
    monkeypatch.setattr(pg, "_native_ok", lambda: False)
    monkeypatch.setattr(
        bridge,
        "gram_from_rust",
        lambda q=None: (_ for _ in ()).throw(FileNotFoundError("hecke-gram not built")),
    )

    with pytest.raises(FileNotFoundError):
        bridge.gram_matrix_from_rust()
    with pytest.raises(FileNotFoundError):
        bridge.gram_det_from_rust()


def test_bridge_uses_proton_pin_q0_when_native_verified(monkeypatch):
    """Default `q` in `bridge.gram_matrix_from_rust()` / `gram_det_from_rust()`
    must be `float(pyhecke.gram.q0)` (proton pin `1.1099785827513808`), not the
    retired muon literal `1.1099785955541805`."""
    from pyhecke import gram as pg

    seen_q: list[float] = []

    class _VerifiedNativeStub:
        def gram_matrix(self, q):
            seen_q.append(q)
            return pg.G.tolist()

        def gram_determinant(self, q):
            seen_q.append(q)
            return 0.0

    monkeypatch.setattr(bridge, "_NATIVE", _VerifiedNativeStub())
    monkeypatch.setattr(pg, "_native_ok", lambda: True)

    G = bridge.gram_matrix_from_rust()
    det = bridge.gram_det_from_rust()
    assert G.shape == (6, 6)
    assert det == 0.0
    assert seen_q == [float(pg.q0), float(pg.q0)]

