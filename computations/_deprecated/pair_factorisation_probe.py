#!/usr/bin/env python3
"""
Traced-product pair volumes V̂_{ij} per prop:mass-endomorphism-tower.

The current `atom_per_generator_volumes` gives **scalar** V̂_i — a
Plancherel-aggregated scalar per generator.  Pair terms in the mass
tower are computed as V̂_i · V̂_j (product of two scalars), which
implicitly assumes

    χ^λ(σ_i σ_j)  =  χ^λ(σ_i) · χ^λ(σ_j)

This character-factorisation is **false in general** (only holds for
1-dim irreps — trivial and sign).  The true pair contribution should
be the Plancherel-aggregated traced product:

    V̂_{ij}  =  Σ_λ w_λ · tr_λ(ρ^λ(σ_i σ_j)) / d_λ
            =  Σ_λ w_λ · χ^λ(σ_i σ_j) / d_λ

where σ_i, σ_j here mean the FULL atom-braid factor-products at
generators i and j respectively (each may be a product of several
(c·σ + d·I) factors), and σ_i σ_j denotes their composition in
atom-braid-word order.

This module builds V̂_{ij} for all pairs (i < j) by per-irrep
seminormal character evaluation + Plancherel sum.  Used as the
traced-product fix for the pair terms in `tower_mass_level`.

Computational cost: O(p(n) · dim²) per pair, vs O(p(n) · dim) for
V̂_i.  For n_strands = 3A ≤ 12, tractable in seconds.
"""
from __future__ import annotations

import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def _factors_at_gen(word: list[tuple[float, float, int]],
                     gen: int) -> list[tuple[float, float]]:
    """Sub-list of (c, d) factors of `word` that act at generator `gen`
    (in atom-braid-word original order)."""
    return [(c, d) for (c, d, g) in word if g == gen]


def _ordered_ij_factors(word: list[tuple[float, float, int]],
                         i: int, j: int) -> list[tuple[float, float, int]]:
    """Factors of `word` restricted to gens i and j, preserving order."""
    return [(c, d, g) for (c, d, g) in word if g == i or g == j]


def atom_per_pair_volumes(Z: int, N: int, *,
                             include_inter: bool = True,
                             m_pp: int = 1, m_pn: int = 1,
                             m_nn: int = 1) -> dict:
    """Plancherel-aggregated V̂_{ij} for all pairs (i < j) in the
    atom braid word.

    Returns {(i, j): V_ij_scalar} where V_ij_scalar is the real
    Plancherel sum Σ_λ (d_q(λ)² / [n]_q!) · χ^λ(σ_ij-word) / d_λ.
    """
    import numpy as np
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_characters import (partitions_of, dim_q, qfac,
                                    build_seminormal_matrices)

    A = Z + N
    if A < 1:
        return {}
    n_strands = 3 * A
    n_gens = n_strands - 1 if include_inter else 2 * A
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    # When include_inter=False, word only has generators up to 2A-1
    # and generators 3k+2 are simply absent.  atom_per_generator_volumes
    # re-maps to 2A gens; we mirror that.
    if not include_inter:
        # Re-map word to free basis: gen 3k → 2k, 3k+1 → 2k+1
        remapped = []
        for (c, d, g) in word:
            k = g // 3
            rem = g % 3
            if rem == 0:
                remapped.append((c, d, 2 * k))
            elif rem == 1:
                remapped.append((c, d, 2 * k + 1))
        word = remapped

    from scipy.sparse import issparse, eye as speye
    import numpy as np
    nfac = qfac(n_strands)
    out: dict[tuple[int, int], float] = {}
    # Precompute seminormal matrices per shape (small n, cache)
    shape_mats: dict[tuple, tuple] = {}
    for shape in partitions_of(n_strands):
        s, d, _ = build_seminormal_matrices(shape)
        shape_mats[shape] = (s, d)

    for i in range(n_gens):
        for j in range(i + 1, n_gens):
            ij_word = _ordered_ij_factors(word, i, j)
            if not ij_word:
                out[(i, j)] = 1.0  # identity at both → V_ij = 1
                continue
            V_ij = 0.0
            for shape in partitions_of(n_strands):
                sigmas, dim = shape_mats[shape]
                if dim == 0:
                    continue
                dq = dim_q(shape)
                if dq == 0:
                    continue
                w_lam = (dq * dq) / nfac
                is_sparse = issparse(sigmas[0]) if sigmas else False
                if is_sparse:
                    prod = speye(dim, format='csr')
                    I = speye(dim, format='csr')
                else:
                    prod = np.eye(dim)
                    I = np.eye(dim)
                for (c, d, g) in ij_word:
                    if g < len(sigmas):
                        M = c * sigmas[g] + d * I
                        prod = prod @ M
                if is_sparse:
                    chi = float(prod.diagonal().sum())
                else:
                    chi = float(np.trace(prod))
                V_ij += w_lam * chi / dim
            out[(i, j)] = V_ij
    return out


# ── Probe: tower mass with traced-product V̂_ij ─────────────

