#!/usr/bin/env python3
"""A: can ANY element of the six-strand braid image give a charge-charge pair shift?
C: spectator distance d between the two nucleon blocks.

Pre-registration: np_charge_vertex_search_preregistration.md (committed before this file).
Exact Fraction arithmetic; A1 rank also checked modulo a large prime.
"""
from fractions import Fraction as Fr
import itertools, sys

def rmat(q):
    h = q - 1 / q
    return [[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]]

def rinv(q):
    h = q - 1 / q
    return [[1 / q, 0, 0, 0], [0, -h, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1 / q]]

class Space:
    def __init__(self, N, q):
        self.N, self.q = N, q
        self.R, self.Ri = rmat(q), rinv(q)
    def bits(self, s):
        return [(s >> (self.N - 1 - k)) & 1 for k in range(self.N)]
    def act(self, i, inv, v):
        """(σ_i^{±1} v) for sparse dict v."""
        R = self.Ri if inv else self.R
        N = self.N; out = {}
        for s, x in v.items():
            bi = (s >> (N - 1 - i)) & 1; bj = (s >> (N - 2 - i)) & 1
            col = 2 * bi + bj
            base = s & ~((1 << (N - 1 - i)) | (1 << (N - 2 - i)))
            for row in range(4):
                c = R[row][col]
                if c:
                    t = base | ((row >> 1) << (N - 1 - i)) | ((row & 1) << (N - 2 - i))
                    out[t] = out.get(t, 0) + c * x
        return {k: x for k, x in out.items() if x != 0}
    def word_on(self, w, v):
        for (i, inv) in reversed(w):
            v = self.act(i, inv, v)
        return v

def core(lo):
    return [(lo, False), (lo + 1, True)] * 3

def sector_traces(S, words, blkA, blkB):
    """For each word X: vector over sectors (Q_A, Q_B) of Tr(K^N Π V_A^3 V_B^3 X)."""
    N, q = S.N, S.q
    Vw = core(blkA) + core(blkB)
    res = []
    for X in words:
        W = Vw + X
        T = {}
        for s in range(2 ** N):
            d = S.word_on(W, {s: 1}).get(s, 0)
            if d == 0:
                continue
            b = S.bits(s)
            z = b.count(0)
            Kw = q ** z * (1 / q) ** (N - z)
            key = (b[blkA:blkA + 3].count(0) - 1, b[blkB:blkB + 3].count(0) - 1)
            T[key] = T.get(key, 0) + Kw * d
        res.append(T)
    return res

def rank_span(vectors):
    """Row-reduce list of Fraction vectors; return basis (echelon rows with pivots)."""
    rows = []
    piv = []
    for v in vectors:
        v = list(v)
        for r, p in zip(rows, piv):
            if v[p] != 0:
                f = v[p] / r[p]
                v = [a - f * b for a, b in zip(v, r)]
        nz = [k for k, x in enumerate(v) if x != 0]
        if nz:
            rows.append(v); piv.append(nz[0])
    return rows, piv

def in_span(rows, piv, v):
    v = list(v)
    for r, p in zip(rows, piv):
        if v[p] != 0:
            f = v[p] / r[p]
            v = [a - f * b for a, b in zip(v, r)]
    return all(x == 0 for x in v)

def perm_words(n):
    """A reduced word (positive letters) for each permutation of S_n, by BFS."""
    start = tuple(range(n)); seen = {start: []}; frontier = [start]
    while frontier:
        nxt = []
        for p in frontier:
            for i in range(n - 1):
                l = list(p); l[i], l[i + 1] = l[i + 1], l[i]; t = tuple(l)
                if t not in seen:
                    seen[t] = seen[p] + [(i, False)]; nxt.append(t)
        frontier = nxt
    return list(seen.values())

