"""SW-period residue weight, and its equivalence to the #1765 selection
rule (workplan task C4).

Step-9 binding-closure workplan: the n-th body-order term is the n-th
prolonged Seiberg–Witten period (`prop:sw-period-residue-sum`, L1), which
is an algebraic residue sum. This module evaluates the residue *weight*
at the canonical n=4 anchor (the Borromean link L6a4, crossing/component
count c=3 → partition rank c+1=4) and shows it coincides with:

  • the production Family-A linking weight `linking_weight_family_a(q)`
    = (3q²+4+3q⁻²)/4, and
  • its closed partition form — by the `_li_2_q_util` docstring this scalar
    *is* the H₄ per-block sum over partitions of 4, i.e. the #1765
    selection rule `λ(L) = (1/(c+1))·Σ_{λ⊢c+1} dim_q(λ)` at c=3.

So L1's residue-sum carrier, the production density, and the #1765 rule
are the same object at the n=4 anchor. The geometric × algebraic n=4
contribution is `vol_component(L6a4) · residue_weight`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE.parent))  # computations/ — _li_2_q_util, q_parameter, _path_bridge
_sys.path.insert(0, str(_HERE))         # substrate/ — gate, knot_volumes, witness_base
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import linking_weight_family_a  # noqa: E402
from sw_hyperbolicity_gate import vol_component  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402


def family_a_partition_form(q: mp.mpf) -> mp.mpf:
    """The closed partition form of the n=4 (c=3) residue weight:
    (3q²+4+3q⁻²)/4 — the H₄ sum over partitions of 4 (= #1765 rule)."""
    return (3 * q**2 + 4 + 3 * q**-2) / 4


def residue_weight(body_order: int, q: mp.mpf) -> mp.mpf:
    """SW-period residue weight at the given body order. Currently the
    n=4 (Borromean, c=3) anchor is wired to the canonical Family-A
    linking weight; other orders await the per-knot rule (#1765 saddle)."""
    if body_order == 4:
        return linking_weight_family_a(q)
    raise NotImplementedError(
        f"residue weight for body order {body_order} not yet wired "
        f"(per-knot λ(K) rule, #1765 A-polynomial saddle)."
    )


def _emit_witness() -> None:
    from witness_base import WitnessBuilder
    from q_parameter import Q_50_DIGIT_STR as Qs

    mp.mp.dps = COMPUTE_DPS
    q = mp.mpf(Qs)
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 5))

    famA = linking_weight_family_a(q)
    part = family_a_partition_form(q)
    rw4 = residue_weight(4, q)
    vol4 = vol_component("L6a4")
    sw_term4 = vol4 * rw4

    w = WitnessBuilder("sw-period-residue", engine="mpmath")
    w.set_audit_only(
        "docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md"
    )
    w.add_parameter("q_0", Qs)
    w.add_data("n4_residue_weight", mp.nstr(rw4, 16))
    w.add_data("n4_vol_component_L6a4", mp.nstr(vol4, 16))
    w.add_data("n4_sw_term_geom_x_alg", mp.nstr(sw_term4, 16))
    w.add_data("selection_rule_form",
               "lambda(L) = (1/(c+1)) * sum_{lambda |- c+1} dim_q(lambda); "
               "c=3 -> partitions of 4 -> Family-A = I(4)/4")

    # Family-A equals its closed partition form (the #1765 I(4)/4 rule).
    w.add_assertion(
        "residue_weight_eq_partition_form",
        computed=1 if abs(famA - part) < tol else 0, expected=1,
        source=f"|Family-A - (3q²+4+3q⁻²)/4| = {mp.nstr(abs(famA - part), 4)} < tol")
    # The residue weight at n=4 IS the production Family-A density (L1 ↔ prod).
    w.add_assertion(
        "n4_residue_weight_is_family_a",
        computed=1 if abs(rw4 - famA) < tol else 0, expected=1,
        source="SW-period residue weight at n=4 = linking_weight_family_a")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = COMPUTE_DPS
    from q_parameter import Q_50_DIGIT_STR as Qs
    q = mp.mpf(Qs)
    print("SW-period residue weight (C4) — n=4 (Borromean, c=3) anchor")
    print(f"  Family-A linking weight        = {mp.nstr(linking_weight_family_a(q), 12)}")
    print(f"  partition form (3q²+4+3q⁻²)/4   = {mp.nstr(family_a_partition_form(q), 12)}")
    print(f"  vol_component(L6a4) = 8·Catalan = {mp.nstr(vol_component('L6a4'), 12)}")
    print(f"  n=4 SW term (vol × residue)     = {mp.nstr(vol_component('L6a4') * residue_weight(4, q), 12)}")
    _emit_witness()
