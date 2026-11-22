#!/usr/bin/env python3
"""Addendum 6 (E10, E11): Brunnian braids on 4-6 strands at short length.
Exact: integer strand tracking; triviality by the Artin action on the free group
(faithful on every B_m), so no faithfulness caveat."""
from __future__ import annotations
import json, sys, time
from pathlib import Path

def ladd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}
def lmul(a, b):
    r = {}
    for i, x in a.items():
        for j, y in b.items():
            r[i + j] = r.get(i + j, 0) + x * y
    return {k: v for k, v in r.items() if v}

def burau_letter(m, g, s):
    """Unreduced Burau of sigma_g^s in B_m (m strands)."""
    M = [[({0: 1} if i == j else {}) for j in range(m)] for i in range(m)]
    if s > 0:
        M[g][g], M[g][g + 1], M[g + 1][g], M[g + 1][g + 1] = {0: 1, 1: -1}, {1: 1}, {0: 1}, {}
    else:
        M[g][g], M[g][g + 1], M[g + 1][g], M[g + 1][g + 1] = {}, {0: 1}, {-1: 1}, {0: 1, -1: -1}
    return M
def mm(A, B):
    m = len(A)
    return [[ladd({}, {}) if False else _dot(A, B, i, j, m) for j in range(m)] for i in range(m)]
def _dot(A, B, i, j, m):
    r = {}
    for k in range(m):
        if A[i][k] and B[k][j]:
            r = ladd(r, lmul(A[i][k], B[k][j]))
    return r
def burau(m, word):
    M = [[({0: 1} if i == j else {}) for j in range(m)] for i in range(m)]
    for g, s in word:
        M = mm(M, burau_letter(m, g, s))
    return M
def is_id(M):
    return all(M[i][j] == ({0: 1} if i == j else {}) for i in range(len(M)) for j in range(len(M)))

def fred(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def artin_is_id(m, word):
    """Artin action of B_m on the free group F_m (faithful). Generators 1..m, inverses
    negative. sigma_i: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i."""
    imgs = [(j,) for j in range(1, m + 1)]
    for g, s in word:
        i, j = g + 1, g + 2
        if s > 0:
            sub = {i: (i, j, -i), j: (i,)}
        else:
            sub = {i: (j,), j: (-j, i, j)}
        def apply(w):
            out = []
            for x in w:
                a = abs(x)
                if a in sub:
                    piece = sub[a] if x > 0 else tuple(-y for y in reversed(sub[a]))
                else:
                    piece = (x,)
                out.extend(piece)
            return fred(out)
        imgs = [apply(w) for w in imgs]
    return all(imgs[k] == (k + 1,) for k in range(m))

def delete_strand(n, word, k):
    """Delete the strand with label k (labels = starting positions)."""
    pos = list(range(n))  # pos[p] = label at position p
    out = []
    for g, s in word:
        a, b = pos[g], pos[g + 1]
        if a != k and b != k:
            p = pos.index(k)
            out.append((g - 1 if g > p else g, s))
        pos[g], pos[g + 1] = b, a
    return tuple(out)

def search(n, maxlen, report):
    letters = [(g, s) for g in range(n - 1) for s in (1, -1)]
    pairs = {(i, j): idx for idx, (i, j) in enumerate((i, j) for i in range(n) for j in range(i + 1, n))}
    found = {}
    nodes = [0]
    t0 = time.time()
    def inv(pos):
        return sum(1 for i in range(n) for j in range(i + 1, n) if pos[i] > pos[j])
    def dfs(word, pos, lk):
        nodes[0] += 1
        if nodes[0] % 2_000_000 == 0:
            print(f"    n={n} nodes {nodes[0]:,} {time.time()-t0:.0f}s", flush=True)
        L = len(word)
        if L and L % 2 == 0 and pos == tuple(range(n)) and not any(lk):
            # pure, zero linking: test Brunnian
            ok = True
            for k in range(n):
                d = delete_strand(n, word, k)
                if not artin_is_id(n - 1, d):
                    ok = False; break
            if ok:
                whole_id = artin_is_id(n, word)
                found.setdefault(L, []).append((word, whole_id))
        rem = maxlen - L
        if rem == 0:
            return
        # prune: need at least sum|lk| + inversions crossings to restore
        if sum(abs(x) for x in lk) > rem or inv(pos) > rem:
            return
        for c in letters:
            if word and word[-1][0] == c[0] and word[-1][1] == -c[1]:
                continue
            g, s = c
            p = list(pos); a, b = p[g], p[g + 1]; p[g], p[g + 1] = b, a
            l2 = list(lk); l2[pairs[(min(a, b), max(a, b))]] += s
            dfs(word + (c,), tuple(p), tuple(l2))
    dfs((), tuple(range(n)), tuple([0] * len(pairs)))
    res = {}
    for L, ws in sorted(found.items()):
        nontriv = [w for w, wid in ws if not wid]
        res[L] = {"pure_zero_lk_all_deletions_trivial": len(ws),
                  "brunnian": len(nontriv),
                  "examples": ["".join(f"s{g}" + ("" if s > 0 else "'") for g, s in w) for w in nontriv[:5]]}
    report[n] = {"maxlen": maxlen, "nodes": nodes[0], "wall_s": round(time.time() - t0, 1), "by_length": res}
    print(f"n={n} maxlen={maxlen}: nodes {nodes[0]:,}, {time.time()-t0:.0f}s, {res}", flush=True)

def main():
    # self-check: beta_Bor on 3 strands is Brunnian by this test
    rep = {}
    search(3, 6, rep)
    assert rep[3]["by_length"][6]["brunnian"] == 4
    out = {"E10": {}, "E11": {}}
    for n in (4, 5, 6):
        search(n, 6, out["E10"])
    for L in (8, 10, 12, 14):
        search(4, L, out["E11"])
        out["E11"][f"len{L}"] = out["E11"].pop(4)
        Path(__file__).with_name("why-three-strands.result.json").write_text(json.dumps(out, indent=1))
    Path(__file__).with_name("why-three-strands.result.json").write_text(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
