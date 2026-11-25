#!/usr/bin/env python3
"""(a) Gassmann (almost-conjugate, non-conjugate) subgroup pairs in S5 = Aut(Bring).
(b) photon filtration ranks F_k in H_4(q) with sliding photons (owner ruling 2026-11-22):
    W_4 = span{s_i, s_{i+1}, s_i s_{i+1}^{-1} : i=0,1}. Exact, q specialised to a rational
    generic value 7/5 for the rank count (rank over Q(q) >= rank at a specialisation; we also
    check a second value 11/3). Pure integer/rational arithmetic, no floats."""
import itertools, json
from fractions import Fraction as Fr
from pathlib import Path

# ---------- (a) S5 ----------
n = 5
def mul(a, b): return tuple(a[b[i]] for i in range(n))
def inv(a):
    r = [0]*n
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
G = list(itertools.permutations(range(n)))
def closure(gens):
    e = tuple(range(n)); S = {e}; fr = [e]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                y = mul(x, g)
                if y not in S: S.add(y); nf.append(y)
        fr = nf
    return frozenset(S)
subs = set()
for a in G:
    for b in G:
        subs.add(closure([a, b]))
def ctype(p):
    seen = set(); t = []
    for i in range(n):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        t.append(L)
    return tuple(sorted(t))
def profile(H):
    d = {}
    for h in H: d[ctype(h)] = d.get(ctype(h), 0) + 1
    return tuple(sorted(d.items()))
def conj(H, g): return frozenset(mul(mul(g, h), inv(g)) for h in H)
classes = []
for H in subs:
    if not any(H in c for c in classes):
        classes.append({conj(H, g) for g in G})
reps = [next(iter(c)) for c in classes]
by_prof = {}
for H in reps: by_prof.setdefault((len(H), profile(H)), []).append(H)
gassmann = [k for k, v in by_prof.items() if len(v) > 1]
out = {'q0Anchor': 'independent', 'q0AnchorReason': 'symbolic in q over Q(q) or at rational q; never reads the substrate q0', 'S5_subgroups': len(subs), 'S5_conj_classes_of_subgroups': len(reps),
       'S5_gassmann_pairs': len(gassmann), 'S5_gassmann_profiles': [str(k) for k in gassmann]}
print(out)

# ---------- (b) H_4 regular rep, sliding photons ----------
def h4_ranks(qv):
    m = 4
    W = list(itertools.permutations(range(m)))
    def length(w): return sum(1 for i in range(m) for j in range(i+1, m) if w[i] > w[j])
    def smul(i, w):  # s_i * w (left, act on positions values) : left mult swaps values i,i+1
        ww = list(w); a, b = ww.index(i), ww.index(i+1); ww[a], ww[b] = ww[b], ww[a]; return tuple(ww)
    idx = {w: k for k, w in enumerate(W)}; N = len(W); hq = qv - 1/qv
    def Lmat(i):
        M = [[Fr(0)]*N for _ in range(N)]
        for w in W:
            sw = smul(i, w); j = idx[w]
            if length(sw) > length(w): M[idx[sw]][j] += 1
            else: M[j][j] += hq; M[idx[sw]][j] += 1
        return M
    def mm(A, B): return [[sum(A[i][k]*B[k][j] for k in range(N) if A[i][k]) for j in range(N)] for i in range(N)]
    def add(A, B, c=Fr(1)): return [[A[i][j] + c*B[i][j] for j in range(N)] for i in range(N)]
    I = [[Fr(int(i == j)) for j in range(N)] for i in range(N)]
    S = [Lmat(i) for i in range(m-1)]
    Sinv = [add(s, I, -hq) for s in S]
    gens = []
    for i in range(m-2): gens += [S[i], S[i+1], mm(S[i], Sinv[i+1])]
    def col(M): return [M[r][idx[tuple(range(m))]] for r in range(N)]
    def rank(vs):
        A = [list(v) for v in vs]; r = 0; cols = N
        for c in range(cols):
            p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
            if p is None: continue
            A[r], A[p] = A[p], A[r]
            for i in range(len(A)):
                if i != r and A[i][c] != 0:
                    f = A[i][c]/A[r][c]; A[i] = [x - f*y for x, y in zip(A[i], A[r])]
            r += 1
        return r
    layer = [I]; allv = [col(I)]; ranks = [1]
    for k in range(1, 8):
        layer = [mm(x, g) for x in layer for g in gens]
        # prune layer to independent set to keep it small
        keep = []; basis = list(allv)
        for x in layer:
            if rank(basis + [col(x)]) > len(basis): basis.append(col(x)); keep.append(x)
        layer = keep if keep else layer[:0]
        allv = basis; ranks.append(len(allv))
        if len(allv) == N or not keep: break
    return ranks
for qv in (Fr(7, 5), Fr(11, 3)):
    out[f'H4_photon_filtration_ranks_q={qv}'] = h4_ranks(qv)
    print(qv, out[f'H4_photon_filtration_ranks_q={qv}'])
Path(__file__).with_name('s5-gassmann-h4-filtration.witness.json').write_text(json.dumps(out, indent=1))
