#!/usr/bin/env python3
"""n-p gap at q = 1: categorical mass at q = 1 and the E0 pole.

Audit: docs/audits/2026-11-22-np-gap-at-q-one-unit-map.md. Issue #9002.

Part A (exact, sympy over Q(q)): framing-corrected Jones-Markov mass of
def:mass-identity, (1+q^2)^n q^(-n-2w) * Tr(K^n rho(beta)) / Tr(K^n), with the
Jimbo R-check (eigenvalue q on Sym^2, -1/q on Lambda^2) and K = diag(q, 1/q).
Checks Markov invariance on stabilisation and prints m(q), m(1) for the
Borromean nucleon (s1 s2^-1)^3, its mirror, the electron s1 s2 s1, the trefoil.

Part B (mpmath, 40 dps): the n-p cell 2 E0 log q at the proton q0 read as an
energy (current corpus reading) and as a mass through def:mass-energy (/ c_q^2).
The CODATA numbers appear only in the final comparison lines.
"""
import os, sys
import sympy as sp
import mpmath as mp

q = sp.symbols('q', positive=True)
K = sp.diag(q, 1 / q)


def rcheck():
    R = sp.zeros(4, 4)
    R[0, 0] = q
    R[3, 3] = q
    R[1, 2] = 1
    R[2, 1] = 1
    R[1, 1] = q - 1 / q
    return R


R = rcheck()
RI = R.inv()


def gen(n, i, inv):
    M = RI if inv else R
    return sp.kronecker_product(sp.eye(2 ** i), M, sp.eye(2 ** (n - i - 2)))


def mass(n, word):
    rho = sp.eye(2 ** n)
    for a in word:
        rho = rho * gen(n, abs(a) - 1, a < 0)
    w = sum(1 if a > 0 else -1 for a in word)
    Kn = K
    for _ in range(n - 1):
        Kn = sp.kronecker_product(Kn, K)
    return sp.factor(sp.simplify((1 + q ** 2) ** n * q ** (-n - 2 * w)
                                 * (Kn * rho).trace() / Kn.trace()))


CASES = [
    ('nucleon (s1 s2^-1)^3, 3 components', 3, [1, -2] * 3, 3),
    ('mirror (s1^-1 s2)^3, 3 components', 3, [-1, 2] * 3, 3),
    ('stabilised +s3', 4, [1, -2] * 3 + [3], 3),
    ('stabilised -s3', 4, [1, -2] * 3 + [-3], 3),
    ('electron s1 s2 s1 (Hopf), 2 components', 3, [1, 2, 1], 2),
    ('trefoil s1^3, 1 component', 2, [1, 1, 1], 1),
    ('unknot (B1)', 1, [], 1),
]

ok = True
res = {}
print('Part A: categorical mass, exact over Q(q)')
for name, n, word, comps in CASES:
    m = mass(n, word) if n > 1 else sp.factor(1 + q ** 2) / q
    res[name] = m
    m1 = m.subs(q, 1)
    good = (m1 == 2 ** comps)
    ok &= bool(good)
    print(f'  {name:42s} m(1) = {m1}  (2^c = {2**comps})  m(q) = {m}')
p = res['nucleon (s1 s2^-1)^3, 3 components']
pm = res['mirror (s1^-1 s2)^3, 3 components']
for k in ('stabilised +s3', 'stabilised -s3'):
    ok &= sp.simplify(res[k] - p) == 0
mirror_rule = sp.simplify(pm - p.subs(q, 1 / q)) == 0
amph = sp.simplify(pm - p) == 0
ok &= mirror_rule
print('  Markov invariance on +/- stabilisation:', sp.simplify(res['stabilised +s3'] - p) == 0,
      sp.simplify(res['stabilised -s3'] - p) == 0)
print('  mirror rule m(mirror)(q) = m(q^-1):', mirror_rule)
print('  Borromean amphichiral, m(mirror) = m at every q:', amph)

print('\nPart B: the n-p cell at the proton q0 (mpmath, 40 dps)')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'tools', 'qou-substrate', 'python'))
from qou_substrate import constants as C  # noqa: E402

mp.mp.dps = 40
q0 = C.q_at(40)
me = mp.mpf(C.M_E_MEV_STR)
hq = 1 - 1 / q0
cq = 1 / (q0 - 1)
E0 = me * cq ** 2 * hq
L = mp.log(q0)
cellE = 2 * E0 * L
cellM = cellE / cq ** 2
print('  q0 =', mp.nstr(q0, 15), ' E0 =', mp.nstr(E0, 10), 'MeV  c_q^2 =', mp.nstr(cq ** 2, 10))
print('  energy reading 2 E0 log q      =', mp.nstr(cellE, 10), 'MeV  (/m_e =', mp.nstr(cellE / me, 10), ')')
print('  mass reading 2 m_e hbar_q log q =', mp.nstr(cellM, 10), 'MeV  (/m_e =', mp.nstr(cellM / me, 10), ')')
dnp = mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR)
print('  comparison only: CODATA m_n - m_p =', mp.nstr(dnp, 10), 'MeV;',
      'energy reading', mp.nstr(100 * (cellE / dnp - 1), 6), '%;',
      'mass reading', mp.nstr(100 * (cellM / dnp - 1), 6), '%')
print('\nALL CHECKS PASS' if ok else '\nCHECK FAILED')
sys.exit(0 if ok else 1)
