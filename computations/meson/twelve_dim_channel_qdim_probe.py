#!/usr/bin/env python3
"""Exact classification of sl2 x sl3 isotypes of classical dimension 12 and their q-dimensions.

Bean qou-mk34 (compute-accuracy C5, option 2: is the V2 (x) Sym^2_q W3* channel forced?).
Mathematics only: exact Laurent polynomials in q (sympy), no measured number, no float.

An isotype is V_n (x) W_(a,b): V_n the n-dimensional U_q(sl2) irrep (dim_q = [n]),
W_(a,b) the U_q(sl3) irrep of highest weight (a,b) (dim_q = [a+1][b+1][a+b+2]/[2]).
Balanced q-integers [n] = (q^n - q^-n)/(q - q^-1).

Checks:
 1. classical dimension 12 forces (n,(a,b)) in {(2,(2,0)),(2,(0,2)),(4,(1,0)),(4,(0,1)),(12,(0,0))}.
 2. q-dims: the four with nontrivial sl3 factor all equal [3][4]; the trivial one is [12] != [3][4].
 3. first tensor degree k at which each isotype occurs in F^{(x)k}, F = V2 (+) W3* (Pieri).
"""
import sys
import sympy as sp

q = sp.symbols("q")


def qint(n):
    return sp.cancel((q**n - q**-n) / (q - q**-1))


def dim_sl3(a, b):
    return (a + 1) * (b + 1) * (a + b + 2) // 2


def qdim_sl3(a, b):
    return sp.cancel(qint(a + 1) * qint(b + 1) * qint(a + b + 2) / qint(2))


TARGET = sp.expand(qint(3) * qint(4))


def classical_twelve():
    out = []
    for n in range(1, 13):
        if 12 % n:
            continue
        m = 12 // n
        for a in range(0, 13):
            for b in range(0, 13):
                if dim_sl3(a, b) == m:
                    out.append((n, (a, b)))
    return out


def first_degree(kmax=12):
    """Isotypes of F^{(x)k}: sl2 part from V2^{(x)i}, sl3 part from W3*^{(x)(k-i)}."""
    sl2 = {0: {1}}
    for i in range(1, kmax + 1):
        sl2[i] = {m for n in sl2[i - 1] for m in (n - 1, n + 1) if m >= 1}
    sl3 = {0: {(0, 0)}}
    for j in range(1, kmax + 1):
        nxt = set()
        for a, b in sl3[j - 1]:  # tensor with W3* = (0,1)
            nxt.add((a, b + 1))
            if b >= 1:
                nxt.add((a + 1, b - 1))
            if a >= 1:
                nxt.add((a - 1, b))
        sl3[j] = nxt
    first = {}
    for k in range(0, kmax + 1):
        for i in range(0, k + 1):
            for n in sl2[i]:
                for ab in sl3[k - i]:
                    first.setdefault((n, ab), k)
    return first


def main():
    ok = True
    iso = classical_twelve()
    expected = [(2, (0, 2)), (2, (2, 0)), (4, (0, 1)), (4, (1, 0)), (12, (0, 0))]
    c1 = sorted(iso) == sorted(expected)
    print("1. classical-dim-12 isotypes:", sorted(iso), "PASS" if c1 else "FAIL")
    ok &= c1
    first = first_degree()
    for n, (a, b) in sorted(iso):
        qd = sp.expand(sp.cancel(qint(n) * qdim_sl3(a, b)))
        eq = sp.simplify(qd - TARGET) == 0
        print(f"2. V_{n} x W_{(a, b)}: dim_q == [3][4]? {eq}; first in F^(x)k at k = {first.get((n, (a, b)))}")
        if (a, b) != (0, 0):
            ok &= eq
        else:
            ok &= (not eq) and sp.simplify(qd - qint(12)) == 0
    print("ALL PASS" if ok else "FAILURES")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
