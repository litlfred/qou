"""qou-99qc, pre-registration ε-L1: does the photon twist channel L± break u<->d?

Pre-registered in bean qou-99qc (2026-11-16 07:30Z) before computing.
Same traced setup as ε-TR1 (multiplicity_trace_epsilon_probe.Mmat), words built from
V = σ1σ2^-1, L+ = σ1σ2 (writhe +2, breit-wheeler-vertex), L- = σ1^-1σ2^-1.
Reports ε_tr for n->p and p->n and their ratio, exact over Q(q); q0 display only.
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

V, LP, LM = [1, -2], [1, 2], [-1, -2]
WORDS = {"L+": LP, "L-": LM, "L+V^3": LP + V * 3, "V^3L+": V * 3 + LP,
         "L+L-": LP + LM, "L+s1 (e- type)": LP + [1]}


def writhe(w):
    return sum(1 if g > 0 else -1 for g in w)


def main():
    E3, F3 = coprod3()
    ud = PR * vec3_2({(U, D): 1})
    nA = sp.Matrix(kr(ud, sp.Matrix([0, 1])))
    nB = sp.Matrix(kr(sp.Matrix([0, 1]), ud))
    pA, pB = (E3 * nA).applyfunc(sp.cancel), (E3 * nB).applyfunc(sp.cancel)
    uuu = vec3({(U, U, U): 1})
    s_plus = (F3 * uuu).applyfunc(sp.cancel)
    s_minus = (F3 * s_plus).applyfunc(sp.cancel)
    w_plus = [i for i in range(8) if bin(i).count("1") == 1]
    w_minus = [i for i in range(8) if bin(i).count("1") == 2]
    DS = deltaS_op()
    rows = []
    for name, w in WORDS.items():
        ops = word_ops(w)
        r = {"word": name, "letters": w, "writhe": writhe(w)}
        eps = {}
        for dn, init, fb, fi, pair in [("n->p", [nA, nB], [pA, pB, s_plus], w_plus, (D, U)),
                                       ("p->n", [pA, pB], [nA, nB, s_minus], w_minus, (U, D))]:
            t0 = sp.cancel(Mmat(init, fb, fi, ops, [], pair).trace())
            t1 = sp.cancel(Mmat(init, fb, fi, ops, [DS], pair).trace())
            e = sp.factor(sp.cancel(t1 / t0)) if t0 != 0 else None
            eps[dn] = e
            r[dn] = {"Tr_M1": str(sp.factor(t0)), "eps_tr": str(e),
                     "eps_tr_q0": str(sp.N(e.subs(q, Q0), 10)) if e is not None else None}
        if eps["n->p"] is not None and eps["p->n"] is not None:
            rat = sp.factor(sp.cancel(eps["p->n"] / eps["n->p"]))
            r["ratio_pn_np"] = str(rat)
            r["symmetric"] = bool(sp.simplify(rat - 1) == 0)
        rows.append(r)
        print(json.dumps(r, ensure_ascii=False), flush=True)
    res = {"producer": "computations/probes/gg_twist_channel_np_probe.py", "bean": "qou-99qc",
           "preregistration": "ε-L1", "arithmetic": "exact (sympy over Q(q)); q0 only for display",
           "q0_anchor": "proton (display only)", "rows": rows}
    pathlib.Path(__file__).with_name("gg-twist-channel-np.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
