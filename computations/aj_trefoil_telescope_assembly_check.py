#!/usr/bin/env python3
"""Sympy pre-verification for the trefoil annihilation Lean assembly
(beans 6q9g + rz8b).

Unlike 4_1 (order 2, genuine qZeilberger certificate), the trefoil
annihilator is order 1 and the Rosso-Jones tower extends by a SINGLE term
per color, so no creative-telescoping certificate is needed.  With

  n = N-1,  v = w^2,  q = w^4,  x = q^N,
  P(n) = sum_{j=0..n} (-1)^j w^{6j(j+1)} [2j+1]_v,
  J(N) = (-1)^n w^{-6n(n+2)} P(n) / [N]_v          (T_j^3 rearranged),

the annihilation  a1(q,x) J(N+1) + a0(q,x) J(N) = b(q,x)  splits into two
2-variable rational identities in (v, y = v^N)  (all quadratic-in-n
w-exponents cancel in the ratios; w^{6(n+1)(n+3)} = w^{6n(n+2)} w^{6(2n+3)}):

  [C1]  the P(n)-coefficients cancel:
        a1 (-1)^{n+1} w^{-6(n+1)(n+3)}/[N+1] + a0 (-1)^n w^{-6n(n+2)}/[N] = 0
        <=>  a0/a1 = y^{-6} v^{-3} [N]/[N+1]
  [C2]  the single new term supplies the inhomogeneous part:
        a1 w^{-6(n+1)} [2N+1]/[N+1] ... = b
        <=>  a1 y^{-3} [2N+1]_v / [N+1]_v = b

plus [J-form]: the rearrangement J(N) = (-1)^n w^{-6n(n+2)} P(n)/[N]_v
matches the Lean `coloredJonesTrefoil` definition (checked numerically for
N = 1..10 at a random rational w), and [N0]: the N = 0 instance (where the
Lean tower gives J(0) = 0 by division-by-zero convention and a0(x=1) = 0).

Everything printed PASS/FAIL; run before trusting the Lean transcription.
Audit-only; no witness (pre-flight for a Lean proof).
"""
from __future__ import annotations

import sys
from fractions import Fraction

import sympy as sp

v, y = sp.symbols("v y")  # v = w^2, y = v^N

# operator in (q, x) = (v^2, y^2)
q_ = v**2
x_ = y**2
a0 = -(x_ - 1) / x_**5
a1 = -(q_ * (x_ * q_ - 1)) / x_**2
b = -(q_ * (x_**2 * q_ - 1)) / x_**4

qN = (y - 1 / y) / (v - 1 / v)            # [N]_v
qN1 = (v * y - 1 / (v * y)) / (v - 1 / v)  # [N+1]_v
q2N1 = (v * y**2 - 1 / (v * y**2)) / (v - 1 / v)  # [2N+1]_v

ok_all = True


def check(name, expr):
    global ok_all
    val = sp.expand(sp.fraction(sp.together(expr))[0])
    ok = val == 0
    ok_all &= ok
    print(f"  [{name}] {'PASS' if ok else 'FAIL: ' + str(val)}")
    return ok


print("\n== trefoil annihilation pre-verification ==\n")

# [C1] a0/a1 == y^{-6} v^{-3} [N]/[N+1]
check("C1 P-coefficient cancellation",
      a0 / a1 - qN / (y**6 * v**3 * qN1))

# [C2] a1 * y^{-3} * [2N+1]/[N+1] == b
check("C2 boundary term", a1 * q2N1 / (y**3 * qN1) - b)

# [N0] N = 0: a0(x=1) = 0 and a1(q,1)*J(1) = b(q,1) with J(1) = 1
check("N0 instance", (a1.subs(y, 1) * 1 - b.subs(y, 1)))

# [J-form + SIM] full numeric simulation N = 1..10, random rational w
w_ = Fraction(9, 7)


def qint_num(vv, k):
    return (vv**k - vv**-k) / (vv - vv**-1) if k > 0 else Fraction(0)


