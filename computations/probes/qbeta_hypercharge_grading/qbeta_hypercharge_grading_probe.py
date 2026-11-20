#!/usr/bin/env python3
"""qou-99qc: a hypercharge grading as a quark/lepton separator for n⊗ν → p⊗e⁻.

Pre-registered in PREREGISTRATION.md (same directory), committed before this probe ran.
Lean companion: QOU/QuarkState/HyperchargeGradingNoGo.lean.

Exact sympy over Q(q, g_q, g_l, c). No float anywhere. No value of c is selected and no
Q_beta number is produced: the pre-registration fixes that a number is computed only for a
FORCED c, and the corpus forces none (see the witness field `forced_c`). CODATA is not read.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import sympy as sp  # noqa: E402
from sympy.physics.quantum import TensorProduct as TP  # noqa: E402

T0 = time.time()
ASSERTS: list = []
FAILED: list = []
q, gq, gl, s = sp.symbols("q g_q g_l s", positive=True)
c = sp.symbols("c", real=True)


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def is_zero(M):
    return all(sp.simplify(e) == 0 for e in sp.Matrix(M))


# strands: (type, flavour); 2T3 and 3Y (integers)
TWO_T3 = {"u": 1, "d": -1}
THREE_Y = {"q": 1, "l": -3}
N_NU = [("q", "u"), ("q", "d"), ("q", "d"), ("l", "u")]
P_E = [("q", "u"), ("q", "u"), ("q", "d"), ("l", "d")]


def main() -> int:
    log("Arm 1: conserved totals and grouplike weights")
    for name, f in (("2T3", lambda t, fl: TWO_T3[fl]), ("3Y", lambda t, fl: THREE_Y[t]),
                    ("6Q=3(2T3)+3Y", lambda t, fl: 3 * TWO_T3[fl] + THREE_Y[t])):
        a = sum(f(*x) for x in N_NU)
        b = sum(f(*x) for x in P_E)
        check(f"total_{name}", a == b, f"n⊗ν {a}, p⊗e⁻ {b}")
    # grouplike q^{2T3 + cY}: product over strands, Y = 3Y/3
    w = lambda lst: sp.Mul(*[q ** (TWO_T3[fl] + c * sp.Rational(THREE_Y[t], 3)) for t, fl in lst])
    check("grouplike_q^(2T3+cY)", sp.simplify(sp.powsimp(w(N_NU) / w(P_E), force=True)) == 1,
          "ratio of four-strand weights is 1 for symbolic c")

    log("Arm 2: matrices (quark ⊗ lepton pair)")
    K = sp.diag(q, 1 / q)
    E = sp.Matrix([[0, 1], [0, 0]])
    F = sp.Matrix([[0, 0], [1, 0]])
    EF = sp.Matrix(TP(E, F))
    D = sp.Matrix(TP(gq * K, gl * K))
    check("EF_commutes_dressed", is_zero(D * EF - EF * D), "[(g_q K)⊗(g_l K), E⊗F] = 0")
    yq, yl = sp.symbols("y_q y_l")
    twoQ = lambda y: sp.diag(1 + y, -1 + y)
    I2 = sp.eye(2)
    Qtot = sp.Matrix(TP(twoQ(yq), I2)) + sp.Matrix(TP(I2, twoQ(yl)))
    check("EF_commutes_charge", is_zero(Qtot * EF - EF * Qtot), "[2Q⊗1+1⊗2Q, E⊗F] = 0")
    Rc = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, q - 1 / q, 0], [0, 0, 0, q]])
    Dql = sp.Matrix(TP(gq * K, gl * K))
    Dlq = sp.Matrix(TP(gl * K, gq * K))
    check("Rc_intertwines_dressed", is_zero(Rc * Dql - Dlq * Rc), "Ř (g_qK⊗g_lK) = (g_lK⊗g_qK) Ř")

    log("Arm 3: Markov-normalised trace with scalar dressing")
    X = sp.Matrix(2, 2, sp.symbols("x0:4"))
    lhs = (gq * K * X).trace() / (gq * K).trace()
    rhs = (K * X).trace() / K.trace()
    check("normalised_trace_dressing_cancels", sp.simplify(lhs - rhs) == 0, "g cancels")

    log("Arm 4: per-strand unnormalised additive energy")
    kap = {"u": q, "d": 1 / q}
    g = {"q": gq, "l": gl}
    eps = lambda lst: sum(g[t] * kap[fl] for t, fl in lst)
    split = sp.simplify(eps(N_NU) - eps(P_E))
    check("split_eq", sp.simplify(split - (gl - gq) * (q - 1 / q)) == 0, f"split = {sp.factor(split)}")
    split_hyper = sp.simplify(split.subs({gq: s, gl: s ** -3}))
    check("split_hyper", sp.simplify(split_hyper - (s ** -3 - s) * (q - 1 / q)) == 0,
          f"g_q = s = q^(c/3), g_l = s^-3: {sp.factor(split_hyper)}")
    split_c = sp.simplify(split.subs({gq: q ** (c / 3), gl: q ** (-c)}))
    check("split_q_to_1", sp.limit(split_c, q, 1) == 0, "→ 0 as q → 1 for every c")
    check("split_c0_zero", sp.simplify(split_c.subs(c, 0)) == 0, "c = 0 reproduces #8661's zero")
    # leading behaviour near q = 1: q = e^λ
    lam = sp.symbols("lambda", positive=True)
    ser = sp.series(split_c.subs(q, sp.exp(lam)), lam, 0, 4).removeO()
    lead = sp.factor(sp.simplify(ser))
    log(f"  split(q = e^λ) = {lead} + O(λ⁴)")

    out = {
        "arms": {
            "1_conserved_total": "zero split for every c (scope (b), invariant: separability)",
            "2_matrices": "E⊗F commutes with dressed K and with total 2Q; Ř intertwines",
            "3_normalised_trace": "scalar dressing cancels: ruled functional blind to c",
            "4_unnormalised_per_strand": "split = (g_l − g_q)(q − 1/q); NOT the ruled functional",
        },
        "split_symbolic": str(sp.factor(split)),
        "split_hypercharge_c": str(sp.simplify(split_c)),
        "split_small_lambda": str(lead),
        "forced_c": "none: no corpus structure fixes the normalisation of a strand U(1)_Y grading "
                    "(eightfold-open-problems item 'Hypercharge Y' is open; gl2 centre K1K2 acts "
                    "as q on every fundamental strand, quark or lepton). c = 1 corresponds to the "
                    "electric-charge grading q^(2Q) = K·q^Y, which would be a premise.",
        "qbeta_number": "not computed (no forced c; pre-registered)",
        "scope": "(b) for arms 1-3; arm 4 is a scope-(a) family over an unforced premise",
        "selected": "none",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    from q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-hypercharge-grading", engine="python", start_time=T0,
                        output_dir=_HERE)
    wb.set_description("qou-99qc: hypercharge q^(cY) as a second strand grading for n⊗ν → p⊗e⁻. "
                       "Exact sympy; no number computed. Pre-registered in PREREGISTRATION.md.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("q0_used", "no (symbolic only)")
    for key, val in out.items():
        wb.add_data(key, val)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0",
                         source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
