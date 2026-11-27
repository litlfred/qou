#!/usr/bin/env python3
"""A5 least hyperbolic chi probe (bean qou-qhcr).

Exact integer checks, no floats, no substrate parameter:
  1. Riemann-Hurwitz arithmetic: the hyperbolic genera g >= 2 an A5-action allows
     (periods in {2,3,5}) start at g = 4; list them up to g = 30.
  2. Orbifold form: among hyperbolic signatures (h; m_1..m_r) with m_i in {2,3,5},
     the largest chi_orb is -1/10, attained only by (0; 2,5,5).  60 * (-1/10) = -6.
  3. An explicit A5-map with chi = -6: darts D = A5, sigma = left mult by y (order 5),
     alpha = left mult by x (order 2), A5 acting on the right.  Checks: alpha a
     fixed-point-free involution, the map connected, the right action commutes with
     sigma and alpha, is free on darts, and chi = c(sigma) - c(alpha) + c(sigma alpha) = -6.
Writes a witness JSON next to this file.
"""
import itertools, json, os
from fractions import Fraction

PERIODS = (2, 3, 5)

# 1. RH arithmetic: 2g - 2 = 60(2h - 2) + sum(60 - 60/m)
def admissible(g, hmax=3, rmax=12):
    for h in range(hmax + 1):
        for r in range(rmax + 1):
            for ms in itertools.combinations_with_replacement(PERIODS, r):
                if 2 * g - 2 == 60 * (2 * h - 2) + sum(60 - 60 // m for m in ms):
                    return (h, ms)
    return None

genera = {g: admissible(g) for g in range(2, 31)}
allowed = [g for g, s in genera.items() if s is not None]

# 2. orbifold chi, hyperbolic only
best = None
for h in range(0, 3):
    for r in range(0, 8):
        for ms in itertools.combinations_with_replacement(PERIODS, r):
            chi = Fraction(2 - 2 * h) - sum(1 - Fraction(1, m) for m in ms)
            if chi < 0 and (best is None or chi > best[0]):
                best = (chi, h, ms)
            elif chi < 0 and chi == best[0]:
                best = best + ((h, ms),)

# 3. explicit map on A5
def compose(p, q):  # (p*q)(i) = p(q(i))
    return tuple(p[q[i]] for i in range(5))
def parity(p):
    s, seen = 0, set()
    for i in range(5):
        if i in seen: continue
        j, L = i, 0
        while j not in seen:
            seen.add(j); j = p[j]; L += 1
        s += L - 1
    return s % 2
A5 = [p for p in itertools.permutations(range(5)) if parity(p) == 0]
idx = {p: k for k, p in enumerate(A5)}
e = tuple(range(5))
def order(p):
    k, q = 1, p
    while q != e:
        q = compose(p, q); k += 1
    return k
x = (0, 3, 4, 1, 2)            # (13)(24), order 2
y = (1, 2, 3, 4, 0)            # (01234), order 5
assert order(x) == 2 and order(y) == 5 and x in idx and y in idx
sigma = [idx[compose(y, d)] for d in A5]
alpha = [idx[compose(x, d)] for d in A5]
sa = [sigma[alpha[k]] for k in range(60)]
def ncycles(perm):
    seen, c = set(), 0
    for i in range(len(perm)):
        if i in seen: continue
        c += 1; j = i
        while j not in seen:
            seen.add(j); j = perm[j]
    return c
inv = all(alpha[alpha[k]] == k for k in range(60))
fpf = all(alpha[k] != k for k in range(60))
# connectivity of <sigma, alpha>
comp, stack = {0}, [0]
while stack:
    u = stack.pop()
    for v in (sigma[u], alpha[u]):
        if v not in comp: comp.add(v); stack.append(v)
connected = len(comp) == 60
# right action d . g := d * g^{-1}
def inverse(p):
    q = [0] * 5
    for i in range(5): q[p[i]] = i
    return tuple(q)
act = lambda g, k: idx[compose(A5[k], inverse(g))]
commutes = all(act(g, sigma[k]) == sigma[act(g, k)] and act(g, alpha[k]) == alpha[act(g, k)]
               for g in A5 for k in range(60))
free = all(act(g, k) != k for g in A5 if g != e for k in range(60))
cs, ca, csa = ncycles(sigma), ncycles(alpha), ncycles(sa)
# Cell stabilisers.  The right action is free on darts, so it is free on the edges and
# triangles of the barycentric subdivision (both are indexed by darts); its vertices are the
# old vertices, edge midpoints and face centres, with stabilisers of order |cycle| =
# ord(y), 2, ord(yx).  So the subdivision meets the hypotheses of chi_le_neg_six_of_A5_map
# (free on edges and faces, cyclic vertex stabilisers) and has the same chi.
def cycles(perm):
    seen, out = set(), []
    for i in range(len(perm)):
        if i in seen: continue
        c, j = [], i
        while j not in seen:
            seen.add(j); c.append(j); j = perm[j]
        out.append(frozenset(c))
    return out
def stab_orders(cells):
    res = set()
    for c in cells:
        res.add(sum(1 for g in A5 if frozenset(act(g, k) for k in c) == c))
    return res
stabV, stabE, stabF = stab_orders(cycles(sigma)), stab_orders(cycles(alpha)), stab_orders(cycles(sa))
subV, subE, subF = cs + ca + csa, 3 * 60, 2 * 60
chi_sub = subV - subE + subF
chi = cs - ca + csa
ord_sa = order(compose(y, x))

checks = {
    "least_hyperbolic_genus_is_4": allowed[0] == 4,
    "genera_2_to_8_are_4_5_6": [g for g in allowed if g <= 8] == [4, 5, 6],
    "max_hyperbolic_chi_orb_is_minus_1_over_10": best[0] == Fraction(-1, 10),
    "attained_only_by_0_2_5_5": best[1:3] == (0, (2, 5, 5)) and len(best) == 3,
    "sixty_times_chi_orb_is_minus_6": 60 * best[0] == -6,
    "alpha_fixed_point_free_involution": inv and fpf,
    "map_connected": connected,
    "right_A5_action_commutes": commutes,
    "right_A5_action_free_on_darts": free,
    "sigma_alpha_has_order_5": ord_sa == 5,
    "cycle_counts_12_30_12": (cs, ca, csa) == (12, 30, 12),
    "map_chi_is_minus_6": chi == -6,
    "cell_stabilisers_cyclic_orders_5_2_5": (stabV, stabE, stabF) == ({5}, {2}, {5}),
    "subdivision_54_180_120_chi_minus_6": (subV, subE, subF, chi_sub) == (54, 180, 120, -6),
}
out = {
    "probe": "a5_least_hyperbolic_chi_probe",
    "bean": "qou-qhcr",
    "arithmetic": "exact int / Fraction; no float, no substrate parameter",
    "allowed_hyperbolic_genera_le_30": allowed,
    "signatures": {str(g): [genera[g][0], list(genera[g][1])] for g in allowed},
    "max_chi_orb": str(best[0]),
    "explicit_map": {"x": "(13)(24)", "y": "(01234)", "V": cs, "E": ca, "F": csa, "chi": chi, "subdivision": {"V": subV, "E": subE, "F": subF, "chi": chi_sub}},
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5-least-hyperbolic-chi.witness.json")
with open(path, "w") as f:
    json.dump(out, f, indent=2); f.write("\n")
for k, v in checks.items():
    print(("PASS " if v else "FAIL ") + k)
print(f"{out['passed']}/{out['total']}  allowed genera: {allowed}")
raise SystemExit(0 if all(checks.values()) else 1)
