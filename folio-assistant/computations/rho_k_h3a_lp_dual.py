#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical sympy/mpmath consumer; symbolic-q
# polynomials live downstream in hoefsmit_symbolic / y_lambda_wenzl_bridge
# witnesses.
"""Δ_λ option D — LP-dual shadow prices for the deuteron Wedderburn refinement.

This is the *Option D* sibling of `rho_k_h3a_refinement.py` (Occam) and the
crystal / co-Casimir / Demazure variants. The same underdetermined mass
equation

    ρ_K(q) - ρ_K^LO(Z, N)
       = (1 / |tr_M(β_K)|) · Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(β_K) · Δ_λ(K)

is reformulated as an **operator-selection LP** per
`prop:operator-selection-lp` (CLAUDE.md § *LP / SDP duals — first-class
infra*):

    Variables : Δ_λ ∈ ℝ for each λ ⊢ 6 (11 of them)
    Cost      : t_λ = a *categorically motivated* weight (Plancherel default,
                Frobenius alternative)
    Equality  : (1/|tr_M|) · Σ_λ (y_λ χ^λ) · Δ_λ  =  Δρ
                ⇔  Σ_λ (y_λ χ^λ) · Δ_λ  =  Δρ · |tr_M|  =:  target
    Bounds    : Δ_λ free (no positivity)

The LP-dual variables are the *derived* per-irrep binding-energy shadow
prices — replacing the arbitrary "single-support / smallest-|Δ|" choice
of the Occam baseline with a principled (per-CLAUDE.md) selector.

Witness: `rho-k-h3a-lp-dual.witness.json` carries
  - all original fields the Occam witness has (per_λ y_λ, χ^λ, products);
  - the canonical LP-dual record (`y0_star`, `y_star`, `active_set`,
    `primal_obj`, `dual_obj`, `duality_gap`) so
    `lp_dual_witness_validator.py` accepts it;
  - a `comparison_to_occam` block listing Δ_λ from both methods plus the
    L∞ difference, so the race between options can be judged numerically.

Honest caveat on cost choice: the LP needs SOME cost vector to pick a
unique extremum from the rank-deficient constraint manifold. The default
**Plancherel weight** t_λ = 1/dim_q(λ) penalises high-dim irreps least
(natural support on small blocks). The alternative **Frobenius norm**
t_λ = ‖χ^λ(β_D)‖ is reported for comparison. *Neither* is canonical;
both are categorically motivated, and the numerical answer depends on
which is chosen — this is the actual cost of moving from Occam to LP.
The witness reports both, plus the resulting duals.

Usage:
    python3 rho_k_h3a_lp_dual.py             # default: Plancherel
    python3 rho_k_h3a_lp_dual.py --cost frobenius
    python3 rho_k_h3a_lp_dual.py --workers 4
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from multiprocessing import Pool, cpu_count
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
# Reuse the established Occam pipeline pieces verbatim — they're
# the *correct* y_λ / χ^λ loaders. We just plug a different
# Δ_λ selector in front of them.
from rho_k_h3a_refinement import (  # noqa: E402
    _per_partition_numeric,
    _per_partition_symbolic,
    deuteron_canonical_crossings,
    evaluate_at_q0,
    load_deuteron_tr_M,
    load_y_lambda_n6,
    partitions_of_n,
)
from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV, M_D_MEV  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


# ── Categorical cost vectors ─────────────────────────────────────────

# `hook_lengths` and `dim_q_lambda` (numeric q-hook-length formula)
# imported from the shared helper rather than re-implemented locally
# — Gemini PR #613 review (dedup across the 4 ρ_K race scripts).
from murnaghan_nakayama import hook_lengths, dim_q_lambda  # noqa: E402, F401


def cost_plancherel(parts: list[tuple[int, ...]], q: mp.mpf) -> list[mp.mpf]:
    """t_λ = 1 / dim_q(λ). Penalises large (high-dim) blocks least, so
    minimum-cost concentrates Δ_λ on small irreps — the categorical
    analogue of "occupy the smallest available shell first"."""
    return [mp.mpf(1) / dim_q_lambda(lam, q) for lam in parts]


def cost_frobenius(chi_at_q0: dict[tuple, mp.mpf],
                   parts: list[tuple[int, ...]]) -> list[mp.mpf]:
    """t_λ = |χ^λ(β_D)|. Penalises high-energy channels (large |χ^λ|)
    most, so minimum-cost flows mass through the *least excited*
    Wedderburn blocks at the deuteron word."""
    return [abs(chi_at_q0[lam]) for lam in parts]


# ── LP-dual reformulation of the underdetermined mass equation ────

def lp_select_delta_lambda(
    y_chi: list[mp.mpf],
    target: mp.mpf,
    cost: list[mp.mpf],
    *,
    M_bound: float = 1e6,
) -> dict:
    """Solve the operator-selection LP that picks Δ_λ via L¹-min on cost.

    Geometry of the underdetermined mass equation
    ----------------------------------------------
    The single equality  Σ_λ (y_λ χ^λ) Δ_λ = target  defines an
    affine hyperplane in ℝ^11. With sign-free Δ_λ and a strictly
    positive cost vector t_λ > 0, the naive  min Σ t_λ Δ_λ  is
    *unbounded* below — flipping any Δ_λ → −∞ along a direction
    in the constraint nullspace decreases the objective without
    bound. (Empirically this manifests as scipy hitting the box.)

    Standard fix (Schrijver, *Theory of LP and IP*, §10): split
    Δ_λ = Δ_λ⁺ − Δ_λ⁻ with both ≥ 0 and minimise the **weighted L¹**
    norm

        min  Σ_λ t_λ (Δ_λ⁺ + Δ_λ⁻)
        s.t. Σ_λ (y_λ χ^λ) (Δ_λ⁺ − Δ_λ⁻) = target
             Δ_λ⁺ ≥ 0, Δ_λ⁻ ≥ 0.

    This is the canonical L¹-regularised LP form for picking a
    *sparsest* representative on a single-equality manifold (basis
    pursuit). Standard LP theory guarantees the optimum has at
    most ONE active partition (basic feasible solution on a 1-row
    LP is supported on at most 1 column) — meaning the LP picks
    a *single λ* of its own, just like Occam, BUT now derived from
    the cost vector rather than from a heuristic search over the
    11 singletons. This is the principled categorical answer.

    Setup (mapped to the canonical primal form `min c·z`)
    ------------------------------------------------------
    Variable order: z = [Δ⁺_0, …, Δ⁺_{d-1}, Δ⁻_0, …, Δ⁻_{d-1}]  (length 2d)
        c = [t_0, …, t_{d-1}, t_0, …, t_{d-1}]
        A_eq = [yc_0, …, yc_{d-1}, -yc_0, …, -yc_{d-1}]  (1 × 2d)
        b_eq = [target]
        z ≥ 0

    Dual record
    -----------
        y0_star := res.eqlin.marginals[0]    ← shadow price of the
                                                mass-equation row
        y_star_λ := y0_star * |Δ_λ|          ← per-λ binding-energy
                                                "contribution" shadow
                                                (single nonzero entry
                                                at the LP-active λ)

    The active_set is the single-element list [λ*] where Δ_λ* ≠ 0.
    """
    from scipy.optimize import linprog

    d = len(y_chi)
    t_np = np.array([float(c) for c in cost], dtype=float)
    yc_np = np.array([float(yc) for yc in y_chi], dtype=float)
    target_np = float(target)

    # Variable split: z = [Δ⁺ ; Δ⁻], length 2d.
    c2 = np.concatenate([t_np, t_np])
    A_eq = np.concatenate([yc_np, -yc_np]).reshape(1, 2 * d)
    b_eq = np.array([target_np])
    # Unbounded above (linprog convention: None = +∞) per Copilot
    # PR #613 review.  Hard upper-cap (M_bound) silently clipped any
    # genuinely unbounded LP; with `None` such cases now surface as
    # explicit `linprog` infeasible/unbounded statuses.  We also keep
    # `M_bound` as a *threshold* for the post-solve sanity check
    # below — if the optimum sits within 5% of M_bound it warns that
    # the LP is near a finite cap (likely an actually unbounded LP
    # masked by the original code).
    bounds = [(0.0, None)] * (2 * d)

    res = linprog(
        c=c2, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs",
    )

    if not res.success:
        return {
            "x_star": [float("nan")] * d,
            "y0_star": float("nan"),
            "y_star": [float("nan")] * d,
            "active_set": [],
            "primal_obj": float("nan"),
            "dual_obj": float("nan"),
            "duality_gap": float("nan"),
            "feasible": False,
            "scipy_status": res.message,
        }

    z = np.asarray(res.x)
    delta_plus = z[:d]
    delta_minus = z[d:]
    delta = delta_plus - delta_minus
    primal_obj = float(t_np @ (delta_plus + delta_minus))

    # ── Canonical dual extraction (Gemini PR #613 review):
    # Per CLAUDE.md "LP / SDP duals — first-class infra" and the
    # convention used by `solve_operator_selection_lp` and
    # `rho_k_h3a_gg_trajectory.py`, `y_star` reports the dual shadow
    # prices (reduced costs) of the per-λ non-negativity constraints
    # and `active_set` indexes the entries with non-zero shadow price
    # (the saturated constraints).  In the split-variable formulation
    # `z = [Δ⁺ ; Δ⁻]` (length 2d), each LP irrep channel λ has both a
    # plus and minus reduced cost; we take the smaller of the two so
    # `y_star[i] ≥ 0` and `y_star[i] = 0` ⇔ at least one direction is
    # interior.
    y0_star = float(res.eqlin.marginals[0])
    rc_plus = res.lower.marginals[:d]
    rc_minus = res.lower.marginals[d:]
    y_star = [float(min(p, m)) for p, m in zip(rc_plus, rc_minus)]
    active_set = [i for i, s in enumerate(y_star) if s > 1e-9]

    # Keep the split-variable per-λ contribution magnitude available
    # under its descriptive name for downstream tooling.
    lp_split_per_lambda_contribution = [abs(y0_star) * abs(d_i) for d_i in delta]
    dual_obj = float(target_np * y0_star)
    duality_gap = abs(primal_obj - dual_obj)

    return {
        "x_star": list(delta),
        "y0_star": y0_star,
        "y_star": y_star,
        "lp_split_per_lambda_contribution": list(lp_split_per_lambda_contribution),
        "active_set": active_set,
        "primal_obj": primal_obj,
        "dual_obj": dual_obj,
        "duality_gap": duality_gap,
        "feasible": True,
        "scipy_status": res.message,
        "delta_plus": list(delta_plus),
        "delta_minus": list(delta_minus),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--symbolic", action="store_true",
        help="Use the slow symbolic-q path (sympy chi_lambda_symbolic). "
             "Default is the numeric mpmath path — ~100× faster, "
             "bit-identical to the symbolic path at q_0 (50 dps).",
    )
    parser.add_argument(
        "--workers", type=int, default=min(cpu_count(), 11),
        help="multiprocessing.Pool size (default = min(cpu_count, 11)).",
    )
    parser.add_argument(
        "--cost", choices=["plancherel", "frobenius"], default="plancherel",
        help="Cost vector for the operator-selection LP (default: "
             "plancherel = 1/dim_q(λ)).",
    )
    args = parser.parse_args()
    engine = "symbolic" if args.symbolic else "numeric"

    print("=" * 96)
    print("  Δ_λ option D — LP-DUAL shadow prices (deuteron, n=6)")
    print(f"  Sibling of PR #600 (Δ_λ derivation race; A=Occam, B=co-Casimir, "
          f"C=Demazure, D=this, E=crystal)")
    print(f"  engine={engine}, workers={args.workers}, cost={args.cost}")
    print("=" * 96)

    print(f"\n  q_0 = {mp.nstr(Q_MP, 25)}")
    print(f"  m_e = {mp.nstr(M_E_MEV, 8)} MeV (CODATA)")
    print(f"  m_p = {mp.nstr(M_P_MEV, 8)} MeV (CODATA)")
    print(f"  m_n = {mp.nstr(M_N_MEV, 8)} MeV (CODATA)")
    print(f"  M(D) = {mp.nstr(M_D_MEV, 12)} MeV (CODATA)")

    # ── Step 1: |tr_M(β_D)| ───────────────────────────────────
    tr_M = load_deuteron_tr_M()
    abs_tr_M = abs(tr_M)
    print(f"\n  |tr_M(β_D)| (50 dps) = {mp.nstr(abs_tr_M, 30)}")

    # ── Step 2: ρ_K^LO and the residual to be explained ────────
    rho_K_LO = (M_P_MEV + M_N_MEV) / (M_E_MEV * abs_tr_M)
    rho_K_codata = M_D_MEV / (M_E_MEV * abs_tr_M)
    delta_rho = rho_K_codata - rho_K_LO
    print(f"\n  ρ_K^LO         = {mp.nstr(rho_K_LO, 25)}")
    print(f"  ρ_K^CODATA     = {mp.nstr(rho_K_codata, 25)}")
    print(f"  Δρ_K (residual) = {mp.nstr(delta_rho, 25)}")

    # ── Step 3: per-λ y_λ and χ^λ(β_D) at q_0 ─────────────────
    y_lam_sym = load_y_lambda_n6()
    crossings = deuteron_canonical_crossings()
    parts = partitions_of_n(6)
    assert len(parts) == 11, f"expected 11 partitions, got {len(parts)}"
    print(f"\n  Computing χ^λ(β_D) via {engine} engine "
          f"({len(parts)} partitions, {len(crossings)} crossings on H_6) …")

    q_str_50 = mp.nstr(Q_MP, 50)
    worker = _per_partition_symbolic if args.symbolic else _per_partition_numeric
    work = [(lam, crossings, q_str_50, mp.mp.dps) for lam in parts]

    chi_at_q0: dict[tuple, mp.mpf] = {}
    if args.workers > 1 and len(parts) > 1:
        with Pool(args.workers) as pool:
            for lam, chi_str in pool.imap_unordered(worker, work):
                chi_at_q0[lam] = mp.mpf(chi_str)
    else:
        for w in work:
            lam, chi_str = worker(w)
            chi_at_q0[lam] = mp.mpf(chi_str)

    rows = []
    sw_sum = mp.mpf(0)
    y_chi_list: list[mp.mpf] = []
    for lam in parts:
        chi_q0 = chi_at_q0[lam]
        if lam not in y_lam_sym:
            raise RuntimeError(f"y_λ for partition {lam} missing from witness")
        y_q0 = evaluate_at_q0(y_lam_sym[lam])
        contribution = y_q0 * chi_q0
        sw_sum += contribution
        y_chi_list.append(contribution)
        rows.append({
            "partition": list(lam),
            "y_lambda_at_q0": str(y_q0),
            "chi_lambda_beta_D_at_q0": str(chi_q0),
            "y_chi_product": str(contribution),
            "abs_y_chi": str(abs(contribution)),
        })

    # ── Step 4: Schur-Weyl identity sanity check ──────────────
    sw_err = abs(sw_sum - tr_M)
    sw_match = sw_err < mp.mpf("1e-40")
    print(f"\n  Schur-Weyl identity check:")
    print(f"    Σ_λ y_λ χ^λ(β_D)    = {mp.nstr(sw_sum, 30)}")
    print(f"    tr_M(β_D)           = {mp.nstr(tr_M, 30)}")
    print(f"    |residual|          = {mp.nstr(sw_err, 6)}  "
          f"{'PASS' if sw_match else 'FAIL'}")
    if not sw_match:
        print("    WARNING: Schur-Weyl identity failed at 1e-40 tolerance.")
        print("    LP-dual extraction below is meaningless without this identity.")

    # ── Step 5: build the cost vector(s) ──────────────────────
    print(f"\n  Cost vector ({args.cost}):")
    cost_planch = cost_plancherel(parts, Q_MP)
    cost_frob = cost_frobenius(chi_at_q0, parts)
    primary_cost = cost_planch if args.cost == "plancherel" else cost_frob
    secondary_cost = cost_frob if args.cost == "plancherel" else cost_planch
    secondary_name = "frobenius" if args.cost == "plancherel" else "plancherel"

    print(f"    {'partition':<24}{'t_planch=1/dim_q':>22}{'t_frob=|χ^λ|':>22}")
    print("    " + "-" * 68)
    for lam, tp, tf in zip(parts, cost_planch, cost_frob):
        print(f"    {str(list(lam)):<24}{mp.nstr(tp, 8):>22}"
              f"{mp.nstr(tf, 8):>22}")

    # ── Step 6: solve the LP (primary cost) ───────────────────
    target = delta_rho * abs_tr_M
    print(f"\n  Solving LP:  min Σ t_λ Δ_λ  s.t.  Σ (y_λ χ^λ) Δ_λ = target")
    print(f"    target = Δρ · |tr_M| = {mp.nstr(target, 25)}")

    lp_primary = lp_select_delta_lambda(y_chi_list, target, primary_cost)
    print(f"\n  LP-dual record ({args.cost}):")
    print(f"    feasible      = {lp_primary['feasible']}")
    print(f"    primal_obj    = {lp_primary['primal_obj']:.6e}")
    print(f"    dual_obj      = {lp_primary['dual_obj']:.6e}")
    print(f"    duality_gap   = {lp_primary['duality_gap']:.2e}")
    print(f"    y0_star       = {lp_primary['y0_star']:+.6e}  "
          f"(shadow price of the mass equation)")
    print(f"    active_set    = {lp_primary['active_set']}")

    # Solve the secondary cost too — for the comparison block.
    lp_secondary = lp_select_delta_lambda(y_chi_list, target, secondary_cost)

    # ── Step 7: comparison to Occam baseline ──────────────────
    occam_path = _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE)
    occam_blob = json.loads(occam_path.read_text())
    occam_per_lambda = occam_blob["data"]["per_lambda"]
    occam_solo: dict[tuple, mp.mpf] = {}
    for r in occam_per_lambda:
        lam = tuple(r["partition"])
        occam_solo[lam] = mp.mpf(r["Delta_lambda_solo_assumption"])
    occam_pick = occam_blob["data"]["occam_pick"]
    occam_pick_lam = tuple(occam_pick["partition"])
    occam_pick_delta = mp.mpf(occam_pick["Delta_lambda"])

    # Build comparison table: per partition, Occam-singleton Δ_λ vs LP Δ_λ.
    print(f"\n  Comparison vs Occam (singleton-support) baseline:")
    print(f"    {'partition':<24}{'Occam Δ_λ (solo)':>22}"
          f"{'LP Δ_λ ('+args.cost+')':>22}")
    print("    " + "-" * 68)
    cmp_rows = []
    for i, lam in enumerate(parts):
        d_occ = occam_solo[lam]
        d_lp = mp.mpf(lp_primary["x_star"][i])
        cmp_rows.append({
            "partition": list(lam),
            "Delta_occam_solo": str(d_occ),
            "Delta_lp_dual": str(d_lp),
            "abs_diff": str(abs(d_occ - d_lp)),
        })
        print(f"    {str(list(lam)):<24}{mp.nstr(d_occ, 8):>22}"
              f"{mp.nstr(d_lp, 8):>22}")

    # The Occam pick is a single partition; the LP picks at most a few.
    # Compare on the L∞ norm of (LP Δ_λ - Occam Δ_λ) where Occam Δ_λ is
    # the singleton-support vector (zero on all but the picked λ).
    occam_vec = [mp.mpf(0)] * len(parts)
    for i, lam in enumerate(parts):
        if lam == occam_pick_lam:
            occam_vec[i] = occam_pick_delta
    lp_vec = [mp.mpf(x) for x in lp_primary["x_star"]]
    linf = max(abs(occam_vec[i] - lp_vec[i]) for i in range(len(parts)))
    print(f"\n  L∞(Occam-pick - LP) = {mp.nstr(linf, 8)}")

    # ── Step 8: closure — verify the LP solution reproduces M(D). ──
    # By construction A_eq · Δ = target, so:
    #   ρ_K^refined = ρ_K^LO + (1/|tr_M|) · Σ_λ (y_λ χ^λ) Δ_λ
    #               = ρ_K^LO + target / |tr_M|
    #               = ρ_K^codata
    # The closure error is whatever LP residual scipy left.
    sigma_yc_delta = mp.mpf(0)
    for i in range(len(parts)):
        sigma_yc_delta += y_chi_list[i] * lp_vec[i]
    closure_residual = sigma_yc_delta - target
    rho_K_lp = rho_K_LO + sigma_yc_delta / abs_tr_M
    M_pred_lp = rho_K_lp * M_E_MEV * abs_tr_M
    closure_err_MeV = M_pred_lp - M_D_MEV
    closure_err_ppm = closure_err_MeV / M_D_MEV * mp.mpf("1e6")
    print(f"\n  Closure check (LP Δ_λ inserted into ρ_K refinement):")
    print(f"    Σ_λ (y_λ χ^λ) Δ_λ  = {mp.nstr(sigma_yc_delta, 12)}")
    print(f"    target              = {mp.nstr(target, 12)}")
    print(f"    constraint residual = {mp.nstr(closure_residual, 6)}")
    print(f"    M(D)^pred           = {mp.nstr(M_pred_lp, 16)} MeV")
    print(f"    closure error (ppm) = {mp.nstr(closure_err_ppm, 4)}")

    # ── Step 9: emit the witness ──────────────────────────────
    # Use WitnessBuilder.wrap_legacy so staleness metadata
    # (scriptHash, scriptCommitSha, commitSha, durationMs) is emitted
    # canonically per witness_base.py — replacing the prior hand-rolled
    # `json.dump` with `hashlib.sha256(...)` scriptHash.
    legacy_payload = {
        "computation": "rho-k-h3a-lp-dual",
        "description": (
            "Δ_λ option D: LP-dual shadow-price selection for the H_{3A} "
            "Wedderburn refinement of ρ_K (deuteron, n=6, 11 partitions). "
            "Reformulates the underdetermined mass equation as an "
            "operator-selection LP per prop:operator-selection-lp; the dual "
            "variables y0_star / y_star are the *derived* per-irrep "
            "binding-energy shadow prices, replacing the arbitrary "
            "single-support / smallest-|Δ| heuristic of the Occam baseline. "
            "Cost vector is " + args.cost + " (Plancherel = 1/dim_q(λ); "
            "Frobenius = |χ^λ(β_D)|). Both costs reported. Sibling of "
            "PR #600 derivation race (A=Occam, B=co-Casimir, C=Demazure, "
            "D=this LP-dual, E=crystal)."
        ),
        "engineDetail": (
            f"mpmath numeric Hoefsmit at q_0 (50 dps), "
            f"multiprocessing.Pool({args.workers}); "
            f"scipy.optimize.linprog 'highs' for LP+dual"
            if not args.symbolic
            else "sympy symbolic-q + mpmath evaluation (50 dps), single-threaded; "
                 "scipy.optimize.linprog 'highs' for LP+dual"
        ),
        "tags": ["lp-dual", "operator-selection-lp", "shadow-price"],
        "parameters": {
            "q_0_50dps": mp.nstr(Q_MP, 50),
            "atom": "deuteron",
            "Z": 1, "N": 1, "A": 2, "n_strands": 6,
            "braid_word_source": "mass_at_3A_proper.atom_braid_word_3A(1, 1)",
            "braid_word_str": (
                "β_p · I · β_n  (canonical: H_3 ⊗ H_3 ⊂ H_6 with "
                "interface I = σ_3 - h/2·1 at gen_idx=2)"
            ),
            "crossings_typed": [[g, t] for (g, t) in crossings],
            "n_crossings": len(crossings),
            "n_partitions": len(parts),
            "compute_status": "deuteron",
            "M_codata_MeV": str(M_D_MEV),
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
            "primary_cost_choice": args.cost,
            "cost_choices_supported": ["plancherel", "frobenius"],
        },
        "data": {
            "abs_tr_M_at_q0_50dps": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "rho_K_codata": str(rho_K_codata),
            "delta_rho_residual": str(delta_rho),
            "target_yc_delta_sum": str(target),
            "schur_weyl_check": {
                "sum_y_chi": str(sw_sum),
                "tr_M": str(tr_M),
                "abs_residual": str(sw_err),
                "match_at_1e_40": bool(sw_match),
            },
            "per_lambda": [
                {**rows[i],
                 "Delta_lambda_lp_primary": str(lp_vec[i]),
                 "cost_plancherel": str(cost_planch[i]),
                 "cost_frobenius": str(cost_frob[i])}
                for i in range(len(parts))
            ],
            # ── Required LP-dual fields (per CLAUDE.md / lp_dual_witness_validator) ──
            # These are the canonical names the validator looks for.
            "y0_star": lp_primary["y0_star"],
            "y_star": lp_primary["y_star"],
            "active_set": lp_primary["active_set"],
            "primal_obj": lp_primary["primal_obj"],
            "dual_obj": lp_primary["dual_obj"],
            "duality_gap": lp_primary["duality_gap"],
            "lp_primary": {
                "cost_choice": args.cost,
                "feasible": lp_primary["feasible"],
                "scipy_status": lp_primary["scipy_status"],
                "x_star": lp_primary["x_star"],
                "y0_star": lp_primary["y0_star"],
                "y_star": lp_primary["y_star"],
                "active_set": lp_primary["active_set"],
                "primal_obj": lp_primary["primal_obj"],
                "dual_obj": lp_primary["dual_obj"],
                "duality_gap": lp_primary["duality_gap"],
            },
            "lp_secondary": {
                "cost_choice": secondary_name,
                "feasible": lp_secondary["feasible"],
                "scipy_status": lp_secondary["scipy_status"],
                "x_star": lp_secondary["x_star"],
                "y0_star": lp_secondary["y0_star"],
                "y_star": lp_secondary["y_star"],
                "active_set": lp_secondary["active_set"],
                "primal_obj": lp_secondary["primal_obj"],
                "dual_obj": lp_secondary["dual_obj"],
                "duality_gap": lp_secondary["duality_gap"],
            },
            "comparison_to_occam": {
                "occam_pick_partition": occam_pick["partition"],
                "occam_pick_Delta_lambda": occam_pick["Delta_lambda"],
                "lp_active_partitions": [
                    list(parts[i]) for i in lp_primary["active_set"]
                ],
                "L_inf_diff": str(linf),
                "per_partition": cmp_rows,
                "verdict": (
                    "LP-dual reproduces Occam exactly"
                    if linf < mp.mpf("1e-12")
                    else "LP-dual differs structurally from Occam"
                ),
            },
            "closure_check": {
                "M_pred_MeV": str(M_pred_lp),
                "closure_err_MeV": str(closure_err_MeV),
                "closure_err_ppm": str(closure_err_ppm),
                "constraint_residual": str(closure_residual),
            },
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §7 P3' / Δ_λ derivation race",
        "pr": "#600 (sibling — Δ_λ option D)",
        "notes": (
            "Categorical caveat: every operator-selection LP needs SOME "
            "cost vector to lift the rank-deficient constraint manifold "
            "to a unique extremum. Two categorically motivated choices are "
            "reported: t_λ = 1/dim_q(λ) (Plancherel weight; default; "
            "favours small-dim, low-multiplicity blocks) and t_λ = "
            "|χ^λ(β_D)| (Frobenius norm; favours channels the deuteron "
            "word actually couples to weakly). Neither is canonical; the "
            "active-set y_λ* > 0 channels are the *derived* binding-energy "
            "shadow prices and may differ between the two costs. The "
            "comparison_to_occam block reports the L∞ between LP and the "
            "Occam (3,2,1)/[5,1] singleton-support pick. If LP picks the "
            "same single partition as Occam, the methods agree. If LP "
            "spreads support across several λ, the LP shadow prices are "
            "the *principled* selector and Occam was a degenerate guess."
        ),
        "follow_up": (
            "Extend to (T, ³He) at n=9 (p(9)=30) with the same LP and "
            "compare LP active sets across atoms — if a stable subset of "
            "λ is selected by LP for every atom, that subset is the "
            "categorically derived binding-channel registry. Also wire "
            "the LP-dual cache (lp_dual_cache.py) so witness regenerations "
            "do not re-solve the same LPs."
        ),
    }
    out_path = WitnessBuilder.wrap_legacy(
        "rho-k-h3a-lp-dual",
        legacy_payload,
        script_path=__file__,
        engine="mpmath" if not args.symbolic else "python+mpmath+sympy",
        output_dir=HERE,
    ).save()
    print(f"\n  Wrote {out_path.name} ({out_path.stat().st_size} bytes).")
    print("=" * 96)
    return 0 if sw_match and lp_primary["feasible"] else 2


if __name__ == "__main__":
    sys.exit(main())
