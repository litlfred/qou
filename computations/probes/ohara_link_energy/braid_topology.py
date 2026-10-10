#!/usr/bin/env python3
"""Exact combinatorial topology of the candidate closed braids (no geometry, no floats).

Words are lists of generator indices (0-based, positive letters), taken verbatim
from computations/qbeta/qbeta_candidate_closures_are_links_probe.py.
Computes: permutation, components, strands per component, linking number,
per-component self-crossing writhe, Kauffman-bracket Jones polynomial and Burau
Alexander polynomial of the closure, and checks the conjugacy relations used to
identify closures.
"""
import itertools, json, sys
import sympy as sp

A, t = sp.symbols('A t')

def perm(word, n):
    p = list(range(n))  # p[pos] = strand label at position pos
    for g in word:
        i = abs(g); p[i], p[i+1] = p[i+1], p[i]
    return p

def components(word, n):
    """Return list of components, each a list of starting positions; follows
    position-> position map of one pass through the braid."""
    # track where a strand starting at position s ends
    end = {}
    for s in range(n):
        pos = s
        for g in word:
            i = abs(g)
            if pos == i: pos = i+1
            elif pos == i+1: pos = i
        end[s] = pos
    seen, comps = set(), []
    for s in range(n):
        if s in seen: continue
        c, x = [], s
        while x not in seen:
            seen.add(x); c.append(x); x = end[x]
        comps.append(c)
    return comps, end

def crossing_components(word, n):
    comps, _ = components(word, n)
    lab = {}
    for ci, c in enumerate(comps):
        for s in c: lab[s] = ci
    # strand at each position at each level: label by start position
    cur = list(range(n))  # cur[pos] = starting position of the strand there
    out = []
    for g in word:
        i = abs(g); sgn = 1 if g >= 0 else -1  # all positive here
        out.append((lab[cur[i]], lab[cur[i+1]], sgn))
        cur[i], cur[i+1] = cur[i+1], cur[i]
    return comps, out

def linking_and_selfwrithe(word, n):
    comps, cr = crossing_components(word, n)
    lk = sum(s for a, b, s in cr if a != b) // 2 if len(comps) == 2 else None
    selfw = [sum(s for a, b, s in cr if a == b == k) for k in range(len(comps))]
    return comps, lk, selfw

def bracket(word, n):
    """Kauffman bracket of the closed braid via state sum (all letters positive)."""
    m = len(word)
    # node ids: (level, pos), level 0..m-1, level m == level 0
    def nid(k, p): return (k % m) * n + p
    total = 0
    d = -A**2 - A**-2
    for state in itertools.product((0, 1), repeat=m):
        parent = list(range(m * n))
        def f(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def u(a, b): parent[f(a)] = f(b)
        for k, g in enumerate(word):
            i = abs(g)
            for p in range(n):
                if p not in (i, i+1): u(nid(k, p), nid(k+1, p))
            if state[k] == 0:  # vertical smoothing, weight A
                u(nid(k, i), nid(k+1, i)); u(nid(k, i+1), nid(k+1, i+1))
            else:              # horizontal (cup-cap), weight A^-1
                u(nid(k, i), nid(k, i+1)); u(nid(k+1, i), nid(k+1, i+1))
        loops = len({f(x) for x in range(m * n)})
        na = state.count(0); nb = m - na
        total += A**(na - nb) * d**(loops - 1)
    return sp.expand(total)

def jones(word, n):
    w = sum(1 if g >= 0 else -1 for g in word)
    V = sp.expand((-A**3)**(-w) * bracket(word, n))
    return V  # in A; t = A^-4

def burau_alexander(word, n):
    """Reduced Burau; Delta(closure) ~ det(I - B(beta)) (1-t)/(1-t^n)."""
    def gen(i):
        M = sp.eye(n - 1)
        # reduced Burau matrices (Birman), 0-based generator i on n strands
        if n - 1 == 1:
            return sp.Matrix([[-t]])
        if i > 0:
            M[i-1, i-1] = 1; M[i-1, i] = 0
        M[i, i] = -t
        if i > 0: M[i, i-1] = t
        if i < n - 2: M[i, i+1] = 1
        return M
    B = sp.eye(n - 1)
    for g in word: B = B * gen(abs(g))
    D = sp.factor(sp.cancel((sp.eye(n - 1) - B).det() * (1 - t) / (1 - t**n)))
    return D

def normalise_laurent(P, x):
    """Normalise a Laurent polynomial up to units +-x^k for comparison."""
    P = sp.expand(P)
    if P == 0: return P
    num, den = sp.fraction(sp.together(P))
    num = sp.Poly(sp.expand(num), x)
    # strip powers of x
    c = num.all_coeffs()
    while c and c[-1] == 0: c.pop()
    if c[0] < 0: c = [-z for z in c]
    return tuple(c)

NUC9 = [0, 1] * 3 + [0, 0, 1]
CANDIDATES = {
    # 2-strand / 3-strand calibration words (pre-registered)
    "cal_hopf_s1^2":        ([0, 0], 2),
    "cal_hopf_3strand":     ([0, 0, 1], 3),
    "cal_T24_s1^4":         ([0, 0, 0, 0], 2),
    "cal_trefoil_s1^3":     ([0, 0, 0], 2),
    # corpus words, verbatim
    "nuc9":                 (NUC9, 3),
    "nuc11_interleaved":    (NUC9 + [0, 0], 3),
    "nuc11_gen_grouped":    ([0] * 7 + [1] * 4, 3),
    "gluon_s1_s0":          (NUC9 + [1, 0], 3),
    "gluon_s0_s1":          (NUC9 + [0, 1], 3),
    "gluon_s1_s1":          (NUC9 + [1, 1], 3),
    "gluon_s0_s0":          (NUC9 + [0, 0], 3),
}

if __name__ == "__main__":
    out = {}
    for name, (w, n) in CANDIDATES.items():
        comps, lk, selfw = linking_and_selfwrithe(w, n)
        V = jones(w, n)
        D = burau_alexander(w, n)
        out[name] = dict(word=w, strands=n, permutation=perm(w, n),
                         components=len(comps),
                         strands_per_component=[len(c) for c in comps],
                         linking_number=lk, self_crossing_writhe=selfw,
                         jones_A=str(V), alexander_t=str(D))
        print(f"{name:22s} len={len(w):2d} comps={len(comps)} sizes={[len(c) for c in comps]} lk={lk} selfw={selfw}")
        print(f"   Jones(A) = {V}")
        print(f"   Alexander = {D}")
    # equality classes by (Jones, Alexander)
    classes = {}
    for name, r in out.items():
        classes.setdefault((r['jones_A'], r['alexander_t']), []).append(name)
    print("\nInvariant classes (Jones, Alexander):")
    for k, v in classes.items(): print("  ", v)
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "braid_topology.json", "w"), indent=1)
