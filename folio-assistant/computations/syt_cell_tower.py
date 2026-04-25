#!/usr/bin/env python3
"""
SYT-cell JM mass tower — Track 1 of the mass-prediction guidance.

Replaces the generator-indexed scalar volumes $\hat V_i$ with
Jucys--Murphy (JM) cell-indexed volumes $\hat V_k^{\mathrm{JM}}$
($k = 1, \ldots, n$ over SYT cells, not generator positions):

    V_hat_JM[k](W)
      = tr_M(L_k . rho(W))
      = Sum_{lambda |- n} w_lambda . (1/d_lambda)
          . Sum_{T in SYT(lambda)} q^{2 c_T(k)} . <T | W^lambda | T>

where L_k is the JM element, acting diagonally on the Young basis
as q^{2 c_T(k)}, w_lambda = d_q(lambda)^2 / [n]_q! is the Plancherel
weight, and d_lambda = #SYT(lambda).

Tower mass (per mass-tower-syt-cells.md, eq:syt-cell-tower):

    m^(n) = | prod_k V_hat_JM[k] |
          + sum_k Phi_q(|V_hat_JM[k]|)
          + z^2 sum_{k1 < k2} Phi_q(|V_hat_JM[k1] . V_hat_JM[k2]|)

All pairs contribute (no adjacent vs far distinction) because
[L_i, L_j] = 0.  This matches the empirical beta(d) = 1 descent
rate and avoids the pair-incompleteness that was the suspected
source of the T residual in the scalar path.

Compared against the scalar generator-indexed tower from
adjacent_vs_full_probe.mass_from_tower_probe on D / T / 3He.
Proton calibrates E_0 for each path independently.

Cost: O(#partitions(n) . dim(lambda) . len(word) + n^2) per atom.
For n = 3A with A = 1 (proton, n = 3) or A = 2 (D, n = 6) this is
fast; A = 3 (T, 3He; n = 9; 30 partitions, max dim = 42) takes
seconds; A = 4 (4He, n = 12; 77 partitions, max dim ~ 132) is
minutes.
"""
from __future__ import annotations

import sys
import time
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy.sparse import issparse, eye as speye

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from mass_endomorphism import Phi_q, z_mark
from canonical_plus_multibrane import phi_q_safe
from hecke_characters import (partitions_of, dim_q, qfac,
                                standard_young_tableaux,
                                build_seminormal_matrices)
from mass_at_3A_proper import atom_braid_word_3A, _cached_seminormal
from atom_braid_sdp_gluon import atom_braid_word_3A_sdp_gluon


def _word_diagonal_in_lambda_given(sigmas, dim,
                                      word: list[tuple[float, float, int]]
                                      ) -> list[float]:
    """diag(W^lambda) in the Hoefsmit seminormal basis, given
    pre-built sigmas + dim from _cached_seminormal.  Caller reuses
    the same SYTs so we avoid the duplicate standard_young_tableaux
    enumeration (PR #383 review)."""
    if dim == 0:
        return []
    sparse = bool(sigmas) and issparse(sigmas[0])
    if sparse:
        prod = speye(dim, format='csr')
        I = speye(dim, format='csr')
    else:
        prod = np.eye(dim)
        I = np.eye(dim)
    for (c, d, g) in word:
        if g < len(sigmas):
            prod = prod @ (c * sigmas[g] + d * I)
    diag = prod.diagonal() if sparse else np.diag(prod)
    return [float(x) for x in diag]


