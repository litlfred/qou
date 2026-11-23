"""qou-g0jn, pre-registration 7: emission read as the R-check coefficient of the vertex.

Pre-registered in bean qou-g0jn (2026-11-15 20:33Z) before computing.
At site k write the vertex W in the basis {1, letter_k}: W = a_k + b_k * letter_k.
Reading B: emission at site k = b_k * (unchanged word), so
A_w = (sum_k b_k) * T_w[d, d], with T_w the closed trace of RESULT 6.
Also checks W_corpus = q^-1 J and W_mirror = q J, J = P_+ - P_-.
Exact sympy, no floats.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import h, q  # noqa: E402
from word_dressing_chirality_probe import I4, D, PL, PR, S, Sinv, vertex  # noqa: E402
from closed_trace_chirality_probe import close12, on3  # noqa: E402

Q0 = sp.Rational(1109978582751381, 10**15)  # proton pin, display only


def basis_coeffs(W, L):
    """Solve W = a*1 + b*L exactly (4x4)."""
    a, b = sp.symbols("a b")
    sol = sp.solve(list((W - a * I4 - b * L).applyfunc(sp.simplify)), [a, b], dict=True)
    assert len(sol) == 1, "vertex not in span{1, letter}"
    return sp.simplify(sol[0][a]), sp.simplify(sol[0][b])


def word_op(word):
    M = sp.eye(8)
    for L in word:
        M = on3(S if L > 0 else Sinv, abs(L)) * M
    return M


def main():
    J = (PL - PR).applyfunc(sp.simplify)
    Wc, Wm = vertex(False), vertex(True)
    checks = {"W_corpus_eq_qinv_J": bool((Wc - J / q).applyfunc(sp.simplify) == sp.zeros(4)),
              "W_mirror_eq_q_J": bool((Wm - q * J).applyfunc(sp.simplify) == sp.zeros(4))}
    coeff = {}
    for mirror, W in ((False, Wc), (True, Wm)):
        for sign, L in ((1, S), (-1, Sinv)):
            coeff[(mirror, sign)] = basis_coeffs(W, L)
    words = {"V^3 = (s1 s2^-1)^3": [1, -2] * 3, "s1 s2^-1": [1, -2],
             "s1^4": [1] * 4, "(s1 s2)^5": [1, 2] * 5}
    rows = []
    for name, w in words.items():
        T = close12(word_op(w))[D, D]
        A = {m: sp.factor(sum(coeff[(m, 1 if L > 0 else -1)][1] for L in w) * T) for m in (False, True)}
        ratio = sp.factor(A[False] ** 2 / A[True] ** 2) if A[True] != 0 else None
        rows.append({"word": name, "T_dd": str(sp.factor(T)),
                     "A_corpus": str(A[False]), "A_mirror": str(A[True]),
                     "ratio_sq": str(ratio),
                     "ratio_sq_at_q0": str(sp.N(ratio.subs(q, Q0), 12)) if ratio is not None else None,
                     "ratio_is_q_minus4": bool(ratio is not None and sp.simplify(ratio - q**-4) == 0)})
    res = {"producer": "computations/probes/emission_reading_chirality_probe.py", "bean": "qou-g0jn",
           "arithmetic": "exact (sympy over Q(q)); q0 used only for display",
           "q0_anchor": "proton (display only)",
           "q0Anchor": "proton",
           "q0AnchorReason": "algebra is exact over Q(q); the only numeric column (ratio_sq_at_q0) substitutes Q0, a 16-digit rational of the proton pin",
           "q0Value": "1.109978582751381",
           "checks": checks,
           "coefficients": {f"{'mirror' if m else 'corpus'}_{'s' if s > 0 else 's^-1'}": [str(c) for c in v]
                            for (m, s), v in coeff.items()},
           "rows": rows}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("emission-reading-chirality.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
