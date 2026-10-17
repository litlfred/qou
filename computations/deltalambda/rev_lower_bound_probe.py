#!/usr/bin/env python3
r"""
rev_lower_bound_probe.py — the matching LOWER bound  M_n >= A sqrt(2n) - K3  for EVERY n >= 1
(qou-fxym, arc qou-3e6w / qou-hok7)

## What was open

`rev_bounded_excess_upper_bound_probe.py` proved e_n := M_n - A sqrt(2n) <= K2 = 85.37.  The
lower side was closed only at TRIANGULAR n = T_k, where the staircase delta_k has the closed form
V(delta_k) = A k - B - F(n) + rem_k (`rev_staircase_closed_form_and_constant_term_probe.py`,
Lean `staircase_hookSum`).  For n = T_k + r, 1 <= r <= k, adding r outer corners to delta_k
one at a time costs O(r) = O(sqrt n) in the naive accounting.

## The family: a CONTIGUOUS corner block at the top

For 0 <= r <= k let mu(r, k-r) := delta_k plus its r TOP outer corners, i.e. row lengths
(1-indexed)  k+1, k, ..., k+2-r, k-r, k-r-1, ..., 1  (r + (k-r) = k rows).  Equivalently
(0-indexed cells, a := r, c := k - r):

    (i, j) in mu(a, c)   <=>   i + j < a + c   or   (i + j = a + c and i < a).

Its hooks split into THREE blocks (Lean `cornerBlock_hook_*`, `cornerBlock_hookSum`):

    i < a,  j <= c :  h = 2(a + c - i - j)        -> twice the hooks of an a x (c+1) RECTANGLE
    i < a,  j >  c :  h = 2(a + c - i - j) + 1    -> the staircase delta_a
    i >= a, j <= c :  h = 2(a + c - i - j) - 1    -> the staircase delta_c

so the hook multiset is  hooks(delta_a) + hooks(delta_c) + 2 * hooks(a x (c+1) rectangle).
This is why the contiguous block costs O(1) and the naive accounting O(r): the cells whose
hooks turned even all sit in ONE rectangle, and doubling its hooks sends eps(2h) to a convergent
series with positive terms, instead of r separate (eps(1) - 2D)-sized defects.

## The argument (each step a stated inequality; checks below verify each)

Notation as in the upper-bound probes: q0 proton pin, L = ln q0, t = q0^2, eps(m) = -log(1-t^-m),
A = sum_{j>=1} eps(2j-1), B = sum_{j>=1} (j-1) eps(2j-1), C = sum_{m>=1} eps(m), n = T_k + r,
0 <= r <= k, S_delta(m) := sum_{c in delta_m} eps(h(c)), R(m) := sum_{j>m} (j-1-m) eps(2j-1).

  (L1) HOOK DECOMPOSITION (Lean `cornerBlock_hookSum`, any g into an AddCommMonoid):
          sum_{c in mu(r,k-r)} eps(h(c)) = S_delta(r) + S_delta(k-r) + G(r, k-r),
          G(a, c) := sum_{i<a, j<=c} eps(2(i+j+1)) >= 0.
  (L2) STAIRCASE SERIES (staircase probe + Lean `staircase_hookSum`):
          S_delta(m) = A m - B + R(m),  R(m) >= 0.
  (L3) ZERO ENERGY:  H(mu(r,k-r)) = H_min(n)  (its cells are delta_k plus r cells on
       antidiagonal k+1, which is statement (A) of the upper-bound probe).  Hence
          Psi(mu) = sum eps(h) - F(n) >= A k - 2B - C + G + R(r) + R(k-r) >= A k - 2B - C,
       using F(n) <= C (eps > 0).
  (L4) ROOT:  2n = k^2 + k + 2r <= k^2 + 3k < (k + 3/2)^2,  so  A k > A sqrt(2n) - 3A/2.

  Assembled:   M_n >= Psi(mu(r, k-r)) >= A sqrt(2n) - K3,   K3 := 3A/2 + 2B + C,

for EVERY n >= 1 (r = 0 is the staircase itself).  Combined with the upper bound,

          -K3  <=  e_n = M_n - A sqrt(2n)  <=  K2      for every n >= 1.

So e_n is BOUNDED (both sides, explicit constants).  This does NOT prove e_n converges, nor
the value kappa = -10.72317 conjectured in #7294; K3 is a crude constant (it drops G, R and
uses the worst case of sqrt(2n) - k).  The measured family deficit is much smaller (L6 below).

## Checks

  L0  constants A, B, C, K3 (geometric series; tail terms reported).
  L1  hook-multiset decomposition, by enumeration, for every (a, c) with a + c <= N_DECOMP
      (exact integer multisets); and the three per-region hook formulas.
  L2  the staircase series S_delta(m) = A m - B + R(m), R(m) >= 0, m <= N_DECOMP, 60 dps.
  L3  H(mu(r, k-r)) = H_min(n) against brute-force H_min, all n <= N_SCAN; |mu| = n.
  L4  2n < (k + 3/2)^2, exact integers, n <= N_ROOT.
  L5  per-n chain on all n <= N_SCAN against brute-force M_n:
          M_n >= Psi(mu) = [closed (L1)+(L2) form] >= A k - 2B - C >= A sqrt(2n) - K3.
  L6  closed-form scan (no enumeration) to large n: Psi(mu) via (L1)+(L2) for all r, k <= K_SCAN
      and sampled k up to K_FAR; reports min of Psi(mu) - A sqrt(2n) (measured family deficit).
  L7  measured (NOT proved): the gain Psi(mu(r,k-r)) - Psi(delta_k) + (F(n) - F(T_k)) >= 0 for
      every r, k <= K_SCAN, i.e. the top corner block never lowers the hook-eps sum.

Arithmetic: mpmath 60 dps for eps-valued quantities; partition data and (L1), (L3), (L4) exact
(ints).  No float64.  Witness: computations/rev-lower-bound.witness.json.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/BraidKnot/CornerBlockHookMultiset.lean
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter
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
EPS, F, A_CONST, C_CONST = base.EPS, base.F, base.A_CONST, base.C_CONST
_NEPS = len(EPS)
tri, k_r_of = base.tri, base.k_r_of

B_CONST = mp.fsum(((m + 1) // 2 - 1) * EPS[m] for m in range(1, _NEPS, 2))
K3 = 3 * A_CONST / 2 + 2 * B_CONST + C_CONST

N_SCAN = int(os.environ.get("REV_LOWER_N_SCAN", "40"))
N_DECOMP = int(os.environ.get("REV_LOWER_N_DECOMP", "60"))
N_ROOT = int(os.environ.get("REV_LOWER_N_ROOT", "200000"))
K_SCAN = int(os.environ.get("REV_LOWER_K_SCAN", "120"))
K_FAR = int(os.environ.get("REV_LOWER_K_FAR", "2000"))
HTRUNC = 1000  # eps(2h) for h > HTRUNC is < t^(-2000), far below 10^-60


def eps(m):
    return EPS[m] if 0 < m < _NEPS else mp.mpf(0)


def mu_shape(a, c):
    """Row lengths of mu(a, c) = delta_{a+c} plus its top a outer corners (0 <= a, c)."""
    k = a + c
    rows = [k + 1 - i for i in range(a)] + [k - i for i in range(a, k)]
    return tuple(x for x in rows if x > 0)


def stair_hooks(m):
    return Counter({2 * j - 1: m + 1 - j for j in range(1, m + 1)})


def rect_double_hooks(a, c):
    """2 * hooks of an a x (c+1) rectangle: h = 2(i+j+1), i < a, j <= c."""
    out = Counter()
    for i in range(a):
        for j in range(c + 1):
            out[2 * (i + j + 1)] += 1
    return out


_JMAX = _NEPS // 2          # odd arguments 2j-1 < _NEPS
_TAILA = [mp.mpf(0)] * (_JMAX + 2)   # _TAILA[m] = sum_{j>m} eps(2j-1)
_R = [mp.mpf(0)] * (_JMAX + 2)       # _R[m] = sum_{j>m} (j-1-m) eps(2j-1)
for _m in range(_JMAX - 1, -1, -1):
    _TAILA[_m] = _TAILA[_m + 1] + eps(2 * _m + 1)
    _R[_m] = _R[_m + 1] + _TAILA[_m + 1]   # R(m) - R(m+1) = sum_{j>m+1} eps(2j-1)


def R_tail(m):
    return _R[m] if m <= _JMAX else mp.mpf(0)


def R_tail_direct(m):
    return mp.fsum((j - 1 - m) * eps(2 * j - 1) for j in range(m + 1, _JMAX + 1))


def S_delta_closed(m):
    return A_CONST * m - B_CONST + R_tail(m)


def G_val(a, c):
    """G(a,c) = sum_{i<a, j<=c} eps(2(i+j+1)) = sum_h mult(h) eps(2h), mult = #{i+j+1 = h}."""
    if a == 0:
        return mp.mpf(0)
    tot = mp.mpf(0)
    for h in range(1, min(a + c, HTRUNC) + 1):
        lo, hi = max(0, h - 1 - c), min(a - 1, h - 1)
        if hi >= lo:
            tot += (hi - lo + 1) * eps(2 * h)
    return tot


