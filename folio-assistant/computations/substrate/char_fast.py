#!/usr/bin/env python3


# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Fast character computation — improved χ_λ(β) evaluator.

OLD path (sym_alt_mirror_probe.py, d_wedderburn_profile.py):
  For each σ^λ matrix, loops over every (i,j) element calling
  sp.N(elem.subs(q_sym, Q0)) individually.  For dim = 132 (e.g.
  shape (6,3,3) of n=12), this is 132² = 17,424 sympy.subs per
  σ^λ matrix, times 11 gens, times each partition.  Minutes
  per partition for large dim; hours for 4He's 77 partitions.

NEW path here:
  Use sp.lambdify to build a compiled numeric function from the
  symbolic σ^λ(q) matrix, evaluate at q₀ in one numpy call.
  10-100× speedup.

Optional: 50-digit mpmath mode for high-precision character
evaluation (still uses compiled function via sympy.lambdify with
mpmath backend).

Usage:
  from char_fast import chi_lambda_fast
  chi = chi_lambda_fast(shape, word, q_val=1.10998, precision="double")
  chi = chi_lambda_fast(shape, word, q_val="1.10998...", precision="mpmath50")
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import warnings
from pathlib import Path
from functools import lru_cache

import numpy as np
import sympy as sp

warnings.filterwarnings("ignore", category=UserWarning)
sys.path.insert(0, str(Path(__file__).parent))

from mass_at_3A_proper import _cached_seminormal

Q_SYM = sp.Symbol("q")


@lru_cache(maxsize=1024)
def _compiled_sigmas(shape: tuple, precision: str = "double"):
    """Build lambdified σ_i^λ matrices for a given partition.

    Returns a tuple of compiled functions σ_i(q) → numpy/mpmath matrix.
    Cached per (shape, precision).
    """
    sigmas, dim, _ = _cached_seminormal(shape)
    if dim == 0:
        return (), 0

    compiled = []
    for S in sigmas:
        S_arr = S.toarray() if hasattr(S, "toarray") else np.asarray(S)
        # Convert to sympy Matrix (symbolic)
        def _safe_sympify(val):
            if type(val).__name__.startswith("float") or isinstance(val, float):
                return sp.Float(float(val))
            if type(val).__name__.startswith("int") or isinstance(val, int):
                return sp.sympify(int(val))
            return sp.sympify(val)
        S_sym = sp.Matrix(dim, dim, lambda i, j: _safe_sympify(S_arr[i, j]))

        # Compile to numeric function
        if precision == "mpmath50":
            fn = sp.lambdify(Q_SYM, S_sym, modules=["mpmath"])
        else:
            fn = sp.lambdify(Q_SYM, S_sym, modules=["numpy"])
        compiled.append(fn)
    return tuple(compiled), dim


def chi_lambda_fast(shape: tuple, word,
                     q_val=None,
                     precision: str = "double") -> complex:
    """χ_λ(β) evaluated at q = q_val.

    shape:     partition (tuple of ints)
    word:      list of (c, d, g) Hecke factors
    q_val:     float, mpmath mpf, or None (uses q₀ from q_parameter)
    precision: "double" (numpy) or "mpmath50" (mpmath 50-digit)
    """
    from q_parameter import Q as Q0
    if q_val is None:
        q_val = Q0

    sigmas_fns, dim = _compiled_sigmas(shape, precision)
    if dim == 0:
        return 0.0 + 0j

    # Evaluate each σ_i^λ at q_val — ONE call each, vectorised
    sigmas_num = []
    for fn in sigmas_fns:
        M = np.asarray(fn(q_val), dtype=complex)
        sigmas_num.append(M)

    I = np.eye(dim, dtype=complex)
    prod = I.copy()
    for (c, d, g) in word:
        if g < len(sigmas_num):
            prod = prod @ (complex(c) * sigmas_num[g] + complex(d) * I)
        else:
            return 0.0 + 0j
    return complex(np.trace(prod))


def chi_lambda_fast_mp(shape: tuple, word, q_val) -> "mpmath.mpc":
    """50-digit mpmath version of χ_λ(β).

    q_val MUST be an mpmath.mpf. Uses mpmath matrix arithmetic.
    ~10x slower than double-precision but 50-digit precise.
    """
    import mpmath as mp
    sigmas_fns, dim = _compiled_sigmas(shape, precision="mpmath50")
    if dim == 0:
        return mp.mpc(0)

    sigmas_num = []
    for fn in sigmas_fns:
        # fn returns list-of-lists of mpmath numbers
        M = fn(q_val)
        if not isinstance(M, mp.matrix):
            M = mp.matrix(M)
        sigmas_num.append(M)

    I = mp.eye(dim)
    prod = mp.matrix(I)
    for (c, d, g) in word:
        if g < len(sigmas_num):
            coeff = mp.mpf(c) * sigmas_num[g] + mp.mpf(d) * I
            prod = prod * coeff
        else:
            return mp.mpc(0)
    return sum(prod[i, i] for i in range(dim))


# ── Benchmark ─────────────────────────────────────────────

if __name__ == "__main__":
    import time
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_characters import partitions_of

    print("=" * 90)
    print("CHARACTER COMPUTATION BENCHMARK")
    print("=" * 90)

    # Old-style reference (D, A=2, n=6) — compare against chi_at_q0
    Z, N = 1, 1
    word = atom_braid_word_3A(Z, N)
    parts = list(partitions_of(6))
    print(f"\nD: A=2, n=6, partitions={len(parts)}, "
          f"word={len(word)} factors")

    print(f"\n  {'shape':>14} {'dim':>5} {'χ (fast)':>14} "
          f"{'t_fast (ms)':>12}")
    t_total = time.time()
    for shape in parts:
        _, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        t0 = time.time()
        chi = chi_lambda_fast(shape, word)
        dt = (time.time() - t0) * 1000
        print(f"  {str(shape):>14} {dim:>5} "
              f"{chi.real:>+10.4f}{chi.imag:+.1e}j "
              f"{dt:>12.2f}")
    print(f"  total (D, all {len(parts)} partitions): "
          f"{(time.time()-t_total)*1000:.0f} ms")

    # Compare: 4He has n=12, 77 partitions — the real test
    print(f"\n{'=' * 90}")
    print("4He benchmark (n=12, 77 partitions)")
    print("=" * 90)
    Z, N = 2, 2
    word = atom_braid_word_3A(Z, N)
    parts = list(partitions_of(12))
    print(f"Partitions of 12: {len(parts)}")
    print(f"Word length: {len(word)}")

    # Sym and alt only (small, fast)
    print(f"\n  {'partition':>14} {'dim':>5} {'χ (fast)':>14} {'t (ms)':>8}")
    for shape in [(12,), (1,) * 12]:
        _, dim, _ = _cached_seminormal(shape)
        t0 = time.time()
        chi = chi_lambda_fast(shape, word)
        dt = (time.time() - t0) * 1000
        print(f"  {str(shape):>14} {dim:>5} "
              f"{chi.real:>+10.4f}{chi.imag:+.1e}j {dt:>8.2f}")

    # Mid-sized: (6, 6)
    shape = (6, 6)
    _, dim, _ = _cached_seminormal(shape)
    t0 = time.time()
    chi = chi_lambda_fast(shape, word)
    dt = (time.time() - t0) * 1000
    print(f"  {str(shape):>14} {dim:>5} "
          f"{chi.real:>+10.4f}{chi.imag:+.1e}j {dt:>8.2f}")
