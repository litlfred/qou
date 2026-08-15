"""P1 smoke tests — verify the public API surface is importable and
the dataclasses behave."""
from __future__ import annotations

import re
from decimal import Decimal

import pytest


def test_imports():
    """Every advertised symbol resolves."""
    import qou_mass as qm
    for sym in (
        "__version__",
        "predict", "predict_nucleon", "predict_table",
        "compute_tr_M", "canonical_braid",
        "Prediction", "Witness", "BraidWord",
    ):
        assert hasattr(qm, sym), f"qou_mass missing public symbol: {sym}"


def test_version_string():
    import qou_mass as qm
    assert isinstance(qm.__version__, str)
    # Was `startswith("0.")  # alpha series`. That pinned the series rather
    # than the shape, so it had to fail the first time the package left
    # alpha — which v1.0.0 did, on a witness-JSON change (MAJOR per the
    # policy in _version.py). Assert the shape instead.
    assert re.fullmatch(r"\d+\.\d+\.\d+([ab]\d+)?", qm.__version__)
    # The two version sources are edited by hand (see _version.py); this
    # catches them drifting apart, which nothing else does.
    import tomllib
    from pathlib import Path
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    declared = tomllib.loads(pyproject.read_text())["project"]["version"]
    assert declared == qm.__version__, (
        f"pyproject.toml says {declared}, qou_mass.__version__ says "
        f"{qm.__version__} — bump both"
    )


def test_prediction_str():
    from qou_mass import Prediction
    p = Prediction(
        atom="4He",
        Z=2, N=2,
        observable="binding_energy",
        value=Decimal("28.295"),
        units="MeV",
        method="markov_peel",
        precision_dps=50,
    )
    s = str(p)
    assert "4He" in s
    assert "28.295" in s
    assert "MeV" in s


# test_p1_stubs_raise_notimplemented removed in P2 — the public
# compute paths are now LIVE (read from vendored per-Z shards).
# See test_p2_integration.py for the numerical golden tests that
# replaced this shape-only check.
