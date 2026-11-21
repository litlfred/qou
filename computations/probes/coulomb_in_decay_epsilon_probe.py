"""qou-99qc, pre-registration ε-EM1: Coulomb exchange in the decay's intermediate state.

Pre-registered in bean qou-99qc (2026-11-15 23:40Z) before computing.
As ε-TR1 (trace over the isospin-1/2 multiplicity space). Charge Q = T3 + Y/2 on V
(strands 1-4), Q = -(T3 + Y/2) of the index on the V* strand 5; Y is a SYMBOL.
X = sum_{a<b<=5} Q_a Q_b, inserted after Δ_S and before Ř34.
δε = Tr M(Δ_S, X) / Tr M(1) (first order in the coupling). Exact sympy; no data.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import q  # noqa: E402
from word_dressing_chirality_probe import PR, U, D, kr  # noqa: E402
from word_level_epsilon_probe import Q0, deltaS_op, word_ops  # noqa: E402
from neutron_vector_epsilon_probe import coprod3, vec3, vec3_2  # noqa: E402
from multiplicity_trace_epsilon_probe import Mmat  # noqa: E402

Y = sp.Symbol("Y")


def coulomb():
    X = sp.zeros(32, 32)
    for n in range(32):
        bits = [(n >> (4 - k)) & 1 for k in range(5)]
        Qs = [(sp.Rational(1, 2) if b == U else -sp.Rational(1, 2)) + Y / 2 for b in bits]
        Qs[4] = -Qs[4]
        X[n, n] = sum(Qs[a] * Qs[b] for a in range(5) for b in range(a + 1, 5))
    return X


def main():
    E3, F3 = coprod3()
    ud = PR * vec3_2({(U, D): 1})
    nA = sp.Matrix(kr(ud, sp.Matrix([0, 1])))
    nB = sp.Matrix(kr(sp.Matrix([0, 1]), ud))
    pA, pB = (E3 * nA).applyfunc(sp.cancel), (E3 * nB).applyfunc(sp.cancel)
    s_plus = (F3 * vec3({(U, U, U): 1})).applyfunc(sp.cancel)
    s_minus = (F3 * s_plus).applyfunc(sp.cancel)
    w_plus = [i for i in range(8) if bin(i).count("1") == 1]
    w_minus = [i for i in range(8) if bin(i).count("1") == 2]
    DS, X = deltaS_op(), coulomb()
    rows = []
    for k in (0, 3, 6):
        ops = word_ops([1, -2] * k)
        r = {"word": f"V^{k}"}
        vals = {}
        for dn, init, fb, fi, pair in [("n->p", [nA, nB], [pA, pB, s_plus], w_plus, (D, U)),
                                       ("p->n", [pA, pB], [nA, nB, s_minus], w_minus, (U, D))]:
            t0 = sp.cancel(Mmat(init, fb, fi, ops, [], pair).trace())
            t1 = sp.cancel(Mmat(init, fb, fi, ops, [DS], pair).trace())
            tX = sp.cancel(Mmat(init, fb, fi, ops, [DS, X], pair).trace())
            eps, deps = sp.cancel(t1 / t0), sp.cancel(tX / t0)
            rel = sp.factor(sp.cancel(deps / eps))
            vals[dn] = rel
            r[dn] = {"eps_tr": str(sp.factor(eps)), "d_eps": str(sp.factor(deps)),
                     "d_eps_over_eps": str(rel), "d_eps_over_eps_at_q1": str(sp.factor(sp.limit(rel, q, 1))),
                     "d_eps_over_eps_q0_Y_third": str(sp.N(rel.subs({q: Q0, Y: sp.Rational(1, 3)}), 10))}
        diff = sp.factor(sp.cancel(vals["p->n"] - vals["n->p"]))
        r["asym_rel_pn_minus_np"] = str(diff)
        r["asym_at_q1"] = str(sp.factor(sp.limit(diff, q, 1)))
        r["asym_Y_coeffs"] = {str(i): str(sp.factor(c)) for i, c in enumerate(sp.Poly(sp.numer(sp.together(diff)), Y).all_coeffs()[::-1])}
        rows.append(r)
        print(json.dumps(r, ensure_ascii=False), flush=True)
    res = {"producer": "computations/probes/coulomb_in_decay_epsilon_probe.py", "bean": "qou-99qc",
           "preregistration": "ε-EM1", "arithmetic": "exact (sympy over Q(q, Y)); q0, Y=1/3 display only",
           "q0_anchor": "proton (display only)",
           "q0Anchor": "proton",
           "q0AnchorReason": "algebra is exact over Q(q, Y); the only numeric column (d_eps_over_eps_q0_Y_third) substitutes Q0 from word_level_epsilon_probe, a 16-digit rational of the proton pin",
           "q0Value": "1.109978582751381",
           "rows": rows}
    pathlib.Path(__file__).with_name("coulomb-in-decay-epsilon.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
