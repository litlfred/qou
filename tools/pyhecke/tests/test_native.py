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


def _canonical_q0() -> float:
    """The repo's q_0, read from the source of truth rather than pinned here.

    These tests compare the Rust kernels against the Python ones. Both derive
    from q_0, so a q_0 hardcoded in the test compares the two implementations
    at DIFFERENT points and reports the difference as a kernel mismatch.

    That is what happened: the literal `1.1099785955541805` had drifted from
    the canonical `1.1099785827513808` at the 9th significant digit
    (dq ~ 1.3e-8), and `test_native_gram_matches_python` reported
    `max|native - python| = 6.64e-08` against a 1e-14 tolerance. At the
    canonical q_0 the two agree to exactly 0.0 — the kernels were never wrong.
    Sourcing the value is what keeps this a test of the kernels rather than of
    a stale constant. Bean `qou/ftuv`.
    """
    from pyhecke import gram as _pg
    return float(_pg.q0)


def _cargo_version() -> str:
    """`version = "..."` from `pyhecke-native/Cargo.toml`."""
    import re
    from pathlib import Path
    toml = (Path(__file__).resolve().parents[2]
            / "pyhecke-native" / "Cargo.toml").read_text()
    m = re.search(r'(?m)^version\s*=\s*"([^"]+)"', toml)
    assert m, "no version in pyhecke-native/Cargo.toml"
    return m.group(1)


def test_native_version():
    import pyhecke_native
    # Version is wired from Cargo.toml via env!("CARGO_PKG_VERSION") in
    # lib.rs. Compare against Cargo.toml rather than a literal: the literal
    # was pinned at "0.4.0" while the crate reached "0.9.0", so this asserted
    # a stale fact through five bumps despite its own comment saying to update
    # it in the same commit. Reading the source of truth checks the WIRING,
    # which is what the test is for, and cannot drift.
    assert pyhecke_native.__version__ == _cargo_version()


def test_native_markov_z_matches_python():
    import pyhecke_native

    from pyhecke import gram as pg

    q = _canonical_q0()
    assert abs(pyhecke_native.markov_z(q) - pg.z) < 1e-14


def test_native_trace_weights_match_python():
    import pyhecke_native

    from pyhecke import gram as pg

    q = _canonical_q0()
    tr = pyhecke_native.trace_weights(q)
    assert len(tr) == 6
    for a, b in zip(tr, pg.TR_M.tolist()):
        assert abs(a - b) < 1e-14


def test_native_gram_matches_python():
    import numpy as np
    import pyhecke_native

    from pyhecke import gram as pg

    G_native = np.array(pyhecke_native.gram_matrix(_canonical_q0()))
    assert G_native.shape == (6, 6)
    assert np.max(np.abs(G_native - pg.G)) < 1e-14


def test_native_det_matches_python():
    import numpy as np
    import pyhecke_native

    from pyhecke import gram as pg

    d_native = pyhecke_native.gram_determinant(_canonical_q0())
    d_py = np.linalg.det(pg.G)
    assert abs(d_native - d_py) < 1e-10


def test_bridge_dispatches_to_native():
    """When native is present, gram_matrix_from_rust uses it."""
    import numpy as np

    G = bridge.gram_matrix_from_rust()
    assert G.shape == (6, 6)
    assert abs(G[0, 0] - 1.0) < 1e-14


