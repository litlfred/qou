"""qou-99qc, pre-registration ε-W1: word-level ε from the emission process.

Pre-registered in bean qou-99qc (2026-11-15 22:36Z) before computing.
Space (C²)^⊗3 ⊗ V ⊗ V* (32-dim), as in word_dressing_chirality_probe (#7981).
State N ⊗ coev_45 (plain), N = |udd> or |udd>+|dud>+|ddu>. Apply X on the
quark strands, then the emission crossing Ř on strands (3,4) (#7973 arm A).
A(X) = sum of components on {two u, one d on 1-3} ⊗ (d on 4, u on 5).
eps_W = A(Delta_S · V^k) / A(V^k), k = 3, 6. Q = |eps_W|·E0·m_e, E0 = 1/(q(q-1)).
Also checks Delta_S = -(q h [2]/4)(W1 + W2). Exact sympy; q0 only for display.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import h, q  # noqa: E402
from word_dressing_chirality_probe import I2, S, Sinv, U, D, idx, kr, on_quarks, vertex  # noqa: E402

Q2 = q + 1 / q
Q0 = sp.Rational(1109978582751381, 10**15)  # proton pin, display only
Q0_STR = "1.109978582751381"  # decimal text of Q0, recorded as the witness q0Value
assert sp.Rational(Q0_STR) == Q0
ME = sp.Rational("0.51099895069")
QB_CODATA = sp.Rational("0.78233")


def apply(M, v):
    return (M * v).applyfunc(sp.cancel)


def deltaS_op():
    s1, s2 = on_quarks(S, 1), on_quarks(S, 2)
    return h**2 / 2 * sp.eye(32) - h / 2 * (s1 + s2)


def word_ops(word):
    return [on_quarks(S if L > 0 else Sinv, abs(L)) for L in word]


def amplitude(N, ops):
    psi = sp.zeros(32, 1)
    for bits in N:
        for i in (0, 1):
            psi[idx(list(bits) + [i, i])] += 1
    for M in ops:
        psi = apply(M, psi)
    psi = apply(kr(I2, I2, S, I2), psi)
    amp = sum(psi[idx([a, b, c, D, U])] for a in (0, 1) for b in (0, 1) for c in (0, 1)
              if [a, b, c].count(U) == 2)
    return sp.factor(sp.cancel(amp))


def main():
    W = vertex(False)
    I8 = sp.eye(8)
    DS8 = h**2 / 2 * I8 - h / 2 * (kr(S, I2) + kr(I2, S))
    ident = (DS8 + q * h * Q2 / 4 * (kr(W, I2) + kr(I2, W))).applyfunc(sp.simplify) == sp.zeros(8)
    states = {"|udd>": [(U, D, D)], "T3=-1/2 sum": [(U, D, D), (D, U, D), (D, D, U)]}
    words = {"V^3": [1, -2] * 3, "V^6": [1, -2] * 6}
    DS = deltaS_op()
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    rows = []
    for wn, w in words.items():
        ops = word_ops(w)
        for sn, N in states.items():
            a0 = amplitude(N, ops)
            a1 = amplitude(N, ops + [DS])
            eps = sp.factor(sp.cancel(a1 / a0)) if a0 != 0 else None
            row = {"word": wn, "state": sn, "A_word": str(a0), "A_DeltaS_word": str(a1),
                   "eps_W": str(eps), "eps_W_equals_minus_h": bool(eps is not None and sp.simplify(eps + h) == 0)}
            if eps is not None:
                Qv = sp.N((sp.Abs(eps) * E0 * ME).subs(q, Q0), 12)
                row.update({"eps_W_at_q0": str(sp.N(eps.subs(q, Q0), 12)), "Q_MeV_at_q0": str(Qv),
                            "Q_vs_codata_pct": str(sp.N((Qv / QB_CODATA - 1) * 100, 6))})
            rows.append(row)
    res = {"producer": "computations/probes/word_level_epsilon_probe.py", "bean": "qou-99qc",
           "arithmetic": "exact (sympy over Q(q)); q0 and m_e only for display",
           "q0_anchor": "proton (display only)",
           "q0Anchor": "proton", "q0Value": Q0_STR,
           "q0AnchorReason": "all published results are exact over Q(q); q0 enters only the display-only *_q0 fields, evaluated at word_level_epsilon_probe.Q0 = the proton pin truncated to 16 significant digits",
                      "checks": {"DeltaS_eq_minus_qh2over4_W1_plus_W2": bool(ident)},
           "rows": rows}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("word-level-epsilon.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
