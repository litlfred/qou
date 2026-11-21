"""qou-g0jn, pre-registration 5: does word dressing on the real udd state carry chirality?

Pre-registered in bean qou-g0jn (2026-11-15 20:04Z) before computing.
Space (C²)^⊗3 ⊗ V ⊗ V* (32-dim): quark strands 1-3, created pair 4-5.
Initial |u d d> ⊗ coev_45 (plain). For word w on strands 1-3 and each site k,
letter k is replaced by delta_k = W(letter) - letter (corpus vertex
W = s P_R + s^-1 P_L, or the mirror with P_L <-> P_R); then the emission
crossing Ř on strands (3,4) (PR #7973 arm A). A(w) = sum_k of the component
on {two u, one d on 1-3} ⊗ (d ūbar on 4-5).
Exact sympy, no floats.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import R, h, q, is_zero  # noqa: E402

S = R("std")
I4 = sp.eye(4)
I2 = sp.eye(2)
Q2 = q + 1 / q
PL = (S + I4 / q) / Q2
PR = (q * I4 - S) / Q2
Sinv = S - h * I4
U, D = 0, 1  # K = q on e1 for the std R (#7971)


def kr(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


def on_quarks(M2, i):
    return kr(M2, I2, I2, I2) if i == 1 else kr(I2, M2, I2, I2)


def vertex(mirror):
    L, Rr = (PR, PL) if mirror else (PL, PR)
    return S * Rr + Sinv * L


def letter(sign, mirror=None, deviate=False):
    base = S if sign > 0 else Sinv
    if not deviate:
        return base
    return sp.simplify(vertex(mirror) - base)


def idx(bits):
    n = 0
    for b in bits:
        n = 2 * n + b
    return n


def amplitude(word, mirror):
    psi = sp.zeros(32, 1)
    for i in (0, 1):  # plain coev on 4,5
        psi[idx([U, D, D, i, i])] = 1
    emit = kr(I2, I2, S, I2)
    total = sp.zeros(32, 1)
    for k in range(len(word)):
        M = sp.eye(32)
        for j, L in enumerate(word):
            sign, pos = (1 if L > 0 else -1), abs(L)
            M = on_quarks(letter(sign, mirror, deviate=(j == k)), pos) * M
        total += emit * M * psi
    total = total.applyfunc(sp.simplify)
    amp = sum(total[idx([a, b, c, D, U])] for a in (0, 1) for b in (0, 1) for c in (0, 1)
              if [a, b, c].count(U) == 2)
    return sp.factor(sp.simplify(amp))


def main():
    words = {"s1 s2^-1": [1, -2], "(s1 s2^-1)^3": [1, -2] * 3,
             "s1^4": [1] * 4, "(s1 s2)^5": [1, 2] * 5}
    rows = []
    for name, w in words.items():
        ac, am = amplitude(w, False), amplitude(w, True)
        ratio = sp.factor(sp.simplify(ac**2 / am**2)) if am != 0 else "inf (mirror amplitude 0)"
        rows.append({"word": name, "A_corpus": str(ac), "A_mirror": str(am),
                     "abs_ratio_sq_corpus_over_mirror": str(ratio),
                     "magnitudes_differ": bool(sp.simplify(ac**2 - am**2) != 0)})
    res = {"producer": "computations/probes/word_dressing_chirality_probe.py", "bean": "qou-g0jn",
           "arithmetic": "exact (sympy over Q(q)); no floats", "q0_anchor": "none (symbolic in q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "probe never reads q0: every quantity is exact over Q(q) (sympy), with q a free symbol; its import cone (w_braid_reconcile_probe) evaluates nothing at a substrate pin",
           "rows": rows,
           "checks": {"expectation_magnitudes_differ_all_words": all(r["magnitudes_differ"] for r in rows)}}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("word-dressing-chirality.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