def test_bridge_det_uses_native():
    """The bridge reaches the Rust determinant, and that determinant is ZERO.

    This pinned `-0.3608011166161873` to within 1e-10. The Gram's determinant
    is not that number and has not been for as long as anyone can measure — it
    is **zero**, confirmed four independent ways:

        numpy.linalg.det(pg.G)              3.998399968397726e-17
        pyhecke_native.gram_determinant     0.0
        bridge.gram_det_from_rust()         3.5985600328525204e-16
        mpmath det of the 50-dps strings   -2.00868433511e-57

    and the MPFR determinant tracks the working precision rather than
    converging (-2.0e-57 at 60 dps, +5.7e-117 at 120 dps, sign flip included),
    which is what an exactly-zero determinant looks like in floating point. The
    H_3 Gram has a one-dimensional kernel; see `qou/ftuv`.

    So this was the one test in the repo that would have caught the Gram going
    singular, and it has been failing invisibly — `test_native.py` skips
    entirely when the `pyhecke_native` wheel is absent, which it usually is.
    A check that cannot run cannot fail.

    Asserting the property instead of a literal: the bridge must return the
    same value the native kernel does (that is what "uses native" means), and
    that value must be zero to f64 resolution.
    """
    import pyhecke_native
    from pyhecke import gram as pg

    det = bridge.gram_det_from_rust()
    assert det == pytest.approx(
        pyhecke_native.gram_determinant(float(pg.q0)), abs=1e-12
    ), "bridge is not returning the native determinant"
    assert abs(det) < 1e-12, (
        f"det(G) = {det!r}; the H_3 Gram is singular, so a nonzero determinant "
        "means the basis or q_0 changed — do not re-pin, investigate"
    )


def test_native_has_no_gram_inverse_and_quotient_inverse_kills_the_radical():
    """`pyhecke_native.gram_inverse` is GONE under convention D, and its
    replacement inverts only on the quotient.

    This replaces `test_native_gram_inverse_is_right_inverse`, which asserted
    `G @ gram_inverse(q) == I`. Convention D makes that identity false — the
    form is singular with corank 1 — and the binding was removed rather than
    repointed, so the old test would now raise AttributeError. It never did,
    because the module skips when `pyhecke_native` is not installed."""
    import numpy as np
    import pyhecke_native

    assert not hasattr(pyhecke_native, "gram_inverse"), (
        "gram_inverse must stay removed: under convention D the 6x6 inverse "
        "does not exist, and repointing the name at the pseudoinverse is how a "
        "wrong number keeps circulating under a trusted label"
    )

    q = _canonical_q0()
    G = np.array(pyhecke_native.gram_matrix(q))
    GP = np.array(pyhecke_native.gram_quotient_inverse(q))
    rad = np.array(pyhecke_native.gram_radical(q))

    assert np.linalg.norm(G @ rad) < 1e-10
    assert np.linalg.norm(GP @ rad) < 1e-10
    assert np.allclose(G @ GP @ G, G, atol=1e-10)


def test_native_different_q_differs():
    """Different q values produce different Gram matrices."""
    import numpy as np
    import pyhecke_native

    G1 = np.array(pyhecke_native.gram_matrix(1.10))
    G2 = np.array(pyhecke_native.gram_matrix(1.20))
    assert not np.allclose(G1, G2)


# ── M3d+: hm / nf_tr / nf_net ──────────────────────────────────────────

def test_native_hm_identity_action():
    """hm(γ, 1, 0, 0) → σ_0 — matches pyhecke.gram.hm byte-for-byte."""
    import pyhecke_native
    from pyhecke import gram as pg

    nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    out_native = pyhecke_native.hm(nf, 1.0, 0.0, 0)
    out_py = pg.hm(nf, 1.0, 0.0, 0)
    for a, b in zip(out_native, out_py):
        assert abs(a - b) < 1e-14


def test_native_hm_nontrivial_matches_python():
    """Multi-step hm chain agrees with Python."""
    import pyhecke_native
    from pyhecke import gram as pg

    # Apply σ_0 then σ_1 to γ
    nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    a1 = pyhecke_native.hm(nf, 1.0, 0.0, 0)
    a2 = pyhecke_native.hm(a1, 1.0, 0.0, 1)
    p1 = pg.hm(nf, 1.0, 0.0, 0)
    p2 = pg.hm(p1, 1.0, 0.0, 1)
    for a, b in zip(a2, p2):
        assert abs(a - b) < 1e-14


def test_native_hm_rejects_wrong_length():
    """hm must reject nf vectors that aren't length 6."""
    import pytest
    import pyhecke_native

    with pytest.raises(ValueError):
        pyhecke_native.hm([1.0, 2.0, 3.0], 1.0, 0.0, 0)


def test_native_nf_tr_matches_python():
    """nf_tr result agrees with pyhecke.gram.nf_tr."""
    import pyhecke_native
    from pyhecke import gram as pg

    nf = [1.5, -0.3, 0.7, -0.2, 0.11, 0.05]
    assert abs(pyhecke_native.nf_tr(nf) - pg.nf_tr(nf)) < 1e-14


