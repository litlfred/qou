"""The Rust character kernel must give the same number as the Python loop.

Bean `qou-sv7h`. `unified_iterative_correction` now routes its per-partition
matrix product through `pyhecke_native.chi_q_atomic_mpfr` instead of
multiplying mpf matrices in Python. That took deuterium from "did not finish
in 150 s of profiling" (bean estimate: ~40 days) to 44 s.

A speedup that changes the number is worthless, and this producer feeds
binding energies. So: run both paths on inputs small enough that the Python
one finishes, and require agreement at mpf roundoff.

The bean asked for exactly this before the change could land — "Landing it
needs a value-equality check on a subset that completes both ways (use
k_exact to shrink the partition set)".
"""

from __future__ import annotations

import os
import sys

import pytest

_COMPUTATIONS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "computations")
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

mp = pytest.importorskip("mpmath")
L = pytest.importorskip("hecke_core_legacy")

pytestmark = pytest.mark.skipif(
    not getattr(L, "_HAVE_RUST_CHI", False),
    reason="pyhecke_native.chi_q_atomic_mpfr unavailable; Python path only")

# Agreement at 50 dps is ~1e-48 (measured 7.3e-50 .. 1.1e-48 over k_exact
# 4..7). 1e-40 is loose enough not to be flaky and eight decades tighter than
# anything that would signal a real divergence.
REL_TOL = mp.mpf("1e-40")


@pytest.fixture(autouse=True)
def _dps():
    """50 dps per test, without leaking the setting to other test modules."""
    with mp.workdps(50):
        yield


@pytest.mark.parametrize("k_exact", [4, 5, 6, 7])
def test_rust_and_python_paths_agree(k_exact):
    """Same input, both paths, same number."""
    py = mp.mpf(L.unified_iterative_correction(1, 1, k_exact=k_exact,
                                               use_rust=False))
    rs = mp.mpf(L.unified_iterative_correction(1, 1, k_exact=k_exact,
                                               use_rust=True))
    rel = abs(py - rs) / abs(py) if py else abs(py - rs)
    assert rel < REL_TOL, (
        f"k_exact={k_exact}: python={mp.nstr(py, 20)} "
        f"rust={mp.nstr(rs, 20)} rel={mp.nstr(rel, 6)}")


@pytest.mark.parametrize("Z,N", [(1, 1), (1, 2), (2, 1)])
def test_paths_agree_across_nuclides(Z, N):
    """The chains differ per (Z, N) — check more than one ordering."""
    py = mp.mpf(L.unified_iterative_correction(Z, N, k_exact=5, use_rust=False))
    rs = mp.mpf(L.unified_iterative_correction(Z, N, k_exact=5, use_rust=True))
    rel = abs(py - rs) / abs(py) if py else abs(py - rs)
    assert rel < REL_TOL, f"(Z,N)=({Z},{N}) rel={mp.nstr(rel, 6)}"


def test_rust_is_the_default_when_available():
    """`use_rust=None` must pick the fast path, or the speedup is theoretical."""
    auto = mp.mpf(L.unified_iterative_correction(1, 1, k_exact=5))
    rs = mp.mpf(L.unified_iterative_correction(1, 1, k_exact=5, use_rust=True))
    assert auto == rs


def test_explicit_use_rust_without_the_kernel_raises():
    """Asking for Rust when it is absent must fail loudly, not fall back.

    A silent fallback would turn a 40x regression into something only a
    stopwatch could find.
    """
    saved = L._HAVE_RUST_CHI
    try:
        L._HAVE_RUST_CHI = False
        with pytest.raises(RuntimeError, match="pyhecke_native"):
            L.unified_iterative_correction(1, 1, k_exact=4, use_rust=True)
    finally:
        L._HAVE_RUST_CHI = saved
