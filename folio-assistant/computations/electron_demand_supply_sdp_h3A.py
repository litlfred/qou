#!/usr/bin/env python3
"""
Demand-supply SDP at the H_{3A} Plancherel (per-shape) level.

The H_3 version collapsed the atom state to a 6-D NF vector, losing
the per-irrep structure that the H_{3A} Plancherel sum exposes.  This
version operates at the true Plancherel level:

  tr_M(K)  =  Σ_λ  w_λ · χ_λ(K) / dim_λ

Each partition λ ⊢ 3A is a channel.  Per clause (iv) of
[prop:knot-operator-selection](#prop:knot-operator-selection), the
atom splits into per-irrep components via Schur orthogonality; the
demand-supply pairing operates per-shape.

  • For each shape λ with  tr_M_λ(K) < 0  (demand shape):
      require  Σ_α a_α · (tr_M_λ(K · β(T_α)) − tr_M_λ(K))  ≥  |tr_M_λ(K)|
  • Minimise  Σ_α  c(T_α) · a_α        (crossing energy)
  • a_α ≥ 0

Candidate set:  {T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}}  — exclude T_{1,0}
(identity has zero crossings and trivially dominates).

For Z > 1 electrons the SDP runs iteratively: after committing Φ₁,
the atom state updates to K · Φ₁ and we recompute per-shape demand.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A

try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


KNOT_OP_BRAID_WORDS = {
    "T_1_0": [],
    "T_2_1": [(1.0, 0.0, 0)],
    "T_2_2": [(1.0, 0.0, 0), (1.0, 0.0, 0)],
    "T_2_3": [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],
    "T_2_5": [(1.0, 0.0, 0), (1.0, 0.0, 1),
                 (1.0, 0.0, 0), (1.0, 0.0, 1),
                 (1.0, 0.0, 0)],
}
KNOT_OP_CROSSINGS = {"T_1_0": 0, "T_2_1": 1, "T_2_2": 2,
                          "T_2_3": 3, "T_2_5": 5}
ELECTRON_OPS = ["T_2_1", "T_2_2", "T_2_3", "T_2_5"]


def plancherel_per_shape(word, n_strands):
    """Return dict {shape_tuple: (w_lambda_chi_over_dim, chi, w_lambda, dim)}
    — the per-shape contribution to tr_M_Plancherel."""
    from scipy.sparse import issparse, eye as speye
    nfac = qfac(n_strands)
    out = {}
    for shape in partitions_of(n_strands):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        w_lambda = (dq * dq) / nfac
        contribution = w_lambda * chi / dim
        out[tuple(shape)] = (contribution, chi, w_lambda, dim)
    return out


def solve_h3A_demand_supply_sdp(K_per_shape: dict,
                                      T_alpha_per_shape: dict[str, dict]
                                      ) -> dict:
    """SDP at H_{3A} Plancherel level.

    K_per_shape:   {shape: (contribution_to_trM, ...)} for K · 1
                    = the current atom state
    T_alpha_per_shape[alpha]: same, for K · β(T_α).

    SDP variables: a_α ≥ 0, one per electron op.
    Demand shapes are those with K's contribution < 0.
    Supply on shape λ from Φ = Σ a_α T_α:
      supply_λ = Σ_α a_α · (T_alpha_contribution_λ − K_contribution_λ)
    Constraint (per demand shape λ):
      supply_λ ≥ |K_contribution_λ|
    Objective:
      min Σ_α c(T_α) · a_α
    """
    if not HAVE_CVXPY:
        raise ImportError("cvxpy required for H_{3A} demand-supply SDP")

    # Identify demand shapes from K
    demand_shapes = [sh for sh, (ctr, *_) in K_per_shape.items()
                          if ctr < -1e-12]
    if not demand_shapes:
        return {
            "status": "no_demand",
            "weights": {op: 0.0 for op in ELECTRON_OPS},
            "dominant": "T_2_3",   # default to canonical electron
            "E_cross": 0.0,
            "n_demand_shapes": 0,
        }

    n = len(ELECTRON_OPS)
    a = cp.Variable(n, nonneg=True)
    crossings = np.array([KNOT_OP_CROSSINGS[op] for op in ELECTRON_OPS],
                              dtype=float)
    constraints = []
    for sh in demand_shapes:
        K_ctr = K_per_shape[sh][0]    # negative
        # supply_lambda = sum_alpha a_alpha · (T_alpha_ctr - K_ctr)
        supply_coefs = []
        for op in ELECTRON_OPS:
            T_ctr = T_alpha_per_shape[op].get(sh, (0.0,))[0]
            supply_coefs.append(T_ctr - K_ctr)
        # constraint: supply ≥ |K_ctr|
        constraints.append(np.array(supply_coefs) @ a >= -K_ctr)
    prob = cp.Problem(cp.Minimize(crossings @ a), constraints)
    try:
        prob.solve(solver="CLARABEL")
    except Exception as e:
        return {
            "status": f"solver_error: {e}",
            "weights": {op: 0.0 for op in ELECTRON_OPS},
            "dominant": "T_2_3",
            "E_cross": 0.0,
            "n_demand_shapes": len(demand_shapes),
        }

    if prob.status not in {"optimal", "optimal_inaccurate"}:
        return {
            "status": prob.status,
            "weights": {op: 0.0 for op in ELECTRON_OPS},
            "dominant": "T_2_3",
            "E_cross": 0.0,
            "n_demand_shapes": len(demand_shapes),
        }

    weights = {op: float(a.value[i]) for i, op in enumerate(ELECTRON_OPS)}
    dominant = max(weights.items(), key=lambda kv: kv[1])[0]
    return {
        "status": prob.status,
        "weights": weights,
        "dominant": dominant,
        "E_cross": float(crossings @ a.value),
        "n_demand_shapes": len(demand_shapes),
    }


def iterate_h3A_demand_supply(Z: int, N: int, B_AME: float) -> dict:
    A = Z + N
    n = 3 * A

    word_atom = list(atom_braid_word_3A(
        Z, N, include_inter=True, include_electrons=False))
    word_free = list(atom_braid_word_3A(
        Z, N, include_inter=False, include_electrons=False))

    K_ps = plancherel_per_shape(word_atom, n)
    trM_a_base = sum(v[0] for v in K_ps.values())
    F_ps = plancherel_per_shape(word_free, n)
    trM_f_base = sum(v[0] for v in F_ps.values())
    B_base = E_0_BETA_DECAY_MEV * (abs(trM_f_base) - abs(trM_a_base))
    err_base = abs(B_base - B_AME) / (A * 938.272) * 100

    result = {
        "Z": Z, "N": N, "A": A, "B_AME_MeV": B_AME, "n_strands": n,
        "baseline_no_electrons_plancherel": {
            "trM_atom": trM_a_base, "trM_free": trM_f_base,
            "B_pred_MeV": B_base, "err_pct": err_base,
            "n_shapes_total": len(K_ps),
            "n_shapes_negative": sum(1 for v in K_ps.values()
                                              if v[0] < 0),
        },
        "electrons": [],
    }

    current_word_atom = list(word_atom)
    current_word_free = list(word_free)
    for e_i in range(Z):
        t0 = time.time()
        # Per-shape for current atom K and K · T_α for each α
        K_ps = plancherel_per_shape(current_word_atom, n)
        T_ps = {}
        for op in ELECTRON_OPS:
            word_op = current_word_atom + KNOT_OP_BRAID_WORDS[op]
            T_ps[op] = plancherel_per_shape(word_op, n)
        sdp = solve_h3A_demand_supply_sdp(K_ps, T_ps)
        dt = time.time() - t0

        weights = sdp["weights"]
        dominant = sdp["dominant"]
        print(f"  e {e_i+1}/{Z}: dominant={dominant}  "
              f"E_cross={sdp['E_cross']:+.4f}  "
              f"|demand shapes|={sdp['n_demand_shapes']}  [{dt:.1f}s]")
        for op in ELECTRON_OPS:
            w = weights[op]
            if abs(w) > 1e-6:
                print(f"    a_{op} = {w:+.4e}")

        # Evaluate binding for each op + for the chosen dominant
        op_word_used = KNOT_OP_BRAID_WORDS[dominant]
        current_word_atom = current_word_atom + op_word_used
        current_word_free = current_word_free + op_word_used

        # Final per-shape tr_M after this electron
        K_after = plancherel_per_shape(current_word_atom, n)
        F_after = plancherel_per_shape(current_word_free, n)
        trM_a = sum(v[0] for v in K_after.values())
        trM_f = sum(v[0] for v in F_after.values())
        B = E_0_BETA_DECAY_MEV * (abs(trM_f) - abs(trM_a))
        err = abs(B - B_AME) / (A * 938.272) * 100
        print(f"    after {dominant}: trM_a={trM_a:+.4e}  "
              f"B={B:+.4f}  err={err:.4f}%")

        result["electrons"].append({
            "electron_index": e_i,
            "sdp_status": sdp["status"],
            "dominant_op": dominant,
            "weights": weights,
            "E_cross": sdp["E_cross"],
            "n_demand_shapes": sdp["n_demand_shapes"],
            "trM_atom_after": trM_a,
            "trM_free_after": trM_f,
            "B_pred_MeV": B, "err_pct": err,
            "time_sec": dt,
        })

    final_trM_a = sum(v[0] for v in plancherel_per_shape(
        current_word_atom, n).values())
    final_trM_f = sum(v[0] for v in plancherel_per_shape(
        current_word_free, n).values())
    B_final = E_0_BETA_DECAY_MEV * (abs(final_trM_f) - abs(final_trM_a))
    err_final = abs(B_final - B_AME) / (A * 938.272) * 100

    # Legacy pile-up: Z × σ₁⁻¹ at gen 1 in H_{3A}
    leg_atom = word_atom + [(1.0, -float(h), 1) for _ in range(Z)]
    leg_free = word_free + [(1.0, -float(h), 1) for _ in range(Z)]
    trM_a_leg = sum(v[0] for v in plancherel_per_shape(
        leg_atom, n).values())
    trM_f_leg = sum(v[0] for v in plancherel_per_shape(
        leg_free, n).values())
    B_leg = E_0_BETA_DECAY_MEV * (abs(trM_f_leg) - abs(trM_a_leg))
    err_leg = abs(B_leg - B_AME) / (A * 938.272) * 100

    result["final"] = {
        "trM_atom": final_trM_a, "trM_free": final_trM_f,
        "B_pred_MeV": B_final, "err_pct": err_final,
        "dominant_ops": [e["dominant_op"]
                              for e in result["electrons"]],
    }
    result["legacy_pile_up"] = {
        "trM_atom": trM_a_leg, "trM_free": trM_f_leg,
        "B_pred_MeV": B_leg, "err_pct": err_leg,
    }
    return result


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    out = (Path(__file__).parent
             / "electron-demand-supply-sdp-h3A.witness.json")
    print("=" * 110)
    print("ELECTRON DEMAND-SUPPLY SDP — H_{3A} Plancherel per-shape")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        print(f"\n{name} (Z={Z}, N={N}, A={A}, n_shapes=p({3*A}))")
        try:
            r = iterate_h3A_demand_supply(Z, N, B_AME)
            r["atom"] = name
            all_results.append(r)
            base = r["baseline_no_electrons_plancherel"]
            fin = r["final"]
            leg = r["legacy_pile_up"]
            print(f"  baseline (no e, Plancherel):  "
                  f"B={base['B_pred_MeV']:+.4f}  err={base['err_pct']:.4f}%  "
                  f"({base['n_shapes_negative']}/{base['n_shapes_total']} "
                  f"shapes negative)")
            print(f"  legacy pile-up Z×σ₁⁻¹:         "
                  f"B={leg['B_pred_MeV']:+.4f}  err={leg['err_pct']:.4f}%")
            print(f"  H_{{3A}} demand-supply SDP     "
                  f"(ops={fin['dominant_ops']}): "
                  f"B={fin['B_pred_MeV']:+.4f}  err={fin['err_pct']:.4f}%")
        except Exception as e:
            import traceback
            print(f"  ERR: {type(e).__name__}: {e}")
            traceback.print_exc()
            all_results.append({"atom": name, "Z": Z, "N": N,
                                    "error": str(e)})
        out.write_text(json.dumps({
            "computation": "electron-demand-supply-sdp-h3A",
            "description": (
                "Demand-supply SDP at H_{3A} Plancherel per-shape "
                "level. Each partition lambda is a channel; demand is "
                "on shapes with tr_M_lambda(K) < 0. SDP picks "
                "weights a_alpha ≥ 0 over {T_{2,1}, T_{2,2}, T_{2,3}, "
                "T_{2,5}} minimising crossing energy subject to "
                "per-shape supply ≥ demand."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                              "electron_ops": ELECTRON_OPS},
            "results": all_results,
        }, indent=2, default=str))

    print(f"\nWitness: {out}")
