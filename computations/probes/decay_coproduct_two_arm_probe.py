"""qou-g0jn: which coproduct splits the neutron? Two arms, pre-registered.

Pre-registration (bean qou-g0jn, 2026-11-15 19:35Z, written before computing):
  Q: applied to the neutron (labels u d d, with u = the K = q vector, derived in
     PR #7971 / QOU/QuarkState/OverStrandWeight.lean), does the map give a
     component (u u d) ⊗ X with X of weight T^3 = -1 (W^- quantum numbers)?
     Report the coefficient exactly in q. No experimental value is used; a
     nonzero coefficient means "allowed", not a rate.
  Arm A  strand/categorical: coev V* pair creation then one crossing of the
         converting d strand with the created V. Variants: sign ±, coev plain
         or pivotal (weighted by K), both R conventions.
  Arm B  the 𝓗_q substrate Δ read as deconcatenation of braid words (q-shuffle
         Hopf algebra; this reading is an ASSUMPTION). Each tensor factor acts
         on the same 3 strands. Words: s1^4, (s1 s2)^5, s1 s2 s1.
  Prediction in advance: arm B gives 0 for every word (by C2 of
  w_braid_reconcile_probe: letters commute with Δ(K)); arm A is nonzero only
  through the transposition term.

Exact sympy over Q(q); no floats.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from w_braid_reconcile_probe import R, h, q, is_zero  # noqa: E402


def k_orientation(S):
    """Index (0 or 1) of the basis vector carrying K = q, forced by Markov (C1)."""
    for a in (1, -1):
        K = sp.diag(q**a, q**-a)
        P = sp.kronecker_product(sp.eye(2), K) * S
        part = sp.simplify(sp.Matrix(2, 2, lambda i, j: sum(P[2 * i + k, 2 * j + k] for k in range(2))))
        if is_zero(part - part[0, 0] * sp.eye(2)):
            return (0 if a == 1 else 1), K
    raise AssertionError("no Markov orientation")


def arm_a():
    rows = []
    for slot in ("std", "swp"):
        S = R(slot)
        Sinv = sp.simplify(S - h * sp.eye(4))
        u, K = k_orientation(S)
        d = 1 - u
        wt = {u: sp.Rational(1, 2), d: sp.Rational(-1, 2)}  # T^3 of e_i; e^i has -wt
        for coev in ("plain", "pivotal"):
            for sign, M in (("+", S), ("-", Sinv)):
                # state on V ⊗ V ⊗ V*, index 4*a + 2*b + c (a,b in V, c in V*)
                out = sp.zeros(8, 1)
                for i in (0, 1):
                    c_i = 1 if coev == "plain" else K[i, i]
                    vin = sp.zeros(4, 1)
                    vin[2 * d + i] = 1  # converting d strand ⊗ created e_i
                    vout = M * vin
                    for ab in range(4):
                        out[2 * ab + i] += c_i * vout[ab]
                out = sp.simplify(out)
                comps = []
                for idx in range(8):
                    if out[idx] != 0:
                        a, b, c = idx // 4, (idx // 2) % 2, idx % 2
                        comps.append({"out_quark": "u" if a == u else "d",
                                      "pair": ("u" if b == u else "d") + ("ubar" if c == u else "dbar"),
                                      "pair_T3": str(wt[b] - wt[c]),
                                      "coeff": str(out[idx])})
                w = [x for x in comps if x["out_quark"] == "u" and x["pair_T3"] == "-1"]
                rows.append({"h_slot": slot, "coev": coev, "sign": sign,
                             "components": comps,
                             "W_minus_coeff": w[0]["coeff"] if w else "0"})
    return rows


def rep3(S):
    I2 = sp.eye(2)
    return {1: sp.kronecker_product(S, I2), 2: sp.kronecker_product(I2, S)}


def arm_b():
    rows = []
    S = R("std")
    u, _ = k_orientation(S)
    d = 1 - u
    g = rep3(S)
    words = {"s1^4": [1] * 4, "(s1 s2)^5": [1, 2] * 5, "s1 s2 s1": [1, 2, 1]}
    nvec = sp.zeros(8, 1)
    nvec[4 * u + 2 * d + d] = 1  # |u d d>
    T3 = lambda idx: sum(sp.Rational(1, 2) if ((idx >> s) & 1) == u else sp.Rational(-1, 2) for s in range(3))
    for name, w in words.items():
        max_proton = sp.Integer(0)
        for k in range(len(w) + 1):
            for part in (w[:k], w[k:]):
                M = sp.eye(8)
                for L in part:
                    M = M * g[L]
                v = sp.simplify(M * nvec)
                prot = [v[i] for i in range(8) if T3(i) == sp.Rational(1, 2)]
                max_proton = max_proton if all(x == 0 for x in prot) else sp.Integer(1)
        rows.append({"word": name, "n_terms": len(w) + 1,
                     "any_factor_reaches_proton_weight": bool(max_proton),
                     "W_minus_coeff": "0" if max_proton == 0 else "nonzero"})
    return rows


def main():
    a, b = arm_a(), arm_b()
    checks = {
        "B_prediction_zero": all(r["W_minus_coeff"] == "0" for r in b),
        "A_has_W_minus_component": all(r["W_minus_coeff"] != "0" for r in a),
    }
    res = {"producer": "computations/probes/decay_coproduct_two_arm_probe.py",
           "bean": "qou-g0jn", "arithmetic": "exact (sympy over Q(q)); no floats",
           "q0_anchor": "none (symbolic in q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "exact sympy arithmetic over Q(q) with q a free symbol; no substrate q0 is read or substituted",
           "arm_A_strand_coev": a, "arm_B_Hq_deconcatenation": b, "checks": checks}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    pathlib.Path(__file__).with_name("decay-coproduct-two-arm.witness.json").write_text(
        json.dumps(res, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
