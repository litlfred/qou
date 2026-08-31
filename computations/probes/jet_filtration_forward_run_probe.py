#!/usr/bin/env python3
"""jet_filtration_forward_run_probe.py

Front C: run the jet filtration FORWARD with the corpus's own multiplicity and
volumes. It runs on three points, all of which were used to set it, and stops
at A=4 for want of Vol_A. There is no out-of-sample test anywhere.

WHY THIS EXISTS
---------------
`bk-coordination-multiplicity.md` gives w_n(K) = M_n(A) * Vol_n(K) with the
multiplicity read off AME as M_need(A) = B_AME/(m_e * Vol_A), matched at the
non-magic A=3 pair by z = A-1 to better than 3%. Nobody had run the resulting
construction forward and asked what it predicts. This does that, using the
corpus's own numbers and adding nothing.

MEASURED, mpmath 50 dps, AME and m_e from the vendored table:

    iso    A   Vol_A       z   B_pred    B_AME    pred/AME   M_need   M_need/z
    2H     2   0.0         1    0.0      2.2246    0.0        nan      --
    3H     3   8.2863168   2    8.4686   8.4818    0.99844    2.00312  1.00156
    3He    3   7.3277248   2    7.4889   7.7180    0.97031    2.06119  1.03059
    4He    4   7.3277248   3   11.2334  28.2957    0.397      7.55667  2.51889

THE FINDING -- it is about the DATA available to the construction
------------------------------------------------------------------
1. **A=2 is not a test of this form.** Vol(Hopf) = 0 EXACTLY (Seifert-fibred),
   so B_pred = 0 against 2.2246 MeV. The block says so itself and offers the
   coordination count as the non-vanishing replacement there. Excluded as a
   test, not counted as a failure.

2. **A=3 is where the multiplicity was READ OFF.** 3H at 0.16% and 3He at 3.0%
   are the calibration points reproducing themselves, not predictions.

3. **A=4 needs the whole enhancement**: pred/AME = 0.397, i.e. the construction
   supplies 39.7% of the 4He binding and the remaining factor 2.51889 is the
   `M_need/z ~ 2.52 ~ a_D^(4)` magic-shell term.

4. **A >= 5 CANNOT BE RUN.** Vol_A needs a per-nucleus link assignment, and
   `computations/binding_link_volumes.py` supplies one only for 2H (Hopf, Vol=0),
   3H (8_11), 3He (L6a4) and the 4He "L6a4 base". I found no nucleus->knot
   accessor covering A >= 5; the knot-periodic-table appendix is KNOT-indexed,
   not nucleus-indexed, so it does not supply one either.

CONSEQUENCE -- the route is currently untestable, and that is not the same as
wrong
------------------------------------------------------------------------------
Every point where the construction runs is a point used to set it: two at A=3
fix the multiplicity, one at A=4 fixes the enhancement, and A=2 is degenerate.
**Zero out-of-sample support.** That is a strictly worse shape than bean
`qou-ebs6`'s recorded "one parameter, two points, zero out-of-sample support" --
here the 2.52 is one parameter against ONE point.

This does not refute the jet filtration and does not say 2.52 is wrong. It says
no amount of work on the magnitude can be VALIDATED until Vol_A extends past
A=4, because there is nothing to validate against. Extending the per-nucleus
link assignment is therefore the prerequisite for deciding any of the three
routes on the table, not a side quest.

It also composes with the session's earlier measurement that the AME light-nucleus
cumulant tower is convention-limited to under one significant digit
(`binding_magnitude_is_not_validatable_probe`): that bounded the PRECISION of
the target, this bounds the COUNT of independent targets. Both point the same
way -- the constraint is the data, not the search.

SCOPE
-----
Scope-(a). Nothing refuted, no mechanism excluded, nothing wired, no new number
proposed. The three ratios are the corpus's own construction evaluated.

NO FLOAT64: mpmath 50 dps; AME, m_e and the volumes from the corpus.
"""

import sys
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from substrate.codata_constants import M_E_MEV  # noqa: E402
from substrate.codata_constants import ame_binding_mev as B  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

# volumes exactly as computations/binding_link_volumes.py records them
VOL = {
    "2H": (mp.mpf(0), "Hopf L2a1, Seifert-fibred, Vol = 0"),
    "3H": (mp.mpf("8.286316817806593"), "8_11 knot"),
    "3He": (mp.mpf("7.327724753417752"), "L6a4 = Borromean"),
    "4He": (mp.mpf("7.327724753417752"), "L6a4 base"),
}
ROWS = [("2H", 1, 2), ("3H", 1, 3), ("3He", 2, 3), ("4He", 2, 4)]


def fmt(x):
    return mp.nstr(mp.mpf(x), 30)


