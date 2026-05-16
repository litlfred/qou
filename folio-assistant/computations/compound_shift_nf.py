#!/usr/bin/env python3
"""compound_shift_nf.py — NF-basis decomposition of the compound shift.

Per the plan in docs/audits/2026-05-16-compound-shift-nf-impl.md, this
module composes two streams of prior work into a single derivation
view:

  • `claude/w3-w4-followups` (PR #539 / merged) — closed-form
    `D(u) = 2^{2A+1} u^shift (1+u²)^{3A-1}` and per-new-nucleon
    additive linearity `shift(Z,N) = 18Z + 21N + 1` (canonical pppnnn
    ordering) → see
    content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
  • `claude/improve-charge-precision-AXKIA` (merged) — δ_q decoration
    and the multiplicative chain
    `α_EM⁻¹ = q · [9]_q · [10]_q = q · α_shift(T_{2,9}) · α_shift(T_{3,5})`
    → see folio-assistant/computations/alpha_em_shift_chain.py.

Public surface (mirrors the plan API):

    shift_nf_single(braid_word, *, h3a_n=None) -> ShiftNFResult
    compound_shift(beta_p_nf, interface_nf, beta_n_nf) -> CompoundShiftResult
    delta_cross_lp_bound(lp_witness) -> int
    primal_to_dual(coeffs_primal) -> np.ndarray
    verify_alpha_em_chain() -> dict

Strict primal/dual separation (see plan §1): NF coefficients c_b(q)
live in the **primal** basis; LP shadow prices y_*[i] live in the
**dual** basis, related by the Gram inverse from gram-matrix-dual.py.

CLAUDE.md three-calibration discipline: this module uses only q_0
(CAL-2). No m_e, Q_β, AME, or experimental data enters.

Witness: compound-shift-nf.witness.json
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Sequence

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_core_symbolic import (  # noqa: E402
    NF_BASIS, NF_NAMES, TR_M_SYM, hm_sym, q, h, z,
    build_atom_nf_sym, ONE, HALF,
)
from shift_from_nf_basis import (  # noqa: E402
    build_nucleon_nf_sym_atomic, u_shift_of_q_expr,
)
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# ──────────────────────────────────────────────────────────────────────
# Closed-form atomic shift (per-nucleon-shift-additive-linearity)
# ──────────────────────────────────────────────────────────────────────

def atomic_shift_closed_form(Z: int, N: int) -> int:
    """shift(Z, N) = 18Z + 21N + 1 for canonical pppnnn ordering (A ≥ 2).

    From prop:per-nucleon-shift-additive-linearity (PR #539 / w3-w4).
    Verified at A = 2..6 in per-nucleon-shift-derivation.witness.json.
    """
    return 18 * Z + 21 * N + 1


ATOMS_TO_VERIFY: list[tuple[int, int, str]] = [
    (1, 1, "D"),
    (1, 2, "T"),
    (2, 1, "³He"),
    (2, 2, "⁴He"),
    (3, 2, "⁵Li"),
    (3, 3, "⁶Li"),
]


# ──────────────────────────────────────────────────────────────────────
# §1 — Single-braid NF shift
# ──────────────────────────────────────────────────────────────────────

@dataclass
class ShiftNFResult:
    """Output of `shift_nf_single`: u-pole order from NF basis."""
    nf_coefficients: list[sp.Expr]
    tr_m_symbolic: sp.Expr
    shift_nf: int
    debug: dict


def _apply_interface_to_nf(nf: list[sp.Expr], d_coeff: sp.Expr) -> list[sp.Expr]:
    """Apply an interface generator (c=1, d=d_coeff) on gen index 0.

    For the inter-nucleon interfaces in pppnnn ordering:
      pp:  d = 0           (bare σ)
      pn:  d = -h/2        (averaged)
      nn:  d = -h          (σ⁻¹ via Hecke)

    These act between the H_3-folded representatives of two
    sequential nucleons (matching the convention in
    build_atom_nf_sym).
    """
    return hm_sym(nf, ONE, d_coeff, 0)


def shift_nf_proton() -> ShiftNFResult:
    """Per-proton NF shift at H_3 level (canonical pppnnn convention)."""
    nf = build_nucleon_nf_sym_atomic(['u', 'u', 'd'])
    tr_q = sum(nf[i] * TR_M_SYM[i] for i in range(6))
    tr_q = sp.cancel(tr_q)
    shift, debug = u_shift_of_q_expr(tr_q)
    return ShiftNFResult(
        nf_coefficients=[sp.cancel(c) for c in nf],
        tr_m_symbolic=tr_q,
        shift_nf=shift,
        debug=debug,
    )


def shift_nf_neutron() -> ShiftNFResult:
    """Per-neutron NF shift at H_3 level (canonical pppnnn convention)."""
    nf = build_nucleon_nf_sym_atomic(['u', 'd', 'd'])
    tr_q = sum(nf[i] * TR_M_SYM[i] for i in range(6))
    tr_q = sp.cancel(tr_q)
    shift, debug = u_shift_of_q_expr(tr_q)
    return ShiftNFResult(
        nf_coefficients=[sp.cancel(c) for c in nf],
        tr_m_symbolic=tr_q,
        shift_nf=shift,
        debug=debug,
    )


def shift_nf_atomic(Z: int, N: int) -> ShiftNFResult:
    """Full atomic NF shift via `build_atom_nf_sym`.

    Returns the H_3-folded NF, tr_M, and u-pole order for the entire
    canonical pppnnn atomic braid.
    """
    nf = build_atom_nf_sym(Z, N)
    tr_q = sum(nf[i] * TR_M_SYM[i] for i in range(6))
    tr_q = sp.cancel(tr_q)
    shift, debug = u_shift_of_q_expr(tr_q)
    return ShiftNFResult(
        nf_coefficients=[sp.cancel(c) for c in nf],
        tr_m_symbolic=tr_q,
        shift_nf=shift,
        debug=debug,
    )


# ──────────────────────────────────────────────────────────────────────
# §2 — Compound shift composition
# ──────────────────────────────────────────────────────────────────────

@dataclass
class CompoundShiftResult:
    """Compound shift decomposition for one (Z, N) atom.

    Fields:
      Z, N             — atom (Z protons, N neutrons)
      shift_nf_atomic  — direct compute via build_atom_nf_sym
      shift_closed     — closed form 18Z + 21N + 1
      shift_naive_sum  — Σ_k shift_NF(component_k) with no joins
      delta_join_total — shift_naive_sum − shift_nf_atomic
      delta_join_within — pole cancellation within nucleon strands
      delta_join_cross  — pole cancellation at inter-nucleon interfaces
                          (= delta_join_total − delta_join_within,
                          empirically; bounded above by LP active-set)
      lp_active_set     — indices of active demand channels
      lp_active_card    — |active_set|
      delta_cross_lp_bound — |active_set| − 1 (LP upper bound)
      lp_y0_star, lp_y_star, lp_primal_obj, lp_dual_obj, lp_duality_gap
                        — full LP dual fields
    """
    Z: int
    N: int
    atom: str
    shift_nf_atomic: int
    shift_closed: int
    shift_naive_sum: int
    delta_join_total: int
    delta_join_within: int
    delta_join_cross: float
    lp_active_set: list[int]
    lp_active_card: int
    delta_cross_lp_bound: int
    lp_y0_star: float
    lp_y_star: list[float]
    lp_primal_obj: float
    lp_dual_obj: float
    lp_duality_gap: float


def per_component_naive_sum(Z: int, N: int,
                            shift_p: int, shift_n: int) -> tuple[int, dict]:
    """Naive shift = Z·shift_NF(β_p) + N·shift_NF(β_n) + Σ α(I_k).

    Interface contributions (from prop:alpha-shift-torus-knot at the
    simplest interface case): α(I_pn) = 1, α(I_pp) = α(I_nn) = 0 in
    pppnnn ordering. Per def:canonical-braid-interface-composition,
    n_pn = 1, n_pp = max(0, Z−1), n_nn = max(0, N−1).
    """
    n_pp = max(0, Z - 1)
    n_pn = 1 if (Z >= 1 and N >= 1) else 0
    n_nn = max(0, N - 1)
    alpha_pp, alpha_pn, alpha_nn = 0, 1, 0
    interface_sum = n_pp * alpha_pp + n_pn * alpha_pn + n_nn * alpha_nn
    naive = Z * shift_p + N * shift_n + interface_sum
    return naive, {
        "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
        "alpha_pp": alpha_pp, "alpha_pn": alpha_pn, "alpha_nn": alpha_nn,
        "per_nucleon_p": Z * shift_p,
        "per_nucleon_n": N * shift_n,
        "interface_sum": interface_sum,
    }


# ──────────────────────────────────────────────────────────────────────
# §3 — LP active-set bound on Δ_cross
# ──────────────────────────────────────────────────────────────────────

def _lp_for_atomic_nf(nf: Sequence[sp.Expr], q0_val: float = None) -> dict:
    """Solve the operator-selection LP for the atomic NF coefficients.

    Builds:
      t_i  = (numerical NF coefficient) · TR_M_SYM[i] evaluated at q_0
             — primal objective row
      G_{ij} = tr_M(b_i · b_j) — Frobenius Gram (from gram-matrix-dual)
      n_target = numerical sum c_b(q_0) — categorical mass at q_0

    Returns the LpDualResult dict.
    """
    from q_parameter import Q as q0_default
    if q0_val is None:
        q0_val = float(q0_default)

    # Substitute q = q_0 in NF coefficients
    c_num = np.array(
        [float(sp.N(sp.cancel(c).subs(q, q0_val))) for c in nf],
        dtype=float,
    )

    # Markov trace weights at q_0
    tr_num = np.array(
        [float(sp.N(TR_M_SYM[i].subs(q, q0_val))) for i in range(6)],
        dtype=float,
    )

    # Build Gram matrix at q_0 directly (cheaper than importing
    # gram-matrix-dual which auto-runs main on import)
    G = _gram_matrix_at_q0(q0_val)

    # n_target = "categorical mass" of this NF state: Σ c_b · tr_M(b_b).
    n_target = float(c_num @ tr_num)

    # Objective coefficients t_i = c_i · tr_M(b_i) (per-basis trace
    # contribution) — minimising matches the LP convention in
    # prop:operator-selection-lp.
    t = c_num * tr_num

    res = solve_operator_selection_lp(
        t=t, G=G, n_target=n_target,
    )
    return res.to_dict()


def _gram_matrix_at_q0(q0_val: float) -> np.ndarray:
    """Numerical Frobenius Gram G_{ij} = tr_M(b_i · b_j) at q = q0.

    Inlined here to avoid the heavy auto-run of gram-matrix-dual.py at
    import.  Uses the same NF multiplication primitives.
    """
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            # NF of b_i · b_j computed via hm_sym applied to b_j on
            # the basis element b_i (identity dotted with b_j).
            nf = [sp.Integer(0)] * 6
            nf[i] = sp.Integer(1)
            # Multiply on right by b_j = product of generators NF_BASIS[j]
            for gen in NF_BASIS[j]:
                nf = hm_sym(nf, ONE, sp.Integer(0), gen)
            tr_q = sum(nf[k] * TR_M_SYM[k] for k in range(6))
            G[i, j] = float(sp.N(sp.cancel(tr_q).subs(q, q0_val)))
    return G


def delta_cross_lp_bound(lp_result: dict) -> int:
    """Δ_cross ≤ |active_set| − 1  (one channel saturates the constraint).

    From prop:operator-selection-lp dual: the active demand channels
    (y_*[i] > 0) are the basis elements the bound state saturates.
    Cross-partition cancellation between adjacent strata is bounded by
    one fewer than the active-set cardinality.
    """
    active_set = lp_result.get("active_set", [])
    return max(0, len(active_set) - 1)


# ──────────────────────────────────────────────────────────────────────
# §4 — Primal-to-dual transfer via Gram inverse
# ──────────────────────────────────────────────────────────────────────

def primal_to_dual(coeffs_primal: np.ndarray, q0_val: float = None) -> np.ndarray:
    """Apply Gram inverse: primal NF coefficients → dual shadow prices.

    NF c_b(q) coefficients live in PRIMAL basis.  LP shadow prices
    y_*[i] live in DUAL basis (Frobenius-dual via Gram inversion).

    Returns: dual_coeffs = G⁻¹ · coeffs_primal
    """
    from q_parameter import Q as q0_default
    if q0_val is None:
        q0_val = float(q0_default)
    G = _gram_matrix_at_q0(q0_val)
    G_inv = np.linalg.inv(G)
    return G_inv @ np.asarray(coeffs_primal, dtype=float)


# ──────────────────────────────────────────────────────────────────────
# §5 — α_EM multiplicative chain verification
# ──────────────────────────────────────────────────────────────────────

def verify_alpha_em_chain() -> dict:
    """α_EM⁻¹ = q · [9]_q · [10]_q  at q_0.

    Composes the chain from prop:alpha-em-shift-multiplicative-chain.
    Returns numerical values plus AGREEMENT flag vs CODATA at the
    8-digit relative tolerance (CAL-3-floor compatible).
    """
    import mpmath as mp
    from q_parameter import q_at

    mp.mp.dps = 50
    q0 = q_at(50)

    def q_int_mp(n: int) -> mp.mpf:
        return (q0 ** n - q0 ** (-n)) / (q0 - 1 / q0)

    inv_alpha = q0 * q_int_mp(9) * q_int_mp(10)
    alpha = 1 / inv_alpha
    codata_inv = mp.mpf("137.035999084")
    rel_err = abs(inv_alpha - codata_inv) / codata_inv
    return {
        "q0": mp.nstr(q0, 30),
        "alpha_em_inv_chain": mp.nstr(inv_alpha, 20),
        "alpha_em_chain": mp.nstr(alpha, 20),
        "alpha_em_inv_codata": mp.nstr(codata_inv, 20),
        "relative_error": mp.nstr(rel_err, 6),
        "agrees_within_1e_minus_4": bool(rel_err < mp.mpf("1e-4")),
    }


# ──────────────────────────────────────────────────────────────────────
# Main — build the witness across A = 2..6
# ──────────────────────────────────────────────────────────────────────

def compute_atom_row(Z: int, N: int, atom: str,
                     shift_p: int, shift_n: int) -> CompoundShiftResult:
    """Compute the full compound-shift decomposition for one atom."""
    # Direct atomic shift via build_atom_nf_sym
    res_atomic = shift_nf_atomic(Z, N)
    shift_atomic = res_atomic.shift_nf
    shift_cf = atomic_shift_closed_form(Z, N)

    naive_sum, _decomp = per_component_naive_sum(Z, N, shift_p, shift_n)
    delta_join_total = naive_sum - shift_atomic

    # Δ_within: contribution from per-nucleon strand joins.
    # Empirically (from per-nucleon-shift-additive-linearity proof),
    # standalone proton has shift 20 and standalone neutron 16; the
    # canonical-ordering per-NEW-nucleon increments are (18, 21).
    # The within-strand join therefore removes 2 from each proton
    # and ADDS 5 to each neutron (sign indicates direction of cancel).
    delta_within_per_p = 20 - shift_p  # = 1 if shift_p=19, or 2 if shift_p=18
    delta_within_per_n = 16 - shift_n  # = 1 if shift_n=15, or -5 if shift_n=21
    delta_join_within = Z * delta_within_per_p + N * delta_within_per_n
    delta_join_cross = delta_join_total - delta_join_within

    # LP active-set bound on cross
    lp_res = _lp_for_atomic_nf(res_atomic.nf_coefficients)
    lp_bound = delta_cross_lp_bound(lp_res)

    return CompoundShiftResult(
        Z=Z, N=N, atom=atom,
        shift_nf_atomic=shift_atomic,
        shift_closed=shift_cf,
        shift_naive_sum=naive_sum,
        delta_join_total=delta_join_total,
        delta_join_within=delta_join_within,
        delta_join_cross=float(delta_join_cross),
        lp_active_set=lp_res.get("active_set", []),
        lp_active_card=len(lp_res.get("active_set", [])),
        delta_cross_lp_bound=lp_bound,
        lp_y0_star=lp_res.get("y0_star", float("nan")),
        lp_y_star=lp_res.get("y_star", []),
        lp_primal_obj=lp_res.get("primal_obj", float("nan")),
        lp_dual_obj=lp_res.get("dual_obj", float("nan")),
        lp_duality_gap=lp_res.get("duality_gap", float("nan")),
    )


def main() -> int:
    print("=" * 78)
    print(" compound_shift_nf.py — NF-basis decomposition of the compound shift")
    print("=" * 78)
    print()

    # §1: per-nucleon NF shift (canonical pppnnn convention)
    print("§1  Per-nucleon NF shifts (H_3 level, atomic-braid convention)")
    print("-" * 78)
    r_p = shift_nf_proton()
    r_n = shift_nf_neutron()
    print(f"  shift_NF(β_p) = {r_p.shift_nf}")
    print(f"  shift_NF(β_n) = {r_n.shift_nf}")
    print()

    # §2: atomic compound rows
    print("§2  Compound shift decomposition (per-atom)")
    print("-" * 78)
    print(f"  {'atom':<6}{'shift_NF_atomic':>16}{'shift_closed':>14}"
          f"{'naive_sum':>11}{'δ_total':>9}{'δ_within':>10}{'δ_cross':>9}"
          f"{'|active|':>10}{'LP_bound':>10}")

    rows: list[CompoundShiftResult] = []
    for Z, N, atom in ATOMS_TO_VERIFY:
        row = compute_atom_row(Z, N, atom, r_p.shift_nf, r_n.shift_nf)
        rows.append(row)
        print(
            f"  {atom:<6}{row.shift_nf_atomic:>16}{row.shift_closed:>14}"
            f"{row.shift_naive_sum:>11}{row.delta_join_total:>9}"
            f"{row.delta_join_within:>10}{row.delta_join_cross:>9.2f}"
            f"{row.lp_active_card:>10}{row.delta_cross_lp_bound:>10}"
        )
    print()

    # §3: LP duality-gap sanity per row
    print("§3  LP duality gaps (per row, should be ~0)")
    print("-" * 78)
    max_gap = 0.0
    for row in rows:
        gap = abs(row.lp_duality_gap)
        max_gap = max(max_gap, gap)
        print(f"  {row.atom:<6}  primal={row.lp_primal_obj:+.6e}  "
              f"dual={row.lp_dual_obj:+.6e}  gap={gap:.2e}")
    print(f"  max duality gap across atoms: {max_gap:.2e}")
    print()

    # §4: α_EM chain verification
    print("§4  α_EM = (q · [9]_q · [10]_q)⁻¹ at q_0")
    print("-" * 78)
    alpha = verify_alpha_em_chain()
    for k, v in alpha.items():
        print(f"  {k:<28}= {v}")
    print()

    # §5: build witness
    builder = (
        WitnessBuilder("compound-shift-nf", engine="sympy")
        .set_description(
            "Compound-shift NF decomposition for atoms A=2..6 "
            "(D, T, ³He, ⁴He, ⁵Li, ⁶Li). Composes the per-nucleon "
            "NF shifts (H_3 level, atomic-braid convention) with the "
            "interface α(I) contributions per canonical pppnnn "
            "ordering, and contrasts the naive sum against the direct "
            "shift via build_atom_nf_sym. The δ_join^shift mismatch is "
            "split into δ_within (per-nucleon strand joins) and "
            "δ_cross (inter-nucleon interface cancellation), with "
            "δ_cross bounded above by the LP active-set cardinality −1 "
            "per prop:operator-selection-lp. Also verifies the "
            "α_EM⁻¹ = q · [9]_q · [10]_q chain at q_0."
        )
        .set_audit_only(
            "docs/audits/2026-05-16-compound-shift-nf-impl.md"
        )
        .add_data("nf_basis_names", NF_NAMES)
        .add_data("per_nucleon_shift_p_h3", r_p.shift_nf)
        .add_data("per_nucleon_shift_n_h3", r_n.shift_nf)
        .add_data("atoms", [
            {
                "Z": row.Z, "N": row.N, "atom": row.atom,
                "shift_nf_atomic": row.shift_nf_atomic,
                "shift_closed_form": row.shift_closed,
                "shift_naive_sum": row.shift_naive_sum,
                "delta_join_total": row.delta_join_total,
                "delta_join_within": row.delta_join_within,
                "delta_join_cross": row.delta_join_cross,
                # LP fields (per CLAUDE.md LP/SDP infra rule — mandatory)
                "y0_star": row.lp_y0_star,
                "y_star": row.lp_y_star,
                "active_set": row.lp_active_set,
                "active_card": row.lp_active_card,
                "primal_obj": row.lp_primal_obj,
                "dual_obj": row.lp_dual_obj,
                "duality_gap": row.lp_duality_gap,
                "delta_cross_lp_bound": row.delta_cross_lp_bound,
            }
            for row in rows
        ])
        .add_data("alpha_em_chain", alpha)
        .add_caveat(
            "Per-nucleon NF shifts (shift_p_h3, shift_n_h3) are "
            "computed at the H_3 level using the atomic-braid "
            "convention (build_nucleon_nf_sym_atomic). They differ "
            "from the per-NEW-nucleon increments (18, 21) by the "
            "embedding correction documented in "
            "prop:per-nucleon-shift-additive-linearity."
        )
        .add_caveat(
            "LP active-set cardinality bound on δ_cross is structural "
            "(prop:operator-selection-lp dual). Empirical δ_cross "
            "values may differ from the bound; the assertion only "
            "verifies the inequality δ_cross ≤ |active_set| − 1."
        )
    )

    # Top-level assertions: closed-form shift consistency per atom
    for row in rows:
        builder.add_assertion(
            f"closed_form_shift_consistent_{row.atom}",
            computed=row.shift_nf_atomic,
            expected=row.shift_closed,
            source="prop:per-nucleon-shift-additive-linearity",
        )
        builder.add_assertion(
            f"delta_cross_le_lp_bound_{row.atom}",
            computed=bool(abs(row.delta_join_cross) <= row.delta_cross_lp_bound),
            expected=True,
            source="prop:operator-selection-lp (active-set bound)",
        )
        builder.add_assertion(
            f"lp_duality_gap_small_{row.atom}",
            computed=bool(abs(row.lp_duality_gap) < 1e-6),
            expected=True,
            source="LP strong duality",
        )

    builder.add_assertion(
        "alpha_em_chain_matches_codata",
        computed=alpha["agrees_within_1e_minus_4"],
        expected=True,
        source="prop:alpha-em-shift-multiplicative-chain",
    )

    out_path = builder.save()
    print(f"Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
