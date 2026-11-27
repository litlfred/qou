#!/usr/bin/env python3
"""bring54_cochain_complex_probe -- exact checks on the Bring {5,4} map.

Context: owner request 2026-11-25 (docs/coordination/owner-rulings.md) to review
an external essay's claims that (i) QOU observables project onto triangulation
cochains of Bring's surface as a chain map, and (ii) "Bring's triangulation
prevents Navier-Stokes blow-up".  Audit:
docs/audits/2026-11-25-holography-qns-essay-review.md.

Everything here is EXACT: integer incidence matrices, ranks over Q by
Fraction Gaussian elimination, characteristic polynomials with sympy over Z.
No float enters any computed quantity.

The map.  Bring's surface is the genus-4 Riemann surface with orientation-
preserving automorphism group S5; its regular hyperbolic tessellation is
{5,4} with 24 pentagons (Riera-Rodriguez 1992; Braden-Northover 2012, both
held in library/).  A regular orientable map of type {5,4} with group G is
given by darts = G, vertex rotation = right multiplication by y (order 4),
edge involution = right multiplication by t (order 2), face rotation
phi = sigma o alpha, i.e. g -> g*t*y, of order 5.  We search S5 for (y, t)
with |y| = 4, |t| = 2, |t*y| = 5 and <y, t> = S5, which gives
V = 120/4 = 30, E = 60, F = 24, chi = -6, genus 4, 240 flags.

Checks:
  C1  V, E, F, chi, flags.
  C2  d1 . d0 = 0 (it is a cochain complex).
  C3  Betti numbers over Q: b0 = 1, b1 = 8, b2 = 1.
  C4  dim ker of the combinatorial Hodge Laplacian Delta_1 = 8 (unit inner
      products).  The essay's "no ungapped zero mode" is false for velocity.
  C5  every harmonic 1-cochain has zero vorticity (d1 h = 0), so the 8 modes
      carry zero enstrophy.
  C6  Stokes: 1^T d1 = 0 (sum of coherently oriented face boundaries is 0),
      so a nonzero CONSTANT face value is never d1 of any 1-cochain.  The
      essay's face value "evaluate V0" on every face is not in im d1.
  C7  lambda_1(Delta_0) > 0 and lambda_1(Delta_2 on (ker)^perp) > 0: spectral
      gaps exist, as on ANY finite connected complex; reported with charpoly
      factorisations so the S5 structure is visible but not over-claimed.
  C8  homological (Z2) code on the map: n = 60 edges, k = 2g = 8; distances
      d_Z = shortest homologically nontrivial cycle in the vertex graph,
      d_X = same in the dual (face) graph.
"""
import itertools
import json
import pathlib
import sys
from collections import deque
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / p) for p in
                ("computations", "computations/substrate", "tools/qou-substrate/python")]

import sympy  # noqa: E402

ASSERTS = []


def check(label, ok, detail=""):
    ASSERTS.append((label, bool(ok), detail))
    print(f"[{'ok' if ok else 'FAIL'}] {label}{(' -- ' + detail) if detail else ''}")


# ---------- S5 as tuples ----------
N = 5
ID = tuple(range(N))


def mul(a, b):  # (a*b)(i) = a(b(i)); right multiplication g -> g*b means g o b
    return tuple(a[b[i]] for i in range(N))


def order(a):
    k, x = 1, a
    while x != ID:
        x, k = mul(x, a), k + 1
    return k


S5 = list(itertools.permutations(range(N)))


def generated(gens):
    seen, frontier = {ID}, [ID]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = mul(g, h)
                if x not in seen:
                    seen.add(x)
                    nxt.append(x)
        frontier = nxt
    return seen


def find_pair():
    for y in S5:
        if order(y) != 4:
            continue
        for t in S5:
            if order(t) == 2 and order(mul(t, y)) == 5 and len(generated([y, t])) == 120:
                return y, t
    raise RuntimeError("no (y,t) found")


y, t = find_pair()
idx = {g: i for i, g in enumerate(S5)}
sigma = [idx[mul(g, y)] for g in S5]          # vertex rotation
alpha = [idx[mul(g, t)] for g in S5]          # edge involution
phi = [sigma[alpha[d]] for d in range(120)]   # face rotation


def cycles(perm):
    seen, out = set(), []
    for d in range(len(perm)):
        if d in seen:
            continue
        c, x = [], d
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = perm[x]
        out.append(c)
    return out


Vc, Ec, Fc = cycles(sigma), cycles(alpha), cycles(phi)
V, E, F = len(Vc), len(Ec), len(Fc)
vert_of = {d: i for i, c in enumerate(Vc) for d in c}
face_of = {d: i for i, c in enumerate(Fc) for d in c}
rep = [c[0] for c in Ec]  # oriented edge e = dart rep[e], tail vert_of[d], head vert_of[alpha d]
edge_of = {}
for e, c in enumerate(Ec):
    edge_of[c[0]] = (e, +1)
    edge_of[c[1]] = (e, -1)

