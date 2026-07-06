#!/usr/bin/env python3
"""
alpha_em_shift_chain.py — numerical re-evaluation of the multiplicative chain

  α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q
         = q · [9]_q · [10]_q

at the canonical substrate value q₀.

Composes:
  - prop:em-coupling-projection            (the bare 1/α formula)
  - prop:alpha-shift-torus-knot            (α_shift(T_{p,k}) = k(p-1))
  → prop:alpha-em-shift-multiplicative-chain

Cross-checks against:
  - q_parameter.Q_MP (50-digit canonical q₀)
  - The independent witness
    computations/alpha-shift-torus.witness.json
    (reads the recorded α_shift values and uses them as the
    q-integer indices, demonstrating the chain composes).

@module computations/alpha_em_shift_chain
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

CODATA_ALPHA_INV = mp.mpf("137.035999084")  # CODATA 2022 (8.1×10⁻¹⁰ rel. unc.)


def q_integer(q: mp.mpf, n: int) -> mp.mpf:
    """[n]_q = (q^n − q^{−n}) / (q − q⁻¹)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def main() -> None:
    mp.mp.dps = 50
    q0 = q_at(50)

    # Read α_shift values from the upstream witness — this is the
    # composition: we are not re-deriving them, we are *using* them.
    upstream = _pb.witness_path("alpha-shift-torus.witness.json", HERE)
    with upstream.open("r", encoding="utf-8") as f:
        ut = json.load(f)
    knots = ut["data"]["torus_knots"]
    a29 = int(knots["T_2_9"]["alpha_shift"])
    a35 = int(knots["T_3_5"]["alpha_shift"])

    # Composed chain (using α_shift values as q-integer indices)
    qa29 = q_integer(q0, a29)
    qa35 = q_integer(q0, a35)
    inv_alpha_chain = q0 * qa29 * qa35
    alpha_chain = 1 / inv_alpha_chain

    # Bare formula (using the literal 9, 10) — must match by construction
    inv_alpha_bare = q0 * q_integer(q0, 9) * q_integer(q0, 10)

    delta = abs(inv_alpha_chain - inv_alpha_bare)
    delta_codata = abs(inv_alpha_chain - CODATA_ALPHA_INV)

    print("=" * 78)
    print(" α_EM⁻¹ multiplicative chain — numerical re-evaluation at q₀")
    print("=" * 78)
    print(f"  q₀                       = {mp.nstr(q0, 30)}")
    print(f"  α_shift(T_{{2,9}})         = {a29}   (← from alpha-shift-torus.witness.json)")
    print(f"  α_shift(T_{{3,5}})         = {a35}   (← from alpha-shift-torus.witness.json)")
    print(f"  [α_shift(T_{{2,9}})]_q     = {mp.nstr(qa29, 20)}")
    print(f"  [α_shift(T_{{3,5}})]_q     = {mp.nstr(qa35, 20)}")
    print(f"  q · [9]_q · [10]_q       = {mp.nstr(inv_alpha_bare, 25)}  (bare em-coupling-projection)")
    print(f"  q · [α_shift(2,9)]_q · [α_shift(3,5)]_q = {mp.nstr(inv_alpha_chain, 25)}  (chain)")
    print(f"  |chain − bare|           = {mp.nstr(delta, 5)}   (must be 0 by composition)")
    print(f"  α_EM (chain)             = {mp.nstr(alpha_chain, 20)}")
    print(f"  α_EM⁻¹ (chain)           = {mp.nstr(inv_alpha_chain, 20)}")
    print(f"  CODATA α_EM⁻¹            = {mp.nstr(CODATA_ALPHA_INV, 20)}")
    print(f"  |chain − CODATA|         = {mp.nstr(delta_codata, 5)}")

    w = WitnessBuilder("alpha-em-shift-multiplicative-chain", engine="mpmath")
    w.set_description(
        "Numerical re-evaluation of the multiplicative-chain identity "
        "α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q at q₀, "
        "composing prop:em-coupling-projection with prop:alpha-shift-torus-knot. "
        "α_shift values are read from alpha-shift-torus.witness.json (not "
        "recomputed here) — the witness validates that composition is exact."
    )
    w.set_content_block("prop:alpha-em-shift-multiplicative-chain")
    w.add_parameter("q0_dps", 50)
    w.add_parameter("alpha_shift_T_2_9", a29)
    w.add_parameter("alpha_shift_T_3_5", a35)
    w.add_data("upstream_witness", "alpha-shift-torus.witness.json")
    w.add_data("q0", mp.nstr(q0, 50))
    w.add_data("inv_alpha_chain", mp.nstr(inv_alpha_chain, 40))
    w.add_data("inv_alpha_bare", mp.nstr(inv_alpha_bare, 40))
    w.add_data("delta_chain_minus_bare", mp.nstr(delta, 10))
    w.add_data("inv_alpha_codata", str(CODATA_ALPHA_INV))
    w.add_data("delta_chain_minus_codata", mp.nstr(delta_codata, 10))

    # Composition is exact at the symbolic level; numerical agreement
    # is to mpmath precision (1e-45).
    w.add_assertion(
        name="chain_equals_bare_to_mpmath_precision",
        computed=float(delta),
        expected=0.0,
        tolerance=1e-30,
    )
    # Bridge consistency: the indices used in the chain match the
    # q-integer indices in the bare formula.
    w.add_assertion(
        name="alpha_shift_T_2_9_equals_9",
        computed=a29,
        expected=9,
    )
    w.add_assertion(
        name="alpha_shift_T_3_5_equals_10",
        computed=a35,
        expected=10,
    )

    out = w.save()
    print(f"\nWitness written: {out}")
    print(f"All passed: {all(a.passed for a in w.assertions)}")


if __name__ == "__main__":
    main()
