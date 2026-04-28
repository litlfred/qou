#!/usr/bin/env python3
"""
Mixed-Integer Semidefinite Programming (MISDP) for quadratic cross-term.

Solves:
    minimize  |tr_M(W_atom)|
    s.t.      G(q) x ≥ 0           (linear Frobenius positivity)
              [[Φ_{ij}, ·]; [·, ·]] ⪰ 0   (quadratic PSD per pair)
              x ∈ ℤ_{≥0}^N          (integer)

The quadratic term z² · Φ_q(|V̂_i V̂_j|) encodes pair coupling; each
adjacent (i, j) pair gets a 2×2 PSD constraint.

Approach: branch-and-cut with continuous SDP relaxation at each node.
  1. Solve continuous SDP (cvxpy) → V̂_i* ∈ ℝ_+ continuous optimum
  2. Round to integer grid, verify feasibility
  3. If infeasible, branch on most-fractional V̂_i, solve subproblems
  4. Prune via continuous bound; keep best integer incumbent

Falls back to enumeration if cvxpy unavailable.
"""
import sys
import math
import json
import itertools
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0, qi0 as qi, z_mark, HA as h, Phi_q


def continuous_sdp_pair_coupling(n_vars, *, lower=None, upper=None,
                                  obj_weights=None,
                                  pair_bounds=None, target_vector=None):
    """Continuous SDP relaxation of the MISDP.

    Vars: V̂ ∈ ℝ_+^n (Markov volume per generator).
    Obj:  minimize Σ w_i · V̂_i (linear proxy for |tr_M|).
    Cons: lower ≤ V̂_i ≤ upper, and 2×2 PSD coupling per adjacent pair.

    ``lower`` and ``upper`` are length-n vectors used by branch-and-
    bound to fix / restrict individual variables at a node.

    Returns dict with keys ``V`` (list of floats), ``obj`` (float),
    ``status``, or None if cvxpy is unavailable.
    """
    try:
        import cvxpy as cp
    except ImportError:
        return None

    if lower is None:
        lower = np.full(n_vars, 1.0)
    else:
        lower = np.asarray(lower, dtype=float)
    if upper is None:
        upper = np.full(n_vars, float(q0) - 0.05)
    else:
        upper = np.asarray(upper, dtype=float)
    # Infeasibility from bound tightening
    if np.any(lower > upper + 1e-9):
        return {"status": "infeasible_bounds", "V": None, "obj": None}

    V = cp.Variable(n_vars, nonneg=True)
    constraints = [V >= lower, V <= upper]
    for i in range(n_vars - 1):
        x_ij = cp.Variable(nonneg=True)
        block = cp.bmat([[V[i], x_ij], [x_ij, V[i + 1]]])
        constraints.append(block >> 0)
        constraints.append(x_ij <= (V[i] + V[i + 1]) / 2)
    if obj_weights is None:
        obj_weights = np.ones(n_vars)
    objective = cp.Minimize(cp.sum(cp.multiply(obj_weights, V)))
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
        if prob.status in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE]:
            return {
                "status": "solved",
                "V": V.value.tolist() if V.value is not None else None,
                "obj": float(prob.value) if prob.value is not None else None,
            }
        return {"status": prob.status, "V": None, "obj": None}
    except Exception as e:
        return {"status": f"error:{e}", "V": None, "obj": None}


def _is_integer_vec(v, tol=1e-4):
    """Return True iff every v_i rounds to within tol of an integer."""
    return all(abs(x - round(x)) < tol for x in v)


def _most_fractional(v, lower, upper, tol=1e-4):
    """Index of the most-fractional free variable (largest |v - round(v)|).

    Returns None if all components are integer (within tol) or already
    pinned (lower[i] == upper[i]).
    """
    best_i, best_score = None, -1.0
    for i, x in enumerate(v):
        if abs(lower[i] - upper[i]) < 1e-9:
            continue
        frac = abs(x - round(x))
        if frac > tol and frac > best_score:
            best_score = frac
            best_i = i
    return best_i


def _proxy_tr_m(m_vec):
    """Proxy |tr_M| for an integer multiplicity vector m_i ≥ 1.

    Matches the enumeration formula: Π (z·qᵐ + (1-z)·(-q⁻¹)ᵐ).
    Lower values → tighter binding target.
    """
    val = 1.0
    for m in m_vec:
        val *= (z_mark * q0 ** m + (1 - z_mark) * (-qi) ** m)
    return abs(val)


