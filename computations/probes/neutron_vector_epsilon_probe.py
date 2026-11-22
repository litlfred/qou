"""qou-99qc, pre-registrations ε-N1 and ε-J1.

Pre-registered in bean qou-99qc (2026-11-15 23:05Z) before computing.
ε-N1: the nucleon has isospin 1/2, so the neutron lies in ker F on the T3 = -1/2
weight space of V^{⊗3} (U_q(sl2), Δ(E) = E⊗K + 1⊗E, Δ(F) = F⊗1 + K⁻¹⊗F; both
commute with Ř 'std', checked). That kernel is 2-dim. The proton is p = E·n.
Report ε_np(n) and ε_pn(E n) on the whole family n = n_A + t n_B, where
n_A = [ud]_12 ⊗ d and n_B = d ⊗ [ud]_23 ([ud] = P- (u⊗d), the q-singlet pair).
ε-J1: the J23-dressed ratio ε_pn/ε_np for words V^0, V^1, V^2 (pre-registered states).
Exact sympy; q0 for display only; nothing compared to data.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import q  # noqa: E402
from word_dressing_chirality_probe import I2, I4, PL, PR, S, U, D, idx, kr, on_quarks  # noqa: E402
from word_level_epsilon_probe import Q0_STR, Q0, apply, deltaS_op, word_ops  # noqa: E402

t = sp.Symbol("t")
EMIT = kr(I2, I2, S, I2)
E1 = sp.Matrix([[0, 1], [0, 0]])
F1 = E1.T
K1 = sp.diag(q, 1 / q)
Ki1 = sp.diag(1 / q, q)


def coprod3():
    E3 = kr(E1, K1, K1) + kr(I2, E1, K1) + kr(I2, I2, E1)
    F3 = kr(F1, I2, I2) + kr(Ki1, F1, I2) + kr(Ki1, Ki1, F1)
    return E3, F3


def vec3(coeffs):
    v = sp.zeros(8, 1)
    for bits, c in coeffs.items():
        n = 0
        for b in bits:
            n = 2 * n + b
        v[n] += c
    return v


def lift(v8):
    """quark vector (8) ⊗ coev on 4,5 -> 32."""
    psi = sp.zeros(32, 1)
    for n in range(8):
        if v8[n] != 0:
            bits = [(n >> 2) & 1, (n >> 1) & 1, n & 1]
            for i in (0, 1):
                psi[idx(bits + [i, i])] += v8[n]
    return psi


def amp(v8, pre, post, n_u, pair):
    psi = lift(v8)
    for M in pre + [EMIT] + post:
        psi = apply(M, psi)
    a = sum(psi[idx([x, y, z, pair[0], pair[1]])] for x in (0, 1) for y in (0, 1)
            for z in (0, 1) if [x, y, z].count(U) == n_u)
    return sp.factor(sp.cancel(a))


def eps(v8, ops, X, n_u, pair):
    a0 = amp(v8, ops, [], n_u, pair)
    a1 = amp(v8, ops + [deltaS_op()] + X, [], n_u, pair)
    return sp.factor(sp.cancel(a1 / a0)) if a0 != 0 else None


def main():
    E3, F3 = coprod3()
    ud = (PR * vec3_2({(U, D): 1}))  # P- (u⊗d), a 4-vector
    nA = sp.Matrix(kr(ud, sp.Matrix([0, 1])))
    nB = sp.Matrix(kr(sp.Matrix([0, 1]), ud))
    checks = {
        "nA_in_kerF": (F3 * nA).applyfunc(sp.cancel) == sp.zeros(8, 1),
        "nB_in_kerF": (F3 * nB).applyfunc(sp.cancel) == sp.zeros(8, 1),
        "nA_nB_independent": sp.Matrix.hstack(nA, nB).rank() == 2,
        "sum_state_in_kerF": (F3 * vec3({(U, D, D): 1, (D, U, D): 1, (D, D, U): 1})).applyfunc(sp.cancel) == sp.zeros(8, 1),
        "udd_in_kerF": (F3 * vec3({(U, D, D): 1})).applyfunc(sp.cancel) == sp.zeros(8, 1),
    }
    print("checks", checks, flush=True)
    J = PL - PR
    rows = []
    for wn, w in {"V^3": [1, -2] * 3, "V^6": [1, -2] * 6}.items():
        ops = word_ops(w)
        for X_name, X in {"none": [], "J23": [on_quarks(J, 2)]}.items():
            n = nA + t * nB
            p = (E3 * n).applyfunc(sp.cancel)
            e_np = eps(n, ops, X, 2, (D, U))
            e_pn = eps(p, ops, X, 1, (U, D))
            r = {"part": "ε-N1", "word": wn, "X": X_name, "eps_np(t)": str(e_np), "eps_pn(t)": str(e_pn)}
            for tn, tv in {"nA (t=0)": 0, "nB (t=inf)": None, "t=1": 1, "t=-1": -1}.items():
                if tv is None:
                    en = eps(nB, ops, X, 2, (D, U))
                    ep = eps((E3 * nB).applyfunc(sp.cancel), ops, X, 1, (U, D))
                else:
                    en, ep = (e_np.subs(t, tv) if e_np is not None else None,
                              e_pn.subs(t, tv) if e_pn is not None else None)
                r[tn] = {"eps_np": str(sp.factor(en)) if en is not None else None,
                         "eps_pn": str(sp.factor(ep)) if ep is not None else None,
                         "eps_np_q0": str(sp.N(en.subs(q, Q0), 10)) if en is not None else None,
                         "eps_pn_q0": str(sp.N(ep.subs(q, Q0), 10)) if ep is not None else None,
                         "ratio_q0": str(sp.N((ep / en).subs(q, Q0), 10)) if en and ep else None}
            r["eps_np_depends_on_t"] = bool(e_np is not None and sp.diff(e_np, t) != 0)
            rows.append(r)
            print(wn, X_name, json.dumps({k: r[k] for k in r if k.startswith(("n", "t", "eps_np_dep"))}), flush=True)
    jrows = []
    states = {"single": ({(U, D, D): 1}, {(U, U, D): 1}),
              "T3 sum": ({(U, D, D): 1, (D, U, D): 1, (D, D, U): 1}, {(U, U, D): 1, (U, D, U): 1, (D, U, U): 1})}
    for k in (0, 1, 2):
        ops = word_ops([1, -2] * k)
        for sn, (cn, cp) in states.items():
            en = eps(vec3(cn), ops, [on_quarks(J, 2)], 2, (D, U))
            ep = eps(vec3(cp), ops, [on_quarks(J, 2)], 1, (U, D))
            rat = sp.factor(sp.cancel(ep / en)) if en and ep else None
            jr = {"part": "ε-J1", "word": f"V^{k}", "state": sn, "eps_np": str(en), "eps_pn": str(ep),
                  "ratio": str(rat), "ratio_equals_q": bool(rat is not None and sp.cancel(rat - q) == 0)}
            jrows.append(jr)
            print("J1", jr["word"], sn, jr["ratio"], jr["ratio_equals_q"], flush=True)
    res = {"producer": "computations/probes/neutron_vector_epsilon_probe.py", "bean": "qou-99qc",
           "preregistration": ["ε-N1", "ε-J1"], "arithmetic": "exact (sympy over Q(q)); q0 only for display",
           "q0_anchor": "proton (display only)",
           "q0Anchor": "proton", "q0Value": Q0_STR,
           "q0AnchorReason": "all published results are exact over Q(q); q0 enters only the display-only *_q0 fields, evaluated at word_level_epsilon_probe.Q0 = the proton pin truncated to 16 significant digits",
           "checks": checks, "rows_N1": rows, "rows_J1": jrows}
    pathlib.Path(__file__).with_name("neutron-vector-epsilon.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


def vec3_2(coeffs):
    v = sp.zeros(4, 1)
    for (a, b), c in coeffs.items():
        v[2 * a + b] += c
    return v


if __name__ == "__main__":
    main()
