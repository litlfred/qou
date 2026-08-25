#!/usr/bin/env python3
"""Cross-check `chi_lambda_of_word_sparse_mp` against the dense routine.

The sparse routine's whole claim is that it computes the SAME number as
`chi_lambda_of_word_mp` far faster. That is only worth anything if it is
checked, so this is the check.

Run: `python3 computations/hoefsmit_sparse_character_test.py`
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE / "substrate")]

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

# BEFORE any mpf arithmetic. `_precision`'s own docstring: "IMPORTING THIS
# MODULE DOES NOT SET mp.dps". Neither does `hoefsmit_mpmath`. Omitting this
# leaves mpmath at its default 15, both routines then compute at float64 grade,
# and they agree to ~1e-16 for that reason alone -- a test that passes while
# measuring nothing. That exact mistake is why bean `qou-fmoi` exists.
set_compute_dps()

import mass_at_3A_proper as m3  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from hoefsmit_mpmath import (  # noqa: E402
    BlockCacheMP,
    chi_lambda_of_word_mp,
    chi_lambda_of_word_sparse_mp,
    seminormal_matrices_mp,
)

# Small shapes only: the dense reference is O(dim^3 * len(word)), which is the
# reason the sparse routine exists. (6,6) at dim=132 already takes ~80 s, so
# anything larger would make the test unrunnable -- and a test nobody runs
# checks nothing.
SHAPES = [(6, 6), (9, 1, 1, 1)]

# Exact agreement means "to the working precision", not "to some tolerance we
# chose". At dps=70 the two routines differ at ~1e-71; 1e-60 leaves headroom
# for the accumulation order without admitting a float64-grade result, which
# would show up at ~1e-16 and fail loudly.
TOL = mp.mpf(10) ** -60


def main() -> int:
    assert mp.mp.dps >= 50, f"working precision is {mp.mp.dps}; test is meaningless"
    word = m3.atom_braid_word_3A(2, 2)
    # The 50-digit string, NOT `q_parameter.Q` -- that is a Python float, so
    # `mpf(str(Q))` keeps 16 digits and silently pins the whole test to a
    # float64-truncated substrate. It would still compare dense against sparse
    # correctly (same q both sides), but at the wrong q, and the character it
    # printed would disagree with the probe's at ~1e-16 for a reason having
    # nothing to do with either routine.
    q = mp.mpf(Q_50_DIGIT_STR)
    cache = BlockCacheMP(q)

    print(f"dps={mp.mp.dps}  word={len(word)} factors")
    failures = 0
    for shape in SHAPES:
        sig, dim, _ = seminormal_matrices_mp(shape, cache=cache)

        t = time.time()
        ref = chi_lambda_of_word_mp(sig, dim, word, 11)
        t_dense = time.time() - t

        t = time.time()
        got = chi_lambda_of_word_sparse_mp(sig, dim, word, 11)
        t_sparse = time.time() - t

        rel = abs(got - ref) / abs(ref) if ref != 0 else abs(got)
        ok = rel < TOL
        failures += 0 if ok else 1
        print(f"  {str(shape):<14} dim={dim:<5} "
              f"rel={mp.nstr(rel, 3):<12} "
              f"dense={t_dense:6.1f}s sparse={t_sparse:5.1f}s "
              f"({t_dense / t_sparse:.0f}x)  {'OK' if ok else 'FAIL'}")
        if not ok:
            print(f"      dense  = {mp.nstr(ref, 25)}")
            print(f"      sparse = {mp.nstr(got, 25)}")

    # A word using a generator the partition cannot supply must raise rather
    # than silently return a wrong trace -- the dense routine promises this and
    # the sparse one must not quietly differ.
    sig, dim, _ = seminormal_matrices_mp((6, 6), cache=cache)
    try:
        chi_lambda_of_word_sparse_mp(sig, dim, [(1, 0, 999)], 11)
    except IndexError:
        print("  out-of-range generator      raises IndexError          OK")
    else:
        print("  out-of-range generator      DID NOT RAISE              FAIL")
        failures += 1

    print("PASS" if failures == 0 else f"FAIL ({failures})")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
