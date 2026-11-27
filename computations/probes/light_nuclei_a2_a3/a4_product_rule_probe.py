"""a4_product_rule_probe.py: locality and the product rule for gamma-gamma bonds at A = 4,
with the Markov parameter z left FREE (exploratory; follows bond_structure_probe (d), which
found both rules at A = 3; not preregistered).

Predictions, written before this probe was run, extrapolated from A = 3:

(L) Locality. A single bond (i, j) inside the A = 4 word changes the trace by exactly the
    A = 2 ratio for the type of nucleon j: (single - free) f2 = d2 free, at every order.
(P) Product rule. For a bond set S, X = atom free^(|S|-1) - prod_{b in S} single_b is
    exactly 0 when no two bonds of S go into the same nucleon. Otherwise X starts at h^6
    and X / free^|S| has leading coefficient m (1 - z^2), m = number of unordered pairs
    of bonds in S with the same receiving nucleon j.

Tested as polynomial identities in z on all 16 orders, over and under transport, for all
15 two-bond sets, the chain, the three-into-one set, two disjoint-receiver sets, and the
four all-pairs formation routes of he4_all_pairs_exact_probe. Exact over Q[h, z].
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
exec(_src, _g)  # reuse trace / h_order_and_lead / at_h0 without running that probe
F, Z = _g["F"], _g["Z"]
trace, hol, at_h0 = _g["trace"], _g["h_order_and_lead"], _g["at_h0"]
T0 = time.time()

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
SETS = {str(list(s)): list(s) for s in itertools.combinations(PAIRS, 2)}
SETS.update({
    "chain": [(0, 1), (1, 2), (2, 3)],
    "three into 3": [(0, 3), (1, 3), (2, 3)],
    "01+23": [(0, 1), (2, 3)],
    "02+13": [(0, 2), (1, 3)],
    "D+D pairing a": [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
    "D+D pairing b": [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
    "3H+p": [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
    "3He+n": [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
})
A2 = {}


def a2():
    for t in "pn":
        f = trace(4, F.atom_word("p" + t, [], "over", start=1))
        A2[t] = (f, trace(4, F.atom_word("p" + t, [(0, 1)], "over", start=1)) - f)


def run_order(order):
    if not A2:
        a2()
    n = 3 * len(order) - 2
    free = trace(n, F.atom_word(order, [], "over", start=1))
    f0 = at_h0(free)
    rows = []
    for v in ("over", "under"):
        single = {}
        for b in PAIRS:
            single[b] = trace(n, F.atom_word(order, [b], v, start=1))
            f2, d2 = A2[order[b[1]]]
            rows.append({"kind": "L", "order": order, "variant": v, "bond": b,
                         "match": ((single[b] - free) * f2 - d2 * free) == 0})
        for name, S in SETS.items():
            atom = trace(n, F.atom_word(order, S, v, start=1))
            P = single[S[0]]
            for b in S[1:]:
                P = P * single[b]
            X = atom * free ** (len(S) - 1) - P
            m = sum(1 for a, b in itertools.combinations(S, 2) if a[1] == b[1])
            if X == 0:
                k, rel = None, None
                good = (m == 0)
            else:
                k, lead = hol(X)
                good = (m > 0 and k == 6 and lead == m * (1 - Z * Z) * f0 ** len(S))
                rel = f"({lead}) / ({f0 ** len(S)})"
            rows.append({"kind": "P", "order": order, "variant": v, "set": name, "bonds": S,
                         "m_same_receiver_pairs": m, "h_order": None if k is None else int(k), "relative_lead": rel,
                         "match": good})
    print(f"[{time.time() - T0:7.1f}s] {order} done, "
          f"{sum(r['match'] for r in rows)}/{len(rows)} match", flush=True)
    return rows


if __name__ == "__main__":
    import multiprocessing as mp_
    orders = ["".join(t) for t in itertools.product("pn", repeat=4)]
    with mp_.get_context("fork").Pool(int(os.environ.get("NPROC", "4"))) as pool:
        rows = [r for part in pool.map(run_order, orders, chunksize=1) for r in part]
    L = [r for r in rows if r["kind"] == "L"]
    P = [r for r in rows if r["kind"] == "P"]
    misses = [r for r in P if not r["match"]]
    checks = {"locality_A4": f"{sum(r['match'] for r in L)}/{len(L)}",
              "product_rule_A4": f"{sum(r['match'] for r in P)}/{len(P)}"}
    print(checks)
    for r in misses[:40]:
        print("MISS", r["order"], r["variant"], r["set"], r["m_same_receiver_pairs"],
              r["h_order"], r["relative_lead"])
    with open(os.path.join(HERE, "a4-product-rule.witness.json"), "w") as fh:
        json.dump({"q0Anchor": "independent",
                   "q0AnchorReason": "exact fmpq_mpoly arithmetic in Q[h, z] with both h = q - q^-1 "
                                     "and the Markov parameter z formal; q0 is never read",
                   "description": __doc__.strip(), "engine": "python-flint exact Q[h, z]",
                   "exploratory": True, "checks": checks, "rows": rows}, fh, indent=1,
                  default=lambda o: int(o) if hasattr(o, "bit_length") or type(o).__name__ == "fmpz" else list(o))
