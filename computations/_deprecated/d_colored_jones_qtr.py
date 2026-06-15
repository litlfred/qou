#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
D's colored-Jones tower with quantum trace + root-of-unity limit.

Fixes two defects in d_colored_jones_tower.py:

  1. QUANTUM TRACE instead of ordinary trace: for the colored
     Jones, we trace ρ(β) · K^⊗n where K = diag(q^{N-1}, q^{N-3}, ...,
     q^{-(N-1)}).  This is the Reshetikhin-Turaev convention.

  2. ROOT-OF-UNITY LIMIT: at q = e^{2πi/N}, both qtr and [N]_q vanish;
     the ratio J_N = qtr/[N]_q^{n-1} is finite via L'Hôpital.
     Implemented by evaluating at q = root · exp(i·ε) for small ε and
     taking ε → 0 (Richardson extrapolation from ε ∈ {1e-4, 1e-5, 1e-6}).

Goal: J_N(β_D, e^{2πi/N}) for N = 2, 3, 4, 5 and check whether the
Kashaev-style asymptotic 2π log|J_N|/N converges to B_AME(D)/m_e.
"""
from __future__ import annotations

import sys
import json
import time
import cmath
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp
import mpmath

# Precision applied only when the script is run directly.  This avoids
# leaking mpmath.mp.dps into other modules that import symbols from
# this file.  Inside functions we use mpmath.workdps for local scope.
_MP_DPS = 40
if __name__ == "__main__":
    mpmath.mp.dps = _MP_DPS

from hecke_symbolic import (
    SymbolicHeckeElement, SymbolicHeckeDivision,
    q as q_sym, HA as HA_sym,
)
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV

B_D_AME = 2.22456612
TARGET_VOL = B_D_AME / M_E_MEV
N_STRANDS = 6


def _factor_from(c_f, d_f, g):
    c = sp.Integer(1) if abs(c_f - 1.0) < 1e-6 else sp.Integer(0)
    if abs(d_f) < 1e-12:
        d = sp.Integer(0)
    elif abs(d_f + float(HA_sym.subs(q_sym, sp.Rational(str(Q0_FLOAT))))) < 1e-3:
        d = -HA_sym
    elif abs(d_f + 0.5 * float(HA_sym.subs(q_sym,
                                                sp.Rational(str(Q0_FLOAT))))) < 1e-3:
        d = -HA_sym / 2
    else:
        d = sp.nsimplify(d_f)
    return SymbolicHeckeElement({(g,): c, (): d})


def build_d_nf():
    word = atom_braid_word_3A(1, 1)
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since = 0
    for (c_f, d_f, g) in word:
        elem = elem * _factor_from(c_f, d_f, g)
        since += 1
        if since >= 4:
            elem, _ = div.reduce(elem)
            since = 0
    if since > 0:
        elem, _ = div.reduce(elem)
    return elem


def r_matrix_N(N: int, q: complex) -> np.ndarray:
    """R-matrix for V ⊗ V at given q (complex), where V = V_{N-1} is
    the N-dimensional vector space.

    **Note: the construction below is the Hecke generalization that
    is exact for N = 2 (standard Jones polynomial).  For N > 2 the
    colored-Jones R-matrix of U_q(sl_2) on V_{N-1} is NOT a simple
    element-by-element generalization — the braid group action does
    NOT factor through H_n(q).  Results from this module for N > 2
    are DIAGNOSTIC ONLY and should not be interpreted as correct
    colored-Jones values.  The N=2 results are valid.**

    Returns an (N·N) × (N·N) complex matrix.
    """
    dim = N * N
    R = np.zeros((dim, dim), dtype=complex)
    def idx(j, k): return j * N + k
    # Hecke relation R² = (q − q⁻¹)·R + I requires the (q − q⁻¹)
    # diagonal entry for EVERY i < j pair, not just adjacent ones.
    for j in range(N):
        for k in range(N):
            if j == k:
                R[idx(j, k), idx(j, k)] = q
            elif j < k:
                R[idx(j, k), idx(k, j)] = 1.0
                R[idx(j, k), idx(j, k)] = q - 1.0 / q
            else:
                R[idx(j, k), idx(k, j)] = 1.0
    return R


def r_at_position(R: np.ndarray, N: int, pos: int, n: int) -> np.ndarray:
    # Build identities directly via np.eye on the needed dimensions,
    # avoiding repeated np.kron calls that rebuild I ⊗ I ⊗ ...
    left = np.eye(N ** pos, dtype=complex) if pos > 0 else None
    right_dim = n - pos - 2
    right = np.eye(N ** right_dim, dtype=complex) if right_dim > 0 else None
    if left is None and right is None:
        return R
    if left is None:
        return np.kron(R, right)
    if right is None:
        return np.kron(left, R)
    return np.kron(np.kron(left, R), right)


def braid_matrix(word, n, N, q, *, r_position_cache=None):
    """Build the braid operator on V_{N-1}^⊗n.

    `r_position_cache`: optional dict {gen_index: matrix} precomputed
    once for fixed (n, N, q) and reused across words.  If None, the
    cache is built locally (OK for one-off calls but inefficient in
    a loop).
    """
    dim = N ** n
    M = np.eye(dim, dtype=complex)
    if r_position_cache is None:
        R = r_matrix_N(N, q)
        r_position_cache = {}
        for g in word:
            if g not in r_position_cache:
                r_position_cache[g] = r_at_position(R, N, g, n)
    for g in word:
        if g not in r_position_cache:
            R = r_matrix_N(N, q)
            r_position_cache[g] = r_at_position(R, N, g, n)
        M = M @ r_position_cache[g]
    return M


def build_r_position_cache(n, N, q):
    """Precompute r_at_position for all generator indices 0..n-2.

    Use once outside a loop over words to avoid recomputing R and
    embedding it at each position on every braid_matrix call.
    """
    R = r_matrix_N(N, q)
    return {g: r_at_position(R, N, g, n) for g in range(n - 1)}


def quantum_trace_K(N: int, n: int, q: complex) -> np.ndarray:
    """Diagonal 'ribbon/K' factor K^⊗n on V_{N-1}^⊗n.

    K = diag(q^{N-1}, q^{N-3}, ..., q^{-(N-1)}) acting on V_{N-1}.
    qtr(M) = tr(M · K^⊗n).
    """
    # Build diag on single V_{N-1}
    k_single = np.array([q ** (N - 1 - 2 * j) for j in range(N)],
                          dtype=complex)
    # kron-product n times
    diag = k_single.copy()
    for _ in range(n - 1):
        diag = np.kron(diag, k_single)
    return diag  # shape (N^n,) — multiply diag * M elementwise on diagonal


def j_N_qtr(basis_word, n_strands, N, q, *, r_position_cache=None):
    """Quantum Jones J_N(closure of basis_word) at q via quantum trace.

    If calling in a loop over many basis words at fixed (n_strands, N, q),
    build an r_position_cache with build_r_position_cache once and pass
    it in — this avoids rebuilding the R-matrix and position embeddings
    for every word.
    """
    dim = N ** n_strands
    if len(basis_word) == 0:
        M = np.eye(dim, dtype=complex)
    else:
        M = braid_matrix(basis_word, n_strands, N, q,
                          r_position_cache=r_position_cache)
    K_diag = quantum_trace_K(N, n_strands, q)
    qtr = np.sum(K_diag * np.diag(M))
    # N_q = [N]_q = (q^N - q^{-N})/(q - q^{-1})
    # Edge cases (L'Hôpital):
    #   q = 1  → N.
    #   q = -1 → N · (-1)^(N-1):  +N for N odd, −N for N even.
    q_c = complex(q)
    if abs(q_c - 1.0) < 1e-15:
        nq = complex(N)
    elif abs(q_c + 1.0) < 1e-15:
        nq = complex(N * ((-1) ** (N - 1)))
    else:
        nq = (q_c ** N - q_c ** (-N)) / (q_c - 1 / q_c)
    # J_N(β̂) normalization: qtr / [N]_q^{n_components - 1}
    # For a braid on n strands closed to a link with c components,
    # the normalization involves [N]_q^c / [N]_q = [N]_q^{c-1} for
    # the "unnormalized" Kauffman.  We use J_N(unknot) = 1
    # convention: J_N = qtr / [N]_q^{n_strands}  (gives unknot-per-
    # strand = 1 consistency).
    if abs(nq) < 1e-300:
        return complex("nan")
    return qtr / (nq ** n_strands)


def build_eps_caches(n, N, eps_list):
    """Precompute r-position caches for each (q = root · exp(iε))
    value.  Call once outside a loop over NF basis words to avoid
    rebuilding these caches (N^n matrices) for every word.

    Returns {eps: r_position_cache} where r_position_cache is the
    dict produced by build_r_position_cache for q = root · exp(iε).
    """
    root = complex(mpmath.exp(2j * mpmath.pi / N))
    return {eps: build_r_position_cache(n, N, root * cmath.exp(1j * eps))
            for eps in eps_list}


def j_N_at_root_via_limit(basis_word, n, N,
                              eps_list=(1e-4, 1e-5, 1e-6, 1e-7),
                              eps_caches=None) -> complex:
    """Evaluate J_N at q = e^{2πi/N} via limit from q = root · e^{iε}.

    Returns Richardson-extrapolated value as ε → 0.

    Richardson scheme: if f(ε) = f(0) + c₁·ε + c₂·ε² + ...  and
    successive ε_k halve (or shrink by factor r), the k-th Richardson
    estimate is
        R_k = (r · f(ε_k) − f(ε_{k-1})) / (r − 1)
    This cancels the leading ε term, leaving O(ε²) error.  Iterated on
    the Richardson table removes higher powers.

    `eps_caches`: optional {eps: r_position_cache} produced by
    build_eps_caches.  Pass this in when calling j_N_at_root_via_limit
    in a loop over NF basis words at fixed (n, N, eps_list) — without
    it each call rebuilds N^n-dim matrices for every ε on every word.
    """
    # Convergence threshold for the last two Richardson inputs.
    # 1% is permissive but consistent with the colored-Jones
    # evaluation being DIAGNOSTIC only (the N>2 R-matrix is not the
    # true colored-Jones R-matrix anyway, see r_matrix_N docstring).
    # For 1-ppb precision work on the PRODUCTION mass formula, this
    # tolerance would need to be tightened to 1e-9 and the R-matrix
    # rewritten.  Left at 1e-2 for the diagnostic regime.
    DIVERGENCE_REL_TOL = 0.01
    # Use mpmath for the root-of-unity construction so it matches
    # the script's configured precision, then cast to complex for
    # downstream numpy usage.
    root = complex(mpmath.exp(2j * mpmath.pi / N))
    vals = []
    for eps in eps_list:
        q_eps = root * cmath.exp(1j * eps)
        if eps_caches is not None and eps in eps_caches:
            r_cache = eps_caches[eps]
        else:
            r_cache = build_r_position_cache(n, N, q_eps)
        v = j_N_qtr(basis_word, n, N, q_eps, r_position_cache=r_cache)
        vals.append(v)
    if any(cmath.isnan(v) for v in vals):
        return complex("nan")
    # Standard relative-error convergence check.
    diff = abs(vals[-1] - vals[-2])
    denom = abs(vals[-1]) if abs(vals[-1]) > 1e-9 else 1.0
    if diff / denom > DIVERGENCE_REL_TOL:
        return complex("nan")   # divergent

    # Richardson table: assume ε_k = eps_list[k] decreases geometrically.
    # Build one column of Richardson estimates for each pair.
    # Single-step Richardson at pair (k-1, k):
    #   R = (r · vals[k] − vals[k-1]) / (r − 1), r = eps_{k-1} / eps_k
    # Iterate: at the m-th column (m = 1, 2, ...), the pair-level
    # Richardson estimate cancels the O(ε^m) error term.  The correct
    # formula therefore uses r^m (not r) in the numerator weight:
    #   R_m = (r^m · vals[k] − vals[k-1]) / (r^m − 1)
    col = list(vals)
    m = 1
    while len(col) >= 2:
        next_col = []
        for k in range(1, len(col)):
            i_this = len(vals) - len(col) + k
            i_prev = i_this - 1
            r = eps_list[i_prev] / eps_list[i_this]
            if abs(r - 1) < 1e-15:
                next_col.append(col[k])
            else:
                r_m = r ** m
                next_col.append((r_m * col[k] - col[k - 1]) / (r_m - 1))
        col = next_col
        m += 1
    return col[0] if col else vals[-1]


def main() -> int:
    print("=" * 100)
    print("D COLORED-JONES with QUANTUM TRACE + ROOT-OF-UNITY LIMIT")
    print(f"  Target: B_AME(D)/m_e = {TARGET_VOL:.10f}")
    print("=" * 100)

    print("\n  Building D's NF…")
    nf = build_d_nf()
    print(f"  {nf.n_terms()} basis terms")

    # Compute J_N for N = 2, 3, 4, 5.  At N=5, dim = 5^6 = 15625,
    # each matrix mult is ~4e12 ops; not feasible in dense.
    results = {}
    for N in [2, 3, 4]:
        dim = N ** N_STRANDS
        print(f"\n  --- N = {N}  (dim V_{{{N-1}}}^⊗6 = {dim}) ---")

        t0 = time.time()
        J_at_q0 = 0j
        # Precompute the R-matrix position-embeddings for this (N, q₀)
        # pair once; reuse for every NF basis word.
        r_cache_q0 = build_r_position_cache(N_STRANDS, N, complex(Q0_FLOAT))
        for (basis, coeff) in nf.terms.items():
            coeff_fn = sp.lambdify(q_sym, coeff, modules=["numpy", "cmath"])
            c_val = complex(coeff_fn(complex(Q0_FLOAT)))
            j_val = j_N_qtr(basis, N_STRANDS, N, complex(Q0_FLOAT),
                              r_position_cache=r_cache_q0)
            if not (np.isnan(j_val.real) or np.isnan(j_val.imag)):
                J_at_q0 += c_val * j_val
        dt_q0 = time.time() - t0
        print(f"    J_{N}(β_D, q₀)      = {J_at_q0}")
        print(f"    |J_{N}(β_D, q₀)|     = {abs(J_at_q0):.10f}")
        print(f"    ({dt_q0:.1f}s)")

        # Root via limit
        t0 = time.time()
        J_at_root = 0j
        root = cmath.exp(2j * cmath.pi / N)
        fail = 0
        # Precompute r-position caches once per ε for every q_eps; reused
        # across all NF basis words to avoid N^n-dim cache rebuilds.
        eps_list = (1e-4, 1e-5, 1e-6, 1e-7)
        eps_caches = build_eps_caches(N_STRANDS, N, eps_list)
        for (basis, coeff) in nf.terms.items():
            coeff_fn = sp.lambdify(q_sym, coeff, modules=["numpy", "cmath"])
            # Also evaluate coeff at root (no limit needed — coeff is
            # a polynomial)
            c_val_root = complex(coeff_fn(root))
            j_val = j_N_at_root_via_limit(basis, N_STRANDS, N,
                                            eps_list=eps_list,
                                            eps_caches=eps_caches)
            if np.isnan(j_val.real):
                fail += 1
                continue
            J_at_root += c_val_root * j_val
        dt_root = time.time() - t0
        print(f"    J_{N}(β_D, e^(2πi/{N})) = {J_at_root}")
        print(f"    |J_{N}(β_D, e^(2πi/{N}))| = {abs(J_at_root):.10f}")
        print(f"    ({fail} basis-word limits failed, {dt_root:.1f}s)")

        if abs(J_at_root) > 1e-300:
            vol_N = 2 * cmath.pi.real * cmath.log(abs(J_at_root)).real / N
        else:
            vol_N = float("nan")
        print(f"    Kashaev-style: 2π log|J_{N}|/{N} = {vol_N}")
        print(f"    vs target {TARGET_VOL}: "
              f"err = {(vol_N - TARGET_VOL)/TARGET_VOL*100:+.4f}% "
              f"= {(vol_N - TARGET_VOL)/TARGET_VOL*1e9:+.3e} ppb")

        results[N] = {
            "J_q0": str(J_at_q0), "abs_J_q0": abs(J_at_q0),
            "J_root": str(J_at_root), "abs_J_root": abs(J_at_root),
            "vol_kashaev": vol_N,
            "dim": dim,
        }

    out = Path(__file__).parent / "d-colored-jones-qtr.witness.json"
    witness = {
        "computation": "d-colored-jones-qtr",
        "description": (
            "D's colored-Jones polynomial via quantum trace "
            "qtr(M) = tr(M · K^⊗n) with K = diag(q^{N-1}, q^{N-3}, ..., "
            "q^{-(N-1)}).  At q = e^{2πi/N}, uses ε-limit to bypass "
            "the [N]_q = 0 singularity.  Kashaev asymptotic "
            "2π log|J_N|/N at N = 2, 3, 4 to test volume-conjecture "
            "convergence to B_AME(D)/m_e."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "target_vol": TARGET_VOL,
        "B_AME_D": B_D_AME,
        "n_nf_terms": nf.n_terms(),
        "results_by_N": {str(k): v for k, v in results.items()},
    }
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
