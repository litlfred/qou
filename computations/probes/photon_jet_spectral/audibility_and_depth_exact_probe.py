#!/usr/bin/env python3
"""Audit §14. Exact (no float) checks:
 A. The Markov trace form B(x,y) = tr_M(xy) on H3(q): its determinant as a function of z, and its
    radical at convention D. The k-photon responses determine x modulo this radical (since
    products of photons span H3), so the radical is the exact "inaudible part" of a state.
 B. n = 4: F_3 != H_4 for every q, by an explicit annihilator over Q(q) checked symbolically on
    every product of at most 3 photons; F_4 = H_4 by full rank at a rational q.
 C. n = 5: ranks of F_k in exact rational arithmetic (Fraction) at q = 7/5 and 11/3.
Never reads q0."""
import itertools, json
from fractions import Fraction as Fr
from pathlib import Path
import sympy as sp

out = {'q0Anchor': 'independent', 'q0AnchorReason': 'symbolic or exact rational q; never reads q0'}
q, z = sp.symbols('q z')
h = q - 1/q

def length(w): return sum(1 for i in range(len(w)) for j in range(i+1, len(w)) if w[i] > w[j])
def hecke(n, hval, zero, one):
    W = list(itertools.permutations(range(n))); idx = {w: i for i, w in enumerate(W)}; L = [length(w) for w in W]
    def rmul_s(vec, s):
        outv = [zero]*len(W)
        for j, c in enumerate(vec):
            if c == 0: continue
            w = list(W[j]); w[s], w[s+1] = w[s+1], w[s]; k = idx[tuple(w)]
            if L[k] > L[j]: outv[k] += c
            else: outv[j] += hval*c; outv[k] += c
        return outv
    def rmul_sinv(vec, s): return [a - hval*b for a, b in zip(rmul_s(vec, s), vec)]
    gens = [('s', i) for i in range(n-1)] + [('V', i) for i in range(n-2)]
    def rmul(vec, g): return rmul_s(vec, g[1]) if g[0] == 's' else rmul_sinv(rmul_s(vec, g[1]), g[1]+1)
    e = [zero]*len(W); e[idx[tuple(range(n))]] = one
    return W, idx, L, gens, rmul, e

# ---- A. trace form on H3
W3, idx3, L3, gens3, rmul3, e3 = hecke(3, h, sp.Integer(0), sp.Integer(1))
basis = []
for w in W3:  # T_w as vector: product of simple letters of a reduced word, via right multiplication from e
    pass
# reduced words for the 6 permutations of S3 (right multiplication builds T_w)
words = {(0,1,2): [], (1,0,2): [0], (0,2,1): [1]}
for w in W3:
    if w not in words:
        # find by BFS
        pass
def build_words(n):
    W = list(itertools.permutations(range(n))); ws = {tuple(range(n)): []}; frontier = [tuple(range(n))]
    while frontier:
        nf = []
        for w in frontier:
            for s in range(n-1):
                v = list(w); v[s], v[s+1] = v[s+1], v[s]; v = tuple(v)
                if v not in ws and length(v) == length(w) + 1: ws[v] = ws[w] + [s]; nf.append(v)
        frontier = nf
    return ws
ws3 = build_words(3)
def Tvec(w):
    v = list(e3)
    for s in ws3[w]: v = rmul3(v, ('s', s))
    return [sp.expand(x) for x in v]
Tv = {w: Tvec(w) for w in W3}
def mult(x, y):  # x*y for x, y vectors: x * T_w = x * (letters)
    res = [sp.Integer(0)]*6
    for w, c in zip(W3, y):
        if c == 0: continue
        v = list(x)
        for s in ws3[w]: v = rmul3(v, ('s', s))
        res = [a + c*b for a, b in zip(res, v)]
    return [sp.expand(a) for a in res]
def trM(x):  # Ocneanu: tr(T_w) by number of letters per class: e:1, length1: z, length2: z^2, w0: (hz+1)z
    val = {0: 1, 1: z, 2: z**2, 3: (h*z + 1)*z}
    return sp.expand(sum(c*val[L3[i]] for i, c in enumerate(x)))
