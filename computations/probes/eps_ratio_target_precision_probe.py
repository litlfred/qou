#!/usr/bin/env python3
"""eps_ratio_target_precision_probe.py

The eps(2)/eps(1) target is 1.21 +- 0.06, NOT 1.2137076.

WHY THIS EXISTS
---------------
PR #6173 closed the negative half of qou-edt7 and reduced the open question to a
single number: eps(2)/eps(1) = 1.2137076, the factor by which the mean binding
per nucleon pair rises from coordination 1 to coordination 2. That figure was
quoted to eight significant digits because AME2020 knows the binding energies to
that precision.

**That was my error, and it matters for what counts as a derivation.** The AME
uncertainty is not the uncertainty on this quantity. eps(2) requires a
CHARGE-SYMMETRIC A=3 binding, and there is no such measurement -- there are two
mirror nuclei, 3H (pnn) and 3He (ppn), split by 0.76375488 MeV, which is almost
entirely the Coulomb energy of 3He's pp pair. Which of them (or which combination)
represents "the" A=3 nuclear binding is a CONVENTION, and the conventions differ
by 9.4%:

    3He alone                 ratio = 1.1564864
    isospin average           ratio = 1.2137076   <- what #6173 quoted
    3H alone / Coulomb-corr   ratio = 1.2709289

The corpus's own Tjon block already uses the Coulomb-corrected convention for the
alpha (B = 29.0 +- 0.1 against AME's 28.2956624), so the two legs of the ladder
were not even being read in the same convention.

CONSEQUENCES, and they cut both ways
------------------------------------
1. A derivation only has to land within a few percent. Several structurally
   motivated quantities already do: 2*z_D = 1.2254 (0.96% from the isospin
   average), 6/5 = 1.2 (1.1%), q0^2 = 1.2321 (1.5%). Under #6173's framing these
   read as failures; they are inside the systematic.
2. **Therefore a near-match at this level is nearly worthless as evidence.** With
   a ~9% band and an unbounded supply of candidate expressions, hitting it is
   expected, not informative. Discrimination has to come from somewhere else --
   e.g. from a candidate that ALSO predicts eps(3)/eps(2), which none of the
   above does (measured 1.7467 iso-avg / 1.6680 3H-based; 2*z_D and 6/5 are
   nowhere near either).
3. The entropy argument makes this precise. An expression family with k small
   integer parameters of height H supplies ~(2H)^k candidates; matching a target
   known to d digits is evidence only when (2H)^k << 10^d. Here d ~ 1-2 after the
   systematic, so essentially NO closed-form guess can be evidence. The
   algebraic-guess route is entropically dead at the available precision.

This probe records the band, not a result. It derives nothing.

Bean qou-edt7.
"""
from __future__ import annotations

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q_MP  # noqa: E402  (exact mpf; NEVER mpf(str(Q)) -- Q is f64)
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def main() -> int:
    wb = WitnessBuilder("eps-ratio-target-precision", engine="mpmath")
    wb.set_description(
        "The eps(2)/eps(1) target of qou-edt7 carries a 9.4% CONVENTION "
        "systematic from the 3H/3He mirror splitting, so it is 1.21 +- 0.06, not "
        "the 8-digit 1.2137076 quoted in PR #6173. Corrects that framing. Cuts "
        "both ways: candidates previously read as failures are inside the band, "
        "and a near-match in the band is therefore not evidence."
    )

    D = ame_binding_mev(1, 2)
    T3, He3 = ame_binding_mev(1, 3), ame_binding_mev(2, 3)
    He4 = ame_binding_mev(2, 4)
    split = T3 - He3

    conv = {"3He_alone": He3, "isospin_average": (T3 + He3) / 2, "3H_alone": T3}
    ratios = {k: (v / 3) / D for k, v in conv.items()}
    lo, hi = min(ratios.values()), max(ratios.values())
    mid = ratios["isospin_average"]
    width = (hi - lo) / mid

    print(f"mirror splitting B(3H) - B(3He) = {mp.nstr(split, 9)} MeV (mostly Coulomb)\n")
    for k in ("3He_alone", "isospin_average", "3H_alone"):
        print(f"   {k:<18} eps(2)/eps(1) = {mp.nstr(ratios[k], 9)}")
    print(f"\n   band {mp.nstr(lo,7)} .. {mp.nstr(hi,7)}   width {mp.nstr(width*100,4)}%")

    wb.add_data("convention_band", {k: fmt(v) for k, v in ratios.items()})
    wb.add_assertion(
        name="target_carries_a_convention_systematic",
        computed=fmt(width), expected="0.09429", tolerance="1e-4",
        unit="fractional width of the convention band",
        source=("3H/3He mirror splitting 0.76375488 MeV; no charge-symmetric A=3 "
                "binding is measured, so the choice is a convention"),
    )

    # candidates that #6173 read as failures and that are in fact inside the band
    q = +Q_MP
    inband = {"2*z_D": 2 * q**3 / (q**2 + 1), "6/5": mp.mpf(6) / 5, "q0^2": q**2}
    print("\ncandidates INSIDE the band (so: not refuted -- and not evidence either):")
    rows = []
    for k, v in inband.items():
        dev = abs(v - mid) / mid
        rows.append({"candidate": k, "value": fmt(v), "dev_from_isoavg": fmt(dev)})
        print(f"   {k:<8} = {mp.nstr(v,10):>14}   {mp.nstr(dev*100,4)}% from the iso-average")
    wb.add_data("in_band_candidates", rows)

    # the discriminator none of them survives
    e2 = {k: v / 3 for k, v in conv.items()}
    print("\nthe discriminator -- eps(3)/eps(2), which none of them predicts:")
    for k in ("isospin_average", "3H_alone"):
        print(f"   {k:<18} = {mp.nstr((He4/6)/e2[k], 9)}")
    wb.add_data("second_ratio_discriminator", {
        "iso_average": fmt((He4 / 6) / e2["isospin_average"]),
        "3H_based": fmt((He4 / 6) / e2["3H_alone"]),
        "note": "2*z_D = 1.2254 and 6/5 = 1.2 are nowhere near either; a candidate "
                "that fits the first ratio and not the second has fitted one number",
    })

    wb.add_data("scope", {
        "derives_anything": False,
        "what_it_corrects": "PR #6173 quoted the target to 8 digits; the physical "
                            "quantity is defined only to ~1-2 digits",
        "consequence": "closed-form guessing cannot be evidence at this precision; "
                       "a mechanism must predict the SECOND ratio too",
    })
    wb.save()
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
