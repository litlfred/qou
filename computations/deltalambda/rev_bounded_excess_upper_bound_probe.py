#!/usr/bin/env python3
r"""
rev_bounded_excess_upper_bound_probe.py — e_n := M_n - A sqrt(2n) <= K2 for EVERY n >= 1:
the bounded-excess upper bound (qou-fxym, arc qou-3e6w / qou-hok7)

## What was open

`rev_sharp_coefficient_upper_bound_probe.py` (#7715) proved `M_n <= A sqrt(2n) + (A+c)(2n)^{1/4} + K0`.
The `n^{1/4}` had TWO sources, both slack in the argument, not in M_n:

  (i)  integrality: the continuous water-fill p is off the half-integer grid; rounding costs an
       energy defect l/4, and a pair-term loss LINEAR in |t - p| exploits it for free
       (T1(l) ~ (c/2) sqrt(l));
  (ii) row count: #7185's 2(H_l^min - H_min) >= (l-k)^2 - r lets l exceed k by sqrt(r) <= sqrt(k)
       rows at zero cost, i.e. A sqrt(k) ~ n^{1/4}.

## The argument (each step a stated inequality; checks below verify each)

Notation as in #7715: L = ln q0, eps(x) = -log(1 - q0^{-2x}), |eps'(x)| = 2L/(q0^{2x} - 1),
A = sum eps(odd), S_2 = sum_k k eps(2k), t_i = lambda_i + i - 1/2 (1-indexed), wall w_i = i + 1/2,
2H = sum t^2 - sum m^2, n = T_k + r (0 <= r <= k), Delta_k(v) = sum_{i<=l-k}(v_i - v_{i+k}).

  (A) H IS LINEAR IN CELLS.  H(lambda) = sum of hook lengths = n(lambda) + n(lambda') + n
      = sum_{(i,j) in lambda} (i + j - 1).  So with a_d := #cells on anti-diagonal d (a_d <= d),
      H = sum_d d a_d, and the greedy fill o (diagonals 1..k full, r cells on k+1) attains
      H_min(n) = P_k + r(k+1), P_k = sum_{d<=k} d^2 (any r of the k+1 outer corners of the
      staircase delta_k can be added).
  (B) DIAGONAL EXCHANGE (Lean `diagonal_exchange`).  sum (a_d - o_d) d = sum (a_d - o_d)(d - k - 1)
      >= sum_{d >= k+2} a_d (d - k - 1), termwise.  An l-row shape has its first-column cell on every
      diagonal d <= l, so  H(lambda) - H_min(n) >= T_{l-k-1} = (l-k)(l-k-1)/2  for l >= k+1.
      (No `- r`: this is the fix for (ii).)
  (C) ROUNDED WATER-FILL.  Let q be the water-fill rounded to the grid with the extra units on the
      LAST flat rows (#7715's `rounded_feasible`): q = max(w, c), c sorted in {a, a+1}.  Then q is
      nondecreasing with steps <= 1, i.e. an l-row PARTITION, and every l-row t with the same sum
      has t_i < q_i only where q_i = c_i <= a + 1 (because t_i >= w_i), while a <= q everywhere.
      Lean `rounded_pythagoras`:
          sum t^2 >= sum q^2 + sum d_i^2 - sum |d_i|,   d := t - q  (INTEGER vector).
      In particular q attains H_l^min, and  2(H - H(q)) >= sum (d_i^2 - |d_i|)  (fix for (i)).
  (D) LOSS IS SEPARABLE.  q nondecreasing => Delta_k(q) <= 0, and Delta_k(d) = sum over the first
      m_k minus the last m_k coordinates (middle cancels), m_k = min(k, l-k), so
          sum_k |eps'(2k)| Delta_k(t) <= sum_i omega_i |d_i|,
          omega_i := sum_{k<l, i in first m_k or last m_k} |eps'(2k)|,
      sum_i omega_i <= c1 := 2 sum_k k |eps'(2k)|,  omega_i <= c0 := sum_k |eps'(2k)|.
  (E) PER-COORDINATE TRADE-OFF (Lean `int_tradeoff`): for x in N,
          omega x - (L/2)(x^2 - x) <= omega + omega^2/(2L);   summed: <= K1 := c1 + c0 c1/(2L).
  (F) EXTRA ROWS (Lean `extra_rows_tradeoff`): j A - (L/2) j(j-1) <= J := (A + L/2)^2/(2L).

  Assembled, with #7715's tangent step  sum_c eps(h) <= l A + S_2 + sum_k |eps'(2k)| Delta_k(t)
  and L(H - H_min) = (L/2)(sum t^2 - sum q^2) + L(H(q) - H_min):
      Psi(lambda) <= l A + S_2 - F(n) + sum_i [omega_i |d_i| - (L/2)(d_i^2 - |d_i|)] - L T_{l-k-1}
                  <= A k + S_2 - F(n) + K1 + J,
  and since k <= sqrt(2n + 1/4) - 1/2 < sqrt(2n) and F(n) >= eps(1):

      e_n = M_n - A sqrt(2n)  <=  K2 := S_2 + K1 + J - eps(1)        for every n >= 1.

So the excess is BOUNDED ABOVE.  K2 = 85.37 is far above what is measured: e_n = -12.48 at n = 40,
and the conjecture of #7294 is M_n = A sqrt(2n + 1/4) + kappa + o(1), kappa = -10.72317, under
which e_n -> kappa.  (Do not compare K2 with qou-as81's `e_inf = 2.4393`: that is the constant of
a different normalisation, not M_n - A sqrt(2n).)  This proves an upper bound only: NOT the value
kappa, NOT convergence, NOT a lower bound on e_n.

## Checks

  B1  constants c0, c1, K1, J, K2 (convergent sums; tail terms reported).
  B2  (A): H = sum (i+j-1) = hook sum, and H_min(n) = P_k + r(k+1), all shapes n <= N_EXACT.
  B3  (B): H - H_min >= T_{l-k-1} on every shape; its hypotheses a_d <= d, a_d >= 1 (d <= l).
  B4  (C): q is an l-row partition with the sum; a <= q; t_i < q_i => q_i <= a+1; the discrete
      Pythagoras exactly; q attains brute-force H_l^min.
  B5  (D): Delta_k(q) <= 0 and Delta_k(d) <= sum over I_k of |d_i|, exact.
  B6  per-shape chain (first line of the assembly) on all shapes n <= N_EXACT, 60 dps.
  B7  M_n <= U2(n) <= A k + S_2 - F(n) + K1 + J and e_n <= K2, exact M_n for n <= N_SCAN.

Arithmetic: mpmath 60 dps for eps-valued quantities; partition data, (A)-(D) exact (ints/Fractions).
No float64.  Witness: computations/rev-bounded-excess-upper-bound.witness.json.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction

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
EPS, F, DEPS2, KMAX = base.EPS, base.F, base.DEPS2, base.KMAX
A_CONST, S2_CONST = base.A_CONST, base.S2_CONST
t_vec, m_sq_sum, waterfill = base.t_vec, base.m_sq_sum, base.waterfill
rounded_feasible, is_partition_t, delta_k = base.rounded_feasible, base.is_partition_t, base.delta_k
tri, k_r_of = base.tri, base.k_r_of

N_EXACT = int(os.environ.get("REV_BOUNDED_N_EXACT", "30"))
N_SCAN = int(os.environ.get("REV_BOUNDED_N_SCAN", "40"))

C0 = mp.fsum(DEPS2[k] for k in range(1, KMAX + 1))
C1 = 2 * mp.fsum(k * DEPS2[k] for k in range(1, KMAX + 1))
K1 = C1 + C0 * C1 / (2 * LNQ)
JCAP = (A_CONST + LNQ / 2) ** 2 / (2 * LNQ)
K2 = S2_CONST + K1 + JCAP - EPS[1]


def frac_mp(x: Fraction):
    return mp.mpf(x.numerator) / x.denominator


def omegas(ell):
    """omega_i (0-indexed i) = sum_{k<l, i in first m_k or last m_k} |eps'(2k)|."""
    om = [mp.mpf(0)] * ell
    for k in range(1, ell):
        m = min(k, ell - k)
        idx = set(range(m)) | set(range(ell - m, ell))
        for i in idx:
            om[i] += DEPS2[k]
    return om


