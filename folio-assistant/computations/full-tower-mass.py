#!/usr/bin/env python3
"""
Full 2×2 brane tower mass computation for atoms.

For each atom (Z, N):
1. Build ground-state ordering (nucleons + electrons)
2. Per generator i: accumulate the 2×2 standard-rep matrix M_i
   through the Garside staircase (including gluon crossings)
3. Per generator: compute the brane tower product
   Π_{k=1}^∞ det(I - q⁻ᵏ M_i)⁻¹
4. Also track forward AND dual towers
5. Combine all generators for the total atom mass

The binding = Σ_i ln|Z_tower(M_i)| where Z_tower is the
partition function per generator.
"""

import numpy as np
import math
from q_parameter import Q as q0, Q_INV as qi0, HA as h, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

z_markov = 1.0 / (q0**0.5 + qi0**0.5)

# 2×2 standard rep matrices for H₃(q)
# σ₀: diagonal in seminormal basis
sigma0 = np.array([[q0, 0], [0, -qi0]])
# σ₁: off-diagonal
dv = h / (qi0**2 - q0**2)
ov = np.sqrt(1 - dv**2)
sigma1 = np.array([[dv, ov], [ov, -dv]])
# Inverses
sigma0_inv = sigma0 - h * np.eye(2)
sigma1_inv = sigma1 - h * np.eye(2)
# Mixed
sigma0_mix = 0.5 * (sigma0 + sigma0_inv)
sigma1_mix = 0.5 * (sigma1 + sigma1_inv)
# Identity
I2 = np.eye(2)


def crossing_matrix(t1, t2, gen=0):
    """2×2 standard-rep matrix for typed crossing.
    gen=0 → σ₀ basis, gen=1 → σ₁ basis (for inter-nucleon crossings
    gen is always 0 since we work per-generator)."""
    pair = tuple(sorted([t1, t2]))
    if pair == ('p', 'p'): return sigma0         # pp: σ
    elif pair == ('n', 'n'): return sigma0_inv    # nn: σ⁻¹
    elif pair == ('n', 'p'): return sigma0_mix    # pn: ½(σ+σ⁻¹)
    elif pair == ('e', 'p'): return sigma0_inv    # pe: σ⁻¹ (EM)
    elif pair == ('e', 'n'): return I2            # ne: identity
    elif pair == ('e', 'e'): return sigma0        # ee: σ
    return I2


def crossing_matrix_dual(t1, t2):
    """Dual (antipode) of crossing matrix. S(σ)=σ⁻¹, S(σ⁻¹)=σ."""
    pair = tuple(sorted([t1, t2]))
    if pair == ('p', 'p'): return sigma0_inv
    elif pair == ('n', 'n'): return sigma0
    elif pair == ('n', 'p'): return sigma0_mix  # S(½(σ+σ⁻¹)) = same
    elif pair == ('e', 'p'): return sigma0
    elif pair == ('e', 'n'): return I2
    elif pair == ('e', 'e'): return sigma0_inv
    return I2


def gluon_matrices_forward(particle_type):
    """Forward gluon crossing matrices for a nucleon."""
    if particle_type == 'p':
        return [sigma0, sigma0]  # 2×σ₀
    elif particle_type == 'n':
        return [sigma0, sigma0, sigma0, sigma0]  # L₊L₋ effective
    return []


def gluon_matrices_dual(particle_type):
    """Dual gluon crossing matrices."""
    if particle_type == 'p':
        return [sigma0_inv, sigma0_inv]
    elif particle_type == 'n':
        return [sigma0_inv, sigma0_inv, sigma0_inv, sigma0_inv]
    return []


def ground_state_ordering(Z, N):
    """Alternating pn ordering."""
    ordering = []
    pi, ni = 0, 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            ordering.append('p')
            pi += 1
        else:
            ordering.append('n')
            ni += 1
    return ordering


def insert_electrons(nuc_ordering, Z):
    """Insert electrons before protons (ep pairs)."""
    full = []
    for t in nuc_ordering:
        if t == 'p':
            full.append('e')
        full.append(t)
    return full


def brane_tower_det(M, max_k=500):
    """Compute Π_{k=1}^∞ det(I - q⁻ᵏ M)⁻¹.
    Returns ln of the product (for numerical stability)."""
    eigs = np.linalg.eigvals(M)
    ln_prod = 0.0
    for k in range(1, max_k + 1):
        qk = qi0 ** k
        det = 1.0
        for lam in eigs:
            det *= abs(1.0 - qk * lam)
        if det < 1e-300:
            return float('inf')
        ln_prod -= math.log(det)
        if qk * max(abs(eigs)) < 1e-15:
            break
    return ln_prod


