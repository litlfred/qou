#!/usr/bin/env python3
"""Exact check of the gamma-gamma pair-production table (bean qou-qs2u, PR #7825).

Recomputes gamma(phi) * gamma(psi) in H_3(q) with h = q - q^{-1} kept symbolic, where
gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^{-1} (def:photon; the last term is
the chiral vertex by owner ruling 2026-11-18, bean qou-99qc, confirmed 2026-11-20),
and compares the six channel coefficients with
brings-surface/trivial-knot-photon-interpretation-table5-data.md. The superseded
straight form 1 + phi0 s0 + phi1 s1 + phi01 s0 s1 is kept as gamma_straight and its
table is re-checked too, together with the coordinate change
gamma(phi0, phi1, phi01) = gamma_straight(phi0 - h phi01, phi1, phi01).
Exact sympy arithmetic only: no floats, no q0, no witness. The script's assertions
are the gate.
"""
import sympy as sp

h = sp.Symbol("h")
f0, f1, f01, p0, p1, p01 = sp.symbols("phi0 phi1 phi01 psi0 psi1 psi01")

# Basis words are reduced words in S_3, generators 0 and 1.
NAMES = {(): "1", (0,): "s0", (1,): "s1", (0, 1): "L+", (1, 0): "L-", (0, 1, 0): "e-"}


def canon(w):
    """Reduce using the braid relation s1 s0 s1 = s0 s1 s0. Words have length <= 3."""
    return (0, 1, 0) if w == (1, 0, 1) else w


def gen_times(s, w):
    """T_s T_w in H_3: T_{sw} if l(sw) > l(w), else h T_w + T_{sw}."""
    w = canon(w)
    if len(w) == 3:  # longest word: write it as (s, 1-s, s) so s is the first letter
        return {w: h, (1 - s, s): 1}
    if w and w[0] == s:  # s is a left descent
        return {w: h, w[1:]: 1}
    return {canon((s,) + w): 1}


def mul(a, b):
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            cur = {wb: cb * ca}
            for s in reversed(wa):
                nxt = {}
                for w, c in cur.items():
                    for w2, c2 in gen_times(s, w).items():
                        nxt[w2] = nxt.get(w2, 0) + c * c2
                cur = nxt
            for w, c in cur.items():
                out[w] = sp.expand(out.get(w, 0) + c)
    return out


def add(*xs):
    out = {}
    for x in xs:
        for w, c in x.items():
            out[w] = sp.expand(out.get(w, 0) + c)
    return out
def scale(c, x):
    return {w: c * v for w, v in x.items()}
S0, S1, ONE = {(0,): 1}, {(1,): 1}, {(): 1}
S1INV = {(1,): 1, (): -h}  # s1^{-1} = s1 - h
assert {w: c for w, c in mul(S1, S1INV).items() if c != 0} == {(): 1}
assert {w: c for w, c in mul(S1INV, S1).items() if c != 0} == {(): 1}
VERTEX = mul(S0, S1INV)  # the chiral pair-production vertex s0 s1^{-1}
def gamma(a0, a1, a01):
    """def:photon, built with the algebra product."""
    return add(ONE, scale(a0, S0), scale(a1, S1), scale(a01, VERTEX))
def gamma_straight(a0, a1, a01):
    return {(): 1, (0,): a0, (1,): a1, (0, 1): a01}
# coordinate change: same family of elements
for w, c in add(gamma(f0, f1, f01), scale(-1, gamma_straight(f0 - h * f01, f1, f01))).items():
    assert sp.expand(c) == 0, (w, c)
prod = mul(gamma(f0, f1, f01), gamma(p0, p1, p01))
table5 = {
    (): 1 + f0 * p0 + f1 * p1 - h * (f0 * p01 + f01 * p0) + h**2 * f01 * p01,
    (0,): f0 + p0 + f0 * p0 * h + f01 * p1 - h * (f01 + p01)
          - h**2 * (f0 * p01 + f01 * p0) + h**3 * f01 * p01,
    (1,): f1 + p1 + f1 * p1 * h + f0 * p01 - h * f01 * p01,
    (0, 1): f01 + p01 + f0 * p1 + h * f0 * p01 - h**2 * f01 * p01,
    (1, 0): f1 * p0 + f01 * p01 - h * f1 * p01,
    (0, 1, 0): f01 * p0 + f1 * p01,
}
prod_straight = mul(gamma_straight(f0, f1, f01), gamma_straight(p0, p1, p01))
table5_straight = {
    (): 1 + f0 * p0 + f1 * p1,
    (0,): f0 + p0 + f0 * p0 * h + f01 * p1,
    (1,): f1 + p1 + f1 * p1 * h + f0 * p01,
    (0, 1): f01 + p01 + f0 * p1 + h * (f0 * p01 + f01 * p1),
    (1, 0): f1 * p0 + f01 * p01,
    (0, 1, 0): f01 * p0 + f1 * p01 + f01 * p01 * h,
}
for w in NAMES:
    assert sp.expand(prod_straight.get(w, 0) - table5_straight[w]) == 0, ("straight", w)
ok = True
for w in NAMES:
    got = sp.expand(prod.get(w, 0))
    diff = sp.expand(got - table5[w])
    status = "OK" if diff == 0 else f"MISMATCH (got - table = {diff})"
    ok &= diff == 0
    print(f"{NAMES[w]:>3}: {got}   [{status}]")

# Reference point of the confinement conjecture: all coefficients zero.
zero = {x: 0 for x in (f0, f1, f01, p0, p1, p01)}
print("at phi = psi = 0:", {NAMES[w]: sp.sympify(prod.get(w, 0)).subs(zero) for w in NAMES})
assert all(sp.sympify(prod.get(w, 0)).subs(zero) == (1 if w == () else 0) for w in NAMES)
assert ok, "table5 disagrees with the exact H_3 product"
print("PASS")
