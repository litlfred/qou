#!/usr/bin/env python3
r"""
rev_sharp_coefficient_upper_bound_probe.py — M_n <= A sqrt(2n) + O(n^{1/4}): the SHARP
coefficient of the upper bound (qou-fxym, arc qou-3e6w / qou-hok7)

## What was open

#7185 proved `M_n <= (C + L/2) sqrt(2n) + O(1)` (so REV_n = Theta(sqrt n)), by bounding the
one-body term `sum_i F(beta_i) <= l C` and DISCARDING the pair term.  #7286 showed the gap between
that coefficient `C sqrt2 = 8.728` and the staircase rate `A sqrt2 = 5.096` is exactly one term,
`C - A = E_2 = sum_d eps(2d)`, the staircase's pair term per row.  #7294 then MEASURED (excess
bounded to n = 3916) that the true coefficient is `A sqrt2`.  The upper bound with that coefficient
was not proved: the "pair-term lower bound that survives the energy trade-off" (hok7 2026-09-13).

## The argument (every step is a stated inequality; checks below verify each one)

Notation (proton pin, `L = ln q0`, `t = q0^2`): `eps(x) = -log(1 - t^{-x})` — convex, decreasing on
x > 0; `|eps'(x)| = 2L/(t^x - 1)`.  `C = sum_{m>=1} eps(m)`, `A = sum_{j>=1} eps(2j-1)`,
`E_2 = sum_{d>=1} eps(2d) = C - A`.  For lambda |- n with l rows, 1-indexed
`beta_i = lambda_i + l - i`, `m_i = l + 1/2 - 2i`, `t_i = beta_i - m_i` (half-integers).

  (a) (I') of #7282:  sum_c eps(h(c)) = sum_i F(beta_i) - P,   P = sum_{i<j} eps(beta_i - beta_j).
  (b) completed square (#7294, HookSumCompletedSquare.lean):  2H = sum_i t_i^2 - sum_i m_i^2.
  (c) TANGENT LINES, organised by neighbour order k (no Jensen, no (l,W) summary).  Since
      `beta_i - beta_{i+k} - 2k = t_i - t_{i+k}` and eps is convex,
          P  >=  sum_{k<l} (l-k) eps(2k)  -  sum_{k<l} |eps'(2k)| Delta_k(t),
          Delta_k(v) := sum_{i=1}^{l-k} (v_i - v_{i+k}).
      With F(beta_i) <= C:   sum_c eps(h) <= l A + S_2 + sum_k |eps'(2k)| Delta_k(t),
      S_2 := sum_{k>=1} k eps(2k)   (uses l C - sum_{k<l}(l-k) eps(2k) = l(C-E_2) + sum_{k<l} k eps(2k)
      + l sum_{k>=l} eps(2k) <= l A + S_2).
  (d) THE HARD-WALL REFERENCE.  An l-row partition has `beta_i >= l - i + 1`, i.e. `t_i >= w_i :=
      i + 1/2`, and `sum t_i = n + l^2/2 =: T`.  Let p be the Euclidean projection of 0 onto the convex
      set K = {sum t = T, t >= w}: `p_i = max(tau, w_i)` (water-filling).  Then
        (d1) Pythagoras:  sum t^2 >= sum p^2 + |t - p|^2  for every t in K;
        (d2) p is NONDECREASING, so Delta_k(p) <= 0 for every k;
        (d3) Delta_k(t - p) <= sqrt(2 min(k, l-k)) |t - p|   (Cauchy-Schwarz on 2min(k,l-k) coords);
        (d4) rounding p's flat part to the half-integer grid is a FEASIBLE l-row partition, so
             2 H_l^min + sum m^2 <= sum p^2 + l/4,  hence  2(H - H_l^min) >= max(0, y^2 - l/4),  y := |t-p|.
      So the pair-term loss is at most  c y,  c := sum_{k>=1} |eps'(2k)| sqrt(2k)  (finite),
      and it is PAID by the within-row-count energy:
          T1(l) := sup_{y>=0} [ c y - (L/2) max(0, y^2 - l/4) ]  <=  (c/2) sqrt(l) + c^2/(2L).
  (e) THE ROW-COUNT ENERGY, unchanged from #7185 (HookSumRowTangentBound.lean):
          2(H_l^min - H_min(n)) >= (l - k)^2 - r,   n = T_k + r, 0 <= r <= k,
      and trivially >= 0.  For l <= sqrt(2n), l A <= A sqrt(2n) with no energy at all.

  Assembled:  M_n = max_lambda [ sum_c eps(h) - F(n) - L(H - H_min(n)) ]
                 <= S_2 - F(n) + max_l [ l A - L D(l) + T1(l) ] =: U(n),
              D(l) := max(0, ((l-k)^2 - r)/2) for l > k, 0 otherwise.
  Closed form:   U(n) <= A sqrt(2n) + (A + c) (2n)^{1/4} + K_0,
                 K_0 := S_2 + c^2/(2L) + c/2 + (A + c/2)^2/L.

Consequence: limsup M_n / sqrt(2n) <= A.  With the staircase (V(delta_k) = A k - B - F(n) + rem_k,
proved closed form, StaircaseHookMultiset.lean) this gives lim M_n/sqrt(2n) = A along triangular n
— the coefficient #7294 MEASURED is now PROVED (modulo the step-(e) caveat below).  The ERROR term
is O(n^{1/4}), NOT O(1): the constant `e_inf` / kappa of the M_n = A sqrt(2n+1/4) + kappa + o(1)
conjecture is NOT reached by this argument.

Caveat carried from #7185: (e) uses H(lambda^+) = P_k + r(k+1) (attainment of the closed form by
lambda^+), verified exactly here and in #7185 but not in Lean; only H_min(n) <= H(lambda^+) is
needed, which IS attainment.

## Checks

  S1  constants: c, S_2, A + E_2 = C.
  S2  (a),(b) exact on all shapes n <= N_EXACT.
  S3  (c) tangent pair bound on all shapes n <= N_EXACT (60 dps, signed slack reported).
  S4  (d1)-(d4) in exact rationals on all shapes n <= N_EXACT; H_l^min by brute force.
  S5  (e) exact integers, all (n, l), n <= N_EXACT.
  S6  per-shape chain: Psi(lambda) <= l A + S_2 - F(n) + c y - (L/2)max(0, y^2 - l/4) - L Delta_l.
  S7  M_n <= U(n) <= closed form, exact M_n by full scan n <= N_SCAN.
  S8  rate scan of U(n) to n = 1e10 (closed form, no enumeration): U/sqrt(2n) -> A,
      (U - A sqrt(2n)) / (2n)^{1/4} bounded.

Arithmetic: mpmath 60 dps; all partition data, (b), (d1)-(d4), (e) in exact integers/Fractions.
No float64.  Witness: computations/rev-sharp-coefficient-upper-bound.witness.json.
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

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60
Q0 = Q_MP
LNQ = mp.log(Q0)
TT = Q0 ** 2

from zn_hook_length_closed_form_probe import hooks, partitions  # noqa: E402

N_EXACT = int(os.environ.get("REV_SHARP_N_EXACT", "30"))
N_SCAN = int(os.environ.get("REV_SHARP_N_SCAN", "40"))

_NEPS = 2200
EPS = [mp.mpf(0)] + [-mp.log(1 - TT ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]
C_CONST = _F[_NEPS - 1]
A_CONST = mp.fsum(EPS[m] for m in range(1, _NEPS, 2))
E2_CONST = mp.fsum(EPS[m] for m in range(2, _NEPS, 2))
KMAX = _NEPS // 2 - 1


def F(k: int):
    return _F[min(k, _NEPS - 1)]


def deps_abs(x: int):
    """|eps'(x)| = 2L/(t^x - 1)."""
    return 2 * LNQ / (TT ** x - 1)


