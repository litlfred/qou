#!/usr/bin/env python3
"""
Refine k=6 [3,2,1] scaling using exact character polynomial data.

Current first-order formula:
    m_{321}(Z,N) ≈ DELTA_W2 · ZN / A^{4/3}        [hecke_core.py:1040]

But exact character data (DERIVATION-STATUS.md §1) shows:
  - m_{321} ≠ 0 for N=Z nuclei (⁴He, ¹²C, ...), so the formula misses
    an N=Z-symmetric contribution
  - The sign flips between ⁸Be (-31 keV) and ¹²C (+19.5 keV),
    indicating non-monotonic A-dependence

This script:
  1. Computes exact m_{321}(Z,N) for A=2..30 (where numerics are stable)
  2. Fits multi-parameter refined scalings
  3. Reports best fit and residuals

The exact character uses the inter-nucleon crossing chain
    Π_{i<j} (σ_g + d_ij · I),  g = (i+j) mod 5
with d_ij ∈ {0, -h, -h/2}, as in symbolic_k6_characters.py.
"""
import math
import sys
from pathlib import Path
from functools import lru_cache

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from q_parameter import Q as q0, HA
from experimental_constants import M_E_MEV
from level_k_binding import standard_young_tableaux, seminormal_matrix
from hoefsmit_witness import load_witness


SHAPE_321 = (3, 2, 1)
N_GENS = 5


def _nuclear_ordering(Z, N):
    ordering = []
    pc = nc = 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append(1); pc += 1
        else:
            ordering.append(0); nc += 1
    return ordering


@lru_cache(maxsize=4096)
def m_321_exact(Z, N):
    """Exact Markov contribution m_{321}(Z,N) = w·χ/dim·m_e in MeV."""
    A = Z + N
    if A < 2:
        return 0.0
    dim = 16
    w = 0.35863564  # from witness
    sigmas = [seminormal_matrix(SHAPE_321, g) for g in range(N_GENS)]
    I = np.eye(dim)
    M = np.eye(dim)
    ordering = _nuclear_ordering(Z, N)
    for i in range(A - 1):
        for j in range(i + 1, A):
            ti, tj = ordering[i], ordering[j]
            if ti == 1 and tj == 1: shift = 0.0
            elif ti == 0 and tj == 0: shift = -HA
            else: shift = -HA / 2
            g = (i + j) % N_GENS
            M = M @ (sigmas[g] + shift * I)
            # Detect numerical overflow early
            if not np.all(np.isfinite(M)):
                return float('nan')
    chi = float(np.trace(M))
    return w * chi / dim * M_E_MEV


# ── Build training set: A=2..30 stable nuclei ─────────────────
# AME2020-like set filtered to A≤30 where characters are numerically stable

NUCLEI = [
    (1, 0, 'H'),   (1, 1, 'D'),    (2, 2, '⁴He'),  (3, 4, '⁷Li'),
    (4, 5, '⁹Be'), (5, 6, '¹¹B'),  (6, 6, '¹²C'),  (7, 7, '¹⁴N'),
    (8, 8, '¹⁶O'), (9, 10, '¹⁹F'), (10, 10, '²⁰Ne'),
    (11, 12, '²³Na'), (12, 12, '²⁴Mg'), (13, 14, '²⁷Al'), (14, 14, '²⁸Si'),
    # N=Z mirrors
    (1, 2, '³H'),  (2, 1, '³He'), (3, 3, '⁶Li'), (4, 4, '⁸Be'),
    (5, 5, '¹⁰B'), (6, 7, '¹³C'), (7, 6, '¹³N'),
    # A≥15, non-N=Z
    (20, 20, '⁴⁰Ca'),
]


def compute_training_set():
    """Returns dict name → (Z, N, A, m_321) for STABLE nuclei only.

    Filter A≤16 where the 16-dim matrix product stays numerically
    well-conditioned.  Larger A has up to A(A-1)/2 crossings; the
    operator c·σ + d·I has eigenvalues up to ~1.1 in magnitude,
    so the product can accumulate 1.1^{A(A-1)/2} numerical error.
    """
    data = {}
    for Z, N, name in NUCLEI:
        A = Z + N
        if A > 16:
            continue   # numerical stability limit
        m = m_321_exact(Z, N)
        if math.isnan(m):
            continue
        data[name] = (Z, N, A, m)
    return data


# ── Multi-parameter fits ──────────────────────────────────────

def fit_model(name, data, kernels, kernel_names):
    """Fit m_{321} = Σ cᵢ · kernelᵢ(Z, N, A)."""
    xs = []
    ys = []
    for key, (Z, N, A, m) in data.items():
        if A < 2:
            continue
        row = [k(Z, N, A) for k in kernels]
        xs.append(row)
        ys.append(m)
    X = np.array(xs)
    y = np.array(ys)
    coef, res, rank, sv = np.linalg.lstsq(X, y, rcond=None)
    fit = X @ coef
    residuals = y - fit
    rms = math.sqrt(float(np.mean(residuals**2)))
    maxabs = float(np.max(np.abs(residuals)))
    r2 = 1.0 - float(np.sum(residuals**2) / np.sum((y - np.mean(y))**2))
    print(f"\n[Model: {name}]")
    for k_name, c in zip(kernel_names, coef):
        print(f"    {c*1e3:>+10.4f} keV × {k_name}")
    print(f"    RMS residual: {rms*1e3:.3f} keV   max: {maxabs*1e3:.3f} keV   R² = {r2:.4f}")
    return coef, residuals, rms