def test_native_nf_net_matches_python():
    import pyhecke_native
    from pyhecke import gram as pg

    nf = [1.5, -0.3, 0.7, -0.2, 0.11, 0.05]
    assert abs(pyhecke_native.nf_net(nf) - pg.nf_net(nf)) < 1e-14


def test_native_version_bumped():
    # The installed wheel, Cargo.toml and pyproject.toml must agree — a wheel
    # built from a different tree than the one under test is exactly the
    # confusion this catches.
    import pyhecke_native
    import re
    from pathlib import Path

    assert pyhecke_native.__version__ == _cargo_version()
    pyproject = (Path(__file__).resolve().parents[2]
                 / "pyhecke-native" / "pyproject.toml")
    if pyproject.exists():
        m = re.search(r'(?m)^version\s*=\s*"([^"]+)"', pyproject.read_text())
        if m:
            assert m.group(1) == _cargo_version(), (
                f"pyproject.toml {m.group(1)} != Cargo.toml {_cargo_version()}")


# ── M3d++: build_atom_nf ───────────────────────────────────────────────

@pytest.mark.parametrize("z,n", [(1, 0), (1, 1), (2, 1), (2, 2), (6, 6), (8, 8), (20, 20)])
def test_native_build_atom_nf_matches_python(z, n):
    """Rust build_atom_nf must be byte-identical to Python for every
    physically relevant (Z, N)."""
    import pyhecke_native
    from pyhecke import gram as pg  # noqa: F401 — triggers hecke_core import
    import hecke_core
    import numpy as np

    py = hecke_core.build_atom_nf(z, n)
    rs = pyhecke_native.build_atom_nf(z, n)
    diff = np.max(np.abs(np.array(py) - np.array(rs)))
    assert diff < 1e-12, f"Z={z} N={n}: max diff {diff}"


def test_native_build_atom_nf_vacuum():
    """(0, 0) must return the identity NF."""
    import pyhecke_native
    nf = pyhecke_native.build_atom_nf(0, 0)
    assert abs(nf[0] - 1.0) < 1e-14
    for x in nf[1:]:
        assert abs(x) < 1e-14


def test_native_build_atom_nf_length_six():
    import pyhecke_native
    assert len(pyhecke_native.build_atom_nf(6, 6)) == 6


# ── B2+: atom_per_generator_volumes ────────────────────────────────────

@pytest.mark.parametrize("z,n", [(1, 0), (2, 2), (6, 6), (8, 8), (20, 20)])
def test_native_atom_per_generator_volumes_matches_python(z, n):
    """Rust per-generator Wedderburn volumes match Python to f64 eps."""
    import pyhecke_native
    from pyhecke import gram as pg  # noqa: F401 — triggers hecke_core
    import hecke_core

    py = hecke_core.atom_per_generator_volumes(z, n)
    rs = pyhecke_native.atom_per_generator_volumes(z, n)
    assert len(py) == len(rs), f"Z={z} N={n}: length {len(py)} vs {len(rs)}"
    max_diff = max(
        abs(p[k] - r[k])
        for p, r in zip(py, rs)
        for k in ("sym", "std", "alt", "full")
    )
    assert max_diff < 1e-12, f"Z={z} N={n}: max diff {max_diff}"


def test_native_atom_per_generator_volumes_vacuum():
    import pyhecke_native
    assert pyhecke_native.atom_per_generator_volumes(0, 0) == []


def test_native_atom_per_generator_volumes_free_baseline():
    """include_inter=False gives n_gens_total = 2A."""
    import pyhecke_native
    vols = pyhecke_native.atom_per_generator_volumes(2, 2, include_inter=False)
    assert len(vols) == 2 * (2 + 2)  # 8 generators


def test_native_atom_per_generator_volumes_inter_baseline():
    """include_inter=True gives n_gens_total = 3A - 1."""
    import pyhecke_native
    vols = pyhecke_native.atom_per_generator_volumes(2, 2, include_inter=True)
    assert len(vols) == 3 * (2 + 2) - 1  # 11 generators