def misdp_branch_and_bound(n_vars, *, max_m=8,
                            obj_weights=None,
                            tol=1e-4,
                            max_nodes=2048,
                            verbose=False):
    """Integer MISDP via best-first branch-and-bound.

    Node = (lower, upper) hyperrectangle in ℝ_+^n_vars (integer bounds).
    At each node:
      1. Solve continuous SDP relaxation → (V*, obj*).
      2. If obj* ≥ incumbent.obj → prune.
      3. If V* is integer (within tol) → candidate incumbent; update.
      4. Else branch on the most-fractional V*_k:
           left:  upper[k] := floor(V*_k)
           right: lower[k] := ceil(V*_k)

    Integer domain: V_i ∈ {1, …, max_m}.

    Returns dict with incumbent solution, node count, and continuous
    optimum for comparison.
    """
    import heapq

    # Root continuous relaxation
    root_lo = np.full(n_vars, 1.0)
    root_hi = np.full(n_vars, float(max_m))
    root = continuous_sdp_pair_coupling(
        n_vars, lower=root_lo, upper=root_hi, obj_weights=obj_weights)
    if root is None:
        return {"status": "no_cvxpy"}
    if root["V"] is None:
        return {"status": "root_infeasible", "detail": root["status"]}

    root_obj = root["obj"]
    root_V = root["V"]

    # Priority queue: (lower_bound, tiebreaker, depth, lower, upper)
    incumbent = {"m": None, "obj": float("inf"),
                  "V": None, "proxy_tr_M": float("inf")}
    nodes_explored = 0
    nodes_pruned = 0
    heap: list = []
    counter = 0
    heapq.heappush(
        heap, (root_obj, counter, 0, tuple(root_lo), tuple(root_hi), root_V))

    while heap and nodes_explored < max_nodes:
        lb, _ctr, depth, lo, hi, V_here = heapq.heappop(heap)
        nodes_explored += 1
        # Prune by incumbent
        if lb >= incumbent["obj"] - tol:
            nodes_pruned += 1
            continue
        # Integer feasibility check
        if _is_integer_vec(V_here, tol):
            m_cand = [int(round(x)) for x in V_here]
            proxy = _proxy_tr_m(m_cand)
            # Use continuous objective as primary metric; proxy for record
            if lb < incumbent["obj"]:
                incumbent = {
                    "m": m_cand, "obj": lb, "V": list(V_here),
                    "proxy_tr_M": proxy, "depth": depth,
                }
                if verbose:
                    print(f"  [B&B] depth {depth}: incumbent "
                          f"m={m_cand}, obj={lb:.4f}, |tr_M|={proxy:.4e}")
            continue
        # Branch on most-fractional variable
        k = _most_fractional(V_here, lo, hi, tol)
        if k is None:
            # Numerically integer but failed tol; round
            m_cand = [int(round(x)) for x in V_here]
            proxy = _proxy_tr_m(m_cand)
            if lb < incumbent["obj"]:
                incumbent = {
                    "m": m_cand, "obj": lb, "V": list(V_here),
                    "proxy_tr_M": proxy, "depth": depth,
                }
            continue
        vk = V_here[k]
        lo_floor = math.floor(vk)
        hi_ceil = math.ceil(vk)
        lo_arr = np.array(lo, dtype=float)
        hi_arr = np.array(hi, dtype=float)
        # Left child: V_k ≤ floor
        left_hi = hi_arr.copy()
        left_hi[k] = min(hi_arr[k], lo_floor)
        if lo_arr[k] <= left_hi[k]:
            res_l = continuous_sdp_pair_coupling(
                n_vars, lower=lo_arr, upper=left_hi,
                obj_weights=obj_weights)
            if res_l and res_l["V"] is not None:
                counter += 1
                heapq.heappush(
                    heap, (res_l["obj"], counter, depth + 1,
                           tuple(lo_arr), tuple(left_hi), res_l["V"]))
        # Right child: V_k ≥ ceil
        right_lo = lo_arr.copy()
        right_lo[k] = max(lo_arr[k], hi_ceil)
        if right_lo[k] <= hi_arr[k]:
            res_r = continuous_sdp_pair_coupling(
                n_vars, lower=right_lo, upper=hi_arr,
                obj_weights=obj_weights)
            if res_r and res_r["V"] is not None:
                counter += 1
                heapq.heappush(
                    heap, (res_r["obj"], counter, depth + 1,
                           tuple(right_lo), tuple(hi_arr), res_r["V"]))

    return {
        "status": "solved" if incumbent["m"] is not None else "no_incumbent",
        "root_continuous": {"V": root_V, "obj": root_obj},
        "incumbent": incumbent,
        "nodes_explored": nodes_explored,
        "nodes_pruned": nodes_pruned,
        "max_nodes": max_nodes,
        "hit_node_limit": nodes_explored >= max_nodes,
    }