chi = V - E + F
check("C1 V,E,F = 30,60,24; chi = -6; genus 4; 240 flags",
      (V, E, F, chi, 4 * E) == (30, 60, 24, -6, 240),
      f"V={V} E={E} F={F} chi={chi} flags={4*E}; y={y} t={t}")
check("C1b every vertex has degree 4 and every face 5 edges",
      all(len(c) == 4 for c in Vc) and all(len(c) == 5 for c in Fc))

# coboundaries: d0 : C^0 -> C^1 (E x V), d1 : C^1 -> C^2 (F x E)
d0 = [[0] * V for _ in range(E)]
for e in range(E):
    d = rep[e]
    d0[e][vert_of[d]] -= 1
    d0[e][vert_of[alpha[d]]] += 1
d1 = [[0] * E for _ in range(F)]
for f, c in enumerate(Fc):
    for d in c:  # face boundary traverses dart d from its tail to its head
        e, s = edge_of[d]
        d1[f][e] += s


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def T(A):
    return [list(r) for r in zip(*A)]


def rank_q(A):
    M = [[Fraction(x) for x in r] for r in A]
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


check("C2 d1 . d0 = 0", all(x == 0 for r in matmul(d1, d0) for x in r))
r0, r1 = rank_q(d0), rank_q(d1)
b0, b1, b2 = V - r0, E - r0 - r1, F - r1
check("C3 Betti over Q: (1, 8, 1)", (b0, b1, b2) == (1, 8, 1), f"rank d0={r0} rank d1={r1}")

L0 = matmul(T(d0), d0)
L1 = [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(matmul(d0, T(d0)), matmul(T(d1), d1))]
L2 = matmul(d1, T(d1))
k0, k1, k2 = V - rank_q(L0), E - rank_q(L1), F - rank_q(L2)
check("C4 dim ker Delta_1 = 8 = 2g (harmonic velocity modes exist)", k1 == 8,
      f"dim ker Delta_0={k0}, Delta_1={k1}, Delta_2={k2}")

# harmonic basis: kernel of L1 by exact nullspace
Lm = sympy.Matrix(L1)
H = Lm.nullspace()
d1m, d0m = sympy.Matrix(d1), sympy.Matrix(d0)
check("C5 every harmonic 1-cochain has zero vorticity d1 h = 0 and zero divergence d0^T h = 0",
      len(H) == 8 and all((d1m * h).is_zero_matrix and (d0m.T * h).is_zero_matrix for h in H))

ones_F = [1] * F
col_sums = [sum(d1[f][e] for f in range(F)) for e in range(E)]
check("C6 Stokes: 1^T d1 = 0, so a nonzero constant face value is not in im d1",
      all(s == 0 for s in col_sums),
      "for any 1-cochain a: sum_f (d1 a)(f) = 0, while sum_f c = 24c")

lam = sympy.symbols("lam")
cp0 = sympy.Matrix(L0).charpoly(lam).as_expr()
cp2 = sympy.Matrix(L2).charpoly(lam).as_expr()
f0, f2 = sympy.factor_list(cp0), sympy.factor_list(cp2)


def factor_str(fl):
    return " * ".join(f"({sympy.sstr(p)})^{m}" for p, m in fl[1])


def min_positive_root(fl):
    # exact: smallest positive root over all irreducible factors (CRootOf / radicals)
    cands = []
    for fac, _m in fl[1]:
        for r in sympy.Poly(fac, lam).real_roots():
            if r.is_positive:
                cands.append(r)
    best = cands[0]
    for r in cands[1:]:
        if (r - best).is_negative:
            best = r
    return best


check("C7a lambda=0 is a root of Delta_0 of multiplicity exactly 1 (connected)",
      k0 == 1 and dict((sympy.Poly(f, lam), m) for f, m in f0[1]).get(sympy.Poly(lam, lam)) == 1)
check("C7b lambda=0 is a root of Delta_2 of multiplicity exactly 1",
      k2 == 1 and dict((sympy.Poly(f, lam), m) for f, m in f2[1]).get(sympy.Poly(lam, lam)) == 1)
print("charpoly Delta_0 =", factor_str(f0))
print("charpoly Delta_2 =", factor_str(f2))
lam1_0, lam1_2 = min_positive_root(f0), min_positive_root(f2)
check("C7c spectral gaps are positive (exact algebraic numbers)",
      lam1_0.is_positive and lam1_2.is_positive,
      f"lambda_1(Delta_0) = {sympy.sstr(sympy.radsimp(lam1_0))} ~ {sympy.N(lam1_0, 20)}; "
      f"lambda_1(Delta_2) = {sympy.sstr(sympy.radsimp(lam1_2))} ~ {sympy.N(lam1_2, 20)} (display)")

