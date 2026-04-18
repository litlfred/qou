"""Tests for the PyO3 native acceleration layer.

Skipped if `pyhecke_native` has not been built (requires
`cd tools/pyhecke-native && maturin build && pip install target/wheels/*.whl`).
"""

from __future__ import annotations

import pytest

from pyhecke import bridge


pytestmark = pytest.mark.skipif(
    not bridge.has_native(),
    reason="pyhecke_native wheel not installed — run `maturin build && pip install ...`",
)


def test_native_version():
    import pyhecke_native
    assert pyhecke_native.__version__ == "0.1.0"


def test_native_markov_z_matches_python():
    import pyhecke_native

    from pyhecke import gram as pg

    q = 1.1099785955541805
    assert abs(pyhecke_native.markov_z(q) - pg.z) < 1e-14


def test_native_trace_weights_match_python():
    import pyhecke_native

    from pyhecke import gram as pg

    q = 1.1099785955541805
    tr = pyhecke_native.trace_weights(q)
    assert len(tr) == 6
    for a, b in zip(tr, pg.TR_M.tolist()):
        assert abs(a - b) < 1e-14


def test_native_gram_matches_python():
    import numpy as np
    import pyhecke_native

    from pyhecke import gram as pg

    G_native = np.array(pyhecke_native.gram_matrix(1.1099785955541805))
    assert G_native.shape == (6, 6)
    assert np.max(np.abs(G_native - pg.G)) < 1e-14


def test_native_det_matches_python():
    import numpy as np
    import pyhecke_native

    from pyhecke import gram as pg

    d_native = pyhecke_native.gram_determinant(1.1099785955541805)
    d_py = np.linalg.det(pg.G)
    assert abs(d_native - d_py) < 1e-10


def test_bridge_dispatches_to_native():
    """When native is present, gram_matrix_from_rust uses it."""
    import numpy as np

    G = bridge.gram_matrix_from_rust()
    assert G.shape == (6, 6)
    assert abs(G[0, 0] - 1.0) < 1e-14


def test_bridge_det_uses_native():
    det = bridge.gram_det_from_rust()
    assert abs(det - (-0.3608011166161873)) < 1e-10


def test_native_gram_inverse_is_right_inverse():
    import numpy as np
    import pyhecke_native

    q = 1.1099785955541805
    G = np.array(pyhecke_native.gram_matrix(q))
    Gi = np.array(pyhecke_native.gram_inverse(q))
    prod = G @ Gi
    assert np.allclose(prod, np.eye(6), atol=1e-10)


def test_native_different_q_differs():
    """Different q values produce different Gram matrices."""
    import numpy as np
    import pyhecke_native

    G1 = np.array(pyhecke_native.gram_matrix(1.10))
    G2 = np.array(pyhecke_native.gram_matrix(1.20))
    assert not np.allclose(G1, G2)