def part_A(q):
    print(f"\n===== A at q = {q} =====")
    S = Space(6, q)
    words = perm_words(6)
    trs = sector_traces(S, words, 0, 3)
    T1 = trs[0]  # empty word first
    assert words[0] == []
    keys = sorted(k for k, v in T1.items() if v != 0)
    print("sectors with T_1 ≠ 0:", len(keys))
    vecs = [[T.get(k, 0) for k in keys] for T in trs]
    rows, piv = rank_span(vecs)
    print("A2: dimension of the span of sector vectors over all 720 words:", len(rows), "of", len(keys))
    uT1 = [T1[k] for k in keys]
    uQ = [k[0] * k[1] * T1[k] for k in keys]
    uW = [(2 * k[0] - 1) * (2 * k[1] - 1) * T1[k] for k in keys]
    ua = [k[0] * T1[k] for k in keys]
    ub = [k[1] * T1[k] for k in keys]
    print("  T_1 in span:", in_span(rows, piv, uT1))
    print("  O1 Coulomb  (Q_aQ_b·T_1 in span):", in_span(rows, piv, uQ))
    print("  O2 isospin  (W_aW_b·T_1 in span):", in_span(rows, piv, uW))
    r2, p2 = rank_span([r for r in rows] + [ua, ub])
    print("  O3 affine-bilinear (Q_aQ_b·T_1 in span + Q_a·T_1 + Q_b·T_1):", in_span(r2, p2, uQ))
    # restricted to the four nucleon sectors only
    nk = [k for k in [(1, 1), (1, 0), (0, 1), (0, 0)] if k in keys]
    nidx = [keys.index(k) for k in nk]
    nrows, npiv = rank_span([[v[i] for i in nidx] for v in vecs])
    print("  nucleon sectors only: span dimension", len(nrows), "of", len(nk),
          "| O1:", in_span(nrows, npiv, [uQ[i] for i in nidx]),
          "| O2:", in_span(nrows, npiv, [uW[i] for i in nidx]))
    return len(rows), len(keys)

def part_A1(qnum, qden, p=2_147_483_647):
    """Dimension of the image of H_6 on (C^2)^6, as a rank modulo p."""
    q = qnum * pow(qden, -1, p) % p
    qi = pow(q, -1, p); h = (q - qi) % p
    R = [[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]]
    N = 6
    def act(i, v):
        out = [0] * 64
        for s in range(64):
            x = v[s]
            if not x: continue
            bi = (s >> (N - 1 - i)) & 1; bj = (s >> (N - 2 - i)) & 1
            base = s & ~((1 << (N - 1 - i)) | (1 << (N - 2 - i)))
            for row in range(4):
                c = R[row][2 * bi + bj]
                if c:
                    t = base | ((row >> 1) << (N - 1 - i)) | ((row & 1) << (N - 2 - i))
                    out[t] = (out[t] + c * x) % p
        return out
    mats = []
    for w in perm_words(6):
        cols = []
        for s in range(64):
            v = [0] * 64; v[s] = 1
            for (i, _) in reversed(w):
                v = act(i, v)
            cols.extend(v)
        mats.append(cols)
    # rank mod p
    rows = []; piv = []
    for v in mats:
        v = v[:]
        for r, pc in zip(rows, piv):
            if v[pc]:
                f = v[pc] * pow(r[pc], -1, p) % p
                v = [(a - f * b) % p for a, b in zip(v, r)]
        nz = next((k for k, x in enumerate(v) if x), None)
        if nz is not None:
            rows.append(v); piv.append(nz)
    print(f"A1: dim of image of H_6 on (C^2)^6 at q = {qnum}/{qden} (rank mod {p}): {len(rows)}")

def band(d):
    """X_d = (σ_2…σ_{1+d}) σ_{2+d} (σ_2…σ_{1+d})^{-1}."""
    up = [(2 + k, False) for k in range(d)]
    down = [(2 + k, True) for k in reversed(range(d))]
    return up + [(2 + d, False)] + down

def part_C(q, dmax):
    print(f"\n===== C at q = {q} =====")
    for d in range(dmax + 1):
        S = Space(6 + d, q)
        T1, TX = sector_traces(S, [[], band(d)], 0, 3 + d)
        dE = {k: TX.get(k, 0) / T1[k] for k in [(1, 1), (1, 0), (0, 1), (0, 0)]}
        pp, pn, np_, nn = dE[(1, 1)], dE[(1, 0)], dE[(0, 1)], dE[(0, 0)]
        I = pp - pn - np_ + nn
        print(f"d={d}: pp={float(pp):.10f} pn={float(pn):.10f} np={float(np_):.10f} nn={float(nn):.10f} "
              f"I={float(I):.10e} pp-nn={float(pp-nn):.10e} pn-np={float(pn-np_):.10e}")
        print(f"      exact I = {I}")
        sys.stdout.flush()

if __name__ == "__main__":
    part_A1(111, 100)
    part_A1(7, 5)
    for q in (Fr(111, 100), Fr(7, 5)):
        part_A(q)
    dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    for q in (Fr(111, 100), Fr(7, 5)):
        part_C(q, dmax)
