"""qou-99qc, pre-registration ε-NP1: does the emission step break n<->p symmetry?

Pre-registered in bean qou-99qc (2026-11-15 22:45Z) before computing.
Same space and emission as word_level_epsilon_probe (ε-W1). n->p starts from
|udd> (or the T3=-1/2 sum) and projects onto (two u, one d) ⊗ (d on 4, u on 5).
The p->n mirror starts from |uud> (or the T3=+1/2 sum) and projects onto
(one u, two d) ⊗ (u on 4, d on 5). eps = A(Delta_S·V^k)/A(V^k).
H0: eps_pn = eps_np. H1: eps_pn(q) = eps_np(1/q). Exact sympy; no data compared.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import q  # noqa: E402
from word_dressing_chirality_probe import I2, S, U, D, idx, kr  # noqa: E402
from word_level_epsilon_probe import Q0_STR, Q0, apply, deltaS_op, word_ops  # noqa: E402


def amplitude(N, ops, n_u_final, pair):
    psi = sp.zeros(32, 1)
    for bits in N:
        for i in (0, 1):
            psi[idx(list(bits) + [i, i])] += 1
    for M in ops:
        psi = apply(M, psi)
    psi = apply(kr(I2, I2, S, I2), psi)
    amp = sum(psi[idx([a, b, c, pair[0], pair[1]])] for a in (0, 1) for b in (0, 1)
              for c in (0, 1) if [a, b, c].count(U) == n_u_final)
    return sp.factor(sp.cancel(amp))


def eps(N, ops, DS, n_u_final, pair):
    a0 = amplitude(N, ops, n_u_final, pair)
    a1 = amplitude(N, ops + [DS], n_u_final, pair)
    return (sp.factor(sp.cancel(a1 / a0)) if a0 != 0 else None), a0


def main():
    DS = deltaS_op()
    cases = {
        "single": ([(U, D, D)], [(U, U, D)]),
        "T3 sum": ([(U, D, D), (D, U, D), (D, D, U)], [(U, U, D), (U, D, U), (D, U, U)]),
    }
    words = {"V^3": [1, -2] * 3, "V^6": [1, -2] * 6}
    rows = []
    for wn, w in words.items():
        ops = word_ops(w)
        for cn, (Nn, Np) in cases.items():
            e_np, a_np = eps(Nn, ops, DS, 2, (D, U))
            e_pn, a_pn = eps(Np, ops, DS, 1, (U, D))
            row = {"word": wn, "state": cn, "eps_np": str(e_np), "eps_pn": str(e_pn),
                   "A_np": str(a_np), "A_pn": str(a_pn)}
            if e_np is not None and e_pn is not None:
                ratio = sp.factor(sp.cancel(e_pn / e_np))
                row.update({
                    "ratio_pn_over_np": str(ratio),
                    "H0_equal": bool(sp.cancel(e_pn - e_np) == 0),
                    "H1_q_to_1_over_q": bool(sp.cancel(e_pn - e_np.subs(q, 1 / q)) == 0),
                    "eps_np_at_q0": str(sp.N(e_np.subs(q, Q0), 12)),
                    "eps_pn_at_q0": str(sp.N(e_pn.subs(q, Q0), 12)),
                    "ratio_at_q0": str(sp.N(ratio.subs(q, Q0), 12)),
                })
            rows.append(row)
    res = {"producer": "computations/probes/np_emission_asymmetry_probe.py", "bean": "qou-99qc",
           "preregistration": "ε-NP1", "arithmetic": "exact (sympy over Q(q)); q0 only for display",
           "q0_anchor": "proton (display only)",
           "q0Anchor": "proton", "q0Value": Q0_STR,
           "q0AnchorReason": "all published results are exact over Q(q); q0 enters only the display-only *_q0 fields, evaluated at word_level_epsilon_probe.Q0 = the proton pin truncated to 16 significant digits",
           "rows": rows}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("np-emission-asymmetry.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
