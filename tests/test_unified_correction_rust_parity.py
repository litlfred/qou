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


# ── atom_character_raw (bean `qou-sv7h`) ──────────────────────────────
#
# `binding_energy` is three terms and only one of them was routed through Rust
# at first. That was not enough: the nuclide table ran 21 minutes without
# completing deuterium, because `binding_from_frobenius_pairing` ->
# `atom_markov_trace` calls `atom_character_raw` once per partition and it was
# still the O(dim^3) mpmath loop. One accelerated term out of three is no
# faster than the slowest term.


def _active_entries(k_max, want=4):
    """A few real partition-table entries, smallest dim first."""
    rows = [e for e in L._PARTITION_TABLE
            if e.get("has_ysn") and e.get("ysn") and e.get("k", 0) <= k_max]
    rows.sort(key=lambda e: e.get("dim", 0))
    return rows[:want]


@pytest.mark.parametrize("include_inter", [True, False])
def test_atom_character_raw_paths_agree(include_inter):
    """Rust and Python must return the same character, both conventions.

    Compared as `chi * exp(log_norm)`, not `chi` alone: the Python path splits
    the value across a mantissa and a rescaling exponent, while the Rust path
    needs no rescaling (MPFR's exponent range makes the `m_max > 1e80` guard
    unnecessary) and returns log_norm = 0. Both callers multiply them back
    together, so that product is the quantity that must match.
    """
    with mp.workdps(50):
        entries = _active_entries(k_max=5)
        assert entries, "no YSN partition entries available"
        for e in entries:
            py = L.atom_character_raw(1, 1, e, include_inter=include_inter,
                                      use_rust=False)
            rs = L.atom_character_raw(1, 1, e, include_inter=include_inter,
                                      use_rust=True)
            vp = py[0] * mp.exp(py[1])
            vr = rs[0] * mp.exp(rs[1])
            rel = abs(vp - vr) / abs(vp) if vp else abs(vp - vr)
            assert rel < REL_TOL, (
                f"{e['partition']} include_inter={include_inter}: "
                f"py={mp.nstr(vp, 20)} rust={mp.nstr(vr, 20)} "
                f"rel={mp.nstr(rel, 6)}")
            assert rs[1] == 0, "the Rust path should need no rescaling"
            assert py[2] == rs[2], "dim disagrees"


def test_atom_character_raw_defaults_to_rust():
    """`use_rust=None` must take the fast path, or the speedup is theoretical."""
    with mp.workdps(50):
        e = _active_entries(k_max=4, want=1)[0]
        auto = L.atom_character_raw(1, 1, e)
        rs = L.atom_character_raw(1, 1, e, use_rust=True)
        assert auto[0] == rs[0] and auto[1] == rs[1]


def test_atom_character_raw_explicit_rust_without_kernel_raises():
    """Absent the kernel, asking for Rust must fail loudly, not fall back."""
    saved = L._HAVE_RUST_CHI
    try:
        L._HAVE_RUST_CHI = False
        e = _active_entries(k_max=4, want=1)[0]
        with pytest.raises(RuntimeError, match="pyhecke_native"):
            L.atom_character_raw(1, 1, e, use_rust=True)
    finally:
        L._HAVE_RUST_CHI = saved


# ── atom_markov_trace (bean `qou-uiut`) ───────────────────────────────
#
# `atom_character_raw` parity above is NOT sufficient for its callers.
# `atom_markov_trace` recombines the per-partition results as
#
#     max_ln = max(log_norm over partitions)
#     chi_eff = chi * exp(log_norm - max_ln)
#
# so it depends on `log_norm`, and the Rust path returns log_norm = 0 by
# construction (MPFR needs no rescaling). Where the Python path also produces
# log_norm = 0 — which is everywhere the running product stays under 1e80 —
# the two must agree exactly. This pins that.
#
# Where they DIVERGE is documented rather than tested, because it cannot be
# tested here: log_norm only becomes non-zero for large-dim partitions at high
# A, and those are precisely the cases the pure-Python path cannot finish, which
# is why the Rust path exists. See the bean.


@pytest.mark.parametrize("Z,N", [(1, 1), (1, 2), (2, 2)])
@pytest.mark.parametrize("include_inter", [True, False])
def test_atom_markov_trace_paths_agree(Z, N, include_inter):
    """The recombination, not just the per-partition character."""
    with mp.workdps(50):
        saved = L._HAVE_RUST_CHI
        try:
            L._HAVE_RUST_CHI = False
            py = mp.mpf(L.atom_markov_trace(Z, N, k_cap=5,
                                            include_inter=include_inter))
            L._HAVE_RUST_CHI = True
            rs = mp.mpf(L.atom_markov_trace(Z, N, k_cap=5,
                                            include_inter=include_inter))
        finally:
            L._HAVE_RUST_CHI = saved
        rel = abs(py - rs) / abs(py) if py else abs(py - rs)
        assert rel < REL_TOL, (
            f"(Z,N)=({Z},{N}) include_inter={include_inter}: "
            f"py={mp.nstr(py, 20)} rust={mp.nstr(rs, 20)} rel={mp.nstr(rel, 6)}")
