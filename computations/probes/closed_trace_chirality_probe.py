"""qou-g0jn, pre-registration 6: closed-trace emission amplitude, corpus vertex vs mirror.

Pre-registered in bean qou-g0jn (2026-11-15 20:15Z) before computing.
M_w = sum_k (word w with letter k replaced by delta_k = W(letter) - letter)
on (C²)^⊗3. Spectator strands 1, 2 are closed with the D Markov weights
(partial quantum trace, K⊗K, K = diag(q, q⁻¹)), leaving a 2×2 operator T_w
on strand 3, the converting strand. The emission amplitude (#7973 arm A) is T_w[d, d].
Exact sympy, no floats.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import h, q  # noqa: E402
from word_dressing_chirality_probe import I2, U, D, kr, letter  # noqa: E402

K = sp.diag(q, 1 / q)


def on3(M4, pos):
    return kr(M4, I2) if pos == 1 else kr(I2, M4)


def M_w(word, mirror):
    tot = sp.zeros(8)
    for k in range(len(word)):
        M = sp.eye(8)
        for j, L in enumerate(word):
            M = on3(letter(1 if L > 0 else -1, mirror, deviate=(j == k)), abs(L)) * M
        tot += M
    return tot.applyfunc(sp.simplify)


def close12(M):
    T = sp.zeros(2)
    for a in (0, 1):
        for b in (0, 1):
            for x in (0, 1):
                for y in (0, 1):
                    w = K[x, x] * K[y, y]
                    T[a, b] += w * M[4 * x + 2 * y + a, 4 * x + 2 * y + b]
    return T.applyfunc(sp.simplify)


def main():
    words = {"V^3 = (s1 s2^-1)^3": [1, -2] * 3, "s1 s2^-1": [1, -2],
             "s1^4": [1] * 4, "(s1 s2)^5": [1, 2] * 5}
    rows = []
    for name, w in words.items():
        out = {}
        for mirror in (False, True):
            T = close12(M_w(w, mirror))
            out[mirror] = T
        tc, tm = sp.factor(out[False][D, D]), sp.factor(out[True][D, D])
        ratio = sp.factor(tc**2 / tm**2) if tm != 0 else None
        rows.append({"word": name,
                     "T_corpus": [[str(sp.factor(x)) for x in r] for r in out[False].tolist()],
                     "T_mirror": [[str(sp.factor(x)) for x in r] for r in out[True].tolist()],
                     "T_corpus_scalar": bool(out[False][0, 1] == 0 and out[False][1, 0] == 0
                                             and sp.simplify(out[False][0, 0] - out[False][1, 1]) == 0),
                     "T_mirror_scalar": bool(out[True][0, 1] == 0 and out[True][1, 0] == 0
                                             and sp.simplify(out[True][0, 0] - out[True][1, 1]) == 0),
                     "emission_corpus": str(tc), "emission_mirror": str(tm),
                     "abs_ratio_sq_corpus_over_mirror": str(ratio)})
    res = {"producer": "computations/probes/closed_trace_chirality_probe.py", "bean": "qou-g0jn",
           "arithmetic": "exact (sympy over Q(q)); no floats", "q0_anchor": "none (symbolic in q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "exact sympy arithmetic over Q(q) with q a free symbol; no substrate q0 is read or substituted",
           "rows": rows}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("closed-trace-chirality.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
