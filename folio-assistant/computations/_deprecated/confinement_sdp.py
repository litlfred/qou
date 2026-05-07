#!/usr/bin/env python3
"""
Confinement operator selection as a proper SDP — upgrade of
``confinement-lp.py``.

The original LP is:

    min  tᵀ x
    s.t. 1ᵀ x = n_target
         G x ≥ 0        (componentwise — this is LP-form)

The author of confinement-lp.py noted that the Gram matrix G has a
**negative eigenvalue** at q₀ ≈ 1.11, so componentwise G·x ≥ 0 is a
weaker certificate than the true quadratic Frobenius positivity
xᵀG x ≥ 0.  The LP therefore exploits degenerate directions and
finds solutions that aren't realisable braid-group elements (see
docs/ilp-sdp-audit.md, confinement-lp.py:405-423).

This module runs a Lasserre moment relaxation SDP:

    M = [[1, xᵀ], [x, X]] ∈ S^7_+
    M ⪰ 0                               (moment matrix PSD)
    M[0,0] = 1
    sum(x) = n_target                   (net — same as LP)
    G·x ≥ 0                              (LP Frobenius — same as LP)
    tr(G · X) ≥ 0                        (SDP Frobenius — new)
    min tᵀx                              (same objective)

The new constraint tr(G · X) ≥ 0 is exactly the quadratic Frobenius
certificate that the LP couldn't express.  If the LP solution happens
to lie in the positive cone of G, both give the same answer; if not,
the SDP rejects the LP degeneracy.

Compares SDP to LP on the same two cases (proton and neutron), reports
whether the SDP reaches the B₃ reference solution.
"""
from __future__ import annotations

import json
import sys
import numpy as np
import cvxpy as cp
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

# Reuse NF-basis, Gram builder, typed-crossing machinery from the LP
# module.  ``confinement-lp.py`` has a hyphen in its name, so use
# importlib.
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "confinement_lp_mod",
    Path(__file__).parent / "confinement-lp.py")
# confinement-lp.py runs its top-level LP loop on import — that's
# noisy but harmless.  Suppress stdout.
import os
_prev_stdout = os.dup(1)
_null = os.open(os.devnull, os.O_WRONLY)
os.dup2(_null, 1)
try:
    _cmod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_cmod)
finally:
    os.dup2(_prev_stdout, 1)
    os.close(_null)
    os.close(_prev_stdout)

NF_BASIS = _cmod.NF_BASIS
NF_NAMES = _cmod.NF_NAMES
TR_M_BASIS = _cmod.TR_M_BASIS
apply_typed_crossings = _cmod.apply_typed_crossings
expand_inverse = _cmod.expand_inverse
reduce_nf = _cmod.reduce_nf
to_vec = _cmod.to_vec
G = _cmod.G
b3_vec = _cmod.b3_vec


def solve_sdp(target_net: float, *, solver: str = "CLARABEL",
                bounds: tuple[float, float] = (-10.0, 10.0)
                ) -> dict:
    """Lasserre-moment SDP relaxation of the confinement LP."""
    x = cp.Variable(6)
    X = cp.Variable((6, 6), symmetric=True)
    # Moment matrix: M = [[1, xᵀ], [x, X]] ⪰ 0
    M = cp.bmat([[np.ones((1, 1)), cp.reshape(x, (1, 6))],
                   [cp.reshape(x, (6, 1)), X]])

    constraints = [
        M >> 0,                        # moment matrix PSD
        X >> 0,                        # redundant but tightens
        cp.sum(x) == target_net,       # net
        G @ x >= 0,                    # LP Frobenius (componentwise)
        cp.trace(G @ X) >= 0,          # SDP Frobenius (quadratic)
        x >= bounds[0],
        x <= bounds[1],
    ]
    objective = cp.Minimize(TR_M_BASIS @ x)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=solver)
    except cp.error.SolverError as e:
        return {"status": "solver_error", "error": str(e)}
    if prob.status not in {"optimal", "optimal_inaccurate"}:
        return {"status": prob.status}
    x_opt = np.asarray(x.value).flatten()
    X_opt = np.asarray(X.value)
    return {
        "status": prob.status,
        "objective": float(prob.value),
        "x": x_opt.tolist(),
        "X": X_opt.tolist(),
        "G_x": (G @ x_opt).tolist(),
        "tr_G_X": float(np.trace(G @ X_opt)),
        "moment_rank_numeric": int(
            np.sum(np.linalg.svd(X_opt, compute_uv=False) > 1e-6)),
    }


def solve_lp(target_net: float,
               bounds: tuple[float, float] = (-10.0, 10.0)) -> dict:
    """Reference LP with cvxpy (same objective / constraints)."""
    x = cp.Variable(6)
    constraints = [
        cp.sum(x) == target_net,
        G @ x >= 0,
        x >= bounds[0],
        x <= bounds[1],
    ]
    prob = cp.Problem(cp.Minimize(TR_M_BASIS @ x), constraints)
    try:
        prob.solve(solver="HIGHS")
    except cp.error.SolverError as e:
        return {"status": "solver_error", "error": str(e)}
    if prob.status not in {"optimal", "optimal_inaccurate"}:
        return {"status": prob.status}
    x_opt = np.asarray(x.value).flatten()
    return {
        "status": prob.status,
        "objective": float(prob.value),
        "x": x_opt.tolist(),
        "G_x": (G @ x_opt).tolist(),
        "xT_G_x": float(x_opt @ G @ x_opt),
    }


