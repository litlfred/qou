"""The measured crossing counts break the b3=0 locus, then miss on sign by 8.11x.

CONTEXT.  QOU.Mass.CountChannelCarrierLocus reduced qou-brng's open question to
one acceptance test: a carrier must break mu_t = 3*mu_p, where mu = (n+ + n-)/2
is the count multiplicity of QOU.Mass.BrunnianBindingChannel.countChannel.

QOU.MassTheory.CrossingCountAffine supplies the corpus's MEASURED crossing
counts, from level3_em_channel_parity_probe.py across 12 nuclei to A = 39:

    n+ = 5A - 1 + 2Z        n- = 5A - 1 - 2Z

so mu(A) = (n+ + n-)/2 = 5A - 1, charge-free. This is not a guess and not a fit
-- it is what the canonical atomic braids measure, and it is exactly the
multiplicity the count channel carries. So the acceptance test can be run with
ZERO freedom.

RESULT.  It passes the test and then fails on sign.

    mu(2) = 9,  mu(3) = 14,  3*mu(2) = 27      14 != 27  -> locus broken (good)
    b3/b2 = mu(3)/mu(2) - 3 = 14/9 - 3 = -13/9 = -1.4444
    measured                                   = +0.6411

THE GENERAL CONSTRAINT.  For any affine mu(A) = a*A + b the cumulant is exact,
b3 = mu(3) - 3*mu(2) = -(3a + 2b), so with b2 = 2a + b > 0

    b3 > 0  <=>  2b < -3a      i.e.   -2a < b < -1.5a

and the RATIO depends only on b/a, not on the slope. The measured model has
b/a = -0.2 where the window is (-2, -1.5) and the value reproducing the measured
b3/b2 is -1.6214 -- off by a factor 8.11.

So the gap is not in the FORM of the derived model (affine, and the affine family
does contain solutions) but in one ratio whose required value is now known.

NO FREE PARAMETERS: exact Fraction arithmetic throughout; the only inputs are
AME2020 and the measured (5, -1).
"""
import datetime
import json
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

AME = {"D": F("2.224566"), "3H": F("8.481798"), "3He": F("7.718043"),
       "4He": F("28.295673")}

# The MEASURED affine crossing-count model (QOU.MassTheory.CrossingCountAffine).
ALPHA, BETA = F(5), F(-1)


def mu(A, a=ALPHA, b=BETA):
    return a * A + b


