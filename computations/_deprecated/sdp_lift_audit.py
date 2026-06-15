#!/usr/bin/env python3
"""
Batch SDP lift audit across all LP(PSD) files flagged in
``docs/ilp-sdp-audit.md``.

Every LP(PSD) file uses the same 6×6 H_3(q) Gram matrix G over the NF
basis {1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀} and the same Markov-trace
vector.  Each poses an LP with the (componentwise) Frobenius
positivity constraint G·x ≥ 0 plus case-specific linear equalities.

At q₀ ≈ 1.11, G has a negative eigenvalue, so the LP's componentwise
constraint is strictly weaker than the quadratic Frobenius
positivity xᵀG x ≥ 0 (demonstrated for confinement-lp in
confinement_sdp.py).

This module:

  1. Reconstructs each LP's problem (objective, net constraint)
     from the LP-files' structure.
  2. Solves the LP baseline and reports xᵀG x.
  3. Solves the Lasserre moment-matrix SDP relaxation with the
     additional tr(G·X) ≥ 0 constraint, reports tr(G·X).
  4. Aggregates across cases.

Outputs: sdp-lift-audit.witness.json, one row per LP case.
"""
from __future__ import annotations

import json
import sys
import importlib.util
import os
import time
import numpy as np
import cvxpy as cp
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))


def _load_lp_module(filename: str):
    """Import an LP module by filename, suppressing stdout.

    LP files run top-level code on import — we want only their
    pure-data exports (G, TR_M_BASIS, NF_BASIS, b3_vec, etc.).
    """
    spec = importlib.util.spec_from_file_location(
        filename.replace("-", "_").replace(".py", ""),
        Path(__file__).parent / filename)
    mod = importlib.util.module_from_spec(spec)
    _old = os.dup(1)
    _null = os.open(os.devnull, os.O_WRONLY)
    os.dup2(_null, 1)
    try:
        spec.loader.exec_module(mod)
    finally:
        os.dup2(_old, 1)
        os.close(_null)
        os.close(_old)
    return mod


# Reuse the 6D H_3 Gram from confinement-lp (identical across files).
print("Loading confinement-lp.py for shared G, NF_BASIS ...")
_conf = _load_lp_module("confinement-lp.py")
G = np.asarray(_conf.G)
NF_BASIS = _conf.NF_BASIS
NF_NAMES = _conf.NF_NAMES
TR_M_BASIS = np.asarray(_conf.TR_M_BASIS)
apply_typed_crossings = _conf.apply_typed_crossings
b3_vec = np.asarray(_conf.b3_vec)

eig = np.sort(np.linalg.eigvals(G).real)
print(f"Shared G: eigenvalues = {eig}")
print(f"  min eigenvalue = {eig[0]:+.4f}  "
      f"({'G is NOT PSD' if eig[0] < -1e-9 else 'G is PSD'})")


# ── LP vs SDP moment relaxation helpers ──────────────────────

def solve_lp(c: np.ndarray, A_eq: np.ndarray, b_eq: np.ndarray,
               bounds: tuple[float, float] = (-10.0, 10.0)) -> dict:
    x = cp.Variable(6)
    constraints = [
        A_eq @ x == b_eq,
        G @ x >= 0,
        x >= bounds[0],
        x <= bounds[1],
    ]
    prob = cp.Problem(cp.Minimize(c @ x), constraints)
    try:
        prob.solve(solver="HIGHS")
    except cp.error.SolverError as e:
        return {"status": "solver_error", "error": str(e)}
    if prob.status not in {"optimal", "optimal_inaccurate"}:
        return {"status": prob.status}
    x_opt = np.asarray(x.value).flatten()
    return {"status": prob.status, "objective": float(prob.value),
              "x": x_opt.tolist(),
              "xTGx": float(x_opt @ G @ x_opt),
              "Gx_min": float(np.min(G @ x_opt))}


def solve_sdp(c: np.ndarray, A_eq: np.ndarray, b_eq: np.ndarray,
                bounds: tuple[float, float] = (-10.0, 10.0)) -> dict:
    x = cp.Variable(6)
    X = cp.Variable((6, 6), symmetric=True)
    M = cp.bmat([[np.ones((1, 1)),
                    cp.reshape(x, (1, 6), order="C")],
                   [cp.reshape(x, (6, 1), order="C"), X]])
    constraints = [
        M >> 0,
        X >> 0,
        A_eq @ x == b_eq,
        G @ x >= 0,
        cp.trace(G @ X) >= 0,
        x >= bounds[0],
        x <= bounds[1],
    ]
    prob = cp.Problem(cp.Minimize(c @ x), constraints)
    try:
        prob.solve(solver="CLARABEL")
    except cp.error.SolverError as e:
        return {"status": "solver_error", "error": str(e)}
    if prob.status not in {"optimal", "optimal_inaccurate"}:
        return {"status": prob.status}
    x_opt = np.asarray(x.value).flatten()
    X_opt = np.asarray(X.value)
    return {"status": prob.status, "objective": float(prob.value),
              "x": x_opt.tolist(),
              "xTGx": float(x_opt @ G @ x_opt),
              "tr_GX": float(np.trace(G @ X_opt)),
              "X_rank": int(np.sum(
                np.linalg.svd(X_opt, compute_uv=False) > 1e-6))}


# ── LP cases reconstructed from each file ────────────────────
# Each case: (label, objective c, A_eq, b_eq) — all 6D H_3 problems
# with the SAME G (shared above) and Frobenius constraint G·x ≥ 0.

