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

Precision (NO-FLOAT64, owner directive 2026-08-18): every quantity is an
mpmath mpf at COMPUTE_DPS = 70 from the proton q_0 = q_at(70); the H_3
LP instance is passed to the clarabel-MPFR solver as decimal strings
(gram_matrix_mp_strings / tr_m_mp_strings); witness values are
serialised with _precision.fmt. Until 2026-11-20 the accumulators were
float literals, h/q0/qi were the float64 hecke_core constants, the LP
inputs were np.asarray(dtype=float) and every witness value went through
float() (QA re-adjudication 2026-11-20).

# Ref: [leitner2026] folio/quantum-observable-universe/mass-theory/knot-operator-lp-selection.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import hecke_core  # noqa: E402, F401  (bootstrap: puts pyhecke on sys.path)

# LP-dual emission deps (witness __main__ path). Imported at module
# level right after the sys.path setup per repo import convention —
# hecke_core's own bootstrap has already put pyhecke on sys.path.
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import q_at  # noqa: E402  (proton pin)
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from pyhecke.atom import nucleon_gen_chains  # noqa: E402
from pyhecke.gram import (  # noqa: E402
    gram_matrix_mp_strings as _gram_matrix_mp_strings,
    tr_m_mp_strings as _tr_m_mp_strings,
    _nf_of_word_mp, nf_net as _nf_net,
)

COMPUTE_DPS = 70

# All module-level constants are built inside ONE precision context: an
# mpf carries the precision of the operation that created it.
with mp.workdps(COMPUTE_DPS):
    q0 = mp.mpf(q_at(COMPUTE_DPS))
    qi = 1 / q0
    h = q0 - qi
    _PROTON_G0, _PROTON_G1 = nucleon_gen_chains(['u', 'u', 'd'], q=q0)
    _NEUTRON_G0, _NEUTRON_G1 = nucleon_gen_chains(['u', 'd', 'd'], q=q0)


def q_int(n: int) -> mp.mpf:
    """[n]_q = (q^n - q^-n)/(q - q^-1) at the module q_0, COMPUTE_DPS."""
    with mp.workdps(COMPUTE_DPS):
        return (q0 ** n - qi ** n) / h

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402


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

    # Per-generator 2x2 matrix accumulators (initialise to identity), mpf.
    one, zero = mp.mpf(1), mp.mpf(0)
    m11 = [one] * n_gens_total
    m12 = [zero] * n_gens_total
    m21 = [zero] * n_gens_total
    m22 = [one] * n_gens_total
    sp_arr = [one] * n_gens_total  # λ^sym
    ap_arr = [one] * n_gens_total  # λ^alt

    def apply_crossing(i: int, c, d) -> None:
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
                base_cross = (one, zero)
                m_this = m_pp if m_pp is not None else crossings_per_pair
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (one, -h)
                m_this = m_nn if m_nn is not None else crossings_per_pair
            else:
                base_cross = (one, _pn_d(h))
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
    with mp.workdps(COMPUTE_DPS):
        return _wedderburn_pair_volumes(
            Z, N, include_inter=include_inter,
            crossings_per_pair=crossings_per_pair,
            m_pp=m_pp, m_nn=m_nn, m_pn=m_pn)