def main():
    b2 = AME["D"]
    bbar3 = (AME["3H"] + AME["3He"]) / 2
    b3 = bbar3 - 3 * b2
    b4 = AME["4He"] - 6 * b2 - 4 * b3
    meas3, meas4 = b3 / b2, b4 / b2

    print("MEASURED crossing-count model (CrossingCountAffine, 12 nuclei to A=39)")
    print("  mu(A) = (n+ + n-)/2 = 5A - 1   [charge-free]\n")
    for A in (2, 3, 4):
        print(f"    mu({A}) = {mu(A)}")

    breaks = mu(3) != 3 * mu(2)
    print(f"\n  acceptance test  mu_t == 3*mu_p ?   {mu(3)} vs {3 * mu(2)}"
          f"   -> {'BREAKS the locus (passes)' if breaks else 'ON the locus'}")

    m3 = mu(3) / mu(2) - 3
    m4 = (mu(4) - 6 * mu(2) - 4 * (mu(3) - 3 * mu(2))) / mu(2)
    print(f"\n  model    b3/b2 = {m3} = {float(m3):+.6f}"
          f"     b4/b2 = {m4} = {float(m4):+.6f}")
    print(f"  measured b3/b2 = {float(meas3):+.6f}     b4/b2 = {float(meas4):+.6f}")
    print("  -> b3 has the WRONG SIGN\n")

    # The general affine constraint. b3 = -(3a + 2b); ratio depends only on b/a.
    r_model = BETA / ALPHA
    r_req = -(3 + 2 * meas3) / (meas3 + 2)
    lo, hi = F(-2), F(-3, 2)
    print("  general affine mu(A) = a*A + b:   b3 = -(3a + 2b),"
          "  b3/b2 = -(3 + 2r)/(2 + r),  r = b/a")
    print(f"    b3 > 0 window for r : ({lo}, {hi})")
    print(f"    measured model  r   : {r_model} = {float(r_model):+.6f}"
          f"   {'INSIDE' if lo < r_model < hi else 'OUTSIDE'}")
    print(f"    required        r   : {float(r_req):+.6f}")
    print(f"    off by a factor     : {float(r_req / r_model):.4f}")

    assertions = [
        {"name": "the measured model BREAKS the b3=0 locus (mu_t != 3*mu_p), so "
                 "it passes CountChannelCarrierLocus's acceptance test",
         "passed": bool(breaks)},
        {"name": "but its b3 has the WRONG SIGN against the measured b3/b2 > 0",
         "passed": bool(m3 < 0 < meas3)},
        {"name": "b3/b2 depends only on the intercept-to-slope ratio r = b/a "
                 "(checked by rescaling the slope with r held fixed)",
         "passed": bool(
             (mu(3, 10 * ALPHA, 10 * BETA) / mu(2, 10 * ALPHA, 10 * BETA) - 3)
             == m3)},
        {"name": "the measured r = -0.2 lies OUTSIDE the b3>0 window (-2, -1.5)",
         "passed": bool(not (lo < r_model < hi))},
        {"name": "the required r is inside that window, so the affine family is "
                 "not excluded -- only this intercept is",
         "passed": bool(lo < r_req < hi)},
    ]
    ok = all(a["passed"] for a in assertions)
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The corpus's MEASURED crossing-count model mu(A) = 5A - 1 "
            "(CrossingCountAffine, 12 nuclei to A=39) breaks the b3=0 pair-local "
            "locus that the Hopf/Borromean carriers sat on, so it passes "
            "CountChannelCarrierLocus's acceptance test -- and then gives "
            "b3/b2 = -13/9, the wrong sign against a measured +0.6411239316. For "
            "any affine mu the ratio depends only on r = intercept/slope; the "
            "b3>0 window is r in (-2, -1.5), the measured model has r = -0.2, and "
            "the required value is -1.6214. The gap is one ratio, off by 8.11x, "
            "not the functional form."),
        "q0_pin": "not applicable -- consumes no framework q-dependent quantity",
        "free_parameters": 0,
        "measured_model": {"alpha": str(ALPHA), "beta": str(BETA),
                           "mu_2": str(mu(2)), "mu_3": str(mu(3)),
                           "mu_4": str(mu(4)),
                           "source": "QOU.MassTheory.CrossingCountAffine, from "
                                     "level3_em_channel_parity_probe.py"},
        "model_b3_over_b2": str(m3),
        "model_b4_over_b2": str(m4),
        "measured_b3_over_b2": f"{float(meas3):.12f}",
        "measured_b4_over_b2": f"{float(meas4):.12f}",
        "intercept_ratio": {"model": str(r_model),
                            "required": f"{float(r_req):.12f}",
                            "b3_pos_window": f"({lo}, {hi})",
                            "off_by_factor": f"{float(r_req / r_model):.6f}"},
        "assertions": assertions,
        "scope": (
            "(a) on the conjunction {affine count multiplicity, the measured "
            "(5, -1)}. It excludes neither the count channel nor affine models "
            "in general -- the required r sits inside the window, so an affine "
            "carrier CAN work. What is measured is that the corpus's own "
            "crossing counts miss the required intercept ratio by 8.11x."),
        "caveats": [
            "b4 is NOT reproduced either (model 17/9 = 1.889 vs measured 4.155), "
            "and fixing r to match b3 does not free a second parameter to match "
            "b4 -- an affine mu has only one ratio. So matching b3 alone would "
            "leave b4 as an independent test, which is the honest way to use "
            "this: r is determined by b3, then b4 is a prediction.",
            "mu(A) = 5A - 1 is charge-free, so it cannot distinguish 3H from 3He. "
            "That is consistent with using the isospin-averaged Bbar(3) here, but "
            "it also means the model has nothing to say about the mirror "
            "splitting.",
            "The 12-nucleus fit behind (5, -1) is the sibling's measurement, not "
            "re-derived here. If those counts are revised the verdict moves, and "
            "this probe should be re-run rather than quoted.",
        ],
        "lean": ("QOU/Mass/AffineCountMultiplicityWindow.lean "
                 "(11 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/count-channel-carrier-locus.witness.json",
            "probes/pair-locality-shortfall.witness.json",
        ],
        "source": "AME2020; crossing counts from QOU.MassTheory.CrossingCountAffine",
    }
    out = _HERE / "affine-count-intercept-window.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
