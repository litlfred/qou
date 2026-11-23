"""qou-g0jn, pre-registration 4: multi-crossing interference of the W⁻ emission.

Pre-registered in bean qou-g0jn (2026-11-15 20:00Z) before computing.
At each letter the deviation of the weak vertex from the bare letter is
delta = W(letter) - letter: -h P_L on s, +h P_R on s^-1 (W(s^-1) = W(s), PR #7975).
Its local W⁻ amplitude is the Ř-coefficient of delta (PR #7977: the
equivariant vertices are a + bŘ, and only b emits). Summed over sites for
words of mixed sign; mirror vertex (P_L <-> P_R) for comparison.
LIMITATION (stated in advance): local site amplitudes only; dressing by
the rest of the word acting on the state is not included.
Exact sympy, no floats.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import R, h, q, is_zero  # noqa: E402
from flavour_vertex_chirality_probe import coeffs  # noqa: E402

S = R("std")
I = sp.eye(4)
Q2 = q + 1 / q
PL = (S + I / q) / Q2
PR = (q * I - S) / Q2
Sinv = S - h * I


def vertex(mirror: bool):
    L, Rr = (PR, PL) if mirror else (PL, PR)
    return S * Rr + Sinv * L  # corpus: W = s P_R + s^-1 P_L


def site_amp(sign: int, mirror: bool):
    W = vertex(mirror)
    letter = S if sign > 0 else Sinv
    _, b = coeffs(sp.simplify(W - letter), S)
    return sp.factor(b)


def main():
    words = {"s1 s2^-1": [1, -2], "(s1 s2^-1)^3": [1, -2] * 3,
             "s1^4": [1] * 4, "(s1 s2)^5": [1, 2] * 5}
    assert is_zero(vertex(False) - S + h * PL)
    rows = []
    pred_ok = True
    for mirror in (False, True):
        sp_amp = {s: site_amp(s, mirror) for s in (1, -1)}
        for name, w in words.items():
            total = sp.factor(sum(sp_amp[1 if L > 0 else -1] for L in w))
            pred = (-1 if not mirror else 1) * len(w) * h / Q2
            ok = sp.simplify(total - pred) == 0
            pred_ok = pred_ok and ok
            rows.append({"vertex": "mirror" if mirror else "corpus", "word": name,
                         "site_amp_positive_letter": str(sp_amp[1]),
                         "site_amp_inverse_letter": str(sp_amp[-1]),
                         "sum": str(total), "matches_prediction": ok})
    res = {"producer": "computations/probes/multi_crossing_interference_probe.py", "bean": "qou-g0jn",
           "arithmetic": "exact (sympy over Q(q)); no floats", "q0_anchor": "none (symbolic in q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "probe never reads q0: every quantity is exact over Q(q) (sympy), with q a free symbol; its import cone (w_braid_reconcile_probe, flavour_vertex_chirality_probe) evaluates nothing at a substrate pin",
           "limitation": "local site amplitudes; dressing by the rest of the word not included",
           "rows": rows, "checks": {"prediction_constructive_and_mirror_same_magnitude": pred_ok}}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("multi-crossing-interference.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
