"""Mirror vertices and the scored nucleon element (bean qou-99qc, brief for PR #8696 question D).

Measures, exactly in Q(q), the scored flavour split eps_flavour (owner ruling D1 = A, PR #8586,
`per_observable_100x_status.py`) on all eight three-vertex words in {V, Vbar}, V = s0 s1^-1,
Vbar = s0^-1 s1, three strands, Jimbo R-check representation (as #8696 `jimbo.py`).
Reading 3 for the same eight words is already measured in `computations/probes/gg_two_orientations`
(all eight pass; level 3 sees pure vs mixed only).

Also free-reduces the five-strand candidate V2 V0 V1 V2 of #8696 and reports closure components
and pairwise linking numbers with beta_Bor on strands 0-2.

Nothing is selected; no CODATA is read. Run: PYTHONPATH=tools/qou-substrate/python python3 <this>.
"""
import itertools

import mpmath as mp
import sympy as sp
from qou_substrate.constants import Q_50_DIGIT_STR

q = sp.symbols("q", positive=True)
h = q - 1 / q
N = 3
basis = list(itertools.product([0, 1], repeat=N))  # 0 = u, 1 = d
idx = {b: i for i, b in enumerate(basis)}


def rcheck(i):
    M = sp.zeros(2 ** N)
    for b in basis:
        a, c = b[i], b[i + 1]
        j = idx[b]
        if a == c:
            M[j, j] = q
        elif (a, c) == (0, 1):
            s = list(b); s[i], s[i + 1] = 1, 0
            M[idx[tuple(s)], j] = 1
        else:
            s = list(b); s[i], s[i + 1] = 0, 1
            M[idx[tuple(s)], j] = 1
            M[j, j] += h
    return M


S = [rcheck(0), rcheck(1)]
Si = [m - h * sp.eye(2 ** N) for m in S]
assert sp.simplify(S[0] * S[1] * S[0] - S[1] * S[0] * S[1]) == sp.zeros(2 ** N)
V = S[0] * Si[1]
B = Si[0] * S[1]
K = sp.diag(*[sp.prod([q if x == 0 else 1 / q for x in b]) for b in basis])


def weight_trace(X, n_d):
    return sp.simplify(sum((K * X)[idx[b], idx[b]] for b in basis if sum(b) == n_d))


P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
scored = (q**2 - 1) * P / (q**4 * (q**2 + 1) ** 3)   # eps_flavour(V^3), the scored row
two = q + 1 / q

mp.mp.dps = 70
q0 = mp.mpf(Q_50_DIGIT_STR)
results = {}
for w in itertools.product("VB", repeat=3):
    X = sp.eye(2 ** N)
    for c in w:
        X = X * (V if c == "V" else B)
    eps = sp.factor(sp.simplify((weight_trace(X, 2) - weight_trace(X, 1)) / two ** 3))
    results["".join(w)] = eps
    val = sp.lambdify(q, eps, "mpmath")(q0)
    print("".join(w), eps, " eps(q0) =", mp.nstr(val, 15))

assert sp.simplify(results["VVV"] - scored) == 0, "does not reproduce the scored eps_flavour(V^3)"
assert sp.simplify(results["BBB"] - scored) == 0
mixed = results["VVB"]
assert all(sp.simplify(results[k] - mixed) == 0 for k in results if k not in ("VVV", "BBB"))
ratio = sp.lambdify(q, sp.simplify(mixed / scored), "mpmath")(q0)
print("CHECK pure pair equal: PASS; six mixed words equal each other: PASS")
print("mixed / pure at proton q0 =", mp.nstr(ratio, 15))

# --- five strands: V2 V0 V1 V2 ------------------------------------------------------------
def vtx(i):
    return [(i, 1), (i + 1, -1)]


word = vtx(2) + vtx(0) + vtx(1) + vtx(2)
red = []
for g in word:
    if red and red[-1][0] == g[0] and red[-1][1] == -g[1]:
        red.pop()
    else:
        red.append(g)
print("V2V0V1V2 letters:", word)
print("adjacent free reduction:", red, "(length", len(red), "of", len(word), ")")
bor = [(0, 1), (1, -1)] * 3
pos = list(range(5)); lk = {}
for g, s in word + bor:
    a, b = pos[g], pos[g + 1]
    key = tuple(sorted((a, b))); lk[key] = lk.get(key, 0) + s
    pos[g], pos[g + 1] = b, a
perm = {pos[p]: p for p in range(5)}
seen, comps = set(), []
for s0 in range(5):
    if s0 in seen:
        continue
    c, x = [], s0
    while x not in seen:
        seen.add(x); c.append(x); x = perm[x]
    comps.append(c)
cid = {x: i for i, c in enumerate(comps) for x in c}
L = {}
for (a, b), v in lk.items():
    if cid[a] != cid[b]:
        k = tuple(sorted((cid[a], cid[b]))); L[k] = L.get(k, 0) + v
print("components (strands):", comps)
print("inter-component signed crossings (linking = half):", L)
assert len(red) == 4 and comps == [[0, 1], [2, 3], [4]] and L.get((1, 2)) == -2
print("ALL CHECKS PASS")
