#!/usr/bin/env python3
"""Exact probe: which ranks can an S5-stable sublattice of H_1(Bring, Z)^k have?

Reading tested: conj:magic-numbers-bring / conj:homological-shell-condensation,
"magic n = rank of an S5-stable (tau-hat-stable) period sub-lattice of
H_1(Bring, Z)^{k(n)}".

Everything is exact (integers, fractions.Fraction). No floats.

Step 1. Build Bring's curve combinatorially as the S5-cover of P^1 with
        signature (0; 2, 4, 5): generators a (order 2), b (order 4), c (order 5)
        with a*b*c = 1 generating S5. Check Riemann-Hurwitz gives genus 4.
Step 2. Count fixed points of every g in S5 on the 60 + 30 + 24 branch-fibre
        points (cosets of <a>, <b>, <c>); free fibres contribute none.
Step 3. Lefschetz: 1 - tr(g | H_1) + 1 = #Fix(g)  =>  chi(g) = 2 - #Fix(g).
Step 4. Decompose chi against characters built from scratch (permutation
        character, sign). Report the isotypic type and multiplicity.
Step 5. Every Q[S5]-subrepresentation of an isotypic module of type V is
        isomorphic to V^m (Lean: QOU.ShellCondensation.BringLatticeRanks.
        four_dvd_finrank_of_isotypic), so the realisable ranks are dim(V) * m.
        Compare with the magic set on 0..126.

Ref: [leitner2026] conj:magic-numbers-bring; Bring's curve signature (2,4,5)
     is standard (e.g. Weber, Bring's curve: its period matrix ..., 2005).
"""
from fractions import Fraction
from itertools import permutations

N = 5
G = list(permutations(range(N)))
IDX = {g: i for i, g in enumerate(G)}


def mul(g, h):  # (g*h)(x) = g(h(x))
    return tuple(g[h[x]] for x in range(N))


def inv(g):
    r = [0] * N
    for i, gi in enumerate(g):
        r[gi] = i
    return tuple(r)


E = tuple(range(N))


def order(g):
    k, x = 1, g
    while x != E:
        x, k = mul(x, g), k + 1
    return k


def cycle_type(g):
    seen, ct = set(), []
    for i in range(N):
        if i in seen:
            continue
        j, L = i, 0
        while j not in seen:
            seen.add(j)
            j, L = g[j], L + 1
        ct.append(L)
    return tuple(sorted(ct, reverse=True))


def sign(g):
    return (-1) ** sum(L - 1 for L in cycle_type(g))


def generated(gens):
    S, frontier = {E}, [E]
    while frontier:
        nxt = []
        for x in frontier:
            for s in gens:
                y = mul(x, s)
                if y not in S:
                    S.add(y)
                    nxt.append(y)
        frontier = nxt
    return S


def cyclic(g):
    S, x = [E], g
    while x != E:
        S.append(x)
        x = mul(x, g)
    return S


# Step 1: a generating triple of signature (2,4,5).
triple = None
for a in G:
    if order(a) != 2:
        continue
    for b in G:
        if order(b) != 4:
            continue
        c = inv(mul(a, b))
        if order(c) == 5 and len(generated([a, b])) == 120:
            triple = (a, b, c)
            break
    if triple:
        break
a, b, c = triple
assert mul(mul(a, b), c) == E
# Riemann-Hurwitz: 2g - 2 = |G| (-2 + sum (1 - 1/m_i))
two_g_minus_2 = Fraction(120) * (-2 + sum(1 - Fraction(1, m) for m in (2, 4, 5)))
genus = (two_g_minus_2 + 2) / 2
assert genus == 4, genus


# Step 2: fixed points on branch fibres (cosets x<h>).
def cosets(h):
    H = cyclic(h)
    seen, reps = set(), []
    for x in G:
        if x in seen:
            continue
        cos = frozenset(mul(x, y) for y in H)
        seen |= cos
        reps.append(cos)
    return reps


FIBRES = [cosets(a), cosets(b), cosets(c)]
assert [len(f) for f in FIBRES] == [60, 30, 24]


def fix(g):
    n = 0
    for fib in FIBRES:
        for cos in fib:
            x = next(iter(cos))
            if mul(g, x) in cos:
                n += 1
    return n


# Lefschetz applies to g != 1 (isolated fixed points); tr(1 | H_1) = 2g.
chi = {g: (2 - fix(g)) if g != E else int(2 * genus) for g in G}


# Step 4: characters from scratch.
def inner(f1, f2):
    return Fraction(sum(f1[g] * f2[g] for g in G), len(G))  # all chars real here


perm = {g: sum(1 for i in range(N) if g[i] == i) for g in G}
sgn = {g: sign(g) for g in G}
std = {g: perm[g] - 1 for g in G}
std_sgn = {g: std[g] * sgn[g] for g in G}

assert inner(std, std) == 1 and inner(std_sgn, std_sgn) == 1
assert inner(std, std_sgn) == 0  # distinct irreducibles

m_std = inner(chi, std)
m_std_sgn = inner(chi, std_sgn)
norm_chi = inner(chi, chi)

classes = {}
for g in G:
    classes.setdefault(cycle_type(g), g)
print("cycle type      |class|  #Fix  chi(H_1)  std  std*sgn")
for ct, g in sorted(classes.items()):
    size = sum(1 for h in G if cycle_type(h) == ct)
    print(f"{str(ct):15s} {size:6d} {fix(g):5d} {chi[g]:8d} {std[g]:4d} {std_sgn[g]:7d}")
print(f"<chi,std> = {m_std}, <chi,std*sgn> = {m_std_sgn}, <chi,chi> = {norm_chi}")
# <chi,chi> = sum m_i^2 over irreducibles; = 4 with m_{std*sgn} = 2 forces chi = 2 std*sgn.
assert m_std_sgn == 2 and norm_chi == 4 and m_std == 0
print("=> H_1(Bring, Q) = 2 * (std (x) sgn), dim V = 4 (NOT 2 * std).")

# Step 5: realisable ranks.
d = 4
magic = {2, 8, 20, 28, 50, 82, 126}
realisable = {n for n in range(0, 127) if n % d == 0}
print("magic & realisable    :", sorted(magic & realisable))
print("magic NOT realisable  :", sorted(magic - realisable))
print("realisable, not magic :", len(realisable - magic), "values, e.g.", sorted(realisable - magic)[:8])
assert magic - realisable == {2, 50, 82, 126}
assert magic & realisable == {8, 20, 28}
# Irreducible S5-stable sublattices (and irreducible Q[S5 x {1, tau}]-modules, tau
# an idempotent commuting with S5) all have rank exactly d = 4.
print("irreducible stable sublattice rank: {4} only")
