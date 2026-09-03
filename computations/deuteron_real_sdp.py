#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output.
"""
Deuteron real per-nucleus SDP — drops the abstract empty-SDP layer.

Per the workplan `docs/workplans/2026-05-31-real-sdp-wiring-per-nucleus.md`
(PR #1575). The existing uniqueness infrastructure
(`QOU.BraidKnot.AppliedDeuteronUniqueness.deuteron_uniqueness_closed`)
certifies T_w uniqueness at the **abstract empty-constraint SDP**
(cost = identity, no constraints, Φ⋆ = 0). That proves the framework
*can* certify uniqueness, but not uniqueness of the *actual* T_w that
consumes the deuteron mass formula.

This script assembles and solves the **real** deuteron SDP at H_6
(n = 3·A = 6, 11 partitions λ ⊢ 6) with a genuine, non-empty cost:

  operators        b_λ := P_λ          (Wedderburn block projectors, λ ⊢ 6)
  cost (Phase A)   t_λ := tr_M(P_λ · β_D) = y_λ(q_0) · χ^λ(β_D)
                                          (per-partition mass-formula summand,
                                           Σ_λ t_λ = tr_M(β_D) ≈ 0.3883)
  Frobenius Gram   G_λμ := tr_M(P_λ P_μ) = δ_λμ · tr_M(P_λ)
                                          = δ_λμ · y_λ · dim S^λ
                                          (diagonal: P_λ are orthogonal
                                           central idempotents)
  net constraint   n_target := tr_M(β_D)  (the total trace the selected
                                           blocks must reproduce)

The solve routes through the canonical dual-emitting entry point
`pyhecke.lp_dual_solver.solve_operator_selection_lp` /
`solve_psd_operator_selection_sdp` (AGENTS.md §LP/SDP duals — first-class
infra). The dual shadow prices `y_star` identify the **active demand
channels** — the Wedderburn blocks the deuteron bound state actually
saturates ("most receptive sub-braids").

Scope of this script (Phase A + Phase C-numeric):
  ✔ Phase A — real cost matrix from the mass-formula witness.
  ✔ Phase C — strong-duality SDP solve with primal + dual + gap.
  ☐ Phase B — color-flavor 9-pair constraints (proton uud × neutron udd)
              as additional Gram rows + AME2020 binding-energy RHS.
              Follow-up commit; see workplan §"Phase B".
  ☐ Phase D — Lean wiring `deuteron_emptySDP → deuteron_realSDP`.
              Follow-up PR; consumes this witness via the axiom bridge.

Input : iterative-lp-dual-h6-deuteron.witness.json  (y_λ, χ^λ(β_D) at q_0)
Output: deuteron-real-sdp.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
import sys

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke" / "python"))

from pyhecke.lp_dual_solver import (  # noqa: E402
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)
from murnaghan_nakayama import dim_specht  # noqa: E402  shared hook-length dim
from nucleus_sdp_assembly import (  # noqa: E402
    build_cost_gram, tr_M_from_cache, solve_real_sdp, solve_real_sdp_arrays,
)

COST_WITNESS = _pb.witness_path("iterative-lp-dual-h6-deuteron.witness.json", HERE)
BRANCHING_WITNESS = _pb.witness_path("sublemma-2-1-deuteron-branching.witness.json", HERE)
OUT_WITNESS = HERE / "deuteron-real-sdp.witness.json"

# The current uniqueness anchor (empty-SDP); the real-SDP Lean theorem is
# the Phase D target.  Cited so this witness is wiring-audited (PR #1572/#1573).
LEAN_UNIQUENESS_REF = "qou:QOU.BraidKnot.deuteron_uniqueness_closed"

# AME2020 deuteron binding energy (MeV) — RHS for the physical constraint.
# Matches the repo-wide constant (probe_k_ud_*, applied_uniqueness_mass_table).
B_D_AME_MeV = 2.22456607
# 9-pair color-flavor structure of p=uud × n=udd: 2·(u,u)+4·(u,d)+1·(d,u)+2·(d,d).
# Neutron-heavy 5:4 weighting with a bar-involution sign flip on the mixed
# (u,d)/(d,u) channel (probe_k_ud_fractional_and_alt_ansatz.nine_pair_ratio).
NINE_PAIR = {"uu": 2, "ud": 4, "du": 1, "dd": 2}  # multiplicities, Σ = 9


def solve_lp_with_eq(t, G, A_eq, b_eq, n_target):
    """LP-dual solve via the canonical entry point, with optional extra
    equality rows folded into the square-Gram operator-selection form.

    The pyhecke entry point takes (t, G_square, n_target) where the only
    constraints are Σx = n_target and Gx ≥ 0. Equality rows A_eq x = b_eq
    are not natively supported there, so for methods that need them we fall
    back to a direct scipy/HiGHS solve and report primal+dual ourselves.
    """
    import numpy as _np
    from scipy.optimize import linprog as _linprog

    t = _np.asarray(t, float)
    G = _np.asarray(G, float)
    d = len(t)
    A_ub = -G  # Gx ≥ 0  ⇔  -Gx ≤ 0
    b_ub = _np.zeros(G.shape[0])
    A_eq_full = [_np.ones(d)]
    b_eq_full = [n_target]
    if A_eq is not None:
        for row, rhs in zip(A_eq, b_eq):
            A_eq_full.append(_np.asarray(row, float))
            b_eq_full.append(float(rhs))
    res = _linprog(
        c=t, A_ub=A_ub, b_ub=b_ub,
        A_eq=_np.array(A_eq_full), b_eq=_np.array(b_eq_full),
        bounds=[(-1e6, 1e6)] * d, method="highs",
    )
    out = {
        "status": res.status,
        "feasible": bool(res.success),
        "primal_obj": float(res.fun) if res.success else None,
        "x_star": res.x.tolist() if res.success else None,
        "duality_gap": 0.0 if res.success else None,
        # This is a RAW scipy solve, not the canonical entry point: the
        # phase-B methods stack extra equality rows onto `A_eq`, which
        # `solve_operator_selection_lp` cannot express (it takes the net row
        # plus `Gx >= 0`). So it is genuinely f64 and has no MPFR path today —
        # the same gap `solve_frobenius_dual_lp` has, and for the same reason.
        # Recording the backend is what lets the float64 gate SEE it instead
        # of it sitting in the unannotated bucket. Bean `qou/ftuv`.
        "backend": "scipy-highs",
    }
    if res.success and res.eqlin is not None:
        out["eq_duals"] = _np.asarray(res.eqlin.marginals).tolist()
    if res.success and res.ineqlin is not None:
        out["ineq_duals"] = _np.asarray(res.ineqlin.marginals).tolist()
    return out


def project_rows_to_support(A_eq, b_eq, support_idx, n_blocks):
    """Project equality rows onto the support columns, reporting what is lost.

    A row `sum_lambda a_lambda x_lambda = b` restricted to the support DROPS
    its kernel terms. That is a MODELLING DECISION, not an algebraic identity:
    it asserts `x_lambda = 0` on every zero-weight block — "do not occupy a
    block the Markov trace cannot see", which under convention D is exactly
    `y_lambda = 0 => tr_M(P_lambda) = 0`. It is stated here rather than folded
    silently into the solve.

    A row whose weight lies ENTIRELY on the kernel degenerates to `0 = b`:
    vacuous when `b == 0`, INFEASIBLE otherwise. Both are reported per row so
    an encoding that dies under projection is visible as such rather than as a
    bare `feasible: False`.
    """
    import numpy as _np
    if A_eq is None:
        return None, None, []
    kernel_idx = [i for i in range(n_blocks) if i not in set(support_idx)]
    rows_out, rhs_out, report = [], [], []
    for j, (row, rhs) in enumerate(zip(A_eq, b_eq)):
        a = _np.asarray(row, float)
        w_sup = float(_np.abs(a[support_idx]).sum())
        w_ker = float(_np.abs(a[kernel_idx]).sum()) if kernel_idx else 0.0
        total = w_sup + w_ker
        degenerate = w_sup == 0.0
        report.append({
            "row": j,
            "weight_on_support": w_sup,
            "weight_on_kernel": w_ker,
            "fraction_dropped": (w_ker / total) if total > 0 else 0.0,
            "degenerate_under_projection": degenerate,
            "verdict": ("infeasible (0 = b, b != 0)" if degenerate and float(rhs) != 0.0
                        else "vacuous (0 = 0)" if degenerate
                        else "ok"),
        })
        rows_out.append(a[support_idx])
        rhs_out.append(float(rhs))
    return rows_out, rhs_out, report


def solve_lp_with_eq_both(t, frob_diag, A_eq, b_eq, n_target, support_idx):
    """Full-space solve plus the support-projected one, with the row report.

    Under convention D the full-space answer is not a result: the kernel blocks
    carry zero cost and a vacuous positivity row, and the net constraint is a
    PLAIN SUM, so they absorb `sum x = n_target` for free and the optimum is 0.
    The projected solve is the one to read. Both are emitted so the difference
    stays auditable rather than being asserted in prose.
    """
    import numpy as _np
    full = solve_lp_with_eq(t, _np.diag(frob_diag), A_eq, b_eq, n_target)
    t_sup = _np.asarray(t, float)[support_idx]
    g_sup = _np.diag(_np.asarray(frob_diag, float)[support_idx])
    rows_sup, rhs_sup, report = project_rows_to_support(
        A_eq, b_eq, support_idx, len(t))
    proj = solve_lp_with_eq(t_sup, g_sup, rows_sup, rhs_sup, n_target)
    return {
        "result": full,
        "result_support_projected": proj,
        "projection_row_report": report,
    }


def parse_partition(key: str) -> tuple[int, ...]:
    """'(3, 2, 1)' -> (3, 2, 1)."""
    return tuple(int(p) for p in key.strip("()").rstrip(",").split(",") if p.strip())


def conjugate_partition(part: tuple[int, ...]) -> tuple[int, ...]:
    """Conjugate (transpose) partition λ ↦ λ' — the 'skew'/column-reading."""
    if not part:
        return ()
    return tuple(sum(1 for r in part if r > j) for j in range(part[0]))


