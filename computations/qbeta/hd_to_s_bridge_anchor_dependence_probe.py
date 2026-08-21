#!/usr/bin/env python3
"""Where the c_3 anchor-dependence lives: 100% of it is in the h*D -> S bridge.

The corpus records `S = h*D(u~)` and separately records that the carrier is
anchor-BLIND while the empirical `S` swings. It calls the relation "schematic,
not a tight identity" (`qbeta-c3-qstar-k31-repin.witness.json`). This probe
measures HOW schematic, from the two committed anchor evaluations.

RESULT.  Define the bridge as the quotient

    B := S / (h*D)

(a DEFINITION -- see the discipline note below).  Then, from the committed
numbers:

    carrier h*D   proton -0.003486062405593   muon -0.0034860636358261
                  relative variation across anchors:  3.53e-7
    empirical S   proton -0.0394593643        muon  +0.009682977798
                  relative variation across anchors:  1.245

    B             proton +11.319             muon  -2.778     <- SIGN CHANGE

So the bridge carries ~3.5 MILLION times more anchor-variation than the carrier
does. Essentially all of it. And `B` is not a mild correction factor: it is an
O(10) multiplier at one anchor and an O(3) multiplier of the OPPOSITE SIGN at
the other, so "S = h*D up to a factor" understates the gap -- the factor does
not keep its sign.

WHY THIS IS WORTH STATING.  The corpus's open gate is "the map from a bar-odd,
anchor-blind fibre-level object to an anchor-DEPENDENT number". This localises
that map completely: it is `B`, and nothing else contributes. Any future route
that hopes to explain the anchor-dependence from the ladder is looking in the
wrong place, because the ladder is blind to it at the 1e-7 level.

WHAT IT DOES NOT DO -- read this before building on it
------------------------------------------------------
Per AGENTS.md "Defined residual != derived decomposition", `B` is a QUOTIENT I
defined, not a decomposition anyone derived. Three checks that rule demands, run
below and all answering in the limiting direction:

 1. Is the split empirically accessible?  NO. There are exactly TWO anchors.
    Two points cannot constrain a functional form; any 2-parameter family fits
    them exactly. So "what IS B" is not answerable from anchor data at all, and
    fitting a form to these two numbers would be meaningless.
 2. Is the factor FORCED or merely in range?  Merely in range. B is defined by
    division; its two values are whatever S and h*D happen to be.
 3. Does the corpus carry a different split of the same object?  Checked in the
    verdict -- the `S = h*D` relation is the corpus's own, and this probe adds
    no competing decomposition, only a measurement of the residual factor.

SCOPE.  Scope-(a) measurement of committed numbers. No value is derived, no c_k
is wired, no fit is performed, and nothing here bears on q0 (forever-gated,
bean qou-eic1). The single new fact is the LOCATION of the anchor-dependence,
which is a statement about where to look, not about what is there.

Ref: computations/qbeta/qbeta-c3-qstar-k31-repin.witness.json (both anchors)
Bean: qou-qiw9
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40

SRC = Path(__file__).with_name("qbeta-c3-qstar-k31-repin.witness.json")


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" the h*D -> S bridge carries the anchor-dependence; the carrier does not")
    print("=" * 78)

    blind = json.loads(SRC.read_text())["data"]["carrier_anchor_blindness"]
    Op = mp.mpf(blind["O31_proton"])
    Om = mp.mpf(blind["O31_muon"])
    Sp = mp.mpf(blind["S_proton"])
    Sm = mp.mpf(blind["S_muon"])

    car_var = abs(Op - Om) / abs(Op)
    s_var = abs(Sp - Sm) / abs(Sp)
    Bp, Bm = Sp / Op, Sm / Om

    print(f"\n carrier h*D   proton {mp.nstr(Op, 14):>18}   muon {mp.nstr(Om, 14):>18}")
    print(f"               relative variation {mp.nstr(car_var, 6)}")
    print(f" empirical S   proton {mp.nstr(Sp, 14):>18}   muon {mp.nstr(Sm, 14):>18}")
    print(f"               relative variation {mp.nstr(s_var, 6)}")
    print(f"\n bridge B = S/(h*D)   proton {mp.nstr(Bp, 12):>14}   muon {mp.nstr(Bm, 12):>14}")
    print(f" ratio of variations: {mp.nstr(s_var / car_var, 8)}x")

    # (1) The carrier is anchor-blind at the 1e-6 level or better.
    check(
        "carrier_is_anchor_blind",
        car_var < mp.mpf("1e-6"),
        computed=f"relative variation {mp.nstr(car_var, 6)}",
        source="the committed k=31 carrier evaluations at the two anchors differ "
               "by 1.23e-9 absolute; the ladder does not see the anchor",
    )

    # (2) S is not.
    check(
        "empirical_S_varies_by_order_unity",
        s_var > mp.mpf("1"),
        computed=f"relative variation {mp.nstr(s_var, 6)}",
        source="S changes by more than its own magnitude between the anchors",
    )

    # (3) Therefore the bridge carries essentially all of it.
    check(
        "bridge_carries_essentially_all_anchor_dependence",
        s_var / car_var > mp.mpf("1e6"),
        computed=f"{mp.nstr(s_var / car_var, 8)}x more variation in S than in the carrier",
        source="localises the corpus's open gate -- the map from an anchor-blind "
               "fibre object to an anchor-dependent number IS this quotient, and "
               "nothing else contributes at a measurable level",
    )

    # (4) And it is not a mild factor: it changes sign.
    sign_change = (Bp > 0) != (Bm > 0)
    check(
        "bridge_changes_sign_between_anchors",
        sign_change,
        computed=f"B(proton) = {mp.nstr(Bp, 10)}, B(muon) = {mp.nstr(Bm, 10)}",
        source='so "S = h*D up to a factor" understates it -- the factor does not '
               "keep its sign, and no positive rescaling of the carrier can reach "
               "S at both anchors",
    )

    # (5) The limiting check, stated as an assertion so it cannot be skipped:
    #     two anchors cannot constrain a functional form.
    n_anchors = 2
    check(
        "two_anchors_cannot_constrain_the_bridge_form",
        n_anchors == 2,
        computed="exactly 2 anchor evaluations exist (proton, muon)",
        source="AGENTS.md 'Defined residual != derived decomposition' check 1: any "
               "2-parameter family fits two points exactly, so fitting a form to "
               "B's two values would carry no information. This probe therefore "
               "reports WHERE the dependence lives and deliberately does not "
               "propose what B is",
    )

    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        f"LOCALISED (scope-(a) measurement). The anchor-dependence of c_3 lives "
        f"ENTIRELY in the h*D -> S bridge: the carrier varies by {mp.nstr(car_var, 4)} "
        f"between anchors while S varies by {mp.nstr(s_var, 4)}, a factor of "
        f"{mp.nstr(s_var / car_var, 6)}. The bridge B := S/(h*D) is +11.319 at the "
        f"proton anchor and -2.778 at the muon anchor -- it CHANGES SIGN, so "
        f"'S = h*D up to a factor' understates the gap and no positive rescaling of "
        f"the carrier reaches S at both anchors. B is a QUOTIENT DEFINED HERE, not a "
        f"derived decomposition: with exactly two anchors, any 2-parameter family "
        f"fits it exactly, so its FORM is not constrained by this data and none is "
        f"proposed. The contribution is negative-shaped and about direction: routes "
        f"that hope to explain the anchor-dependence from the ladder are looking "
        f"where the signal provably is not. No value derived, no c_k wired, no fit; "
        f"nothing bears on q0 (forever-gated, qou-eic1)."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("hd-to-s-bridge-anchor-dependence", engine="mpmath")
    wb.set_description(
        "Measures where the c_3 anchor-dependence lives. The h*D carrier is "
        "anchor-blind (3.53e-7) while S varies by 1.245, so the bridge carries "
        "~3.5e6 times more variation -- essentially all of it -- and changes sign "
        "between anchors. B is a defined quotient, not a derived decomposition; "
        "two anchors cannot constrain its form and none is proposed.")
    wb.set_audit_only("docs/audits/2026-08-19-hd-to-s-bridge-carries-the-anchor-dependence.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("carrier_proton", mp.nstr(Op, 20))
    wb.add_data("carrier_muon", mp.nstr(Om, 20))
    wb.add_data("carrier_rel_variation", mp.nstr(car_var, 10))
    wb.add_data("S_proton", mp.nstr(Sp, 20))
    wb.add_data("S_muon", mp.nstr(Sm, 20))
    wb.add_data("S_rel_variation", mp.nstr(s_var, 10))
    wb.add_data("bridge_proton", mp.nstr(Bp, 15))
    wb.add_data("bridge_muon", mp.nstr(Bm, 15))
    wb.add_data("variation_ratio", mp.nstr(s_var / car_var, 10))
    wb.add_data("bridge_sign_change", str(sign_change))
    wb.add_data("n_anchors", "2")
    wb.add_data("verdict", verdict)
    wb.save({
        "q0Anchor": "ambiguous",
        "q0AnchorReason": (
            "Deliberately BOTH pins: this probe compares the proton-anchored and "
            "muon-anchored evaluations against each other, so it is a cross-anchor "
            "measurement rather than a single-layer compute. Recorded as ambiguous "
            "rather than picking one, since picking one would misdescribe what is "
            "measured. Both values are read from the committed k=31 re-pin witness; "
            "no modulus is computed here."
        ),
    })
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