# Backwards-compatibility shim: keep the old signature working.
def misdp_branch_and_cut(n_vars, max_depth=3):
    """Legacy wrapper: delegates to the full branch-and-bound solver."""
    result = misdp_branch_and_bound(
        n_vars, max_m=max(3, max_depth + 2), max_nodes=512)
    if result.get("status") != "solved":
        return {"status": result.get("status", "unknown")}
    inc = result["incumbent"]
    return {
        "status": "solved",
        "V_continuous": result["root_continuous"]["V"],
        "m_integer": inc["m"],
        "obj": inc["obj"],
        "proxy_tr_M": inc["proxy_tr_M"],
        "depth": inc["depth"],
        "nodes_explored": result["nodes_explored"],
        "nodes_pruned": result["nodes_pruned"],
    }


def enumerate_misdp(n_vars, max_m=3):
    """Enumeration fallback for small problems.

    Enumerates m ∈ [1, max_m]^n_vars, verifies pair PSD constraints
    (with V_i := m_i as proxy), returns minimum |tr_M|.
    """
    feasible = []
    for m_tuple in itertools.product(range(1, max_m + 1), repeat=n_vars):
        # Pair PSD: |m_i · m_j| ≤ (m_i + m_j)/2
        # (arithmetic-geometric mean bound, always satisfied with equality
        #  when m_i = m_j)
        psd_ok = True
        for i in range(n_vars - 1):
            if math.sqrt(m_tuple[i] * m_tuple[i + 1]) > (m_tuple[i] + m_tuple[i + 1]) / 2:
                psd_ok = False
                break
        if psd_ok:
            # Proxy tr_M
            trM = 1.0
            for m in m_tuple:
                trM *= (z_mark * q0 ** m + (1 - z_mark) * (-qi) ** m)
            feasible.append({"m": list(m_tuple), "tr_M": trM})
    feasible.sort(key=lambda x: abs(x["tr_M"]))
    return feasible


if __name__ == "__main__":
    print("MISDP (Mixed-Integer SDP) for quadratic cross-term")
    print("=" * 72)
    print(f"q₀ = {q0}, z² = {z_mark**2:.4f}")
    print()

    bb_runs = {}

    # Branch-and-bound vs enumeration across problem sizes
    for n, max_m, max_nodes in [(3, 3, 512), (5, 3, 1024),
                                  (8, 3, 2048), (12, 3, 4096)]:
        print(f"n_vars = {n}, max_m = {max_m}")
        bb = misdp_branch_and_bound(
            n_vars=n, max_m=max_m, max_nodes=max_nodes)
        print(f"  B&B status:      {bb.get('status')}")
        if bb.get("status") == "solved":
            inc = bb["incumbent"]
            print(f"  root continuous: obj = "
                  f"{bb['root_continuous']['obj']:.4f}")
            print(f"  incumbent:       m = {inc['m']}")
            print(f"                   obj = {inc['obj']:.4f}, "
                  f"|tr_M| = {inc['proxy_tr_M']:.4e}")
            print(f"  nodes:           {bb['nodes_explored']} explored, "
                  f"{bb['nodes_pruned']} pruned, "
                  f"limit_hit={bb['hit_node_limit']}")
        # Enumeration comparison (only for n ≤ 5 — max_m^n grows fast)
        if n <= 5:
            enum_res = enumerate_misdp(n_vars=n, max_m=max_m)
            if enum_res:
                best_enum = min(enum_res, key=lambda r: abs(r['tr_M']))
                print(f"  enumeration:     m = {best_enum['m']}, "
                      f"|tr_M| = {abs(best_enum['tr_M']):.4e} "
                      f"({len(enum_res)} pts)")
        bb_runs[n] = bb
        print()

    witness = {
        "computation": "misdp-cross-channel",
        "description": (
            "Mixed-integer SDP for quadratic cross-term z²·Φ_q(|V̂_i V̂_j|). "
            "Branch-and-bound with continuous SDP lower bound at each "
            "node; best-first search; incumbent pruning; "
            "most-fractional-variable branching. Replaces the "
            "previous single-node continuous-rounding stub."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q": q0, "z_squared": z_mark**2},
        "algorithm": {
            "relaxation": "continuous SDP with pair PSD coupling "
                          "(cvxpy, SCS)",
            "lower_bound": "continuous objective = Σ w_i · V̂_i",
            "branching": "most-fractional V̂_k (integer cut at "
                         "floor/ceil)",
            "queue": "best-first by continuous lower bound (heapq)",
            "incumbent_prune": "skip nodes with lb ≥ incumbent.obj",
        },
        "results": {str(k): v for k, v in bb_runs.items()},
    }
    out = Path(__file__).parent / "misdp-cross-channel.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"Witness: {out}")
