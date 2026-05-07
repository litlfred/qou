"""pytest for the LP/SDP cache layer."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from lp_dual_cache import (  # noqa: E402
    cached_solve_operator_selection_lp,
    clear_lp_cache,
    lp_cache_info,
    set_lp_cache_size,
)
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402


def _sample_lp() -> tuple[np.ndarray, np.ndarray, float]:
    t = np.array([1.0, 0.5, 0.3])
    G = np.array([[1.0, 0.2, 0.1],
                  [0.2, 1.0, 0.3],
                  [0.1, 0.3, 1.0]])
    return t, G, 1.0


def test_first_call_is_a_miss():
    clear_lp_cache()
    t, G, n = _sample_lp()
    cached_solve_operator_selection_lp(t, G, n)
    info = lp_cache_info()
    assert info["lp_misses"] == 1
    assert info["lp_hits"] == 0
    assert info["lp_size"] == 1


def test_repeat_calls_are_hits():
    clear_lp_cache()
    t, G, n = _sample_lp()
    for _ in range(50):
        cached_solve_operator_selection_lp(t, G, n)
    info = lp_cache_info()
    assert info["lp_misses"] == 1
    assert info["lp_hits"] == 49


def test_perturbed_input_is_a_miss():
    clear_lp_cache()
    t, G, n = _sample_lp()
    cached_solve_operator_selection_lp(t, G, n)
    t2 = t.copy()
    t2[0] += 1e-12
    cached_solve_operator_selection_lp(t2, G, n)
    assert lp_cache_info()["lp_misses"] == 2


def test_different_n_target_is_a_miss():
    clear_lp_cache()
    t, G, _ = _sample_lp()
    cached_solve_operator_selection_lp(t, G, 1.0)
    cached_solve_operator_selection_lp(t, G, 2.0)
    assert lp_cache_info()["lp_misses"] == 2


def test_cached_result_matches_uncached():
    clear_lp_cache()
    t, G, n = _sample_lp()
    direct = solve_operator_selection_lp(t, G, n).to_dict()
    cached = cached_solve_operator_selection_lp(t, G, n).to_dict()
    assert cached == direct


def test_clear_cache_resets_everything():
    clear_lp_cache()
    t, G, n = _sample_lp()
    cached_solve_operator_selection_lp(t, G, n)
    cached_solve_operator_selection_lp(t, G, n)
    clear_lp_cache()
    info = lp_cache_info()
    assert info == {
        "lp_hits": 0, "lp_misses": 0, "lp_size": 0, "lp_maxsize": 1024,
        "sdp_hits": 0, "sdp_misses": 0, "sdp_size": 0, "sdp_maxsize": 256,
    }


def test_cache_eviction_on_size_limit():
    clear_lp_cache()
    set_lp_cache_size(3)  # tiny cache
    t, G, _ = _sample_lp()
    # Fill 5 distinct entries; oldest 2 must be evicted
    for k in range(5):
        cached_solve_operator_selection_lp(t, G, float(k + 1))
    info = lp_cache_info()
    assert info["lp_size"] == 3
    assert info["lp_misses"] == 5
    set_lp_cache_size(1024)  # restore default


def test_cached_result_is_independent_object():
    """Mutating a cached result must not poison the cache."""
    clear_lp_cache()
    t, G, n = _sample_lp()
    r1 = cached_solve_operator_selection_lp(t, G, n)
    r1.x_star[0] = -999.0
    r2 = cached_solve_operator_selection_lp(t, G, n)
    assert r2.x_star[0] != -999.0
