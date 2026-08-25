"""Compute the Gram matrix of STANDARD polytabloids in M^mu with tabloids orthonormal.
Tests the claim `specht_gram_orthogonal`: <e_S, e_T> = 0 for standard S != T.
"""
from itertools import permutations
from collections import defaultdict

def partitions(n):
    def go(n, mx):
        if n == 0: yield ()
        for k in range(min(n, mx), 0, -1):
            for rest in go(n-k, k): yield (k,)+rest
    return list(go(n, n))

def cells(mu):
    return [(i,j) for i,r in enumerate(mu) for j in range(r)]

def tableaux(mu):
    """All bijective fillings cells -> 1..n, as dict cell->label."""
    cs = cells(mu); n = len(cs)
    for p in permutations(range(1, n+1)):
        yield dict(zip(cs, p))

def is_standard(mu, T):
    for (i,j),v in T.items():
        if (i,j+1) in T and T[(i,j+1)] < v: return False
        if (i+1,j) in T and T[(i+1,j)] < v: return False
    return True

def tabloid(mu, T):
    """Row-equivalence class: tuple of frozensets of row contents."""
    rows = defaultdict(set)
    for (i,j),v in T.items(): rows[i].add(v)
    return tuple(frozenset(rows[i]) for i in range(len(mu)))

def col_stab(mu, T):
    """Permutations of labels preserving each column setwise (as label->label maps)."""
    colsets = defaultdict(list)
    for (i,j),v in T.items(): colsets[j].append(v)
    cols = [sorted(colsets[j]) for j in sorted(colsets)]
    # cartesian product of per-column permutations
    out = [({}, 1)]
    for c in cols:
        new = []
        for perm in permutations(c):
            # sign of this column permutation
            sgn = 1
            lst = list(perm); ref = list(c)
            idx = [ref.index(x) for x in lst]
            # count inversions
            inv = sum(1 for a in range(len(idx)) for b in range(a+1,len(idx)) if idx[a]>idx[b])
            sgn = (-1)**inv
            for base, bs in out:
                d = dict(base); d.update(dict(zip(c, perm))); new.append((d, bs*sgn))
        out = new
    return out

def polytabloid(mu, T):
    """e_T as dict tabloid -> coeff."""
    vec = defaultdict(int)
    for pi, sgn in col_stab(mu, T):
        # apply pi to labels of T
        T2 = {c: pi.get(v, v) for c,v in T.items()}
        vec[tabloid(mu, T2)] += sgn
    return {k:v for k,v in vec.items() if v != 0}

def inner(u, v):
    return sum(c*v.get(k,0) for k,c in u.items())

for n in range(2, 6):
    for mu in partitions(n):
        if len(mu) == 1 or mu == tuple([1]*n):
            pass  # still include, cheap
        syt = [T for T in tableaux(mu) if is_standard(mu, T)]
        if len(syt) < 2: continue
        polys = [polytabloid(mu, T) for T in syt]
        G = [[inner(polys[a], polys[b]) for b in range(len(syt))] for a in range(len(syt))]
        offdiag = [G[a][b] for a in range(len(G)) for b in range(len(G)) if a!=b]
        nz = [x for x in offdiag if x != 0]
        print(f"mu={mu}  #SYT={len(syt)}  diag={[G[a][a] for a in range(len(G))]}  nonzero_offdiag={len(nz)}/{len(offdiag)}")
        if nz and n <= 4:
            for row in G: print("     ", row)