def main():
    print(f"{'='*72}")
    print("EXACT k=6 [3,2,1] CHARACTER DATA (stable nuclei only)")
    print(f"{'='*72}")
    print(f"q₀ = {q0:.8f}, h = {HA:.6f}, m_e = {M_E_MEV:.6f} MeV\n")

    data = compute_training_set()
    print(f"{'nucleus':>8s} {'Z':>3s} {'N':>3s} {'A':>3s} {'m_{321} [keV]':>15s}")
    print("-" * 44)
    for key, (Z, N, A, m) in data.items():
        print(f"{key:>8s} {Z:>3d} {N:>3d} {A:>3d} {m*1e3:>+15.4f}")

    print(f"\n{len(data)} nuclei, "
          f"range [{min(m for _,_,_,m in data.values())*1e3:.2f}, "
          f"{max(m for _,_,_,m in data.values())*1e3:.2f}] keV\n")

    # ── First-order baselines ────────────────────────────────
    print(f"{'='*72}")
    print("BASELINE MODELS")
    print(f"{'='*72}")

    fit_model("current: ZN/A^{4/3}", data,
              [lambda Z,N,A: Z*N / A**(4/3)],
              ["Z·N/A^{4/3}"])

    fit_model("alt: (Z-N)(A-1)/A^{4/3}", data,
              [lambda Z,N,A: (Z-N)*(A-1) / A**(4/3)],
              ["(Z-N)(A-1)/A^{4/3}"])

    # ── Refined multi-term models ────────────────────────────
    print(f"\n{'='*72}")
    print("REFINED MODELS (multi-term)")
    print(f"{'='*72}")

    # Model R1: splits pn and nn contributions
    fit_model("R1: ZN + Z(Z-1) + N(N-1) over A^{4/3}", data,
              [lambda Z,N,A: Z*N / A**(4/3),
               lambda Z,N,A: Z*(Z-1) / A**(4/3),
               lambda Z,N,A: N*(N-1) / A**(4/3)],
              ["ZN/A^{4/3}", "Z(Z-1)/A^{4/3}", "N(N-1)/A^{4/3}"])

    # Model R2: adds A-dependent cross term
    fit_model("R2: ZN, ZN(A-4), (N-Z)² all /A^{4/3}", data,
              [lambda Z,N,A: Z*N / A**(4/3),
               lambda Z,N,A: Z*N*(A-4) / A**(7/3),
               lambda Z,N,A: (N-Z)**2 / (4*A**(4/3))],
              ["ZN/A^{4/3}", "ZN(A-4)/A^{7/3}", "(N-Z)²/(4A^{4/3})"])

    # Model R3: generic low-order polynomial basis
    fit_model("R3: polynomial basis {Z, N, ZN, Z², N², A}/A^{4/3}", data,
              [lambda Z,N,A: Z / A**(4/3),
               lambda Z,N,A: N / A**(4/3),
               lambda Z,N,A: Z*N / A**(4/3),
               lambda Z,N,A: Z*Z / A**(4/3),
               lambda Z,N,A: N*N / A**(4/3),
               lambda Z,N,A: A / A**(4/3)],
              ["Z/A^{4/3}", "N/A^{4/3}", "ZN/A^{4/3}",
               "Z²/A^{4/3}", "N²/A^{4/3}", "A^{-1/3}"])

    # Model R4: braid-length-based (A(A-1)/2 crossings)
    fit_model("R4: crossings n_c=A(A-1)/2, with pp/nn/pn split",
              data,
              [lambda Z,N,A: Z*(Z-1)/2 / A**(4/3),
               lambda Z,N,A: N*(N-1)/2 / A**(4/3),
               lambda Z,N,A: Z*N / A**(4/3)],
              ["n_pp/A^{4/3}", "n_nn/A^{4/3}", "n_pn/A^{4/3}"])

    # ── Report best model ────────────────────────────────────
    print(f"\n{'='*72}")
    print("CONCLUSION")
    print(f"{'='*72}\n")
    print("Best multi-term fit determines the refined k=6 [3,2,1] scaling.")
    print("If R4 (pp/nn/pn crossings split) wins, the refined formula is:")
    print("  m_{321} = C_pp · Z(Z-1)/2·A^{-4/3} + C_nn · N(N-1)/2·A^{-4/3}")
    print("          + C_pn · Z·N·A^{-4/3}")
    print("\nThis replaces DELTA_W2 × Z·N / A^{4/3} in hecke_core.py:1040\n")


if __name__ == "__main__":
    main()
