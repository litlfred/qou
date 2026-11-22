#!/usr/bin/env python3
"""
probe_qbeta_over_e0_classical_vanishing.py — I1 probe for
`prop:q-beta-over-e0-classical-vanishing`.

The proposition: with the substrate closed forms

    Q_β(q) = m_e · (2q + 1 − q²)(q + 1) / (2q³),
    E_0^{N=0}(q) = m_e / (q(q − 1)),

the ratio S(q) = Q_β(q)/E_0(q) simplifies to

    S(q) = (2q + 1 − q²)(q² − 1) / (2q²)

and S(1) = 0 as an algebraic identity over any commutative ring (the
m_e scale cancels). This is the algebraic obstruction (PR #1769) showing
the audit-doc recipe "c_k from u_ladder Taylor of S = Q_β/E_0" is
degenerate (0/0 at q = 1) — so the c_k ladder normalization is NOT this
S; it is Q_β / [Q_A·cos(α)] instead.

Symbolic arms are exact over ℚ(q) (true for all q, the proved content);
the numeric arm reports S(q₀) ≈ 0.18689, the SDP affine target n_target.

Mirrors the sorry-free Lean theorems
`QOU.QBeta.OverE0ClassicalVanishing.{qbeta_over_e0_numerator_at_one_eq_zero,
qbeta_over_e0_at_one_eq_zero}`.

Output: probe-qbeta-over-e0-classical-vanishing.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import sympy as sp
import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    q = sp.symbols("q")

    # Substrate closed forms (m_e cancels in the ratio, so drop it).
    Q_beta_over_me = (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0_over_me = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    S = sp.simplify(Q_beta_over_me / E0_over_me)

    S_claimed = (2 * q + 1 - q ** 2) * (q ** 2 - 1) / (2 * q ** 2)
    numerator = (2 * q + 1 - q ** 2) * (q ** 2 - 1)

    print("=" * 78)
    print("  Probe — prop:q-beta-over-e0-classical-vanishing")
    print("=" * 78)
    print(f"  S(q) = Q_β/E_0 simplified : {sp.simplify(S)}")
    print(f"  claimed closed form       : {sp.simplify(S_claimed)}")

    # (1) closed-form identity: S == (2q+1-q²)(q²-1)/(2q²) over ℚ(q)
    closed_form_ok = sp.simplify(S - S_claimed) == 0
    # (2) numerator vanishes at q=1 (matches the Lean `ring` theorem)
    num_at_one = sp.expand(numerator.subs(q, 1))
    num_zero = num_at_one == 0
    # (3) full simplified ratio vanishes at q=1
    S_at_one = sp.simplify(S_claimed.subs(q, 1))
    ratio_zero = S_at_one == 0

    print(f"  closed-form identity S = (2q+1-q²)(q²-1)/(2q²) : {closed_form_ok}")
    print(f"  numerator (2q+1-q²)(q²-1) at q=1               : {num_at_one}  (==0: {num_zero})")
    print(f"  S(1)                                            : {S_at_one}  (==0: {ratio_zero})")

    # (4) numeric S(q₀): the SDP affine target n_target ≈ 0.18689
    q0 = Q_MP
    S_q0 = ((2 * q0 + 1 - q0 ** 2) * (q0 ** 2 - 1)) / (2 * q0 ** 2)
    print(f"  S(q₀) = n_target (numeric)                      : {mp.nstr(S_q0, 12)}")

    all_ok = closed_form_ok and num_zero and ratio_zero
    if not all_ok:
        print("  ✗ a symbolic assertion FAILED")
        return 1

    wb = WitnessBuilder("probe-qbeta-over-e0-classical-vanishing", engine="sympy+mpmath")
    wb.set_content_block("prop:q-beta-over-e0-classical-vanishing")
    wb.set_description(
        "I1 probe: verifies S(q) = Q_β(q)/E_0(q) simplifies to "
        "(2q+1-q²)(q²-1)/(2q²) and S(1) = 0 as an exact ℚ(q) identity "
        "(the m_e scale cancels), mirroring the sorry-free Lean theorems. "
        "Reports the numeric S(q₀) ≈ 0.18689 SDP affine target. Symbolic "
        "arms are exact (all q); the q₀ value is evidence, not a fit."
    )
    # computed == expected ⇒ assertion passes (1 == 1)
    wb.add_assertion(
        "S_eq_closed_form_over_Qq", computed=int(bool(closed_form_ok)), expected=1,
    )
    wb.add_assertion(
        "numerator_vanishes_at_q_eq_1", computed=int(bool(num_zero)), expected=1,
    )
    wb.add_assertion(
        "ratio_vanishes_at_q_eq_1", computed=int(bool(ratio_zero)), expected=1,
    )
    wb.add_data("symbolic", {
        "S_simplified": str(sp.simplify(S)),
        "closed_form_identity_exact_in_Qq": bool(closed_form_ok),
        "numerator_at_q1": int(num_at_one),
        "S_at_q1": int(S_at_one),
        "lean_theorems": [
            "QOU.QBeta.OverE0ClassicalVanishing.qbeta_over_e0_numerator_at_one_eq_zero",
            "QOU.QBeta.OverE0ClassicalVanishing.qbeta_over_e0_at_one_eq_zero",
        ],
    })
    wb.add_data("numeric_at_q0", {"S_q0_n_target": mp.nstr(S_q0, 20)})
    out = wb.save()
    print(f"  ✓ Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
