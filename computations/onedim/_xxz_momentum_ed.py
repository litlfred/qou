#!/usr/bin/env python3
"""Momentum-resolved ED of the XXZ chain: MEASURE the m-magnon bound-state
band instead of quoting a formula.

Self-check built in: the union of the momentum-block spectra must equal the
full-sector spectrum. If that fails the symmetrisation is wrong and no result
below is trustworthy.
"""
from itertools import combinations
from mpmath import mp, mpf, mpc, matrix, exp, pi, cos, cosh, log, nstr, eig, sqrt

mp.dps = 30

def sectors(N, m):
    return list(combinations(range(N), m))

def transl(s, N):
    return tuple(sorted(((i + 1) % N) for i in s))

def orbit_data(N, m):
    """rep -> period; and state -> (rep, shift)."""
    reps, info = [], {}
    for s in sectors(N, m):
        if s in info:
            continue
        orb, t, j = [], s, 0
        while True:
            orb.append(t); t = transl(t, N); j += 1
            if t == s: break
        P = j
        rep = min(orb)
        ri = orb.index(rep)
        for idx, st in enumerate(orb):
            info[st] = (rep, (idx - ri) % P, P)
        reps.append((rep, P))
    return sorted(set(reps)), info

def H_terms(s, N, Delta):
    """Apply H = sum_i (sx sx + sy sy + Delta sz sz) to |s>; yield (coef, state)."""
    down = set(s)
    dz = 0
    for i in range(N):
        j = (i + 1) % N
        dz += (-1 if i in down else 1) * (-1 if j in down else 1)
    yield (Delta * dz, s)
    for i in list(down):
        for j in ((i + 1) % N, (i - 1) % N):
            if j not in down:
                yield (mpf(2), tuple(sorted(down - {i} | {j})))

def block(N, m, r, Delta, reps, info):
    """Momentum-r block in the translation-symmetrised basis."""
    basis = [(rep, P) for rep, P in reps if (r * P) % N == 0]
    idx = {rep: a for a, (rep, P) in enumerate(basis)}
    per = {rep: P for rep, P in basis}
    D = len(basis)
    H = matrix(D, D)
    k = 2 * pi * mpf(r) / N
    for a, (rep, P) in enumerate(basis):
        for coef, s2 in H_terms(rep, N, Delta):
            rep2, shift, P2 = info[s2]
            if rep2 not in idx:
                continue
            b = idx[rep2]
            amp = coef * exp(mpc(0, 1) * k * shift) * sqrt(mpf(P) / P2)
            H[b, a] = H[b, a] + amp
    return H, D

def spectrum(H):
    if H.rows == 0:
        return []
    return sorted(mp.re(v) for v in eig(H, left=False, right=False))

def run(N, m, Delta, label):
    reps, info = orbit_data(N, m)
    Evac = Delta * N
    bands = {}
    allv = []
    for r in range(N):
        H, D = block(N, m, r, Delta, reps, info)
        sp = spectrum(H)
        bands[r] = [v - Evac for v in sp]
        allv += sp
    # SELF-CHECK: union of blocks == full sector spectrum
    full = matrix(len(sectors(N, m)), len(sectors(N, m)))
    st = sectors(N, m); ix = {s: a for a, s in enumerate(st)}
    for s in st:
        for coef, s2 in H_terms(s, N, Delta):
            full[ix[s2], ix[s]] = full[ix[s2], ix[s]] + coef
    fsp = spectrum(full)
    ok = len(fsp) == len(allv) and max(abs(a - b) for a, b in
                                       zip(sorted(allv), sorted(fsp))) < mpf('1e-18')
    print(f"  [{'PASS' if ok else 'FAIL'}] self-check: blocks == full sector "
          f"({len(allv)} vs {len(fsp)} eigenvalues)")
    if not ok:
        return None
    print(f"  {label}: N={N} m={m} Delta={nstr(Delta,12)}")
    print("    r   lowest (E-Evac)   2nd        gap to 2nd")
    for r in range(N):
        b = sorted(bands[r])
        if len(b) >= 2:
            print(f"   {r:2d}   {nstr(b[0],10):>13} {nstr(b[1],10):>11}"
                  f"   {nstr(b[1]-b[0],8):>11}")
    return bands