def main():
    wb = WitnessBuilder("jet-filtration-forward-run", engine="mpmath")
    wb.set_description(
        "Runs the jet filtration forward with the corpus's own M_n = z = A-1 "
        "and Vol_A. It reproduces the A=3 pair it was read off from (0.16% and "
        "3.0%), supplies only 39.7% of 4He (the rest is the 2.51889 magic-shell "
        "factor), is degenerate at A=2 (Vol(Hopf) = 0 exactly), and CANNOT RUN "
        "at A>=5 because binding_link_volumes assigns links only up to 4He and "
        "no nucleus->knot accessor covers A>=5. Every point where it runs was "
        "used to set it: ZERO out-of-sample support, a worse shape than "
        "qou-ebs6's one-parameter-two-points. Scope-(a): nothing refuted; the "
        "route is untestable until Vol_A extends past A=4."
    )

    me = mp.mpf(str(M_E_MEV))
    ok = True
    data = {}

    print(f"{'iso':>5s}{'A':>3s}{'Vol_A':>12s}{'z':>4s}{'B_pred':>11s}"
          f"{'B_AME':>11s}{'pred/AME':>10s}{'M_need':>9s}{'M_need/z':>10s}")
    for lbl, Z, A in ROWS:
        V, note = VOL[lbl]
        z = A - 1
        pred = me * z * V
        ame = B(Z, A)
        ratio = pred / ame
        if V > 0:
            mneed = ame / (me * V)
            menz = mneed / z
        else:
            mneed = menz = None
        data[lbl] = {"A": A, "Vol": fmt(V), "vol_note": note, "z": z,
                     "B_pred": fmt(pred), "B_AME": fmt(ame),
                     "pred_over_AME": fmt(ratio),
                     "M_need": fmt(mneed) if mneed is not None else "undefined (Vol=0)",
                     "M_need_over_z": fmt(menz) if menz is not None else "undefined"}
        print(f"{lbl:>5s}{A:>3d}{mp.nstr(V,8):>12s}{z:>4d}{mp.nstr(pred,7):>11s}"
              f"{mp.nstr(ame,7):>11s}{mp.nstr(ratio,5):>10s}"
              f"{mp.nstr(mneed,6) if mneed is not None else 'n/a':>9s}"
              f"{mp.nstr(menz,6) if menz is not None else '--':>10s}")
    wb.add_data("forward_run", data)

    # 1. the A=3 pair reproduces itself -- calibration, not prediction
    r3h = mp.mpf(data["3H"]["pred_over_AME"])
    r3he = mp.mpf(data["3He"]["pred_over_AME"])
    wb.add_assertion(
        name="A3_pair_reproduces_the_points_it_was_read_off",
        computed=fmt(max(abs(1 - r3h), abs(1 - r3he))),
        expected="0.0297", tolerance="0.001",
        unit="worst relative miss on the A=3 pair",
        source=("3H 0.16%, 3He 3.0%; these are the calibration points, so "
                "agreement here is not a prediction"))
    if abs(max(abs(1 - r3h), abs(1 - r3he)) - mp.mpf("0.0297")) > mp.mpf("0.001"):
        ok = False
        print("   FAIL: A=3 miss moved")

    # 2. A=4 needs the whole enhancement
    r4 = mp.mpf(data["4He"]["pred_over_AME"])
    wb.add_assertion(
        name="A4_supplied_fraction_before_enhancement",
        computed=fmt(r4), expected="0.397", tolerance="0.001",
        unit="fraction of B(4He) the construction supplies",
        source="the remaining factor is M_need/z = 2.51889, the magic-shell term")
    if abs(r4 - mp.mpf("0.397")) > mp.mpf("0.001"):
        ok = False
        print("   FAIL: A=4 fraction moved")

    # 3. A=2 is degenerate, structurally
    wb.add_assertion(
        name="A2_volume_carrier_vanishes_exactly",
        computed=fmt(VOL["2H"][0]), expected="0", tolerance="0",
        unit="Vol(Hopf)",
        source=("Seifert-fibred, so B_pred = 0 against 2.2246 MeV. Excluded as "
                "a test of this form, not counted as a failure -- the block "
                "offers the coordination count as the replacement there"))
    if VOL["2H"][0] != 0:
        ok = False
        print("   FAIL: Vol(Hopf) is not exactly 0")

    wb.add_data("why_A5_and_beyond_cannot_run", {
        "requirement": "Vol_A needs a per-nucleus link assignment",
        "what_exists": ("binding_link_volumes.py: 2H Hopf (Vol=0), 3H 8_11, "
                        "3He L6a4, 4He 'L6a4 base'. Nothing above A=4."),
        "what_does_not": ("no nucleus->knot accessor for A>=5 found; the "
                          "knot-periodic-table appendix is KNOT-indexed, not "
                          "nucleus-indexed, so it does not supply one"),
    })
    wb.add_data("out_of_sample_support", {
        "independent_points_where_it_runs": 3,
        "used_for_calibration": ("2 at A=3 fix the multiplicity; 1 at A=4 fixes "
                                 "the 2.51889 enhancement"),
        "degenerate": "A=2, Vol = 0 exactly",
        "out_of_sample": 0,
        "comparison": ("strictly worse than bean qou-ebs6's recorded 'one "
                       "parameter, two points, zero out-of-sample support' -- "
                       "here 2.52 is one parameter against ONE point"),
        "prerequisite": ("extending the per-nucleus link assignment past A=4 is "
                         "the prerequisite for DECIDING any route here, not a "
                         "side quest"),
    })

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
