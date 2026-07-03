#!/usr/bin/env python3
"""Sympy pre-verification for the Lean telescope assembly (bean udmw).

Verifies, exactly, every identity the Lean assembly transcribes to
discharge the general-N annihilation sorry in
QOU/BraidKnot/AJFigureEight.lean — the DIVISION-FREE reformulation of the
qZeilberger certificate telescope (valid at roots of unity: divisions only
by powers of q and x = q^N):

  anchors at k = m+2:  A = risingA(x, m),  B0 = risingB(x, m+2),
  w := q^(m+1)  (so q^k = q*w, q^(m+2) = q*w).

  [K3]  the master local identity in (q, x, w) after eliminating B1, B2
        through the exact factor matches (a2 supplies (q^2 x - 1),
        a1 supplies (xq-1)^2, the A-shift supplies (qx-1)):
          T2 + T1 + T0 = W(m+3)/(A*B0/Dprod) - W(m+2)/(A*B0/Dprod)
  [W0]  backward-recursion boundary: W(0) = -b(x)  (with W(1) := W(2) -
        LHS_local(1), W(0) := W(1) - LHS_local(0))
  [N0]  the N = 0 annihilation instance (x = 1)
  [SIM] full numeric simulation: for N = 1..6 at random rational q, the
        Lean-side Wfun telescope reproduces the annihilation exactly.

Run this BEFORE trusting the Lean transcription; each identity is printed
PASS/FAIL.  Audit-only; no witness (pre-flight for a Lean proof).
"""
from __future__ import annotations

import sys
from fractions import Fraction

import sympy as sp

q, x, w = sp.symbols("q x w")

# operator (verified witness aj-figure-eight-operator-construct-verify)
a0 = (x - 1) * (x**2 * q**3 - 1) / x**6
a1 = -((x * q - 1) ** 2 * (x * q + 1)
       * (x**4 * q**4 - x**3 * q**3 - x**2 * q**3 - x**2 * q - x * q + 1)) \
     / (x**8 * q**2)
a2 = (x * q**2 - 1) * (x**2 * q - 1) / x**6
b = (x * q + 1) * (x**2 * q - 1) * (x**2 * q**3 - 1) / (x**7 * q)
C = (q * x + 1) * (q * x**2 - 1) * (q**3 * x**2 - 1)

ok_all = True


def check(name, expr):
    global ok_all
    val = sp.simplify(sp.together(expr))
    ok = val == 0
    ok_all &= ok
    print(f"  [{name}] {'PASS' if ok else 'FAIL: ' + str(val)}")
    return ok


print("\n== udmw telescope assembly pre-verification ==\n")

# ---- [K3] master local identity (k = m+2), B1/B2 eliminated -------------
# per-term reductions (all divided by the common A*B0/Dprod(m+2)):
T2 = (x**2 * q - 1) * (x - 1) * (x * q**2 * w - 1) * (x * q**3 * w - 1) / (x**6 * q)
P4 = x**4 * q**4 - x**3 * q**3 - x**2 * q**3 - x**2 * q - x * q + 1
T1 = -(x * q - 1) * (x * q + 1) * P4 * (x - 1) * (x - w) * (x * q**2 * w - 1) \
     / (x**8 * q**2)
T0 = (x - 1) * (x**2 * q**3 - 1) / x**6 * (x - w) * (x - q * w)
RHS = -C * (1 - x) * (1 - q * x) * (
    (x - w) * (x * q**2 * w - 1) / x**8 - q * w / x**7) / q**2
check("K3 master local identity", T2 + T1 + T0 - RHS)

# ---- [W0] boundary: backward recursion hits -b ---------------------------
# W(2): m=0 -> A(0)=1, B(2)=(xq-1)(xq^2-1), q^k=q^2, Dprod(2)=x^2 q^3
W2 = -C * (1 - x) * (1 - q * x) * q**2 * (x * q - 1) * (x * q**2 - 1) \
     / (q**2 * x**7 * x**2 * q**3)
