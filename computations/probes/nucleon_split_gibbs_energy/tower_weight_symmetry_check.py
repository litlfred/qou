"""Exact check, up the tower: on (C^2)^{(x)n} with the Jimbo braiding, the plain trace of a braid
word on the weight space mu equals its trace on -mu (n = 3, 5, 7; random words with inverses).

This is the tower analogue of HeckeWeightSpaceSymmetry.trace_rho_n_eq_trace_rho_p (proved at
H_3). It is what NucleonSplitGibbsEnergy.logZ_split needs as its common factor s(q). Exact
Fraction arithmetic at rational q (no float). Bean qou-myts.
"""
from __future__ import annotations
import random
import sys
from fractions import Fraction as Fr
from itertools import combinations


def basis(n, mu):
    k = (n + mu) // 2  # number of u (=0) strands
    out = []
    for ups in combinations(range(n), k):
        out.append(tuple(0 if i in ups else 1 for i in range(n)))
    return out


def apply_gen(vec, i, inv, q):
    h = q - 1 / q
    res = {}
    def add(st, c):
        res[st] = res.get(st, 0) + c
    for st, c in vec.items():
        a, b = st[i], st[i + 1]
        if a == b:
            add(st, c * (q if not inv else (q - h)))
            continue
        sw = st[:i] + (b, a) + st[i + 2:]
        if a == 0:            # u d -> d u
            add(sw, c)
            if inv:
                add(st, -h * c)
        else:                 # d u -> u d + h d u
            add(sw, c)
            if not inv:
                add(st, h * c)
    return res


def trace_on(word, n, mu, q):
    B = basis(n, mu)
    tr = Fr(0)
    for st in B:
        v = {st: Fr(1)}
        for (i, inv) in reversed(word):   # word acts right-to-left
            v = apply_gen(v, i, inv, q)
        tr += v.get(st, 0)
    return tr


def main():
    rng = random.Random(20261127)
    q = Fr(111, 100)
    ok = True
    n_checked = 0
    for n in (3, 5, 7):
        for trial in range(12):
            L = rng.randint(1, 3 * n)
            word = [(rng.randrange(n - 1), rng.random() < 0.4) for _ in range(L)]
            for mu in range(1, n + 1, 2):
                a, b = trace_on(word, n, mu, q), trace_on(word, n, -mu, q)
                n_checked += 1
                if a != b:
                    ok = False
                    print(f"MISMATCH n={n} mu={mu} word={word}: {a} vs {b}")
    # negative control: a strand-0 'u' weight (not an algebra element) must break the symmetry
    global apply_gen
    orig = apply_gen
    apply_gen = lambda v, i, inv, q_: {st: (c * 2 if st[0] == 0 else c)
                                        for st, c in orig(v, i, inv, q_).items()}
    w = [(0, False), (1, False), (0, True)]
    control_breaks = trace_on(w, 3, 1, q) != trace_on(w, 3, -1, q)
    apply_gen = orig
    print(f"negative control breaks the symmetry: {control_breaks}")
    ok &= control_breaks
    print(f"checked {n_checked} (word, n, mu) triples at q=111/100 exactly: "
          f"{'all tr_mu == tr_-mu' if ok else 'MISMATCHES'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
