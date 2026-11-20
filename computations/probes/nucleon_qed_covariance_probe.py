#!/usr/bin/env python3
"""Braid-covariant vs adjacent pairwise QED insertion on the nucleon weight spaces.

Companion to ``QOU/BraidsAndKnots/NucleonQEDCovariance.lean`` (T1-T6). Exact
symbolic algebra in ``sympy`` (field Q(q)); numerical evaluation at the proton
q0 in ``mpmath`` at 70 dps. No float64 arithmetic, no fitted parameter, no
selection: every number printed is either a Lean-stated closed form or the
value of a defined operator at q0. The adjacent-insertion figures from PR #8518
are reproduced for comparison only.

Run:  PYTHONPATH=tools/qou-substrate/python python3 computations/probes/nucleon_qed_covariance_probe.py
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 70
q = sp.symbols("q", positive=True)
qi = 1 / q
R = sp.Rational

A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, q - qi]])
A2 = sp.Matrix([[0, 1, 0], [1, q - qi, 0], [0, 0, q]])
B1, B2 = A2, A1
A2i = sp.simplify(A2.inv())
B2i = sp.simplify(B2.inv())
V3p = sp.simplify((A1 * A2i) ** 3)
V3n = sp.simplify((B1 * B2i) ** 3)
N = sp.Matrix(3, 3, lambda i, j: q ** (i + j - 3))
M = N - q * sp.eye(3)
P3 = sp.simplify(N / N.trace())
P21 = sp.eye(3) - P3
d = lambda *x: sp.diag(*[R(v) for v in x])
Q = {
    "12p": d("4/9", "-2/9", "-2/9"), "23p": d("-2/9", "-2/9", "4/9"), "13p": d("-2/9", "4/9", "-2/9"),
    "12n": d("-2/9", "-2/9", "1/9"), "23n": d("1/9", "-2/9", "-2/9"), "13n": d("-2/9", "1/9", "-2/9"),
}


def E(X):
    return (X * P3).trace() * P3 + (X * P21).trace() / 2 * P21


def coords(X):
    """(a, b) with X = a*1 + b*M (X must lie in the commutant)."""
    a, b = sp.symbols("a b")
    sol = sp.solve(list(X - a * sp.eye(3) - b * M), [a, b], dict=True)
    assert sol, "not in span{1, M}"
    return sp.factor(sol[0][a]), sp.factor(sol[0][b])


checks = []
# T1 sanity: M commutes, Q_adj does not
checks.append(("M in commutant", sp.simplify(M * A1 - A1 * M) == sp.zeros(3) and sp.simplify(M * A2 - A2 * M) == sp.zeros(3)))
Qadjp, Qadjn = Q["12p"] + Q["23p"], Q["12n"] + Q["23n"]
checks.append(("Q_adj(p) not covariant", sp.simplify(Qadjp * A1 - A1 * Qadjp) != sp.zeros(3)))
# T3
checks.append(("T3 tr(Qadj V3) = -tr(Q13 V3)", sp.simplify((Qadjp * V3p).trace() + (Q["13p"] * V3p).trace()) == 0))
# T6
QpairP = Q["12p"] + Q["23p"] + Q["13p"]
QpairN = Q["12n"] + Q["23n"] + Q["13n"]
checks.append(("E(Qpair_p) = 0", sp.simplify(E(QpairP)) == sp.zeros(3)))
checks.append(("E(Qpair_n) = -1/3", sp.simplify(E(QpairN) + R(1, 3) * sp.eye(3)) == sp.zeros(3)))
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
assert all(ok for _, ok in checks)

print("\n-- coordinates in span{1, M} --")
for lab, X in [("E(Q_pair p)", E(QpairP)), ("E(Q_pair n)", E(QpairN)),
               ("E(Q12+Q23 p)", E(Qadjp)), ("E(Q12+Q23 n)", E(Qadjn)),
               ("E(Q13 p)", E(Q["13p"])), ("E(Q13 n)", E(Q["13n"]))]:
    a, b = coords(sp.simplify(X))
    print(f"{lab:14s} a = {a}    b = {b}")

q0 = mp.mpf(__import__("qou_substrate.constants", fromlist=["q_at"]).q_at())


def ev(expr):
    return mp.mpf(sp.N(sp.together(expr).subs(q, sp.Rational(str(q0))), 80))


rows = {
    "(1/3) tr(V3)": V3p.trace() / 3,
    "tr N = q^-3+q^-1+q": N.trace(),
    "(1/3) tr((Q12+Q23)_p V3)  [#8518 conn p]": (Qadjp * V3p).trace() / 3,
    "(1/3) tr(Q13_p V3)  [dropped pair]": (Q["13p"] * V3p).trace() / 3,
    "(1/3) tr(E(Q_pair)_p V3)": (E(QpairP) * V3p).trace() / 3,
    "(1/3) tr(E(Q_pair)_n V3)": (E(QpairN) * V3n).trace() / 3,
    "(1/3) [tr(E(Q_pair)_n V3) - tr(E(Q_pair)_p V3)]": ((E(QpairN) * V3n).trace() - (E(QpairP) * V3p).trace()) / 3,
    "(1/3) tr(E(Q12+Q23)_p V3)  [comparison]": (E(Qadjp) * V3p).trace() / 3,
    "(1/3) tr(E(Q12+Q23)_n V3)  [comparison]": (E(Qadjn) * V3n).trace() / 3,
    "(1/3) [tr(E(Qadj)_n V3) - tr(E(Qadj)_p V3)]  [comparison]": ((E(Qadjn) * V3n).trace() - (E(Qadjp) * V3p).trace()) / 3,
    "(1/3) [tr(E(Qadj)_n V3) + (2/9) tr(V3) - tr(E(Qadj)_p V3)]  [#8518-style conn diff, comparison]":
        ((E(Qadjn) * V3n).trace() + R(2, 9) * V3n.trace() - (E(Qadjp) * V3p).trace()) / 3,
    "#8518 conn diff (n-p), recomputed": ((Qadjn * V3n).trace() + R(2, 9) * V3n.trace() - (Qadjp * V3p).trace()) / 3,
}
print(f"\n-- values at proton q0 = {mp.nstr(q0, 25)} (70 dps) --")
for k, v in rows.items():
    print(f"{mp.nstr(ev(sp.simplify(v)), 20):>28s}   {sp.factor(sp.simplify(v))}   {k}")
