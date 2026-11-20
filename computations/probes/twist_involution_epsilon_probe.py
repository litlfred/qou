"""qou-99qc, pre-registration ε-TW1: Δ_S followed by a twist or an involution.

Pre-registered in bean qou-99qc (2026-11-15 22:46Z) before computing.
Same process as np_emission_asymmetry_probe (ε-NP1). eps_X = A(X·Δ_S·V^k)/A(V^k),
X applied after Δ_S and before the emission crossing (F4: after the crossing).
X in {T23 = Ř² on 2,3; J23 = P+ - P- on 2,3; F3, Fall, F4 = u<->d flips}.
No prediction; nothing selected by closeness to -h or CODATA. Exact sympy.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import q  # noqa: E402
from word_dressing_chirality_probe import I2, PL, PR, S, U, D, idx, kr, on_quarks  # noqa: E402
from word_level_epsilon_probe import ME, Q0, QB_CODATA, apply, deltaS_op, word_ops  # noqa: E402,F401

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
FLIP = sp.Matrix([[0, 1], [1, 0]])
EMIT = kr(I2, I2, S, I2)


def amp(N, pre, post, n_u, pair):
    psi = sp.zeros(32, 1)
    for bits in N:
        for i in (0, 1):
            psi[idx(list(bits) + [i, i])] += 1
    for M in pre + [EMIT] + post:
        psi = apply(M, psi)
    a = sum(psi[idx([x, y, z, pair[0], pair[1]])] for x in (0, 1) for y in (0, 1)
            for z in (0, 1) if [x, y, z].count(U) == n_u)
    return sp.factor(sp.cancel(a))


def main():
    DS = deltaS_op()
    J = PL - PR  # P+ - P-: PL = (σ+q⁻¹)/[2] = P+, PR = (q-σ)/[2] = P-
    X = {
        "none": ([], []),
        "T23": ([on_quarks(S * S, 2)], []),
        "J23": ([on_quarks(J, 2)], []),
        "F3": ([kr(I2, I2, FLIP, I2, I2)], []),
        "Fall": ([kr(FLIP, FLIP, FLIP, I2, I2)], []),
        "F4": ([], [kr(I2, I2, I2, FLIP, I2)]),
    }
    assert (J * J - sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4)
    cases = {"single": ([(U, D, D)], [(U, U, D)]),
             "T3 sum": ([(U, D, D), (D, U, D), (D, D, U)], [(U, U, D), (U, D, U), (D, U, U)])}
    dirs = {"n->p": (0, 2, (D, U)), "p->n": (1, 1, (U, D))}
    words = {"V^3": [1, -2] * 3, "V^6": [1, -2] * 6}
    rows = []
    for wn, w in words.items():
        ops = word_ops(w)
        for cn, Ns in cases.items():
            for dn, (k, n_u, pair) in dirs.items():
                N = Ns[k]
                a0 = amp(N, ops, [], n_u, pair)
                for xn, (pre, post) in X.items():
                    a1 = amp(N, ops + [DS] + pre, post, n_u, pair)
                    e = sp.factor(sp.cancel(a1 / a0)) if a0 != 0 else None
                    r = {"word": wn, "state": cn, "dir": dn, "X": xn, "eps": str(e)}
                    if e is not None:
                        Qv = sp.N((sp.Abs(e) * E0 * ME).subs(q, Q0), 10)
                        r.update({"eps_at_q0": str(sp.N(e.subs(q, Q0), 10)),
                                  "Q_MeV_display": str(Qv),
                                  "Q_vs_codata_pct_display": str(sp.N((Qv / QB_CODATA - 1) * 100, 5))})
                    rows.append(r)
                    print(wn, cn, dn, xn, r.get("eps_at_q0"), r.get("Q_vs_codata_pct_display"), flush=True)
    res = {"producer": "computations/probes/twist_involution_epsilon_probe.py", "bean": "qou-99qc",
           "preregistration": "ε-TW1", "arithmetic": "exact (sympy over Q(q)); q0 only for display",
           "q0_anchor": "proton (display only)", "rows": rows}
    pathlib.Path(__file__).with_name("twist-involution-epsilon.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