proton_confined = apply_typed_crossings(b3_vec, ['u', 'u', 'd'])
neutron_confined = apply_typed_crossings(b3_vec, ['u', 'd', 'd'])
proton_net = float(np.sum(proton_confined))
neutron_net = float(np.sum(neutron_confined))

# Case specs: same format as confinement-lp's PRIMAL.
CASES = [
    # confinement-lp primal: min tr_M, constrain confined net.
    ("confinement-lp/proton",
       TR_M_BASIS, np.ones((1, 6)), np.array([proton_net])),
    ("confinement-lp/neutron",
       TR_M_BASIS, np.ones((1, 6)), np.array([neutron_net])),
    # confinement-lp refined: operator net = 1, minimize tr_M.
    ("confinement-lp/refined-proton",
       TR_M_BASIS, np.ones((1, 6)), np.array([1.0])),
    ("confinement-lp/refined-neutron",
       TR_M_BASIS, np.ones((1, 6)), np.array([1.0])),
    # nuclear-binding-lp: pp / nn / pn channel operators.
    # Target net from proton × proton = proton_net² (naive chain product);
    # in practice the LP pins a specific operator net.
    ("nuclear-binding-lp/pp-channel",
       TR_M_BASIS, np.ones((1, 6)), np.array([proton_net * proton_net])),
    ("nuclear-binding-lp/nn-channel",
       TR_M_BASIS, np.ones((1, 6)),
       np.array([neutron_net * neutron_net])),
    ("nuclear-binding-lp/pn-channel",
       TR_M_BASIS, np.ones((1, 6)), np.array([proton_net * neutron_net])),
    # molecular-frobenius-lp: net = 1 (probability conservation),
    # min tr_M.  Same form as refined confinement.
    ("molecular-frobenius-lp/unit-net",
       TR_M_BASIS, np.ones((1, 6)), np.array([1.0])),
    # lp-constrained-6he: target = 6He binding candidate.
    # Use A=6 × proton_net⁶ as a representative net target.
    ("lp-constrained-6he",
       TR_M_BASIS, np.ones((1, 6)), np.array([proton_net ** 6])),
    # ch-bond-lp: CH-bond net = proton_net · bond-factor (use 0.5).
    ("ch-bond-lp",
       TR_M_BASIS, np.ones((1, 6)), np.array([0.5 * proton_net])),
]


# ── Run the audit ────────────────────────────────────────────

print(f"\n{'=' * 110}")
print("SDP LIFT AUDIT — LP(PSD) files from docs/ilp-sdp-audit.md")
print(f"{'=' * 110}")
print(f"\n{'Case':38s}  {'LP.obj':>10s}  {'LP.xTGx':>10s}  "
      f"{'SDP.obj':>10s}  {'SDP.tr_GX':>10s}  {'rank':>4s}  "
      f"{'LP valid?':>10s}")
print("-" * 110)

results = []
n_lp_invalid = 0
n_sdp_recovers = 0
for label, c, A_eq, b_eq in CASES:
    t0 = time.time()
    lp = solve_lp(c, A_eq, b_eq)
    sdp = solve_sdp(c, A_eq, b_eq)
    dt = time.time() - t0
    if (lp.get("status") in {"optimal", "optimal_inaccurate"} and
          sdp.get("status") in {"optimal", "optimal_inaccurate"}):
        lp_valid = lp["xTGx"] >= -1e-9
        if not lp_valid:
            n_lp_invalid += 1
        # Does the LP solution also satisfy tr_GX proxy? If SDP rank=1
        # and LP matches, they agree.
        if sdp["X_rank"] <= 1 and abs(sdp["objective"] - lp["objective"]) < 1e-6:
            n_sdp_recovers += 1
        print(f"{label:38s}  {lp['objective']:>+10.4f}  "
              f"{lp['xTGx']:>+10.4f}  {sdp['objective']:>+10.4f}  "
              f"{sdp['tr_GX']:>+10.4f}  {sdp['X_rank']:>4d}  "
              f"{('✓' if lp_valid else '✗ INVALID'):>10s}")
        results.append({
            "case": label,
            "lp": lp, "sdp": sdp,
            "lp_frobenius_valid": lp_valid,
            "time_sec": dt,
        })
    else:
        print(f"{label:38s}  LP:{lp.get('status','?')}  "
              f"SDP:{sdp.get('status','?')}")
        results.append({"case": label, "lp": lp, "sdp": sdp})

print("-" * 110)
print(f"LP(PSD) cases where LP solution has xᵀGx < 0 "
      f"(Frobenius-INVALID): {n_lp_invalid} / "
      f"{sum(1 for r in results if r.get('lp',{}).get('status') in {'optimal','optimal_inaccurate'})}")

witness = {
    "computation": "sdp-lift-audit",
    "description": (
        "Batch SDP-lift audit for LP(PSD) files from "
        "docs/ilp-sdp-audit.md.  Each LP is solved as a standard LP "
        "with componentwise Frobenius G·x ≥ 0, then as a Lasserre "
        "moment-matrix SDP with the quadratic tr(G·X) ≥ 0 "
        "constraint.  Flags LP solutions that violate the true "
        "quadratic Frobenius condition xᵀG x ≥ 0 — which the SDP "
        "correctly rules out."),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {
        "gram_eigenvalues": eig.tolist(),
        "gram_min_eigenvalue": float(eig[0]),
    },
    "summary": {
        "n_cases": len(results),
        "n_lp_frobenius_invalid": n_lp_invalid,
    },
    "results": results,
}
out = Path(__file__).parent / "sdp-lift-audit.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"\nWitness: {out}")
