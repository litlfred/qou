"""Operator-level Gell-Mann-Okubo for the weighted Jucys-Murphy sum. Exact over Q(q).

Companion to murphy_octet_probe.py, which takes traces over whole weight spaces (decuplet
and octet mixed). Here the octet is projected out and Lambda is separated from Sigma0:

* space (C^3)^{x3}, Jimbo braiding R (StrangeStrandOctet.jimbo) on strands (1,2), (2,3);
* M_w = sum_k D_k L_k, D_k = diagonal weight of the flavour on strand k,
  L1 = 1, L2 = s1^2, L3 = s2 s1^2 s2;
* P_oct = 1 - P_sym - P_anti, with P_sym ~ sum q^l(w) T_w and P_anti ~ sum (-1/q)^l(w) T_w
  (central idempotents of H_3 on this space; rank 16 = 8 x 2);
* isospin: the U_q(sl2) on the two flavours u, d with the coproduct that commutes with
  sigma_1, sigma_2 (checked), and its Casimir; the I-projector is the Casimir eigenprojector;
* "mass" of a state = tr(Q M_w) / tr(Q), Q = P_oct * P_I * (weight-space projector).
  Q commutes with every L_k, so tr(Q D L) = tr(Q L D): no ordering ambiguity in M_w.

Flavour order is an input. The U_q(sl2) on (u, d) with the simple coproduct only commutes
with R when u and d are adjacent in the order, so the orders run are u<d<s and s<u<d.
Measured data (PDG octet baryons) appear only in the final comparison lines, never upstream.

Usage: python3 octet_gmo_operator_probe.py   (about 5 min per order)
"""
import itertools
import sys

from sympy import (Integer, Matrix, Rational, diag, eye, factor, simplify, symbols,
                   zeros)
from sympy.matrices.expressions.kronecker import kronecker_product

q = symbols('q', positive=True)
wu, wd, ws = symbols('wu wd ws')
h = q - 1 / q
N = 27
WORDS = list(itertools.product(range(3), repeat=3))
IDX = {w: i for i, w in enumerate(WORDS)}


def r2(x, y):
    """Jimbo braiding entry (output x, input y) on C^3 (x) C^3, order = index order."""
    if y[0] == y[1]:
        return q if x == y else 0
    v = 1 if x == (y[1], y[0]) else 0
    if y[1] < y[0] and x == y:
        v += h
    return v


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = kronecker_product(out, m)
    return Matrix(out)


def normalise(p):
    p = p.applyfunc(simplify)
    p2 = (p * p).applyfunc(simplify)
    for a in range(N):
        for b in range(N):
            if p[a, b] != 0:
                return (p / simplify(p2[a, b] / p[a, b])).applyfunc(simplify)
    raise ValueError("zero projector")


def run(U, D, S):
    s1, s2 = zeros(N), zeros(N)
    for x in WORDS:
        for y in WORDS:
            if x[2] == y[2]:
                s1[IDX[x], IDX[y]] = r2((x[0], x[1]), (y[0], y[1]))
            if x[0] == y[0]:
                s2[IDX[x], IDX[y]] = r2((x[1], x[2]), (y[1], y[2]))
    one = eye(N)
    assert (s1 * s2 * s1 - s2 * s1 * s2).applyfunc(simplify) == zeros(N)
    L = [one, s1 * s1, s2 * s1 * s1 * s2]
    w = [None] * 3
    w[U], w[D], w[S] = wu, wd, ws
    M = zeros(N)
    for x in WORDS:
        j = IDX[x]
        for k in range(3):
            for i in range(N):
                M[j, i] += w[x[k]] * L[k][j, i]
    T = {0: [one], 1: [s1, s2], 2: [s1 * s2, s2 * s1], 3: [s1 * s2 * s1]}
    psym = normalise(sum((q ** l * t for l, ts in T.items() for t in ts), zeros(N)))
    panti = normalise(sum(((-1 / q) ** l * t for l, ts in T.items() for t in ts), zeros(N)))
    poct = (one - psym - panti).applyfunc(simplify)
    assert (poct * poct - poct).applyfunc(simplify) == zeros(N)
    E, F = zeros(3), zeros(3)
    E[U, D] = 1
    F[D, U] = 1
    kd = [Integer(1)] * 3
    kd[U], kd[D] = q, 1 / q
    K, Ki, I3 = diag(*kd), diag(*[Integer(1) / x for x in kd]), eye(3)
    EE = kron(E, K, K) + kron(I3, E, K) + kron(I3, I3, E)
    FF = kron(F, I3, I3) + kron(Ki, F, I3) + kron(Ki, Ki, F)
    for sg in (s1, s2):
        assert (EE * sg - sg * EE).applyfunc(simplify) == zeros(N), "coproduct does not commute"
    cas = (FF * EE + (q * kron(K, K, K) + kron(Ki, Ki, Ki) / q) / h ** 2).applyfunc(simplify)
    lam = lambda i2: (q ** (i2 + 1) + q ** (-(i2 + 1))) / h ** 2

    def wsp(ms):
        p = zeros(N)
        for x in WORDS:
            if sorted(x) == sorted(ms):
                p[IDX[x], IDX[x]] = 1
        return p

    def mass(ms, i2):
        Q = (poct * wsp(ms)).applyfunc(simplify)
        for o in [lam(j) for j in range(4) if j != i2]:
            Q = (Q * (cas - o * one) / (lam(i2) - o)).applyfunc(simplify)
        assert Q.subs(q, Rational(3, 2)).rank() == 2
        return simplify((Q * M).trace() / Q.trace())

    m = {'N': mass((U, U, D), 1), 'Sigma': mass((U, U, S), 2), 'Xi': mass((U, S, S), 1),
         'Lambda': mass((U, D, S), 0), 'Sigma0': mass((U, D, S), 2)}
    gmo = simplify(2 * (m['N'] + m['Xi']) - 3 * m['Lambda'] - m['Sigma'])
    return m, gmo


if __name__ == '__main__':
    q0 = Rational('1.1099785827513808')  # proton pin, evaluation only
    a, b = symbols('a b')
    for label, (U, D, S) in [('u<d<s', (0, 1, 2)), ('s<u<d', (1, 2, 0))]:
        m, gmo = run(U, D, S)
        print(f'== order {label}')
        print('  GMO at q=1 (general weights):', simplify(gmo.subs(q, 1)))
        iso = {wu: a, wd: a, ws: b}
        xn = simplify((m['Xi'] - m['N']).subs(iso))
        r = factor(simplify(gmo.subs(iso) / xn))
        print('  GMO / (Xi - N), isospin-symmetric weight:', r)
        print('    at q0:', r.subs(q, q0).evalf(12))
        for k in ('Sigma', 'Lambda'):
            rk = simplify((m[k] - m['N']).subs(iso) / xn)
            print(f'  ({k} - N)/(Xi - N): q=1 {rk.subs(q, 1)}, q0 {rk.subs(q, q0).evalf(10)}')
        print('  Sigma0 - Sigma+ :', factor(simplify(m['Sigma0'] - m['Sigma'])))
    mN, mS, mX, mL = (Rational(v) for v in ('938.92', '1193.15', '1318.29', '1115.68'))
    print('== comparison (PDG octet baryons, MeV, exact rationals):')
    print('  GMO/(Xi-N) =', ((2 * (mN + mX) - 3 * mL - mS) / (mX - mN)).evalf(4),
          ' (Sigma-N)/(Xi-N) =', ((mS - mN) / (mX - mN)).evalf(4),
          ' (Lambda-N)/(Xi-N) =', ((mL - mN) / (mX - mN)).evalf(4))
    sys.exit(0)