def V_hat_JM_all(Z: int, N: int, *, include_inter: bool,
                   m_pp: int = 1, m_pn: int = 1,
                   m_nn: int = 1,
                   sdp_gluon: bool = False) -> list[float]:
    """JM cell volumes V_hat_JM[k] for k = 1..n, n = 3A.

    Computes all n cell volumes in a single pass over partitions —
    the dominant cost is building seminormal matrices and the word
    product, both of which are reused across k.

    sdp_gluon: if True, use atom_braid_word_3A_sdp_gluon so each
      neutron carries the integer-LP-optimal gluon tail L₊L₋ = σ₀σ₁σ₁σ₀
      (proton unchanged).  If False (default), uses the uniform 2·σ₀
      tail from atom_braid_word_3A.
    """
    A = Z + N
    n = 3 * A
    nfac = qfac(n)

    if sdp_gluon:
        word = atom_braid_word_3A_sdp_gluon(
            Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
            include_inter=include_inter)
    else:
        word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                    include_inter=include_inter)
    # adjacent_vs_full_probe / mass_from_tower_probe treats
    # include_inter=False as the free path.  atom_braid_word_3A
    # respects the flag — no remap needed here.

    V_JM = [0.0] * n  # V_JM[k-1] stores the k-th cell volume (k = 1..n)

    # Reuse SYTs from the cached seminormal build: avoid calling
    # standard_young_tableaux twice per partition (PR #383 review).
    # Contents are recomputed from cells (cheap) since
    # build_seminormal_matrices returns syts but not contents.
    for shape in partitions_of(n):
        sigmas, dim, syts = _cached_seminormal(shape)
        d_lambda = len(syts)
        if d_lambda == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_lambda = (dq * dq) / nfac
        # Re-derive contents (row, col → col - row) from shape cells.
        cells = [(i, j) for i, r in enumerate(shape) for j in range(r)]
        contents = [c - r for (r, c) in cells]

        diag = _word_diagonal_in_lambda_given(sigmas, dim, word)
        if not diag:
            continue

        # For each cell index k (1..n), sum q^{2 c_T(k)} . diag[T].
        # contents[syts[t][k]] is the content of the cell holding
        # entry k in SYT t.
        for k in range(1, n + 1):
            cell_sum = 0.0
            for t_idx, syt in enumerate(syts):
                c_T_k = contents[syt[k]]
                cell_sum += (Q0 ** (2 * c_T_k)) * diag[t_idx]
            V_JM[k - 1] += w_lambda * cell_sum / d_lambda

    return V_JM


def tower_mass_JM(V_JM: list[float], *,
                     cap_frac: float = 0.98) -> tuple[float, dict]:
    """Assemble tower mass from cell volumes per eq:syt-cell-tower.

    Uses `phi_q_safe(..., cap_frac=cap_frac)` for each Phi_q argument
    so values near the Q0 singularity are capped rather than silently
    skipped (PR #383 review: silent skip would under-estimate mass
    if any |V_JM[k]| or |V_JM[k1]·V_JM[k2]| approaches Q0).
    """
    n = len(V_JM)
    desc = abs(math.prod(V_JM)) if V_JM else 1.0
    single = sum(phi_q_safe(abs(v), cap_frac=cap_frac) for v in V_JM)
    cross = 0.0
    # All pairs, no distance filter — [L_i, L_j] = 0.
    for i in range(n):
        for j in range(i + 1, n):
            prod = abs(V_JM[i] * V_JM[j])
            cross += (z_mark ** 2) * phi_q_safe(prod, cap_frac=cap_frac)
    return desc + single + cross, {'desc': desc, 'single': single,
                                       'cross': cross, 'V_JM': V_JM}