DEPS2 = [mp.mpf(0)] + [deps_abs(2 * k) for k in range(1, KMAX + 1)]
S2_CONST = mp.fsum(k * EPS[2 * k] for k in range(1, KMAX + 1))
C_PAIR = mp.fsum(DEPS2[k] * mp.sqrt(2 * k) for k in range(1, KMAX + 1))
K0_CONST = S2_CONST + C_PAIR ** 2 / (2 * LNQ) + C_PAIR / 2 + (A_CONST + C_PAIR / 2) ** 2 / LNQ


def tri(k):
    return k * (k + 1) // 2


def k_r_of(n):
    k = 0
    while tri(k + 1) <= n:
        k += 1
    return k, n - tri(k)


# ------------------------------------------------------------------ beta / t coordinates (exact)
def t_vec(lam):
    """t_i = beta_i - m_i, as Fractions (half-integers), i = 1..l."""
    ell = len(lam)
    out = []
    for i in range(1, ell + 1):
        beta = lam[i - 1] + ell - i
        m = Fraction(2 * ell + 1 - 4 * i, 2)
        out.append(beta - m)
    return out


def m_sq_sum(ell):
    return sum(Fraction(2 * ell + 1 - 4 * i, 2) ** 2 for i in range(1, ell + 1))


def waterfill(ell, Tsum):
    """Projection of 0 onto {sum t = Tsum, t_i >= i + 1/2}: p_i = max(tau, w_i). Returns (p, tau, mflat)."""
    w = [Fraction(2 * i + 1, 2) for i in range(1, ell + 1)]
    for mf in range(1, ell + 1):
        tau = (Tsum - sum(w[mf:])) / mf
        lo = w[mf - 1]
        hi = w[mf] if mf < ell else None
        if tau >= lo and (hi is None or tau <= hi):
            return [max(tau, wi) for wi in w], tau, mf
    raise AssertionError("waterfill: infeasible")