def J_lean(N):
    """Lean coloredJonesTrefoil at rational w (exact Fractions)."""
    n = N - 1
    vv = w_**2
    tot = Fraction(0)
    for j in range(n + 1):
        Tj = Fraction(-1) ** ((n - j) % 2) * w_ ** (2 * j * (j + 1) - n * (n + 2))
        tot += Tj**3 * qint_num(vv, 2 * j + 1)
    return w_ ** (-3 * n * (n + 2)) * tot / qint_num(vv, N)


def J_P(N):
    """P(n)-form: (-1)^n w^{-6n(n+2)} P(n)/[N]."""
    n = N - 1
    vv = w_**2
    P = sum(Fraction(-1) ** (j % 2) * w_ ** (6 * j * (j + 1))
            * qint_num(vv, 2 * j + 1) for j in range(n + 1))
    return Fraction(-1) ** (n % 2) * w_ ** (-6 * n * (n + 2)) * P / qint_num(vv, N)


sim_ok = True
qv = w_**4
for N in range(1, 11):
    xv = qv**N
    a0v = -(xv - 1) / xv**5
    a1v = -(qv * (xv * qv - 1)) / xv**2
    bv = -(qv * (xv**2 * qv - 1)) / xv**4
    form_ok = (J_lean(N) == J_P(N))
    ann_ok = (a1v * J_lean(N + 1) + a0v * J_lean(N) == bv)
    sim_ok &= form_ok and ann_ok
    if not (form_ok and ann_ok):
        print(f"  [SIM N={N}] J-form:{form_ok} annihilation:{ann_ok}  FAIL")
ok_all &= sim_ok
print(f"  [SIM N=1..10] J-form + annihilation at w = 9/7: "
      f"{'PASS' if sim_ok else 'FAIL'}")

# [B/C cores] root-of-unity evaluation lemmas (numeric, 40 dps): at the
# degenerate colors the operator's own zero coefficients (a0 at x=1, a1 at
# xq=1) mask the Lean division-by-zero junk values, and the surviving
# term needs J = 1 exactly:
#   [B]  (w^4)^N = 1, w^4 != 1   =>  J(N+1) = 1
#   [C]  (w^4)^(N+1) = 1, w^4 != 1  =>  J(N) = 1
# These are the two cited cores of the Lean case split (they are the
# root-of-unity periodicity of the Rosso-Jones sum).
import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()


def qint_mp(vv, k):
    den = vv - 1 / vv
    return (vv**k - vv**-k) / den if abs(den) > mp.mpf("1e-30") else mp.mpf(0)


def J_mp(w, N):
    n = N - 1
    vv = w**2
    dN = qint_mp(vv, N)
    if abs(dN) < mp.mpf("1e-30"):
        return None
    tot = mp.fsum((-1) ** ((n - j) % 2)
                  * w ** (3 * (2 * j * (j + 1) - n * (n + 2)))
                  * qint_mp(vv, 2 * j + 1) for j in range(n + 1))
    return w ** (-3 * n * (n + 2)) * tot / dN


worstB = worstC = mp.mpf(0)
for N in range(1, 9):
    wB = mp.expjpi(mp.mpf(2) / (4 * N))          # w^(4N) = 1
    if abs(wB**4 - 1) > 1e-20:
        jv = J_mp(wB, N + 1)
        if jv is not None:
            worstB = max(worstB, abs(jv - 1))
    wC = mp.expjpi(mp.mpf(2) / (4 * (N + 1)))    # w^(4(N+1)) = 1
    if abs(wC**4 - 1) > 1e-20:
        jv = J_mp(wC, N)
        if jv is not None:
            worstC = max(worstC, abs(jv - 1))
okB = worstB < mp.mpf("1e-30")
okC = worstC < mp.mpf("1e-30")
ok_all &= okB and okC
print(f"  [B core, numeric 40dps] worst |J(N+1)-1| at w^(4N)=1: {mp.nstr(worstB, 5)} "
      f"{'PASS' if okB else 'FAIL'}")
print(f"  [C core, numeric 40dps] worst |J(N)-1| at w^(4N+4)=1: {mp.nstr(worstC, 5)} "
      f"{'PASS' if okC else 'FAIL'}")

print(f"\n  OVERALL: {'ALL PASS — safe to transcribe' if ok_all else 'FAILURES — fix before Lean'}")
sys.exit(0 if ok_all else 1)