def _wedderburn_pair_volumes(
    Z: int, N: int, *, include_inter: bool,
    crossings_per_pair: int, m_pp, m_pn, m_nn,
) -> list[dict]:
    mats = atom_per_generator_full_matrices(
        Z, N,
        include_inter=include_inter,
        crossings_per_pair=crossings_per_pair,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
    )

    # H_3 Wedderburn weights (match hecke_core convention)
    z_mark = q0**3 / (q0**2 + 1)
    qdim_sym = mp.mpf(1)
    qdim_std = q_int(2)
    qdim_alt = mp.mpf(1)
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
    # Script entry only: raise the global precision before any mpf below.
    set_compute_dps(COMPUTE_DPS)
    # Quick sanity check
    print("Wedderburn pair volumes — quick test (deuteron Z=1, N=1):")
    pairs = wedderburn_pair_volumes(1, 1)
    n = len(pairs)
    print(f"  n_pairs = {n}")
    print(f"  first 3 pairs:")
    for p in pairs[:3]:
        # mp.nstr, not an f-string :.4f -- these are mpmath.mpf and mpf has no
        # __format__ for the float presentation types, so `:.4f` raises
        # TypeError. AGENTS.md permits float(x) only inside an f-string for
        # display and prefers mp.nstr; this is display, so mp.nstr it is.
        print(f"    ({p['i']}, {p['j']}): "
              f"sym={mp.nstr(p['sym'], 5)}  std={mp.nstr(p['std'], 5)}  "
              f"alt={mp.nstr(p['alt'], 5)}  full={mp.nstr(p['full'], 5)}")

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
    # Serialise at OUTPUT_DPS via fmt (no float()).
    w.add_data(
        "pairs",
        [
            {
                "i": p["i"],
                "j": p["j"],
                "sym": fmt(p["sym"]),
                "std": fmt(p["std"]),
                "alt": fmt(p["alt"]),
                "full": fmt(p["full"]),
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
    all_full_finite = all(mp.isfinite(p["full"]) for p in pairs)
    w.add_assertion(
        "wedderburn_full_pair_volumes_finite",
        computed=1 if all_full_finite else 0,
        expected=1,
        tolerance=0,
        source="prop:knot-operator-lp-selection",
    )

    # ── Canonical LP-dual record ─────────────────────────────────
    # Per AGENTS.md §"LP / SDP duals — first-class infra": every
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
    # (imports live at module level, after the sys.path setup)

    # Decimal strings in, so the MPFR solver never sees a float64.
    _LP_DPS = 50  # the clarabel-MPFR solve runs at prec_bits=167 ~ 50 dps
    _t = _tr_m_mp_strings(_LP_DPS + 5)
    _G = _gram_matrix_mp_strings(_LP_DPS + 5)
    with mp.workdps(COMPUTE_DPS):
        _b3_nf = _nf_of_word_mp([0, 1, 0, 1, 0, 1], h)
        _n_target_mp = _nf_net(_b3_nf)
    _n_target = mp.nstr(_n_target_mp, _LP_DPS)
    # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
    # whether the Rust binary happens to be built, so the same script
    # yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
    # makes a missing binary an error rather than a changed answer.
    # Bean `qou/ftuv`.
    _lp = solve_operator_selection_lp(_t, _G, _n_target, backend="clarabel")
    _lp_rec = _lp.to_dict()
    # Merge the validator-required dual fields at top level (the
    # lp_dual_witness_validator scans for them there).
    # `to_dict()` keeps the f64 fields for its arithmetic consumers and adds
    # the full-precision `*_str` companions from the MPFR solve. This
    # witness has no arithmetic consumer, so the base field carries the
    # full-precision decimal and no float64 enters the witness.
    for _k, _v in _lp_rec.items():
        w.add_data(_k, _v if _k.endswith("_str") else _lp_rec.get(_k + "_str", _v))
    w.add_data(
        "lp_instance",
        {
            "basis": ["1", "s0", "s1", "s0*s1", "s1*s0", "s0*s1*s0"],
            "t_source": "pyhecke.gram.tr_m_mp_strings (mpmath, no float64)",
            "G_source": "pyhecke.gram.gram_matrix_mp_strings (mpmath, no float64)",
            "n_target_source": "net(NF((s0*s1)^3)) — canonical B3 word, mpmath",
            "n_target": fmt(_n_target_mp),
        },
    )
    _gap_raw = _lp_rec.get("duality_gap_str", _lp_rec.get("duality_gap"))
    _gap = abs(mp.mpf(str(_gap_raw))) if _gap_raw is not None else mp.inf
    w.add_assertion(
        "lp_strong_duality_gap_small",
        computed=1 if _gap < mp.mpf("1e-6") else 0,
        expected=1,
        tolerance=0,
        source=("Strong duality on the canonical H_3 operator-"
                "selection LP: |primal_obj - dual_obj| < 1e-6 "
                "(prop:operator-selection-lp dual program; solver "
                "lp_dual_solver.solve_operator_selection_lp)."),
    )

    w.save()