def rounded_feasible(ell, p, tau, mf):
    """Round the flat part to the half-integer grid, keeping the sum: a feasible l-row t-vector."""
    # tau0 = largest half-integer <= tau
    twice = 2 * tau
    fl = twice.numerator // twice.denominator  # floor(2 tau)
    if fl % 2 == 0:
        fl -= 1  # half-integers are odd/2
    tau0 = Fraction(fl, 2)
    extra = sum(p[:mf]) - mf * tau0
    assert extra.denominator == 1 and 0 <= extra <= mf, (extra, mf)
    q = [tau0] * mf
    for j in range(int(extra)):
        q[mf - 1 - j] += 1
    return q + p[mf:]


def is_partition_t(ell, tv):
    """t-vector -> partition with exactly l rows? (beta strictly decreasing integers, beta_l >= 1)."""
    betas = []
    for i in range(1, ell + 1):
        b = tv[i - 1] + Fraction(2 * ell + 1 - 4 * i, 2)
        if b.denominator != 1:
            return False
        betas.append(int(b))
    return all(betas[i] > betas[i + 1] for i in range(ell - 1)) and betas[-1] >= 1


def delta_k(v, k):
    ell = len(v)
    return sum(v[i] - v[i + k] for i in range(ell - k))


def T1(ell):
    """sup_{y>=0} [c y - (L/2) max(0, y^2 - l/4)] (closed form)."""
    y0 = mp.sqrt(ell) / 2
    if y0 >= C_PAIR / LNQ:
        return C_PAIR * y0
    return C_PAIR ** 2 / (2 * LNQ) + LNQ * y0 ** 2 / 2


def U_of(n):
    """U(n) = S_2 - F(n) + max_l [l A - L D(l) + T1(l)]  and its argmax l."""
    k, r = k_r_of(n)
    best, barg = None, None
    # l <= k: D = 0, value increasing in l -> l = k candidate; l > k scanned
    xmax = int(mp.sqrt(r)) + int(4 * (A_CONST + C_PAIR) / LNQ) + 60
    for ell in [max(k, 1)] + [k + x for x in range(1, xmax + 1)]:
        x = ell - k
        D = max(Fraction(0), Fraction(x * x - r, 2)) if x > 0 else Fraction(0)
        v = ell * A_CONST - LNQ * mp.mpf(D.numerator) / D.denominator + T1(ell)
        if best is None or v > best:
            best, barg = v, ell
    return S2_CONST - F(n) + best, barg


def closed_form(n):
    return A_CONST * mp.sqrt(2 * n) + (A_CONST + C_PAIR) * mp.mpf(2 * n) ** mp.mpf("0.25") + K0_CONST