def sanitize_nan(val):
    """Replace NaN/Inf floats with None so the witness is RFC 8259 JSON.

    The infeasible/unbounded SDP path can return NaN entries (e.g. the
    cvxpy `X_star`); standard JSON (and bun/JS `JSON.parse` in the content
    pipeline) reject `NaN`/`Infinity` literals.
    """
    if isinstance(val, dict):
        return {k: sanitize_nan(v) for k, v in val.items()}
    if isinstance(val, list):
        return [sanitize_nan(x) for x in val]
    if isinstance(val, float) and not math.isfinite(val):
        return None
    return val


def main() -> int:
    data = json.loads(COST_WITNESS.read_text())["data"]
    y_lambda = data["y_lambda_at_q0"]
    chi_beta_D = data["chi_lambda_beta_D_at_q0"]

    # Cost + Frobenius Gram via the shared assembly module (centralises the
    # t_λ=y_λ·χ^λ / G_λλ=y_λ·dim pattern duplicated across ~67 scripts; the
    # Burnside dim check + tr_M cross-check run inside build_cost_gram).
    _cg = build_cost_gram(
        y_lambda, chi_beta_D, n=6, tr_M_check=float(data["tr_M_check_at_q0"]),
    )
    keys, parts, dims = _cg.keys, _cg.parts, _cg.dims
    y, chi = _cg.y, _cg.chi
    t, frob_diag = _cg.t, _cg.frob_diag
    tr_M_beta_D = _cg.tr_M
    n_target = tr_M_beta_D            # net constraint
    tr_M_recorded = float(data["tr_M_check_at_q0"])
    tr_M_rel_err = abs(tr_M_beta_D - tr_M_recorded) / abs(tr_M_recorded)

    # ── Phase A diagnostic — REWRITTEN FOR CONVENTION D (2026-08-26) ──────
    #
    # This block used to read: "the q_0 Frobenius Gram is INDEFINITE ... some
    # blocks carry a negative q-trace norm ... the unconstrained LP is
    # unbounded ... which is precisely why Phase B's color-flavor constraints
    # are required."  Every clause of that was true in convention **C** and is
    # false in **D**, which has been canonical since 2026-08-09 (owner ruling
    # R1, reaffirmed 2026-08-15).
    #
    # D caps the Markov weights at two rows: `y_λ = 0` for `ℓ(λ) > 2`.  Since
    # `G_λλ = tr_M(P_λ) = y_λ · dim S^λ` and `t_λ = y_λ · χ^λ(β_D)`, a
    # three-or-more-row block contributes **zero to the Gram and zero to the
    # cost**.  It is not a forbidden channel carrying a negative norm; it is
    # simply absent.  Measured at n = 6: C gave eleven nonzero Gram entries,
    # three of them negative; D gives four positive and seven exactly zero,
    # and there is no negative weight at n = 3, 6, 9 or 12.
    #
    # CONSEQUENCE, measured by re-running this producer: the program is
    # **bounded** and strong duality **holds** (gap 3.7e-43, against 43926.6
    # under C).  So the singularity needs no repair to make the LP well posed —
    # the unboundedness *was* the indefiniteness, and that was convention C.
    #
    # WHAT THE SINGULARITY DOES COST is the dual's information content.  The
    # seven kernel blocks have zero cost and a vacuous constraint (`0·x ≥ 0`),
    # so their occupations are free null directions and the solver returns an
    # arbitrary interior point on them — measured, a uniform `y_star = 0.168`
    # across all seven, which is filler rather than a shadow price.  Reading
    # `active_set` off the full space therefore reports all eleven blocks as
    # "active", which is meaningless.  Worse, because the net constraint is a
    # plain sum `Σx = n_target`, those free blocks absorb the entire net
    # requirement at zero cost, so the full-space OPTIMUM is ~0 as well —
    # satisfied by occupations that contribute nothing to tr_M.  The fix is to
    # solve on the support; that is `support_restricted` below, and it is the
    # one whose objective AND dual should be read.
    forbidden_blocks = [keys[i] for i, g in enumerate(frob_diag) if g < 0.0]
    kernel_blocks = [keys[i] for i, g in enumerate(frob_diag) if g == 0.0]
    support_idx = [i for i, g in enumerate(frob_diag) if g != 0.0]
    support_blocks = [keys[i] for i in support_idx]

    # Phase C — solve the real SDP with the true (indefinite) Frobenius Gram.
    # The canonical operator-selection entry point takes a square (d,d) Gram,
    # so the only positivity is Gx ≥ 0 with G = diag(tr_M(P_λ)).  Because that
    # Gram is indefinite at q_0, the program is UNBOUNDED (primal drives to the
    # M_bound rail; duality gap blows up).  This is the headline Phase A
    # result: a real per-nucleus SDP is ill-posed without Phase B's
    # color-flavor constraints — the empty-SDP layer cannot be trivially
    # upgraded by attaching a cost alone.
    # paired LP+SDP operator-selection solve (always emits both duals) via the
    # shared dual-emitting wrapper.
    _r = solve_real_sdp(_cg, n_target)
    lp_d, sdp_d = _r["lp"], _r["sdp"]
    _gap_full = lp_d.get("duality_gap")
    bounded = (_gap_full is not None and abs(float(_gap_full)) < 1e-6
               and bool(lp_d.get("feasible", True)))

    # active demand channels = blocks the deuteron bound state saturates.
    # NOTE: on the full space under D this is not informative — see the Phase A
    # note above. Read `support_restricted.active_blocks` instead.
    active_idx = lp_d.get("active_set", [])
    active_blocks = [keys[i] for i in active_idx if i < len(keys)]

    # ── Support-restricted solve (convention D) ──────────────────────────
    # Drop the zero-Gram / zero-cost blocks and re-solve on the support, where
    # the Gram is diagonal and strictly positive. This is what makes `y_star`
    # a shadow price again rather than solver filler on a null direction.
    # It is NOT the same move as C's "drop the forbidden negative-norm blocks":
    # there the dropped blocks carried nonzero cost and a violated positivity
    # constraint. Here they carry zero cost and a vacuous constraint.
    #
    # The restriction DOES change the optimum, and that is the point. The
    # feasible set is `{x : Σx = n_target, Gx ≥ 0, x ≥ -M_bound}` — the net
    # constraint is a PLAIN SUM over blocks, not a trace-weighted one. So a
    # kernel block, having zero cost and no positivity constraint, can absorb
    # the entire `Σx = n_target` requirement for free. Measured: the full-space
    # optimum is 3.7e-43 (i.e. zero) while the support-restricted optimum is
    # 0.0370. The full-space answer is a free lunch through the kernel — it
    # satisfies the net requirement using blocks that contribute nothing to
    # tr_M — and it is an artifact of carrying null directions, not a result.
    #
    # THAT is what the D singularity actually costs. It does not make the
    # program unbounded (C's indefiniteness did that); it makes the full-space
    # optimum vacuous and the full-space dual uninformative. Both are repaired
    # by solving where the weights live.
    _t_sup = np.array([t[i] for i in support_idx], dtype=float)
    _g_sup = np.diag([frob_diag[i] for i in support_idx])
    _r_sup = solve_real_sdp_arrays(_t_sup, _g_sup, n_target)
    lp_sup = _r_sup["lp"]
    _sup_active = lp_sup.get("active_set", [])
    support_restricted = {
        "blocks": support_blocks,
        "n_blocks": len(support_idx),
        "rationale": (
            "Convention D zeroes y_lambda for ell(lambda) > 2, so the kernel "
            "blocks carry zero cost AND a vacuous positivity constraint. The "
            "net constraint is a PLAIN SUM (Sum x = n_target), so those blocks "
            "can absorb the whole requirement for free: the full-space optimum "
            "is ~0 (3.7e-43), achieved on blocks contributing nothing to tr_M, "
            "with y_star a uniform 0.168 of filler. Restricting to the support "
            "removes that escape. The optimum CHANGES (to 0.0370) and that is "
            "the correct value; the full-space one is an artifact of carrying "
            "null directions."),
        "active_blocks": [support_blocks[i] for i in _sup_active
                          if i < len(support_blocks)],
        "lp": lp_sup,
        "sdp": _r_sup["sdp"],
    }

    # ── Symmetry analysis (involution / bar / skew) ──────────────────────
    # The Frobenius-norm sign structure is governed by the bar-involution
    # (q ↦ q⁻¹) composed with the skew/conjugate map λ ↦ λ'.  Empirically
    # every negative-norm forbidden block is the conjugate of a dominant
    # positive block, with tr_M(P_λ) sign-flipped — the §7b "symmetric
    # crystal / Type-B folding" signature.  We record the pairing.
    key_of = {parse_partition(k): k for k in keys}
    trM_block = {k: float(frob_diag[i]) for i, k in enumerate(keys)}
    symmetry = []
    for i, k in enumerate(keys):
        p = parse_partition(k)
        cp = conjugate_partition(p)
        ck = key_of.get(cp)
        t_self = trM_block[k]
        t_conj = trM_block.get(ck) if ck else None
        symmetry.append({
            "block": k,
            "conjugate": ck,
            "self_conjugate": (ck == k),
            "trM": t_self,
            "trM_conjugate": t_conj,
            "sign_flip_under_conjugation": (
                t_conj is not None and (t_self < 0) != (t_conj < 0)
            ),
        })
    self_conjugate_blocks = [s["block"] for s in symmetry if s["self_conjugate"]]
    sign_flip_pairs = sorted({
        tuple(sorted((s["block"], s["conjugate"])))
        for s in symmetry if s["sign_flip_under_conjugation"]
    })

    # ── Phase B (interim) — bounded subspace on positive-norm blocks ─────
    # Drop the bar-conjugate forbidden blocks (tr_M(P_λ) < 0); on the
    # surviving positive-Gram subspace the operator-selection program is
    # bounded and strong duality holds.  This is the well-posed interim
    # result (no quark constraints yet) that de-risks the Phase D Lean
    # wiring; the full color-flavor SDP is the follow-up.
    pos = [i for i, g in enumerate(frob_diag) if g > 0.0]
    pos_keys = [keys[i] for i in pos]
    t_pos = t[pos]
    G_pos = np.diag(frob_diag[pos])
    n_target_pos = float(t_pos.sum())
    # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
    # whether the Rust binary happens to be built, so the same script
    # yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
    # makes a missing binary an error rather than a changed answer.
    # Bean `qou/ftuv`.
    lp_pos = solve_operator_selection_lp(t_pos, G_pos, n_target_pos, backend="clarabel")
    lp_pos_d = lp_pos.to_dict()
    _gap_pos = lp_pos_d.get("duality_gap")
    interim_bounded = (_gap_pos is not None and abs(float(_gap_pos)) < 1e-6
                       and bool(lp_pos_d.get("feasible", True)))
    interim_active = [pos_keys[i] for i in lp_pos_d.get("active_set", []) if i < len(pos_keys)]

    # ── Phase B (full) — four constraint-encoding methods, side by side ──
    # Each tries to regularise the indefinite-Gram unbounded program with a
    # different physical constraint. Reported together so the encoding choice
    # is auditable; method (2) is explicitly flagged as an un-vetted ansatz.
    chi = np.array([chi_beta_D[k] for k in keys])  # χ^λ(β_D) per block
    n_blocks = len(keys)
    methods = {}

    # (1) Bar-involution / Type-B folding (§7b): pair each block with its
    #     conjugate and impose x_λ = x_λ' (symmetric fold). This collapses the
    #     sign-flipped conjugate pairs, definitising the folded Gram — the
    #     symmetry-driven regulariser (no invented weights).
    fold_rows, fold_rhs = [], []
    seen = set()
    for i, k in enumerate(keys):
        cp = conjugate_partition(parse_partition(k))
        ck = key_of.get(cp)
        if ck and ck != k and (k, ck) not in seen and (ck, k) not in seen:
            j = keys.index(ck)
            row = np.zeros(n_blocks); row[i] = 1.0; row[j] = -1.0
            fold_rows.append(row); fold_rhs.append(0.0)
            seen.add((k, ck))
    methods["1_bar_involution_fold"] = {
        "description": "x_λ = x_λ' (bar-involution/Type-B fold, §7b) — symmetry regulariser",
        "ansatz_flag": False,
        **solve_lp_with_eq_both(t, frob_diag, fold_rows, fold_rhs, n_target, support_idx),
    }

    # (2) Character-projection color-flavor constraints (UN-VETTED ANSATZ).
    #     One row per pair-type: A_pair[λ] = mult(pair)·χ^λ(β_D)/[6]_q!, RHS
    #     apportions B_D across pairs by multiplicity. Flagged for the
    #     canonical-watcher — the pair→block map does not exist in the repo.
    bracket6 = float(data.get("bracket_6_q0", 1.0))  # [6]_q! if recorded, else 1
    cf_rows, cf_rhs = [], []
    total_mult = sum(NINE_PAIR.values())
    for pair, mult in NINE_PAIR.items():
        sign = -1.0 if pair in ("ud", "du") else 1.0  # bar-flip on mixed channel
        row = sign * mult * chi / bracket6
        cf_rows.append(row)
        cf_rhs.append(B_D_AME_MeV * mult / total_mult)
    methods["2_character_projection_colorflavor"] = {
        "description": "per-pair χ^λ projection rows + AME-apportioned RHS",
        "ansatz_flag": True,
        "ansatz_warning": "UN-VETTED: pair→block map invented here; flag to canonical-watcher / CAL-4 discipline before any production use.",
        **solve_lp_with_eq_both(t, frob_diag, cf_rows, cf_rhs, n_target, support_idx),
    }

    # (3) Conservation-law constraints only: baryon number (Σx fixes total)
    #     and charge. Minimal and safe; weak (2 rows for 11 blocks).
    #     Baryon: Σ x_λ = n_target (already the net constraint). Charge:
    #     weight blocks by χ^λ sign as a proxy for the +1 deuteron charge.
    cons_rows = [np.sign(chi)]
    cons_rhs = [1.0]  # net charge +1 (proxy)
    methods["3_conservation_laws"] = {
        "description": "baryon (net) + charge (sign-weighted) conservation rows",
        "ansatz_flag": False,
        **solve_lp_with_eq_both(t, frob_diag, cons_rows, cons_rhs, n_target, support_idx),
    }

    # (4) AME-binding equality: retarget the net constraint to the physical
    #     binding energy t·x = B_D instead of tr_M(β_D). One-line physical
    #     anchor; composes with any of 1–3 (here stand-alone).
    methods["4_ame_binding_equality"] = {
        "description": "t·x = B_D_AME (physical binding-energy target)",
        "ansatz_flag": False,
        "production_default": False,
        "non_default_reason": "imposes the AME binding as an equality (consumes "
                              "the experimental answer); a validation anchor, not "
                              "a substrate derivation.",
        **solve_lp_with_eq_both(t, frob_diag, [t], [B_D_AME_MeV], n_target, support_idx),
    }

    # (5) CANONICAL — Littlewood-Richardson branching H_6 ⊃ H_3 × H_3.
    #     The deuteron is proton-H_3 ⊗ neutron-H_3; the constraint rows come
    #     from the *verified* LR breakdown
    #       χ^λ(β_D) = Σ_{μ,ν⊢3} c^λ_{μν} χ^μ(p) χ^ν(n)
    #     (sublemma-2-1-deuteron-branching.witness.json, branching_verified).
    #     For each constituent block μ⊢3 we impose that the occupation projected
    #     through the LR map reproduces the disjoint-product trace — i.e.
    #     Σ_λ [Σ_ν c^λ_{μν} χ^ν(n)] x_λ = χ^μ(p) · tr_M_neutron.  This is a
    #     representation-theory identity, NOT a fit: the c^λ_{μν} are integers
    #     and the χ are computed at q_0.  Three rows (μ ∈ {(3),(2,1),(1³)}).
    branch = json.loads(BRANCHING_WITNESS.read_text())
    lr = branch["lr_breakdown_per_lambda"]            # {λ_key: [{mu,nu,c,term_re}]}
    # `re` is serialized as a 60-digit STRING (the drained precision convention,
    # qou-t0rf) — NOT a float. Reading it raw made every downstream product a
    # `str * float`, so this producer could not run at all on `main`; that is
    # why its committed witness stayed stale in the convention-C frame while
    # its input witness had already been migrated to D. Parsed here at the
    # numpy boundary, which is where the LP rows are assembled and where the
    # narrowing is visible, rather than silently upstream.
    chi_p = {k: float(v["re"]) for k, v in branch["chi_proton_h3"].items()}
    chi_n = {k: float(v["re"]) for k, v in branch["chi_neutron_h3"].items()}
    parts3 = ["(3,)", "(2, 1)", "(1, 1, 1)"]

    def pkey(lst):  # [3] -> "(3,)" ; [2,1] -> "(2, 1)"
        return "(" + ", ".join(str(x) for x in lst) + ("," if len(lst) == 1 else "") + ")"

    # tr_M_neutron = Σ_ν y_ν χ^ν(n), the canonical H_3 neutron Markov trace
    # (full-Hecke y_ν from the y-lambda-at-q0 cache; no Rust). Centralised in
    # nucleus_sdp_assembly.tr_M_from_cache (the PR #2219 correctness fix —
    # never the unweighted proxy Σ_ν χ^ν, never /len(parts3)).
    tr_M_neutron = tr_M_from_cache(chi_n, n=3)
    lr_rows, lr_rhs = [], []
    for mu in parts3:
        row = np.zeros(n_blocks)
        for li, lkey in enumerate(keys):
            terms = lr.get(lkey, [])
            coeff = 0.0
            for term in terms:
                if pkey(term["mu"]) == mu:
                    coeff += term["c"] * chi_n.get(pkey(term["nu"]), 0.0)
            row[li] = coeff
        lr_rows.append(row)
        lr_rhs.append(chi_p[mu] * tr_M_neutron)  # stated identity: no /len(parts3)
    methods["5_lr_branching_canonical"] = {
        "description": "Littlewood-Richardson H_6⊃H_3×H_3 branching rows: "
                       "Σ_λ[Σ_ν c^λ_{μν} χ^ν(n)] x_λ = χ^μ(p)·tr_M_neutron, "
                       "tr_M_neutron = Σ_ν y_ν χ^ν(n) (canonical, no fit).",
        "ansatz_flag": False,
        "canonical": True,
        "production_default": True,
        "tr_M_neutron": tr_M_neutron,
        **solve_lp_with_eq_both(t, frob_diag, lr_rows, lr_rhs, n_target, support_idx),
    }

    # (6) Scalar 9-pair weighted ratio (FITTED — must be labelled near-match).
    #     Single row Σ_λ r_λ x_λ = ratio · tr_M(β_D), where r_λ is the
    #     per-block interface ratio χ_D/χ_disjoint and `ratio` is the
    #     neutron-heavy 5:4 weighted 9-pair value with the bar-involution
    #     sign flip on the mixed channel.  NOT substrate-canonical.
    interface = branch["deuteron_interface_ratios"]
    # Same string-serialization boundary as `chi_p`/`chi_n` above: `ratio[0]`
    # is a drained-precision STRING, and np.array of those gives dtype '<U64',
    # on which np.mean raises. Parsed explicitly.
    r_lambda = np.array([float(interface[k]["ratio"][0]) for k in keys])
    # neutron-heavy weighted ratio using interface magnitudes (bar-flip baked in
    # via signed ratios); scalar target = mean interface ratio · tr_M.
    ratio_scalar = float(np.mean(r_lambda))
    methods["6_scalar_9pair_ratio_fitted"] = {
        "description": "single 9-pair weighted-ratio row (FITTED; bar-flip on mixed channel)",
        "ansatz_flag": True,
        "production_default": False,
        "discipline_label": "near-match / exploratory — NOT substrate-canonical (CAL-4)",
        **solve_lp_with_eq_both(
            t, frob_diag, [r_lambda], [ratio_scalar * n_target], n_target,
            support_idx,
        ),
    }

    witness = {
        "engine": "deuteron_real_sdp",
        "engineVersion": "0.1.0",
        "computation": (
            "Deuteron real per-nucleus SDP (Phase A cost + Phase C dual "
            "solve) — replaces the abstract empty-constraint SDP. "
            "operator-selection-lp / lp-dual."
        ),
        "scriptFile": "deuteron_real_sdp.py",
        "lean_uniqueness_ref": LEAN_UNIQUENESS_REF,
        "data": {
            "n_strands": 6,
            "nucleus": "deuteron (²H, Z=1, N=1, A=2)",
            "partitions": keys,
            "irrep_dims": dims,
            "cost_t_lambda": t.tolist(),
            "frobenius_gram_diag": frob_diag.tolist(),
            "frobenius_gram_indefinite": bool((frob_diag < 0).any()),
            "forbidden_blocks_negative_norm": forbidden_blocks,
            "n_target": n_target,
            "tr_M_beta_D": tr_M_beta_D,
            "tr_M_rel_err_vs_witness": tr_M_rel_err,
            # ---- primal + dual (AGENTS.md §LP/SDP duals — required fields) ----
            "lp": lp_d,
            "sdp": sdp_d,
            "y0_star": lp_d.get("y0_star"),
            "y_star": lp_d.get("y_star"),
            "active_set": active_idx,
            "active_blocks": active_blocks,
            "primal_obj": lp_d.get("primal_obj"),
            "dual_obj": lp_d.get("dual_obj"),
            "duality_gap": lp_d.get("duality_gap"),
            # `lp_d` is a to_dict() and carries the companions; mirroring the
            # numbers up without them is what left these bare.
            **{_sk: lp_d[_sk] for _sk in
               ("y0_star_str", "y_star_str", "primal_obj_str",
                "dual_obj_str", "duality_gap_str") if _sk in lp_d},
            **{_k: lp_d[_k] for _k in ("backend", "precision_bits")
               if _k in lp_d},
            "strong_duality_holds": bounded,
            "real_sdp_well_posed_without_constraints": bounded,
            "diagnostic": (
                "Real SDP UNBOUNDED at q_0 — Frobenius Gram is indefinite "
                "(negative-norm blocks forbidden). Phase B color-flavor "
                "constraints required for a well-posed bounded program."
            ) if not bounded else "Real SDP bounded; strong duality holds.",
            # ---- symmetry (involution / bar / skew) ----
            "symmetry_conjugate_pairing": symmetry,
            "self_conjugate_blocks": self_conjugate_blocks,
            "sign_flip_conjugate_pairs": [list(p) for p in sign_flip_pairs],
            "symmetry_note": (
                "CONVENTION D (2026-08-26). This field used to read: 'Every "
                "negative-norm forbidden block is the conjugate lambda -> "
                "lambda' of a dominant positive block with tr_M(P_lambda) "
                "sign-flipped -- the S7b bar-involution / Type-B-folding "
                "signature.' That was a convention-C statement and it does "
                "not survive: under D there are NO negative-norm blocks, so "
                "sign_flip_conjugate_pairs is empty and the claimed signature "
                "has no instances. What conjugation does under D is map the "
                "entire support (the two-row partitions) into the kernel, "
                "since a two-row lambda of n >= 6 has lambda_1 >= 3 hence "
                "ell(lambda') >= 3. (3,2,1) remains the self-conjugate "
                "partition of 6, and under D its weight is zero -- it sits in "
                "the kernel, not at a fixed point of a sign flip."
            )
            if not sign_flip_pairs else
            (
                "Every negative-norm forbidden block is the conjugate λ↦λ' "
                "of a dominant positive block with tr_M(P_λ) sign-flipped — "
                "the §7b bar-involution (q↦q⁻¹) / Type-B-folding signature."
            ),
            # ---- convention-D kernel structure ----
            "kernel_blocks_zero_weight": kernel_blocks,
            "phase_B_kernel_free_lunch_open": (
                "CLOSED, with a NEGATIVE result (bean qou-6tcn). Each "
                "encoding below now carries `result` (full space) AND "
                "`result_support_projected`, plus a per-row "
                "`projection_row_report`. Read the projected one. "
                "MEASURED: all six are INFEASIBLE once projected. The reason "
                "is structural, not numerical. On the support G is strictly "
                "positive, so Gx >= 0 IS x >= 0 there; on the kernel G = 0, "
                "so Gx >= 0 imposes nothing and x may go NEGATIVE. That is "
                "what the kernel actually bought -- not merely absorbing the "
                "net constraint at zero cost, but supplying signed "
                "occupations. Remove it and the objective is bounded by "
                "max(t)*n_target = 0.146058, against B_D(AME2020) = 2.224566: "
                "short by 15.2x. Two rows also degenerate to 0 = b, one of "
                "them (5_lr_branching_canonical row 2, mu = (1,1,1)) "
                "infeasibly -- and that encoding is the production default. "
                "SCOPE (a): this bounds THIS cost on THIS program with "
                "non-negative occupations of the D-supported blocks. It "
                "refutes no binding conjecture and says nothing about a "
                "different cost, a different Wenzl level, or a program that "
                "admits signed occupations for a stated reason. See "
                "computations/meson/deuteron_support_reachability_probe.py "
                "(6 assertions)."),
            "support_blocks": support_blocks,
            "support_restricted": support_restricted,
            # ---- Phase B interim (bounded positive-norm subspace) ----
            "phase_B_interim": {
                "positive_norm_blocks": pos_keys,
                "n_target": n_target_pos,
                "bounded": interim_bounded,
                "strong_duality_holds": interim_bounded,
                "active_blocks": interim_active,
                "lp": lp_pos_d,
            },
            # ---- Phase B full — four encodings compared ----
            "B_D_AME_MeV": B_D_AME_MeV,
            "nine_pair_multiplicities": NINE_PAIR,
            "phase_B_full_methods": methods,
            "production_default_encoding": "5_lr_branching_canonical",
            "production_default_note": (
                "The canonical (substrate-derived, no-fit) LR-branching "
                "encoding is the production default. Encoding 4 (AME equality) "
                "consumes the experimental binding and is a validation anchor "
                "only; encoding 6 is fitted; encoding 2 is an un-vetted ansatz. "
                "The canonical encoding does NOT yet reproduce the deuteron "
                "binding — that closure is the open Δ_λ gate (AGENTS.md); "
                "production reports the honest canonical result, not a fit."
            ),
            # ---- scope markers ----
            "phase_A_cost": "done",
            "phase_B_constraints": "interim (bounded subspace) + 4 full encodings compared (method 2 un-vetted ansatz); full color-flavor 9-pair + AME2020 RHS",
            "phase_C_dual_solve": (
                "diagnostic (unbounded on full space; bounded on positive "
                "subspace)"
                if not bounded else
                "bounded on the full space under convention D; read the dual "
                "from support_restricted (the full-space y_star is filler on "
                "the seven zero-Gram null directions)"),
            "phase_D_lean_wiring": "pending (deuteron_emptySDP -> deuteron_realSDP)",
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    OUT_WITNESS.write_text(json.dumps(sanitize_nan(witness), indent=2) + "\n")

    print(f"deuteron real SDP @ H_6 — {len(keys)} blocks")
    print(f"  tr_M(β_D)      = {tr_M_beta_D:.10f}  (rel_err vs witness {tr_M_rel_err:.2e})")
    print(f"  primal_obj     = {lp_d.get('primal_obj')}")
    print(f"  dual_obj       = {lp_d.get('dual_obj')}")
    print(f"  duality_gap    = {lp_d.get('duality_gap')}")
    print(f"  Gram indefinite at q_0: {bool((frob_diag < 0).any())}  "
          f"forbidden (neg-norm) blocks = {forbidden_blocks}")
    print(f"  active blocks (full, unbounded) = {active_blocks}")
    print(f"  self-conjugate block(s)         = {self_conjugate_blocks}")
    print(f"  sign-flip conjugate pairs       = {[list(p) for p in sign_flip_pairs]}")
    print(f"  Phase B interim — bounded: {interim_bounded}  "
          f"gap={lp_pos_d.get('duality_gap')}")
    print(f"  Phase B interim — active blocks = {interim_active}")
    print("  Phase B full — six encodings:")
    for name, m in methods.items():
        r = m["result"]
        flag = "  ⚠ANSATZ" if m["ansatz_flag"] else ""
        print(f"    {name:38} feasible={r['feasible']}  "
              f"primal_obj={r['primal_obj']}{flag}")
    print(f"  wrote {OUT_WITNESS.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
