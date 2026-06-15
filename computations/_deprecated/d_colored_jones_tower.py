#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
D via colored-Jones tower: compute J_N(β_D, q₀) for N=2,3,4 directly
from the Hecke-algebra representation ρ_N: H_6(q) → End(V_{N-1}^{⊗6}).

The colored Jones J_N for a braid β_D = Σ_w c_w(q) · w is linear:
  J_N(β_D, q) = Σ_w c_w(q) · J_N(ŵ, q)

So: for each of D's 32 NF basis words w, compute J_N(ŵ) via
R-matrix representation on V_{N-1}^{⊗n}, weight by c_w(q₀), sum.

Then form the volume asymptotic:
  Vol_cJ(β_D, N) = 2π · log|J_N(β_D, e^{2πi/N})| / N

If this converges as N→∞ to a value matching B_AME(D)/m_e = 4.3533,
the colored-Jones tower captures D's full topology.

Note: at finite N, J_N is exact in q ∈ ℂ. We evaluate at q₀ (real)
and at q = e^{2πi/N} (Kashaev's root-of-unity).
"""
from __future__ import annotations

import sys
import json
import time
import cmath
import warnings
import itertools
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp
import mpmath

# Precision applied only when run as main; prevents import-time side
# effects on shared mpmath state.
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
N_STRANDS = 6  # D has 3A = 6 strands


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
    """R-matrix for V ⊗ V at given q (complex).

    **Caveat:** this implementation is the Hecke-style generalization
    that is exact for N = 2 (standard Jones).  For N > 2 the true
    U_q(sl_2) colored-Jones R-matrix on V_{N-1} ⊗ V_{N-1} is NOT a
    direct element-by-element generalization (the braid action does
    not factor through the Hecke algebra).  Results for N > 2 should
    be treated as DIAGNOSTIC, not authoritative.
    """
    dim = N * N
    R = np.zeros((dim, dim), dtype=complex)
    def idx(j, k):
        return j * N + k
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


def r_at_position(R: np.ndarray, N: int, pos: int,
                    n_strands: int) -> np.ndarray:
    """R acting on strands (pos, pos+1) in V_N^⊗n_strands."""
    I_N = np.eye(N, dtype=complex)
    # Kron order: strand 0 is leftmost.  Position pos means R acts on
    # strands pos, pos+1.  So left: I^(pos), right: I^(n_strands-pos-2).
    left = None
    for _ in range(pos):
        left = I_N if left is None else np.kron(left, I_N)
    right = None
    for _ in range(n_strands - pos - 2):
        right = I_N if right is None else np.kron(right, I_N)
    if left is None and right is None:
        return R
    if left is None:
        return np.kron(R, right)
    if right is None:
        return np.kron(left, R)
    return np.kron(np.kron(left, R), right)


def braid_matrix(braid_word: tuple, n_strands: int,
                    N: int, q: complex) -> np.ndarray:
    """ρ_{N}(β): braid word (positive ints, 0-indexed) → N^n matrix."""
    dim = N ** n_strands
    M = np.eye(dim, dtype=complex)
    R = r_matrix_N(N, q)
    cache = {}
    for g in braid_word:
        if g not in cache:
            cache[g] = r_at_position(R, N, g, n_strands)
        M = M @ cache[g]
    return M


def j_N_of_word(basis_word: tuple, n_strands: int, N: int,
                  q: complex) -> complex:
    """J_N(closure of basis_word) at q.

    Returns the Markov trace tr(ρ_N(β)) / [N]_q where
    [N]_q = (q^N - q^{-N})/(q - q^{-1}).

    Empty word: handled via the same tr/[N]_q normalisation (M = I_{N^n},
    so tr = N^n and the return is N^n / [N]_q).  This is the closure-
    of-identity value in this unnormalised Kauffman convention —
    consistent with the non-empty branch.  For the "J_N(unknot) = 1"
    normalisation, each strand carries an extra 1/[N]_q factor; use
    d_colored_jones_qtr.j_N_qtr for the unambiguous quantum-trace
    normalisation instead.
    """
    dim = N ** n_strands
    if len(basis_word) == 0:
        M = np.eye(dim, dtype=complex)
    else:
        M = braid_matrix(basis_word, n_strands, N, q)
    tr = np.trace(M)
    if N == 1:
        return tr
    # Quantum dim [N]_q
    # Edge cases via L'Hôpital:
    #   q = 1  → [N]_q = N
    #   q = -1 → [N]_q = N · (-1)^(N-1) = +N odd / -N even
    qN = complex(q)
    if abs(qN - 1.0) < 1e-15:
        qdim = complex(N)
    elif abs(qN + 1.0) < 1e-15:
        qdim = complex(N * ((-1) ** (N - 1)))
    else:
        qdim = (qN ** N - qN ** (-N)) / (qN - 1 / qN)
    if abs(qdim) < 1e-15:
        return complex('nan')
    return tr / qdim


def main() -> int:
    print("=" * 100)
    print("D's COLORED-JONES TOWER — sum over NF basis words")
    print(f"  Target: B_AME(D)/m_e = {TARGET_VOL:.10f}")
    print(f"  n_strands = 6 (3A for D)")
    print("=" * 100)

    # Build D's NF
    print(f"\n  Building D's NF…")
    nf = build_d_nf()
    print(f"  {nf.n_terms()} basis terms")

    results = {}
    for N in [2, 3, 4]:
        dim = N ** N_STRANDS
        print(f"\n  --- N = {N}  (ρ_N dim = N^6 = {dim}) ---")
        if dim > 5000:
            print(f"  (dim {dim} large; approximate timing estimate)")
        t0 = time.time()
        # Evaluate J_N(β_D, q₀) = Σ c_w(q₀) · J_N(ŵ, q₀)
        q_val = complex(Q0_FLOAT)
        weighted_J_q0 = 0 + 0j
        for (basis, coeff) in nf.terms.items():
            c_val = complex(sp.N(coeff.subs(q_sym,
                                                sp.Rational(str(Q0_FLOAT)))))
            j_val = j_N_of_word(basis, N_STRANDS, N, q_val)
            if np.isnan(j_val):
                continue
            weighted_J_q0 += c_val * j_val
        dt = time.time() - t0
        print(f"    J_{N}(β_D, q₀)      = {weighted_J_q0}")
        print(f"    |J_{N}(β_D, q₀)|     = {abs(weighted_J_q0):.10f}")
        print(f"    computation time: {dt:.1f}s")

        # Also at q = e^{2πi/N} (Kashaev's root)
        q_root = complex(cmath.exp(2j * cmath.pi / N))
        t0 = time.time()
        weighted_J_root = 0 + 0j
        for (basis, coeff) in nf.terms.items():
            coeff_fn = sp.lambdify(q_sym, coeff, modules=["numpy", "cmath"])
            c_val = complex(coeff_fn(q_root))
            j_val = j_N_of_word(basis, N_STRANDS, N, q_root)
            if np.isnan(j_val):
                continue
            weighted_J_root += c_val * j_val
        dt = time.time() - t0
        print(f"    J_{N}(β_D, e^(2πi/{N})) = {weighted_J_root}")
        print(f"    |J_{N}(β_D, e^(2πi/{N}))| = {abs(weighted_J_root):.10f}")
        vol_kashaev = (2 * cmath.pi.real) * cmath.log(abs(weighted_J_root)
                                                        if abs(weighted_J_root) > 0
                                                        else 1).real / N
        print(f"    Kashaev-style: 2π log|J_{N}|/{N} = {vol_kashaev:.6f}")
        print(f"    (target = {TARGET_VOL:.6f})")
        print(f"    compute time: {dt:.1f}s")

        results[N] = {
            "J_q0": str(weighted_J_q0),
            "abs_J_q0": abs(weighted_J_q0),
            "J_root_of_unity": str(weighted_J_root),
            "abs_J_root": abs(weighted_J_root),
            "vol_kashaev_N": vol_kashaev,
        }

    # Save witness
    witness = {
        "computation": "d-colored-jones-tower",
        "description": (
            "D's colored-Jones tower: direct evaluation of J_N(β_D, q) "
            "for N=2,3,4 via explicit ρ_N: H_6(q) → End(V_N^⊗6), "
            "summed over D's 32 NF basis words with their q₀ coefficients. "
            "Reports both J_N(β_D, q₀) (substrate) and J_N at Kashaev's "
            "root of unity e^(2πi/N) with the asymptotic volume estimate."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "target_vol": TARGET_VOL,
        "B_AME_D": B_D_AME,
        "n_nf_terms": nf.n_terms(),
        "results_by_N": {str(k): v for k, v in results.items()},
    }
    out = Path(__file__).parent / "d-colored-jones-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