def compute_atom_tower(Z, N):
    """Full 2×2 brane tower for atom (Z, N).

    Returns per-generator tower data and total binding.
    """
    nuc_ordering = ground_state_ordering(Z, N)
    full_ordering = insert_electrons(nuc_ordering, Z)
    n_strands = len(full_ordering)
    n_gens = n_strands - 1

    gen_data = []

    for i in range(n_gens):
        # Accumulate 2×2 matrix at generator i
        M_fwd = np.eye(2)
        M_dual = np.eye(2)

        # Gluon crossings for particle at strand i
        for gm in gluon_matrices_forward(full_ordering[i]):
            M_fwd = M_fwd @ gm
        for gm in gluon_matrices_dual(full_ordering[i]):
            M_dual = M_dual @ gm

        # Garside staircase: generator i interacts with all j > i
        for j in range(i + 1, n_strands):
            M_fwd = M_fwd @ crossing_matrix(full_ordering[i], full_ordering[j])
            M_dual = M_dual @ crossing_matrix_dual(full_ordering[i], full_ordering[j])

        # Eigenvalues
        eigs_fwd = np.linalg.eigvals(M_fwd)
        eigs_dual = np.linalg.eigvals(M_dual)

        # Brane tower: Π_k det(I - q⁻ᵏ M)⁻¹
        ln_Z_fwd = brane_tower_det(M_fwd)
        ln_Z_dual = brane_tower_det(M_dual)

        gen_data.append({
            'gen': i,
            'pair': full_ordering[i] + full_ordering[i+1],
            'M_fwd': M_fwd,
            'M_dual': M_dual,
            'eigs_fwd': eigs_fwd,
            'eigs_dual': eigs_dual,
            'ln_Z_fwd': ln_Z_fwd,
            'ln_Z_dual': ln_Z_dual,
        })

    return full_ordering, gen_data


# ══════════════════════════════════════════════════════════════
# Run for Z=1 to Z=20
# ══════════════════════════════════════════════════════════════

isotopes = [
    (1, 0, "H", 938.783), (1, 1, "D", 1876.124),
    (2, 2, "He", 3728.401), (3, 4, "Li", 6535.367),
    (4, 5, "Be", 8394.794), (5, 6, "B", 10255.103),
    (6, 6, "C", 11177.930), (7, 7, "N", 13043.781),
    (8, 8, "O", 14899.169), (9, 10, "F", 17696.901),
    (10, 10, "Ne", 18622.835), (11, 12, "Na", 21414.830),
    (12, 12, "Mg", 22341.908), (13, 14, "Al", 25133.143),
    (14, 14, "Si", 26060.344), (15, 16, "P", 28851.873),
    (16, 16, "S", 29781.800), (17, 18, "Cl", 32573.283),
    (18, 22, "Ar", 37224.719), (19, 20, "K", 36294.464),
    (20, 20, "Ca", 37224.918),
]

print("FULL 2×2 BRANE TOWER: ATOM MASSES")
print("=" * 80)
print()
print(f"{'Atom':>4} {'Z':>3} {'N':>3} {'gens':>5} {'Σ ln Z_fwd':>12} {'Σ ln Z_dual':>12} "
      f"{'Σ ln Z_comb':>12} {'B_obs':>10}")
print("-" * 80)

tower_sums = []
B_obs_list = []

for Z, N, sym, M_obs in isotopes:
    A = Z + N
    M_free = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    B_obs = M_free - M_obs

    ordering, gen_data = compute_atom_tower(Z, N)

    sum_ln_fwd = sum(g['ln_Z_fwd'] for g in gen_data if g['ln_Z_fwd'] < 1e10)
    sum_ln_dual = sum(g['ln_Z_dual'] for g in gen_data if g['ln_Z_dual'] < 1e10)
    sum_ln_comb = sum_ln_fwd + sum_ln_dual

    n_inf_fwd = sum(1 for g in gen_data if g['ln_Z_fwd'] >= 1e10)
    n_inf_dual = sum(1 for g in gen_data if g['ln_Z_dual'] >= 1e10)

    fwd_str = f"{sum_ln_fwd:>12.4f}" if n_inf_fwd == 0 else f"{'INF('+str(n_inf_fwd)+')':>12}"
    dual_str = f"{sum_ln_dual:>12.4f}" if n_inf_dual == 0 else f"{'INF('+str(n_inf_dual)+')':>12}"
    comb_str = f"{sum_ln_comb:>12.4f}" if n_inf_fwd + n_inf_dual == 0 else "INF"

    print(f"{sym:>4} {Z:>3} {N:>3} {len(gen_data):>5} {fwd_str} {dual_str} "
          f"{comb_str:>12} {B_obs:>10.2f}")

    if n_inf_fwd == 0:
        tower_sums.append((sum_ln_fwd, sum_ln_dual, sum_ln_comb, B_obs, sym, Z, N))
        B_obs_list.append(B_obs)

# Fit E_gauge from tower sums
if tower_sums:
    X_fwd = np.array([t[0] for t in tower_sums]).reshape(-1, 1)
    X_dual = np.array([t[1] for t in tower_sums]).reshape(-1, 1)
    X_comb = np.array([t[2] for t in tower_sums]).reshape(-1, 1)
    y = np.array([t[3] for t in tower_sums])

    for label, X in [("Forward", X_fwd), ("Dual", X_dual), ("Combined", X_comb)]:
        if np.all(np.isfinite(X)):
            coeff = float(np.linalg.lstsq(X, y, rcond=None)[0][0])
            y_pred = X.flatten() * coeff
            residuals = y - y_pred
            rmse = np.sqrt(np.mean(residuals**2))
            print(f"\n{label}: E_gauge = {coeff:.4f} MeV, RMSE = {rmse:.2f} MeV")

            # Show predictions
            print(f"  {'Atom':>4} {'B_pred':>10} {'B_obs':>10} {'err MeV':>10} {'err%':>8}")
            for i, (sf, sd, sc, bo, sym, Z, N) in enumerate(tower_sums):
                x_val = X[i, 0]
                bp = x_val * coeff
                err = bp - bo
                M_obs_i = [iso[3] for iso in isotopes if iso[0] == Z and iso[1] == N][0]
                err_pct = err / M_obs_i * 100
                print(f"  {sym:>4} {bp:>10.2f} {bo:>10.2f} {err:>+10.2f} {err_pct:>+7.3f}%")