def main() -> int:
    t0 = time.time()
    results = []

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}", flush=True)

    print("=" * 78)
    print("rev_sharp_coefficient_upper_bound_probe -- M_n <= A sqrt(2n) + O(n^{1/4})")
    print("=" * 78)
    print(f"  q0 = {mp.nstr(Q0, 25)} (proton)  L = {mp.nstr(LNQ, 15)}")
    print(f"  A = {mp.nstr(A_CONST, 20)}  E2 = {mp.nstr(E2_CONST, 20)}  C = {mp.nstr(C_CONST, 20)}")
    print(f"  c = {mp.nstr(C_PAIR, 20)}  S2 = {mp.nstr(S2_CONST, 20)}  K0 = {mp.nstr(K0_CONST, 15)}",
          flush=True)

    tol = mp.mpf(10) ** (-(mp.dps - 15))

    # ------------------------------------------------------------- S1 constants
    check("S1_constants_A_plus_E2_is_C_and_c_finite",
          abs(A_CONST + E2_CONST - C_CONST) < tol and C_PAIR > 0,
          f"A + E2 - C = {mp.nstr(A_CONST + E2_CONST - C_CONST, 3)}; c = sum_k |eps'(2k)| sqrt(2k) = "
          f"{mp.nstr(C_PAIR, 15)} (tail term k={KMAX}: {mp.nstr(DEPS2[KMAX] * mp.sqrt(2 * KMAX), 3)}); "
          f"S2 = sum k eps(2k) = {mp.nstr(S2_CONST, 15)}; coefficient A sqrt2 = "
          f"{mp.nstr(A_CONST * mp.sqrt(2), 12)} against #7185's (C + L/2) sqrt2 = "
          f"{mp.nstr((C_CONST + LNQ / 2) * mp.sqrt(2), 12)}.")

    # ------------------------------------------------------------- enumeration n <= N_SCAN
    v_ab = v_tan = v_pyth = v_mono = v_cs = v_round = v_e = v_chain = 0
    min_tan_slack = None
    worst_ab = mp.mpf(0)
    n_shapes = 0
    max_round_excess_ratio = Fraction(0)
    Mrows = []
    for n in range(1, N_SCAN + 1):
        k, r = k_r_of(n)
        shapes = list(partitions(n))
        Hs = {}
        for lam in shapes:
            Hs[lam] = sum(hooks(lam))
        Hmin = min(Hs.values())
        Hmin_l = {}
        for lam in shapes:
            ell = len(lam)
            Hmin_l[ell] = min(Hmin_l.get(ell, Hs[lam]), Hs[lam])
        Mn, argM = None, None
        Fn = F(n)
        for lam in shapes:
            ell = len(lam)
            H = Hs[lam]
            hk = hooks(lam)
            heps = mp.fsum(EPS[h] for h in hk)
            psi = heps - Fn - LNQ * (H - Hmin)
            if Mn is None or psi > Mn:
                Mn, argM = psi, lam
            if n > N_EXACT:
                continue
            n_shapes += 1
            tv = t_vec(lam)
            betas = [lam[i] + ell - 1 - i for i in range(ell)]
            # (a), (b)
            pair = mp.fsum(EPS[betas[i] - betas[j]] for i in range(ell) for j in range(i + 1, ell))
            one = mp.fsum(F(b) for b in betas)
            worst_ab = max(worst_ab, abs(heps - (one - pair)))
            if 2 * H != sum(x * x for x in tv) - m_sq_sum(ell):
                v_ab += 1
            # (c)
            lowp = mp.fsum((ell - kk) * EPS[2 * kk] for kk in range(1, ell)) - mp.fsum(
                DEPS2[kk] * mp.mpf(delta_k(tv, kk).numerator) / delta_k(tv, kk).denominator
                for kk in range(1, ell))
            sl = pair - lowp
            if sl < -tol:
                v_tan += 1
            min_tan_slack = sl if min_tan_slack is None else min(min_tan_slack, sl)
            # (d)
            Tsum = Fraction(2 * n + ell * ell, 2)
            assert sum(tv) == Tsum
            p, tau, mf = waterfill(ell, Tsum)
            d = [a - b for a, b in zip(tv, p)]
            ysq = sum(x * x for x in d)
            if sum(x * x for x in tv) < sum(x * x for x in p) + ysq:
                v_pyth += 1
            for kk in range(1, ell):
                if delta_k(p, kk) > 0:
                    v_mono += 1
                dk = delta_k(d, kk)
                if dk > 0 and dk * dk > 2 * min(kk, ell - kk) * ysq:
                    v_cs += 1
            qv = rounded_feasible(ell, p, tau, mf)
            gsum = 2 * Hmin_l[ell] + m_sq_sum(ell)
            if not is_partition_t(ell, qv) or sum(qv) != Tsum:
                v_round += 1
            if gsum > sum(x * x for x in p) + Fraction(ell, 4) or gsum > sum(x * x for x in qv):
                v_round += 1
            exc = sum(x * x for x in qv) - sum(x * x for x in p)
            if ell > 0:
                max_round_excess_ratio = max(max_round_excess_ratio, exc / ell)
            # (e)
            if 2 * (Hmin_l[ell] - Hmin) < (ell - k) ** 2 - r and ell > k:
                v_e += 1
            # chain (S6)
            y = mp.sqrt(mp.mpf(ysq.numerator) / ysq.denominator)
            e_in = max(mp.mpf(0), y * y - mp.mpf(ell) / 4)
            rhs = (ell * A_CONST + S2_CONST - Fn + C_PAIR * y - LNQ / 2 * e_in
                   - LNQ * (Hmin_l[ell] - Hmin))
            if psi > rhs + tol:
                v_chain += 1
        U, Uarg = U_of(n)
        Mrows.append({"n": n, "k": k, "r": r, "M_n": mp.nstr(Mn, 20), "argmax": list(argM),
                      "U_n": mp.nstr(U, 15), "U_argmax_l": Uarg,
                      "closed_form": mp.nstr(closed_form(n), 15),
                      "A_sqrt_2n": mp.nstr(A_CONST * mp.sqrt(2 * n), 15),
                      "bound_7185": mp.nstr((C_CONST + LNQ / 2) * mp.sqrt(2 * n)
                                            + C_CONST ** 2 / (2 * LNQ) - C_CONST, 15)})
        print(f"  n={n:3d} shapes={len(shapes):6d}  M_n={mp.nstr(Mn, 10)}  U={mp.nstr(U, 10)}  "
              f"[{time.time() - t0:.1f}s]", flush=True)

    check("S2_identities_a_I_prime_and_b_completed_square",
          worst_ab < tol and v_ab == 0,
          f"{n_shapes} shapes n <= {N_EXACT}: |sum_c eps(h) - (sum F(beta) - P)| <= "
          f"{mp.nstr(worst_ab, 3)}; 2H = sum t^2 - sum m^2 exact, violations {v_ab}.")
    check("S3_tangent_pair_bound_by_neighbour_order",
          v_tan == 0,
          f"P >= sum_k (l-k) eps(2k) - sum_k |eps'(2k)| Delta_k(t) on {n_shapes} shapes: violations "
          f"{v_tan}, min slack {mp.nstr(min_tan_slack, 6)} (0 on the staircase shapes, where every "
          f"k-th neighbour distance is exactly 2k).")
    check("S4_hard_wall_projection_pythagoras_monotone_CS_rounding",
          v_pyth == 0 and v_mono == 0 and v_cs == 0 and v_round == 0,
          f"exact rationals, {n_shapes} shapes: Pythagoras viol {v_pyth}; Delta_k(p) > 0 viol "
          f"{v_mono}; Cauchy-Schwarz viol {v_cs}; rounding (feasible, sum preserved, "
          f"2H_l^min + sum m^2 <= sum p^2 + l/4) viol {v_round}; worst rounding excess / l = "
          f"{max_round_excess_ratio} (bound 1/4).")
    check("S5_row_count_energy_tangent_bound_7185",
          v_e == 0,
          f"2(H_l^min - H_min(n)) >= (l-k)^2 - r for l > k, all (n, l), n <= {N_EXACT}: violations {v_e}.")
    check("S6_per_shape_chain",
          v_chain == 0,
          f"Psi(lambda) <= l A + S2 - F(n) + c y - (L/2)max(0,y^2-l/4) - L(H_l^min - H_min) on all "
          f"{n_shapes} shapes n <= {N_EXACT}: violations {v_chain}.")
    okM = all(mp.mpf(rw["M_n"]) <= mp.mpf(rw["U_n"]) <= mp.mpf(rw["closed_form"]) for rw in Mrows)
    check("S7_M_n_le_U_n_le_closed_form",
          okM,
          f"exact M_n (full scan) <= U(n) <= A sqrt(2n) + (A+c)(2n)^(1/4) + K0 for n = 1..{N_SCAN}. "
          f"n={N_SCAN}: M={Mrows[-1]['M_n'][:10]}, U={Mrows[-1]['U_n'][:10]}, closed="
          f"{Mrows[-1]['closed_form'][:10]}, #7185 bound={Mrows[-1]['bound_7185'][:10]}. The constants "
          f"are large (asymptotic statement); at reachable n the bound is looser than #7185's.")

    # ------------------------------------------------------------- S8 rate scan
    scan = []
    for e in range(2, 11):
        n = 10 ** e
        U, Uarg = U_of(n)
        s2n = mp.sqrt(2 * n)
        scan.append({"n": n, "U_over_sqrt2n": mp.nstr(U / s2n, 15),
                     "excess_over_quarter": mp.nstr((U - A_CONST * s2n) / mp.mpf(2 * n) ** mp.mpf("0.25"), 12),
                     "U_minus_closed": mp.nstr(U - closed_form(n), 12),
                     "U_argmax_l_minus_k": Uarg - k_r_of(n)[0]})
        print(f"  n=1e{e}: U/sqrt(2n)={scan[-1]['U_over_sqrt2n']}  "
              f"(U-A sqrt2n)/(2n)^.25={scan[-1]['excess_over_quarter']}", flush=True)
    rat = [mp.mpf(s["U_over_sqrt2n"]) for s in scan]
    exq = [mp.mpf(s["excess_over_quarter"]) for s in scan]
    ok8 = (all(rat[i] > rat[i + 1] for i in range(len(rat) - 1)) and rat[-1] - A_CONST < mp.mpf("0.02")
           and all(mp.mpf(s["U_minus_closed"]) <= 0 for s in scan) and max(exq[4:]) <= A_CONST + C_PAIR)
    check("S8_rate_scan_U_over_sqrt2n_tends_to_A",
          ok8,
          "U(n)/sqrt(2n) = " + ", ".join(f"1e{i + 2}:{str(s['U_over_sqrt2n'])[:8]}" for i, s in enumerate(scan))
          + f" -> A = {mp.nstr(A_CONST, 10)} (decreasing; U <= closed form at every n); "
          f"(U - A sqrt(2n))/(2n)^(1/4) = " + ", ".join(str(s['excess_over_quarter'])[:6] for s in scan)
          + f"; <= A + c = {mp.nstr(A_CONST + C_PAIR, 6)} for n >= 1e6 (the K0/(2n)^(1/4) part dominates below). "
          f"The approach to A is SLOW (1e10: +0.30 %), as an O(n^(-1/4)) correction must be. This is the RATE of a "
          f"proved bound, not a measurement of M_n.")

    n_ok = sum(1 for x in results if x["pass"])
    print("\n" + "=" * 78)
    print(f"{n_ok}/{len(results)} checks passed   [{time.time() - t0:.1f}s]")
    print("VERDICT: M_n <= A sqrt(2n) + (A + c)(2n)^{1/4} + K0; limsup M_n/sqrt(2n) <= A (sharp: the "
          "staircase attains A at triangular n). Error O(n^{1/4}), NOT O(1): e_inf not reached.")
    print("=" * 78)

    payload = {
        "probe": "rev_sharp_coefficient_upper_bound_probe",
        "bean": ["qou-fxym", "qou-3e6w", "qou-hok7"],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "constants": {
            "A": mp.nstr(A_CONST, 40), "E2": mp.nstr(E2_CONST, 40), "C": mp.nstr(C_CONST, 40),
            "ln_q0": mp.nstr(LNQ, 40), "c_pair": mp.nstr(C_PAIR, 40), "S2": mp.nstr(S2_CONST, 40),
            "K0": mp.nstr(K0_CONST, 30), "A_sqrt2": mp.nstr(A_CONST * mp.sqrt(2), 30),
        },
        "statements": {
            "(c)": "P >= sum_{k<l}(l-k) eps(2k) - sum_k |eps'(2k)| Delta_k(t)  (tangent lines at 2k)",
            "(d)": "t in K={sum t=T, t_i>=i+1/2}; p=proj_K(0) nondecreasing; sum t^2 >= sum p^2 + |t-p|^2; "
                   "2(H - H_l^min) >= max(0, |t-p|^2 - l/4)",
            "(e)": "2(H_l^min - H_min(n)) >= (l-k)^2 - r  (#7185)",
            "main": "M_n <= A sqrt(2n) + (A + c)(2n)^{1/4} + K0, K0 = S2 + c^2/(2L) + c/2 + (A+c/2)^2/L",
            "corollary": "limsup M_n / sqrt(2n) <= A; = A along triangular n (staircase)",
            "not_established": "M_n = A sqrt(2n + 1/4) + kappa + o(1) (the e_inf constant); error here is O(n^{1/4})",
        },
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "n_exact": N_EXACT,
        "n_scan": N_SCAN,
        "table": Mrows,
        "rate_scan": scan,
    }
    out = os.path.join(_COMPUTATIONS, "rev-sharp-coefficient-upper-bound.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