def phi_int(om):
    """max_{x in N} [om x - (L/2)(x^2 - x)] (exact integer maximisation)."""
    best, x = mp.mpf(0), 0
    while True:
        x += 1
        v = om * x - LNQ / 2 * (x * x - x)
        if v < best:
            return best
        best = v


def cell_H(lam):
    return sum(i + j - 1 for i in range(1, len(lam) + 1) for j in range(1, lam[i - 1] + 1))


def diag_counts(lam):
    a = {}
    for i in range(1, len(lam) + 1):
        for j in range(1, lam[i - 1] + 1):
            a[i + j - 1] = a.get(i + j - 1, 0) + 1
    return a


def main() -> int:
    t0 = time.time()
    results = []

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}", flush=True)

    print("=" * 78)
    print("rev_bounded_excess_upper_bound_probe -- e_n = M_n - A sqrt(2n) <= K2")
    print("=" * 78)
    print(f"  q0 = {mp.nstr(Q0, 25)} (proton)  L = {mp.nstr(LNQ, 15)}  A = {mp.nstr(A_CONST, 15)}")
    print(f"  c0 = {mp.nstr(C0, 15)}  c1 = {mp.nstr(C1, 15)}  K1 = {mp.nstr(K1, 15)}  J = {mp.nstr(JCAP, 15)}"
          f"  K2 = {mp.nstr(K2, 15)}", flush=True)
    tol = mp.mpf(10) ** (-(mp.dps - 15))

    check("B1_constants_finite",
          C0 > 0 and C1 > 0 and DEPS2[KMAX] * KMAX < tol,
          f"c0 = sum|eps'(2k)| = {mp.nstr(C0, 15)}; c1 = 2 sum k|eps'(2k)| = {mp.nstr(C1, 15)}; "
          f"K1 = c1 + c0 c1/(2L) = {mp.nstr(K1, 15)}; J = (A+L/2)^2/(2L) = {mp.nstr(JCAP, 15)}; "
          f"S2 = {mp.nstr(S2_CONST, 15)}; K2 = S2 + K1 + J - eps(1) = {mp.nstr(K2, 20)}; tail term "
          f"k={KMAX}: {mp.nstr(DEPS2[KMAX] * KMAX, 3)}.")

    v_cell = v_hmin = v_diag = v_dhyp = v_q = v_pyth = v_qmin = v_mono = v_sep = v_chain = 0
    n_shapes = 0
    min_chain_slack = None
    rows = []
    for n in range(1, N_SCAN + 1):
        k, r = k_r_of(n)
        shapes = list(partitions(n))
        Hs = {lam: sum(hooks(lam)) for lam in shapes}
        Hmin = min(Hs.values())
        Hmin_l = {}
        for lam in shapes:
            Hmin_l[len(lam)] = min(Hmin_l.get(len(lam), Hs[lam]), Hs[lam])
        Fn = F(n)
        Mn, argM = None, None
        omcache = {}
        for lam in shapes:
            ell = len(lam)
            H = Hs[lam]
            heps = mp.fsum(EPS[h] for h in hooks(lam))
            psi = heps - Fn - LNQ * (H - Hmin)
            if Mn is None or psi > Mn:
                Mn, argM = psi, lam
            if n > N_EXACT:
                continue
            n_shapes += 1
            # (A)
            if cell_H(lam) != H:
                v_cell += 1
            # (B)
            a = diag_counts(lam)
            if any(a[d] > d for d in a) or any(a.get(d, 0) < 1 for d in range(1, ell + 1)):
                v_dhyp += 1
            jj = ell - k
            if jj >= 1 and 2 * (H - Hmin) < jj * (jj - 1):
                v_diag += 1
            # (C)
            tv = t_vec(lam)
            Tsum = Fraction(2 * n + ell * ell, 2)
            p, tau, mf = waterfill(ell, Tsum)
            qv = rounded_feasible(ell, p, tau, mf)
            amin = min(qv[:mf])
            w = [Fraction(2 * i + 1, 2) for i in range(1, ell + 1)]
            if (not is_partition_t(ell, qv) or sum(qv) != Tsum
                    or any(qv[i] != w[i] and not (amin <= qv[i] <= amin + 1) for i in range(ell))
                    or any(x < amin for x in qv)
                    or any(tv[i] < qv[i] and qv[i] > amin + 1 for i in range(ell))):
                v_q += 1
            d = [x - y for x, y in zip(tv, qv)]
            if any(x.denominator != 1 for x in d):
                v_q += 1
            sq_t = sum(x * x for x in tv)
            sq_q = sum(x * x for x in qv)
            dd = sum(x * x for x in d)
            d1 = sum(abs(x) for x in d)
            if sq_t < sq_q + dd - d1:
                v_pyth += 1
            if 2 * Hmin_l[ell] != sq_q - m_sq_sum(ell):
                v_qmin += 1
            # (D)
            for kk in range(1, ell):
                if delta_k(qv, kk) > 0:
                    v_mono += 1
                m = min(kk, ell - kk)
                idx = set(range(m)) | set(range(ell - m, ell))
                if delta_k(d, kk) > sum(abs(d[i]) for i in idx):
                    v_sep += 1
            # chain (first line of the assembly), with the proved row-count energy
            if ell not in omcache:
                omcache[ell] = omegas(ell)
            om = omcache[ell]
            gain = mp.fsum(om[i] * int(abs(d[i])) - LNQ / 2 * (int(d[i]) ** 2 - int(abs(d[i])))
                           for i in range(ell))
            rowpen = LNQ * tri(jj - 1) if jj >= 1 else mp.mpf(0)
            rhs = ell * A_CONST + S2_CONST - Fn + gain - rowpen
            sl = rhs - psi
            min_chain_slack = sl if min_chain_slack is None else min(min_chain_slack, sl)
            if sl < -tol:
                v_chain += 1
        if Hmin != sum(dd * dd for dd in range(1, k + 1)) + r * (k + 1):
            v_hmin += 1
        # U2(n): max over l of the first assembly line's upper bound (per-coordinate phi)
        best = None
        for ell in range(1, k + int(2 * (A_CONST + LNQ) / LNQ) + 4):
            om = omegas(ell)
            jj = ell - k
            val = ell * A_CONST + mp.fsum(phi_int(o) for o in om) - (LNQ * tri(jj - 1) if jj >= 1 else 0)
            best = val if best is None or val > best else best
        U2 = S2_CONST - Fn + best
        cap = A_CONST * k + S2_CONST - Fn + K1 + JCAP
        e_n = Mn - A_CONST * mp.sqrt(2 * n)
        rows.append({"n": n, "k": k, "r": r, "M_n": mp.nstr(Mn, 20), "argmax": list(argM),
                     "e_n": mp.nstr(e_n, 15), "U2_n": mp.nstr(U2, 15), "cap_Ak_plus_const": mp.nstr(cap, 15),
                     "e_n_bound_K2": mp.nstr(K2, 15),
                     "U_7715": mp.nstr(base.U_of(n)[0], 15)})
        print(f"  n={n:3d} M_n={mp.nstr(Mn, 10)} e_n={mp.nstr(e_n, 8)} U2={mp.nstr(U2, 10)} "
              f"cap={mp.nstr(cap, 10)}  [{time.time() - t0:.1f}s]", flush=True)

    check("B2_H_is_linear_in_cells_and_Hmin_closed_form",
          v_cell == 0 and v_hmin == 0,
          f"{n_shapes} shapes n <= {N_EXACT}: hook sum = sum (i+j-1) violations {v_cell}; "
          f"H_min(n) = P_k + r(k+1) violations {v_hmin} (n <= {N_SCAN}).")
    check("B3_diagonal_exchange_row_count_energy",
          v_diag == 0 and v_dhyp == 0,
          f"2(H - H_min) >= (l-k)(l-k-1) for l > k on every shape: violations {v_diag}; hypotheses "
          f"a_d <= d and a_d >= 1 for d <= l: violations {v_dhyp}.")
    check("B4_rounded_waterfill_discrete_pythagoras",
          v_q == 0 and v_pyth == 0 and v_qmin == 0,
          f"q an l-row partition with the sum, a <= q, (t_i < q_i => q_i <= a+1), d integer: viol {v_q}; "
          f"sum t^2 >= sum q^2 + sum d^2 - sum|d| exact: viol {v_pyth}; q attains brute-force "
          f"H_l^min: viol {v_qmin}.")
    check("B5_separable_loss",
          v_mono == 0 and v_sep == 0,
          f"Delta_k(q) > 0: {v_mono}; Delta_k(d) > sum_(first m_k, last m_k) |d_i|: {v_sep}.")
    check("B6_per_shape_chain",
          v_chain == 0,
          f"Psi <= l A + S2 - F(n) + sum_i[omega_i|d_i| - (L/2)(d_i^2-|d_i|)] - L T_(l-k-1) on {n_shapes} "
          f"shapes: violations {v_chain}, min slack {mp.nstr(min_chain_slack, 8)}.")
    ok7 = all(mp.mpf(rw["M_n"]) <= mp.mpf(rw["U2_n"]) + tol <= mp.mpf(rw["cap_Ak_plus_const"]) + 2 * tol
              and mp.mpf(rw["e_n"]) <= K2 for rw in rows)
    maxe = max(rows, key=lambda rw: mp.mpf(rw["e_n"]))
    check("B7_M_n_le_U2_le_cap_and_e_n_le_K2",
          ok7,
          f"n = 1..{N_SCAN}: M_n <= U2(n) <= A k + S2 - F(n) + K1 + J, and e_n <= K2 = {mp.nstr(K2, 10)}. "
          f"Largest measured e_n = {maxe['e_n']} at n = {maxe['n']}; at n = {N_SCAN}: e_n = "
          f"{rows[-1]['e_n'][:10]}, U2 - A sqrt(2n) = "
          f"{mp.nstr(mp.mpf(rows[-1]['U2_n']) - A_CONST * mp.sqrt(2 * N_SCAN), 8)}, #7715 U = "
          f"{rows[-1]['U_7715'][:10]}.")

    n_ok = sum(1 for x in results if x["pass"])
    print("\n" + "=" * 78)
    print(f"{n_ok}/{len(results)} checks passed   [{time.time() - t0:.1f}s]")
    print(f"VERDICT: e_n = M_n - A sqrt(2n) <= K2 = {mp.nstr(K2, 12)} for every n >= 1 (bounded excess). "
          f"NOT the conjectured limit kappa = -10.72317, NOT convergence, NOT a lower bound.")
    print("=" * 78)

    payload = {
        "probe": "rev_bounded_excess_upper_bound_probe",
        "bean": ["qou-fxym", "qou-3e6w", "qou-hok7"],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton",
        "dps": mp.dps,
        "constants": {
            "A": mp.nstr(A_CONST, 40), "ln_q0": mp.nstr(LNQ, 40), "S2": mp.nstr(S2_CONST, 40),
            "c0": mp.nstr(C0, 40), "c1": mp.nstr(C1, 40), "K1": mp.nstr(K1, 40),
            "J": mp.nstr(JCAP, 40), "eps1": mp.nstr(EPS[1], 40), "K2": mp.nstr(K2, 40),
        },
        "statements": {
            "(A)": "H(lambda) = sum_{(i,j) in lambda} (i+j-1); H_min(n) = P_k + r(k+1)",
            "(B)": "H(lambda) - H_min(n) >= T_{l-k-1} for an l-row shape (Lean diagonal_exchange)",
            "(C)": "sum t^2 >= sum q^2 + sum (t-q)^2 - sum |t-q| at the rounded water-fill q "
                   "(Lean rounded_pythagoras); q attains H_l^min",
            "(D)": "sum_k |eps'(2k)| Delta_k(t) <= sum_i omega_i |d_i|, sum omega <= c1, omega <= c0",
            "(E)": "omega x - (L/2)(x^2-x) <= omega + omega^2/(2L), x in N (Lean int_tradeoff)",
            "(F)": "j A - (L/2) j (j-1) <= (A + L/2)^2/(2L) (Lean extra_rows_tradeoff)",
            "main": "M_n <= A k_n + S2 - F(n) + K1 + J  =>  e_n = M_n - A sqrt(2n) <= K2 for all n >= 1",
            "not_established": "e_n -> e_inf; the value of limsup e_n; any lower bound on e_n for general n",
        },
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "n_exact": N_EXACT,
        "n_scan": N_SCAN,
        "table": rows,
    }
    out = os.path.join(_COMPUTATIONS, "rev-bounded-excess-upper-bound.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
