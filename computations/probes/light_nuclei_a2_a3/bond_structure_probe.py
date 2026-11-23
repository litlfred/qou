"""bond_structure_probe.py: why the trace kills orders h^1..h^3 of a gamma-gamma bond, and
what the next order looks like (exploratory, not preregistered; follows the generic-z probes).

All exact over Q[h, z] (python-flint), z the free Markov parameter, h = q - q^-1.

(a) V^3 - 1 as an element of H_3: it starts at h^2, and the h^2 part is c - c^-1, the two
    3-cycles. V^3 is the Borromean braid, a commutator of pure braids, so no h^1 term.
(b) The h^2 term dies in the trace for EVERY receiving word: at h = 0 the trace is
    z^(n - #cycles), and for any permutation w fixing strand 0 (the strand only the bond
    touches), w c and w c^-1 have the same number of cycles. Checked for n = 3..8.
(c) The h^3 term does not die for every word. On the 15 basis words of length <= 3 on the
    receiving strands it dies exactly when the two strands shared with the bond lie in
    different cycles of the word's h = 0 permutation. Both production blocks reduce at
    h = 0 to the transposition s_2, which separates them, so h^3 dies too.
(d) Next orders, A = 3: a single bond (i, j) in place gives EXACTLY the A = 2 ratio for the
    type of nucleon j, at every order (48 cells). Several bonds multiply exactly,
    ratio = product of single-bond ratios, unless two bonds go into the same nucleon; then
    the product rule fails first at h^6, by (1 - z^2) h^6 relative, in every order and
    variant (64 cells).
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_src = open(os.path.join(HERE, "a3_bonds_generic_z_probe.py")).read().split("BOND_SETS =")[0]
_g = {"__name__": "a3_lib", "__file__": os.path.join(HERE, "a3_bonds_generic_z_probe.py")}
exec(_src, _g)  # reuse trace / mul_letter / h_order_and_lead without running that probe
F, CTX, ONE, Z = _g["F"], _g["CTX"], _g["ONE"], _g["Z"]
trace, mul_letter, hol, at_h0 = _g["trace"], _g["mul_letter"], _g["h_order_and_lead"], _g["at_h0"]
T0 = time.time()
out = {}

# (a)
x = {(0, 1, 2): ONE}
for _ in range(3):
    x = mul_letter(mul_letter(x, "S", 0), "I", 1)
x[(0, 1, 2)] = x.get((0, 1, 2), 0) - ONE
out["a_V3_minus_1"] = {str(w): str(c) for w, c in sorted(x.items()) if c != 0}
assert min(min(a for a, _ in c.to_dict()) for c in x.values() if c != 0) == 2
print("(a)", out["a_V3_minus_1"], flush=True)


# (b)
def ncyc(p):
    seen, r = set(), 0
    for i in range(len(p)):
        if i not in seen:
            r += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return r


def comp(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


bad = {}
for n in range(3, 9):
    c = tuple([1, 2, 0] + list(range(3, n)))
    ci = tuple([2, 0, 1] + list(range(3, n)))
    bad[n] = sum(ncyc(comp((0,) + p, c)) != ncyc(comp((0,) + p, ci))
                 for p in itertools.permutations(range(1, n)))
out["b_cycle_count_failures"] = bad
assert all(v == 0 for v in bad.values())
print("(b)", bad, flush=True)

# (c)
V3 = [("S", 0), ("I", 1)] * 3
rows_c, ok_c = [], 0
for L in range(4):
    for t in itertools.product([1, 2], repeat=L):
        letters = [("S", i) for i in t]
        d = trace(4, letters + V3) - trace(4, letters)
        k = hol(d)[0] if d != 0 else None
        p = list(range(4))
        for i in t:
            p[i], p[i + 1] = p[i + 1], p[i]
        cyc_of = {}
        for s in range(4):
            j, cyc = s, []
            while j not in cyc:
                cyc.append(j)
                j = p[j]
            cyc_of[s] = frozenset(cyc)
        same = cyc_of[1] == cyc_of[2]
        good = (k == 3) == same
        ok_c += good
        rows_c.append({"word": list(t), "h_order": None if k is None else int(k),
                       "shared_strands_same_cycle": same, "rule_holds": good})
blocks = {}
for o in ("pp", "pn"):
    p = list(range(4))
    for _, i in F.atom_word(o, [], "over", start=1):
        p[i], p[i + 1] = p[i + 1], p[i]
    blocks[o[1]] = p
out["c_rule"] = f"{ok_c}/{len(rows_c)}"
out["c_rows"] = rows_c
out["c_block_perm_at_h0"] = blocks
assert ok_c == len(rows_c) and blocks["p"] == blocks["n"] == [0, 1, 3, 2]
print("(c)", out["c_rule"], blocks, flush=True)

# (d)
A2 = {}
for t in "pn":
    f = trace(4, F.atom_word("p" + t, [], "over", start=1))
    A2[t] = (f, trace(4, F.atom_word("p" + t, [(0, 1)], "over", start=1)) - f)
loc_ok = loc_n = 0
prod = {}
for order in ("".join(t) for t in itertools.product("pn", repeat=3)):
    free = trace(7, F.atom_word(order, [], "over", start=1))
    for v in ("over", "under"):
        single = {}
        for b in [(0, 1), (1, 2), (0, 2)]:
            single[b] = trace(7, F.atom_word(order, [b], v, start=1))
            f2, d2 = A2[order[b[1]]]
            loc_ok += ((single[b] - free) * f2 - d2 * free) == 0
            loc_n += 1
        for bonds in [[(0, 1), (1, 2)], [(0, 1), (0, 2)], [(0, 2), (1, 2)],
                      [(0, 1), (1, 2), (0, 2)]]:
            atom = trace(7, F.atom_word(order, bonds, v, start=1))
            P = single[bonds[0]]
            for b in bonds[1:]:
                P = P * single[b]
            X = atom * free ** (len(bonds) - 1) - P
            k, lead = hol(X) if X != 0 else (None, 0)
            key = str(bonds)
            rel = None if k is None else f"({lead}) / ({at_h0(free) ** len(bonds)})"
            prod.setdefault(key, set()).add((None if k is None else int(k), rel))
    print(f"[{time.time() - T0:5.1f}s] (d) {order}", flush=True)
out["d_single_bond_equals_A2"] = f"{loc_ok}/{loc_n}"
out["d_product_rule_deviation"] = {k: sorted(map(list, v), key=str) for k, v in prod.items()}
assert loc_ok == loc_n
print("(d)", out["d_single_bond_equals_A2"], out["d_product_rule_deviation"], flush=True)

with open(os.path.join(HERE, "bond-structure.witness.json"), "w") as fh:
    json.dump({"description": __doc__.strip(), "engine": "python-flint exact Q[h, z]",
               "exploratory": True, **out}, fh, indent=1)
