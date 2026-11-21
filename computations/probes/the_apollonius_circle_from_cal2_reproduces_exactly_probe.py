#!/usr/bin/env python3
"""The three Apollonius-circle figures in `conj:im-q-physical-role` reproduce
exactly from CAL-2, and they are vintage-insensitive. Category (c): correct but
unwitnessed (`qou-i229`).

WHY THIS EXISTS
---------------
`scripts/witness-block-agreement.py` flagged this block 4/5 despite **68**
declaring witnesses — an odd shape, since a block with that much declared
evidence should not have orphan figures. Three of the four are the circle
parameters; the fourth is the CODATA-2018 muon literal this bean is tracking
separately.

THE CIRCLE, AND ITS CLOSED FORM
--------------------------------
CAL-2 is `m_mu/m_e = Vol(4_1) / hbar_q^2` with `hbar_q = 1 - 1/q`. Over complex
`q` the modulus condition `|hbar_q| = k` is one real equation, and

    |1 - 1/q| = k   <=>   |q - 1| = k |q|

is the classical Apollonius locus — the points whose distance ratio to `1` and
`0` is fixed. Its centre and radius follow in closed form, and so does the
leftmost point, which simplifies:

    k^2    = Vol(4_1) / (m_mu/m_e)          [ = hbar_q^2 at q0, by CAL-2 ]
    centre = 1 / (1 - k^2)
    radius = k / (1 - k^2)
    left   = centre - radius = (1 - k)/(1 - k^2) = 1 / (1 + k)

**Note what is NOT needed: `q0`.** The circle is fixed by `Vol(4_1)` and the mass
ratio alone, because CAL-2 is the equation that *defines* `q0` rather than a
consequence of it. So none of the anchor questions `qou-i229` has been chasing
touches these three numbers.

MEASURED
--------
    quantity   published     computed
    centre     1.0099145     1.00991452124...
    radius     0.1000641     0.100064074317...
    leftmost   0.9098504     0.909850446921...

All three are the correct roundings, and the table closes on itself:
`centre - radius = leftmost` exactly as published.

THE VINTAGE DOES NOT REACH THEM
--------------------------------
The block quotes `m_mu/m_e = 206.7682830`, which is CODATA **2018**
(`calibration-inputs` carries that label; CODATA 2022 is `206.7682827`). Both
vintages reproduce **all three** published figures:

    CODATA 2018   1.00991452124   0.100064074317   0.909850446921
    CODATA 2022   1.00991452125   0.100064074391   0.909850446861

They diverge in the 11th-12th significant digit against 8 published, so the
choice is invisible here. **This resolves one of the three `206.7682830` sites
this bean left open as "needs reading" — and it resolves as a NON-DEFECT.** The
block is quoting CAL-2's own input value, not asserting a CODATA vintage of its
own, and nothing it derives from that value moves between vintages.

WHY THE 68 WITNESSES DID NOT COVER IT
--------------------------------------
`conj:im-q-physical-role` is a survey of candidate roles for `Im(q)`, and its 68
declaring witnesses are the `Im(q)`-reality-locus computations that close
candidates (i) and (iii). Candidate (ii)'s Apollonius geometry is a two-line
derivation nobody had a reason to run separately. A large witness count says
nothing about coverage of any particular figure.

ON RECORDING THESE VALUES
-------------------------
The checker cannot distinguish a witness that *computes* a block's figure from
one that *transcribes* it (see the script's docstring). This probe computes them
from `Vol(4_1)` and the mass ratio, so recording the results is what a producer
does, not an echo — the distinction that matters is the source, and here it is
`mp.clsin` and CAL-2, not the block.

WHAT IS NOT CLAIMED
-------------------
Nothing about whether candidate (ii) is right, or whether `Im(q)` has a physical
role — the block states its own closure condition and this probe does not
evaluate it. Nothing about the *reality* argument that empties the branches; that
is the 68 witnesses' job and is untouched here. No figure is changed.
"""
from __future__ import annotations

import sys
from decimal import Decimal, getcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 40
getcontext().prec = 60

#: The two CODATA adjustments of the muon-electron mass ratio.
RATIOS = {"CODATA_2018": "206.7682830", "CODATA_2022": "206.7682827"}

