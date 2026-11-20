#!/usr/bin/env python3
"""D-H3 beyond one letter: is the weak knot T(3,5) supported on the left line?

Bean qou-hlx7 (owner decision D-H3, 2026-11-15). Lean side:
QOU/QuarkState/WeakVertexLeftProjector.lean proves, for ONE letter, that the vertex
insertion weakVertex - sigma equals -h * leftLine (derived from the owner-ruled leftLine
definition). This probe asks whether the same one-sidedness holds for the corpus weak
knot T(3,5) = closure of (s1 s2)^5 in H_3, under the convention-D Markov trace.

Split the knot word along the two lines of the letter s1:
    beta = beta * P_L + beta * P_R,   P_L = P_+ (q > 1, leftLine_eq_Pp_iff).
If the weak knot were left-supported, tau_D(beta * P_R) would vanish.

Exact (sympy, symbolic q) for the structure; mpmath at 70 dps at the proton-pinned q0
for the numbers. No float arithmetic. No witness is written (probe). Nothing is fitted:
there are no free parameters.
"""
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools/qou-substrate/python"))
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # proton pin (owner directive 2026-08-07)

mp.mp.dps = 70
q = sp.symbols("q", positive=True)
h = q - 1 / q
ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# --- H_3 Wedderburn blocks: trivial (s -> q), sign (s -> -1/q), (2,1) two-dim ----------
S1 = sp.Matrix([[q, 0], [1, -1 / q]])
S2 = sp.Matrix([[-1 / q, 1], [0, q]])
I2 = sp.eye(2)
for name, S in (("s1", S1), ("s2", S2)):
    check(f"{name} Hecke: s^2 = h s + 1", sp.simplify(S * S - h * S - I2) == sp.zeros(2))
check("braid relation s1 s2 s1 = s2 s1 s2", sp.simplify(S1 * S2 * S1 - S2 * S1 * S2) == sp.zeros(2))

# convention-D Markov weights at n = 3 (y_(1^3) = 0); tr(1) = 1
y3 = (q**4 + 1) / (q**2 + 1) ** 2
y21 = q**2 / (q**2 + 1) ** 2
y111 = sp.Integer(0)
check("convention D normalised: y3 + 2 y21 = 1", sp.simplify(y3 + 2 * y21 - 1) == 0)


class El:
    """An element of H_3 by its image in the three blocks (triv scalar, 21 matrix, sign scalar)."""

    def __init__(self, t, m, s):
        self.t, self.m, self.s = sp.simplify(t), sp.simplify(m), sp.simplify(s)

    def __mul__(self, o):
        return El(self.t * o.t, self.m * o.m, self.s * o.s)

    def __add__(self, o):
        return El(self.t + o.t, self.m + o.m, self.s + o.s)

    def scale(self, c):
        return El(c * self.t, c * self.m, c * self.s)


one = El(1, I2, 1)
s1 = El(q, S1, -1 / q)
s2 = El(q, S2, -1 / q)
s1inv = El(1 / q, sp.simplify(S1.inv()), -q)
s2inv = El(1 / q, sp.simplify(S2.inv()), -q)


def tau(x):
    return sp.factor(sp.simplify(y3 * x.t + y21 * x.m.trace() + y111 * x.s))


def power(x, n):
    r = one
    for _ in range(n):
        r = r * x
    return r


br2 = 1 / (q + 1 / q)
PL = (s1 + one.scale(1 / q)).scale(br2)  # P_+ of s1 = leftLine at q > 1
PR = (one.scale(q) + s1.scale(-1)).scale(br2)  # P_- of s1
check("P_L + P_R = 1", tau((PL + PR) + one.scale(-1)) == 0 and sp.simplify((PL + PR).m - I2) == sp.zeros(2))
check("P_L idempotent (21 block)", sp.simplify(PL.m * PL.m - PL.m) == sp.zeros(2))
check("P_L P_R = 0 (21 block)", sp.simplify(PL.m * PR.m) == sp.zeros(2))

