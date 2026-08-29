#!/usr/bin/env python3
"""m_tau volume-target quantification — census-reach re-scope (EXPLORATORY).

Sharpens the scope of ``rem:m-tau-knot-prediction`` ("Refuted: a direct
search evaluated 25 hyperbolic knots; none within 1% of 3477.23"). That
refutation is scope-(a): *this construction, over the searched census*.
This probe quantifies exactly WHAT the identity
``m_tau/m_e = Vol(K_tau)/hbar_q^k`` demands at the canonical q0, so the
searched region and the unsearched region are on the record:

  * k = 2 (the CAL-2 muon exponent) demands Vol ~ 34.1 — far beyond any
    25-knot low-crossing census (the largest hyperbolic volumes below 9
    crossings are < 13; volume ~34 requires roughly >= 15-17 crossings
    or a multi-component link/composite). The k = 2 identity was
    therefore never actually tested — the census could not reach it.
  * k = 3 demands Vol ~ 3.39 — squarely inside the low-crossing census
    (between 6_1 at 3.163 and 6_2 at 4.401), so the refutation is REAL
    for k = 3 over the census.
  * k = 1 demands Vol ~ 344 — no knot census reaches this; structurally
    out of range for any prime knot of tabulated size.

No candidate knot is proposed; no fit is performed. The output is the
exact target table plus reach verdicts, for the block re-scope (bean
qou-ejxn).
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP, HBAR_Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf  # noqa: E402

# CODATA m_tau/m_e as cited by rem:m-tau-knot-prediction (3477.23).

# Constants below are built at module scope. set_compute_dps() must run
# FIRST: at import time mp.dps is still mpmath's default 15 (~binary64),
# and a literal rounded there cannot be recovered by raising dps later.
set_compute_dps()
M_TAU_OVER_M_E = mpf("3477.23")

# Census-reach reference points (Rolfsen/SnapPea standard values, quoted
# to 6 dp for orientation only — the verdicts depend on order of
# magnitude, not on these digits).
CENSUS_LANDMARKS = {
    "4_1": 2.029883,
    "5_2": 2.828122,
    "6_1": 3.163963,
    "6_2": 4.400833,
    "7_2": 3.331744,
    "8_15 (max 8-crossing)": 9.93065,
    "9_x max (approx)": 12.5,
    "16-crossing max (approx)": 25.0,
    "weaving W(5,4) (approx)": 30.0,
}


def main() -> None:
    set_compute_dps()
    hbar = HBAR_Q_MP
    targets = {k: M_TAU_OVER_M_E * hbar**k for k in (1, 2, 3)}

    verdicts = {
        1: "unreachable by any tabulated prime knot (target ~344)",
        2: ("beyond the 25-knot low-crossing census: needs Vol ~ 34, "
            "i.e. roughly >= 15-17 crossings or a link/composite — "
            "the k=2 identity was never actually tested"),
        3: ("inside the low-crossing census (between 6_1 = 3.164 and "
            "6_2 = 4.401): the census refutation is REAL for k = 3"),
    }

    wb = WitnessBuilder("m-tau-volume-target", engine="mpmath")
    wb.set_description(
        "EXPLORATORY census-reach quantification for obs:m-tau-knot-"
        "prediction (bean qou-ejxn): exact targets Vol = (m_tau/m_e) * "
        "hbar_q^k at canonical q0 for k = 1,2,3, with reach verdicts. "
        "Re-scopes the block's 'Refuted' to scope-(a): real for k=3 "
        "over the census, untested for k=2 (target beyond census "
        "reach), unreachable for k=1. No candidate proposed, no fit.")
    wb.add_data("inputs", {
        "m_tau_over_m_e": str(M_TAU_OVER_M_E),
        "q0": mp.nstr(Q_MP, 20),
        "hbar_q": mp.nstr(hbar, 20),
    })
    wb.add_data("targets", {
        f"k={k}": mp.nstr(v, 20) for k, v in targets.items()
    })
    wb.add_data("verdicts", verdicts)
    wb.add_data("census_landmarks_vol", CENSUS_LANDMARKS)
    wb.set_audit_only("docs/audits/2026-08-01-tau-knot-discussion-review.md")
    wb.add_assertion(
        name="k2_target_value",
        computed=targets[2], expected=34.14, tolerance=0.05,
        unit="hyperbolic volume",
        source="(m_tau/m_e)*hbar_q^2 at canonical q0.")
    wb.add_assertion(
        name="k2_exceeds_9crossing_census_max",
        computed=int(targets[2] > mpf(str(CENSUS_LANDMARKS["9_x max (approx)"]))),
        expected=1, tolerance=0, unit="bool",
        source=("Reach check: the k=2 target exceeds the ~12.5 maximum "
                "hyperbolic volume among knots of <= 9 crossings, so a "
                "25-knot low-crossing census cannot contain it."))
    wb.add_assertion(
        name="k3_target_value",
        computed=targets[3], expected=3.383, tolerance=0.005,
        unit="hyperbolic volume",
        source="(m_tau/m_e)*hbar_q^3 at canonical q0.")
    wb.add_assertion(
        name="k3_within_census_window",
        computed=int(mpf(str(CENSUS_LANDMARKS["6_1"])) < targets[3]
                     < mpf(str(CENSUS_LANDMARKS["6_2"]))),
        expected=1, tolerance=0, unit="bool",
        source=("Reach check: the k=3 target lies strictly between "
                "Vol(6_1) and Vol(6_2), inside the searched census — "
                "that refutation is real."))
    out = wb.save()

    for k in (1, 2, 3):
        print(f"k={k}: Vol target = {mp.nstr(targets[k], 12)}  — {verdicts[k]}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
