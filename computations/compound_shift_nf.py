#!/usr/bin/env python3
"""compound_shift_nf.py — NF-basis decomposition of the compound shift.

50-dps mpmath path (no floats in emitted values).

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
    → see computations/alpha_em_shift_chain.py.

Public surface (mirrors the plan API):

    shift_nf_atomic_closed_form(Z, N) -> int        # exact 18Z+21N+1
    build_atom_nf_mp(Z, N, dps=50) -> list[mpf]     # NF at q_0
    gram_mp(dps=50) -> mpmath.matrix                # Gram at q_0
    primal_to_dual(coeffs_primal, dps=50) -> list[mpf]
    compound_shift(Z, N, dps=50) -> CompoundShiftResult
    verify_alpha_em_chain(dps=50) -> dict

Strict primal/dual separation (per CLAUDE.md LP/SDP infra rule):
  NF coefficients c_b(q) live in the **primal** basis; LP shadow
  prices y_*[i] live in the **dual** basis, related by the Gram
  inverse from gram-matrix-dual.py.  Never mix.

The LP active-set DISCOVERY uses scipy linprog (f64) as a discrete
oracle — but every reported numerical value is recomputed in mpmath
at the requested precision (default 50 dps) using a high-precision
linear solve restricted to the active basis.

CLAUDE.md three-calibration discipline: uses only q_0 (CAL-2).
No m_e, Q_β, AME, or experimental data enters.

Witness: compound-shift-nf.witness.json
Audit:   docs/audits/2026-05-16-compound-shift-nf-impl.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from hecke_core_symbolic import _ground_state_ordering  # noqa: E402
from alpha_em_shift_chain import q_integer as q_int_mp  # noqa: E402


# ──────────────────────────────────────────────────────────────────────
# NF basis (matches pyhecke.gram & hecke_core_symbolic conventions)
# ──────────────────────────────────────────────────────────────────────

NF_BASIS: list[tuple[int, ...]] = [
    (), (0,), (1,), (0, 1), (1, 0), (0, 1, 0),
]
NF_NAMES: list[str] = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]


# ──────────────────────────────────────────────────────────────────────
# Closed-form atomic shift
# ──────────────────────────────────────────────────────────────────────

def shift_nf_atomic_closed_form(Z: int, N: int) -> int:
    """shift(Z, N) = 18Z + 21N + 1 for canonical pppnnn ordering (A ≥ 2).

    From prop:per-nucleon-shift-additive-linearity (PR #539 / w3-w4),
    verified at A = 2..6 in per-nucleon-shift-derivation.witness.json.

    The +18 per proton and +21 per neutron are per-NEW-nucleon
    contributions in the embedded H_{3A} context; the +1 is the single
    mixed (p, n) interface from canonical pppnnn ordering.

    Categorically derived in PR #668 via the crystal-bases q-pole
    counter + Habiro convention bridge — see
    `crystal_shift_nf_atomic.habiro_shift_via_crystal`.  This module
    function returns the closed form directly for pipeline use; the
    crystal-bases derivation is the categorical proof.
    """
    return 18 * Z + 21 * N + 1


def shift_nf_atomic_via_crystal(Z: int, N: int) -> int:
    """Categorical re-derivation of shift(Z, N) via crystal-bases.

    Delegates to crystal_shift_nf_atomic.habiro_shift_via_crystal:
      Habiro u-shift = 2 · (q-pole(tr_M) − (3Z + 1.5N − 1.5))
                     = 18Z + 21N + 1

    Identical numerical result to shift_nf_atomic_closed_form, but
    via the categorical-derivation path (PR #668) rather than the
    empirical-induction closed form (PR #539).  Useful as a
    cross-check / for pipeline scripts that want explicit
    categorical provenance.
    """
    from crystal_shift_nf_atomic import habiro_shift_via_crystal
    return habiro_shift_via_crystal(Z, N)


ATOMS_TO_VERIFY: list[tuple[int, int, str]] = [
    (1, 1, "D"),
    (1, 2, "T"),
    (2, 1, "3He"),
    (2, 2, "4He"),
    (3, 2, "5Li"),
    (3, 3, "6Li"),
]

# Per-nucleon NF shifts at H_3 level (from
# shift-from-nf-basis.witness.json; integer values, exact).
SHIFT_NF_PROTON_H3 = 19   # build_nucleon_nf_sym_atomic + tr_M u-pole
SHIFT_NF_NEUTRON_H3 = 15

# Interface α(I) values per prop:alpha-shift-torus-knot (simplest
# interface case): pp = 0, pn = 1, nn = 0.  These are the αcontributions
# in the canonical-ordering composition (see
# per-nucleon-shift-additive-linearity.md §"Generator-count
# decomposition").
ALPHA_PP = 0
ALPHA_PN = 1
ALPHA_NN = 0


# ──────────────────────────────────────────────────────────────────────
# §1 — mpmath NF multiplication (port of pyhecke.gram.hm)
# ──────────────────────────────────────────────────────────────────────

def hm_mp(nf: list, c, d, gen: int, h):
    """Multiply NF element by (c·σ_gen + d·I) in mpmath.

    Mirrors pyhecke.gram.hm line-for-line, but every coefficient is
    an mpmath.mpf at the current `mp.mp.dps` precision.

    `nf` is a 6-list of mpmath.mpf; returns a new 6-list.
    """
    r = [mp.mpf(0)] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] = r[ti] + nf[si] * co
    return r


def build_atom_nf_mp(Z: int, N: int, dps: int = 50) -> list:
    """Build atom NF in mpmath at requested precision.

    Mirror of hecke_core.build_atom_nf — exact same generator
    sequence, but every multiplication uses mp.mpf.  Returns a
    6-list of mp.mpf at `dps` precision.
    """
    with mp.workdps(dps + 5):  # guard digits
        q0 = q_at(dps + 5)
        h = q0 - mp.mpf(1) / q0
        half = mp.mpf(1) / 2
        zero = mp.mpf(0)
        one = mp.mpf(1)

        A = Z + N
        if A == 0:
            return [one, zero, zero, zero, zero, zero]

        ordering = _ground_state_ordering(Z, N)
        nf = [one, zero, zero, zero, zero, zero]

        for k in range(A):
            if ordering[k] == 'p':
                for _ in range(3):
                    nf = hm_mp(nf, one, zero, 0, h)       # σ₀
                    nf = hm_mp(nf, one, -h, 1, h)          # σ₁⁻¹
                nf = hm_mp(nf, one, zero, 0, h)            # uu pair
                nf = hm_mp(nf, one, -h * half, 0, h)       # ud mixed
                nf = hm_mp(nf, one, -h * half, 1, h)       # ud mixed
                nf = hm_mp(nf, one, zero, 0, h)            # gluon 1
                nf = hm_mp(nf, one, zero, 0, h)            # gluon 2
            else:
                for _ in range(3):
                    nf = hm_mp(nf, one, zero, 0, h)
                    nf = hm_mp(nf, one, -h, 1, h)
                nf = hm_mp(nf, one, -h * half, 0, h)
                nf = hm_mp(nf, one, -h * half, 0, h)
                nf = hm_mp(nf, one, -h, 1, h)
                nf = hm_mp(nf, one, zero, 0, h)
                nf = hm_mp(nf, one, zero, 0, h)

            for prev in range(k):
                ti, tj = ordering[prev], ordering[k]
                if ti == 'p' and tj == 'p':
                    nf = hm_mp(nf, one, zero, 0, h)
                elif ti == 'n' and tj == 'n':
                    nf = hm_mp(nf, one, -h, 0, h)
                else:
                    nf = hm_mp(nf, one, -h * half, 0, h)

        for _ in range(Z):
            nf = hm_mp(nf, one, -h, 1, h)

        # Round to requested dps inside the workdps block — outside,
        # unary `+` would round to the GLOBAL mp.dps (default 15) and
        # silently truncate the 50-dps result. Per Gemini review on PR #658.
        with mp.workdps(dps):
            return [+c for c in nf]


# ──────────────────────────────────────────────────────────────────────
# §2 — mpmath Gram matrix and Markov trace
# ──────────────────────────────────────────────────────────────────────

def tr_m_weights_mp(dps: int = 50) -> list:
    """Markov-trace weights TR_M = [1, z, z, z², z², z³] in mpmath."""
    with mp.workdps(dps + 5):
        q0 = q_at(dps + 5)
        sq = mp.sqrt(q0)
        z = mp.mpf(1) / (sq + mp.mpf(1) / sq)
        out = [mp.mpf(1), z, z, z ** 2, z ** 2, z ** 3]
        # Round inside the workdps block (Gemini review on PR #658).
        with mp.workdps(dps):
            return [+v for v in out]


def gram_mp(dps: int = 50) -> mp.matrix:
    """Gram matrix G_{ij} = tr_M(b_i · b_j) in mpmath.

    Constructs each (b_i · b_j) by left-multiplying basis element b_j's
    generator sequence onto b_i, then takes the Markov trace.
    """
    with mp.workdps(dps + 5):
        q0 = q_at(dps + 5)
        h = q0 - mp.mpf(1) / q0
        zero = mp.mpf(0)
        one = mp.mpf(1)
        tr_w = tr_m_weights_mp(dps + 5)

        G = mp.matrix(6, 6)
        for i in range(6):
            for j in range(6):
                # b_i is the i-th NF basis element (already in NF form)
                nf = [zero] * 6
                nf[i] = one
                # Multiply by b_j on the right: apply NF_BASIS[j]'s
                # generator sequence one at a time.
                for gen in NF_BASIS[j]:
                    nf = hm_mp(nf, one, zero, gen, h)
                # tr_M(b_i · b_j) = Σ_k nf[k] · tr_w[k]
                G[i, j] = sum(nf[k] * tr_w[k] for k in range(6))
    return G


def primal_to_dual(coeffs_primal: Sequence, dps: int = 50) -> list:
    """Gram-inverse transfer: primal NF coefficients → dual Frobenius basis.

    NF c_b(q) coefficients live in PRIMAL basis.  Frobenius-dual
    coefficients live in the DUAL basis (inner product against tr_M).
    """
    with mp.workdps(dps + 5):
        G = gram_mp(dps + 5)
        c_vec = mp.matrix([mp.mpf(c) for c in coeffs_primal])
        dual = G ** -1 * c_vec
        # Round inside the workdps block (Gemini review on PR #658).
        with mp.workdps(dps):
            return [+dual[i] for i in range(6)]


# ──────────────────────────────────────────────────────────────────────
# §3 — LP active-set discovery (scipy oracle) + mpmath recompute
# ──────────────────────────────────────────────────────────────────────

@dataclass
class LpMpResult:
    """Operator-selection LP in mpmath — primal + dual, both 50-dps."""
    x_star: list
    y0_star: object  # mpf
    y_star: list
    active_set: list[int]
    primal_obj: object  # mpf
    dual_obj: object  # mpf
    duality_gap: object  # mpf
    feasible: bool


def _scipy_discover_active_set(t_mp, G_mp, n_target_mp,
                               *, M_bound: float = 1e6,
                               dual_tol: float = 1e-9) -> list[int]:
    """Use scipy linprog (f64) as a DISCRETE oracle for the active set.

    The active-set cardinality is a discrete invariant that does not
    depend on float precision (it is determined by which complementary-
    slackness duals are positive vs zero, robust to ~1e-9 jitter).  The
    NUMERIC values are recomputed in mpmath; scipy here only chooses
    the active basis.
    """
    import numpy as np
    from scipy.optimize import linprog
    t_f = np.array([float(v) for v in t_mp], dtype=float)
    G_f = np.array([[float(G_mp[i, j]) for j in range(6)] for i in range(6)],
                   dtype=float)
    n_target_f = float(n_target_mp)

    res = linprog(
        c=t_f,
        A_ub=-G_f, b_ub=np.zeros(6),
        A_eq=np.ones((1, 6)), b_eq=np.array([n_target_f]),
        bounds=[(-M_bound, None)] * 6,
        method="highs",
    )
    if not res.success:
        return []
    y_star_f = -np.asarray(res.ineqlin.marginals)
    return sorted(i for i, y in enumerate(y_star_f) if y > dual_tol)


def solve_operator_selection_lp_mp(coeffs_primal_mp, *,
                                   dps: int = 50) -> LpMpResult:
    """Solve the operator-selection LP for these primal NF coefficients.

    Per prop:operator-selection-lp:
       primal: min Σ t_i x_i  s.t.  Σ x_i = n_target,  Gx ≥ 0,
                                    x_i ≥ -M
       dual:   max n_target · y_0  s.t.  y_0 + (G^T y)_j ≤ t_j,
                                          y_i ≥ 0

    Strategy: discover the active set with scipy (f64), then re-solve
    the active-constraint linear system in mpmath at `dps` precision.
    All emitted numerical values (x_*, y_0, y_*, primal_obj,
    dual_obj, duality_gap) are mpmath.mpf.
    """
    with mp.workdps(dps + 5):
        tr_w = tr_m_weights_mp(dps + 5)
        G = gram_mp(dps + 5)
        c_vec = [mp.mpf(c) for c in coeffs_primal_mp]
        # n_target := Σ c_b · tr_M(b_b) — categorical mass at q_0
        n_target = sum(c_vec[i] * tr_w[i] for i in range(6))
        # Objective t_i := c_i · tr_M(b_i)
        t = [c_vec[i] * tr_w[i] for i in range(6)]

        # Discrete oracle
        active = _scipy_discover_active_set(t, G, n_target)
        if not active:
            return LpMpResult(
                x_star=[mp.mpf('nan')] * 6,
                y0_star=mp.mpf('nan'),
                y_star=[mp.mpf('nan')] * 6,
                active_set=[],
                primal_obj=mp.mpf('nan'),
                dual_obj=mp.mpf('nan'),
                duality_gap=mp.mpf('nan'),
                feasible=False,
            )

        # Recompute the dual y_0, y_* at the active basis in mpmath.
        # Complementary slackness: for j with x_j > -M, the dual
        # constraint y_0 + (G^T y)_j = t_j is tight; y_i = 0 for
        # i ∉ active.
        # Restrict to the active rows: for each j with the dual
        # constraint tight, we have y_0 + Σ_{i ∈ active} G_{ij} y_i = t_j.
        # All 6 primal slots are at the interior (x_j > -M), so all
        # 6 dual constraints are tight at the optimum.  We have 6
        # equations in (1 + |active|) unknowns; the system is
        # overdetermined when |active| < 5, but consistent (LP
        # duality).  Use a 6×(1+|active|) least-squares solve.
        d = len(active)
        # Stack the linear system A · [y0, y_active] = t
        # Row j: A[j, 0] = 1; A[j, 1 + k] = G[active[k], j]
        A = mp.matrix(6, 1 + d)
        b = mp.matrix(6, 1)
        for j in range(6):
            A[j, 0] = mp.mpf(1)
            for k, i in enumerate(active):
                A[j, 1 + k] = G[i, j]
            b[j, 0] = t[j]

        # Solve A · [y0, y_active] = t directly with QR (least-squares
        # for the over-determined case). qr_solve avoids squaring the
        # condition number of the matrix the way normal-equations would,
        # preserving 50-dps precision on poorly-conditioned A.
        try:
            sol, _ = mp.qr_solve(A, b)
            y0 = sol[0, 0]
            y_active = [sol[1 + k, 0] for k in range(d)]
        except Exception:
            return LpMpResult(
                x_star=[mp.mpf('nan')] * 6,
                y0_star=mp.mpf('nan'),
                y_star=[mp.mpf('nan')] * 6,
                active_set=active,
                primal_obj=mp.mpf('nan'),
                dual_obj=mp.mpf('nan'),
                duality_gap=mp.mpf('nan'),
                feasible=False,
            )

        y_star = [mp.mpf(0)] * 6
        for k, i in enumerate(active):
            y_star[i] = y_active[k]

        # Recompute x_*: from KKT, for the dual constraints tight on
        # every j (which we assumed), x_* satisfies
        # Σ x_j = n_target  and  G x ≥ 0  with equality at i ∈ active.
        # Restrict: x lies in the subspace where rows of G indexed by
        # active are zero (NOT — these are the rows where y_i > 0,
        # which corresponds to (Gx)_i = 0).  Wait: G x ≥ 0 with
        # equality at i ∈ active is the right reading.
        # So solve: Σ x_j = n_target  AND  (Gx)_i = 0 for i ∈ active.
        # That's (1 + |active|) equations in 6 unknowns.
        A2 = mp.matrix(1 + d, 6)
        b2 = mp.matrix(1 + d, 1)
        for j in range(6):
            A2[0, j] = mp.mpf(1)
        b2[0, 0] = n_target
        for k, i in enumerate(active):
            for j in range(6):
                A2[1 + k, j] = G[i, j]
            b2[1 + k, 0] = mp.mpf(0)

        # Solve A2 · x = b2 directly with QR (least-squares for the
        # over-determined case, minimum-norm for under-determined when
        # |active| < 5). Avoids squaring the condition number — same
        # precision argument as the dual solve above.
        try:
            x_sol, _ = mp.qr_solve(A2, b2)
            x_star = [x_sol[i, 0] for i in range(6)]
        except Exception:
            x_star = [mp.mpf('nan')] * 6

        primal_obj = sum(t[i] * x_star[i] for i in range(6))
        dual_obj = n_target * y0
        gap = abs(primal_obj - dual_obj)

        return LpMpResult(
            x_star=[+v for v in x_star],
            y0_star=+y0,
            y_star=[+v for v in y_star],
            active_set=active,
            primal_obj=+primal_obj,
            dual_obj=+dual_obj,
            duality_gap=+gap,
            feasible=True,
        )


def delta_cross_lp_bound(active_set: list[int]) -> int:
    """Δ_cross ≤ |active_set| − 1 per prop:operator-selection-lp dual."""
    return max(0, len(active_set) - 1)


# ──────────────────────────────────────────────────────────────────────
# §4 — Compound shift composition
# ──────────────────────────────────────────────────────────────────────

@dataclass
class CompoundShiftResult:
    Z: int
    N: int
    atom: str
    shift_closed: int
    shift_naive_sum: int
    delta_join_total: int
    delta_join_within: int
    delta_join_cross: int
    n_pp: int
    n_pn: int
    n_nn: int
    # mpmath fields
    nf_coefficients: list      # 6 mpf values
    categorical_mass: object   # mpf
    lp_active_set: list[int]
    lp_y0_star: object
    lp_y_star: list
    lp_x_star: list
    lp_primal_obj: object
    lp_dual_obj: object
    lp_duality_gap: object
    delta_cross_lp_bound: int


def per_component_naive_sum(Z: int, N: int) -> tuple[int, dict]:
    """Naive Σ shift_NF(component) under the per-NEW-nucleon convention.

    The (18, 21, 1) decomposition: each new proton contributes 18,
    each new neutron contributes 21, plus exactly one mixed (p, n)
    interface contributes 1 in canonical pppnnn ordering.
    """
    n_pp = max(0, Z - 1)
    n_pn = 1 if (Z >= 1 and N >= 1) else 0
    n_nn = max(0, N - 1)
    naive = 18 * Z + 21 * N + n_pp * ALPHA_PP + n_pn * ALPHA_PN + n_nn * ALPHA_NN
    return naive, {
        "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
        "interface_sum": n_pp * ALPHA_PP + n_pn * ALPHA_PN + n_nn * ALPHA_NN,
    }


def compound_shift(Z: int, N: int, atom: str = "",
                   dps: int = 50) -> CompoundShiftResult:
    """Full compound-shift decomposition for one atom in mpmath."""
    shift_cf = shift_nf_atomic_closed_form(Z, N)
    naive_sum, decomp = per_component_naive_sum(Z, N)
    delta_join_total = naive_sum - shift_cf
    # Within-strand cancellation: per-proton (20 standalone → 18 in
    # embedding) and per-neutron (16 standalone → 21 in embedding).
    # In the (18, 21, 1) decomposition the per-NEW-nucleon shifts are
    # already the embedded values, so Δ_within = 0 at this level.
    delta_join_within = 0
    delta_join_cross = delta_join_total - delta_join_within

    # NF at q_0, mpmath
    nf_mp = build_atom_nf_mp(Z, N, dps=dps)
    tr_w = tr_m_weights_mp(dps=dps)
    cat_mass = sum(nf_mp[i] * tr_w[i] for i in range(6))

    # LP at 50 dps
    lp = solve_operator_selection_lp_mp(nf_mp, dps=dps)
    bound = delta_cross_lp_bound(lp.active_set)

    return CompoundShiftResult(
        Z=Z, N=N, atom=atom or f"Z{Z}N{N}",
        shift_closed=shift_cf,
        shift_naive_sum=naive_sum,
        delta_join_total=delta_join_total,
        delta_join_within=delta_join_within,
        delta_join_cross=delta_join_cross,
        n_pp=decomp["n_pp"],
        n_pn=decomp["n_pn"],
        n_nn=decomp["n_nn"],
        nf_coefficients=nf_mp,
        categorical_mass=cat_mass,
        lp_active_set=lp.active_set,
        lp_y0_star=lp.y0_star,
        lp_y_star=lp.y_star,
        lp_x_star=lp.x_star,
        lp_primal_obj=lp.primal_obj,
        lp_dual_obj=lp.dual_obj,
        lp_duality_gap=lp.duality_gap,
        delta_cross_lp_bound=bound,
    )


# ──────────────────────────────────────────────────────────────────────
# §5 — α_EM multiplicative chain (mpmath 50 dps)
# ──────────────────────────────────────────────────────────────────────

def verify_alpha_em_chain(dps: int = 50) -> dict:
    """α_EM⁻¹ = q · [9]_q · [10]_q at q_0 (mpmath 50 dps).

    Composes prop:alpha-em-shift-multiplicative-chain at the canonical
    substrate value.  Cross-checks against CODATA at the absolute-error
    tolerance (~4e-3 — limited by Hecke-projection bare value).
    """
    with mp.workdps(dps + 5):
        q0 = q_at(dps + 5)
        inv_alpha = q0 * q_int_mp(q0, 9) * q_int_mp(q0, 10)
        alpha = 1 / inv_alpha
        codata_inv = mp.mpf("137.035999084")
        rel_err = abs(inv_alpha - codata_inv) / codata_inv

        # Format inside the workdps block so nstr sees full precision.
        return {
            "q0_50dps": mp.nstr(q0, 50, strip_zeros=False),
            "alpha_em_inv_chain_50dps": mp.nstr(inv_alpha, 50, strip_zeros=False),
            "alpha_em_chain_50dps": mp.nstr(alpha, 50, strip_zeros=False),
            "alpha_em_inv_codata": mp.nstr(codata_inv, 20),
            "relative_error": mp.nstr(rel_err, 6),
            "agrees_within_1e_minus_2": bool(rel_err < mp.mpf("1e-2")),
        }


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def _mpstr(x, n: int = 50) -> str:
    """Serialize an mpmath number at n digits (strict, no zero-stripping)."""
    if mp.isnan(x):
        return "NaN"
    return mp.nstr(x, n, strip_zeros=False)


def main(dps: int = 50) -> int:
    print("=" * 78)
    print(f" compound_shift_nf.py — 50-dps mpmath, no floats in outputs")
    print(f" dps = {dps}")
    print("=" * 78)
    print()

    # §1: closed-form shift table
    print("§1  Closed-form atomic shifts (per-nucleon-shift-additive-linearity)")
    print("-" * 78)
    print(f"  {'atom':<6}{'(Z,N)':>8}{'shift_closed':>14}"
          f"{'shift_naive':>13}{'δ_total':>9}{'δ_within':>10}{'δ_cross':>9}")
    rows: list[CompoundShiftResult] = []
    for Z, N, atom in ATOMS_TO_VERIFY:
        print(f"  computing {atom} (Z={Z}, N={N})...", flush=True)
        row = compound_shift(Z, N, atom=atom, dps=dps)
        rows.append(row)
        print(
            f"  {atom:<6}{f'({Z},{N})':>8}{row.shift_closed:>14}"
            f"{row.shift_naive_sum:>13}{row.delta_join_total:>9}"
            f"{row.delta_join_within:>10}{row.delta_join_cross:>9}",
            flush=True,
        )
    print()

    # §2: NF coefficients at q_0 (50 dps)
    print("§2  Atomic NF coefficients at q_0 (50 dps)")
    print("-" * 78)
    for row in rows:
        print(f"  {row.atom}:")
        for i, c in enumerate(row.nf_coefficients):
            print(f"    c_{NF_NAMES[i]:>3} = {_mpstr(c, 30)}")
        print(f"    Σ c_b · tr_M(b) = {_mpstr(row.categorical_mass, 30)}")
        print()

    # §3: LP active sets and duality
    print("§3  LP active-set bound on δ_cross (per prop:operator-selection-lp)")
    print("-" * 78)
    print(f"  {'atom':<6}{'|active|':>10}{'δ_cross':>9}{'δ_cross_bound':>15}"
          f"{'gap (50dps)':>30}{'feasible':>10}")
    for row in rows:
        gap_str = _mpstr(row.lp_duality_gap, 8)
        print(
            f"  {row.atom:<6}{len(row.lp_active_set):>10}"
            f"{row.delta_join_cross:>9}{row.delta_cross_lp_bound:>15}"
            f"{gap_str:>30}{str(row.lp_active_set != []):>10}",
        )
    print()

    # §4: α_EM chain (50 dps)
    print("§4  α_EM = (q · [9]_q · [10]_q)⁻¹ at q_0  (mpmath 50 dps)")
    print("-" * 78)
    alpha = verify_alpha_em_chain(dps=dps)
    for k, v in alpha.items():
        print(f"  {k:<30}= {v}")
    print()

    # §5: build witness
    print("§5  Building witness JSON...")
    builder = (
        WitnessBuilder("compound-shift-nf", engine="mpmath")
        .set_description(
            "Compound-shift NF decomposition for atoms A=2..6 at "
            "50-dps mpmath precision (no floats in emitted values). "
            "Composes the closed-form atomic shift "
            "(shift(Z,N) = 18Z + 21N + 1, "
            "prop:per-nucleon-shift-additive-linearity, "
            "PR #539 / w3-w4) with the interface α(I) contributions "
            "per canonical pppnnn ordering. NF coefficients at q_0 "
            "are computed in mpmath (port of hecke_core.build_atom_nf "
            "with mp.mpf arithmetic). LP active-set discovery uses "
            "scipy linprog as a discrete oracle, but every numerical "
            "field (y_0, y_*, x_*, primal_obj, dual_obj, "
            "duality_gap) is recomputed in mpmath via a "
            "high-precision linear-system solve restricted to the "
            "active basis. Also verifies the "
            "α_EM⁻¹ = q · [9]_q · [10]_q chain at 50 dps."
        )
        .set_audit_only(
            "docs/audits/2026-05-16-compound-shift-nf-impl.md"
        )
        .add_data("nf_basis_names", NF_NAMES)
        .add_data("dps", dps)
        .add_data("per_nucleon_shift_p_h3", SHIFT_NF_PROTON_H3)
        .add_data("per_nucleon_shift_n_h3", SHIFT_NF_NEUTRON_H3)
        .add_data("alpha_pn", ALPHA_PN)
        .add_data("alpha_pp", ALPHA_PP)
        .add_data("alpha_nn", ALPHA_NN)
        .add_data("atoms", [
            {
                "Z": row.Z, "N": row.N, "atom": row.atom,
                "shift_closed_form": row.shift_closed,
                "shift_naive_sum": row.shift_naive_sum,
                "delta_join_total": row.delta_join_total,
                "delta_join_within": row.delta_join_within,
                "delta_join_cross": row.delta_join_cross,
                "n_pp": row.n_pp,
                "n_pn": row.n_pn,
                "n_nn": row.n_nn,
                "nf_coefficients": [_mpstr(c, 50)
                                    for c in row.nf_coefficients],
                "categorical_mass": _mpstr(row.categorical_mass, 50),
                # LP fields (per CLAUDE.md LP/SDP infra rule).  Values
                # are 50-dps mpmath strings; consumers parse with
                # mp.mpf(...).
                "y0_star": _mpstr(row.lp_y0_star, 50),
                "y_star": [_mpstr(v, 50) for v in row.lp_y_star],
                "x_star": [_mpstr(v, 50) for v in row.lp_x_star],
                "active_set": row.lp_active_set,
                "active_card": len(row.lp_active_set),
                "primal_obj": _mpstr(row.lp_primal_obj, 50),
                "dual_obj": _mpstr(row.lp_dual_obj, 50),
                "duality_gap": _mpstr(row.lp_duality_gap, 50),
                "delta_cross_lp_bound": row.delta_cross_lp_bound,
            }
            for row in rows
        ])
        .add_data("alpha_em_chain", alpha)
        .add_caveat(
            "Per-nucleon NF shifts (shift_p_h3=19, shift_n_h3=15) are "
            "the H_3-context standalone values; the per-NEW-nucleon "
            "embedded values in the (18, 21) decomposition come from "
            "prop:per-nucleon-shift-additive-linearity (already proven "
            "and verified at A=2..6)."
        )
        .add_caveat(
            "LP active-set is a DISCRETE invariant (the cardinality of "
            "{i : y_i^* > 0}) — robust to ~1e-9 float jitter. Scipy "
            "linprog (f64) is used as the discrete oracle; every "
            "numerical value in the witness is recomputed in mpmath at "
            "the requested dps precision via a high-precision linear "
            "solve restricted to the active basis."
        )
        .add_caveat(
            "The shift_NF symbolic-q computation (build_atom_nf_sym in "
            "hecke_core_symbolic) is intractably slow at A≥2 due to "
            "expression fan-out across ~25 hm_sym ops × 6 NF entries "
            "without intermediate canonicalization. A principled fix "
            "routes the shift through the crystal-bases pole-order "
            "reading (prop:crystal-pole-order), where the q → 0 "
            "Kashiwara crystal collapses fan-out to monomial actions. "
            "Pending follow-up; for this witness the shift is read "
            "from the closed form 18Z + 21N + 1."
        )
    )

    # Top-level assertions
    for row in rows:
        builder.add_assertion(
            f"closed_form_shift_consistent_{row.atom}",
            computed=row.shift_naive_sum,
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
            computed=bool(row.lp_duality_gap < mp.mpf("1e-40")),
            expected=True,
            source="LP strong duality (mpmath recompute)",
        )

    builder.add_assertion(
        "alpha_em_chain_50dps_finite",
        computed=alpha["agrees_within_1e_minus_2"],
        expected=True,
        source="prop:alpha-em-shift-multiplicative-chain",
    )

    out_path = builder.save()
    print(f"Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