def psi_family_closed(k, r):
    n = tri(k) + r
    return S_delta_closed(r) + S_delta_closed(k - r) + G_val(r, k - r) - F(n)


def main() -> int:
    t0 = time.time()
    results = []

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}", flush=True)

    print("=" * 78)
    print("rev_lower_bound_probe -- M_n >= A sqrt(2n) - K3 via the top corner block")
    print("=" * 78)
    print(f"  q0 = {mp.nstr(Q0, 25)} (proton)  A = {mp.nstr(A_CONST, 15)}  B = {mp.nstr(B_CONST, 15)}"
          f"  C = {mp.nstr(C_CONST, 15)}  K3 = {mp.nstr(K3, 15)}", flush=True)
    tol = mp.mpf(10) ** (-(mp.dps - 15))

    tailA = EPS[_NEPS - 1] * _NEPS * _NEPS
    check("L0_constants",
          A_CONST > 0 and B_CONST > 0 and C_CONST > 0 and tailA < tol,
          f"A = {mp.nstr(A_CONST, 20)}; B = {mp.nstr(B_CONST, 20)}; C = {mp.nstr(C_CONST, 20)}; "
          f"K3 = 3A/2 + 2B + C = {mp.nstr(K3, 20)}; truncation at m < {_NEPS}, tail bound "
          f"{mp.nstr(tailA, 3)}.")

    # L1 — hook decomposition and per-region formulas (exact)
    v_dec = v_reg = n_pairs = 0
    for k in range(0, N_DECOMP + 1):
        for a in range(0, k + 1):
            c = k - a
            lam = mu_shape(a, c)
            n_pairs += 1
            got = Counter(hooks(lam))
            pred = stair_hooks(a) + stair_hooks(c) + rect_double_hooks(a, c)
            if got != pred:
                v_dec += 1
            # per-region formulas, 0-indexed
            conj = [sum(1 for x in lam if x > j) for j in range(lam[0] if lam else 0)]
            for i, row in enumerate(lam):
                for j in range(row):
                    if not (i + j < a + c or (i + j == a + c and i < a)):
                        v_reg += 1
                    h = row - j + conj[j] - i - 1
                    if i < a and j <= c:
                        want = 2 * (a + c - i - j)
                    elif i < a:
                        want = 2 * (a + c - i - j) + 1
                    else:
                        want = 2 * (a + c - i - j) - 1
                    if h != want:
                        v_reg += 1
            # membership converse: every cell with the predicate is in the shape
            for i in range(k + 1):
                for j in range(k + 1):
                    if (i + j < a + c or (i + j == a + c and i < a)) and not (i < len(lam) and j < lam[i]):
                        v_reg += 1
    check("L1_corner_block_hook_decomposition",
          v_dec == 0 and v_reg == 0,
          f"{n_pairs} shapes mu(a,c), a + c <= {N_DECOMP}: hooks(mu) = hooks(delta_a) + hooks(delta_c) "
          f"+ 2*hooks(a x (c+1) rect) as exact multisets, violations {v_dec}; membership predicate and "
          f"the three per-region hook formulas, violations {v_reg}.")

    # L2 — staircase series
    v_st = 0
    for m in range(0, N_DECOMP + 1):
        direct = mp.fsum(cnt * eps(h) for h, cnt in stair_hooks(m).items())
        if (abs(direct - S_delta_closed(m)) > tol or R_tail(m) < 0
                or abs(R_tail(m) - R_tail_direct(m)) > tol):
            v_st += 1
    check("L2_staircase_series",
          v_st == 0,
          f"S_delta(m) = A m - B + R(m), R(m) >= 0, m = 0..{N_DECOMP}: violations {v_st} "
          f"(R(0) = B = {mp.nstr(R_tail(0), 12)}).")

    # L3 + L5 — brute force
    v_H = v_size = v_chain = 0
    rows = []
    min_e_gap = None
    for n in range(1, N_SCAN + 1):
        k, r = k_r_of(n)
        shapes = list(partitions(n))
        Hs = {lam: sum(hooks(lam)) for lam in shapes}
        Hmin = min(Hs.values())
        Fn = F(n)
        Mn, argM = None, None
        for lam in shapes:
            psi = mp.fsum(EPS[h] for h in hooks(lam)) - Fn - LNQ * (Hs[lam] - Hmin)
            if Mn is None or psi > Mn:
                Mn, argM = psi, lam
        mu = mu_shape(r, k - r)
        if sum(mu) != n:
            v_size += 1
        if Hs[mu] != Hmin:
            v_H += 1
        psi_mu_direct = mp.fsum(EPS[h] for h in hooks(mu)) - Fn - LNQ * (Hs[mu] - Hmin)
        psi_mu_closed = psi_family_closed(k, r)
        lowA = A_CONST * k - 2 * B_CONST - C_CONST
        lowS = A_CONST * mp.sqrt(2 * n) - K3
        ok = (abs(psi_mu_direct - psi_mu_closed) < tol and Mn + tol >= psi_mu_direct
              and psi_mu_closed + tol >= lowA and lowA > lowS)
        if not ok:
            v_chain += 1
        e_n = Mn - A_CONST * mp.sqrt(2 * n)
        fam_def = psi_mu_direct - A_CONST * mp.sqrt(2 * n)
        min_e_gap = e_n + K3 if min_e_gap is None else min(min_e_gap, e_n + K3)
        rows.append({"n": n, "k": k, "r": r, "M_n": mp.nstr(Mn, 20), "argmax": list(argM),
                     "mu_shape": list(mu), "mu_is_argmax": mu == argM,
                     "Psi_mu": mp.nstr(psi_mu_direct, 20), "M_minus_Psi_mu": mp.nstr(Mn - psi_mu_direct, 12),
                     "e_n": mp.nstr(e_n, 15), "family_e": mp.nstr(fam_def, 15),
                     "lower_bound_A_sqrt2n_minus_K3": mp.nstr(lowS, 15)})
        print(f"  n={n:3d} k={k} r={r} M_n={mp.nstr(Mn, 10)} Psi_mu={mp.nstr(psi_mu_direct, 10)} "
              f"e_n={mp.nstr(e_n, 8)} fam_e={mp.nstr(fam_def, 8)} argmax={argM}  [{time.time() - t0:.1f}s]",
              flush=True)
    check("L3_zero_energy_and_size",
          v_H == 0 and v_size == 0,
          f"n = 1..{N_SCAN}: |mu(r,k-r)| = n violations {v_size}; H(mu) = brute-force H_min(n) "
          f"violations {v_H}.")

    v_root = sum(1 for n in range(1, N_ROOT + 1)
                 if not (4 * 2 * n < (2 * k_r_of(n)[0] + 3) ** 2)) if N_ROOT <= 200000 else -1
    # exact: 2n = k^2+k+2r <= k^2+3k < (k+3/2)^2 ; checked as 8n < (2k+3)^2 in integers
    check("L4_root_bound",
          v_root == 0,
          f"8n < (2k+3)^2 (i.e. sqrt(2n) < k + 3/2) for n = 1..{N_ROOT}: violations {v_root}; "
          f"algebraically 2n <= k^2 + 3k = (k+3/2)^2 - 9/4.")
    n_argmax = sum(1 for rw in rows if rw["mu_is_argmax"])
    worst_gap = max(rows, key=lambda rw: mp.mpf(rw["M_minus_Psi_mu"]))
    check("L5_per_n_chain_vs_brute_force",
          v_chain == 0,
          f"n = 1..{N_SCAN}: M_n >= Psi(mu) = (L1)+(L2) closed form >= A k - 2B - C > A sqrt(2n) - K3, "
          f"violations {v_chain}.  mu is the exact maximiser at {n_argmax}/{N_SCAN} n; largest "
          f"M_n - Psi(mu) = {worst_gap['M_minus_Psi_mu']} at n = {worst_gap['n']}; min(e_n + K3) = "
          f"{mp.nstr(min_e_gap, 10)} > 0.")

    # L6 / L7 — closed-form scan (no enumeration)
    scan = []
    min_fam = None
    v_low = v_gain = 0
    min_gain = None
    ks = list(range(1, K_SCAN + 1)) + [k for k in (200, 300, 500, 800, 1200, K_FAR) if k > K_SCAN]
    for k in ks:
        rs = range(0, k + 1) if k <= K_SCAN else sorted(set([0, 1, 2, k // 4, k // 3, k // 2, (2 * k) // 3,
                                                           (3 * k) // 4, k - 2, k - 1, k]))
        base_stair = S_delta_closed(k)
        kmin = None
        for r in rs:
            n = tri(k) + r
            val = psi_family_closed(k, r)
            fam = val - A_CONST * mp.sqrt(2 * n)
            if fam + K3 < 0:
                v_low += 1
            gain = S_delta_closed(r) + S_delta_closed(k - r) + G_val(r, k - r) - base_stair
            if gain < -tol:
                v_gain += 1
            if r >= 1:
                min_gain = gain if min_gain is None else min(min_gain, gain)
            kmin = fam if kmin is None else min(kmin, fam)
            min_fam = fam if min_fam is None else min(min_fam, fam)
        scan.append({"k": k, "min_r_family_e": mp.nstr(kmin, 15)})
        if k % 20 == 0 or k > K_SCAN:
            print(f"  scan k={k}: min_r [Psi(mu) - A sqrt(2n)] = {mp.nstr(kmin, 10)}  [{time.time() - t0:.1f}s]",
                  flush=True)
    check("L6_closed_form_scan_large_n",
          v_low == 0,
          f"k = 1..{K_SCAN} (all r) and sampled k up to {K_FAR}: Psi(mu) >= A sqrt(2n) - K3 violations "
          f"{v_low}; measured min of Psi(mu) - A sqrt(2n) = {mp.nstr(min_fam, 12)} vs proved -K3 = "
          f"{mp.nstr(-K3, 12)}; at k = {K_FAR}: {scan[-1]['min_r_family_e'][:12]}.")
    check("L7_measured_gain_nonnegative",
          v_gain == 0,
          f"MEASURED, not proved: S(mu(r,k-r)) - S(delta_k) >= 0 on the scan, violations {v_gain}, "
          f"min gain over r >= 1: {mp.nstr(min_gain, 10)} (r = 0 is delta_k, gain 0).")

    n_ok = sum(1 for x in results if x["pass"])
    print("\n" + "=" * 78)
    print(f"{n_ok}/{len(results)} checks passed   [{time.time() - t0:.1f}s]")
    print(f"VERDICT: M_n >= A sqrt(2n) - K3, K3 = {mp.nstr(K3, 12)}, for every n >= 1; with the upper "
          f"bound, -K3 <= e_n <= K2.  NOT convergence of e_n, NOT kappa.")
    print("=" * 78)

    payload = {
        "probe": "rev_lower_bound_probe",
        "bean": ["qou-fxym", "qou-3e6w", "qou-hok7"],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton",
        "dps": mp.dps,
        "constants": {
            "A": mp.nstr(A_CONST, 40), "B": mp.nstr(B_CONST, 40), "C": mp.nstr(C_CONST, 40),
            "ln_q0": mp.nstr(LNQ, 40), "K3": mp.nstr(K3, 40),
        },
        "family": "mu(r, k-r): delta_k plus its r TOP outer corners; rows k+1, k, ..., k+2-r, k-r, ..., 1",
        "statements": {
            "(L1)": "hooks(mu(a,c)) = hooks(delta_a) + hooks(delta_c) + 2*hooks(a x (c+1) rectangle) "
                    "(Lean cornerBlock_hookSum)",
            "(L2)": "S_delta(m) = A m - B + R(m), R(m) >= 0",
            "(L3)": "H(mu(r,k-r)) = H_min(T_k + r)",
            "(L4)": "sqrt(2n) < k + 3/2 for n = T_k + r, r <= k",
            "main": "M_n >= A sqrt(2n) - K3, K3 = 3A/2 + 2B + C, for every n >= 1",
            "not_established": "convergence of e_n; the value kappa; sharp constant; L7 (gain >= 0) is measured only",
        },
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "n_scan": N_SCAN,
        "n_decomp": N_DECOMP,
        "k_scan": K_SCAN,
        "k_far": K_FAR,
        "table": rows,
        "closed_form_scan": scan,
    }
    out = os.path.join(_COMPUTATIONS, "rev-lower-bound.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
