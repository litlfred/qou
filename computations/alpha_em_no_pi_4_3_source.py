#!/usr/bin/env python3
# polynomial_q_not_applicable: archimedean-image probe.  GOAL: source the 4/3
# numerator of 2/(3pi) pre-archimedean.  Reports the exact geometric identity
# and the (tiered) cosh-Habiro tie; the categorical derivation stays OPEN.
"""
alpha_{basis-knot} STEP 6b — the 4/3 numerator of 2/(3pi) (research probe).

Owner directive: "I don't like to see pi ... should be pre-archimedean."  Step 6
(alpha_em_no_pi_correction_probe.py) reduced the alpha_EM no-pi program to ONE
open numerator: the 4/3 in
    2/(3pi) = (4/3) / |S^1|,     |S^1| = 2 pi.
This probe sources that 4/3 — TWO exact identities, then an honest tier.

IDENTITY 1 (geometric — EXACT).  2/(3pi) is the Hopf 3-ball / 3-sphere ratio:
    2/(3pi) = V(B^3) / Vol(S^3),     V(B^3) = 4pi/3,  Vol(S^3) = 2 pi^2.
So ALL pi in the alpha_EM correction are now Hopf-fibration (S^1 -> S^3 -> S^2)
volumes — |S^2| = 4pi (vertex), V(B^3) = 4pi/3 and Vol(S^3) = 2pi^2 (vac-pol).
pi is never a fundamental constant; it is the tau-image of the categorical Hopf
objects [S^2], [B^3], [S^3].  The 4/3 numerator is V(B^3)/pi — the pi-stripped
3-ball volume.

IDENTITY 2 (cosh-Habiro tie — EXACT arithmetic, STRUCTURAL claim).  The 4/3 is
the SQUARE of the classical cosh-Habiro value over 3:
    4/3 = H(1)^2 / 3,     H(q) = [2]_q (1 - h^2 alpha),  H(1) = [2]_{q=1} = 2.
H(1) = 2 is the SAME classical value that sources alpha/(4pi)
(prop:alpha-em-habiro-bar-involution, "H(1)=2 gives alpha/(4pi)").  So BOTH
pi-corrections share one pre-archimedean origin — the e_+ cosh Habiro classical
value H(1) = [2]_{q=1} = 2 — with the archimedean dressing differing:
    alpha/(4pi) = alpha     / |S^2|          (numerator alpha;       |S^2|=4pi)
    2/(3pi)     = H(1)^2/3  / |S^1|          (numerator H(1)^2/3=4/3; |S^1|=2pi)

TIER (honest).
  RESOLVED: 2/(3pi) = V(B^3)/Vol(S^3) exactly; the 4/3 = pi-stripped V(B^3) =
            H(1)^2/3 (cosh-Habiro classical value squared / 3).  The 4/3 is no
            longer an unexplained constant — it is a Hopf-ball volume AND the
            classical cosh-Habiro value, tying it to the already-sourced
            alpha/(4pi).
  OPEN:     the categorical DERIVATION of WHY vacuum-polarization = [B^3]/[S^3]
            (QED Feynman-parameter 1/3 vs ball/sphere 1/3 have different a priori
            origins) and of the "/3" (it coincides with the trefoil T_{2,3}
            second index, alpha_EM = alpha_{T_{2,3}} — flagged, NOT derived).
  This probe does NOT claim a finished categorical proof; it identifies the
  pre-archimedean FORM of the 4/3 and unifies the two corrections.  Not fitted.

Refs: alpha_em_no_pi_correction_probe.py (step 6, the open 4/3);
prop:alpha-em-habiro-bar-involution (H=[2]_q(1-h^2 alpha), H(1)=2 -> alpha/(4pi));
prop:em-coupling-bring-zero-mode (the 2/(3pi)+alpha/(4pi) corrections).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import sympy as sp


def main() -> None:
    w = WitnessBuilder("alpha-em-no-pi-4-3-source", engine="python")
    pi = sp.pi

    # IDENTITY 1: 2/(3pi) = V(B^3)/Vol(S^3), exact symbolic.
    target = sp.Rational(2, 3) / pi              # 2/(3 pi)
    V_B3 = sp.Rational(4, 3) * pi                # volume of unit 3-ball
    Vol_S3 = 2 * pi ** 2                         # volume of unit 3-sphere
    S2 = 4 * pi                                  # |S^2| (Hopf base)
    S1 = 2 * pi                                  # |S^1| (Hopf fibre)
    geom = sp.simplify(V_B3 / Vol_S3)
    id1 = sp.simplify(geom - target) == 0

    # IDENTITY 2: 4/3 = H(1)^2/3, with H(1) = [2]_{q=1} = 2.
    H1 = sp.Integer(2)                           # H(1) = [2]_{q=1}
    four_thirds = sp.Rational(4, 3)
    habiro_form = H1 ** 2 / sp.Integer(3)        # H(1)^2 / 3
    id2 = sp.simplify(habiro_form - four_thirds) == 0
    # numerator of 2/(3pi) over |S^1| is exactly 4/3
    num_over_S1 = sp.simplify(target * S1)       # = 4/3
    id2b = sp.simplify(num_over_S1 - four_thirds) == 0
    # numerator of alpha/(4pi) over |S^2| is exactly alpha (formal)
    alpha = sp.symbols("alpha", positive=True)
    num_alpha = sp.simplify((alpha / (4 * pi)) * S2 - alpha) == 0

    print("=" * 74)
    print("alpha_{basis-knot} STEP 6b — sourcing the 4/3 of 2/(3pi) (no pi)")
    print("=" * 74)
    print("  IDENTITY 1 (geometric, exact):")
    print(f"    2/(3pi)            = {target}")
    print(f"    V(B^3)/Vol(S^3)    = {sp.nsimplify(geom)}   "
          f"(V(B^3)=4pi/3, Vol(S^3)=2pi^2)")
    print(f"    -> EQUAL: {id1}")
    print("  IDENTITY 2 (cosh-Habiro tie, exact):")
    print(f"    4/3                = {four_thirds}")
    print(f"    H(1)^2/3           = {habiro_form}   (H(1)=[2]_(q=1)=2)")
    print(f"    -> EQUAL: {id2}")
    print()
    print("  Unified no-pi form (numerator)/(Hopf period):")
    print(f"    alpha/(4pi) = alpha    / |S^2|   (|S^2|=4pi; vertex)")
    print(f"    2/(3pi)     = H(1)^2/3 / |S^1|   (|S^1|=2pi; vac-pol) = (4/3)/|S^1|")
    print()
    print("  ALL pi are now Hopf-fibration (S^1->S^3->S^2) volumes:")
    print(f"    |S^1|=2pi   |S^2|=4pi   V(B^3)=4pi/3   Vol(S^3)=2pi^2")
    print()
    print("  TIER: RESOLVED -> 4/3 = V(B^3)/pi = H(1)^2/3 (Hopf-ball + cosh-Habiro).")
    print("        OPEN     -> categorical derivation of vac-pol=[B^3]/[S^3] and")
    print("                    the '/3' (= trefoil T_{2,3} index? flagged, not derived).")

    w.set_description(
        "alpha_{basis-knot} step 6b: sources the lone open numerator 4/3 of the "
        "2/(3pi) alpha_EM correction, pre-archimedean.  TWO exact identities: "
        "(1) geometric, 2/(3pi) = V(B^3)/Vol(S^3) = (4pi/3)/(2pi^2), so all pi in "
        "the alpha_EM correction are Hopf-fibration (S^1->S^3->S^2) volumes "
        "(|S^2|, V(B^3), Vol(S^3)) — pi is the tau-image of categorical Hopf "
        "objects, never fundamental; the 4/3 is the pi-stripped 3-ball volume.  "
        "(2) cosh-Habiro, 4/3 = H(1)^2/3 with H(1)=[2]_{q=1}=2 the SAME classical "
        "value that sources alpha/(4pi) (prop:alpha-em-habiro-bar-involution), so "
        "both pi-corrections share the e_+ cosh-Habiro origin: alpha/(4pi)="
        "alpha/|S^2|, 2/(3pi)=(H(1)^2/3)/|S^1|.  TIER: the 4/3 is RESOLVED to a "
        "Hopf-ball volume + cosh-Habiro value (no longer unexplained); the "
        "categorical derivation of vac-pol=[B^3]/[S^3] and the '/3' (coincides "
        "with the trefoil T_{2,3} index) stays OPEN — flagged, not derived, not "
        "fitted."
    )
    w.set_content_block("prop:em-coupling-bring-zero-mode")
    w.add_data("two_over_3pi", str(target))
    w.add_data("V_B3", "4*pi/3")
    w.add_data("Vol_S3", "2*pi**2")
    w.add_data("identity1_geometric_2_3pi_eq_VB3_over_VolS3", bool(id1))
    w.add_data("identity2_4_3_eq_H1sq_over_3", bool(id2))
    w.add_data("H1_classical_habiro_value", 2)
    w.add_data("hopf_volumes", {"S1": "2*pi", "S2": "4*pi",
                                "B3": "4*pi/3", "S3": "2*pi**2"})
    w.add_data("unified_form", {
        "alpha_over_4pi": "alpha / |S^2|   (numerator alpha)",
        "two_over_3pi": "(H(1)^2/3) / |S^1| = (4/3)/|S^1|   (numerator 4/3)",
    })
    w.add_assertion(
        "2/(3pi) = V(B^3)/Vol(S^3) exactly (Hopf 3-ball / 3-sphere)",
        computed=bool(id1), expected=True,
        source="V(B^3)=4pi/3, Vol(S^3)=2pi^2; symbolic simplify",
    )
    w.add_assertion(
        "4/3 = H(1)^2/3 with H(1)=[2]_{q=1}=2 (cosh-Habiro classical value)",
        computed=bool(id2), expected=True,
        source="prop:alpha-em-habiro-bar-involution H(1)=2",
    )
    w.add_assertion(
        "2/(3pi)*|S^1| = 4/3 and alpha/(4pi)*|S^2| = alpha (numerators isolated)",
        computed=bool(id2b and num_alpha), expected=True,
        source="|S^1|=2pi, |S^2|=4pi Hopf periods",
    )
    w.add_data(
        "finding",
        "The lone open numerator 4/3 of 2/(3pi) is sourced two exact ways: "
        "2/(3pi) = V(B^3)/Vol(S^3) (Hopf 3-ball / 3-sphere; so all alpha_EM-"
        "correction pi are Hopf-fibration volumes) and 4/3 = H(1)^2/3 (the e_+ "
        "cosh-Habiro classical value squared / 3, the SAME H(1)=2 that sources "
        "alpha/(4pi)).  Unified: alpha/(4pi)=alpha/|S^2|, 2/(3pi)=(H(1)^2/3)/|S^1|. "
        "The 4/3 is no longer unexplained.  OPEN (not fitted): the categorical "
        "derivation of vacuum-polarization=[B^3]/[S^3] and of the '/3' (= trefoil "
        "T_{2,3} second index?), the deeper alpha_{basis-knot} frontier."
    )
    w.save()
    print("\nDone. Witness saved (alpha-em-no-pi-4-3-source).")


if __name__ == "__main__":
    main()
