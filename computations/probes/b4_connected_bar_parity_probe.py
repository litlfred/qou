#!/usr/bin/env python3
"""I-par (magnitude leg) — bar-parity of the connected 4-body building blocks.

Scoping: docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3
(invariant I-par). The plan asked: prove the connected 4-body Ursell term `b₄`
is BAR-EVEN before computing its magnitude. This probe settles the building-block
parities and REFINES that invariant.

Building blocks (interface_4body_assembly_probe.py convention):
    pair factor  pp/nn = z       (Markov z)
    pair factor  pn    = z − h/2  (bar-invariant projection; h the Markov piece)
    binding B    = E₀ · τ_vac · (1 − ∏ f_i)

RESULT (exact, 40 dps, at q₀ and q₀⁻¹):
  • z is BAR-EVEN   (z(q) = z(q⁻¹))
  • h is BAR-ODD    (h(q) = −h(q⁻¹))
  ⇒ the pn factor z − h/2 is BAR-MIXED: bar-even part z, bar-odd part −h/2.

CONSEQUENCE — I-par is REFINED, not passed as stated. Because every pn bond
carries the bar-odd −h/2, the connected `b₄` is **bar-MIXED**, not purely
bar-even (the original I-par phrasing "prove b₄ is bar-even" is too strong — it
is FALSE). The correct prescription, consistent with the corpus bar-even/odd
binding split (binding_bar_even_odd_probe.py; retained cosh vs emitted sinh):

    the BINDING MAGNITUDE is the BAR-EVEN PROJECTION of b₄,
        b₄^even = ½[ b₄(q) + b₄(q⁻¹) ],
    and the bar-ODD projection b₄^odd = ½[ b₄(q) − b₄(q⁻¹) ] is RADIATED
    (the Q_β-like channel), not retained binding.

So the magnitude compute (the next unit) must target `b₄^even`, and the I-conn /
I-ceil invariants apply to `b₄^even`. This is a scope-(a) structural finding, no
fit: it fixes WHICH projection of the connected term is the binding, closing an
ambiguity the scoping doc left open.

`-- Ref:` scoping note §3 I-par; binding_bar_even_odd_probe.py (retained/emitted).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import closed_form_tau_M as C  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)
Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")


def bar_split(f, q):
    """Return (value_q, value_qinv, even_part, odd_part) of f under q↦q⁻¹."""
    a = f(q)
    b = f(1 / q)
    return a, b, (a + b) / 2, (a - b) / 2


def main() -> int:
    z_q, z_qi, z_even, z_odd = bar_split(C.markov_z, Q0)
    h = lambda q: q - 1 / q
    h_q, h_qi, h_even, h_odd = bar_split(h, Q0)
    # pn factor z − h/2
    pn = lambda q: C.markov_z(q) - h(q) / 2
    pn_q, pn_qi, pn_even, pn_odd = bar_split(pn, Q0)

    TOL = mp.mpf(10) ** (-30)
    z_is_even = abs(z_odd) < TOL
    h_is_odd = abs(h_even) < TOL
    pn_is_mixed = abs(pn_even) > TOL and abs(pn_odd) > TOL

    result = {
        "q0": mp.nstr(Q0, 20),
        "z": {"q": mp.nstr(z_q, 12), "qinv": mp.nstr(z_qi, 12),
              "even": mp.nstr(z_even, 12), "odd": mp.nstr(z_odd, 4), "parity": "bar-even"},
        "h": {"q": mp.nstr(h_q, 12), "qinv": mp.nstr(h_qi, 12),
              "even": mp.nstr(h_even, 4), "odd": mp.nstr(h_odd, 12), "parity": "bar-odd"},
        "pn_factor_z_minus_h_over_2": {
            "even_part": mp.nstr(pn_even, 12), "odd_part": mp.nstr(pn_odd, 12),
            "parity": "bar-MIXED"},
        "verdict": (
            "I-par REFINED: z bar-even, h bar-odd ⇒ pn factor (z−h/2) bar-mixed ⇒ the "
            "connected b₄ is BAR-MIXED, not purely bar-even (original I-par phrasing "
            "too strong). Prescription: the binding magnitude is the BAR-EVEN PROJECTION "
            "b₄^even = ½[b₄(q)+b₄(q⁻¹)]; the bar-odd projection is radiated (Q_β-like), "
            "not retained binding. The magnitude compute (next unit) targets b₄^even; "
            "I-conn / I-ceil apply to b₄^even. Scope-(a), no fit."),
    }

    payload = {
        "computation": "b4-connected-bar-parity",
        "description": ("I-par for the [1^4] connected-Ursell magnitude leg: z is bar-even, "
                        "h bar-odd ⇒ the pn factor and hence b₄ are bar-MIXED. Refines the "
                        "invariant to a prescription — the binding magnitude is the bar-even "
                        "projection b₄^even; bar-odd is radiated. audit-only, no fit."),
        "tier": "structural-exact (40 dps bar-split of the Markov building blocks)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] Ursell operator magnitude, invariant I-par",
            "scoping": "docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3",
            "bar_framework": "computations/binding_bar_even_odd_probe.py (retained/emitted)",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-connected-bar-parity", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("z_is_bar_even", computed=str(bool(z_is_even)), expected="True")
    wb.add_assertion("h_is_bar_odd", computed=str(bool(h_is_odd)), expected="True")
    wb.add_assertion("pn_factor_is_bar_mixed", computed=str(bool(pn_is_mixed)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== I-par: bar-parity of the connected 4-body building blocks ===")
    print(f"  z  = {float(z_q):.6f}   bar-EVEN  (z(q)=z(q⁻¹))")
    print(f"  h  = {float(h_q):.6f}   bar-ODD   (h(q)=−h(q⁻¹))")
    print(f"  pn = z − h/2 : even={float(pn_even):.6f}  odd={float(pn_odd):.6f}  → bar-MIXED")
    print("  ⇒ connected b₄ is bar-MIXED; binding magnitude = bar-EVEN projection b₄^even.")
    print("  (I-par refined from 'b₄ bar-even' to 'use b₄^even'; bar-odd is radiated.)")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
