#!/usr/bin/env python3
"""Does the corner-sl2 one-sidedness persist in a WEIGHTED form? (convention D)

Bean qou-wkcd, owner decision (a) 2026-11-15. Companion of corner_sl2_multiplicity_probe.py
and Lean QOU/QuarkState/ConventionDLineWeights.lean.

Convention D weights (prop:markov-trace-frobenius-selection):
    y_(n-k,k) = [n-2k+1]_q / [2]_q^n,   y_lambda = 0 for >= 3 rows.
In block lambda the q-line of sigma_1 has rank a_lambda = #SYT with 2 in row 1, and the
(-q^-1)-line has rank b_lambda = #SYT with 2 in row 2 (seminormal form; cited).
Trace weight of a line inside block lambda = y_lambda * rank.

Measured, per n:
  T_L = sum y a, T_R = sum y b                      (whole lines)
  S_L = sum over blocks with a >= 2 of y a          (the part carrying an sl2)
  S_R = sum over blocks with b >= 2 of y b
Exact in sympy (symbolic q), then mpmath at 70 dps at the proton q0. No float, no witness,
no free parameter.
"""
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools/qou-substrate/python"))
from qou_substrate.constants import Q_50_DIGIT_STR  # proton pin

mp.mp.dps = 70
q = sp.symbols("q", positive=True)
ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


def qint(m):
    return sp.simplify((q ** m - q ** (-m)) / (q - 1 / q))


def ranks_two_row(n, k):
    """(a, b) for lambda = (n-k, k): count SYT by the row of 2 (hook-length style count)."""
    from math import comb
    # number of SYT of (n-k,k): f = C(n,k) - C(n,k-1)
    def f(m, j):
        if j < 0 or j > m - j:
            return 0
        return comb(m, j) - (comb(m, j - 1) if j >= 1 else 0)
    # 1 in row 1 always. 2 in row 1: remove 1,2 from row 1 -> shape (n-k-2, k) on n-2
    # cells, but row-2 length k must be <= row-1 length n-k (standard), and the remaining
    # filling is an SYT of the skew shape; for two-row shapes this equals ballot counts:
    # a = #ballot sequences of length n-2 ending at (n-k-2, k) starting after "11".
    # Count directly by DP over lattice paths.
    def paths(steps, start, end):
        # start=(r1,r2), each step adds to r1 or r2 keeping r2 <= r1
        from functools import lru_cache

        @lru_cache(None)
        def go(r1, r2, left):
            if left == 0:
                return 1 if (r1, r2) == end else 0
            tot = 0
            tot += go(r1 + 1, r2, left - 1)
            if r2 + 1 <= r1:
                tot += go(r1, r2 + 1, left - 1)
            return tot
        return go(start[0], start[1], steps)
    a = paths(n - 2, (2, 0), (n - k, k)) if n - k >= 2 else 0
    b = paths(n - 2, (1, 1), (n - k, k)) if k >= 1 else 0
    assert a + b == f(n, k)
    return a, b


rows = []
for n in range(2, 17):
    TL = TR = SL = SR = 0
    for k in range(0, n // 2 + 1):
        y = qint(n - 2 * k + 1) / (q + 1 / q) ** n
        a, b = ranks_two_row(n, k)
        TL += y * a
        TR += y * b
        if a >= 2:
            SL += y * a
        if b >= 2:
            SR += y * b
    rows.append((n, sp.simplify(TL), sp.simplify(TR), SL, SR))

z = q ** 3 / (q ** 2 + 1)
three = q ** 2 + 1 + q ** -2
for n, TL, TR, SL, SR in rows:
    good = sp.simplify(TL - (z + 1 / q) / (q + 1 / q)) == 0 and sp.simplify(TR - (q - z) / (q + 1 / q)) == 0
    if not good:
        check(f"n={n}: T_L, T_R equal the Markov values (z+q^-1)/[2], (q-z)/[2]", False)
check("for n = 2..16: T_L = (z_D+q^-1)/[2] and T_R = (q-z_D)/[2] exactly (n-independent)", ok)
check("T_L / T_R = [3]_q symbolically", sp.simplify(rows[-1][1] / rows[-1][2] - three) == 0)

q0 = sp.Rational(Q_50_DIGIT_STR)


def num(e):
    return mp.mpf(sp.N(sp.sympify(e).subs(q, q0), 70))


print("\n n | S_L (sl2 part of L) | S_R (sl2 part of R) | S_L/S_R | [3]_q0")
three0 = num(three)
for n, TL, TR, SL, SR in rows:
    sl, sr = num(SL), num(SR)
    ratio = mp.nstr(sl / sr, 10) if sr != 0 else "inf (R has no D-kept sl2)"
    print(f"{n:2d} | {mp.nstr(sl, 10)} | {mp.nstr(sr, 10)} | {ratio} | {mp.nstr(three0, 10)}")

r4 = num(rows[2][4])
check("n=4: S_R = 0 (exclusive one-sidedness)", r4 == 0)
r5 = num(rows[3][4])
check("n=5: S_R > 0 (exclusivity lost)", r5 > 0)
last = rows[-1]
lr = num(last[3]) / num(last[4])
print(f"n=16: S_L/S_R = {mp.nstr(lr, 12)} vs [3]_q0 = {mp.nstr(three0, 12)}")
check("the weighted ratio approaches [3]_q0 (within 1 % at n=16)", abs(lr / three0 - 1) < mp.mpf("0.01"))
print("at q = 1: [3]_1 = 3, z_D = 1/2 -> T_L : T_R = 3 : 1 (bias present at the classical point)")
check("T_L/T_R at q=1 equals 3", sp.simplify((rows[-1][1] / rows[-1][2]).subs(q, 1) - 3) == 0)
print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
