#!/usr/bin/env python3
r"""
rev_sqrt_n_upper_bound_probe.py — REV_n = O(sqrt n): re-derivation, exact verification, and the
bound-vs-REV table (qou-0ie7 / qou-hok7)

`qou-hok7` left one thing open after #7014 / #7018 / #7065 / #7070 / #7081 / #7093:

    Omega(sqrt n)  <=  REV_n  <=  O(n^{3/4})        -- is the 3/4 sharp?

A dispatched agent (qou-0ie7, 2026-09-07) died uncommitted after CLAIMING a short proof that the
upper bound is O(sqrt n).  This probe re-derives that claim from the definitions the corpus
actually uses, looks for the flaw, and verifies every step exactly.  The Lean half is
`folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumRowTangentBound.lean`.

## 0. Definitions (exactly as the corpus computes them)

`t := q_0^2`, `q_0` the proton pin.  `zn_hook_length_closed_form_probe.py` (C2):

    Z_n(q) = q^{-n} sum_{lambda |- n} q^{H(lambda)} [n]_t! / prod_c [h(c)]_t ,   [m]_t = (t^m-1)/(t-1)

with `H(lambda) = sum_c h(c)` the total hook length, `deg Z_n = n^2 - H_min(n)`,
`H_min(n) = min_lambda H(lambda)`.  `rev_free_energy_over_shapes_probe.py` (F):

    REV_n := log Z_n(q_0) - (deg Z_n) ln q_0  =  log sum_lambda exp( R_lambda - E_lambda ),
    E_lambda := (H(lambda) - H_min(n)) ln q_0  >= 0,
    R_lambda := log term_lambda(q_0) - (n^2 - H(lambda)) ln q_0 ,   term_lambda = the summand of (C2).

`M_n := max_lambda (R_lambda - E_lambda)`.  Since every summand is positive,

    M_n  <=  REV_n  <=  M_n + log p(n).                                                  (0)

## 1. R_lambda is a hook-length energy (exact)

`log [m]_t = 2m ln q_0 - ln(t-1) - eps_m` with `eps_m := -log(1 - t^{-m}) > 0`.  Substituting into
`R_lambda = (2H - n - n^2) ln q_0 + sum_{i<=n} log[i]_t - sum_c log[h(c)]_t`, every `ln q_0` and every
`ln(t-1)` cancels identically (the `ln q_0` coefficient is `2H - n - n^2 + n(n+1) - 2H = 0`), leaving

    R_lambda = sum_c eps_{h(c)} - F(n),      F(k) := sum_{m<=k} eps_m,   C := F(infinity) = 6.1714 .   (1)

This is (I') of #7070 before the beta-coordinate change of variables.  Checked in R1.

## 2. R_lambda <= (l - 1) C, with l the number of rows

Hook lengths strictly decrease along a row (`hookZ_strictAnti_row`, `card_row_filter_hookZ_le_one`
in `HookSumThicknessBound.lean`, PR #7018), so `N_m(lambda) := #{c : h(c) = m} <= l`.  Then

    R_lambda = sum_{m<=n} eps_m (N_m - 1)  <=  (l-1) sum_{m : N_m >= 1} eps_m  <=  (l - 1) C .        (2)

Prior work bounded this by `C r` with `r = min(l, lambda_1)` and then used `r <= sqrt(H)`
(#7018), which is what produced the exponent 3/4.  The point of the dead agent's route is to keep
`l` and bound the ENERGY as a function of `l` instead.  Checked in R2.

## 3. The row form of H

From `sum_hookZ_eq`, `two_mul_sum_snd`, `sum_fst_eq_bStat` (`HookSumClosedForm.lean`), rows
0-indexed, `lambda_i = mu.rowLen i`:

    2H = sum_{i<l} lambda_i (lambda_i - 1) + 2 sum_{i<l} i lambda_i + 2n = sum_{i<l} lambda_i (lambda_i + 2i + 1).   (3)

## 4. The tangent-line lower bound (the actual content of the claim)

Put `m_i := lambda_i - 1 >= 0`.  Row `i` contributes `(m_i+1)(m_i+2i+2) = m_i^2 + 2(i+1) m_i + m_i + 2(i+1)`.
For any integer `j >= 0`, per row:

  * if `i+1 <= j`:  `m^2 + 2(i+1) m  >=  2j m + 2(i+1) j - (i+1)^2 - j^2`,  i.e. `(m + i + 1 - j)^2 >= 0`;
  * if `i+1 >  j`:  `m^2 + 2(i+1) m  >=  2j m`,                            since `m >= 0`, `i+1 >= j`.

Both are `(2j+1) m + 2(i+1) - ((j - (i+1))_+)^2` on the right after adding `m + 2(i+1)`.  Summing over
`i < l` with `sum m_i = n - l`, `2 sum (i+1) = l(l+1)`:

    2H(lambda)  >=  l(l+1) + (n - l)(2j+1) - sum_{i<l} ((j-1-i)_+)^2         for every j >= 0.    (4)

For `j <= l` the last sum is `P_{j-1} := sum_{d<j} d^2 = j(j-1)(2j-1)/6`.  (4) is EXACT (equality) on
the shapes `delta_j + 1^{l-j}` (staircase padded by rows of length 1), which are the minimisers of `H`
at fixed `(n, l)` when `n - l = T_{j-1}`; so (4) is the sharp bound in the regime that matters.

## 5. Specialise j = k, n = T_k + r  (T_k = k(k+1)/2, 0 <= r <= k)

`H^+ := P_k + r(k+1) = H(lambda^+)`, `lambda^+ = delta_k` with its first `r` rows extended by one
cell — the min-hook shape (`hmin_closed_form_and_rev_sublinearity_probe.py`, verified n <= 26; R3
here re-verifies `H^+ = H_min(n)` exactly for n <= 30).  For `l >= k`, (4) with `j = k` and
`6 P_k = k(k+1)(2k+1)` gives, as a polynomial IDENTITY (no slack),

    2 ( H(lambda) - H^+ )  >=  (l - k)^2  -  r .                                                    (5)

For `l <= k` the same (4) with `j = k` (now `j >= l`, the sum in (4) is `P_{k-1} - P_{k-l-1}`) gives

    2 ( H(lambda) - H^+ )  >=  -r  +  (k-l)(2k+1-2l)(k+1-l)/6   >=  -r .                           (5')

(5) is the dead agent's `H - H_min >= (l-k)_+^2/2 - r/2`, now with a proof; (5') is the same
statement on the other side, which the recovered block did not state but which the Lean covers so
that no appeal to "H >= H_min trivially" is needed.  Checked in R3 (exact integers, n <= 30).

## 6. The maximum over shapes

Group `lambda` by `l`.  By (2) and (5)/(5'), with `x := l - k`, `L := ln q_0`:

    M_n <= max_l [ (l-1) C - E_min(l) L ]
        <= max( (k-1) C + rL/2 ,  max_{x>=1} [ (k-1+x) C - (x^2/2 - r/2) L ] )
        <= (k-1) C + (r/2) L + max_{x real} ( x C - x^2 L / 2 )
        =  (k-1) C + (r/2) L + C^2 / (2L).                                                        (6)

With `k <= sqrt(2n)` and `r <= k`:

    M_n  <=  (C + L/2) sqrt(2n) + C^2/(2L) - C   =   8.80 sqrt(n) + 176.5 .                          (6')

The maximiser of the quadratic in (6) is `x^* = C/L = 59.2` rows above the staircase — which is
exactly the drift #7081 observed in its own argmax (`l = 151` at `n = 4000` against
`sqrt(2n) = 89`, `x = 62`) and could not explain.  Checked in R4 and R6.

## 7. REV_n = O(sqrt n), hence Theta(sqrt n)

`log p(n) < pi sqrt(2n/3)` for all n >= 1 (Apostol, *Introduction to Analytic Number Theory*,
Thm 14.5 — an elementary bound, not the asymptotic).  With (0) and (6'):

    REV_n  <=  (C + L/2 + pi/sqrt 3) sqrt(2n) + C^2/(2L) - C  =  11.37 sqrt(n) + 176.5 .             (7)

Together with the prior `REV_n = Omega(sqrt n)` (#7014):  **REV_n = Theta(sqrt n)**, and the
exponent 3/4 of #7018 is NOT sharp.  Every constant in (7) is explicit; nothing is fitted.

## Where the flaw was looked for, and not found

  * (2): `C r` vs `(l-1) C` — using `l` instead of `min(l, lambda_1)` only weakens the bound on R, and is
    what lets the energy be indexed by `l`.  Not a flaw.
  * (5) at `l < k`: the recovered block's `(l-k)_+^2/2 - r/2` reads `-r/2` there, weaker than
    `H >= H_min`; harmless, and (5') proves it anyway.
  * The `r` of (5) is `n - T_k`, NOT the `r = min(l, lambda_1)` of #7018/#7070.  The recovered block
    overloaded the letter; the two never meet in the argument.
  * #7081 measured a relaxation whose `/ n^{3/4}` column RISES to n = 4000.  That relaxation's H lower
    bound (`Hhat`, Cauchy–Schwarz on both halves of `2H = p_2(lambda) + p_2(lambda')`) sits at ~50 % of
    `H_min(n)` at its own argmax `(l, W) = (151, 357)`: the column half assumes the `n - l` remaining
    cells spread evenly over `lambda_1 - 1` columns, which no partition with 151 rows does.  The
    resulting negative "energy" is what its maximiser fed on.  Its calibration to 99–100 % was at
    n <= 40, where `l - k` is small.  So the rise is an artefact of the instrument, not evidence
    against (7).  R5 reproduces the effect at reachable n.

## Checks

  R1  (1): `R_lambda = sum_c eps_{h(c)} - F(n)` against the corpus's `shape_terms` R, all shapes n <= 16.
  R2  (2): `N_m <= l` and `R_lambda <= (l-1) C`, all shapes n <= 30 (exact count; 60-dps R).
  R3  (4),(5),(5'): exact integer inequalities on ALL partitions n <= 30 and all 0 <= j <= n+1;
      `H_min(n)` closed form equals the brute-force minimum and `H(lambda^+) = P_k + r(k+1)`, n <= 30;
      equality cases of (5) recorded.
  R4  (0),(6),(6'),(7): exact `M_n`, `REV_n`, `E_min(l)` by full scan for n <= 44 (60 dps); each link of
      `M_n <= U_exact <= U_tan <= U^* <= (6')` and `REV_n <= M_n + log p(n) <= (7)` holds.
  R5  (b) of the recovered block: the constrained one-body bound `max_lambda [sum_i F(beta_i) - F(n) - E]`
      (the Sigma-beta = n + l(l-1)/2 constraint enforced by enumeration, pair term dropped), against
      `M_n`; and the `Hhat`-relaxation defect of #7081 reproduced at n <= 44.
  R6  (c) of the recovered block: rate scan of `U^*(n)/sqrt n` to n = 10^6 from the closed form (no
      enumeration), converging to `(C + L/2) sqrt 2`.

Arithmetic: `mpmath` at 60 dps; all hook sums, counts and inequalities (4)/(5)/(5') in exact integers.
No float64 anywhere.  Witness: `computations/rev-sqrt-n-upper-bound.witness.json`.
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

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

from zn_hook_length_closed_form_probe import hooks, min_total_hook, partitions  # noqa: E402
from rev_free_energy_over_shapes_probe import shape_terms  # noqa: E402

N_EXACT = int(os.environ.get("REV_SQRTN_N_EXACT", "30"))   # exact-inequality sweep
N_SCAN = int(os.environ.get("REV_SQRTN_N_SCAN", "44"))     # full M_n / REV_n scan
N_IDENT = 16                                               # identity (1) against shape_terms

# ---------------------------------------------------------------------------------------------
# eps_m, F, C  (same convention as rev_beta_coordinate_identity_probe.py, #7070)
# ---------------------------------------------------------------------------------------------
_NEPS = 2000  # t^{-2000} ~ 1e-181, far below 60 dps
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]
C_CONST = _F[_NEPS - 1]


def F(k: int):
    return _F[min(k, _NEPS - 1)]


# ---------------------------------------------------------------------------------------------
# exact combinatorics
# ---------------------------------------------------------------------------------------------
def tri(k: int) -> int:
    return k * (k + 1) // 2


def pyr(k: int) -> int:
    """P_k = sum_{i=1}^k i^2 = k(k+1)(2k+1)/6 = H(delta_k)."""
    return k * (k + 1) * (2 * k + 1) // 6


def k_r_of(n: int) -> tuple:
    """n = T_k + r with k maximal, 0 <= r <= k."""
    k = 0
    while tri(k + 1) <= n:
        k += 1
    return k, n - tri(k)


def h_plus(n: int) -> int:
    """H(lambda^+) = P_k + r(k+1), the closed-form min hook sum."""
    k, r = k_r_of(n)
    return pyr(k) + r * (k + 1)


def lambda_plus(n: int) -> tuple:
    k, r = k_r_of(n)
    return tuple((k - i) + (1 if i < r else 0) for i in range(k)) if k > 0 else ()


def total_hook_rowform(lam: tuple) -> int:
    """2H = sum_{i<l} lambda_i (lambda_i + 2i + 1), 0-indexed rows (eq. (3))."""
    s = 0
    for i, li in enumerate(lam):
        s += li * (li + 2 * i + 1)
    assert s % 2 == 0
    return s // 2


def tangent_rhs(n: int, ell: int, j: int) -> int:
    """RHS of (4): l(l+1) + (n-l)(2j+1) - sum_{i<l} ((j-1-i)_+)^2, exact integer."""
    corr = 0
    for i in range(ell):
        d = j - 1 - i
        if d > 0:
            corr += d * d
    return ell * (ell + 1) + (n - ell) * (2 * j + 1) - corr


def count_partitions(n: int) -> int:
    p = [1] + [0] * n
    for part in range(1, n + 1):
        for s in range(part, n + 1):
            p[s] += p[s - part]
    return p[n]


def R_of(lam: tuple, n: int):
    """R_lambda by (1): sum_c eps_{h(c)} - F(n)."""
    s = mp.mpf(0)
    for h in hooks(lam):
        s += EPS[h]
    return s - F(n)


def logsumexp(vals):
    m = max(vals)
    acc = mp.mpf(0)
    for v in vals:
        acc += mp.exp(v - m)
    return m + mp.log(acc)


def u_star(n: int):
    """Closed-form (6): (k-1)C + (r/2)L + max_{x>=0 integer} (xC - x^2 L/2), and the integer argmax."""
    k, r = k_r_of(n)
    best, bx = mp.mpf(0), 0
    x = 0
    while True:
        v = x * C_CONST - mp.mpf(x * x) / 2 * LNQ
        if v > best:
            best, bx = v, x
        elif x > bx + 2:
            break
        x += 1
    return (k - 1) * C_CONST + mp.mpf(r) / 2 * LNQ + best, bx


def u_bound_67(n: int):
    """(6'): (C + L/2) sqrt(2n) + C^2/(2L) - C."""
    return (C_CONST + LNQ / 2) * mp.sqrt(2 * n) + C_CONST ** 2 / (2 * LNQ) - C_CONST


def main() -> int:
    t0 = time.time()
    results = []

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}")

    print("=" * 78)
    print("rev_sqrt_n_upper_bound_probe  --  REV_n = O(sqrt n)")
    print("=" * 78)
    print(f"  q0 = {mp.nstr(Q0, 25)}  (proton pin)   ln q0 = {mp.nstr(LNQ, 15)}")
    print(f"  C  = sum_m eps_m = {mp.nstr(C_CONST, 20)}     C/L = {mp.nstr(C_CONST / LNQ, 10)}")
    print(f"  (C + L/2) sqrt2 = {mp.nstr((C_CONST + LNQ / 2) * mp.sqrt(2), 12)}   "
          f"C^2/(2L) - C = {mp.nstr(C_CONST ** 2 / (2 * LNQ) - C_CONST, 12)}")

    # ------------------------------------------------------------------ R1: identity (1)
    worst = mp.mpf(0)
    n_shapes = 0
    for n in range(1, N_IDENT + 1):
        for (lam, H, R, _E) in shape_terms(n):
            diff = abs(R - R_of(lam, n))
            worst = max(worst, diff)
            n_shapes += 1
    tol = mp.mpf(10) ** (-(mp.dps - 15))
    check(
        "R1_R_lambda_is_hook_epsilon_sum_minus_F_n",
        worst < tol,
        f"R_lambda = sum_c eps_h(c) - F(n) against shape_terms' R for all {n_shapes} shapes with "
        f"n <= {N_IDENT}: worst |difference| = {mp.nstr(worst, 5)} (tolerance {mp.nstr(tol, 3)}). "
        f"Every ln q0 and ln(t-1) cancels identically; this is (I') of #7070 before the beta change "
        f"of variables.",
    )

    # ------------------------------------------------------------------ R2 + R3 + energy minima
    viol_Nm = viol_R2 = viol_4 = viol_5 = viol_5p = viol_rowform = 0
    hmin_mismatch = hplus_mismatch = 0
    eq5_cases = []
    n_parts_total = 0
    emin_by_ell = {}        # n -> {l: min H over partitions with exactly l rows}
    for n in range(1, N_EXACT + 1):
        k, r = k_r_of(n)
        hp = h_plus(n)
        Hmin_brute = None
        emin = {}
        lp = lambda_plus(n)
        if sum(lp) != n or total_hook_rowform(lp) != hp:
            hplus_mismatch += 1
        for lam in partitions(n):
            n_parts_total += 1
            ell = len(lam)
            hs = hooks(lam)
            H = sum(hs)
            if total_hook_rowform(lam) != H:
                viol_rowform += 1
            Hmin_brute = H if Hmin_brute is None else min(Hmin_brute, H)
            emin[ell] = H if ell not in emin else min(emin[ell], H)
            # (2): N_m <= l, R <= (l-1) C
            cnt = {}
            for h in hs:
                cnt[h] = cnt.get(h, 0) + 1
            if max(cnt.values()) > ell:
                viol_Nm += 1
            if R_of(lam, n) > (ell - 1) * C_CONST + mp.mpf(10) ** (-40):
                viol_R2 += 1
            # (4) for all j
            for j in range(0, n + 2):
                if 2 * H < tangent_rhs(n, ell, j):
                    viol_4 += 1
            # (5) / (5')
            if ell >= k:
                lhs = 2 * (H - hp)
                rhs = (ell - k) ** 2 - r
                if lhs < rhs:
                    viol_5 += 1
                elif lhs == rhs:
                    eq5_cases.append((n, lam))
            else:
                cub6 = (k - ell) * (2 * k + 1 - 2 * ell) * (k + 1 - ell)
                assert cub6 % 6 == 0
                if 2 * (H - hp) < -r + cub6 // 6:
                    viol_5p += 1
        hm_closed, _ = min_total_hook(n)
        if Hmin_brute != hp or hm_closed != hp:
            hmin_mismatch += 1
        emin_by_ell[n] = emin

    check(
        "R2_N_m_le_rows_and_R_le_rows_minus_one_times_C",
        viol_Nm == 0 and viol_R2 == 0,
        f"all {n_parts_total} partitions with n <= {N_EXACT}: #{{c : h(c)=m}} <= l for every m "
        f"({viol_Nm} violations) and R_lambda <= (l-1) C ({viol_R2} violations, C = "
        f"{mp.nstr(C_CONST, 12)}). The prior chain used C r with r = min(l, lambda_1) and then "
        f"r <= sqrt(H); this keeps l and prices the energy against l instead.",
    )
    check(
        "R3_tangent_bound_and_its_j_eq_k_specialisation_exact",
        viol_rowform == 0 and viol_4 == 0 and viol_5 == 0 and viol_5p == 0
        and hmin_mismatch == 0 and hplus_mismatch == 0,
        f"exact integers, all partitions n <= {N_EXACT}: row form (3) matches the cell hook sum "
        f"({viol_rowform} mismatches); (4) 2H >= l(l+1) + (n-l)(2j+1) - sum_(i<l)((j-1-i)_+)^2 for "
        f"every 0 <= j <= n+1 ({viol_4} violations); (5) 2(H - H+) >= (l-k)^2 - r for l >= k "
        f"({viol_5} violations, equality in {len(eq5_cases)} cases, e.g. "
        f"{[(n, list(l)) for n, l in eq5_cases[:4]]}); (5') 2(H - H+) >= -r + (k-l)(2k+1-2l)(k+1-l)/6 "
        f"for l < k ({viol_5p} violations). H+ = P_k + r(k+1) equals the brute-force H_min(n) and the "
        f"committed closed form ({hmin_mismatch} mismatches), and H(lambda+) = H+ "
        f"({hplus_mismatch} mismatches).",
    )

    # ------------------------------------------------------------------ R4: full scan to N_SCAN
    print(f"\n  full scan to n = {N_SCAN} ...")
    rows = []
    all_links_ok = True
    hr_ok = True
    for n in range(2, N_SCAN + 1):
        ts = time.time()
        k, r = k_r_of(n)
        hp = h_plus(n)
        Fn = F(n)
        M = None
        M_shape = None
        vals = []
        emin = {}
        bsig = None   # R5: constrained one-body bound, pair term dropped
        for lam in partitions(n):
            ell = len(lam)
            hs = hooks(lam)
            H = sum(hs)
            emin[ell] = H if ell not in emin else min(emin[ell], H)
            E = (H - hp) * LNQ
            s = mp.mpf(0)
            for h in hs:
                s += EPS[h]
            R = s - Fn
            v = R - E
            vals.append(v)
            if M is None or v > M:
                M, M_shape = v, lam
            # one-body term in beta coordinates: sum_i F(beta_i) - F(n), beta_i = lambda_i + l - i (1-indexed)
            ob = mp.mpf(0)
            for i, li in enumerate(lam):
                ob += F(li + ell - (i + 1))
            vb = ob - Fn - E
            if bsig is None or vb > bsig:
                bsig = vb
        REV = logsumexp(vals)
        p_n = count_partitions(n)
        log_p = mp.log(p_n)
        # U_exact: max_l (l-1)C - (Emin(l) - H+) L
        u_exact = max((ell - 1) * C_CONST - (Hm - hp) * LNQ for ell, Hm in emin.items())
        # U_tan: same with the tangent lower bound (5)/(5') in place of Emin(l)
        u_tan = None
        for ell in range(1, n + 1):
            if ell >= k:
                two_e = (ell - k) ** 2 - r
            else:
                two_e = -r + (k - ell) * (2 * k + 1 - 2 * ell) * (k + 1 - ell) // 6
            v = (ell - 1) * C_CONST - mp.mpf(two_e) / 2 * LNQ
            u_tan = v if u_tan is None else max(u_tan, v)
        ust, xst = u_star(n)
        u67 = u_bound_67(n)
        rev_ub = M + log_p
        hr = mp.pi * mp.sqrt(mp.mpf(2 * n) / 3)
        u7 = u67 + hr
        slack = mp.mpf(10) ** (-45)
        links = (M <= u_exact + slack, u_exact <= u_tan + slack, u_tan <= ust + slack,
                 ust <= u67 + slack, REV <= rev_ub + slack, log_p <= hr, REV <= u7)
        if not all(links):
            all_links_ok = False
        if not (log_p <= hr):
            hr_ok = False
        rows.append({
            "n": n, "k": k, "r": r, "H_plus": hp, "p_n": p_n,
            "M_n": mp.nstr(M, 20), "M_argmax": list(M_shape),
            "REV_n": mp.nstr(REV, 20), "log_p_n": mp.nstr(log_p, 20),
            "U_exact_rows": mp.nstr(u_exact, 20), "U_tangent": mp.nstr(u_tan, 20),
            "U_star": mp.nstr(ust, 20), "U_star_argmax_x": xst,
            "bound_6prime": mp.nstr(u67, 20), "bound_7_REV": mp.nstr(u7, 20),
            "B_sigma_onebody": mp.nstr(bsig, 20),
            "Emin_by_rows": {str(ell): Hm - hp for ell, Hm in sorted(emin.items())},
            "links_ok": all(bool(x) for x in links),
        })
        if n % 4 == 0 or n == N_SCAN:
            print(f"    n={n:2d} p={p_n:7d}  M={mp.nstr(M, 8):>10}  REV={mp.nstr(REV, 8):>10}  "
                  f"Uex={mp.nstr(u_exact, 8):>10}  Utan={mp.nstr(u_tan, 8):>10}  "
                  f"U*={mp.nstr(ust, 8):>10}  (6')={mp.nstr(u67, 8):>10}  "
                  f"Bsig={mp.nstr(bsig, 7):>9}  [{time.time() - ts:5.1f}s]")

    last = rows[-1]
    check(
        "R4_every_link_of_the_chain_holds_to_n_scan",
        all_links_ok and hr_ok,
        f"n = 2..{N_SCAN}, exact scan over p(n) shapes, 60 dps: M_n <= U_exact(rows) <= U_tangent "
        f"<= U* <= (6') and REV_n <= M_n + log p(n) <= (6') + pi sqrt(2n/3) = (7) at every n "
        f"({'0' if all_links_ok else 'SOME'} link failures); log p(n) <= pi sqrt(2n/3) at every n. "
        f"At n={N_SCAN}: M={last['M_n'][:9]}, REV={last['REV_n'][:9]}, U_exact={last['U_exact_rows'][:9]}, "
        f"U_tangent={last['U_tangent'][:9]}, U*={last['U_star'][:9]}, (6')={last['bound_6prime'][:9]}, "
        f"(7)={last['bound_7_REV'][:9]}. The bound is loose by a large constant (C^2/(2L) = "
        f"{mp.nstr(C_CONST ** 2 / (2 * LNQ), 6)}) but its GROWTH is sqrt n, which is the claim.",
    )

    # U_exact vs U_tangent: how much does the tangent step lose?
    gaps = [(row["n"], mp.mpf(row["U_tangent"]) - mp.mpf(row["U_exact_rows"])) for row in rows]
    print("  U_tangent - U_exact (tangent-step loss, should be <= r L / 2 + small): "
          + ", ".join(f"n={n}:{mp.nstr(g, 5)}" for n, g in gaps[-5:]))

    # ------------------------------------------------------------------ R5: (b) constrained bound
    recovered_b = {16: "16.11", 24: "26.14", 32: "34.25", 40: "40.04", 44: "42.24"}
    recovered_7081 = {16: "35.07", 24: "46.30", 32: "54.96", 40: "61.13"}
    tbl = []
    ok_b = True
    for row in rows:
        n = row["n"]
        if n in recovered_b:
            Bs = mp.mpf(row["B_sigma_onebody"])
            M = mp.mpf(row["M_n"])
            # theirs kept a (positive) Jensen pair term, so theirs <= ours is expected
            rec = mp.mpf(recovered_b[n])
            ok_b = ok_b and (M <= Bs) and (rec <= Bs + mp.mpf("0.01"))
            tbl.append(f"n={n}: M_n={mp.nstr(M, 6)}  B_sigma(no pair)={mp.nstr(Bs, 6)}  "
                       f"recovered B_sigma={recovered_b[n]}  #7081={recovered_7081.get(n, '-')}")
    ratio_b = [(row["n"], mp.mpf(row["B_sigma_onebody"]) / mp.mpf(row["M_n"])) for row in rows
               if row["n"] >= 8]
    check(
        "R5_constrained_one_body_bound_table_b",
        ok_b,
        "(b) of the recovered block, re-measured with the Sigma-beta constraint enforced by "
        "enumeration and the pair term dropped (a valid relaxation of (I')): " + " | ".join(tbl)
        + ". M_n <= B_sigma at every n, and the recovered (pair-term-kept) values sit below it as "
        f"they must -- the pair term is most of the gap. B_sigma/M_n = "
        + ", ".join(f"n={n}:{mp.nstr(v, 4)}" for n, v in ratio_b[-4:])
        + ". None of this is needed for the proof; it cross-validates that enforcing Sigma-beta "
        "alone does not close the gap, which is why the route through (5) is the one that does.",
    )

    # -- R5b: the Hhat instrument of #7081 falls below H_min(n) once l >> sqrt(2n)
    def hhat_min(n: int, ell: int):
        """#7081's Cauchy-Schwarz lower bound 2H >= l1^2 + (n-l1)^2/(l-1) + l^2 + (n-l)^2/(l1-1),
        minimised over the row length l1 (2 <= l1 <= n-l+1), as an exact rational."""
        from fractions import Fraction
        best = None
        for l1 in range(2, n - ell + 2):
            v = Fraction(l1 * l1) + Fraction((n - l1) ** 2, ell - 1) + Fraction(ell * ell) \
                + Fraction((n - ell) ** 2, l1 - 1)
            best = v if best is None or v < best else best
        return best / 2

    n_art = rows[-1]["n"]
    k_art, _ = k_r_of(n_art)
    hp_art = h_plus(n_art)
    emin_art = {int(a): b + hp_art for a, b in rows[-1]["Emin_by_rows"].items()}
    art_rows = []
    below = 0
    for ell in sorted(emin_art):
        if ell < 2 or ell > n_art - 1:
            continue
        hh = hhat_min(n_art, ell)
        art_rows.append((ell, hh, emin_art[ell]))
        if hh < hp_art:
            below += 1
    # the n = 4000 case of #7081's own argmax, from the formula alone (no enumeration possible)
    from fractions import Fraction
    n_big, ell_big = 4000, 151
    hh_big = hhat_min(n_big, ell_big)
    hp_big = h_plus(n_big)
    sample = [a for a in art_rows if a[0] in (k_art, 2 * k_art, 3 * k_art, n_art // 2)]
    check(
        "R5b_the_7081_Hhat_instrument_undershoots_H_min_for_many_rows",
        below > 0 and hh_big < Fraction(hp_big),
        f"at n={n_art} (k={k_art}): Hhat_min(l) / exact min H over l-row shapes / H_min(n)={hp_art}: "
        + "; ".join(f"l={a}: {mp.nstr(mp.mpf(b.numerator) / b.denominator, 6)} / {c}" for a, b, c in sample)
        + f". Hhat drops BELOW the global H_min(n) for {below} of the {len(art_rows)} row counts -- a "
        f"negative 'energy' no partition has. At #7081's own n=4000 argmax l=151: Hhat_min = "
        f"{mp.nstr(mp.mpf(hh_big.numerator) / hh_big.denominator, 8)} against H_min(4000) = {hp_big} "
        f"({mp.nstr(mp.mpf(hh_big.numerator) / hh_big.denominator / hp_big * 100, 4)} %). That credit "
        f"is what made its relaxation's /n^(3/4) column rise; it is an artefact of the H lower "
        f"bound used there, not evidence about REV_n. (5) has no such regime: its energy is >= -r/2.",
    )

    # ------------------------------------------------------------------ R6: (c) rate scan
    scan = []
    for n in [44, 100, 200, 1000, 4000, 10 ** 4, 10 ** 5, 10 ** 6]:
        ust, xst = u_star(n)
        k, r = k_r_of(n)
        scan.append({"n": n, "k": k, "r": r, "U_star": mp.nstr(ust, 15),
                     "U_star_over_sqrt_n": mp.nstr(ust / mp.sqrt(n), 12),
                     "U_star_over_n34": mp.nstr(ust / mp.mpf(n) ** mp.mpf("0.75"), 12),
                     "argmax_x": xst})
    lim = (C_CONST + LNQ / 2) * mp.sqrt(2)
    ratios = [mp.mpf(s["U_star_over_sqrt_n"]) for s in scan]
    falling = all(ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1))
    # U* - lim sqrt(n) is bounded by the additive constant of (6'), so the ratio converges like 1/sqrt n
    addc = C_CONST ** 2 / (2 * LNQ) + C_CONST
    close = all(abs(mp.mpf(s["U_star_over_sqrt_n"]) - lim) <= addc / mp.sqrt(s["n"]) for s in scan)
    x_stable = len({s["argmax_x"] for s in scan}) == 1
    check(
        "R6_rate_scan_U_star_over_sqrt_n_converges_to_C_plus_L_half_sqrt2",
        falling and close and x_stable,
        f"(c) of the recovered block from the closed form (6), no enumeration: U*/sqrt n = "
        + ", ".join(f"n={s['n']}:{s['U_star_over_sqrt_n'][:6]}" for s in scan)
        + f"; limit (C + L/2) sqrt2 = {mp.nstr(lim, 8)}, approached from above within "
        f"(C^2/(2L) + C)/sqrt n = {mp.nstr(addc, 6)}/sqrt n at every n; U*/n^(3/4) = "
        + ", ".join(f"{s['U_star_over_n34'][:6]}" for s in scan)
        + f" -> 0. The integer argmax is x = l - k = {scan[0]['argmax_x']} at every n "
        f"(C/L = {mp.nstr(C_CONST / LNQ, 6)}), matching the l - sqrt(2n) = 62 drift #7081 saw at "
        f"n = 4000 and could not explain.",
    )

    n_ok = sum(1 for x in results if x["pass"])
    print("\n" + "=" * 78)
    print(f"{n_ok}/{len(results)} checks passed   [{time.time() - t0:.1f}s]")
    print("VERDICT: REV_n <= (C + L/2 + pi/sqrt3) sqrt(2n) + C^2/(2L) - C = O(sqrt n); with the prior "
          "Omega(sqrt n), REV_n = Theta(sqrt n). The 3/4 exponent is NOT sharp.")
    print("=" * 78)

    payload = {
        "probe": "rev_sqrt_n_upper_bound_probe",
        "bean": ["qou-0ie7", "qou-hok7"],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "constants": {
            "C": mp.nstr(C_CONST, 40),
            "ln_q0": mp.nstr(LNQ, 40),
            "C_over_ln_q0": mp.nstr(C_CONST / LNQ, 20),
            "coef_sqrt_n_M": mp.nstr((C_CONST + LNQ / 2) * mp.sqrt(2), 20),
            "coef_sqrt_n_REV": mp.nstr((C_CONST + LNQ / 2 + mp.pi / mp.sqrt(3)) * mp.sqrt(2), 20),
            "additive_const": mp.nstr(C_CONST ** 2 / (2 * LNQ) - C_CONST, 20),
        },
        "statements": {
            "(1)": "R_lambda = sum_c eps_{h(c)} - F(n), eps_m = -log(1 - q0^{-2m})",
            "(2)": "R_lambda <= (l-1) C, l = number of rows",
            "(4)": "2H >= l(l+1) + (n-l)(2j+1) - sum_{i<l} ((j-1-i)_+)^2 for every j >= 0",
            "(5)": "l >= k, n = T_k + r: 2(H - P_k - r(k+1)) >= (l-k)^2 - r",
            "(5')": "l <= k: 2(H - P_k - r(k+1)) >= -r + (k-l)(2k+1-2l)(k+1-l)/6",
            "(6')": "M_n <= (C + L/2) sqrt(2n) + C^2/(2L) - C",
            "(7)": "REV_n <= (C + L/2 + pi/sqrt3) sqrt(2n) + C^2/(2L) - C = O(sqrt n)",
            "verdict": "REV_n = Theta(sqrt n); the 3/4 exponent (#7018) is not sharp",
        },
        "lean": "folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumRowTangentBound.lean",
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "n_exact_sweep": N_EXACT,
        "n_scan": N_SCAN,
        "bound_vs_rev_table": rows,
        "rate_scan": scan,
    }
    out = os.path.join(_COMPUTATIONS, "rev-sqrt-n-upper-bound.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
