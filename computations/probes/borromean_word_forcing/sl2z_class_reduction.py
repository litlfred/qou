#!/usr/bin/env python3
"""Addendum 5 (E6, E7): reduce 'same chi at writhe 0 => conjugate' to a finite list of
SL(2,Z) classes. Exact integer + Laurent arithmetic only."""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from borromean_word_forcing_probe import (BOR, IDM, T, char, lkey, mmul, mtr, self_check,
                                          show, perm_and_linking, components)

R = ((1, 1), (0, 1)); L = ((1, 0), (1, 1))
def imul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def ipow(A, n):
    M = ((1, 0), (0, 1))
    for _ in range(n): M = imul(M, A)
    return M

def canon(pairs):
    k = len(pairs)
    return min(tuple(pairs[i:] + pairs[:i]) for i in range(k))

def classes_with_trace(t, maxsum):
    """Cyclic positive RL words R^a1 L^b1 ... with trace t (a_i, b_i >= 1), up to rotation."""
    found = set()
    def rec(pairs, M, s):
        if pairs:
            tr = M[0][0] + M[1][1]
            if tr == t:
                found.add(canon(pairs))
            if tr > t:   # trace of a positive word only grows when letters are appended
                return
        for a in range(1, maxsum - s + 1):
            for b in range(1, maxsum - s - a + 1):
                N = imul(imul(M, ipow(R, a)), ipow(L, b))
                rec(pairs + [(a, b)], N, s + a + b)
    rec([], ((1, 0), (0, 1)), 0)
    return sorted(found)

def braid_of(pairs):
    w = []
    for a, b in pairs:
        w += [(0, 1)] * a + [(1, -1)] * b
    return tuple(w)

DELTA = ((0, 1), (1, 1), (0, 1))
def writhe(w): return sum(s for _, s in w)

def chi_writhe0_lift(pairs):
    """Writhe-0 lift w * Delta^{-4k} if writhe(w) = 12k, else None; return (chi, word)."""
    w = braid_of(pairs)
    e = writhe(w)
    if e % 12:
        return None, w, e
    k = e // 12
    inv = tuple((g, -s) for g, s in reversed(DELTA))
    lift = w + inv * (4 * k) if k >= 0 else w + DELTA * (-4 * k)
    assert writhe(lift) == 0
    return lkey(char(lift)), lift, e

def main():
    self_check()
    # monotonicity check used for pruning: appending R or L never lowers the trace of a
    # nonneg matrix with det 1 (entries >= 0), checked on the fly by assertion below.
    chi_bor = lkey(char(BOR))
    # Delta^4 acts as a scalar in the (2,1) rep:
    D = IDM
    for c in DELTA * 4: D = mmul(D, T[c])
    print("rep(Delta^4) =", D)
    out = {}
    cls = classes_with_trace(18, 40)
    rows = []
    for p in cls:
        chi, lift, e = chi_writhe0_lift(p)
        A = ((1, 0), (0, 1))
        for a, b in p: A = imul(imul(A, ipow(R, a)), ipow(L, b))
        rows.append({"RL_word": " ".join(f"R^{a}L^{b}" for a, b in p), "matrix": A,
                     "braid_writhe": e, "writhe0_lift": chi is not None,
                     "chi_equals_bor": chi == chi_bor if chi is not None else None,
                     "lift": show(lift) if chi is not None else None})
    out["E6_trace18_classes"] = rows
    print(f"E6: {len(cls)} SL(2,Z) classes of trace 18 (positive RL words, up to rotation)")
    for r in rows:
        print("  ", r["RL_word"], r["matrix"], "writhe", r["braid_writhe"],
              "writhe-0 lift" if r["writhe0_lift"] else "no writhe-0 lift",
              "| chi == chi(Bor)" if r["chi_equals_bor"] else ("| chi differs" if r["writhe0_lift"] else ""))
    hits = [r for r in rows if r["chi_equals_bor"]]
    print("E6 classes with chi = chi(Bor):", len(hits), [r["RL_word"] for r in hits])

    # E7: for traces 3..40, look for two distinct classes with writhe-0 lifts and equal chi
    e7 = []
    for t in range(3, 41):
        bychi = {}
        for p in classes_with_trace(t, 60):
            chi, lift, e = chi_writhe0_lift(p)
            if chi is None: continue
            bychi.setdefault(chi, []).append(p)
        for chi, ps in bychi.items():
            if len(ps) > 1:
                e7.append({"trace": t, "classes": [" ".join(f"R^{a}L^{b}" for a, b in p) for p in ps]})
    out["E7_same_chi_distinct_classes"] = e7
    print(f"E7: traces 3..40, groups of >1 writhe-0 classes sharing chi: {len(e7)}")
    for x in e7[:10]: print("  ", x)
    Path(__file__).with_name("sl2z-class-reduction.result.json").write_text(json.dumps(out, indent=1, default=list))

if __name__ == "__main__":
    main()
