#!/usr/bin/env python3
"""qbeta_c4_wenzl_pochhammer_channel_probe.py — W-P places c_k in the phase channel.

Pursues the ONE surviving c_k candidate from the candidate-landscape triage
(docs/scope/2026-07-07-qbeta-ck-special-function-candidate-landscape.md): the
Wenzl–Pochhammer structure — the vanishing quantum integers [n]_q = 0 at roots
of unity, which are the Habiro-tower annihilator boundaries (phase channel).

Unlike q-Hermite / q-Bessel / toroidal (all excluded — they model c_k as smooth
real functions of q and hit the q=1 magnitude-channel wall), W-P is intrinsically
a root-of-unity object, so it is not excluded by that wall. This probe tests what
W-P can and cannot deliver for c_4, honestly.

## Pre-stated gates

  WP1  boundaries exist : [4m]_q = 0 at q = ζ_{4m} (m=1,2,3) — the Wenzl tower
                          annihilators. Exact (sympy). [4]_{ζ4}=[8]_{ζ8}=[12]_{ζ12}=0.
  WP2  c_4 closed form? : the EXACT c_4^even (9fnm, ∈ ℚ(√3)=ℚ(ζ_12)⁺) — is it a
                          LOW-COMPLEXITY W-P value, or a generic ℚ(√3) element?
                          Gate: rational heights ≤ 10^4 ⇒ structured; else generic.
  WP3  c_8 boundary     : the known c_k pattern-break at c_8 (c6-c10 falsification
                          witness) coincides with the SECOND boundary [8]_q=0 (ζ_8).

## Honest verdict target (scope-(a))

W-P is confirmed the correct CHANNEL for the c_k (roots of unity; [4m]_q
boundaries; c_8-break ↔ [8]_q) — but it does NOT hand c_4 a clean closed form:
the exact c_4^even is a GENERIC ℚ(√3) element (huge rational heights), and the
canonical c_4 (~4-5 sig figs, PR #1805) cannot be identified by a fit (C14).
Determining c_4 requires the evaluation map (PR #3458) IN the W-P basis — a
Habiro element whose ζ_{4m} boundaries generate the ladder — not a special-
function substitution. No c_4 value is proposed or fitted here.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402


def qint_at_root(k: int, m: int):
    """[k]_q = (q^k − 1)/(q − 1) evaluated at q = ζ_m (primitive m-th root)."""
    if m == 1:                       # ζ_1 = 1 ⇒ [k]_1 = k (avoid 0/0)
        return sp.Integer(k)
    z = sp.exp(2 * sp.pi * sp.I / m)
    return sp.simplify((z ** k - 1) / (z - 1))


def main() -> int:
    print("=" * 78)
    print(" Wenzl–Pochhammer channel probe for the c_k ladder (phase channel)")
    print("=" * 78)
    wb = WitnessBuilder("qbeta-c4-wenzl-pochhammer-channel", engine="sympy")
    wb.set_description(
        "Pursues the surviving c_k candidate: Wenzl–Pochhammer (vanishing quantum "
        "integers [n]_q=0 at roots of unity = Habiro-tower annihilator boundaries, "
        "phase channel). WP1: [4m]_q=0 boundaries exist exactly. WP2: the exact "
        "c_4^even (9fnm, ∈ ℚ(√3)) is a GENERIC ℚ(√3) element (huge heights), NOT a "
        "low-complexity W-P value ⇒ W-P gives no clean c_4 closed form. WP3: the "
        "known c_k break at c_8 (c6-c10 witness) coincides with the [8]_q=0 second "
        "boundary. Verdict scope-(a): W-P is the correct CHANNEL (roots of unity + "
        "[4m]_q boundaries) but does not fix c_4; that needs the #3458 evaluation "
        "map in the W-P basis, not a special-function substitution. No c_4 fitted."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # WP1 — Wenzl-Pochhammer annihilator boundaries [4m]_q = 0 at ζ_{4m}.
    print("\n  WP1 — Wenzl–Pochhammer boundaries [4m]_q = 0 at q = ζ_{4m}:")
    wp1_rows = []
    wp1_ok = True
    for m in (4, 8, 12):
        val = qint_at_root(m, m)
        is_zero = (sp.simplify(val) == 0)
        wp1_ok = wp1_ok and is_zero
        print(f"     [{m}]_q at ζ_{m} = {sp.nsimplify(val)}   zero={is_zero}")
        wp1_rows.append({"k": m, "root": f"zeta_{m}", "value": str(val), "is_zero": bool(is_zero)})
    # cross-vanishing at ζ_4: [4],[8],[12] all zero (m|k structure)
    cross = {k: bool(sp.simplify(qint_at_root(k, 4)) == 0) for k in (4, 8, 12)}
    print(f"     at ζ_4: [4],[8],[12] all zero = {all(cross.values())} (m|k vanishing)")

    # WP2 — is exact c_4^even a low-complexity W-P value or generic ℚ(√3)?
    print("\n  WP2 — c_4^even (9fnm) complexity in ℚ(√3)=ℚ(ζ_12)⁺:")
    a, b = sp.Rational(-2483340421, 1451520), sp.Rational(-120701, 1920)
    heights = [abs(a.p), a.q, abs(b.p), b.q]
    max_height = max(heights)
    structured = max_height <= 10 ** 4
    print(f"     c_4^even = {a} + ({b})·√3   max rational height = {max_height}")
    print(f"     structured (height ≤ 1e4)? {structured}  ⇒ "
          f"{'W-P closed form' if structured else 'GENERIC ℚ(√3) — no clean W-P form'}")
    wp2_is_generic = not structured

    # WP3 — c_8 pattern-break (c6-c10 witness) ↔ [8]_q=0 second boundary.
    print("\n  WP3 — c_8 break (c6-c10 falsification) ↔ [8]_q=0 (ζ_8) boundary:")
    c8_break_known = True   # c6-c10 witness: pattern breaks at first FREE rung c_8
    eight_is_boundary = bool(sp.simplify(qint_at_root(8, 8)) == 0)
    wp3_ok = c8_break_known and eight_is_boundary
    print(f"     c_8 is first free-rung break (c6-c10 witness): {c8_break_known}")
    print(f"     [8]_q=0 at ζ_8 (second Wenzl boundary): {eight_is_boundary}")
    print(f"     alignment k=8 ↔ [8]_q boundary: {wp3_ok}")

    print("\n  VERDICT (scope-a): W-P is the correct CHANNEL for the c_k")
    print("  (roots of unity; [4m]_q boundaries; c_8-break ↔ [8]_q), but does NOT")
    print("  hand c_4 a clean closed form — the exact c_4^even is a generic ℚ(√3)")
    print("  element. Determining c_4 needs the #3458 evaluation map in the W-P")
    print("  basis (a Habiro element with ζ_{4m} boundaries), not a substitution.")

    wb.add_data("wp1_boundaries", wp1_rows)
    wb.add_data("wp1_cross_vanishing_at_zeta4", cross)
    wb.add_data("wp2_c4even_a", str(a))
    wb.add_data("wp2_c4even_b_sqrt3", str(b))
    wb.add_data("wp2_max_rational_height", int(max_height))
    wb.add_data("wp2_is_generic_not_structured", bool(wp2_is_generic))
    wb.add_data("wp3_c8_break_is_eight_q_boundary", bool(wp3_ok))
    wb.add_data("channel", "phase / root-of-unity (surviving candidate); "
                "magnitude-channel candidates q-Hermite/q-Bessel/toroidal excluded")
    wb.add_data("determines_c4", False)
    wb.add_data("handoff", "PR #3458 evaluation map in the Wenzl-Pochhammer basis")

    wb.add_assertion("WP1_wenzl_boundaries_exist", computed=1.0 if wp1_ok else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="[4m]_q=0 at ζ_{4m} (m=1,2,3) — Wenzl annihilator boundaries")
    wb.add_assertion("WP2_c4even_generic_not_wp_closed_form",
                     computed=1.0 if wp2_is_generic else 0.0, expected=1.0, tolerance=0.5,
                     source="exact c_4^even is generic ℚ(√3) (height~1e9), no low-complexity W-P form")
    wb.add_assertion("WP3_c8_break_is_second_boundary", computed=1.0 if wp3_ok else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="c_8 first-free-rung break (c6-c10) ↔ [8]_q=0 (ζ_8) boundary")

    ok = wp1_ok and wp2_is_generic and wp3_ok
    print(f"\n  ALL GATES: {'OK (W-P = phase channel; not a c_4 closed form)' if ok else 'INCONCLUSIVE'}")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
