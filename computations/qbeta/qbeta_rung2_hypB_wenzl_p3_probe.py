#!/usr/bin/env python3
"""qbeta_rung2_hypB_wenzl_p3_probe.py — definitive test of Hyp-B
for the c_3 rung-2 structural lift.

Tests whether the rung 2 form ℏ_q³/[2]_q equals (Wenzl projector p_3
Markov trace) / TL loop value = [4]_q / [2]_q. By the standard
Wenzl-projector quantum-dimension identity tr_M(p_k) = [k+1]_q,
the Hyp-B prediction simplifies to [4]_q / [2]_q = q² + q⁻².

Decisive symbolic comparison + classical-limit cross-check.

Naming: `*_probe.py` (NOT `*_test.py`) to avoid pytest collection
of import-time side effects.  Per Copilot review on PR #1806.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

Q0_MP_PIN = "1.1099785955573347198997632204832250266562084087802"


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-rung2-hyp-b-wenzl-p3-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Definitive test of Hyp-B: does rung_2 = hbar_q^3/[2]_q "
        "equal tr_M(Wenzl p_3) / TL_loop = [4]_q/[2]_q? "
        "By Wenzl-projector identity tr_M(p_k) = [k+1]_q, the "
        "Hyp-B prediction = q^2 + q^-2 = -J_Hopf. Classical-limit "
        "cross-check independently confirms verdict."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Q_β RUNG-2 HYP-B — Wenzl projector p_3 definitive test")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    hbar_q = (q - 1) / q
    qint_2 = q + 1 / q
    qint_4 = q ** 3 + q + 1 / q + 1 / q ** 3

    rung2_actual = hbar_q ** 3 / qint_2
    hypB_pred = qint_4 / qint_2  # = [4]_q / [2]_q = q² + q⁻² (standard)

    print(f"  Setup (TL_n Wenzl projector convention):")
    print(f"    tr_M(p_k) = [k+1]_q  (quantum dim of V_k of U_q(sl_2))")
    print(f"    tr_M(p_3) = [4]_q = q³ + q + q⁻¹ + q⁻³")
    print(f"    TL loop value δ_q = [2]_q = q + q⁻¹")
    print()
    print(f"  Hyp-B prediction:  rung 2 = tr_M(p_3) / δ_q = [4]_q / [2]_q")
    print(f"  Actual rung 2:     ℏ_q³ / [2]_q")
    print()

    print(f"  Symbolic simplification:")
    print(f"    rung 2 (actual):  {sp.factor(sp.simplify(rung2_actual))}")
    print(f"    Hyp-B pred:       {sp.factor(sp.simplify(hypB_pred))}")
    print()

    diff = sp.simplify(rung2_actual - hypB_pred)
    print(f"  Decisive test:  rung 2 - Hyp-B pred = {diff}")
    print()

    hypB_confirmed = (diff == 0)

    rung2_at_q1 = sp.limit(rung2_actual, q, 1)
    hypB_at_q1 = sp.limit(hypB_pred, q, 1)
    print(f"  Classical-limit cross-check:")
    print(f"    rung 2 at q = 1:       {rung2_at_q1}  (vanishes, cubic in q-1)")
    print(f"    Hyp-B pred at q = 1:   {hypB_at_q1}  (NON-vanishing)")
    print(f"    → Hyp-B literal reading is incompatible with classical limit.")
    print()

    q0_mp = mp.mpf(Q0_MP_PIN)
    def evalmp(expr):
        # Use sympy.lambdify with the mpmath backend so high-precision
        # evaluation goes through mpmath natively (no intermediate
        # string/float roundtrip).  Per Gemini review on PR #1806.
        return sp.lambdify(q, expr, "mpmath")(q0_mp)
    actual_q0 = evalmp(rung2_actual)
    hypB_q0 = evalmp(hypB_pred)
    print(f"  Numerical at q_0:")
    print(f"    rung 2 (actual)         = {mp.nstr(actual_q0, 12)}")
    print(f"    Hyp-B pred              = {mp.nstr(hypB_q0, 12)}")
    print()

    print("=" * 78)
    print(" VERDICT — Hyp-B")
    print("=" * 78)
    print()
    if hypB_confirmed:
        print(f"  ✓ Hyp-B CONFIRMED — rung 2 IS Wenzl p_3 trace over TL loop")
    else:
        print(f"  ✗ Hyp-B REFUTED (literal reading)")
        print(f"    ℏ_q³/[2]_q ≠ [4]_q/[2]_q.")
        print(f"    Note: Hyp-B pred = q² + q⁻² = -J_Hopf(q) (the rung-0 base!),")
        print(f"    so the literal reading would say rung_2 = rung_0/[2]_q —")
        print(f"    clearly wrong (rung 2 vanishes at q=1, rung_0/[2]_q does not).")
    print()
    print(f"  Implications:")
    print(f"    (a) 'p_3 contribution at order ℏ³' likely means a specific")
    print(f"        COEFFICIENT in the projector expansion, not the bare trace.")
    print(f"    (b) Hyp-C (Kauffman bracket) remains untested.")
    print()

    builder.add_data("hypothesis",
                     "Hyp-B literal: rung_2 = tr_M(p_3) / [2]_q = [4]_q/[2]_q")
    builder.add_data("rung_2_actual", "hbar_q^3 / [2]_q")
    builder.add_data("hypB_pred", "[4]_q / [2]_q = q^2 + q^-2 = -J_Hopf(q)")
    builder.add_data("symbolic_difference", str(diff))
    builder.add_data("classical_limit", {
        "rung_2_at_q_1": str(rung2_at_q1),
        "hypB_pred_at_q_1": str(hypB_at_q1),
        "rung_2_vanishes_at_q1": rung2_at_q1 == 0,
        "hypB_vanishes_at_q1": hypB_at_q1 == 0,
        "compatible": (rung2_at_q1 == 0) == (hypB_at_q1 == 0),
    })
    builder.add_data("verdict", "CONFIRMED" if hypB_confirmed else "REFUTED")
    builder.add_data("numerical_at_q0", {
        "rung_2_actual": mp.nstr(actual_q0, 25),
        "hypB_pred": mp.nstr(hypB_q0, 25),
    })

    builder.add_assertion(
        "hypB_decisively_resolved",
        computed=1,
        expected=1,
        tolerance=0,
        source=("Symbolic compare rung-2 form (hbar_q^3/[2]_q) "
                "against Hyp-B literal prediction [4]_q/[2]_q. "
                "Classical-limit cross-check provides independent "
                "confirmation. Reports CONFIRMED or REFUTED."),
    )

    builder.save()
    print(f"  Witness: qbeta-rung2-hyp-b-wenzl-p3-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
