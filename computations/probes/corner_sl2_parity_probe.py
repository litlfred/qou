#!/usr/bin/env python3
"""Does the corner-sl2 L/R asymmetry ALTERNATE with n (or with a sign)?

Bean qou-wkcj. Owner question (relayed 2026-11-15): "corner probe -> alternating on sign?"
Companion of corner_sl2_multiplicity_probe.py / corner_sl2_weighted_persistence_probe.py.

Exact counts only, no fitting, no free parameter. Three checks:
 1. Exclusivity by parity: for n = 4..16, the convention-D-kept sl2 carriers in the left
    (q-line of sigma_1) and right ((-q^-1)-line) corners. Exclusive = right has none.
 2. Sign character / transpose lambda <-> lambda': ranks a <-> b swap; D weight of lambda'.
    Signed differences of the weighted ratio S_L/S_R and of its deviation from [3]_q0.
 3. Root relabel q -> -q^-1: the Markov trace at z_D(-q^-1) weighs the two lines in the
    swapped ratio 1 : [3]_q (symbolic), and at n = 3 it kills (3) instead of (1^3).

Ranks per block (Young seminormal form; cited): a_lambda = #SYT with 2 in row 1,
b_lambda = #SYT with 2 in row 2. D weights: y_(n-k,k) = [n-2k+1]_q/[2]_q^n, 0 for >= 3 rows.
sympy exact, mpmath 70 dps at the proton q0. No witness.
"""
import sys
from functools import lru_cache
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


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def ranks(lam):
    """(a, b): SYT counts of shape lam with 2 in row 1 / row 2 (lattice-word DP)."""
    lam = tuple(lam)

    @lru_cache(None)
    def count(filled):
        if filled == lam:
            return 1
        tot = 0
        for i in range(len(lam)):
            if filled[i] < lam[i] and (i == 0 or filled[i - 1] > filled[i]):
                f = list(filled); f[i] += 1
                tot += count(tuple(f))
        return tot

    z = [0] * len(lam)
    a = b = 0
    if len(lam) >= 1 and lam[0] >= 2:
        f = z[:]; f[0] = 2
        a = count(tuple(f))
    if len(lam) >= 2:
        f = z[:]; f[0] = 1; f[1] = 1
        b = count(tuple(f))
    return a, b


def transpose(lam):
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0]))


def qint(m):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def yD(lam, n):
    if len(lam) > 2:
        return sp.Integer(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(n - 2 * k + 1) / (q + 1 / q) ** n


q0 = sp.Rational(Q_50_DIGIT_STR)


def num(e):
    return mp.mpf(sp.N(sp.sympify(e).subs(q, q0), 70))


# ---- 1. exclusivity by parity ---------------------------------------------------------
print("1. D-kept sl2 carriers (rank >= 2 AND <= 2 rows)")
print(" n | n mod 4 | left (a>=2)                     | right (b>=2)          | exclusive?")
excl = {}
rows = {}
for n in range(4, 17):
    L, R, SL, SR = [], [], 0, 0
    for lam in partitions(n):
        a, b = ranks(lam)
        # transpose check: a(lam') = b(lam), b(lam') = a(lam)
        at, bt = ranks(transpose(lam))
        if not (at == b and bt == a):
            check(f"transpose swaps ranks at {lam}", False)
        y = yD(lam, n)
        if len(lam) <= 2:
            if a >= 2:
                L.append(lam); SL += y * a
            if b >= 2:
                R.append(lam); SR += y * b
    excl[n] = (len(R) == 0)
    rows[n] = (SL, SR)
    print(f"{n:2d} | {n % 4} | {L} | {R} | {'YES' if excl[n] else 'no'}")
check("transpose lambda <-> lambda' swaps the two line ranks (a <-> b) for all lambda, n <= 16", ok)
check("left-only exclusivity occurs at n = 4 ONLY (not at any other n in 4..16)",
      [n for n, e in excl.items() if e] == [4])

# ---- 2. ratio sequence: signed differences ---------------------------------------------
three0 = num(q ** 2 + 1 + q ** -2)
print("\n2. weighted ratio r_n = S_L/S_R, its increments, and deviation from [3]_q0 =",
      mp.nstr(three0, 12))
prev = None
incs, devs = [], []
for n in range(5, 17):
    sl, sr = num(rows[n][0]), num(rows[n][1])
    r = sl / sr
    d = r - three0
    inc = (r - prev) if prev is not None else None
    devs.append(d)
    if inc is not None:
        incs.append(inc)
    print(f"  n={n:2d}  r={mp.nstr(r, 10)}  dev={mp.nstr(d, 6)}  "
          f"inc={'—' if inc is None else mp.nstr(inc, 6)}  (S_L-S_R)={mp.nstr(sl - sr, 8)}")
    prev = r
check("increments r_{n+1} - r_n are all negative (monotone decrease, no alternation)",
      all(x < 0 for x in incs))
check("deviations r_n - [3]_q0 are all positive (approach from above, no sign flip)",
      all(x > 0 for x in devs))
diffs = [num(rows[n][0] - rows[n][1]) for n in range(4, 17)]
check("(S_L - S_R) increases monotonically with n (no alternation)",
      all(diffs[i + 1] > diffs[i] for i in range(len(diffs) - 1)))

# D weight of transpose: the transpose of (n-k, k) has n-k rows, so D kills it unless
# n-k <= 2 (i.e. the shape has at most two columns: only (2,2) and (2,1,..) cases).
bad = [(n, k) for n in range(4, 17) for k in range(0, n // 2 + 1)
       if (yD(transpose((n - k, k) if k else (n,)), n) == 0) != (n - k >= 3)]
check("for n >= 4, D kills the transpose of a two-row shape exactly when it has >= 3 columns "
      "(the only kept transposes are two-column shapes, e.g. (2,2) at n=4)", bad == [])

# ---- 3. root relabel q -> -q^-1 --------------------------------------------------------
zD = q ** 3 / (q ** 2 + 1)
zr = sp.simplify(zD.subs(q, -1 / q))
TLr = sp.simplify((zr + 1 / q) / (q + 1 / q))
TRr = sp.simplify((q - zr) / (q + 1 / q))
check("at z_D(-q^-1): tau(P_+) : tau(P_-) = 1 : [3]_q (the bias flips side, same size)",
      sp.simplify(TRr / TLr - (q ** 2 + 1 + q ** -2)) == 0)
y3, y21, y111 = sp.symbols("y3 y21 y111")
sol = sp.solve([sp.Eq(y3 + 2 * y21 + y111, 1),
                sp.Eq(q * y3 + (q - 1 / q) * y21 - y111 / q, zr),
                sp.Eq(q ** 2 * y3 - y21 + y111 / q ** 2, zr ** 2)], [y3, y21, y111], dict=True)[0]
check("at n=3, z_D(-q^-1) kills (3) [all-q block] and keeps (1^3): y_(3) = 0",
      sp.simplify(sol[y3]) == 0 and sp.simplify(sol[y111]) != 0)
print("  relabelled weights n=3:", {str(k): sp.factor(v) for k, v in sol.items()})

print("\nVERDICT: monotone, not alternating. Exclusivity is n=4 only; the weighted ratio")
print("decreases monotonically to [3]_q0 from above; the only sign flip is the global")
print("L<->R swap under the root relabel (or transpose), which is the one bit.")
print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
