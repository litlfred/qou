"""qou-99qc, pre-registration ε-TR1: ε as a trace over the isospin-1/2 multiplicity space.

Pre-registered in bean qou-99qc (2026-11-15 23:32Z) before computing.
M(X)_ij = coordinate i (basis p_A, p_B of the T=1/2 part, along the T=3/2 line) of the
quark part of the (d on 4, u on 5) component of Ř34·X·V^k·(n_j ⊗ coev).
ε_tr = Tr M(Δ_S) / Tr M(1); p->n mirrored. Exact sympy; q0 display only; no data.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import q  # noqa: E402
from word_dressing_chirality_probe import PL, PR, U, D, idx, kr, on_quarks  # noqa: E402
from word_level_epsilon_probe import Q0_STR, Q0, apply, deltaS_op, word_ops  # noqa: E402
from neutron_vector_epsilon_probe import EMIT, coprod3, lift, vec3, vec3_2  # noqa: E402


def quark_part(psi, pair):
    return sp.Matrix([psi[idx([(n >> 2) & 1, (n >> 1) & 1, n & 1, pair[0], pair[1]])] for n in range(8)])


def coords(v, basis):
    B = sp.Matrix.hstack(*basis)
    sol = B.solve(v) if B.shape[0] == B.shape[1] else (B.T * B).inv() * B.T * v
    return sol.applyfunc(sp.cancel)


def restrict(v, weight_idx):
    return sp.Matrix([v[i] for i in weight_idx])


def Mmat(init, final_basis3, final_idx, ops, X, pair):
    cols = []
    for v in init:
        psi = lift(v)
        for Op in ops + X + [EMIT]:
            psi = apply(Op, psi)
        c = restrict(quark_part(psi, pair), final_idx)
        cols.append(coords(c, [restrict(b, final_idx) for b in final_basis3])[:2, 0])
    return sp.Matrix.hstack(*cols)


def main():
    E3, F3 = coprod3()
    ud = PR * vec3_2({(U, D): 1})
    nA = sp.Matrix(kr(ud, sp.Matrix([0, 1])))
    nB = sp.Matrix(kr(sp.Matrix([0, 1]), ud))
    pA, pB = (E3 * nA).applyfunc(sp.cancel), (E3 * nB).applyfunc(sp.cancel)
    uuu = vec3({(U, U, U): 1})
    s_plus = (F3 * uuu).applyfunc(sp.cancel)
    s_minus = (F3 * s_plus).applyfunc(sp.cancel)
    w_plus = [i for i in range(8) if bin(i).count("1") == 1]   # two u (index 0 = u)
    w_minus = [i for i in range(8) if bin(i).count("1") == 2]  # one u
    DS = deltaS_op()
    J = PL - PR
    rows = []
    for k in (0, 3, 6):
        ops = word_ops([1, -2] * k)
        for xn, X in {"none": [], "J23": [on_quarks(J, 2)]}.items():
            r = {"word": f"V^{k}", "X": xn}
            for dn, init, fb, fi, pair in [("n->p", [nA, nB], [pA, pB, s_plus], w_plus, (D, U)),
                                           ("p->n", [pA, pB], [nA, nB, s_minus], w_minus, (U, D))]:
                M0 = Mmat(init, fb, fi, ops, [], pair)
                M1 = Mmat(init, fb, fi, ops, [DS] + X, pair)
                t0, t1 = sp.cancel(M0.trace()), sp.cancel(M1.trace())
                e = sp.factor(sp.cancel(t1 / t0)) if t0 != 0 else None
                r[dn] = {"Tr_M1": str(sp.factor(t0)), "eps_tr": str(e),
                         "eps_tr_q0": str(sp.N(e.subs(q, Q0), 10)) if e is not None else None}
            en, ep = sp.sympify(r["n->p"]["eps_tr"], locals={"q": q}), sp.sympify(r["p->n"]["eps_tr"], locals={"q": q})
            if r["n->p"]["eps_tr"] != "None" and r["p->n"]["eps_tr"] != "None":
                rat = sp.factor(sp.cancel(ep / en))
                r["ratio_pn_np"] = str(rat)
                r["ratio_q0"] = str(sp.N(rat.subs(q, Q0), 10))
            rows.append(r)
            print(json.dumps(r, ensure_ascii=False), flush=True)
    res = {"producer": "computations/probes/multiplicity_trace_epsilon_probe.py", "bean": "qou-99qc",
           "preregistration": "ε-TR1", "arithmetic": "exact (sympy over Q(q)); q0 only for display",
           "q0_anchor": "proton (display only)",
           "q0Anchor": "proton", "q0Value": Q0_STR,
           "q0AnchorReason": "all published results are exact over Q(q); q0 enters only the display-only *_q0 fields, evaluated at word_level_epsilon_probe.Q0 = the proton pin truncated to 16 significant digits",
           "rows": rows}
    pathlib.Path(__file__).with_name("multiplicity-trace-epsilon.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
