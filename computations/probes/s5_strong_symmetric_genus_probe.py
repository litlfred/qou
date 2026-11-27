#!/usr/bin/env python3
"""S5 strong symmetric genus probe (bean qou-qhcr).

Companion to BraidKnotOctonion/S5StrongSymmetricGenus.lean.  Exact enumeration in S5, no floats.
Checks that no generating vector of S5 has a Euclidean (genus-1) type:
  (0; 2,3,6), (0; 2,4,4), (0; 3,3,3), (0; 2,2,2,2), and (1; -) (two commuting generators);
and that the hyperbolic type (0; 2,4,5) of Bring's curve does have one.
So S5 acts on no torus; with the Lean arithmetic (no genus 0, 2, 3) its least genus is 4.
"""
import itertools, json, os

E = tuple(range(5))
G = list(itertools.permutations(range(5)))
def mul(p, q): return tuple(p[q[i]] for i in range(5))   # p after q
def inv(p):
    r = [0] * 5
    for i in range(5): r[p[i]] = i
    return tuple(r)
def order(p):
    k, q = 1, p
    while q != E: q = mul(p, q); k += 1
    return k
ORD = {p: order(p) for p in G}
def generated(gens):
    seen, frontier = {E}, [E]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                b = mul(g, a)
                if b not in seen: seen.add(b); nxt.append(b)
        frontier = nxt
    return len(seen)

def triangle_vectors(a, b, c):
    n = 0
    for x in G:
        if ORD[x] != a: continue
        for y in G:
            if ORD[y] != b: continue
            z = inv(mul(x, y))
            if ORD[z] == c and generated([x, y]) == 120: n += 1
    return n

def quad_2222():
    invols = [p for p in G if ORD[p] == 2]
    n = 0
    for x1, x2, x3 in itertools.product(invols, repeat=3):
        x4 = inv(mul(x1, mul(x2, x3)))
        if ORD[x4] == 2 and generated([x1, x2, x3]) == 120: n += 1
    return n

def commuting_pairs_generating():
    return sum(1 for x in G for y in G if mul(x, y) == mul(y, x) and generated([x, y]) == 120)

counts = {
    "(0;2,3,6)": triangle_vectors(2, 3, 6),
    "(0;2,4,4)": triangle_vectors(2, 4, 4),
    "(0;3,3,3)": triangle_vectors(3, 3, 3),
    "(0;2,2,2,2)": quad_2222(),
    "(1;-)": commuting_pairs_generating(),
    "(0;2,4,5) Bring": triangle_vectors(2, 4, 5),
}
checks = {
    "no_euclidean_generating_vector": all(counts[k] == 0 for k in
        ["(0;2,3,6)", "(0;2,4,4)", "(0;3,3,3)", "(0;2,2,2,2)", "(1;-)"]),
    "bring_signature_realised": counts["(0;2,4,5) Bring"] > 0,
    "bring_vectors_form_aut_orbits": counts["(0;2,4,5) Bring"] % 120 == 0,
}
out = {"probe": "s5_strong_symmetric_genus_probe", "bean": "qou-qhcr",
       "arithmetic": "exact enumeration in S5", "generating_vector_counts": counts,
       "checks": checks, "passed": sum(checks.values()), "total": len(checks)}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s5-strong-symmetric-genus.witness.json")
with open(path, "w") as f: json.dump(out, f, indent=2); f.write("\n")
print(json.dumps(counts)); [print(("PASS " if v else "FAIL ") + k) for k, v in checks.items()]
raise SystemExit(0 if all(checks.values()) else 1)
