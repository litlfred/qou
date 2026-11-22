#!/usr/bin/env python3
"""Flavour-labelled closure: does labelling the strands give the own-sector reading by itself?

Pre-registration (this docstring, committed with the first run; an exploratory 3x3 run was done
first and is disclosed). A labelled closure keeps each closed component's u/d label, so a
labelling l contributes <l|rho(beta)|l> only if l is constant on the cycles of the braid's
permutation. Questions:
 (1) For the pure Borromean word V^3, does the labelled closure differ from the sector trace?
     (Prediction: no; a pure braid allows every labelling of the sector.)
 (2) For the six positive permutation braids T_sigma, normalised by q^{-(n - c(sigma))}
     (n strands, c closure components), is the labelled count q-independent, and on which
     weight sectors? (Prediction from the exploratory run: 6 on each nucleon sector, not
     constant on uuu/ddd.)
Full 8-dim Jimbo R-matrix on V^{(x)3}; exact sympy; no measured values.
"""
import itertools, json
from pathlib import Path
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
# Jimbo R-check on V(x)V, basis uu, ud, du, dd (u = 0, d = 1)
R2 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
I2 = sp.eye(2)
s1 = sp.kronecker_product(R2, I2)
s2 = sp.kronecker_product(I2, R2)
S1, S2 = s1 - h * sp.eye(8), s2 - h * sp.eye(8)
labs = list(itertools.product("ud", repeat=3))           # index = binary, u=0
idx = {l: i for i, l in enumerate(labs)}
sector = {k: [l for l in labs if l.count("u") == k] for k in range(4)}
checks = []
checks.append(("s1 S1 = 1, s2 S2 = 1", sp.simplify(s1 * S1) == sp.eye(8) and sp.simplify(s2 * S2) == sp.eye(8)))
checks.append(("braid relation s1 s2 s1 = s2 s1 s2", sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(8)))

def perm_of(word):  # word letters 1/2; strand positions
    p = [0, 1, 2]
    for g in word:
        i = g - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p  # p[pos] = original strand now at pos
def labelled(M, word, k):
    p = perm_of(word)
    return sp.simplify(sum(M[idx[l], idx[l]] for l in sector[k] if all(l[i] == l[p[i]] for i in range(3))))
def sector_tr(M, k):
    return sp.simplify(sum(M[idx[l], idx[l]] for l in sector[k]))

# (1) V^3 = (s1 s2^-1)^3, pure
V3 = (s1 * S2) ** 3
wV3 = [1, 2] * 3
checks.append(("V^3 is a pure braid", perm_of(wV3) == [0, 1, 2]))
res1 = {k: {"labelled": str(sp.factor(labelled(V3, wV3, k))), "sector": str(sp.factor(sector_tr(V3, k)))} for k in range(4)}
checks.append(("(1) labelled closure of V^3 = sector trace on every sector",
               all(sp.simplify(labelled(V3, wV3, k) - sector_tr(V3, k)) == 0 for k in range(4))))

# (2) permutation braids
perm_words = {"e": [], "s1": [1], "s2": [2], "s1s2": [1, 2], "s2s1": [2, 1], "s1s2s1": [1, 2, 1]}
mat = {1: s1, 2: s2}
def M_of(w):
    M = sp.eye(8)
    for g in w:
        M = M * mat[g]
    return M
def ncyc(p):
    seen, c = set(), 0
    for i in range(3):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j); j = p[j]
    return c
res2, ex2 = {}, {}
for k in range(4):
    tot = sp.simplify(sum(q ** (ncyc(perm_of(w)) - 3) * labelled(M_of(w), w, k) for w in perm_words.values()))
    ex2[k] = sp.simplify(tot); res2[k] = str(ex2[k])
print("labelled S3 count, q^{c-n} normalised, by #u:", res2)
checks.append(("(2) count = 6 on the proton sector (two u), for all q", sp.simplify(ex2[2] - 6) == 0))
checks.append(("(2) count = 6 on the neutron sector (one u), for all q", sp.simplify(ex2[1] - 6) == 0))
checks.append(("(2) count is NOT q-independent on uuu and ddd",
               all(sp.diff(ex2[k], q) != 0 for k in (0, 3))))
ok = all(c for _, c in checks)
for n, c in checks:
    print(("PASS " if c else "FAIL ") + n)
Path(__file__).with_suffix(".out.json").write_text(json.dumps(
    {"probe": "mn_labelled_closure_probe", "checks": dict(checks), "all_pass": ok,
     "V3_labelled_vs_sector": res1, "S3_labelled_count_by_number_of_u": res2,
     "reading": "Labelling alone does not separate the volume term (V^3 is pure). On the permutation "
                "braids with weight q^{c-n} it gives a q-independent count 6 exactly on the two nucleon sectors."},
    indent=1) + "\n")
raise SystemExit(0 if ok else 1)