B = sp.Matrix(6, 6, lambda i, j: trM(mult(Tv[W3[i]], Tv[W3[j]])))
detB = sp.factor(B.det())
zD = q**3/(q**2 + 1)
BD = B.subs(z, zD).applyfunc(sp.simplify)
rad = BD.nullspace(simplify=True)
out['A_det_trace_form'] = str(detB)
out['A_rank_at_zD'] = int(BD.rank(simplify=True))
out['A_radical_dim_at_zD'] = len(rad)
r = rad[0] / rad[0][0] if rad and rad[0][0] != 0 else (rad[0] if rad else None)
out['A_radical_vector'] = [str(sp.factor(c)) for c in r] if r is not None else None
# antisymmetriser check: sum (-q^{-1})^{l(w)} T_w ... compare up to scale
anti = [(-1/q)**L3[i] for i in range(6)]
out['A_radical_is_sign_idempotent_direction'] = bool(sp.simplify(sp.Matrix(r).cross if False else sp.Matrix(anti) - sp.Matrix(r)) == sp.zeros(6, 1)) if r is not None else None
print('A det', detB, '| rank at zD', out['A_rank_at_zD'], '| radical', out['A_radical_vector'], out['A_radical_is_sign_idempotent_direction'], flush=True)

# ---- B. n = 4 exact generic F_3 != H_4
def fr_rank_basis(n, qv, kmax):
    hv = qv - 1/qv
    W, idx, L, gens, rmul, e = hecke(n, hv, Fr(0), Fr(1))
    N = len(W); piv = {}; chosen = []
    def insert(v, word):
        v = list(v)
        for c, (row, _) in piv.items():
            if v[c] != 0:
                f = v[c]; v = [a - f*b for a, b in zip(v, row)]
        nz = [i for i, a in enumerate(v) if a != 0]
        if not nz: return False
        c = nz[0]; inv = 1/v[c]; v = [a*inv for a in v]
        for c2 in list(piv):
            row, w2 = piv[c2]
            if row[c] != 0:
                f = row[c]; piv[c2] = ([a - f*b for a, b in zip(row, v)], w2)
        piv[c] = (v, word); chosen.append(word); return True
    insert(e, ()); frontier = [(e, ())]; ranks = [1]
    for k in range(1, kmax+1):
        new = []
        for x, word in frontier:
            for g in gens:
                y = rmul(x, g)
                if insert(y, word + (g,)): new.append((y, word + (g,)))
        ranks.append(len(piv)); frontier = new
        if len(piv) == N: break
    return ranks, chosen
ranks4, chosen4 = fr_rank_basis(4, Fr(7, 5), 4)
out['B_n4_ranks_at_q=7/5'] = ranks4
# symbolic vectors of the words chosen up to k=3
W4, idx4, L4, gens4, rmul4, e4 = hecke(4, h, sp.Integer(0), sp.Integer(1))
def symvec(word):
    v = list(e4)
    for g in word: v = [sp.expand(a) for a in rmul4(v, g)]
    return v
chosen3 = [w for w in chosen4 if len(w) <= 3]
M = sp.Matrix([symvec(w) for w in chosen3])          # 22 x 24
ann = M.nullspace(simplify=True)                       # vectors a with M a = 0
out['B_n4_dim_F3_chosen'] = len(chosen3); out['B_n4_annihilator_dim'] = len(ann)
# verify the annihilator kills EVERY product of at most 3 generators (symbolic, exact)
allwords = [()] + [w for k in range(1, 4) for w in itertools.product(gens4, repeat=k)]
bad = 0
for wd in allwords:
    v = sp.Matrix([symvec(wd)])
    for a in ann:
        if sp.simplify((v*a)[0]) != 0: bad += 1
out['B_n4_products_checked'] = len(allwords); out['B_n4_annihilator_failures'] = bad
print('B n=4 ranks', ranks4, '| annihilator dim', len(ann), '| products checked', len(allwords), 'failures', bad, flush=True)

# ---- C. n = 5 exact rational ranks
for qv in (Fr(7, 5), Fr(11, 3)):
    r5, _ = fr_rank_basis(5, qv, 7)
    out[f'C_n5_ranks_at_q={qv}'] = r5
    print('C n=5 q', qv, r5, flush=True)
Path(__file__).with_name('audibility-and-depth-exact.witness.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
