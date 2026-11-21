#!/usr/bin/env python3
"""Pre-registered count survey for the proton identity's 2 and 12.

Pre-registration: docs/audits/2026-11-21-proton-two-twelve-count-survey.md, section 1
(committed 6bbc0b0f3 before this script existed). One definition per candidate K1..K7.
Exact arithmetic: sympy over Q(q) for K1, K2; pure combinatorics for K3, K4, K5, K7;
mpmath at 50 dps for K6. No float.

Hecke convention: (s - q)(s + 1/q) = 0. H_3(q) over Q(q) is split semisimple,
H_3 = Q(q) x M_2(Q(q)) x Q(q) (blocks (3), (2,1), (1,1,1)).
"""
import itertools
import sympy as sp
import mpmath as mp

q = sp.symbols('q')

# ---- the word P = (s0 s1^-1)^3, letters (generator, sign) -------------------------
P = [(0, 1), (1, -1)] * 3

# ---- K1, K2: block images of P ------------------------------------------------------
# (2,1) irrep; c = 1 solves the braid relation (checked below).
S0 = sp.Matrix([[q, 1], [0, -1 / q]])
S1 = sp.Matrix([[-1 / q, 0], [1, q]])
assert sp.simplify(S0 * S1 * S0 - S1 * S0 * S1) == sp.zeros(2)
assert sp.simplify((S0 - q * sp.eye(2)) * (S0 + sp.eye(2) / q)) == sp.zeros(2)
assert sp.simplify((S1 - q * sp.eye(2)) * (S1 + sp.eye(2) / q)) == sp.zeros(2)

def image(gens, word):
    M = sp.eye(gens[0].shape[0])
    for g, e in word:
        M = M * (gens[g] if e == 1 else gens[g].inv())
    return sp.simplify(M)

M21 = image([S0, S1], P)
triv = image([sp.Matrix([[q]]), sp.Matrix([[q]])], P)[0]
sgn = image([sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]])], P)[0]
print("P on (3)     :", sp.simplify(triv))
print("P on (1,1,1) :", sp.simplify(sgn))
print("P on (2,1)   :", M21)
charpoly = sp.factor(M21.charpoly(sp.Symbol('x')).as_expr())
print("charpoly on (2,1):", charpoly)

# centraliser of M21 in M_2: kernel of X -> M X - X M
X = sp.Matrix(2, 2, sp.symbols('x0:4'))
eqs = list(sp.simplify(M21 * X - X * M21))
A, _ = sp.linear_eq_to_matrix(eqs, list(X))
dimC21 = 4 - sp.simplify(A).rank(simplify=True)
K1 = 1 + dimC21 + 1
# min poly of diag(triv, M21, sgn): lcm of (x - triv), (x - sgn), minpoly(M21)
x = sp.Symbol('x')
is_scalar = sp.simplify(M21 - M21[0, 0] * sp.eye(2)) == sp.zeros(2)
mp21 = (x - M21[0, 0]) if is_scalar else M21.charpoly(x).as_expr()
mpoly = sp.lcm(sp.lcm(x - triv, x - sgn), sp.factor(mp21))
K2 = sp.degree(mpoly, x)
print("K1 dim centraliser =", K1, "  K2 dim Q(q)[P] =", K2, "  minpoly:", sp.factor(mpoly))

# ---- K3, K4, K7: combinatorics of the word -----------------------------------------
def perm_of(word, n=3):
    pos = list(range(n))          # pos[strand] = current position
    cross = []                    # (strand_a, strand_b) per crossing
    for g, _ in word:
        a = pos.index(g); b = pos.index(g + 1)
        cross.append(tuple(sorted((a, b))))
        pos[a], pos[b] = g + 1, g
    return pos, cross

pos, cross = perm_of(P)
# components = cycles of the closure permutation strand -> end position
seen, comps = set(), []
for s in range(3):
    if s in seen: continue
    cyc, t = [], s
    while t not in seen:
        seen.add(t); cyc.append(t); t = pos[t]
    comps.append(tuple(cyc))
comp_of = {s: i for i, c in enumerate(comps) for s in c}
K4 = len(comps)
K3 = {}
for a, b in cross:
    ca, cb = comp_of[a], comp_of[b]
    if ca != cb:
        K3[tuple(sorted((ca, cb)))] = K3.get(tuple(sorted((ca, cb))), 0) + 1
self_cross = sum(1 for a, b in cross if comp_of[a] == comp_of[b])
rotations = {tuple(P[i:] + P[:i]) for i in range(len(P))}
K7 = len(rotations)
K5 = 3 - len(P)
print("K3 crossings per component pair =", K3, " self-crossings =", self_cross)
print("K4 components =", K4, "  K5 Seifert chi =", K5, "  K7 rotation orbit =", K7)

# ---- K6: [PSL(2,Z[i]) : Gamma_L] = Vol(L)/covol --------------------------------------
mp.mp.dps = 50
G = mp.catalan
V_oct = 8 * mp.clsin(2, mp.pi / 2) / 2          # 8*Lambda(pi/4), Lambda(t) = Cl2(2t)/2
vol_bor = 2 * V_oct                             # Thurston: two regular ideal octahedra
covol = 8 * mp.zeta(2) * G / (4 * mp.pi ** 2)  # Humbert, D = -4: |D|^{3/2} zeta_K(2)/(4 pi^2)
K6 = vol_bor / covol
print("V_oct =", V_oct, " (4G =", 4 * G, ")")
print("covol PSL(2,Z[i]) =", covol, " (G/3 =", G / 3, ")")
print("K6 index =", mp.nstr(K6, 40))

print()
print("SUMMARY  K1=%s K2=%s K3=%s K4=%s K5=%s K6=%s K7=%s"
      % (K1, K2, sorted(K3.values()), K4, K5, mp.nstr(K6, 20), K7))
