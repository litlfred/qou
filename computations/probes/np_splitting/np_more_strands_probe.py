#!/usr/bin/env python3
"""Reachable pair terms between two nucleon blocks on N > 6 strands, exact at fixed rational q.

Pre-registration: np_more_strands_preregistration.md (committed before this file was run).
Readout as in np_all_q_symbolic_probe.py, with spectator strands summed over in the sector
projector. Arithmetic is python-flint fmpq (exact rationals); no float enters any computation.
Results are exact at the q they are computed at; they are not identities in q.

Run from the repo root:
  python3 -u computations/probes/np_splitting/np_more_strands_probe.py [layout] [p/q]
layout in {L7s, L7e, L8s, L6} (default: all of L6, L7s, L7e at q = 111/100 and 7/5).
"""
import os
import sys
import time

import flint

T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


LAYOUTS = {
    "L6": (6, (0, 1, 2), (3, 4, 5)),
    "L7s": (7, (0, 1, 2), (4, 5, 6)),
    "L7e": (7, (0, 1, 2), (3, 4, 5)),
    "L8s": (8, (0, 1, 2), (5, 6, 7)),
}


def run(layout, q):
    N, A, B = LAYOUTS[layout]
    Dim = 2 ** N
    ONE, ZERO = flint.fmpq(1), flint.fmpq(0)
    qi = ONE / q
    h = q - qi
    RT = [[q, ZERO, ZERO, ZERO], [ZERO, ZERO, ONE, ZERO], [ZERO, ONE, h, ZERO], [ZERO, ZERO, ZERO, q]]
    RI = [[qi, ZERO, ZERO, ZERO], [ZERO, -h, ONE, ZERO], [ZERO, ONE, ZERO, ZERO], [ZERO, ZERO, ZERO, qi]]

    def bits(s):
        return [(s >> (N - 1 - k)) & 1 for k in range(N)]

    def frombits(b):
        s = 0
        for x in b:
            s = 2 * s + x
        return s

    def two_site(i, R):
        M = {}
        for s in range(Dim):
            b = bits(s)
            col = 2 * b[i] + b[i + 1]
            for row in range(4):
                v = R[row][col]
                if v:
                    nb = list(b)
                    nb[i], nb[i + 1] = row >> 1, row & 1
                    M.setdefault(frombits(nb), {})[s] = v
        return M

    def sp_mul(X, Y):
        C = {}
        for i, Xi in X.items():
            Ci = {}
            for k, a in Xi.items():
                Yk = Y.get(k)
                if not Yk:
                    continue
                for j, b in Yk.items():
                    Ci[j] = Ci[j] + a * b if j in Ci else a * b
            Ci = {j: v for j, v in Ci.items() if v}
            if Ci:
                C[i] = Ci
        return C

    def eye():
        return {i: {i: ONE} for i in range(Dim)}

    GEN = {(i, inv): two_site(i, RI if inv else RT) for i in range(N - 1) for inv in (False, True)}

    def word(letters):
        M = eye()
        for let in letters:
            M = sp_mul(M, GEN[let])
        return M

    a0, b0 = A[0], B[0]
    core = [(a0, False), (a0 + 1, True)] * 3 + [(b0, False), (b0 + 1, True)] * 3
    BASE = word(core)
    KD = {s: q ** (2 * sum(1 for x in bits(s) if x == 0) - N) for s in range(Dim)}
    if os.environ.get("QOU_NO_K") == "1":  # diagnostic: plain trace, no K^{⊗N} weight
        KD = {s: ONE for s in range(Dim)}

    def sector(s):
        b = bits(s)
        return (sum(1 for k in A if b[k] == 0) - 1, sum(1 for k in B if b[k] == 0) - 1)

    SECT = [sector(s) for s in range(Dim)]

    def readout(X):
        T = {}
        for s in range(Dim):
            row = BASE.get(s)
            if not row:
                continue
            d = ZERO
            for k, a in row.items():
                x = X.get(k, {}).get(s)
                if x:
                    d += a * x
            if d:
                key = SECT[s]
                T[key] = T.get(key, ZERO) + KD[s] * d
        return T

    T1 = readout(eye())
    keys = sorted(k for k, v in T1.items() if v)

    rows, piv = [], []

    def reduce(v):
        v = list(v)
        for r, p in zip(rows, piv):
            if v[p]:
                f = v[p]
                v = [x - f * y for x, y in zip(v, r)]
        return v

    def add(v):
        v = reduce(v)
        nz = [k for k, x in enumerate(v) if x]
        if not nz:
            return False
        p = nz[0]
        inv = ONE / v[p]
        v = [x * inv for x in v]
        for idx, r in enumerate(rows):
            if r[p]:
                f = r[p]
                rows[idx] = [x - f * y for x, y in zip(r, v)]
        rows.append(v)
        piv.append(p)
        return True

    # BFS over reduced words of S_N; each matrix is its parent's times one generator
    start = tuple(range(N))
    seen = {start}
    frontier = [(start, eye())]
    count = 0
    while frontier:
        nxt = []
        for p, M in frontier:
            T = readout(M)
            add([T.get(k, ZERO) / T1[k] for k in keys])  # ΔE vector
            count += 1
            if count % 2000 == 0:
                log(f"  {layout} q={q}: words {count}, span dim {len(rows)}")
            for i in range(N - 1):
                l = list(p)
                l[i], l[i + 1] = l[i + 1], l[i]
                t = tuple(l)
                if t not in seen:
                    seen.add(t)
                    nxt.append((t, sp_mul(M, GEN[(i, False)])))
        frontier = nxt
    dim = len(rows)
    log(f"{layout} q={q}: {count} words, ΔE span dim {dim} of {len(keys)} sectors")

    # P1: closure under (Q_A, Q_B) -> (1 - Q_B, 1 - Q_A)
    idx = {k: n for n, k in enumerate(keys)}
    closed = True
    for r in list(rows):
        sw = [r[idx[(1 - k[1], 1 - k[0])]] if (1 - k[1], 1 - k[0]) in idx else None for k in keys]
        if any(x is None for x in sw) or any(reduce(sw)):
            closed = False
            break
    log(f"  P1 closed under the sector involution: {closed}")

    # affine-bilinear pair terms: κ·QaQb − a1·Qa − b1·Qb + c in the span (constant is in the span)
    one = reduce([ONE for _ in keys])
    assert not any(one), "constant shift not reachable?"
    rQ = reduce([flint.fmpq(k[0] * k[1]) for k in keys])
    ra = reduce([flint.fmpq(k[0]) for k in keys])
    rb = reduce([flint.fmpq(k[1]) for k in keys])
    M = [[rQ[i], -ra[i], -rb[i]] for i in range(len(keys))]
    mrows, mpiv = [], []
    for row in M:
        v = list(row)
        for r, p in zip(mrows, mpiv):
            if v[p]:
                f = v[p]
                v = [x - f * y for x, y in zip(v, r)]
        nz = [k for k, x in enumerate(v) if x]
        if nz:
            p = nz[0]
            inv = ONE / v[p]
            v = [x * inv for x in v]
            for j, r in enumerate(mrows):
                if r[p]:
                    f = r[p]
                    mrows[j] = [x - f * y for x, y in zip(r, v)]
            mrows.append(v)
            mpiv.append(p)
    rk = len(mrows)
    out = {"layout": layout, "q": q, "dim": dim, "closed": closed, "rank": rk}
    if rk == 2:
        free = [j for j in range(3) if j not in mpiv][0]
        x = [ZERO] * 3
        x[free] = ONE
        for r, p in zip(mrows, mpiv):
            x[p] = -sum((r[j] * x[j] for j in range(3) if j != p), ZERO)
        kappa, a1, b1 = x
        if kappa:
            al, be = a1 / kappa, b1 / kappa
            out.update(alpha=al, beta=be)
            log(f"  rank 2: unique ray, α = {al}, β = {be}, α + β = {al + be}")
        else:
            log("  rank 2 but the ray has κ = 0: no pair term with κ ≠ 0")
    else:
        log(f"  rank {rk} (3: no κ ≠ 0 term; ≤ 1: a family)")
        for r in mrows:
            log(f"    relation on (κ, κα, κβ): {r[0]}·κ + {r[1]}·κα + {r[2]}·κβ = 0")
            out.setdefault("relations", []).append(r)
    # Coulomb test directly: is κ·QaQb (κ = 1) in span + constants?
    coulomb = not any(rQ)
    out["coulomb"] = coulomb
    log(f"  P4 Coulomb form (Q_A Q_B alone) reachable: {coulomb}")
    return out


if __name__ == "__main__":
    lays = [sys.argv[1]] if len(sys.argv) > 1 else ["L6", "L7s", "L7e"]
    qs = [flint.fmpq(*map(int, sys.argv[2].split("/")))] if len(sys.argv) > 2 else [
        flint.fmpq(111, 100), flint.fmpq(7, 5)]
    res = []
    for lay in lays:
        for q in qs:
            res.append(run(lay, q))
    log("summary:")
    for r in res:
        extra = f", α + β = {r['alpha'] + r['beta']}" if "alpha" in r else ""
        log(f"  {r['layout']} q={r['q']}: dim {r['dim']}, involution-closed {r['closed']}, "
            f"rank {r['rank']}, Coulomb {r['coulomb']}{extra}")
    log("done")
