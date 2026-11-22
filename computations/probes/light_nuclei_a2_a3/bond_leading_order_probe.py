"""bond_leading_order_probe.py: leading order at q = 1 of ratio - 1 = tr_atom/tr_free - 1,
per bond and per bond set (exploratory, measured after he4_all_pairs_exact_probe; not
preregistered). Exact in Q(q) via hecke_flint. y = q^2 - 1.

Two candidate rules, both "bonds act additively to leading order" (conjectures, not theorems):
  rule A (written first): a like-proton pair bond gives (3/8) y^4, any other bond (3/2) y^5.
  rule B (written after rule A failed on the CASES below): a bond entering a PROTON block
         (block j of bond (i, j), right closure) gives (3/8) y^4; a bond entering a neutron
         block gives (3/2) y^5. So ratio - 1 = (3/8) n_into_p y^4 + O(y^5) if n_into_p > 0,
         else (3/2) n_bonds y^5 + O(y^6).
Rule B was read off CASES, so CASES cannot test it. HOLDOUT was written down with rule B
before it was run; only HOLDOUT tests rule B. Nothing is fitted; every case is printed.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import flint  # noqa: E402

import hecke_flint as F  # noqa: E402

T0 = time.time()
Qp = flint.fmpq_poly([0, 1])
Y = Qp * Qp - 1
ONE = flint.fmpq(1)

CASES = [
    ("pp", [(0, 1)]), ("pn", [(0, 1)]), ("np", [(0, 1)]), ("nn", [(0, 1)]),
    ("ppn", [(0, 1)]), ("ppn", [(0, 2)]), ("ppn", [(1, 2)]),
    ("pnp", [(0, 2)]), ("pnn", [(0, 1), (1, 2)]), ("pnn", [(0, 1), (1, 2), (0, 2)]),
    ("ppn", [(0, 1), (0, 2), (1, 2)]), ("pnp", [(0, 1), (1, 2), (0, 2)]),
    ("ppp", [(0, 1), (1, 2)]), ("ppp", [(0, 1), (1, 2), (0, 2)]),
]
HOLDOUT = [
    ("npp", [(0, 1), (1, 2), (0, 2)]), ("nnp", [(0, 2), (1, 2)]), ("npn", [(0, 1), (1, 2)]),
    ("nnn", [(0, 1), (1, 2), (0, 2)]),
    ("pnpn", [(0, 1), (1, 2), (2, 3)]), ("nnpp", [(0, 1), (1, 2), (2, 3)]),
    ("npnp", [(0, 3), (1, 2)]), ("pnnp", [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
]


def leading(order, bonds, variant):
    # towerTr_disjoint: block 0 factors out of atom and free alike, so the tail suffices
    n = 3 * len(order) - 2
    num, den = F.div_num(F.tr(n, F.atom_word(order, bonds, variant, start=1)),
                         F.tr(n, F.atom_word(order, [], variant, start=1)))
    D, k = num - den, 0
    while D != 0 and D % Y == 0:
        D, k = D // Y, k + 1
    return k, Fraction(str(D(ONE) / den(ONE)))


def rule(n, k):
    return (4, Fraction(3, 8) * n) if n else (5, Fraction(3, 2) * k)


def rule_A(order, bonds):
    return rule(sum(1 for i, j in bonds if order[i] == order[j] == "p"), len(bonds))


def rule_B(order, bonds):
    return rule(sum(1 for _, j in bonds if order[j] == "p"), len(bonds))


rows, tally = [], {}
for kind, cases in (("cases", CASES), ("holdout", HOLDOUT)):
    for order, bonds in cases:
        for v in ("over", "under"):
            m = leading(order, bonds, v)
            a, b = rule_A(order, bonds), rule_B(order, bonds)
            for name, r in (("A", a), ("B", b)):
                t = tally.setdefault(f"rule_{name}_{kind}", [0, 0])
                t[0] += (m == r)
                t[1] += 1
            rows.append({"set": kind, "order": order, "bonds": bonds, "variant": v,
                         "y_power": m[0], "coefficient": str(m[1]),
                         "rule_A": [a[0], str(a[1])], "rule_B": [b[0], str(b[1])]})
            print(f"[{time.time() - T0:6.1f}s] {kind:7s} {order} {bonds} {v:5s} y^{m[0]} * {m[1]}"
                  f"  A {'ok' if m == a else 'no'}  B {'ok' if m == b else 'no'}", flush=True)
tally = {k: f"{v[0]}/{v[1]}" for k, v in tally.items()}
print(tally)
with open(os.path.join(HERE, "bond-leading-order.witness.json"), "w") as fh:
    json.dump({"q0Anchor": "independent",
               "q0AnchorReason": "exact fmpq_poly arithmetic in Q(q), leading order read off at q = 1 "
                                 "(y = q^2 - 1); q0 is never read",
               "description": __doc__.strip(), "engine": "python-flint exact Q(q)",
               "exploratory": True, "tally_agreeing_over_total": tally, "rows": rows},
              fh, indent=1)
