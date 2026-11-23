"""N_sym from the Hoefsmit slot realisation: exact symbolic derivation.

Block: conj:g-action-on-substrate.  Audit: docs/audits/2026-11-20-nsym-derivation.md.
Lean twin: QOU.QuantumObservableUniverses.NSymSlotDerivation.

Builds V^{x6} (V = 2-dim q-fundamental) with the Hecke generators
sigma_1, sigma_3, sigma_5 acting on strand pairs (1,2), (3,4), (5,6),
the pivotal element K^{x6}, K = diag(q, q^-1), and computes, EXACTLY over Q(q):

  * qtr(E(a,b,c)) for the eight joint carrier idempotents;
  * that qtr/[2]^6 is the Markov trace at convention D, z = q^3/(q^2+1);
  * that the alt idempotent of one slot is rank one and factors through the
    unit (the unique (G-3)/(G-4) e_H on a V(x)V host);
  * N_sym = qtr(e+ (x) e+ (x) e_H) = [3]_q^2.

Numerics: proton q0 (qou_substrate.constants.q_at), mpmath, no float64.
The 213.11 anchor is NOT used anywhere in this script.
"""
import itertools
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools/qou-substrate/python"))

q = sp.symbols("q", positive=True)
qi = 1 / q
two = q + qi


def qint(n):
    return sp.simplify((q**n - q**(-n)) / (q - qi))


# Hecke generator on V(x)V, basis 00,01,10,11
S = sp.Matrix([[q, 0, 0, 0], [0, q - qi, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
I4 = sp.eye(4)
assert sp.simplify(S * S - ((q - qi) * S + I4)) == sp.zeros(4)
ep = (S + qi * I4) / two      # sym  (eigenvalue q)
em = (q * I4 - S) / two       # alt  (eigenvalue -q^-1)
K = sp.diag(q, qi)
KK = sp.kronecker_product(K, K)


def qtr2(x):
    return sp.simplify((KK * x).trace())


assert sp.simplify(qtr2(I4) - two**2) == 0
assert sp.simplify(qtr2(ep) - qint(3)) == 0
assert sp.simplify(qtr2(em) - 1) == 0
# Markov parameter of this trace = convention D
assert sp.simplify(qtr2(S) / two**2 - q**3 / (q**2 + 1)) == 0
# e- is rank one and factors through the unit: e- = u w^T / [2], w.u = [2]
u = sp.Matrix([0, 1, -q, 0])
w = sp.Matrix([0, qi, -1, 0])
assert sp.simplify(em - u * w.T / two) == sp.zeros(4)
assert sp.simplify((w.T * u)[0] - two) == 0
# the -q^-1 eigenspace of S is one-dimensional
assert (S + qi * I4).subs(q, sp.Rational(3, 2)).rank() == 3
# carriers sigma^{2k}: e+ is their q^{2k}-eigenprojector, for k = 2,3,4
for k in (2, 3, 4):
    assert sp.simplify(S**(2 * k) * ep - q**(2 * k) * ep) == sp.zeros(4)
    assert sp.simplify(S**(2 * k) * em - q**(-2 * k) * em) == sp.zeros(4)

# three slots
proj = {True: ep, False: em}
K6 = sp.kronecker_product(KK, sp.kronecker_product(KK, KK))
results = {}
for a, b, c in itertools.product((True, False), repeat=3):
    E = sp.kronecker_product(proj[a], sp.kronecker_product(proj[b], proj[c]))
    val = sp.factor(sp.simplify((K6 * E).trace()))
    results[(a, b, c)] = val
    expect = (qint(3) if a else 1) * (qint(3) if b else 1) * (qint(3) if c else 1)
    assert sp.simplify(val - expect) == 0
# spin-decomposition check: V1^{x3} = V3 + 2V2 + 3V1 + V0 ; V1^{x2} = V2+V1+V0
assert sp.simplify(qint(3)**3 - (qint(7) + 2 * qint(5) + 3 * qint(3) + 1)) == 0
assert sp.simplify(qint(3)**2 - (qint(5) + qint(3) + 1)) == 0

N_sym = results[(True, True, False)]
print("qtr E(+,+,-) = N_sym =", N_sym, "= [3]_q^2")
print("qtr E(+,+,+) =", results[(True, True, True)], "= [3]_q^3")

import mpmath as mp
from qou_substrate.constants import q_at

mp.mp.dps = 50
q0 = q_at(50)
print("proton q0 =", mp.nstr(q0, 30))


def qn(n, x):
    return (x**n - x**(-n)) / (x - 1 / x)


vals = {
    "[3]^2 (derived, EW-sym x e_H)": qn(3, q0) ** 2,
    "[3]^3 (E(+,+,+), all three slots)": qn(3, q0) ** 3,
    "[3]^2/[2]^6 (normalised Markov, z_D)": qn(3, q0) ** 2 / qn(2, q0) ** 6,
    "(a) [4]^2[6]": qn(4, q0) ** 2 * qn(6, q0),
    "(b) 2[4]+[6]": 2 * qn(4, q0) + qn(6, q0),
    "(c) [4][6]": qn(4, q0) * qn(6, q0),
}
for k, v in vals.items():
    print(f"{k:42s} {mp.nstr(v, 15)}")
