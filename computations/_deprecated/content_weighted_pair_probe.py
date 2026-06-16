#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Content-weighted pair terms — SYT-wise probe.

Conjecture: the scalar factorization V̂_i · V̂_j drops the per-SYT
content correlation.  Replace with the SYT-content-weighted pair:

    V̂_{ij}^{content}(W)  =  Σ_λ (d_q(λ)² / [n]_q!) · (1 / d_λ)
                            · Σ_{T ∈ SYT(λ)}
                              q^{2·(c_T(entry_{i+1}) + c_T(entry_{j+1}))}
                              · ⟨T | W^λ | T⟩

where c_T(k) is the content of the cell holding entry k in SYT T,
and ⟨T | W^λ | T⟩ is the diagonal element of the braid word W in
the seminormal λ-irrep at basis |T⟩.

Compared to scalar V̂_i · V̂_j (current default): keeps SYT-level
correlation between gens i and j.  At q = 1 it reduces to the
scalar path (q^{2·(...)} = 1).

Computational cost: per-λ dim d_λ · len(word) matrix-vector
operations per pair.  Full pair sweep ≈ O(n² · p(n) · d_λ · len(W)).

PROBE — compares content-weighted pair tower to scalar on
D, T, ³He, ⁴He; checks if the T/³He residuals move toward AME.
"""
from __future__ import annotations

import sys
import time
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from mass_endomorphism import Phi_q, z_mark
from hecke_characters import (partitions_of, dim_q, qfac,
                                standard_young_tableaux,
                                build_seminormal_matrices)
from mass_at_3A_proper import atom_braid_word_3A


def _diagonal_of_word_in_lambda(shape: tuple[int, ...],
                                 word: list[tuple[float, float, int]]
                                 ) -> list[float]:
    """⟨T | W^λ | T⟩ for T ∈ SYT(λ), in order.

    W = Π_k (c_k σ_{g_k} + d_k I) acting as a linear operator.
    Returns list indexed by SYT position, one diagonal value per T.
    Uses the Hoefsmit seminormal basis.
    """
    import numpy as np
    from scipy.sparse import issparse, eye as speye

    sigmas, dim, syts = build_seminormal_matrices(shape)
    if dim == 0:
        return []
    is_sparse = issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        prod = speye(dim, format='csr')
        I = speye(dim, format='csr')
    else:
        prod = np.eye(dim)
        I = np.eye(dim)
    for (c, d, g) in word:
        if g < len(sigmas):
            M = c * sigmas[g] + d * I
            prod = prod @ M
    if is_sparse:
        diag = prod.diagonal()
    else:
        diag = np.diag(prod)
    return [float(x) for x in diag]


def content_weighted_pair_term(Z: int, N: int, pair: tuple[int, int],
                                  *, include_inter: bool,
                                  m_pp: int = 1, m_pn: int = 1,
                                  m_nn: int = 1) -> float:
    """V̂_{ij}^{content} for pair = (i, j) of generators.

    Gens are 0-indexed; gen i corresponds to the swap of entries
    (i+1) ↔ (i+2) in the SYT filling.  We take the "position" for
    pair term as entries (i+1) and (j+1) — the left entry of each
    generator's pair.
    """
    import numpy as np
    i, j = pair
    A = Z + N
    n_strands = 3 * A
    nfac = qfac(n_strands)
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    if not include_inter:
        remapped = []
        for (c, d, g) in word:
            k = g // 3
            rem = g % 3
            if rem == 0:
                remapped.append((c, d, 2 * k))
            elif rem == 1:
                remapped.append((c, d, 2 * k + 1))
        word = remapped

    entry_i = i + 1
    entry_j = j + 1

    total = 0.0
    for shape in partitions_of(n_strands):
        syts, cells, contents = standard_young_tableaux(shape)
        d_cl = len(syts)
        if d_cl == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_lam = (dq * dq) / nfac

        diag = _diagonal_of_word_in_lambda(shape, word)
        if not diag:
            continue
        lam_sum = 0.0
        for t_idx, syt in enumerate(syts):
            c_i = contents[syt[entry_i]] if entry_i in syt else 0
            c_j = contents[syt[entry_j]] if entry_j in syt else 0
            weight = Q0 ** (2 * (c_i + c_j))
            lam_sum += weight * diag[t_idx]
        total += w_lam * (lam_sum / d_cl)
    return total


def tower_mass_content_weighted(Z: int, N: int, *,
                                   include_inter: bool,
                                   m_pp: int = 1, m_pn: int = 1,
                                   m_nn: int = 1) -> tuple[float, dict]:
    """Tower mass with content-weighted pair terms.

    Uses current scalar V̂_i for desc+single (unchanged); replaces
    the pair cross-term with content-weighted V̂_{ij}^{content}.
    """
    from pyhecke.gram import atom_per_generator_volumes
    if include_inter:
        vols = atom_per_generator_volumes(
            Z, N, include_inter=True,
            m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    else:
        vols = atom_per_generator_volumes(Z, N, include_inter=False)
    V = [v['full'] for v in vols]
    n = len(V)
    desc = abs(math.prod(V)) if V else 1.0
    single = sum(Phi_q(abs(v)) for v in V if abs(v) < Q0)

    pair_vals = {}
    cross = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            V_ij = content_weighted_pair_term(
                Z, N, (i, j), include_inter=include_inter,
                m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
            pair_vals[(i, j)] = V_ij
            if abs(V_ij) < Q0:
                cross += z_mark ** 2 * Phi_q(abs(V_ij))
    return desc + single + cross, {'desc': desc, 'single': single,
                                       'cross': cross,
                                       'pair_vals': pair_vals}


if __name__ == "__main__":
    from adjacent_vs_full_probe import (mass_from_tower_probe,
                                           get_ilp_ground)
    from pyhecke.gram import atom_per_generator_volumes

    ATOMS = [
        ('D',   1, 1,  2.22452),
        ('T',   1, 2,  8.481821),
        ('3He', 2, 1,  7.71804),
    ]

    print("=" * 110)
    print("CONTENT-WEIGHTED PAIR TOWER PROBE (SYT-wise)")
    print(f"q₀ = {Q0:.6f}")
    print("=" * 110)

    # Calibrate E_0 using proton (no pair term needed — only 2 gens,
    # and scalar vs content-weighted should give same at proton level
    # since n_strands=3 is small).  Use scalar path's E_0 for fair
    # comparison.
    vols_p = atom_per_generator_volumes(1, 0, include_inter=False)
    _, _, _, m_p = mass_from_tower_probe(vols_p, cross_mode='full',
                                             phi_q_variant='raw')
    E_0 = 938.272 / m_p
    print(f"Proton calibration: m_p_scalar={m_p:.4e}  E_0={E_0:.6e} MeV/cat")

    # Also compute content-weighted proton for consistency check
    m_p_cw, _ = tower_mass_content_weighted(1, 0, include_inter=False)
    E_0_cw = 938.272 / m_p_cw
    print(f"           content-wt: m_p_cw={m_p_cw:.4e}  E_0={E_0_cw:.6e} MeV/cat")
    print()

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        gs = get_ilp_ground(Z, N)
        mpp = gs.get('m_pp', 1); mpn = gs.get('m_pn', 1); mnn = gs.get('m_nn', 1)
        print(f"{name} A={A}: ILP = {gs}")

        t0 = time.time()
        vols_a = atom_per_generator_volumes(
            Z, N, include_inter=True, m_pp=mpp, m_pn=mpn, m_nn=mnn)
        vols_f = atom_per_generator_volumes(Z, N, include_inter=False)
        _, _, _, m_a_scalar = mass_from_tower_probe(
            vols_a, cross_mode='full', phi_q_variant='raw')
        _, _, _, m_f_scalar = mass_from_tower_probe(
            vols_f, cross_mode='full', phi_q_variant='raw')
        B_scalar = E_0 * (m_f_scalar - m_a_scalar)
        err_scalar = abs(B_scalar - B_AME) / Mtot * 100
        dt_s = time.time() - t0

        t0 = time.time()
        m_a_cw, _ = tower_mass_content_weighted(
            Z, N, include_inter=True, m_pp=mpp, m_pn=mpn, m_nn=mnn)
        m_f_cw, _ = tower_mass_content_weighted(Z, N, include_inter=False)
        # Use content-weighted calibration for content-weighted binding
        B_cw = E_0_cw * (m_f_cw - m_a_cw)
        err_cw = abs(B_cw - B_AME) / Mtot * 100
        dt_cw = time.time() - t0

        print(f"  scalar:  m_a={m_a_scalar:.4e}  m_f={m_f_scalar:.4e}  "
              f"B={B_scalar:+8.3f}  err={err_scalar:.3f}%  ({dt_s:.1f}s)")
        print(f"  content: m_a={m_a_cw:.4e}  m_f={m_f_cw:.4e}  "
              f"B={B_cw:+8.3f}  err={err_cw:.3f}%  ({dt_cw:.1f}s)")
        print()
        results.append({
            'atom': name, 'Z': Z, 'N': N, 'A': A,
            'B_AME': B_AME,
            'ILP': gs,
            'B_scalar_MeV': B_scalar,
            'err_scalar_pct': err_scalar,
            'B_content_MeV': B_cw,
            'err_content_pct': err_cw,
            'scalar_time_sec': dt_s,
            'content_time_sec': dt_cw,
        })

    w = {
        'computation': 'content-weighted-pair-probe',
        'description': (
            'Content-weighted pair terms SYT-wise.  Replaces scalar '
            'V̂_i · V̂_j with V̂_{ij}^{content} = Σ_λ w_λ / d_λ · '
            'Σ_{T ∈ SYT(λ)} q^{2(c_T(i+1) + c_T(j+1))} · ⟨T|W^λ|T⟩.  '
            'Captures per-SYT content correlation between gens i, j '
            'missing from the scalar path.  Tests whether this closes '
            'the T/³He residual gap.'),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'parameters': {'q0': Q0,
                          'E_0_scalar': E_0,
                          'E_0_content_weighted': E_0_cw},
        'results': results,
    }
    p = Path('content-weighted-pair-probe.witness.json')
    p.write_text(json.dumps(w, indent=2, default=str))
    print(f"Witness: {p}")
