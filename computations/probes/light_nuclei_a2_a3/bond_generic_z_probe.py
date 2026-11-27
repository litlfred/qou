"""bond_generic_z_probe.py: the A = 2 bond, exactly over Z[h, z] with the Markov parameter z
left FREE (exploratory, follows bond_leading_order_probe; not preregistered).

By towerTr_disjoint (proved) block 0 factors out, so a single bond (0, 1) acts on a 4-strand
tail: the receiving block's word on sigma_1, sigma_2, then V^3 = (sigma_0 sigma_1^-1)^3.
Letters: S = sigma, I = sigma - h (= sigma^-1), A = sigma - h/2. Ocneanu trace with free z.

Measured: atom - free = h^4 (z^2 - h z - 1) P_p / 4 into a proton, and
h^5 (h^2+1)(h^2+4)(h z - h^2 - 1)(z^2 - h z - 1) / 4 into a neutron. Since y = q h, the
orders in y are 4 and 5, and the leading coefficients of ratio - 1 are (1 - z^2)/2 and
(1 - z^2)/z: 3/8 and 3/2 at z = z_D(1) = 1/2. Both vanish at z^2 - h z - 1 = 0, i.e.
z = q or z = -1/q.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sympy as sp  # noqa: E402

import hecke_flint as F  # noqa: E402

h, z = sp.symbols("h z")


def ev(n, letters):
    x = {tuple(range(n)): sp.Integer(1)}
    for kind, i in letters:
        b = {"S": 0, "I": -h, "A": -h / 2}[kind]
        out = {}
        for w, c in x.items():
            if b != 0:
                out[w] = out.get(w, 0) + c * b
            l = list(w)
            up = l[i] < l[i + 1]
            l[i], l[i + 1] = l[i + 1], l[i]
            u = tuple(l)
            out[u] = out.get(u, 0) + c
            if not up:
                out[w] = out.get(w, 0) + c * h
        x = out
    return sp.expand(sum(c * sp.sympify(str(F.trT(w)).replace("^", "**")) for w, c in x.items()))


def sh(w, d):
    return [(t, i + d) for t, i in w]


out, checks = {}, {}
for name, blk in (("into_proton", sh(F.proton(), 1)), ("into_neutron", sh(F.neutron(), 1))):
    free = ev(4, blk)
    diff = ev(4, blk + F.V3(0))
    diff = sp.expand(diff - free)
    k = 0
    while sp.rem(sp.Poly(diff, h), sp.Poly(h ** (k + 1), h)).is_zero:
        k += 1
    lead = sp.simplify((sp.expand(diff / h ** k)).subs(h, 0) / free.subs(h, 0))
    out[name] = {"free": str(sp.factor(free)), "atom_minus_free": str(sp.factor(diff)),
                 "h_order": k, "leading_coefficient_of_ratio_minus_1": str(lead),
                 "at_z_half": str(lead.subs(z, sp.Rational(1, 2)))}
    print(name, out[name], flush=True)
checks["proton_h4_3/8"] = out["into_proton"]["h_order"] == 4 and out["into_proton"]["at_z_half"] == "3/8"
checks["neutron_h5_3/2"] = out["into_neutron"]["h_order"] == 5 and out["into_neutron"]["at_z_half"] == "3/2"
print(checks)
assert all(checks.values())
with open(os.path.join(HERE, "bond-generic-z.witness.json"), "w") as fh:
    json.dump({"q0Anchor": "independent",
               "q0AnchorReason": "exact sympy polynomial arithmetic in Z[h, z] with formal h and z "
                                 "(specialised only to exact rational z = 1/2 at q = 1); q0 is never read",
               "description": __doc__.strip(), "engine": "sympy exact Z[h,z]", "exploratory": True,
               "results": out, "checks": checks}, fh, indent=1)
