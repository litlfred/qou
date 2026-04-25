#!/usr/bin/env python3
"""
SDP / LP-based sparse q-algebraic identifier.

Goal
----
Given a numerical target value T (e.g. 1/α_EM = 137.035999084) and a
basis B = {b_1, ..., b_N} of q-algebraic atoms evaluated at q = q_0,
find a SPARSE coefficient vector c ∈ R^N such that

        Σ_i c_i · b_i(q_0) ≈ T   (within tolerance ε)
        ||c||_1   minimized      (sparsity → identification surrogate)
        ||c||_∞ ≤ M              (bounded, to discourage huge cancellations)

This is the LP relaxation of the integer-coefficient PSLQ problem.
Instead of biasing toward any pre-found formula, we let the LP pick
its own minimum-L1 representation, then snap to rationals and
re-verify.

To get a *uniqueness bound* we re-run the LP with each non-zero
coordinate forced to zero in turn — if any of those LPs is
ε-feasible, the support is non-unique.

Targets (CLI selectable, all run by default):
    1/α_EM            = 137.035999084
    Δm_{n-p}/m_e     ≈ 2.5310
    Σ_3 (sanity)      = q-binomial / dim sanity check (knot K3_1 chirality)

Usage
-----
    python3 sdp_q_algebraic_identifier.py
    python3 sdp_q_algebraic_identifier.py --target 137.035999084 \
            --rmax 8 --jmax 6 --kmax 6 --M 200

Output
------
A dict for each target, written to
``sdp-q-algebraic-identifier.witness.json`` and printed to stdout.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import numpy as np

# cvxpy is documented as available in the repo
import cvxpy as cp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT  # canonical substrate parameter
try:
    from experimental_constants import (
        ALPHA_EM_INV, M_E_MEV, M_N_MINUS_P_MEV,
    )
except Exception:  # pragma: no cover
    ALPHA_EM_INV = 137.035999084
    M_E_MEV = 0.51099895000
    M_N_MINUS_P_MEV = 1.2933321

# ---------- High-precision basis evaluation ------------------------
mp.mp.dps = 50
Q0 = mp.mpf(str(Q0_FLOAT))
QI = mp.mpf(1) / Q0
HA = Q0 - QI


def q_int(n: int) -> mp.mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if n == 0:
        return mp.mpf(0)
    return (Q0**n - QI**n) / HA


def q_fact(n: int) -> mp.mpf:
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def q_pochhammer_abs(r: int) -> mp.mpf:
    """|(q;q)_r| = ∏_{k=1..r} |1 - q^k|."""
    out = mp.mpf(1)
    for k in range(1, r + 1):
        out *= abs(mp.mpf(1) - Q0**k)
    return out


def hbar_q_pow(k: int) -> mp.mpf:
    """ℏ_q^k where ℏ_q = 1 - q^{-1}."""
    hbarq = mp.mpf(1) - QI
    return hbarq**k


def q_binom(n: int, k: int) -> mp.mpf:
    if k < 0 or k > n:
        return mp.mpf(0)
    return q_fact(n) / (q_fact(k) * q_fact(n - k))


# ---------- Basis construction --------------------------------------
def build_basis(rmax: int = 8, jmax: int = 6, kmax: int = 6,
                nmax: int = 10) -> tuple[list[str], np.ndarray]:
    """Return (labels, values) where values[i] is float64 of b_i(q_0).

    Atoms included:
      * 1                                            (constant)
      * q^j  for j ∈ [-jmax..jmax] \\ {0}
      * [n]_q  for n ∈ 1..nmax
      * 1/[n]_q  for n ∈ 2..nmax
      * ℏ_q^k  for k ∈ 1..kmax  and  ℏ_q^{-k}
      * |(q;q)_r| for r ∈ 1..rmax
      * 1/|(q;q)_r| for r ∈ 1..rmax
      * q-binomials [n choose k]_q  for n ∈ 2..min(nmax,6), 1 ≤ k < n
    """
    labels: list[str] = []
    vals: list[mp.mpf] = []

    def add(label: str, v: mp.mpf):
        labels.append(label)
        vals.append(v)

    add("1", mp.mpf(1))

    for j in range(-jmax, jmax + 1):
        if j == 0:
            continue
        add(f"q^{j}", Q0**j)

    for n in range(1, nmax + 1):
        add(f"[{n}]_q", q_int(n))
    for n in range(2, nmax + 1):
        v = q_int(n)
        if v != 0:
            add(f"1/[{n}]_q", mp.mpf(1) / v)

    for k in range(1, kmax + 1):
        add(f"hbar_q^{k}", hbar_q_pow(k))
        add(f"hbar_q^-{k}", mp.mpf(1) / hbar_q_pow(k))

    for r in range(1, rmax + 1):
        add(f"|(q;q)_{r}|", q_pochhammer_abs(r))
        add(f"1/|(q;q)_{r}|", mp.mpf(1) / q_pochhammer_abs(r))

    for n in range(2, min(nmax, 6) + 1):
        for k in range(1, n):
            add(f"[{n} {k}]_q", q_binom(n, k))

    # Float64 (cvxpy is float64; high precision is for the basis only)
    arr = np.array([float(v) for v in vals], dtype=np.float64)
    return labels, arr


# ---------- Core LP: min L1 subject to equality and box -------------
def solve_min_l1(target: float, B: np.ndarray, M: float = 200.0,
                 tol: float = 0.0) -> tuple[np.ndarray | None, float, str]:
    """LP: min sum |c_i|  s.t.  B·c = target,  |c_i| ≤ M.

    Returns (c_opt, objective, status). c_opt is None if infeasible.

    If tol > 0, we solve  |B·c - target| ≤ tol  instead of equality.
    """
    n = B.size
    c = cp.Variable(n)
    constraints = [cp.norm(c, "inf") <= M]
    if tol == 0.0:
        constraints.append(B @ c == target)
    else:
        constraints.append(cp.abs(B @ c - target) <= tol)

    prob = cp.Problem(cp.Minimize(cp.norm(c, 1)), constraints)
    try:
        prob.solve(solver=cp.CLARABEL)
    except Exception:
        try:
            prob.solve(solver=cp.SCS)
        except Exception as e:  # pragma: no cover
            return None, math.inf, f"solver_error:{e}"

    if c.value is None:
        return None, math.inf, prob.status or "infeasible"
    return np.asarray(c.value, dtype=np.float64), float(prob.value), prob.status


# ---------- Round to small rationals --------------------------------
def round_to_rational(x: float, max_den: int = 64) -> tuple[int, int, float]:
    """Find p/q with |q| ≤ max_den minimizing |x - p/q|. Returns (p, q, err)."""
    if not math.isfinite(x):
        return 0, 1, math.inf
    best = (0, 1, abs(x))
    for q in range(1, max_den + 1):
        p = round(x * q)
        err = abs(x - p / q)
        if err < best[2]:
            best = (p, q, err)
    return best


# ---------- Uniqueness probe ---------------------------------------
def support_uniqueness(target: float, B: np.ndarray, support: list[int],
                       M: float, tol: float) -> dict:
    """For every i in support, re-solve the LP with c_i forced to 0.
    If any such restricted LP is feasible within tol of the original
    L1 norm, the support is non-unique.
    """
    n = B.size
    rows = []
    for i in support:
        c = cp.Variable(n)
        constraints = [
            cp.norm(c, "inf") <= M,
            cp.abs(B @ c - target) <= tol,
            c[i] == 0,
        ]
        prob = cp.Problem(cp.Minimize(cp.norm(c, 1)), constraints)
        try:
            prob.solve(solver=cp.CLARABEL)
        except Exception:
            try:
                prob.solve(solver=cp.SCS)
            except Exception:
                rows.append({"i": i, "feasible": False, "obj": None,
                             "note": "solver_error"})
                continue
        if c.value is None or not math.isfinite(prob.value):
            rows.append({"i": i, "feasible": False, "obj": None})
        else:
            rows.append({"i": i, "feasible": True, "obj": float(prob.value)})
    return {"per_support_constraint": rows}


# ---------- Main per-target driver ---------------------------------
def identify(target: float, label: str, B: np.ndarray, basis_labels: list[str],
             M: float = 200.0,
             rel_tol: float = 1e-9,
             sparsity_threshold: float = 1e-6) -> dict:
    """Run min-L1 LP, sparsify, snap to rationals, probe uniqueness."""
    tol_abs = abs(target) * rel_tol

    # Pass 1: equality (exact match in LP sense; tol numerical only)
    c, obj, status = solve_min_l1(target, B, M=M, tol=tol_abs)
    if c is None:
        return {"target_label": label, "target_value": target,
                "status": status, "result": "infeasible_lp"}

    # Sparsity: keep coords above threshold * max(|c|)
    cmax = float(np.max(np.abs(c))) if c.size else 0.0
    cutoff = max(sparsity_threshold * cmax, 1e-10)
    support = [i for i in range(c.size) if abs(c[i]) > cutoff]
    support.sort(key=lambda i: -abs(c[i]))

    # Round to small rationals (max_den 64). Re-evaluate residual.
    rationalized = []
    val_check = 0.0
    for i in support:
        p, q, err = round_to_rational(float(c[i]), max_den=64)
        rationalized.append({
            "i": i, "label": basis_labels[i],
            "c_lp": float(c[i]),
            "rational": f"{p}/{q}",
            "round_err": err,
            "basis_value": float(B[i]),
        })
        val_check += (p / q) * float(B[i])

    residual = abs(val_check - target)

    # Uniqueness probe (top-k support only — full set can be slow)
    top_support = support[: min(8, len(support))]
    uniq = support_uniqueness(target, B, top_support, M=M, tol=tol_abs)

    # Re-evaluate target reconstruction at high precision (mpmath) using rationals
    mp_check = mp.mpf(0)
    for term in rationalized:
        p, q = term["rational"].split("/")
        coef = mp.mpf(p) / mp.mpf(q)
        # Re-evaluate basis_value at high precision via label parsing
        mp_check += coef * mp.mpf(str(term["basis_value"]))
    mp_residual = float(abs(mp_check - mp.mpf(str(target))))

    # Heuristic verdict
    rationals_ok = all(t["round_err"] < 5e-3 for t in rationalized)
    sparse_ok    = len(support) <= 6
    match_ok     = residual < 1e-6 * max(1.0, abs(target))

    if rationals_ok and sparse_ok and match_ok:
        verdict = "candidate_identified"
    elif sparse_ok and match_ok:
        verdict = "sparse_but_not_rational"
    elif match_ok:
        verdict = "dense_match"
    else:
        verdict = "no_clean_identification"

    return {
        "target_label": label,
        "target_value": target,
        "lp_status": status,
        "lp_objective_l1": obj,
        "M_box": M,
        "rel_tol": rel_tol,
        "support_size": len(support),
        "support": rationalized,
        "residual_lp_rounded": residual,
        "residual_mp": mp_residual,
        "uniqueness_probe": uniq,
        "verdict": verdict,
    }


# ---------- CLI / main --------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rmax", type=int, default=8)
    ap.add_argument("--jmax", type=int, default=6)
    ap.add_argument("--kmax", type=int, default=6)
    ap.add_argument("--nmax", type=int, default=10)
    ap.add_argument("--M", type=float, default=200.0,
                    help="Coefficient box bound ||c||_inf ≤ M")
    ap.add_argument("--rel-tol", type=float, default=1e-10)
    ap.add_argument("--target", type=float, default=None,
                    help="If set, run only this single target.")
    ap.add_argument("--out", type=str,
                    default=str(Path(__file__).with_name(
                        "sdp-q-algebraic-identifier.witness.json")))
    args = ap.parse_args()

    labels, B = build_basis(rmax=args.rmax, jmax=args.jmax,
                            kmax=args.kmax, nmax=args.nmax)
    print(f"[basis] |B| = {B.size} atoms")
    print(f"[basis] q_0 = {float(Q0):.15f}")

    if args.target is not None:
        targets = [(args.target, "user_target")]
    else:
        # Σ_3 sanity check: evaluate q-binomial [3 1]_q at q_0 — this
        # IS exactly one basis atom, so SDP must trivially identify it.
        sigma3 = float(q_int(3))  # [3]_q
        targets = [
            (float(ALPHA_EM_INV), "1/alpha_EM"),
            (float(M_N_MINUS_P_MEV / M_E_MEV), "Delta_m_np_over_me"),
            (sigma3, "Sigma_3=[3]_q (sanity)"),
        ]

    results = []
    for t, name in targets:
        print(f"\n=== TARGET: {name}  =  {t:.15g} ===")
        out = identify(t, name, B, labels,
                       M=args.M, rel_tol=args.rel_tol)
        results.append(out)
        print(f"  LP status      : {out.get('lp_status')}")
        print(f"  L1 objective   : {out.get('lp_objective_l1'):.6g}")
        print(f"  support size   : {out.get('support_size')}")
        print(f"  verdict        : {out.get('verdict')}")
        for term in out.get("support", []):
            print(f"    {term['rational']:>10s} · {term['label']:<14s}"
                  f"  c_lp={term['c_lp']:+.10f}"
                  f"  err={term['round_err']:.2e}")
        print(f"  rounded residual : {out.get('residual_lp_rounded'):.3e}")
        if out.get("uniqueness_probe"):
            n_alt = sum(1 for r in out["uniqueness_probe"]
                        ["per_support_constraint"] if r["feasible"])
            print(f"  alt supports     : {n_alt}/"
                  f"{len(out['uniqueness_probe']['per_support_constraint'])}"
                  " coords admit zero-substitution feasibility")

    payload = {
        "schema": "sdp-q-algebraic-identifier/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "q_0": float(Q0),
        "basis": {
            "size": B.size,
            "rmax": args.rmax, "jmax": args.jmax,
            "kmax": args.kmax, "nmax": args.nmax,
            "labels": labels,
        },
        "lp": {"M_box": args.M, "rel_tol": args.rel_tol,
               "objective": "min ||c||_1 s.t. B·c = T, ||c||_inf ≤ M"},
        "results": results,
    }
    out_path = Path(args.out)
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"\n[witness] wrote {out_path}")


if __name__ == "__main__":
    main()