def tower_mass_traced(V: list[float], V_pair: dict,
                        pair_mode: str = 'full') -> float:
    """Tower mass using traced-product V̂_ij in pair terms."""
    from mass_endomorphism import Phi_q, z_mark
    from q_parameter import Q as Q0
    n = len(V)
    desc = abs(math.prod(V))
    single = sum(Phi_q(abs(v)) for v in V if abs(v) < Q0)
    cross = 0.0
    if pair_mode == 'adjacent':
        pairs = [(i, i + 1) for i in range(n - 1)]
    else:
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for (i, j) in pairs:
        V_ij = V_pair.get((i, j), V[i] * V[j])
        p = abs(V_ij)
        if p < Q0:
            cross += z_mark ** 2 * Phi_q(p)
    return desc + single + cross


# ── CLI ─────────────────────────────────────────────────────

if __name__ == "__main__":
    import time, json
    from datetime import datetime, timezone
    from pyhecke.gram import atom_per_generator_volumes
    from mass_endomorphism import Phi_q, z_mark
    from q_parameter import Q as Q0
    from adjacent_vs_full_probe import mass_from_tower_probe, get_ilp_ground

    ATOMS = [('D', 1, 1, 2.22452),
             ('T', 1, 2, 8.481821),
             ('3He', 2, 1, 7.71804),
             ('4He', 2, 2, 28.295674)]

    # Calibrate E_0 by matching proton tower under scalar mode
    vols_p = atom_per_generator_volumes(1, 0, include_inter=False)
    V_p = [v['full'] for v in vols_p]
    _, _, _, m_p_scalar = mass_from_tower_probe(vols_p, cross_mode='full',
                                                   phi_q_variant='raw')
    V_p_pair = atom_per_pair_volumes(1, 0, include_inter=False)
    m_p_traced = tower_mass_traced(V_p, V_p_pair, pair_mode='full')
    E_0_scalar = 938.272 / m_p_scalar
    E_0_traced = 938.272 / m_p_traced
    print(f"Proton: m_p_scalar = {m_p_scalar:.4e}  E_0_scalar = {E_0_scalar:.4e} MeV/cat")
    print(f"       m_p_traced = {m_p_traced:.4e}  E_0_traced = {E_0_traced:.4e} MeV/cat")
    print()

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        gs = get_ilp_ground(Z, N)
        mpp = gs.get('m_pp', 1); mpn = gs.get('m_pn', 1); mnn = gs.get('m_nn', 1)

        t0 = time.time()
        vols_a = atom_per_generator_volumes(Z, N, include_inter=True,
                                              m_pp=mpp, m_pn=mpn, m_nn=mnn)
        vols_f = atom_per_generator_volumes(Z, N, include_inter=False)
        V_a = [v['full'] for v in vols_a]
        V_f = [v['full'] for v in vols_f]
        _, _, _, m_a_scalar = mass_from_tower_probe(
            vols_a, cross_mode='full', phi_q_variant='raw')
        _, _, _, m_f_scalar = mass_from_tower_probe(
            vols_f, cross_mode='full', phi_q_variant='raw')
        B_scalar = E_0_scalar * (m_f_scalar - m_a_scalar)
        err_scalar = abs(B_scalar - B_AME) / Mtot * 100
        dt_s = time.time() - t0

        t0 = time.time()
        V_a_pair = atom_per_pair_volumes(Z, N, include_inter=True,
                                            m_pp=mpp, m_pn=mpn, m_nn=mnn)
        V_f_pair = atom_per_pair_volumes(Z, N, include_inter=False)
        m_a_traced = tower_mass_traced(V_a, V_a_pair, pair_mode='full')
        m_f_traced = tower_mass_traced(V_f, V_f_pair, pair_mode='full')
        B_traced = E_0_traced * (m_f_traced - m_a_traced)
        err_traced = abs(B_traced - B_AME) / Mtot * 100
        dt_t = time.time() - t0

        print(f"{name} A={A} ILP={gs}:")
        print(f"  scalar:  B={B_scalar:>+10.3f}  err={err_scalar:.3f}%  ({dt_s:.1f}s)")
        print(f"  traced:  B={B_traced:>+10.3f}  err={err_traced:.3f}%  ({dt_t:.1f}s)")

        results.append({'atom': name, 'Z': Z, 'N': N, 'A': A,
                         'B_AME': B_AME,
                         'ILP': gs,
                         'B_scalar_MeV': B_scalar,
                         'err_scalar_pct': err_scalar,
                         'B_traced_MeV': B_traced,
                         'err_traced_pct': err_traced,
                         'scalar_time_sec': dt_s,
                         'traced_time_sec': dt_t})

    w = {'computation': 'pair-factorisation-probe',
         'description': (
             "Tests traced-product V̂_ij (true Plancherel-aggregated "
             "character of σ_i σ_j) vs scalar V̂_i · V̂_j factorisation "
             "in the Φ_q tower pair terms.  Scalar factorisation assumes "
             "χ^λ(σ_iσ_j) = χ^λ(σ_i)·χ^λ(σ_j), which only holds for "
             "1-dim irreps.  Per-pair traced evaluation captures the "
             "character correlation Δ_{ij}^λ that the scalar path drops."),
         'timestamp': datetime.now(timezone.utc).isoformat(),
         'parameters': {'q0': Q0, 'E_0_scalar': E_0_scalar,
                          'E_0_traced': E_0_traced},
         'results': results}
    Path('pair-factorisation-probe.witness.json').write_text(
        json.dumps(w, indent=2, default=str))
    print(f"\nWitness written")