def binding_JM(Z: int, N: int, *, m_pp: int = 1, m_pn: int = 1,
                 m_nn: int = 1, E_0: float,
                 sdp_gluon: bool = False) -> dict:
    """Binding B = E_0 . (m_free - m_atom) via JM tower."""
    V_a = V_hat_JM_all(Z, N, include_inter=True,
                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                          sdp_gluon=sdp_gluon)
    V_f = V_hat_JM_all(Z, N, include_inter=False,
                          sdp_gluon=sdp_gluon)
    m_a, det_a = tower_mass_JM(V_a)
    m_f, det_f = tower_mass_JM(V_f)
    B = E_0 * (m_f - m_a)
    return {'m_atom': m_a, 'm_free': m_f, 'B_MeV': B,
              'V_atom': V_a, 'V_free': V_f,
              'detail_atom': det_a, 'detail_free': det_f}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="SYT-cell JM mass tower probe")
    parser.add_argument("--include-4he", action="store_true",
                          help="Also compute 4He (n = 12, minutes)")
    parser.add_argument("--heavy", action="store_true",
                          help="Heavy-atom AME test: 6Li + 9Be (n = 18, "
                           "27; minutes to hours).  Requires the "
                           "seminormal disk cache in .cache/seminormal/.")
    parser.add_argument("--only", type=str, default=None,
                          help="Comma-separated atom symbols to run "
                           "(e.g. '6Li').  Overrides the default list.")
    args = parser.parse_args()

    from adjacent_vs_full_probe import (mass_from_tower_probe,
                                           get_ilp_ground)
    from hecke_core import atom_per_generator_volumes

    ATOMS = [
        ('D',   1, 1,  2.22452),
        ('T',   1, 2,  8.481821),
        ('3He', 2, 1,  7.71804),
    ]
    if args.include_4he:
        ATOMS.append(('4He', 2, 2, 28.295674))
    if args.heavy:
        # AME2020 binding totals (A * B/A):
        # 6Li: 6 * 5.3326 = 31.9956 MeV
        # 9Be: 9 * 6.4628 = 58.1652 MeV
        ATOMS.append(('6Li', 3, 3, 31.9956))
        ATOMS.append(('9Be', 4, 5, 58.1652))
    if args.only:
        keep = set(s.strip() for s in args.only.split(','))
        ATOMS = [a for a in ATOMS if a[0] in keep]

    print("=" * 110)
    print("SYT-CELL JM TOWER PROBE (Track 1)")
    print(f"q0 = {Q0:.6f}")
    print("=" * 110)

    # Scalar proton calibration (existing path).
    vols_p_s = atom_per_generator_volumes(1, 0, include_inter=False)
    _, _, _, m_p_s = mass_from_tower_probe(vols_p_s, cross_mode='full',
                                               phi_q_variant='raw')
    E_0_scalar = 938.272 / m_p_s

    # JM proton calibration (uniform 2·σ₀ gluon).
    V_p_JM = V_hat_JM_all(1, 0, include_inter=False)
    m_p_JM, _ = tower_mass_JM(V_p_JM)
    E_0_JM = 938.272 / m_p_JM

    # JM proton under SDP-optimal gluon (proton word unchanged, so E_0
    # should equal E_0_JM — sanity check).
    V_p_JM_sdp = V_hat_JM_all(1, 0, include_inter=False, sdp_gluon=True)
    m_p_JM_sdp, _ = tower_mass_JM(V_p_JM_sdp)
    E_0_JM_sdp = 938.272 / m_p_JM_sdp

    print(f"Proton:  scalar m_p = {m_p_s:.4e}  E_0 = {E_0_scalar:.6e}  MeV/cat")
    print(f"         JM     m_p = {m_p_JM:.4e}  E_0 = {E_0_JM:.6e}  MeV/cat")
    print(f"         JM+SDP m_p = {m_p_JM_sdp:.4e}  E_0 = {E_0_JM_sdp:.6e}  "
          f"MeV/cat  (Δ = {abs(m_p_JM-m_p_JM_sdp):.2e})")
    print()

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        gs = get_ilp_ground(Z, N)
        mpp = gs.get('m_pp', 1)
        mpn = gs.get('m_pn', 1)
        mnn = gs.get('m_nn', 1)
        print(f"{name} A={A}  ILP = {gs}")

        # Scalar path
        t0 = time.time()
        vols_a = atom_per_generator_volumes(
            Z, N, include_inter=True, m_pp=mpp, m_pn=mpn, m_nn=mnn)
        vols_f = atom_per_generator_volumes(Z, N, include_inter=False)
        _, _, _, m_a_s = mass_from_tower_probe(
            vols_a, cross_mode='full', phi_q_variant='raw')
        _, _, _, m_f_s = mass_from_tower_probe(
            vols_f, cross_mode='full', phi_q_variant='raw')
        B_s = E_0_scalar * (m_f_s - m_a_s)
        err_s = abs(B_s - B_AME) / Mtot * 100
        dt_s = time.time() - t0

        # JM path (uniform 2·σ₀ gluon)
        t0 = time.time()
        res_JM = binding_JM(Z, N, m_pp=mpp, m_pn=mpn, m_nn=mnn,
                               E_0=E_0_JM)
        err_JM = abs(res_JM['B_MeV'] - B_AME) / Mtot * 100
        dt_JM = time.time() - t0

        # JM + SDP-optimal per-nucleon gluon
        t0 = time.time()
        res_JM_sdp = binding_JM(Z, N, m_pp=mpp, m_pn=mpn, m_nn=mnn,
                                   E_0=E_0_JM_sdp, sdp_gluon=True)
        err_JM_sdp = abs(res_JM_sdp['B_MeV'] - B_AME) / Mtot * 100
        dt_JM_sdp = time.time() - t0

        print(f"  scalar:  m_a={m_a_s:.4e}  m_f={m_f_s:.4e}  "
              f"B={B_s:+8.3f}  err={err_s:.4f}%  ({dt_s:.1f}s)")
        print(f"  JM:      m_a={res_JM['m_atom']:.4e}  "
              f"m_f={res_JM['m_free']:.4e}  "
              f"B={res_JM['B_MeV']:+8.3f}  err={err_JM:.4f}%  ({dt_JM:.1f}s)")
        print(f"  JM+SDP:  m_a={res_JM_sdp['m_atom']:.4e}  "
              f"m_f={res_JM_sdp['m_free']:.4e}  "
              f"B={res_JM_sdp['B_MeV']:+8.3f}  err={err_JM_sdp:.4f}%  "
              f"({dt_JM_sdp:.1f}s)")
        print()

        results.append({
            'atom': name, 'Z': Z, 'N': N, 'A': A,
            'B_AME': B_AME,
            'ILP': gs,
            'B_scalar_MeV': B_s,
            'err_scalar_pct': err_s,
            'B_JM_MeV': res_JM['B_MeV'],
            'err_JM_pct': err_JM,
            'B_JM_SDP_MeV': res_JM_sdp['B_MeV'],
            'err_JM_SDP_pct': err_JM_sdp,
            'V_JM_atom': res_JM['V_atom'],
            'V_JM_free': res_JM['V_free'],
            'V_JM_SDP_atom': res_JM_sdp['V_atom'],
            'V_JM_SDP_free': res_JM_sdp['V_free'],
            'scalar_time_sec': dt_s,
            'JM_time_sec': dt_JM,
            'JM_SDP_time_sec': dt_JM_sdp,
        })

    w = {
        'computation': 'syt-cell-jm-tower',
        'description': (
            'SYT-cell JM mass tower.  V_hat_JM[k] = tr_M(L_k . rho(W)) '
            '= Sum_lambda w_lambda / d_lambda . Sum_T q^{2 c_T(k)} '
            '. <T|W^lambda|T>.  Tower mass = |prod V_JM| + '
            'Sum_k Phi_q(|V_JM[k]|) + z^2 Sum_{k1<k2} '
            'Phi_q(|V_JM[k1] . V_JM[k2]|).  All pairs (L_i L_j '
            'commute).  Compared to scalar generator-indexed tower on '
            'D, T, 3He (and optionally 4He).'),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'parameters': {'q0': Q0,
                          'E_0_scalar': E_0_scalar,
                          'E_0_JM': E_0_JM},
        'results': results,
    }
    out = Path(__file__).parent / 'syt-cell-jm-tower.witness.json'
    out.write_text(json.dumps(w, indent=2, default=str))
    print(f"Witness: {out}")
