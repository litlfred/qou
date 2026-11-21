#!/usr/bin/env python3
"""Does anything force the Borromean word beta_Bor = (s0 s1^-1)^3 ?

Pre-registered in PREREGISTRATION.md (same directory) before this file ran.
Exact arithmetic only: Laurent polynomials in q with Python-int coefficients,
and sympy rational functions for P3. No float, no measured value.

Letters: (gen, sign) with gen in {0,1}, sign in {+1,-1}.
(2,1) representation: T_i = q * Burau_i(t = q^-2), entries in Z[q, q^-1]:
    Burau_0 = [[-t, 1], [0, 1]],   Burau_1 = [[1, 0], [t, -t]].
Eigenvalues of T_i are q and -q^-1 (Hecke relation T^2 = (q - q^-1) T + 1).
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as sp

# ---------------------------------------------------------------- Laurent polys
# A Laurent polynomial is a dict {exponent: int coefficient}, zero terms dropped.


def lp(d):
    return {k: v for k, v in d.items() if v != 0}


def ladd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
    return lp(r)


def lmul(a, b):
    r = {}
    for i, x in a.items():
        for j, y in b.items():
            r[i + j] = r.get(i + j, 0) + x * y
    return lp(r)


def lkey(a):
    return tuple(sorted(a.items()))


ONE = {0: 1}
ZERO = {}


def mmul(A, B):
    return [[ladd(lmul(A[i][0], B[0][j]), lmul(A[i][1], B[1][j])) for j in range(2)]
            for i in range(2)]


def mtr(A):
    return ladd(A[0][0], A[1][1])


# T_i = q * Burau_i(t = q^-2);  T_i^-1 = q^-1 * Burau_i(t)^-1.
# Burau_0^-1 = [[-1/t, 1/t], [0, 1]], Burau_1^-1 = [[1, 0], [1, -1/t]].
T = {
    (0, +1): [[{-1: -1}, {1: 1}], [ZERO, {1: 1}]],
    (1, +1): [[{1: 1}, ZERO], [{-1: 1}, {-1: -1}]],
    (0, -1): [[{1: -1}, {1: 1}], [ZERO, {-1: 1}]],
    (1, -1): [[{-1: 1}, ZERO], [{-1: 1}, {1: -1}]],
}
IDM = [[ONE, ZERO], [ZERO, ONE]]
LETTERS = [(0, 1), (0, -1), (1, 1), (1, -1)]


def char(word):
    M = IDM
    for c in word:
        M = mmul(M, T[c])
    return mtr(M)


def self_check():
    """Hecke relation and braid relation, exactly."""
    h = {1: 1, -1: -1}
    for g in (0, 1):
        Tp, Tm = T[(g, 1)], T[(g, -1)]
        # T T^-1 = 1
        assert all(lkey(mmul(Tp, Tm)[i][j]) == lkey(IDM[i][j]) for i in range(2) for j in range(2))
        # T^2 = h T + 1
        lhs = mmul(Tp, Tp)
        for i in range(2):
            for j in range(2):
                rhs = ladd(lmul(h, Tp[i][j]), IDM[i][j])
                assert lkey(lhs[i][j]) == lkey(rhs)
    a = mmul(mmul(T[(0, 1)], T[(1, 1)]), T[(0, 1)])
    b = mmul(mmul(T[(1, 1)], T[(0, 1)]), T[(1, 1)])
    assert all(lkey(a[i][j]) == lkey(b[i][j]) for i in range(2) for j in range(2))


# ---------------------------------------------------------------- combinatorics

def reduced_words(n):
    if n == 0:
        yield ()
        return
    for w in reduced_words(n - 1):
        for c in LETTERS:
            if w and w[-1][0] == c[0] and w[-1][1] == -c[1]:
                continue
            yield w + (c,)


def writhe(w):
    return sum(s for _, s in w)


def perm_and_linking(w):
    """Strand positions -> strand labels; twice the pairwise linking."""
    pos = [0, 1, 2]  # pos[k] = label of strand currently at position k
    lk2 = {(0, 1): 0, (0, 2): 0, (1, 2): 0}
    for g, s in w:
        a, b = pos[g], pos[g + 1]
        lk2[tuple(sorted((a, b)))] += s
        pos[g], pos[g + 1] = b, a
    return tuple(pos), lk2


def components(w):
    perm, _ = perm_and_linking(w)
    # perm maps position -> label; cycles of the permutation = components
    seen, n = set(), 0
    for k in range(3):
        if k in seen:
            continue
        n += 1
        j = k
        while j not in seen:
            seen.add(j)
            j = perm[j]
    return n


def is_pure(w):
    return perm_and_linking(w)[0] == (0, 1, 2)


def lk_zero(w):
    return all(v == 0 for v in perm_and_linking(w)[1].values())


# symmetry orbit: cyclic rotation, flip s0<->s1, inverse, mirror
def rotations(w):
    return [w[i:] + w[:i] for i in range(len(w))] or [w]


def flip(w):
    return tuple((1 - g, s) for g, s in w)


def inverse(w):
    return tuple((g, -s) for g, s in reversed(w))


def mirror(w):
    return tuple((g, -s) for g, s in w)


def orbit(w):
    out = set()
    frontier = {w}
    while frontier:
        x = frontier.pop()
        if x in out:
            continue
        out.add(x)
        for y in rotations(x) + [flip(x), inverse(x), mirror(x)]:
            if y not in out:
                frontier.add(y)
    return out


def show(w):
    return "".join(f"s{g}" + ("" if s > 0 else "'") for g, s in w)


BOR = ((0, 1), (1, -1)) * 3


def main():
    self_check()
    chi_bor = char(BOR)
    chi_id = char(())
    out = {"chi_bor": {str(k): v for k, v in sorted(chi_bor.items())},
           "chi_identity": {str(k): v for k, v in sorted(chi_id.items())}}
    print("chi(beta_Bor) =", sorted(chi_bor.items()))
    bor_orbit = orbit(BOR)
    print("|orbit(beta_Bor)| (rotation, flip, inverse, mirror) =", len(bor_orbit))

    # ---------------- P1
    p1 = {}
    for n in range(0, 9):
        surv = []
        for w in reduced_words(n):
            if not is_pure(w) or not lk_zero(w):
                continue
            c = char(w)
            if lkey(c) == lkey(chi_id):
                continue
            surv.append(w)
        same = [w for w in surv if lkey(char(w)) == lkey(chi_bor)]
        in_orbit = [w for w in surv if w in bor_orbit]
        other_chars = {}
        for w in surv:
            k = lkey(char(w))
            if k != lkey(chi_bor):
                other_chars.setdefault(k, []).append(show(w))
        p1[n] = {"survivors": len(surv), "same_char_as_bor": len(same),
                 "in_bor_orbit": len(in_orbit),
                 "distinct_other_chars": len(other_chars),
                 "examples_other": [v[0] for v in list(other_chars.values())[:5]]}
        print(f"P1 len {n}: survivors {len(surv)}, same chi as Bor {len(same)}, "
              f"in Bor orbit {len(in_orbit)}, other chars {len(other_chars)}")
        if n == 6:
            p1[n]["survivor_words"] = sorted(show(w) for w in surv)
    out["P1"] = p1

    # ---------------- P2: writhe 0, same chi, or tr = -tr(Bor)
    # tr at writhe 0 = 1 + y21 (chi - 2); tr = -tr_Bor  <=>  chi = 6 - chi_bor - 2 [2]^2 ... computed below
    # -tr_Bor = -1 - y21 (chi_bor - 2)  =>  y21 (chi - 2) = -2 - y21(chi_bor - 2)
    #   => chi = 4 - chi_bor - 2/y21 = 4 - chi_bor - 2 [2]^2,  [2]^2 = q^2 + 2 + q^-2
    two_sq = {2: 1, 0: 2, -2: 1}
    chi_neg = ladd(ladd({0: 4}, {k: -v for k, v in chi_bor.items()}),
                   {k: -2 * v for k, v in two_sq.items()})
    p2 = {}
    for n in range(0, 11, 2):
        same, neg = [], []
        for w in reduced_words(n):
            if writhe(w) != 0:
                continue
            k = lkey(char(w))
            if k == lkey(chi_bor):
                same.append(w)
            elif k == lkey(chi_neg):
                neg.append(w)
        rows = []
        outside = [w for w in same if w not in bor_orbit]
        # classify outside-orbit words by closure data
        cls = {}
        for w in outside:
            perm, lk2 = perm_and_linking(w)
            key = (components(w), tuple(sorted(lk2.values())) if components(w) == 3 else None)
            cls.setdefault(str(key), []).append(show(w))
        p2[n] = {"same_chi": len(same), "in_bor_orbit": len(same) - len(outside),
                 "outside_orbit": len(outside), "minus_tr": len(neg),
                 "outside_by_(components, 2*lk)": {k: {"count": len(v), "examples": v[:4]}
                                                    for k, v in cls.items()}}
        print(f"P2 len {n}: same chi {len(same)} (outside Bor orbit {len(outside)}), "
              f"tr = -tr_Bor: {len(neg)}; outside classes: "
              + "; ".join(f"{k}: {len(v)}" for k, v in cls.items()))
    out["P2"] = p2

    # ---------------- P3: writhe != 0, rational-function equality with convention-D weights
    q = sp.symbols("q", positive=True)
    br2 = q + 1 / q
    br3 = q**2 + 1 + q**-2
    y3 = q**3 / (br2 * br3)  # [3]_q! = [2][3]
    y21 = 1 / br2**2
    y111 = 1 - y3 - 2 * y21

    def lp_to_sym(d):
        return sum(sp.Integer(v) * q**k for k, v in d.items())

    def trM(w):
        e = writhe(w)
        return y3 * q**e + y111 * (-1 / q)**e + y21 * lp_to_sym(char(w))

    tr_bor = sp.simplify(trM(BOR))
    hh = sp.symbols("h")
    corpus = (4 + hh**2 - 3 * hh**4 - hh**6) / (hh**2 + 4)
    check = sp.simplify(tr_bor - corpus.subs(hh, q - 1 / q))
    print("P3 weight check (tr_M(Bor) - corpus closed form) =", check)
    out["P3_weight_check_zero"] = bool(check == 0)
    if check != 0:
        print("weight check FAILED; stopping P3 as pre-registered")
    else:
        p3 = {}
        for n in range(1, 9):
            hits = []
            # group by (writhe, chi) to avoid re-simplifying
            seen = {}
            for w in reduced_words(n):
                e = writhe(w)
                if e == 0 or abs(e) > 4:
                    continue
                key = (e, lkey(char(w)))
                if key not in seen:
                    t = trM(w)
                    d1 = sp.simplify(sp.together(t - tr_bor)) == 0
                    d2 = sp.simplify(sp.together(t + tr_bor)) == 0
                    seen[key] = d1 or d2
                if seen[key]:
                    hits.append(show(w))
            p3[n] = {"distinct_(writhe,chi)": len(seen), "hits": hits[:10], "n_hits": len(hits)}
            print(f"P3 len {n}: distinct (writhe, chi) {len(seen)}, hits {len(hits)}")
        out["P3"] = p3

    dest = Path(__file__).with_name("borromean-word-forcing.result.json")
    dest.write_text(json.dumps(out, indent=1, sort_keys=True))
    print("wrote", dest)


if __name__ == "__main__":
    sys.exit(main())
