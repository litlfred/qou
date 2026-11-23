"""a3_bonds_generic_z_probe.py: Rule B at A = 3 with the Markov parameter z left FREE
(exploratory; follows bond_generic_z_probe, not preregistered).

Prediction, written before this probe was run, from the A = 2 identities
(prop:light-nuclei-a2-bond-tail): bonds add to leading order in h, a bond into a proton
contributing (1 - z^2)/2 at order h^4 and a bond into a neutron (1 - z^2)/z at order h^5. So

    ratio - 1 = n_into_p (1 - z^2)/2 h^4 + O(h^5)   if n_into_p > 0,
              = n_bonds  (1 - z^2)/z h^5 + O(h^6)   otherwise.

At z = 1/2 this is Rule B of bond_leading_order_probe (3/8 and 3/2). Here it is tested as a
polynomial identity in z, on every A = 3 order and four bond sets, over and under transport.

Exact: letter coefficients in Q[h], basis traces in Z[h, z] (hecke_flint.trT), so the trace
is a polynomial in Q[h, z]. Block 0 factors out (towerTr_disjoint), so the tail suffices.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import flint  # noqa: E402

import hecke_flint as F  # noqa: E402

T0 = time.time()
CTX = flint.fmpq_mpoly_ctx.get(("h", "z"), "lex")
H, Z = CTX.gens()
ONE = CTX.from_dict({(0, 0): 1})
B = {"S": None, "I": -H, "A": -H / 2}


def mul_letter(x, kind, i):
    b = B[kind]
    out = {}
    for w, c in x.items():
        if b is not None:
            out[w] = out.get(w, 0) + c * b
        l = list(w)
        up = l[i] < l[i + 1]
        l[i], l[i + 1] = l[i + 1], l[i]
        u = tuple(l)
        out[u] = out.get(u, 0) + c
        if not up:
            out[w] = out.get(w, 0) + c * H
    return {w: c for w, c in out.items() if c != 0}


def trace(n, letters):
    x = {tuple(range(n)): ONE}
    for kind, i in letters:
        x = mul_letter(x, kind, i)
    s = CTX.from_dict({})
    for w, c in x.items():
        s += c * CTX.from_dict({k: int(v) for k, v in F.trT(w).to_dict().items()})
    return s


def h_order_and_lead(d):
    """Lowest power k of h in d, and the coefficient of h^k as a polynomial in z."""
    terms = d.to_dict()
    k = min(a for a, _ in terms)
    lead = CTX.from_dict({(0, b): c for (a, b), c in terms.items() if a == k})
    return k, lead


def at_h0(p):
    return CTX.from_dict({(0, b): c for (a, b), c in p.to_dict().items() if a == 0})


BOND_SETS = [[(0, 1), (1, 2)], [(0, 1), (1, 2), (0, 2)], [(0, 2), (1, 2)], [(0, 2)]]
rows, ok, total = [], 0, 0
for order in ("".join(t) for t in itertools.product("pn", repeat=3)):
    n = 3 * len(order) - 2
    free = trace(n, F.atom_word(order, [], "over", start=1))
    f0 = at_h0(free)
    for bonds in BOND_SETS:
        for v in ("over", "under"):
            atom = trace(n, F.atom_word(order, bonds, v, start=1))
            k, lead = h_order_and_lead(atom - free)
            n_p = sum(1 for _, j in bonds if order[j] == "p")
            if n_p:
                pk, pred = 4, n_p * (1 - Z * Z) / 2 * f0
            else:
                pk, pred = 5, len(bonds) * (1 - Z * Z) * f0
                # (1 - z^2)/z times f0; f0 is a multiple of z, checked below
                pred = CTX.from_dict({(0, b - 1): c for (a, b), c in pred.to_dict().items()})
            good = (k == pk and lead == pred)
            ok += good
            total += 1
            rows.append({"order": order, "bonds": bonds, "variant": v, "h_order": int(k),
                         "lead_over_free_at_h0": f"({lead}) / ({f0})", "predicted_order": pk,
                         "match": good})
            print(f"[{time.time() - T0:6.1f}s] {order} {bonds} {v:5s} h^{k} lead={lead} "
                  f"free0={f0} {'ok' if good else 'NO'}", flush=True)
checks = {"rule_B_generic_z": f"{ok}/{total}"}
print(checks)
assert ok == total
with open(os.path.join(HERE, "a3-bonds-generic-z.witness.json"), "w") as fh:
    json.dump({"q0Anchor": "independent",
               "q0AnchorReason": "exact polynomial arithmetic in Q[h, z] with h and the Markov parameter z left free; q0 is never read",
               "description": __doc__.strip(), "engine": "python-flint exact Q[h, z]",
               "exploratory": True, "checks": checks, "rows": rows}, fh, indent=1)
