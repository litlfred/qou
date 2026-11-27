#!/usr/bin/env python3
"""Photon stopping depth L(n): least k with F_k = H_n(q), F_k = span of products of at most k
sliding photons (generators s_i, s_{i+1}, s_i s_{i+1}^{-1}). Audit §12, predictions P14-P17.

Arithmetic: exact, in Z/p for large primes p, at q a random unit mod p (q^2 != -1).
Full rank mod p certifies full rank over Q(q) (rank cannot rise under reduction), so
"F_k = H_n" is certified exactly. "F_k != H_n" mod p at a random point is probabilistic
(Schwartz-Zippel); it is reported per (p, q) so agreement across runs can be read off.
Never reads q0."""
import itertools, json, random
from pathlib import Path
import numpy as np

def length(w):
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])

def run(n, p, qv):
    W = list(itertools.permutations(range(n))); idx = {w: i for i, w in enumerate(W)}
    N = len(W); L = [length(w) for w in W]
    hq = (qv - pow(qv, p - 2, p)) % p
    def rmul_s(vec, s):  # vec * T_s (right multiplication)
        out = np.zeros(N, dtype=np.int64)
        for j in np.nonzero(vec)[0]:
            w = W[j]; ws = list(w); ws[s], ws[s + 1] = ws[s + 1], ws[s]; ws = tuple(ws); k = idx[ws]
            c = int(vec[j])
            if L[k] > L[j]: out[k] = (out[k] + c) % p
            else: out[j] = (out[j] + hq * c) % p; out[k] = (out[k] + c) % p
        return out
    def rmul_sinv(vec, s):  # T_s^{-1} = T_s - h
        return (rmul_s(vec, s) - hq * vec) % p
    gens = []
    for i in range(n - 1): gens.append(('s', i))
    for i in range(n - 2): gens.append(('V', i))
    def rmul(vec, g):
        if g[0] == 's': return rmul_s(vec, g[1])
        return rmul_sinv(rmul_s(vec, g[1]), g[1] + 1)   # vec * s_i * s_{i+1}^{-1}
    # incremental echelon basis mod p
    piv = {}  # pivot col -> row vector (normalised)
    def insert(v):
        v = v.copy() % p
        for c, r in piv.items():
            if v[c]: v = (v - v[c] * r) % p
        nz = np.nonzero(v)[0]
        if len(nz) == 0: return False
        c = nz[0]; inv = pow(int(v[c]), p - 2, p); v = (v * inv) % p
        for c2 in list(piv):
            r = piv[c2]
            if r[c]: piv[c2] = (r - r[c] * v) % p
        piv[c] = v; return True
    e = np.zeros(N, dtype=np.int64); e[idx[tuple(range(n))]] = 1
    insert(e); frontier = [e]; ranks = [1]
    for k in range(1, 40):
        new = []
        for x in frontier:
            for g in gens:
                y = rmul(x, g)
                if insert(y): new.append(y)
        ranks.append(len(piv)); frontier = new
        if len(piv) == N or not new: break
    return ranks

out = {'q0Anchor': 'independent', 'q0AnchorReason': 'modular exact arithmetic at random q; never reads q0', 'runs': []}
random.seed(20261125)
for n in (3, 4, 5, 6):
    for p in (2147483629, 2147483587):
        qv = random.randrange(2, p - 1)
        r = run(n, p, qv)
        N = n * (n - 1) // 2
        Ln = len(r) - 1 if r[-1] == len(list(itertools.permutations(range(n)))) else None
        rec = {'n': n, 'p': p, 'q': qv, 'ranks': r, 'L': Ln, 'lower_ceil_N_over_2': -(-N // 2), 'upper_floor_n2_over_4': n * n // 4}
        out['runs'].append(rec); print(rec, flush=True)
Path(__file__).with_name('photon-stopping-depth.witness.json').write_text(json.dumps(out, indent=1))
