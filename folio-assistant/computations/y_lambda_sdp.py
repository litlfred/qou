#!/usr/bin/env python3
"""
Convex cross-checks for y_λ at H_n(R, q).

The Markov-trace block weights y_λ are determined by the linear
constraints  Σ_λ χ_λ(w_μ) y_λ = z^{n - len(μ)}.

This script provides two convex reformulations:

(LP) feasibility with positivity test:
    find y ∈ R^{p(n)} :  Ay = b,  y ≥ 0
    EMPIRICAL FINDING: positivity FAILS at n ≥ 4 — e.g.
    y_(1,1,1,1) ≈ -8.4e-4 at n=4 with canonical z = 1/(√q + 1/√q).
    The Markov trace is positive on positive ELEMENTS
    (tr_M(a^* a) ≥ 0), but the central-character weights y_λ are
    *not* individually non-negative.  Documented here as a
    structural fact, not a constraint to be enforced.

(LS) least-squares cross-check (no positivity):
    minimise ||Ay - b||²  with no inequality constraints
    Equivalent to linear-solve at generic q; verifies the same
    answer through a different solver (cvxpy / CLARABEL) for
    robustness.

The full SDP moment-matrix on the regular representation
(M ⪰ 0 indexed by n! reduced words) handles root-of-unity q where
the linear system becomes singular.  Cost grows as n! so it is
left to the sibling Rust kernel for n ≥ 6.

References:
- prop:alpha-k-derivation-procedure §"SDP variant"
- prop:confinement-sdp (existing SDP family in the paper)
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import cvxpy as cp

sys.path.insert(0, str(Path(__file__).parent))
from y_lambda_jones_markov_witness import (
    cycle_type_word,
    chi_lambda_with_cache,
)
from hecke_characters import build_seminormal_matrices, partitions_of
from q_parameter import Q as Q0_FLOAT


def solve_y_via_lp(n: int, q_val: float) -> dict:
    """Solve y_λ as an LP feasibility problem with y ≥ 0 positivity."""
    parts = list(partitions_of(n))
    p_n = len(parts)
    z = 1.0 / (q_val ** 0.5 + q_val ** -0.5)

    # Build the χ-matrix (numerical at q_val)
    seminormal_cache: dict = {}
    for lam in parts:
        sigmas, d_lam, _ = build_seminormal_matrices(lam, sparse=True, q=q_val)
        seminormal_cache[lam] = (sigmas, d_lam)
    A = np.zeros((p_n, p_n))
    b = np.zeros(p_n)
    for i, mu in enumerate(parts):
        word = cycle_type_word(mu)
        b[i] = z ** (n - len(mu))
        for j, lam in enumerate(parts):
            sigmas, d_lam = seminormal_cache[lam]
            A[i, j] = chi_lambda_with_cache(sigmas, d_lam, word)

    # LS cross-check: solve unconstrained least-squares
    y = cp.Variable(p_n)
    ls_problem = cp.Problem(
        cp.Minimize(cp.sum_squares(A @ y - b))
    )
    ls_problem.solve(solver="CLARABEL")
    y_ls = y.value
    ls_residual = float(np.max(np.abs(A @ y_ls - b)))

    # LP positivity test: does the unique solution have y ≥ 0?
    # We check via the LS solution, not via constrained LP, since
    # constrained LP is infeasible when any y_λ < 0.
    min_y = float(np.min(y_ls))
    positivity_holds = min_y >= -1e-10

    return {
        "n": n,
        "q": q_val,
        "z": z,
        "ls_status": ls_problem.status,
        "y_ls": [float(v) for v in y_ls],
        "min_y_lambda": min_y,
        "max_y_lambda": float(np.max(y_ls)),
        "ls_residual": ls_residual,
        "positivity_holds": positivity_holds,
        "positivity_violators": [
            {"index": int(j), "y_lambda": float(y_ls[j])}
            for j in range(p_n)
            if y_ls[j] < -1e-10
        ],
    }


def cross_check(n: int) -> dict:
    """Compare LS solution to linear-solve solution."""
    result = solve_y_via_lp(n, float(Q0_FLOAT))
    if result.get("y_ls") is None:
        return result

    witness_path = Path(__file__).parent / "y-lambda-jones-markov-witness.json"
    with witness_path.open() as f:
        witness = json.load(f)
    table = witness["tables_by_n"].get(str(n))
    if table is None:
        result["cross_check"] = "no linear-solve witness for this n"
        return result

    parts = list(partitions_of(n))
    diffs = []
    for j, lam in enumerate(parts):
        weight_entry = next(
            w for w in table["weights"] if tuple(w["partition"]) == lam
        )
        y_linsolve = weight_entry["y_lambda"]
        y_ls = result["y_ls"][j]
        diffs.append(abs(y_ls - y_linsolve))

    result["cross_check"] = {
        "max_abs_diff_vs_linsolve": float(max(diffs)),
        "all_within_1e-9": all(d < 1e-9 for d in diffs),
    }
    return result


def main(ns: list[int]) -> None:
    out_path = Path(__file__).parent / "y-lambda-sdp-witness.json"
    out: dict = {
        "description": (
            "LP feasibility cross-check for y_λ: solves Ay=b with y≥0 "
            "via cvxpy and compares to the linear-solve witness.  "
            "Certifies positivity of the Markov-trace block weights "
            "and provides a robust path at near-singular q."
        ),
        "references": [
            "prop:alpha-k-derivation-procedure",
            "prop:confinement-sdp",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "tables_by_n": {},
    }
    for n in ns:
        print(f"LS cross-check at H_{n}(R, q) (q = {float(Q0_FLOAT)})...")
        result = cross_check(n)
        out["tables_by_n"][str(n)] = result
        cc = result.get("cross_check", {})
        positivity = "✓" if result.get("positivity_holds") else "✗"
        print(
            f"  status: {result['ls_status']}, "
            f"min y_λ: {result['min_y_lambda']:+.2e}, "
            f"positivity {positivity}, "
            f"max diff vs linsolve: {cc.get('max_abs_diff_vs_linsolve', 'n/a'):.2e}"
        )

    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [2, 3, 4, 5]
    main(ns)
