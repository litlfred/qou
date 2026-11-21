#!/usr/bin/env python3
"""Kauffman bracket of a braid closure via the Temperley-Lieb algebra (Catalan(n) basis).
Polynomials in A are dicts {exponent: int}; exact integer arithmetic."""
from collections import defaultdict

def compose(D1, D2, n):
    par = {}
    def f(x):
        par.setdefault(x, x)
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    def u(a, b): par[f(a)] = f(b)
    for k in range(2 * n):
        u((1, k), (1, D1[k])); u((2, k), (2, D2[k]))
    for j in range(n):
        u((1, n + j), (2, j))
    ext = [(1, k) for k in range(n)] + [(2, n + k) for k in range(n)]
    lab = {x: i for i, x in enumerate(ext)}  # external index: 0..n-1 top, n..2n-1 bottom
    groups = defaultdict(list)
    for x in list(par) + ext:
        groups[f(x)].append(x)
    res = [None] * (2 * n); loops = 0
    for g in groups.values():
        e = [lab[x] for x in set(g) if x in lab]
        if not e:
            loops += 1
        else:
            a, b = e; res[a] = b; res[b] = a
    return tuple(res), loops

def ident(n): return tuple(list(range(n, 2 * n)) + list(range(n)))
def egen(i, n):
    D = list(ident(n)); D[i], D[i + 1] = i + 1, i; D[n + i], D[n + i + 1] = n + i + 1, n + i
    return tuple(D)

def padd(p, q, s=1):
    r = defaultdict(int, p)
    for k, v in q.items(): r[k] += s * v
    return {k: v for k, v in r.items() if v}
def pmul(p, q):
    r = defaultdict(int)
    for a, x in p.items():
        for b, y in q.items(): r[a + b] += x * y
    return {k: v for k, v in r.items() if v}
D_LOOP = {2: -1, -2: -1}
def ppow(p, k):
    r = {0: 1}
    for _ in range(k): r = pmul(r, p)
    return r

def bracket(word, n):
    """<closure>, normalised so the unknot gives 1 (empty diagram of n loops -> d^{n-1})."""
    state = {ident(n): {0: 1}}
    for g, s in word:
        E = egen(g, n); new = defaultdict(dict)
        for D, c in state.items():
            # sigma = A*id + A^-1*e  (positive);  sigma^-1 = A^-1*id + A*e
            a_id, a_e = (1, -1) if s > 0 else (-1, 1)
            new[D] = padd(new[D], pmul(c, {a_id: 1}))
            D2, L = compose(D, E, n)
            new[D2] = padd(new[D2], pmul(c, pmul({a_e: 1}, ppow(D_LOOP, L))))
        state = {D: c for D, c in new.items() if c}
    tot = {}
    for D, c in state.items():
        loops = closure_loops(D, n)
        tot = padd(tot, pmul(c, ppow(D_LOOP, loops - 1)))
    return tot

def closure_loops(D, n):
    par = list(range(2 * n))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for k in range(2 * n): par[f(k)] = f(D[k])
    for j in range(n): par[f(j)] = f(n + j)
    return len({f(k) for k in range(2 * n)})