def print_nf(label: str, vec):
    vec = np.asarray(vec)
    parts = [f"{val:+.6f}·{nm}"
              for nm, val in zip(NF_NAMES, vec) if abs(val) > 1e-9]
    print(f"  {label}: {' '.join(parts)}  [net={vec.sum():+.6f}]")


if __name__ == "__main__":
    print("=" * 90)
    print("CONFINEMENT OPERATOR — PROPER SDP (Lasserre moment relaxation)")
    print("=" * 90)

    # Gram diagnostics.
    eig = np.sort(np.linalg.eigvals(G).real)
    print(f"\nGram eigenvalues: {eig}")
    print(f"  min eigenvalue = {eig[0]:+.6f}  "
          f"({'NEGATIVE — G is not PSD' if eig[0] < -1e-9 else 'non-negative'})")

    CASES = [
        ("PROTON (uud)",  ['u', 'u', 'd']),
        ("NEUTRON (udd)", ['u', 'd', 'd']),
    ]

    results = []
    for name, quark_types in CASES:
        print(f"\n{'=' * 90}")
        print(f"  {name}")
        print("=" * 90)

        # Target net from B₃ + typed crossings (same as LP).
        b3_confined = apply_typed_crossings(b3_vec, quark_types)
        target_net = float(np.sum(b3_confined))
        print(f"  Target net (from B₃): {target_net:+.10f}")
        print_nf("B₃ reference", b3_vec)

        # LP baseline
        print(f"\n  ── LP baseline ──")
        lp = solve_lp(target_net)
        if lp.get("status") not in {"optimal", "optimal_inaccurate"}:
            print(f"  LP status: {lp.get('status')}")
        else:
            print(f"  LP objective (tr_M): {lp['objective']:+.10f}")
            print_nf("LP solution x*", lp["x"])
            print(f"  xᵀ G x = {lp['xT_G_x']:+.10f}"
                  f" ({'≥ 0 (Frobenius-valid)' if lp['xT_G_x'] >= -1e-9 else '< 0 — Frobenius-INVALID'})")
            diff = np.asarray(lp["x"]) - b3_vec
            print(f"  max|LP − B₃| = {np.max(np.abs(diff)):.6f}")

        # SDP
        print(f"\n  ── SDP (moment-matrix relaxation) ──")
        sdp = solve_sdp(target_net)
        if sdp.get("status") not in {"optimal", "optimal_inaccurate"}:
            print(f"  SDP status: {sdp.get('status')}")
        else:
            print(f"  SDP objective (tr_M): {sdp['objective']:+.10f}")
            print_nf("SDP solution x*", sdp["x"])
            print(f"  tr(G · X) = {sdp['tr_G_X']:+.10f} ≥ 0 (SDP Frobenius)")
            print(f"  Moment-matrix numeric rank: {sdp['moment_rank_numeric']}"
                  f" ({'rank-1 ≡ LP would recover' if sdp['moment_rank_numeric'] == 1 else 'higher rank = SDP-only solution'})")
            diff_sdp = np.asarray(sdp["x"]) - b3_vec
            print(f"  max|SDP − B₃| = {np.max(np.abs(diff_sdp)):.6f}")

            # Apply typed crossings
            sdp_confined = apply_typed_crossings(np.asarray(sdp["x"]),
                                                    quark_types)
            print_nf("SDP nucleon", sdp_confined)
            print_nf("B₃  nucleon", b3_confined)
            cdiff = np.max(np.abs(np.asarray(sdp_confined)
                                   - np.asarray(b3_confined)))
            print(f"  max|nucleon diff| = {cdiff:.10f}")

        # Comparison
        if (lp.get("status") in {"optimal", "optimal_inaccurate"} and
              sdp.get("status") in {"optimal", "optimal_inaccurate"}):
            print(f"\n  ── LP vs SDP ──")
            print(f"  LP  objective: {lp['objective']:+.10f}")
            print(f"  SDP objective: {sdp['objective']:+.10f}")
            gap = sdp['objective'] - lp['objective']
            print(f"  SDP − LP = {gap:+.10f}  "
                  f"({'SDP is tighter ✓' if gap > 1e-9 else 'same / LP already tight'})")

        results.append({"nucleon": name, "target_net": target_net,
                          "lp": lp, "sdp": sdp})

    witness = {
        "computation": "confinement-sdp",
        "description": (
            "Proper SDP (Lasserre moment-matrix relaxation) upgrade of "
            "confinement-lp.py.  Adds the quadratic Frobenius "
            "positivity constraint tr(G·X) ≥ 0 — which the LP cannot "
            "express because G has a negative eigenvalue at q₀.  "
            "Verifies the LP(PSD) = SDP-in-disguise claim from "
            "docs/ilp-sdp-audit.md by comparing LP and SDP solutions "
            "on proton and neutron cases."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": float(_cmod.q0), "HA": float(_cmod.HA),
                        "z": float(_cmod.z),
                        "gram_min_eigenvalue": float(eig[0]),
                        "gram_max_eigenvalue": float(eig[-1])},
        "results": results,
    }
    out = Path(__file__).parent / "confinement-sdp.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
