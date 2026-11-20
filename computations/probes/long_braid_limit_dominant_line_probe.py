#!/usr/bin/env python3
"""Long-braid limit as a chirality mechanism: is any observable in the regime?

Bean qou-wkcd (owner decision 2, 2026-11-15). Lean side:
QOU/QuarkState/WeakChiralityRootLabel.lean (`tendsto_normalised_pow`): for |q| > 1,
q^{-N} s^N -> P_+ for one letter. Here: H_3, the torus-knot family T(3,N) = closure of
(s1 s2)^N, under the convention-D Markov trace (y_(1^3) = 0).

Exact (sympy, symbolic q) for the structure; mpmath at 70 dps at the proton-pinned q0
for the numbers. No float arithmetic. No witness is written (probe). Nothing is fitted:
there are no free parameters.

Questions:
 1. Which Wedderburn block dominates (s1 s2)^N, and at what rate?
 2. Is T(3,5) (10 crossings) in the limit regime at q0?
 3. Mirror (s1 s2)^{-N}: does the convention-D trace have a normalised limit?
"""
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools/qou-substrate/python"))
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # proton pin (owner directive 2026-08-07)

mp.mp.dps = 70
q = sp.symbols("q", positive=True)
ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# --- (2,1) block: s1 = diag(q, -1/q); s2 solved from trace, det, braid relation -------
a, c, d = sp.symbols("a c d")
S1 = sp.diag(q, -1 / q)
S2 = sp.Matrix([[a, 1], [c, d]])
eqs = [
    sp.Eq(a + d, q - 1 / q),
    sp.Eq(a * d - c, -1),
]
sols = sp.solve(eqs + list((S1 * S2 * S1 - S2 * S1 * S2)), [a, c, d], dict=True)
sols = [s for s in sols if sp.simplify((S2.subs(s)) - S1) != sp.zeros(2)]
S2 = sp.simplify(S2.subs(sols[0]))
I2 = sp.eye(2)
check("s2 Hecke: s2^2 = h s2 + 1", sp.simplify(S2 * S2 - (q - 1 / q) * S2 - I2) == sp.zeros(2))
check("braid: s1 s2 s1 = s2 s1 s2", sp.simplify(S1 * S2 * S1 - S2 * S1 * S2) == sp.zeros(2))
W = sp.simplify(S1 * S2)
check("(s1 s2)^3 = 1 on the (2,1) block (full twist acts by q^0)",
      sp.simplify(W ** 3 - I2) == sp.zeros(2))
print("char_(2,1)(s1 s2) =", sp.simplify(W.trace()), " (eigenvalues: primitive cube roots of 1)")

# characters of w^N: trivial q^{2N}, sign q^{-2N}, (2,1): 2,-1,-1 by N mod 3
def chi21(N):
    return sp.simplify((W ** (N % 3)).trace())


# --- convention-D Markov weights at n = 3 --------------------------------------------
z = q ** 3 / (q ** 2 + 1)
y3, y21, y111 = sp.symbols("y3 y21 y111")
sol = sp.solve(
    [
        sp.Eq(y3 + 2 * y21 + y111, 1),
        sp.Eq(q * y3 + (q - 1 / q) * y21 - y111 / q, z),
        sp.Eq(q ** 2 * y3 - y21 + y111 / q ** 2, z ** 2),
    ],
    [y3, y21, y111],
    dict=True,
)[0]
Y3, Y21, Y111 = (sp.factor(sol[v]) for v in (y3, y21, y111))
print("y_(3) =", Y3, "| y_(2,1) =", Y21, "| y_(1^3) =", Y111)
check("convention D kills the sign block: y_(1^3) = 0", sp.simplify(Y111) == 0)


def tr(N):
    """Convention-D Markov trace of (s1 s2)^N (N may be negative)."""
    return Y3 * q ** (2 * N) + Y21 * chi21(N) + Y111 * q ** (-2 * N)


# cross-check against the corpus weak-vertex trace (bean qou-egvf, sorry-free Lean
# QOU.Braiding.WeakVertexT35.weakVertexTrace_eq): tr((s1 s2)^5) = q^2(q^12+q^8-1)/(q^2+1)^2
check("T(3,5) trace matches corpus W(q) = q^2(q^12+q^8-1)/(q^2+1)^2",
      sp.simplify(tr(5) - q**2 * (q**12 + q**8 - 1) / (q**2 + 1) ** 2) == 0)

# --- numbers at q0 -------------------------------------------------------------------
q0 = Q_MP
y3n = mp.mpf(sp.N(Y3.subs(q, sp.Rational(Q_50_DIGIT_STR)), 70))
y21n = mp.mpf(sp.N(Y21.subs(q, sp.Rational(Q_50_DIGIT_STR)), 70))
print("q0 =", mp.nstr(q0, 20), " y3 =", mp.nstr(y3n, 15), " y21 =", mp.nstr(y21n, 15))
print("per-crossing decay of the non-dominant part: q0^-1 =", mp.nstr(1 / q0, 15))
print("e-fold length in crossings: 1/ln q0 =", mp.nstr(1 / mp.log(q0), 15))


def resid(N):
    """Relative distance of the normalised trace from its limit y3."""
    chi = mp.mpf(int(chi21(N)))
    return abs(y21n * chi / (y3n * q0 ** (2 * N)))


for N in (1, 2, 3, 5, 10, 20, 50):
    print(f"  T(3,{N}) [{2*N} crossings]: |q0^-2N tr / y3 - 1| = {mp.nstr(resid(N), 6)}")
print("T(3,5) (the 10-crossing weak knot): residual", mp.nstr(resid(5), 8),
      "-> NOT in the limit regime")
check("T(3,5) residual > 0.1 at q0 (finite-N, not a limit)", resid(5) > mp.mpf("0.1"))
Nmin = next(N for N in range(1, 10000) if all(resid(M) < mp.mpf("1e-3") for M in (N, N + 1, N + 2)))
print("smallest N with residual < 1e-3 for three consecutive N:", Nmin, f"({2*Nmin} crossings)")

# --- mirror: (s1 s2)^{-N} ------------------------------------------------------------
for N in (5, 10, 50):
    t = tr(-N)
    tn = mp.mpf(sp.N(t.subs(q, sp.Rational(Q_50_DIGIT_STR)), 70))
    print(f"  mirror T(3,{N}): tr = {mp.nstr(tn, 12)}  (y3 q0^-2N + y21 chi21)")
print("Mirror: the dominant block of (s1 s2)^-N is the sign block (q^{2N}), which convention D")
print("weights by 0, so the trace stays O(1) and oscillates with N mod 3: no normalised limit.")
check("mirror trace bounded (|tr| < 1) at N = 50", abs(mp.mpf(sp.N(tr(-50).subs(q, sp.Rational(Q_50_DIGIT_STR)), 70))) < 1)

# --- the convention-D asymmetry under the root relabel -------------------------------
zr = sp.simplify(z.subs(q, -1 / q))
print("z_D(q) =", z, " ; z_D(-1/q) =", zr, " (relabel the root: sign flips)")
check("z_D is not invariant under the root relabel q -> -1/q", sp.simplify(z - zr) != 0)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
