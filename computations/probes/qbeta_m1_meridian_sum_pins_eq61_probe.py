#!/usr/bin/env python3
"""qbeta_m1_meridian_sum_pins_eq61_probe.py — bean qou-m1nz: the convention is pinned.

QUESTION (qou-m1nz). Why does no summation of the certified 4_1 index
(figure_eight_3d_index.py, GHHR arXiv:1604.02688 Ex 4.1) reproduce the GGM eq (61)
tower S^+_{s1 s1}(q) = 1 - 8q - 9q^2 + 18q^3 + 46q^4 + 90q^5 + 62q^6 + ...?

ANSWER. The earlier probe summed over the wrong cycle. GGM Conj. 4 / eq (S3Dx)
(a theorem for 4_1) reads S^+_{s1 s1}(x;q) = Ind^rot_K(0, x; q) = sum_e I_K(0,e)(q) x^e.
In the homology labelling I_T(x*mu + y*lam) that the certified gluing uses, the summed
charge e is the MERIDIAN label x, with the longitude label y = 0:

    S^+_{s1 s1}(1; q) = sum_{x in Z} I_T(x*mu)(q).

No Neumann-Zagier weight and no prefactor are needed. qou-m1nz's earlier sweep summed
y (the longitude) at x = 0, which gives 1 - 2q - 3q^2 + 4q^3 + ...

TWO INDEPENDENT SIDES, both exact integer q-series:
  (A) the index side: sum over x of the certified gluing, truncation raised to q^16;
  (B) the Stokes side: GGM eq (S41p),
        S^+(q) = 1/2 [[0,-1],[1,1]] W_{-1}(q) [[0,1],[1,0]] W_{-1}(q)^T [[0,-1],[1,2]],
      with W_m built from G^0_m, G^1_m (GGM eqs (gm), (Gm)) and E_1 = 1 - 4 sum q^n/(1-q^n).
      det W = 2 is checked as a sanity gate (GGM eq (det41)).

The two sides agree coefficient by coefficient through q^13. The Stokes side comes out
as -S^+_{11}. That is a global sign of the q^0 normalisation: GGM print S^+(0) = [[1,3],[0,1]],
and the formula as transcribed gives [[-1,-3],...]. It is recorded here, not tuned away.

Source: library/arxiv-2012.00062v3/source/files/GGM_peacock_20v4.tex, lines 1300-1505.
No measured or empirical value enters. Exact rational arithmetic only.
"""
from __future__ import annotations

import importlib.util
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
N = 14  # compare q^0 .. q^13
EQ61 = [1, -8, -9, 18, 46, 90, 62]  # printed, GGM eq (61)


# --------------------------------------------------------------------------- (A)
def index_side() -> list[int]:
    spec = importlib.util.spec_from_file_location(
        "fe3d", os.path.join(HERE, "figure_eight_3d_index.py"))
    fe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fe)
    fe.HI = 2 * (N + 3)  # Q = q^{1/2}; the module default (26) truncates at q^10
    tot = [0] * N
    for x in range(-14, 15):
        d = fe.index(x, 0, kmax=12)
        for j in range(N):
            tot[j] += d.get(2 * j, 0)
        if any(c and p % 2 for p, c in d.items()):
            raise AssertionError(f"half-integer q-power at x={x}")
    return tot


# --------------------------------------------------------------------------- (B)
P = N + 2


def mul(a, b):
    c = [F(0)] * P
    for i, x in enumerate(a):
        if x:
            for j in range(P - i):
                c[i + j] += x * b[j]
    return c


def inv(a):
    b = [F(0)] * P
    b[0] = 1 / a[0]
    for n in range(1, P):
        b[n] = -sum(a[k] * b[n - k] for k in range(1, n + 1)) / a[0]
    return b


def lin(*terms):
    out = [F(0)] * P
    for k, a in terms:
        out = [o + k * x for o, x in zip(out, a)]
    return out


ONE = [F(1)] + [F(0)] * (P - 1)


def mono(k):
    v = [F(0)] * P
    if k < P:
        v[k] = F(1)
    return v


def one_minus_qn(n):
    return lin((1, ONE), (-1, mono(n)))


E1 = lin((1, ONE), *[(-4, mul(mono(n), inv(one_minus_qn(n)))) for n in range(1, P)])


def G(m):
    g0 = [F(0)] * P
    g1 = [F(0)] * P
    poch = ONE
    S = [F(0)] * P
    for n in range(0, 2 * P):
        if n > 0:
            if n < P:
                poch = mul(poch, one_minus_qn(n))
                S = lin((1, S), (1, mul(lin((1, ONE), (1, mono(n))), inv(one_minus_qn(n)))))
            else:
                S = lin((1, S), (1, ONE))
        e = n * (n + 1) // 2 + m * n
        if e >= P:
            if n > 2:
                break
            continue
        term = lin(((-1) ** n, mul(mono(e), inv(mul(poch, poch)))))
        g0 = lin((1, g0), (1, term))
        g1 = lin((1, g1), (1, mul(term, lin((2 * m, ONE), (1, E1), (2, S)))))
    return g0, g1


def mm(A, B):
    return [[lin((1, mul(A[i][0], B[0][j])), (1, mul(A[i][1], B[1][j]))) for j in range(2)]
            for i in range(2)]


def const(M):
    return [[lin((x, ONE)) for x in row] for row in M]


def stokes_side() -> tuple[list[int], list[F]]:
    a0, a1 = G(-1)
    b0, b1 = G(0)
    W = [[a0, a1], [b0, b1]]
    WT = [[W[0][0], W[1][0]], [W[0][1], W[1][1]]]
    det = lin((1, mul(W[0][0], W[1][1])), (-1, mul(W[0][1], W[1][0])))
    S = mm(mm(mm(mm(const([[0, -1], [1, 1]]), W), const([[0, 1], [1, 0]])), WT),
           const([[0, -1], [1, 2]]))
    s11 = [F(1, 2) * c for c in S[0][0]]
    return [int(c) for c in s11[:N]], det[:N]


def main() -> int:
    ok = True
    idx = index_side()
    s11, det = stokes_side()
    gates = [
        ("det W_{-1} = 2 (GGM det41)", det[0] == 2 and all(c == 0 for c in det[1:])),
        ("index side reproduces printed eq (61)", idx[:7] == EQ61),
        ("Stokes side reproduces printed eq (61), up to global sign",
         [-c for c in s11[:7]] == EQ61),
        ("index side == -(Stokes side) through q^13", idx == [-c for c in s11]),
    ]
    print("index  sum_x I_T(x mu):", idx)
    print("Stokes -S^+_11(q)     :", [-c for c in s11])
    for name, g in gates:
        print(f"  [{'PASS' if g else 'FAIL'}] {name}")
        ok = ok and g
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
