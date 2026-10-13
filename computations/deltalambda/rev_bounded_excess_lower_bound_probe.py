#!/usr/bin/env python3
r"""
rev_bounded_excess_lower_bound_probe.py — e_n := M_n - A sqrt(2n) >= -K3 for EVERY n >= 1:
the bounded-excess LOWER bound (qou-fxym, arc qou-3e6w / qou-hok7)

## What was open

#7731 (`rev_bounded_excess_upper_bound_probe.py`) proved `e_n <= K2 = 85.366` for every n.  The
lower half was proved only at triangular n (the staircase delta_k).  Its "next step" asked for a
shape between delta_k and delta_{k+1} with O(1) cost.  The obvious one-corner-at-a-time estimate
loses `2(A - E_2) - eps(1) = 0.4012` per corner, i.e. O(r).

## The shape

For n = T_k + r (0 <= r <= k) let

    lambda_{k,r} := delta_k with one outer corner added on each of its TOP r rows
                  = (k+1, k, ..., k-r+2, k-r, k-r-1, ..., 1)
                  = delta_{k+1} with row r+1 deleted.

## The argument (each step a stated identity or inequality; checks below verify each)

Notation as #7715 / #7731: L = ln q0, eps(x) = -log(1 - q0^{-2x}) (positive, decreasing),
F(x) = sum_{t<=x} eps(t), C = F(inf), A = sum eps(odd), and
    B := sum_{m>=0} m eps(2m+1),     rem_j := sum_{m>=j} (m-j) eps(2m+1)  (>= 0).

  (L1) STAIRCASE (Lean `StaircaseHookMultiset.staircase_hookSum`): the hook multiset of delta_j is
       {2m+1 with multiplicity j-m : m < j}, so  sum_c eps(h) = A j - B + rem_j.
  (L2) BETA-SET FORM (#7282 (I')):  sum_c eps(h) = sum_i F(beta_i) - sum_{i<j} eps(beta_i - beta_j).
       For lambda_{k,r} (l = k rows), with m := k - r:
           beta-set = O u E,  O = {1, 3, ..., 2m-1},  E = {2m+2, 2m+4, ..., 2k}.
  (L3) CLOSED FORM.  Splitting the pair sum into O-O, E-E and E-O, and using
       F(2m+2j) - sum_{s=j}^{m+j-1} eps(2s+1) = E2(<= m+j) + Aodd(<= j),   F(2j-1) = Aodd(<= j) + E2(<= j-1),
       where E2(<= p) = sum_{s<=p} eps(2s), Aodd(<= j) = sum_{s<=j} eps(2s-1), and (L1) twice:
           sum_c eps(h(lambda_{k,r})) = A k - 2B + rem_m + rem_r + X_{k,r},
           X_{k,r} := sum_{j=1}^{r} sum_{s=j}^{m+j} eps(2s)  >= 0.
       In particular  sum_c eps(h) >= A k - 2B.   (The per-corner loss of 0.4012 is exactly paid
       back by the second differences of eps on the r(r-1)/2 doubly-shifted cells.)
  (L4) NO ENERGY COST.  lambda_{k,r}'s cells fill anti-diagonals 1..k and r cells of diagonal k+1,
       so H(lambda_{k,r}) = P_k + r(k+1) = H_min(n) (#7731 (A), attained by delta_k + r outer corners).
  (L5) ASSEMBLY.  M_n >= Psi(lambda_{k,r}) = sum_c eps(h) - F(n) >= A k - 2B - C, and
       2n <= 2T_k + 2k = k^2 + 3k < (k + 3/2)^2, so A sqrt(2n) < A k + 3A/2:

           e_n = M_n - A sqrt(2n)  >=  -K3,    K3 := 3A/2 + 2B + C        for every n >= 1.

With #7731:  -K3 <= e_n <= K2  for every n >= 1.  The excess is BOUNDED on both sides, so
M_n = A sqrt(2n) + O(1).  NOT the conjectured limit kappa = -10.72317, NOT convergence of e_n.

## Checks

  L1  constants A, B, C, K3 and the identity A + E2 = C; tail terms.
  L2  (L1) staircase closed form vs brute-force hooks, j <= N_SHAPE.
  L3  (L2)+(L3): lambda_{k,r} is a partition of T_k + r; its beta-set is O u E; the closed form equals
      the brute-force hook sum for every k <= N_SHAPE, 0 <= r <= k (60 dps).
  L4  H(lambda_{k,r}) = H_min(n) = P_k + r(k+1), and lambda_{k,r} = delta_k + r outer corners.
  L5  e_n >= Psi(lambda_{k,r}) - A sqrt(2n) >= -K3 for n <= N_BIG (closed form, no enumeration),
      and against exact M_n by full partition scan for n <= N_SCAN (how close lambda_{k,r} is to the
      maximiser is reported).
  L6  the naive per-corner estimate eps(1) - 2(A - E2) = -0.4012 < 0, recorded so that the O(r)
      route is not re-attempted, and the exact repayment identity
      sum_{g>=1} [eps(2g-1) - 2 eps(2g) + eps(2g+1)] = 2(A - E2) - eps(1).

Arithmetic: mpmath 60 dps for eps-valued quantities; partition data exact integers.  No float64.
Witness: computations/rev-bounded-excess-lower-bound.witness.json.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from mpmath import mp  # noqa: E402

import rev_sharp_coefficient_upper_bound_probe as base  # noqa: E402  (sets mp.dps = 60)
from zn_hook_length_closed_form_probe import hooks, partitions  # noqa: E402

mp.dps = 60
Q0, LNQ = base.Q0, base.LNQ
EPS, F = base.EPS, base.F
A_CONST, C_CONST, E2_CONST = base.A_CONST, base.C_CONST, base.E2_CONST
tri, k_r_of = base.tri, base.k_r_of
NEPS = len(EPS)

N_SHAPE = int(os.environ.get("REV_LOWER_N_SHAPE", "40"))
N_SCAN = int(os.environ.get("REV_LOWER_N_SCAN", "40"))
N_BIG = int(os.environ.get("REV_LOWER_N_BIG", "20000"))

MMAX = (NEPS - 2) // 2
B_CONST = mp.fsum(m * EPS[2 * m + 1] for m in range(0, MMAX))
K3 = 3 * A_CONST / 2 + 2 * B_CONST + C_CONST


def rem(j: int):
    return mp.fsum((m - j) * EPS[2 * m + 1] for m in range(j, MMAX))


def lam_kr(k: int, r: int):
    """delta_k plus one outer corner on each of its top r rows."""
    lam = [k + 1 - i for i in range(r)] + [k - i for i in range(r, k)]
    return tuple(x for x in lam if x > 0)


def staircase(j: int):
    return tuple(range(j, 0, -1))


def beta_set(lam):
    ell = len(lam)
    return sorted(lam[i] + ell - (i + 1) for i in range(ell))


def X_kr(k: int, r: int):
    m = k - r
    return mp.fsum(EPS[2 * s] for j in range(1, r + 1) for s in range(j, m + j + 1))


def closed_form(k: int, r: int):
    m = k - r
    return A_CONST * k - 2 * B_CONST + rem(m) + rem(r) + X_kr(k, r)


def cell_H(lam):
    return sum(i + j - 1 for i in range(1, len(lam) + 1) for j in range(1, lam[i - 1] + 1))


def main() -> int:
    t0 = time.time()
    results = []
    tol = mp.mpf(10) ** (-(mp.dps - 15))

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}", flush=True)

    print("=" * 78)
    print("rev_bounded_excess_lower_bound_probe -- e_n = M_n - A sqrt(2n) >= -K3")
    print("=" * 78)

    tailB = MMAX * EPS[2 * MMAX - 1]
    check("L1_constants",
          abs(A_CONST + E2_CONST - C_CONST) < tol and tailB < tol,
          f"A = {mp.nstr(A_CONST, 20)}; B = sum m eps(2m+1) = {mp.nstr(B_CONST, 20)}; "
          f"C = {mp.nstr(C_CONST, 20)}; K3 = 3A/2 + 2B + C = {mp.nstr(K3, 20)}; "
          f"|A + E2 - C| = {mp.nstr(abs(A_CONST + E2_CONST - C_CONST), 3)}; B tail term {mp.nstr(tailB, 3)}.")

    # L2 staircase
    worst2 = mp.mpf(0)
    for j in range(0, N_SHAPE + 1):
        lam = staircase(j)
        S = mp.fsum(EPS[h] for h in hooks(lam)) if lam else mp.mpf(0)
        worst2 = max(worst2, abs(S - (A_CONST * j - B_CONST + rem(j))))
    check("L2_staircase_closed_form",
          worst2 < tol,
          f"sum_c eps(h(delta_j)) = A j - B + rem_j for j = 0..{N_SHAPE}: worst |diff| {mp.nstr(worst2, 3)}.")

    # L3 lambda_{k,r}
    worst3 = mp.mpf(0)
    v_part = v_beta = 0
    n_kr = 0
    for k in range(1, N_SHAPE + 1):
        for r in range(0, k + 1):
            lam = lam_kr(k, r)
            n_kr += 1
            if sum(lam) != tri(k) + r or any(lam[i] < lam[i + 1] for i in range(len(lam) - 1)):
                v_part += 1
            m = k - r
            if beta_set(lam) != sorted(list(range(1, 2 * m, 2)) + list(range(2 * m + 2, 2 * k + 1, 2))):
                v_beta += 1
            S = mp.fsum(EPS[h] for h in hooks(lam))
            worst3 = max(worst3, abs(S - closed_form(k, r)))
    check("L3_lambda_kr_closed_form",
          v_part == 0 and v_beta == 0 and worst3 < tol,
          f"{n_kr} shapes (k <= {N_SHAPE}, 0 <= r <= k): partition of T_k + r violations {v_part}; "
          f"beta-set = O u E violations {v_beta}; |hook sum - (A k - 2B + rem_m + rem_r + X)| worst "
          f"{mp.nstr(worst3, 3)}.")

    # L4 energy
    v_H = v_corner = 0
    for k in range(1, N_SHAPE + 1):
        for r in range(0, k + 1):
            lam = lam_kr(k, r)
            if cell_H(lam) != sum(hooks(lam)) or cell_H(lam) != sum(d * d for d in range(1, k + 1)) + r * (k + 1):
                v_H += 1
            st = staircase(k)
            diff = [lam[i] - (st[i] if i < len(st) else 0) for i in range(len(lam))]
            if sorted(diff) != [0] * (len(lam) - r) + [1] * r:
                v_corner += 1
    check("L4_no_energy_cost",
          v_H == 0 and v_corner == 0,
          f"H(lambda_kr) = sum hooks = P_k + r(k+1) = H_min(n): violations {v_H}; lambda_kr = delta_k + "
          f"r outer corners: violations {v_corner}.")

    # L5 assembly: closed form for large n, exact M_n for small n
    worst_e = None
    for n in range(1, N_BIG + 1):
        k, r = k_r_of(n)
        # Psi(lambda_kr) >= A k - 2B - F(n) (drop rem, X >= 0); exact lower value used for small n below
        low = A_CONST * k - 2 * B_CONST - F(n) - A_CONST * mp.sqrt(2 * n)
        worst_e = low if worst_e is None or low < worst_e else worst_e
    rows = []
    v_scan = 0
    for n in range(1, N_SCAN + 1):
        k, r = k_r_of(n)
        Hmin = sum(d * d for d in range(1, k + 1)) + r * (k + 1)
        Fn = F(n)
        Mn, argM = None, None
        for lam in partitions(n):
            psi = mp.fsum(EPS[h] for h in hooks(lam)) - Fn - LNQ * (sum(hooks(lam)) - Hmin)
            if Mn is None or psi > Mn:
                Mn, argM = psi, lam
        psi_kr = closed_form(k, r) - Fn
        e_n = Mn - A_CONST * mp.sqrt(2 * n)
        if not (Mn + tol >= psi_kr and e_n >= -K3):
            v_scan += 1
        rows.append({"n": n, "k": k, "r": r, "M_n": mp.nstr(Mn, 20), "argmax": list(argM),
                     "Psi_lambda_kr": mp.nstr(psi_kr, 20), "gap_M_minus_Psi_kr": mp.nstr(Mn - psi_kr, 12),
                     "e_n": mp.nstr(e_n, 15), "lower_bound_minus_K3": mp.nstr(-K3, 15)})
    maxgap = max(rows, key=lambda rw: mp.mpf(rw["gap_M_minus_Psi_kr"]))
    check("L5_assembly",
          worst_e >= -K3 and v_scan == 0,
          f"A k - 2B - F(n) - A sqrt(2n) >= -K3 for n = 1..{N_BIG}: min {mp.nstr(worst_e, 12)} vs "
          f"-K3 = {mp.nstr(-K3, 12)}.  Exact M_n (full scan) >= Psi(lambda_kr) and e_n >= -K3 for "
          f"n = 1..{N_SCAN}: violations {v_scan}; largest M_n - Psi(lambda_kr) = "
          f"{maxgap['gap_M_minus_Psi_kr']} at n = {maxgap['n']}.")

    # L6 naive route and the repayment identity
    naive = EPS[1] - 2 * (A_CONST - E2_CONST)
    second = mp.fsum(EPS[2 * g - 1] - 2 * EPS[2 * g] + EPS[2 * g + 1] for g in range(1, MMAX))
    check("L6_naive_per_corner_loss_and_repayment",
          naive < 0 and abs(second - (2 * (A_CONST - E2_CONST) - EPS[1])) < tol,
          f"eps(1) - 2(A - E2) = {mp.nstr(naive, 15)} < 0 (one corner at a time loses O(r)); "
          f"sum_g second differences eps(2g-1) - 2eps(2g) + eps(2g+1) = {mp.nstr(second, 15)} = "
          f"2(A - E2) - eps(1): the doubly-shifted cells pay the loss back exactly.")

    n_ok = sum(1 for x in results if x["pass"])
    print("\n" + "=" * 78)
    print(f"{n_ok}/{len(results)} checks passed   [{time.time() - t0:.1f}s]")
    print(f"VERDICT: e_n >= -K3 = {mp.nstr(-K3, 12)} for every n >= 1; with #7731, -K3 <= e_n <= K2. "
          f"NOT the limit kappa = -10.72317, NOT convergence of e_n.")
    print("=" * 78)

    payload = {
        "probe": "rev_bounded_excess_lower_bound_probe",
        "bean": ["qou-fxym", "qou-3e6w", "qou-hok7"],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton",
        "dps": mp.dps,
        "constants": {
            "A": mp.nstr(A_CONST, 40), "B": mp.nstr(B_CONST, 40), "C": mp.nstr(C_CONST, 40),
            "E2": mp.nstr(E2_CONST, 40), "K3": mp.nstr(K3, 40), "ln_q0": mp.nstr(LNQ, 40),
        },
        "statements": {
            "(L1)": "sum_c eps(h(delta_j)) = A j - B + rem_j (Lean staircase_hookSum)",
            "(L2)": "beta-set of lambda_{k,r} = {1,3,...,2m-1} u {2m+2,...,2k}, m = k - r",
            "(L3)": "sum_c eps(h(lambda_{k,r})) = A k - 2B + rem_m + rem_r + X_{k,r}, X >= 0",
            "(L4)": "H(lambda_{k,r}) = H_min(n): no energy penalty",
            "main": "e_n = M_n - A sqrt(2n) >= -(3A/2 + 2B + C) for every n >= 1",
            "not_established": "e_n -> kappa; the value of liminf/limsup e_n; a Lean formalisation of (L2)-(L3)",
        },
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "n_shape": N_SHAPE,
        "n_scan": N_SCAN,
        "n_big": N_BIG,
        "table": rows,
    }
    out = os.path.join(_COMPUTATIONS, "rev-bounded-excess-lower-bound.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
