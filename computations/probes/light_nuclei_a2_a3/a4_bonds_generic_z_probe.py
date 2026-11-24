"""a4_bonds_generic_z_probe.py: Rule B at A = 4 with the Markov parameter z left FREE
(exploratory; follows a3_bonds_generic_z_probe, not preregistered).

Prediction, written before this probe was run, the same rule as at A = 3: bonds add to
leading order in h, a bond (i, j) counted as a bond into nucleon j. So

    ratio - 1 = n_into_p (1 - z^2)/2 h^4 + O(h^5)   if n_into_p > 0,
              = n_bonds  (1 - z^2)/z h^5 + O(h^6)   otherwise,

with n_into_p the number of bonds (i, j) with order[j] = "p". Tested as a polynomial
identity in z on all 16 orders, over and under transport, for the gamma-gamma chain, the
four all-pairs formation routes of he4_all_pairs_exact_probe (bond placement: after the
running maximum of j, as there), and two non-chain sets.

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


BOND_SETS = {
    "chain": [(0, 1), (1, 2), (2, 3)],
    "D+D pairing a": [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
    "D+D pairing b": [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
    "3H+p": [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
    "3He+n": [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
    "02+13": [(0, 2), (1, 3)],
    "13": [(1, 3)],
}
def run_order(order):
    n = 3 * len(order) - 2
    free = trace(n, F.atom_word(order, [], "over", start=1))
    f0 = at_h0(free)
    out = []
    for name, bonds in BOND_SETS.items():
        for v in ("over", "under"):
            atom = trace(n, F.atom_word(order, bonds, v, start=1))
            k, lead = h_order_and_lead(atom - free)
            n_p = sum(1 for _, j in bonds if order[j] == "p")
            if n_p:
                pk, pred = 4, n_p * (1 - Z * Z) / 2 * f0
            else:
                pk, pred = 5, len(bonds) * (1 - Z * Z) * f0
                pred = CTX.from_dict({(0, b - 1): c for (a, b), c in pred.to_dict().items()})
            good = (k == pk and lead == pred)
            out.append({"order": order, "bonds_name": name, "bonds": bonds, "variant": v,
                        "h_order": int(k), "lead": str(lead), "free_at_h0": str(f0),
                        "predicted_order": pk, "predicted_lead": str(pred), "match": good})
            print(f"[{time.time() - T0:6.1f}s] {order} {name:13s} {v:5s} h^{k} lead={lead} "
                  f"free0={f0} {'ok' if good else 'NO'}", flush=True)
    return out


if __name__ == "__main__":
    import multiprocessing as mp_
    orders = ["".join(t) for t in itertools.product("pn", repeat=4)]
    with mp_.get_context("fork").Pool(int(os.environ.get("NPROC", "4"))) as pool:
        rows = [r for part in pool.map(run_order, orders, chunksize=1) for r in part]
    ok, total = sum(r["match"] for r in rows), len(rows)
    checks = {"rule_B_generic_z_A4": f"{ok}/{total}"}
    print(checks)
    with open(os.path.join(HERE, "a4-bonds-generic-z.witness.json"), "w") as fh:
        json.dump({"q0Anchor": "independent",
                   "q0AnchorReason": "exact fmpq_mpoly arithmetic in Q[h, z] with both h = q - q^-1 "
                                     "and the Markov parameter z formal; q0 is never read",
                   "description": __doc__.strip(), "engine": "python-flint exact Q[h, z]",
                   "exploratory": True, "checks": checks, "rows": rows}, fh, indent=1)