# --- 0. letter level, as in the Lean file: the vertex insertion is -h P_L ---------------
W = (s1inv * PL) + (s1 * PR)  # weakVertex at q > 1
ins = W + s1.scale(-1)
check(
    "letter level: weakVertex - s1 = -h P_L in every block",
    sp.simplify(ins.t + h * PL.t) == 0
    and sp.simplify(ins.m + h * PL.m) == sp.zeros(2)
    and sp.simplify(ins.s + h * PL.s) == 0,
)
check("letter level: tau_D of the insertion times P_R is 0", tau(ins * PR) == 0)

# --- 1. the weak knot T(3,5) ---------------------------------------------------------
beta = power(s1 * s2, 5)
W_closed = q**2 * (q**12 + q**8 - 1) / (q**2 + 1) ** 2  # corpus W(q), bean qou-egvf
tb = tau(beta)
check("tau_D((s1 s2)^5) reproduces the corpus W(q)", sp.simplify(tb - W_closed) == 0)
tL = tau(beta * PL)
tR = tau(beta * PR)
check("split adds up: tau(beta P_L) + tau(beta P_R) = W", sp.simplify(tL + tR - W_closed) == 0)
print("tau_D(beta P_L) =", tL)
print("tau_D(beta P_R) =", tR)
check("tau_D(beta P_R) = -q^2/(q^2+1)^3", sp.simplify(tR + q**2 / (q**2 + 1) ** 3) == 0)
check("weak knot is NOT left-supported: tau_D(beta P_R) != 0", sp.simplify(tR) != 0)
check(
    "the sign block carries no weight, so P_R is seen only through the (2,1) block",
    sp.simplify(tR - y21 * (beta * PR).m.trace()) == 0,
)
check("the same holds for the second letter s2", sp.simplify(tau(beta * ((one.scale(q) + s2.scale(-1)).scale(br2))) - tR) == 0)

# the ratio L : R, in terms of [3]_q = q^2 + 1 + q^-2
three = q**2 + 1 + 1 / q**2
ratio = sp.factor(sp.simplify(tL / tR))
print("tau(beta P_L) / tau(beta P_R) =", ratio)
check(
    "ratio = -q^4 [3]_q (q^8 + q^2 - 1)",
    sp.simplify(ratio + q**4 * three * (q**8 + q**2 - 1)) == 0,
)

# --- 2. the family T(3,N): the right-line share is periodic in N, never zero ------------
print("\nT(3,N), N = 1..9: tau_D((s1 s2)^N P_R) (exact)")
right_values = []
for n in range(1, 10):
    v = tau(power(s1 * s2, n) * PR)
    right_values.append(v)
    print(f"  N = {n}: {v}")
check("tau_D((s1 s2)^N P_R) has period 3 in N (the (2,1) block of s1 s2 has order 3)",
      all(sp.simplify(right_values[i] - right_values[i + 3]) == 0 for i in range(6)))
check("tau_D((s1 s2)^N P_R) != 0 for every N not divisible by 3",
      all(sp.simplify(right_values[n - 1]) != 0 for n in range(1, 10) if n % 3 != 0))
check("tau_D((s1 s2)^N P_R) at N = 3k equals tau_D(P_R) = y21 (the full twist is 1 on (2,1))",
      all(sp.simplify(right_values[n - 1] - y21) == 0 for n in (3, 6, 9)))

# --- 3. numbers at the proton q0 (mpmath, 70 dps) -----------------------------------------
q0 = Q_MP
f = sp.lambdify(q, [tb, tL, tR], modules="mpmath")
vb, vl, vr = f(q0)
print("\nat q0 =", mp.nstr(q0, 20))
print("  tau_D(beta)      =", mp.nstr(vb, 25))
print("  tau_D(beta P_L)  =", mp.nstr(vl, 25))
print("  tau_D(beta P_R)  =", mp.nstr(vr, 25))
print("  right-line share =", mp.nstr(vr / vb, 25))
check("at q0 the right-line share is nonzero", abs(vr / vb) > mp.mpf("1e-10"))

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