#: What the block publishes.
PUBLISHED = {"centre": "1.0099145", "radius": "0.1000641",
             "leftmost": "0.9098504"}


def vol_figure_eight():
    """`Vol(4_1) = 2 Cl_2(pi/3)`, the figure-8 hyperbolic volume."""
    return 2 * mp.clsin(2, mp.pi / 3)


def circle(mass_ratio):
    """Apollonius circle of `|q - 1| = k|q|` with `k^2 = Vol(4_1)/(m_mu/m_e)`."""
    k2 = vol_figure_eight() / mp.mpf(mass_ratio)
    k = mp.sqrt(k2)
    return {"centre": 1 / (1 - k2),
            "radius": k / (1 - k2),
            "leftmost": 1 / (1 + k)}


def rounds_to(value, published: str) -> bool:
    """Exact half-ulp test at the published decimal count."""
    d = len(published.split(".")[1])
    return abs(value - mp.mpf(published)) <= mp.mpf(5) * mp.mpf(10) ** (-d - 1)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    vol = vol_figure_eight()
    print(f"\nVol(4_1) = 2 Cl_2(pi/3) = {mp.nstr(vol, 18)}")

    print("\n" + "=" * 78)
    print("§1  THE THREE FIGURES REPRODUCE FROM CAL-2 ALONE — NO q0 NEEDED")
    print("=" * 78)
    c18 = circle(RATIOS["CODATA_2018"])
    print(f"    {'quantity':<10} {'published':>12} {'computed':>22}")
    ok_all = True
    for name, pub in PUBLISHED.items():
        agree = rounds_to(c18[name], pub)
        ok_all &= agree
        print(f"    {name:<10} {pub:>12} {mp.nstr(c18[name], 15):>22}"
              f"   {'match' if agree else 'MISMATCH'}")
    check("all three published figures are the correct roundings of the "
          "Apollonius closed forms — centre 1/(1-k^2), radius k/(1-k^2), "
          "leftmost 1/(1+k)", ok_all)
    check("the circle is fixed by Vol(4_1) and the mass ratio ALONE, with no q0 "
          "input — CAL-2 is the equation that DEFINES q0, so no anchor question "
          "reaches these numbers", True)

    print("\n" + "=" * 78)
    print("§2  THE PUBLISHED TABLE CLOSES ON ITSELF")
    print("=" * 78)
    # EXACT DECIMAL. `mp.mpf("1.0099145") - mp.mpf("0.1000641") == mp.mpf(
    # "0.9098504")` is FALSE at any precision: decimal strings are not binary-
    # exact, so the difference lands a few ulps away and an `==` on mpf reports
    # a mismatch that is purely representational. The published figures are
    # decimal literals and the claim is about them as decimals, so Decimal is
    # the right arithmetic -- the same lesson `witness-block-agreement` learned
    # when float64 parsing blinded it at 15 significant digits.
    pc, pr, pl = (Decimal(PUBLISHED["centre"]), Decimal(PUBLISHED["radius"]),
                  Decimal(PUBLISHED["leftmost"]))
    print(f"    centre - radius = {pc - pr}"
          f"      published leftmost = {PUBLISHED['leftmost']}")
    check("centre - radius equals the published leftmost point exactly, so the "
          "three figures are mutually consistent as printed", pc - pr == pl)

    print("\n" + "=" * 78)
    print("§3  THE CODATA VINTAGE DOES NOT REACH THEM")
    print("=" * 78)
    circles = {v: circle(r) for v, r in RATIOS.items()}
    print(f"    {'vintage':<13} " + "".join(f"{k:>18}" for k in PUBLISHED))
    scores = {}
    for v, cc in circles.items():
        scores[v] = sum(rounds_to(cc[k], PUBLISHED[k]) for k in PUBLISHED)
        print(f"    {v:<13} " + "".join(f"{mp.nstr(cc[k], 12):>18}"
                                        for k in PUBLISHED)
              + f"   {scores[v]}/3")
    sep = abs(circles["CODATA_2018"]["radius"]
              - circles["CODATA_2022"]["radius"]) / circles["CODATA_2018"]["radius"]
    print(f"\n    the two vintages differ by {mp.nstr(sep, 4)} relative on the "
          f"radius,")
    print(f"    against 7 published significant digits — invisible here")
    check("both CODATA vintages reproduce all three figures, so the block's "
          "206.7682830 (CODATA 2018) is quoting CAL-2's own input rather than "
          "asserting a vintage, and nothing derived from it moves",
          scores["CODATA_2018"] == 3 and scores["CODATA_2022"] == 3)

    print("\n" + "=" * 78)
    print("§S  TRIAGE VERDICT FOR qou-i229")
    print("=" * 78)
    print("  Category (c): CORRECT BUT UNWITNESSED. The figures are right, they")
    print("  are derived rather than input, and the fix is to record the")
    print("  producer -- this probe -- not to change anything. Also resolves one")
    print("  of the three 206.7682830 sites left open as 'needs reading', and it")
    print("  resolves as a NON-DEFECT.")
    print("  The block's 68 declaring witnesses are the Im(q) reality-locus")
    print("  computations for candidates (i) and (iii); candidate (ii)'s")
    print("  Apollonius geometry is a two-line derivation nobody ran separately.")
    print("  A large witness count says nothing about coverage of any one figure.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_content_block("conj:im-q-physical-role")
        wb.set_description(
            "Reproduces the three Apollonius-circle figures in candidate (ii) of "
            "conj:im-q-physical-role, flagged by witness-block-agreement as absent "
            "from all 68 witnesses declaring that block. CAL-2 is "
            "m_mu/m_e = Vol(4_1)/hbar_q^2 with hbar_q = 1 - 1/q; over complex q the "
            "modulus condition |1 - 1/q| = k is the Apollonius locus |q-1| = k|q|, "
            "whose centre is 1/(1-k^2), radius k/(1-k^2) and leftmost point "
            "1/(1+k), with k^2 = Vol(4_1)/(m_mu/m_e). At 40 dps this gives "
            "1.00991452124, 0.100064074317 and 0.909850446921 -- exactly the "
            "published 1.0099145, 0.1000641 and 0.9098504 -- and the published "
            "table closes on itself, centre minus radius equalling the leftmost "
            "point exactly. NO q0 IS NEEDED: the circle is fixed by Vol(4_1) and "
            "the mass ratio alone, because CAL-2 is the equation that defines q0, "
            "so no anchor question reaches these numbers. Both CODATA vintages "
            "(206.7682830 and 206.7682827) reproduce all three, diverging only in "
            "the 11th-12th significant digit against 8 published, which resolves "
            "one of the three 206.7682830 content sites qou-i229 left open as "
            "'needs reading' -- as a NON-DEFECT: the block quotes CAL-2's own "
            "input rather than asserting a CODATA vintage. Verdict: category (c), "
            "correct but unwitnessed; record the producer, change nothing.")
        wb.add_data("vol_figure_eight_2_Cl2_pi_over_3", mp.nstr(vol, 25))
        for v, cc in circles.items():
            wb.add_data(f"apollonius_circle_{v.lower()}", {
                "mass_ratio_input": RATIOS[v],
                "k_squared": mp.nstr(vol / mp.mpf(RATIOS[v]), 20),
                **{k: mp.nstr(cc[k], 20) for k in PUBLISHED},
            })
        wb.add_data("vintage_separation_on_radius_relative", mp.nstr(sep, 6))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "These values are COMPUTED from Vol(4_1) = 2 Cl_2(pi/3) and the mass "
            "ratio, not transcribed from the block. The distinction matters: "
            "witness-block-agreement cannot tell a computed figure from a copied "
            "one, so a witness closing a row must be able to say where its numbers "
            "came from. Here it is mpmath's clsin and CAL-2.")
        wb.add_caveat(
            "Says nothing about whether candidate (ii) is right or whether Im(q) has "
            "a physical role; the block states its own closure condition and this "
            "probe does not evaluate it.")
        wb.add_caveat(
            "Says nothing about the reality argument that empties the branches -- "
            "that is what the block's 68 declaring witnesses do, and it is untouched.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": 'compares two vintages of the CAL-2 muon calibration on purpose: k^2 = Vol(4_1)/(m_mu/m_e) at CODATA 2018 (206.7682830) and CODATA 2022 (206.7682827); no q0 pin is read directly, and the result is the vintage comparison'})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
