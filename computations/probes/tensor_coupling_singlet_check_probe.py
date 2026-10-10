#!/usr/bin/env python3
"""
Probe — the two-nucleon tensor coupling acts as the scalar 3(1-|n|^2) on the spin
singlet, and is therefore 0 on the unit sphere.

Exact-arithmetic (sympy, symbolic; NO float64) companion to
    folio/quantum-observable-universe/lean/QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean
and docs/audits/2026-09-03-tensor-coupling-cannot-unbind-singlet.md (bean qou-s42j,
target qou-vbyi route 1).

Checks, all exact:
  1. the explicit 4x4 two-spin matrices written in the Lean file equal the
     Kronecker construction sigma_a (x) 1 and 1 (x) sigma_a  (transcription guard);
  2. sigma1.sigma2 |s> = -3 |s>;
  3. (sigma1.n)(sigma2.n) |s> = -|n|^2 |s>  for symbolic n;
  4. S12(n)|s> = 3(1-|n|^2)|s>, hence 0 when |n|^2 = 1;
  5. sigma2^a |s> = -sigma1^a |s> for a = x,y,z (the singlet is an eigenvector of
     each generator pair — no off-diagonal element out of S = 0).

Exit 0 iff every check passes. Basis order |uu>,|ud>,|du>,|dd>, particle 1 first.
"""
import sys
import sympy as sp

I = sp.I
n1, n2, n3 = sp.symbols('n1 n2 n3', real=True)

sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
E = sp.eye(2)
K = lambda A, B: sp.kronecker_product(A, B)
s1x, s1y, s1z = K(sx, E), K(sy, E), K(sz, E)
s2x, s2y, s2z = K(E, sx), K(E, sy), K(E, sz)

# the explicit 4x4 forms as written in the Lean file
L = dict(
    s1x=sp.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]),
    s2x=sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]),
    s1z=sp.diag(1,1,-1,-1),
    s2z=sp.diag(1,-1,1,-1),
    s1y=sp.Matrix([[0,0,-I,0],[0,0,0,-I],[I,0,0,0],[0,I,0,0]]),
    s2y=sp.Matrix([[0,-I,0,0],[I,0,0,0],[0,0,0,-I],[0,0,I,0]]),
)
KR = dict(s1x=s1x, s1y=s1y, s1z=s1z, s2x=s2x, s2y=s2y, s2z=s2z)

checks = []
def check(name, cond):
    checks.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")

for k in L:
    check(f"explicit {k} == kronecker", L[k] == KR[k])

singlet = sp.Matrix([0, 1, -1, 0])
dot = s1x*s2x + s1y*s2y + s1z*s2z
nd1 = n1*s1x + n2*s1y + n3*s1z
nd2 = n1*s2x + n2*s2y + n3*s2z
S12 = 3*(nd1*nd2) - dot
nsq = n1**2 + n2**2 + n3**2

check("sigma1.sigma2 |s> = -3|s>", sp.simplify(dot*singlet + 3*singlet) == sp.zeros(4, 1))
check("(s1.n)(s2.n)|s> = -|n|^2 |s>", sp.simplify((nd1*nd2)*singlet + nsq*singlet) == sp.zeros(4, 1))
check("S12(n)|s> = 3(1-|n|^2)|s>", sp.simplify(S12*singlet - 3*(1-nsq)*singlet) == sp.zeros(4, 1))
check("S12(n)|s> = 0 on |n|^2=1", sp.simplify((S12*singlet).subs(n3**2, 1-n1**2-n2**2)) == sp.zeros(4, 1))
for a, b, nm in [(s1x, s2x, 'x'), (s1y, s2y, 'y'), (s1z, s2z, 'z')]:
    check(f"sigma2_{nm}|s> = -sigma1_{nm}|s>", sp.simplify(b*singlet + a*singlet) == sp.zeros(4, 1))

npass = sum(1 for _, ok in checks if ok)
print(f"\n{npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
