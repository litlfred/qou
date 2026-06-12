#!/usr/bin/env python3
"""
Wedderburn-coupled pair volumes |V̂_i V̂_j|_Wedderburn.

Per the proposed pair-gen extension to ρ_K
(`prop:rho-k-graded-expansion`):

  α · z² · Σ_{i<j} ln |V̂_i V̂_j|_Wedderburn

where (per the Wedderburn-block decomposition in
thm:wedderburn-mass-formula):

  |V̂_i V̂_j|_Wedderburn
    = w_sym  · λ_i^sym · λ_j^sym       [sym-channel: 1-dim, pure product]
    + w_std  · [z · (M_i M_j)_12 + (M_i M_j)_22]   [std-channel: 2-dim Markov-traced product]
    + w_alt  · λ_i^alt · λ_j^alt       [alt-channel: 1-dim, pure product]

This module:
  1. Extends `atom_per_generator_volumes` to track the FULL 2x2
     transfer matrix M_i per generator (not just the bottom row).
  2. Computes pair-volume |V̂_i V̂_j|_Wedderburn from the matrix
     products M_i M_j.

Output: tested via `rho_k_pair_gen_extension_v2_probe.py`.

Refs:
  - prop:rho-k-graded-expansion (the unified formula)
  - thm:wedderburn-mass-formula (the channel weights)
  - hecke_core.atom_per_generator_volumes (single-gen baseline)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from hecke_core import (  # noqa: E402
    h, q0, qi, q_int,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)


def atom_per_generator_full_matrices(
    Z: int, N: int, *, include_inter: bool = True,
    crossings_per_pair: int = 1,
    m_pp: int = None, m_pn: int = None, m_nn: int = None,
) -> list[dict]:
    """Per-generator FULL 2x2 transfer matrix M_i in the H_3 standard
    rep, for the atom braid.

    Extends `hecke_core.atom_per_generator_volumes` to track the
    complete 2x2 matrix entries (m11, m12, m21, m22) per generator
    instead of only the bottom row (a_i, b_i).

    Returns a list of dicts:
        [{"m11": ..., "m12": ..., "m21": ..., "m22": ...,
          "sym": ..., "alt": ...}, ...]

    The 2x2 transfer matrix is built by right-multiplying the per-
    crossing matrix C = [[c·h+d, c], [c, d]] onto an accumulator
    initialised to the identity.  For the bottom row this matches
    `atom_per_generator_volumes` exactly: (a_i, b_i) = (m21, m22).

    Sym/alt eigenvalue products λ^sym = Π(c·q + d), λ^alt = Π(-c·q⁻¹ + d)
    are tracked in parallel as scalar accumulators (1-dim irreps).
    """
    A = Z + N
    if A < 1:
        return []

    ordering = ['p'] * Z + ['n'] * N

    if include_inter:
        n_strands = 3 * A
        n_gens_total = n_strands - 1
    else:
        n_gens_total = 2 * A

    # Per-generator 2x2 matrix accumulators (initialise to identity)
    m11 = [1.0] * n_gens_total
    m12 = [0.0] * n_gens_total
    m21 = [0.0] * n_gens_total
    m22 = [1.0] * n_gens_total
    sp_arr = [1.0] * n_gens_total  # λ^sym
    ap_arr = [1.0] * n_gens_total  # λ^alt

    def apply_crossing(i: int, c: float, d: float) -> None:
        """Right-multiply the 2x2 matrix at generator i by C(c, d)."""
        # M' = M @ [[c·h+d, c], [c, d]]
        # (M')_11 = m11·(c·h+d) + m12·c
        # (M')_12 = m11·c       + m12·d
        # (M')_21 = m21·(c·h+d) + m22·c
        # (M')_22 = m21·c       + m22·d
        chd = c * h + d
        new_m11 = m11[i] * chd + m12[i] * c
        new_m12 = m11[i] * c   + m12[i] * d
        new_m21 = m21[i] * chd + m22[i] * c
        new_m22 = m21[i] * c   + m22[i] * d
        m11[i] = new_m11
        m12[i] = new_m12
        m21[i] = new_m21
        m22[i] = new_m22
        sp_arr[i] *= c * q0 + d
        ap_arr[i] *= -c * qi + d

    for k, nuc in enumerate(ordering):
        intra    = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        if include_inter:
            base_g0 = 3 * k
            base_g1 = 3 * k + 1
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        for c, d in intra:
            apply_crossing(base_g0, c, d)
        for c, d in intra_g1:
            apply_crossing(base_g1, c, d)
        if include_inter and k < A - 1:
            i = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (1.0, 0.0)
                m_this = m_pp if m_pp is not None else crossings_per_pair
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (1.0, -h)
                m_this = m_nn if m_nn is not None else crossings_per_pair
            else:
                base_cross = (1.0, -h / 2)
                m_this = m_pn if m_pn is not None else crossings_per_pair
            for _ in range(m_this):
                apply_crossing(i, *base_cross)

    return [
        {"m11": m11[i], "m12": m12[i], "m21": m21[i], "m22": m22[i],
         "sym": sp_arr[i], "alt": ap_arr[i]}
        for i in range(n_gens_total)
    ]


def wedderburn_pair_volumes(
    Z: int, N: int, *, include_inter: bool = True,
    crossings_per_pair: int = 1,
    m_pp: int = None, m_pn: int = None, m_nn: int = None,
) -> list[dict]:
    """Compute Wedderburn-coupled pair volumes |V̂_i V̂_j|_Wedderburn for
    all i < j in the atom braid.

    Channel decomposition (matching hecke_core's H_3 weights):
        sym (1-dim): λ_i^sym · λ_j^sym
        std (2-dim): z·(M_i M_j)_12 + (M_i M_j)_22
        alt (1-dim): λ_i^alt · λ_j^alt
        full       : w_sym·sym + w_std·std + w_alt·alt

    Returns list of dicts indexed by pair (i, j):
        [{"i": 0, "j": 1, "sym": ..., "std": ..., "alt": ..., "full": ...}, ...]
    """
    mats = atom_per_generator_full_matrices(
        Z, N,
        include_inter=include_inter,
        crossings_per_pair=crossings_per_pair,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
    )

    # H_3 Wedderburn weights (match hecke_core convention)
    z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)
    qdim_sym = 1.0
    qdim_std = q_int(2)
    qdim_alt = 1.0
    nf3_val = q_int(1) * q_int(2) * q_int(3)
    w_sym = qdim_sym ** 2 / nf3_val
    w_std = qdim_std ** 2 / nf3_val
    w_alt = qdim_alt ** 2 / nf3_val
    wt = w_sym + w_std + w_alt
    w_sym /= wt
    w_std /= wt
    w_alt /= wt

    out = []
    n = len(mats)
    for i in range(n):
        for j in range(i + 1, n):
            Mi = mats[i]
            Mj = mats[j]
            # (M_i M_j)_12 = m11_i · m12_j + m12_i · m22_j
            # (M_i M_j)_22 = m21_i · m12_j + m22_i · m22_j
            mij_12 = Mi["m11"] * Mj["m12"] + Mi["m12"] * Mj["m22"]
            mij_22 = Mi["m21"] * Mj["m12"] + Mi["m22"] * Mj["m22"]
            V_std_pair = z_mark * mij_12 + mij_22
            V_sym_pair = Mi["sym"] * Mj["sym"]
            V_alt_pair = Mi["alt"] * Mj["alt"]
            V_full_pair = (
                w_sym * V_sym_pair
                + w_std * V_std_pair
                + w_alt * V_alt_pair
            )
            out.append({
                "i": i, "j": j,
                "sym": V_sym_pair,
                "std": V_std_pair,
                "alt": V_alt_pair,
                "full": V_full_pair,
            })
    return out


if __name__ == "__main__":
    # Quick sanity check
    print("Wedderburn pair volumes — quick test (deuteron Z=1, N=1):")
    pairs = wedderburn_pair_volumes(1, 1)
    n = len(pairs)
    print(f"  n_pairs = {n}")
    print(f"  first 3 pairs:")
    for p in pairs[:3]:
        print(f"    ({p['i']}, {p['j']}): sym={p['sym']:.4f}  std={p['std']:.4f}  "
              f"alt={p['alt']:.4f}  full={p['full']:.4f}")

    # ── Witness emission ─────────────────────────────────────────
    from witness_base import WitnessBuilder  # noqa: E402

    w = WitnessBuilder("wedderburn-pair-volumes", engine="python")
    w.set_description(
        "Per-pair Wedderburn-coupled volumes |V̂_i V̂_j| = "
        "w_sym·λ^sym + w_std·Markov-trace + w_alt·λ^alt for the "
        "deuteron Z=1, N=1 atom braid; supports "
        "prop:knot-operator-lp-selection by exposing the LP/SDP "
        "input matrix entries for the active set."
    )
    w.set_content_block("prop:knot-operator-lp-selection")
    w.add_parameter("Z", 1)
    w.add_parameter("N", 1)
    w.add_parameter("n_pairs", n)
    # Cast to floats for JSON
    w.add_data(
        "pairs",
        [
            {
                "i": p["i"],
                "j": p["j"],
                "sym": float(p["sym"]),
                "std": float(p["std"]),
                "alt": float(p["alt"]),
                "full": float(p["full"]),
            }
            for p in pairs
        ],
    )
    # Sanity assertion: pair count = C(n_gens, 2) where n_gens = 5
    # (atom Z=1,N=1 with include_inter=True gives n_strands=6, n_gens=5)
    expected_n_pairs = 5 * 4 // 2
    w.add_assertion(
        "n_pairs equals C(n_gens, 2)",
        computed=n,
        expected=expected_n_pairs,
        tolerance=0,
    )
    # F1 (PR #565): structural anchors for the LP-selection
    # consumer. Wedderburn decomposition |V̂_i V̂_j| = w_sym λ^sym +
    # w_std λ^std + w_alt λ^alt is a real-valued sum; entries must
    # be finite reals.
    all_full_finite = all(
        not (p["full"] != p["full"]) and abs(p["full"]) < 1e15
        for p in pairs
    )
    w.add_assertion(
        "wedderburn_full_pair_volumes_finite",
        computed=1.0 if all_full_finite else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="prop:knot-operator-lp-selection",
    )

    # ── Canonical LP-dual record ─────────────────────────────────
    # Per CLAUDE.md §"LP / SDP duals — first-class infra": every
    # operator-selection witness MUST emit primal AND dual variables
    # (y0_star, y_star, active_set, primal_obj, dual_obj,
    # duality_gap). The canonical H_3 knot-operator-selection LP
    # instance: d=6 NF-basis operators {1, s0, s1, s0s1, s1s0,
    # s0s1s0}, objective t_i = tr_M(b_i) (post-2026-05-19-fix
    # TR_M[5] = h z^2 + z), Frobenius constraints G_ij = tr_M(b_i
    # b_j), net target = net(NF(B3)) for the canonical 3-strand
    # proton braid word (s0 s1)^3. Solved through the mandated
    # entry point lp_dual_solver.solve_operator_selection_lp (auto
    # backend: clarabel MPFR ~50 dps when available, else scipy).
    import numpy as np  # noqa: E402
    from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
    from pyhecke.gram import (  # noqa: E402
        TR_M as _TR_M, gram_matrix as _gram_matrix,
        nf_of_word as _nf_of_word, nf_net as _nf_net,
    )

    _t = np.asarray(_TR_M, dtype=float)
    _G = _gram_matrix()
    _b3_nf = _nf_of_word([0, 1, 0, 1, 0, 1])
    _n_target = float(_nf_net(_b3_nf))
    _lp = solve_operator_selection_lp(_t, _G, _n_target)
    _lp_rec = _lp.to_dict()
    # Merge the validator-required dual fields at top level (the
    # lp_dual_witness_validator scans for them there).
    for _k, _v in _lp_rec.items():
        w.add_data(_k, _v)
    w.add_data(
        "lp_instance",
        {
            "basis": ["1", "s0", "s1", "s0*s1", "s1*s0", "s0*s1*s0"],
            "t_source": "pyhecke.gram.TR_M (post-be773569 fix)",
            "G_source": "pyhecke.gram.gram_matrix()",
            "n_target_source": "net(NF((s0*s1)^3)) — canonical B3 word",
            "n_target": _n_target,
        },
    )
    _gap = abs(float(_lp_rec.get("duality_gap", float("nan"))))
    w.add_assertion(
        "lp_strong_duality_gap_small",
        computed=1.0 if _gap < 1e-6 else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("Strong duality on the canonical H_3 operator-"
                "selection LP: |primal_obj - dual_obj| < 1e-6 "
                "(prop:operator-selection-lp dual program; solver "
                "lp_dual_solver.solve_operator_selection_lp)."),
    )

    w.save()
