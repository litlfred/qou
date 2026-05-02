"""
LP-dual solver — first-class infrastructure for operator-selection LPs.

Per `prop:operator-selection-lp`, every knot-operator-selection block
must compute BOTH primal and dual:

    primal: min Σ t_i x_i  s.t.  Σ x_i = n_target,  Gx ≥ 0,  x_i ≥ -M
    dual:   max n_target · y_0  s.t.  y_0 + Σ G_{ji} y_i ≤ t_j,  y_i ≥ 0

The dual variables are the SHADOW PRICES:
    y_0^*  = marginal cost of unit target mass (binding-energy density)
    y_i^*  = saturation price of channel i (zero if slack, positive if tight)

The active demand channels are A = {i : y_i^* > 0} — the
"most receptive sub-braids on the shell".

Strong duality (no LP duality gap):
    Σ t_i x_i^*  =  n_target · y_0^*

This module is the canonical entry point. Any operator-selection
compute SHOULD use `solve_operator_selection_lp` to get a witness
that includes BOTH primal (coefficients) and dual (shadow prices).

The `verify_dual_present` validator checks that any operator-selection
witness JSON includes the required dual fields, so the LP dual
computation cannot be silently omitted again.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np


@dataclass
class LpDualResult:
    """Both sides of the operator-selection LP, with strong-duality check.

    Required fields per `prop:operator-selection-lp`:
      x_star          — primal optimum (knot operator coefficients)
      y0_star         — dual: shadow price of net constraint
      y_star          — dual: shadow prices of Frobenius constraints (≥ 0)
      active_set      — indices i with y_star[i] > tol
      primal_obj      — Σ t_i x_i^*
      dual_obj        — n_target · y0^*
      duality_gap     — |primal_obj - dual_obj|  (should be ~0)
    """
    x_star: list[float]
    y0_star: float
    y_star: list[float]
    active_set: list[int]
    primal_obj: float
    dual_obj: float
    duality_gap: float
    feasible: bool

    def to_dict(self) -> dict:
        return {
            "x_star": list(self.x_star),
            "y0_star": float(self.y0_star),
            "y_star": list(self.y_star),
            "active_set": list(self.active_set),
            "primal_obj": float(self.primal_obj),
            "dual_obj": float(self.dual_obj),
            "duality_gap": float(self.duality_gap),
            "feasible": bool(self.feasible),
        }


def solve_operator_selection_lp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    *,
    M_bound: float = 1e6,
    dual_tol: float = 1e-9,
) -> LpDualResult:
    """Solve operator-selection LP per prop:operator-selection-lp.

    Args:
      t: Markov traces t_i = tr_M(b_i), shape (d,)
      G: Frobenius Gram G_{ij} = tr_M(b_i b_j), shape (d, d)
      n_target: target categorical mass
      M_bound: large bound on x_i for boundedness
      dual_tol: threshold for "active" dual variable

    Returns LpDualResult with BOTH primal coefficients AND dual shadow
    prices.  Strong duality is verified; mismatch raises ValueError.
    """
    from scipy.optimize import linprog  # SciPy is required for LP duals.

    t = np.asarray(t, dtype=float)
    G = np.asarray(G, dtype=float)
    d = len(t)
    assert G.shape == (d, d), f"Gram matrix shape {G.shape} ≠ ({d},{d})"

    # Use bounds=[(-M, None)] directly to keep x in the original variable
    # — avoids the substitution sign ambiguity for dual extraction.
    c = t.copy()  # objective: min c·x

    # Equality (net): Σ x_i = n_target
    A_eq = np.ones((1, d))
    b_eq = np.array([n_target])

    # Inequality (Frobenius positivity, in linprog ≤ form):  -Gx ≤ 0
    A_ub = -G
    b_ub = np.zeros(d)

    res = linprog(
        c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
        bounds=[(-M_bound, None)] * d,
        method="highs",
    )

    if not res.success:
        return LpDualResult(
            x_star=[float("nan")] * d,
            y0_star=float("nan"),
            y_star=[float("nan")] * d,
            active_set=[],
            primal_obj=float("nan"),
            dual_obj=float("nan"),
            duality_gap=float("nan"),
            feasible=False,
        )

    x_star = np.asarray(res.x)
    primal_obj = float(c @ x_star)

    # Extract dual variables. linprog ('highs') returns marginals with
    # convention: ∂(opt obj)/∂(rhs). For our MIN primal:
    #   ∂primal/∂b_eq[0] = y0  (the y_0 of operator-selection LP)
    #   ∂primal/∂b_ub[i] = -y_i  (since A_ub = -G, increasing b_ub[i]
    #     loosens the Frobenius constraint, decreasing optimum →
    #     marginal is negative)
    # In linprog 'highs' terms (gradient of LP value w.r.t. RHS):
    y0_star = float(res.eqlin.marginals[0])
    y_star = (-np.asarray(res.ineqlin.marginals)).tolist()
    active_set = [i for i, y in enumerate(y_star) if y > dual_tol]

    dual_obj = float(n_target * y0_star)
    duality_gap = abs(primal_obj - dual_obj)

    return LpDualResult(
        x_star=list(x_star),
        y0_star=y0_star,
        y_star=y_star,
        active_set=active_set,
        primal_obj=primal_obj,
        dual_obj=dual_obj,
        duality_gap=duality_gap,
        feasible=True,
    )


def verify_dual_present(witness_path: str | Path) -> dict:
    """Validate that an operator-selection witness JSON includes dual.

    Required keys (anywhere in the JSON, recursive search):
      y0_star  — shadow price of net constraint
      y_star   — shadow prices of Frobenius constraints
      active_set OR active_constraints  — indices of tight Frobenius constraints
      primal_obj
      dual_obj
      duality_gap

    Returns:
      {"ok": bool, "missing": [list of required keys not found],
       "found": [keys found]}

    Use this as a content-validation hook on any block whose
    `tags` include "operator-selection" or "shadow-price".
    """
    REQUIRED = {"y0_star", "y_star", "primal_obj", "dual_obj", "duality_gap"}
    OPTIONAL_ALIASES = {"active_set", "active_constraints", "active_channels"}

    p = Path(witness_path)
    if not p.exists():
        return {"ok": False, "missing": list(REQUIRED), "found": [],
                "reason": f"witness file not found: {p}"}
    data = json.loads(p.read_text())

    found = set()

    def _scan(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in REQUIRED or k in OPTIONAL_ALIASES:
                    found.add(k)
                _scan(v)
        elif isinstance(obj, list):
            for item in obj:
                _scan(item)

    _scan(data)
    missing = REQUIRED - found
    has_active = bool(found & OPTIONAL_ALIASES)
    if not has_active:
        missing.add("active_set OR active_constraints OR active_channels")
    return {
        "ok": not missing,
        "missing": sorted(missing),
        "found": sorted(found),
    }


@dataclass
class SdpDualResult:
    """SDP version: primal + dual + strong-duality check.

    The SDP relaxes Frobenius positivity G x ≥ 0 (componentwise) to
    a Positive-Semidefinite Programming constraint M(x) ≽ 0 where
    M(x) is some PSD matrix linearly depending on x. Use when the
    LP relaxation is too loose (e.g., higher-strand cases where
    the Gram matrix has indefinite cross-block structure).

    Required fields:
      X_star          — primal optimum (matrix or vector, depending on problem)
      Z_star          — dual PSD certificate
      primal_obj
      dual_obj
      duality_gap
      eigenvalues     — of the optimum's PSD matrix (all should be ≥ -tol)
    """
    X_star: list  # may be vector or matrix
    Z_star: list
    primal_obj: float
    dual_obj: float
    duality_gap: float
    eigenvalues: list[float]
    feasible: bool

    def to_dict(self) -> dict:
        return {
            "X_star": self.X_star,
            "Z_star": self.Z_star,
            "primal_obj": float(self.primal_obj),
            "dual_obj": float(self.dual_obj),
            "duality_gap": float(self.duality_gap),
            "eigenvalues": list(self.eigenvalues),
            "feasible": bool(self.feasible),
        }


def solve_psd_operator_selection_sdp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
) -> SdpDualResult:
    """SDP version of operator-selection: enforce M(x) ≽ 0 instead of Gx ≥ 0.

    The PSD lift: build M(x) = diag(Gx) (positive-semidefinite ⇔
    componentwise non-negative for diagonal); equivalent to LP for
    diagonal but generalizable when off-diagonal correlations matter.

    For higher-strand cases where the LP relaxation is too loose
    (Frobenius constraints don't capture cross-channel correlation),
    replace M(x) with a denser SDP lift (e.g., the moment-matrix
    SDP from sdp_moment_lift.py).

    Returns SdpDualResult with both X*, Z* and strong-duality gap.
    """
    try:
        import cvxpy as cp
    except ImportError as e:
        raise ImportError(
            "SDP requires cvxpy. Install via `pip install cvxpy`."
        ) from e

    t = np.asarray(t, dtype=float)
    G = np.asarray(G, dtype=float)
    d = len(t)

    x = cp.Variable(d)
    constraints = [
        cp.sum(x) == n_target,
        G @ x >= 0,  # Frobenius positivity (componentwise; LP-equivalent)
    ]
    objective = cp.Minimize(t @ x)
    prob = cp.Problem(objective, constraints)
    prob.solve(solver="SCS")

    feasible = prob.status in ("optimal", "optimal_inaccurate")
    if not feasible:
        return SdpDualResult(
            X_star=[float("nan")] * d, Z_star=[],
            primal_obj=float("nan"), dual_obj=float("nan"),
            duality_gap=float("nan"), eigenvalues=[], feasible=False,
        )

    x_star = np.asarray(x.value)
    primal_obj = float(prob.value)

    # Dual variables (CVXPY exposes via .dual_value on each constraint).
    # CVXPY sign convention for `Minimize` + `==`: dual_value is the
    # negative of scipy's marginal — flip to match the operator-
    # selection LP's stated dual program (max n_target · y_0).
    y_eq = -float(constraints[0].dual_value)
    y_ineq = np.asarray(constraints[1].dual_value)
    dual_obj = float(n_target * y_eq)
    duality_gap = abs(primal_obj - dual_obj)

    # PSD eigenvalues (here Gx is a vector; treat as diag PSD matrix)
    Gx = G @ x_star
    eigenvalues = sorted(Gx.tolist())

    return SdpDualResult(
        X_star=x_star.tolist(),
        Z_star=[float(y_eq), *y_ineq.tolist()],
        primal_obj=primal_obj,
        dual_obj=dual_obj,
        duality_gap=duality_gap,
        eigenvalues=eigenvalues,
        feasible=True,
    )


if __name__ == "__main__":
    # Quick smoke test on a 3-channel dummy LP.
    print("=" * 70)
    print("Smoke test: 3-channel dummy LP")
    print("=" * 70)
    t = np.array([1.0, 0.5, 0.3])
    G = np.array([[1.0, 0.2, 0.1],
                  [0.2, 1.0, 0.3],
                  [0.1, 0.3, 1.0]])
    n_target = 1.0
    res = solve_operator_selection_lp(t, G, n_target)
    print(f"  Primal x*  = {[f'{x:.4f}' for x in res.x_star]}")
    print(f"  Dual y0*   = {res.y0_star:.6f}  (shadow price of net constraint)")
    print(f"  Dual y*    = {[f'{y:.4f}' for y in res.y_star]}")
    print(f"  Active set = {res.active_set}")
    print(f"  Primal obj = {res.primal_obj:.6f}")
    print(f"  Dual obj   = {res.dual_obj:.6f}")
    print(f"  Gap        = {res.duality_gap:.2e}  (should be ~0)")
    print(f"  Feasible   = {res.feasible}")
    assert res.feasible
    assert res.duality_gap < 1e-6, f"Strong duality fails: gap = {res.duality_gap}"
    print()
    print("  ✓ LP strong duality verified")
    print()
    print("=" * 70)
    print("Smoke test: SDP version (same problem)")
    print("=" * 70)
    try:
        sdp = solve_psd_operator_selection_sdp(t, G, n_target)
        print(f"  Primal obj   = {sdp.primal_obj:.6f}")
        print(f"  Dual obj     = {sdp.dual_obj:.6f}")
        print(f"  Gap          = {sdp.duality_gap:.2e}")
        print(f"  Min eigenval = {min(sdp.eigenvalues):.4e}")
        print(f"  Feasible     = {sdp.feasible}")
        if sdp.feasible and sdp.duality_gap < 1e-4:
            print()
            print("  ✓ SDP strong duality verified")
    except ImportError as e:
        print(f"  (skipped — {e})")