F_N_1 = (x - q) * (x * q - 1) / (x * q)
F_N1_1 = q * (x - 1) * (q**2 * x - 1) / (q**2 * x)
F_N2_1 = q * (q * x - 1) * (q**3 * x - 1) / (q**3 * x)
L1 = a2 * F_N2_1 + a1 * F_N1_1 + a0 * F_N_1
L0 = a2 + a1 + a0
W1 = sp.cancel(sp.together(W2 - L1))
W0 = sp.cancel(sp.together(W1 - L0))
check("W0 boundary = -b", W0 + b)
print(f"      W1 (Lean transcription) = {sp.factor(W1)}")

# ---- [N0] the N = 0 case --------------------------------------------------
J2 = q**2 + q**-2 - q - q**-1 + 1
check("N0 annihilation (x=1)",
      (a1.subs(x, 1) * 1 + a2.subs(x, 1) * J2 + a0.subs(x, 1) * 0
       - b.subs(x, 1)))

# ---- [SIM] full Wfun telescope simulation, N = 1..6 ----------------------
def risingA(qv, xv, k):
    out = Fraction(1)
    for j in range(k):
        out *= xv - qv ** (j + 1)
    return out


def risingB(qv, xv, k):
    out = Fraction(1)
    for j in range(k):
        out *= xv * qv ** (j + 1) - 1
    return out


def newton(qv, xv, k):
    # ladder at Lambda = x + 1/x on nodes lam_j
    out = Fraction(1)
    for j in range(1, k + 1):
        out *= xv + 1 / xv - (qv**j + 1 / qv**j)
    return out


def frac(e, subs):
    v = sp.nsimplify(sp.cancel(e.subs(subs)))
    return Fraction(int(sp.numer(v)), int(sp.denom(v)))


qv = Fraction(7, 5)
sim_ok = True
for N in range(1, 7):
    xv = qv**N
    subs = {q: sp.Rational(7, 5), x: sp.Rational(xv.numerator, xv.denominator)}
    a0v, a1v, a2v, bv = (frac(e, subs) for e in (a0, a1, a2, b))
    Cv = frac(C, subs)
    W1v, W0v = frac(W1, subs), frac(W0, subs)

    def Wfun(k):
        if k == 0:
            return W0v
        if k == 1:
            return W1v
        m = k - 2
        Dprod = Fraction(1)
        for j in range(k):
            Dprod *= xv * qv ** (j + 1)
        return -Cv * (1 - xv) * (1 - qv * xv) * qv**k \
            * risingA(qv, xv, m) * risingB(qv, xv, k) \
            / (qv**2 * xv**7 * Dprod)

    # local identities for every k < N+2
    loc_ok = True
    for k in range(N + 2):
        lhs = (a2v * newton(qv, qv ** (N + 2), k)
               + a1v * newton(qv, qv ** (N + 1), k)
               + a0v * newton(qv, xv, k))
        loc_ok &= (lhs == Wfun(k + 1) - Wfun(k))
    top_ok = (Wfun(N + 2) == 0)
    # full annihilation
    def J(M):
        return sum(newton(qv, qv**M, k) for k in range(M))
    ann_ok = (a2v * J(N + 2) + a1v * J(N + 1) + a0v * J(N) == bv)
    sim_ok &= loc_ok and top_ok and ann_ok
    print(f"  [SIM N={N}] local:{'PASS' if loc_ok else 'FAIL'} "
          f"top-zero:{'PASS' if top_ok else 'FAIL'} "
          f"annihilation:{'PASS' if ann_ok else 'FAIL'}")

ok_all &= sim_ok
print(f"\n  OVERALL: {'ALL PASS — safe to transcribe' if ok_all else 'FAILURES — fix before Lean'}")
sys.exit(0 if ok_all else 1)