# ---------- Z2 homological code distances ----------
# Z2 cohomology basis: H^1 = ker d1 / im d0 over GF(2); nontrivial cycle z
# iff <c, z> = 1 for some cocycle c not a coboundary.  Use the harmonic-free
# route: z is nontrivial iff z is NOT in im(d1^T) mod 2 (boundaries of faces).


def gf2_rank(rows):
    basis = {}
    for v in rows:
        x = v
        while x:
            hb = x.bit_length() - 1
            if hb in basis:
                x ^= basis[hb]
            else:
                basis[hb] = x
                break
    return basis


def to_bits(vec):
    b = 0
    for i, x in enumerate(vec):
        if x % 2:
            b |= 1 << i
    return b


def in_span(basis, x):
    while x:
        hb = x.bit_length() - 1
        if hb not in basis:
            return False
        x ^= basis[hb]
    return True


face_bnd = gf2_rank([to_bits(r) for r in d1])            # boundaries in edge space
vert_cobnd = gf2_rank([to_bits(c) for c in T(d0)])         # vertex stars in edge space


def min_nontrivial_cycle(adj_edges, n_nodes, trivial_basis, maxlen):
    """Exact: enumerate every simple cycle of length <= maxlen (start at its
    least node, DFS through larger nodes only) and return the least length of
    one that is not in the span of the trivial cycles mod 2."""
    best = None
    for s0 in range(n_nodes):
        stack = [(s0, 0, 1 << s0, 0)]  # node, length, visited-node mask, edge mask
        while stack:
            u, L, vm, em = stack.pop()
            if best is not None and L + 1 >= best + 1:
                continue
            for v, e in adj_edges[u]:
                if em >> e & 1:
                    continue
                if v == s0 and L >= 2:
                    z = em | (1 << e)
                    if not in_span(trivial_basis, z):
                        best = L + 1 if best is None else min(best, L + 1)
                elif v > s0 and not (vm >> v & 1) and L + 1 < maxlen:
                    stack.append((v, L + 1, vm | (1 << v), em | (1 << e)))
    return best


adjV = [[] for _ in range(V)]
for e in range(E):
    u, w = vert_of[rep[e]], vert_of[alpha[rep[e]]]
    adjV[u].append((w, e))
    adjV[w].append((u, e))
adjF = [[] for _ in range(F)]
for e in range(E):
    fa, fb = face_of[rep[e]], face_of[alpha[rep[e]]]
    adjF[fa].append((fb, e))
    adjF[fb].append((fa, e))
dZ = min_nontrivial_cycle(adjV, V, face_bnd, 10)
dX = min_nontrivial_cycle(adjF, F, vert_cobnd, 10)
check("C8 Bring {5,4} homological code: n = 60, k = 8", E == 60 and b1 == 8,
      f"d_Z (vertex-graph systole) = {dZ}, d_X (dual-graph systole) = {dX}; "
      "exhaustive enumeration of simple cycles of length <= 10; a minimum-weight "
      "nontrivial Z2 class is always represented by a simple cycle")

failures = [a for a in ASSERTS if not a[1]]
print(f"\n=== {len(ASSERTS)-len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("bring54-cochain-complex")
    w.set_description(
        "Exact cochain complex of the regular {5,4} map with orientation-preserving "
        "group S5 (Bring's surface): V,E,F = 30,60,24, Betti (1,8,1), dim ker Delta_1 = 8 "
        "harmonic velocity modes with zero vorticity, Stokes obstruction to a constant "
        "face value in im d1, exact spectral gaps of Delta_0 and Delta_2, and the Z2 "
        "homological code parameters. Measures the essay claims reviewed in "
        "docs/audits/2026-11-25-holography-qns-essay-review.md. All integer/rational.")
    w.add_data("generators", {"y_vertex_rotation": list(y), "t_edge_involution": list(t)})
    w.add_data("counts", {"V": V, "E": E, "F": F, "chi": chi, "flags": 4 * E})
    w.add_data("betti_Q", [b0, b1, b2])
    w.add_data("hodge_kernel_dims", {"Delta_0": k0, "Delta_1": k1, "Delta_2": k2})
    w.add_data("charpoly_Delta_0", factor_str(f0))
    w.add_data("charpoly_Delta_2", factor_str(f2))
    w.add_data("lambda1_Delta_0", sympy.sstr(lam1_0))
    w.add_data("lambda1_Delta_2", sympy.sstr(lam1_2))
    w.add_data("z2_code", {"n": E, "k": b1, "d_Z": dZ, "d_X": dX})
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save({"q0Anchor": "independent",
            "q0AnchorReason": "pure combinatorics of the S5 map; no q enters"})
    print("witness written")
sys.exit(1 if failures else 0)
