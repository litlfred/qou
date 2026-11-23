#!/usr/bin/env python3
"""Rigorous existence of an exact three-photon factorisation of the electron s0 s1 s0.

Photon (owner ruling 2026-11-20): gamma = 1 + phi0*s0 + phi1*s1 + phi01*s0*s1^{-1}.

Setting as electron_three_photon_probe.py: q = 11/10 (sample value of the formal variable,
not an anchor), gamma3 = gamma(3/10, -7/10, 9/20), lam = 1; six polynomial equations
(2-dim block, trivial and sign characters) in the six weights of gamma1, gamma2.

Method: Krawczyk interval test (mpmath interval arithmetic, outward rounding). For a box X
around the Newton point x~ and Y ~ J(x~)^{-1}, K(X) = x~ - Y F(x~) + (I - Y J(X))(X - x~).
If K(X) lies in the interior of X, F has a unique zero in X (Krawczyk 1969; Moore). This
turns the numerical solution into a computer-assisted existence proof of an exact (real,
algebraic) solution. No float arithmetic; equations built exactly in sympy over Q.
"""
import json, pathlib
import sympy as sp
import mpmath as mp
mp.mp.dps = 60
qq = sp.Rational(11, 10)
S0 = sp.Matrix([[qq, 0], [1, -1/qq]]); S1 = sp.Matrix([[-1/qq, 1], [0, qq]])
S1i = sp.Matrix([[-qq, 1], [0, 1/qq]]); C = S0*S1i; I2 = sp.eye(2)
M = lambda a, b, c: I2 + a*S0 + b*S1 + c*C
tr = lambda a, b, c: 1 + qq*(a + b) + c
sg = lambda a, b, c: 1 - (a + b)/qq + c
E = S0*S1*S0
g3 = (sp.Rational(3, 10), sp.Rational(-7, 10), sp.Rational(9, 20))
X = sp.symbols('x0:6')
P = M(*X[0:3])*M(*X[3:6])*M(*g3)
F = [sp.expand(P[i, j] - E[i, j]) for i in range(2) for j in range(2)]
F += [sp.expand(tr(*X[0:3])*tr(*X[3:6])*tr(*g3) - qq**3),
      sp.expand(sg(*X[0:3])*sg(*X[3:6])*sg(*g3) + 1/qq**3)]
J = sp.Matrix(F).jacobian(X)

def ev(expr, vals, iv=False):
    """Evaluate a polynomial with rational coefficients; interval-safe."""
    ctx = mp.iv if iv else mp
    tot = ctx.mpf(0)
    for mon, co in sp.Poly(expr, *X).terms():
        t = ctx.mpf(co.p)/co.q
        for v, e in zip(vals, mon):
            if e: t = t*v**e
        tot += t
    return tot

seed = [mp.mpf(s) for s in ("-45.9720308947", "35.8133528577", "10.4776605468",
                            "1.19719151778", "0.976727560112", "0.956289957858")]
x = mp.findroot(lambda *v: [ev(f, v) for f in F], seed, tol=mp.mpf(10)**-55)
x = [x[i] for i in range(6)]
Jx = mp.matrix([[ev(J[i, j], x) for j in range(6)] for i in range(6)])
Y = mp.inverse(Jx)
mp.iv.dps = 60
r = mp.mpf(10)**-20
xi = [mp.iv.mpf(str(v)) for v in x]
Xbox = [mp.iv.mpf([v - r, v + r]) for v in x]
Fx = [ev(f, xi, iv=True) for f in F]
JX = [[ev(J[i, j], Xbox, iv=True) for j in range(6)] for i in range(6)]
Yi = [[mp.iv.mpf(str(Y[i, j])) for j in range(6)] for i in range(6)]
K = []
for i in range(6):
    s = xi[i] - sum(Yi[i][k]*Fx[k] for k in range(6))
    for j in range(6):
        m = (1 if i == j else 0) - sum(Yi[i][k]*JX[k][j] for k in range(6))
        s += m*(Xbox[j] - xi[j])
    K.append(s)
inside = all(K[i].a > Xbox[i].a and K[i].b < Xbox[i].b for i in range(6))
out = {
    'claim': 'gamma1*gamma2*gamma(3/10,-7/10,9/20) = s0 s1 s0 has a unique exact solution in the box',
    'q_sample': '11/10 (formal variable sample, not an anchor)',
    'box_radius': '1e-20',
    'center': [mp.nstr(v, 30) for v in x],
    'K_inside_box': inside,
    'K_width_max': mp.nstr(max(K[i].delta.b for i in range(6)), 5),
    'method': 'Krawczyk interval test, mpmath iv (outward rounding)',
}
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_name('electron_three_photon_krawczyk.json').write_text(json.dumps(out, indent=1) + '\n')
assert inside
