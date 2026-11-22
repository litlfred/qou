"""Exact Ocneanu trace over ℚ(q) with python-flint (same convention as ../he4_closed_form/hecke_exact.py).

Generators σ_i with σ² = hσ + 1, h = q − q⁻¹; Markov tr(x σ_n) = z tr(x), z = z_D = q³/(q²+1).
Letters are ('S', i) = σ_i, ('I', i) = σ_i⁻¹ = σ_i − h, ('A', i) = σ_i − h/2.

Speed: each letter is scaled by q so the word lives in ℚ[q]·S_n; the trace of each basis
element T_w is computed once in ℤ[h, z] and substituted at the end. A value is returned as
(N, a, b), meaning N(q) / (q^a (q²+1)^b), with N in ℚ[q]. No floats.
"""
from __future__ import annotations

from functools import lru_cache

import flint

Q = flint.fmpq_poly([0, 1])
ONE = flint.fmpq_poly([1])
C = Q * Q + 1
QH = Q * Q - 1  # q·h
HZ = flint.fmpz_mpoly_ctx.get(("h", "z"), "lex")
_h, _z = HZ.gens()
_one = HZ.from_dict({(0, 0): 1})


def _mul_T(x, i):
    out = {}
    for w, c in x.items():
        l = list(w)
        up = l[i] < l[i + 1]
        l[i], l[i + 1] = l[i + 1], l[i]
        u = tuple(l)
        out[u] = out.get(u, 0) + c
        if not up:
            out[w] = out.get(w, 0) + c * _h
    return {w: c for w, c in out.items() if c != 0}


@lru_cache(maxsize=None)
def trT(w):
    """Ocneanu trace of the basis element T_w, in ℤ[h, z]."""
    n = len(w)
    if n == 1:
        return _one
    if w[-1] == n - 1:
        return trT(w[:-1])
    p = w.index(n - 1)
    l = list(w)
    for i in range(p, n - 1):
        l[i], l[i + 1] = l[i + 1], l[i]
    x = {tuple(l[:-1]): _one}
    for i in range(n - 3, p - 1, -1):
        x = _mul_T(x, i)
    s = HZ.from_dict({})
    for u, c in x.items():
        s += c * trT(u)
    return _z * s


_B = {"S": None, "I": -QH, "A": -QH / 2}


def _mul_letter(x, kind, i):
    B = _B[kind]
    out = {}
    for w, c in x.items():
        if B is not None:
            out[w] = out.get(w, 0) + c * B
        l = list(w)
        up = l[i] < l[i + 1]
        l[i], l[i + 1] = l[i + 1], l[i]
        u = tuple(l)
        out[u] = out.get(u, 0) + c * Q
        if not up:
            out[w] = out.get(w, 0) + c * QH
    return {w: c for w, c in out.items() if c != 0}


def tr(n, letters):
    """Trace of the word on n strands, as (N, a, b) = N / (q^a (q²+1)^b)."""
    x = {tuple(range(n)): ONE}
    for kind, i in letters:
        x = _mul_letter(x, kind, i)
    acc = {}
    for w, c in x.items():
        for (a, b), t in trT(w).to_dict().items():
            acc[(a, b)] = acc.get((a, b), 0) + c * int(t)
    H = max(a for a, b in acc)
    Z = max(b for a, b in acc)
    N = flint.fmpq_poly([0])
    for (a, b), c in acc.items():
        N += c * QH ** a * Q ** (H - a + 3 * b) * C ** (Z - b)
    return (N, len(letters) + H, Z)


def mul(u, v):
    return (u[0] * v[0], u[1] + v[1], u[2] + v[2])


def div_num(u, v):
    """u / v as (numerator, denominator) polynomials."""
    a = u[1] - v[1]
    b = u[2] - v[2]
    num, den = u[0], v[0]
    if a > 0:
        den = den * Q ** a
    else:
        num = num * Q ** (-a)
    if b > 0:
        den = den * C ** b
    else:
        num = num * C ** (-b)
    return num, den


def evalq(u, qv):
    """Exact value at a rational q (flint fmpq)."""
    return u[0](qv) / (qv ** u[1] * (qv * qv + 1) ** u[2])


def same(u, v):
    n, d = div_num(u, v)
    return n == d


# production blocks (mass_at_3A_proper.atom_braid_word_3A), on strands k..k+2
def V3(k):
    return [("S", k), ("I", k + 1)] * 3


def proton(k=0):
    return V3(k) + [("S", k), ("A", k), ("A", k + 1), ("S", k), ("S", k)]


def neutron(k=0):
    return V3(k) + [("A", k), ("A", k), ("I", k + 1), ("S", k), ("S", k)]


def bond(i, j, variant):
    """γγ bond on nucleons (i, j): V³ at strands (3j−1, 3j), transported for j > i + 1."""
    gens = list(range(3 * i + 2, 3 * j - 1))
    up, dn = ("S", "I") if variant == "over" else ("I", "S")
    return [(up, g) for g in gens] + V3(3 * j - 1) + [(dn, g) for g in reversed(gens)]


def atom_word(order, bonds, variant, start=0):
    """Blocks in `order`; bonds in route (list) order, each placed after block J, the running
    maximum of j over the route so far (as in he4_gg_all_pairs_probe.build: once a bond
    reaches block J, later bonds stay after J). start=1 drops block 0 and shifts down by 2
    (the tail of towerTr_disjoint)."""
    blk = {"p": proton, "n": neutron}
    after = {k: [] for k in range(len(order))}
    J = 0
    for i, j in bonds:
        J = max(J, j)
        after[J] += bond(i, j, variant)
    w = []
    for k in range(start, len(order)):
        w += blk[order[k]](3 * k) + after[k]
    if start:
        assert min(i for _, i in w) >= 3 * start - 1
        w = [(t, i - (3 * start - 1)) for t, i in w]
    return w
