#!/usr/bin/env python3
"""The two-anchor filter on `K(delta)` — and a self-consistency test that does
not depend on any candidate.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_d_n1_constant_bar_silence_probe.py      (entry 12)
# Ref: computations/qbeta/qbeta_ladder_alpha_form_filter_probe.py       (the z filter)
# Ref: computations/qbeta/qbeta_ladder_required_phase_probe.py          (the anchors)

WHAT THIS IS. Entry 10c derived the N=1 factor's general form from three
conditions and left one freedom, the multiplicative constant `K(delta)`, subject
only to `K(0) = 1`:

    F(a, delta) = cos(a - delta/2) * K(delta)

Entry 12 showed bar-parity is VACUOUS on `K` (`delta = h^2/2` is bar-invariant),
entry 14 withdrew the bar-midpoint rule that had selected `K = cos(delta/2)`, and
entry 15 showed neither block resolution nor Kohno-Drinfeld conjugation reaches
it. `K` is a free function and entry 12 called it the arc's largest single L2
blocker. This applies the two-anchor filter -- the technique the z-form filter
already uses -- to `K` instead of to `z`.

THE PRECONDITION, ASSERTED NOT ASSUMED. Both anchors must carry the SAME
`Q_codata_MeV`, or the "slope" is a confound between two experimental values
rather than a q-derivative. Checked below.

THE TWO ROWS. Requiring the ladder to reproduce Q_beta gives, at each anchor,

    K_required = Q_codata / ( Q_A * (1 - u^2) * cos(alpha - delta/2) )

so a candidate `K` must match a VALUE and a SLOPE `dK/d(delta)`.

RESULT 1 -- NEITHER ADMITTED CANDIDATE REACHES THE VALUE, AND THAT REFRAMES
ENTRY 12. Entry 12 measured the gap BETWEEN the two candidates as 59694 ppb,
7656x the Q_beta 100x target, and called that residual the blocker. But the
residual AFTER choosing either one is far larger:

    |1 - K_required|            281380 ppb   ( 36088x target )   <- K == 1
    |cos(d/2) - K_required|     221686 ppb   ( 28425x target )   <- K = cos(d/2)
    gap between the candidates   59694 ppb   (  7656x target )

So the choice between them is NOT the blocker; the N=1 factor is ~2.8e-4 short
whichever is chosen. Entry 12's framing is not wrong about the gap -- it is
measuring the smaller of two quantities.

RESULT 2 -- THE SLOPE MISSES BY THREE ORDERS, WITH THE WRONG SIGN.

    required   dK/d(delta) = +6.2399501753   (D frame)
                             +6.2934180689   (C frame)
    K = cos(d/2)           = -0.0054631674     ratio -1142.19
    K == 1                 =  0

RESULT 3 -- A SELF-CONSISTENCY TEST NEEDING NO CANDIDATE, and the sharpest of
the three. `K(0) = 1` plus the required value fixes the MEAN slope of `K` over
`[0, delta_0]`; the filter fixes the LOCAL slope at `delta_0`:

    mean slope over [0, delta_0]   = -0.0128759899
    local slope at delta_0         = +6.2399501753
    ratio                          =  -484.62

Any `K` meeting `K(0) = 1`, the value and the slope must therefore have local
derivative ~485x its own mean slope, of opposite sign -- strongly non-monotonic
on the scale of `delta`, with nothing in the arc motivating it.

CONVENTION-INDEPENDENT, which is what makes this a statement about the FORM. C
and D require slopes agreeing to 0.85 % (6.2934 vs 6.2400). The obstruction is
not a convention artifact.

THE SLOPE IS RED-TEAMED, unlike the z filter's. That one was a 2-point secant
over dq = 1.29e-8 and carried an explicit caveat. This one is a central
difference that is STABLE TO 12 SIGNIFICANT FIGURES across twelve orders of
magnitude of step size (rel 1e-8 down to 1e-20), and the independent two-anchor
secant reproduces it to 8. It is a derivative, not an artifact.

SCOPE -- (a), and read the attribution carefully. `K_required` is computed
holding `alpha` at the value THE FORM gives (`alpha = (z-1)h/2` at z_D or z_C),
and this arc's standing position is that `alpha` is NOT derived. So a wrong
`alpha` is absorbed into `K_required`, and this does NOT show that `K` itself
must equal 0.99972. What it shows is that the PAIR (alpha, K) drawn from this
form cannot reproduce both anchors -- a form-level negative, consistent with and
sharper than the arc's existing conclusion that the form must change.

NOT CLAIMED: that no `K` exists (an oscillating one exists mathematically); any
`c_k`; any movement on L2, which stays at 1279 ppb. No fit: nothing is chosen to
match data, the required values are reported and the candidates are measured
against them.

NO FLOAT64: mpmath mpf throughout at 60 dps; `float` appears nowhere.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(60)

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
ANCHOR_WITNESS = HERE / "qbeta-ladder-required-phase.witness.json"
TARGET_PPB = mp.mpf("7.797")          # sigma_exp/100 = 779.7/100; AGENTS.md rounds to 7.8


def _parts(q):
    """h, u, Q_A — all convention-FREE (b and hbar_q are defined from q alone)."""
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    Q_A = ME * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    return h, u, Q_A


def _delta(q):
    h = q - 1 / q
    return h ** 2 / 2


def _z(q, frame):
    return q ** 3 / (q ** 2 + 1) if frame == "D" else mp.sqrt(q) / (q + 1)


def K_required(q, frame):
    h, u, Q_A = _parts(q)
    a = (_z(q, frame) - 1) * h / 2
    return QCOD / (Q_A * (1 - u ** 2) * mp.cos(a - _delta(q) / 2))


def main() -> int:
    w = WitnessBuilder("qbeta-n1-constant-two-anchor-filter", engine="mpmath")
    w.set_description(
        "Two-anchor filter on the N=1 factor's free constant K(delta): neither "
        "admitted candidate reaches the required VALUE (281380 / 221686 ppb, both "
        "far exceeding the 59694 ppb gap BETWEEN them), the required slope "
        "+6.2400 misses cos(delta/2)'s by -1142x, and K(0)=1 plus the value force "
        "a mean slope -485x the local one. Convention-independent."
    )
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    anchors = json.loads(ANCHOR_WITNESS.read_text())["data"]["anchors"]
    check("the_two_anchors_share_Q_codata_EXACTLY",
          anchors[0]["Q_codata_MeV"] == anchors[1]["Q_codata_MeV"],
          "(else the slope is a confound between two experimental values)")
    qp = mp.mpf(str(anchors[0]["q"]))
    qm = mp.mpf(str(anchors[1]["q"]))
    d0 = _delta(qp)

    # ---- the slope, red-teamed across twelve orders of step size ------------
    def local_slope(frame, rel):
        dq = qp * mp.mpf(rel)
        return ((K_required(qp + dq, frame) - K_required(qp - dq, frame))
                / (_delta(qp + dq) - _delta(qp - dq)))

    STEPS = ["1e-8", "1e-9", "1e-10", "1e-12", "1e-14", "1e-16", "1e-20"]
    stable = {}
    print("\n  dK/d(delta), central difference — stability across step size:")
    print(f"    {'rel step':>10}{'frame D':>22}{'frame C':>22}")
    sweeps = {"D": [], "C": []}
    for rel in STEPS:
        row = {f: local_slope(f, rel) for f in ("D", "C")}
        for f in ("D", "C"):
            sweeps[f].append(fmt(row[f]))
        print(f"    {rel:>10}{mp.nstr(row['D'], 12):>22}{mp.nstr(row['C'], 12):>22}")
    for f in ("D", "C"):
        stable[f] = local_slope(f, "1e-14")
        spread = max(abs(local_slope(f, r) - stable[f]) for r in STEPS)
        check(f"slope_is_STABLE_across_12_orders_of_step_size_frame_{f}",
              spread < mp.mpf("1e-9"),
              f"(max spread {mp.nstr(spread, 4)} — a derivative, not an artifact)")

    for f in ("D", "C"):
        sec = ((K_required(qm, f) - K_required(qp, f)) / (_delta(qm) - _delta(qp)))
        check(f"independent_two_anchor_secant_reproduces_it_frame_{f}",
              abs(sec - stable[f]) / abs(stable[f]) < mp.mpf("1e-7"),
              f"(secant {mp.nstr(sec, 12)})")

    check("the_two_conventions_require_the_SAME_slope_to_within_one_percent",
          abs(stable["C"] - stable["D"]) / abs(stable["D"]) < mp.mpf("0.01"),
          "(so the obstruction is a property of the FORM, not of the convention)")

    # ---- row 1: the value, and neither candidate reaches it -----------------
    KD = K_required(qp, "D")
    cand_one = mp.mpf(1)
    cand_cos = mp.cos(d0 / 2)
    miss_one = abs(cand_one - KD) * 10 ** 9
    miss_cos = abs(cand_cos - KD) * 10 ** 9
    gap = abs(cand_one - cand_cos) * 10 ** 9
    print(f"\n  K_required(delta_0), frame D = {mp.nstr(KD, 16)}")
    print(f"    K == 1        misses by {mp.nstr(miss_one, 8)} ppb "
          f"({mp.nstr(miss_one / TARGET_PPB, 6)}x target)")
    print(f"    K = cos(d/2)  misses by {mp.nstr(miss_cos, 8)} ppb "
          f"({mp.nstr(miss_cos / TARGET_PPB, 6)}x target)")
    print(f"    gap BETWEEN the two candidates {mp.nstr(gap, 8)} ppb "
          f"({mp.nstr(gap / TARGET_PPB, 6)}x target)  <- what entry 12 measured")
    check("BOTH_admitted_candidates_miss_the_required_value_by_MORE_than_the_gap_between_them",
          miss_one > gap and miss_cos > gap,
          "(so the choice between them is not the blocker — entry 12 measured "
          "the smaller of two quantities)")

    slope_cos = -mp.sin(d0 / 2) / 2
    check("the_required_slope_misses_cos_delta_over_2_by_three_orders_WITH_THE_WRONG_SIGN",
          stable["D"] * slope_cos < 0
          and abs(stable["D"] / slope_cos) > 1000,
          f"(ratio {mp.nstr(stable['D'] / slope_cos, 8)})")

    # ---- row 3: candidate-free self-consistency -----------------------------
    mean_slope = (KD - 1) / d0                       # forced by K(0) = 1
    ratio = stable["D"] / mean_slope
    print(f"\n  candidate-free consistency (frame D):")
    print(f"    K(0) = 1 and K(delta_0) force mean slope = {mp.nstr(mean_slope, 12)}")
    print(f"    the filter forces local slope          = {mp.nstr(stable['D'], 12)}")
    print(f"    ratio local/mean                       = {mp.nstr(ratio, 8)}")
    check("local_slope_is_hundreds_of_times_the_mean_slope_and_OPPOSITE_IN_SIGN",
          ratio < -100,
          "(any K with K(0)=1 meeting both rows is strongly non-monotonic on the "
          "scale of delta, with nothing in the arc motivating it)")

    w.add_data("precondition", {
        "anchors_share_Q_codata": True,
        "Q_codata_MeV": anchors[0]["Q_codata_MeV"],
        "why": "otherwise the slope is a confound between two experimental "
               "values rather than a q-derivative",
    })
    w.add_data("delta_0", fmt(d0))
    w.add_data("value_row", {
        "K_required_D": fmt(KD),
        "K_required_C": fmt(K_required(qp, "C")),
        "candidate_K_eq_1": {"value": "1", "miss_ppb": fmt(miss_one),
                             "x_target": fmt(miss_one / TARGET_PPB)},
        "candidate_K_eq_cos_half_delta": {"value": fmt(cand_cos),
                                          "miss_ppb": fmt(miss_cos),
                                          "x_target": fmt(miss_cos / TARGET_PPB)},
        "gap_between_candidates_ppb": fmt(gap),
        "gap_x_target": fmt(gap / TARGET_PPB),
        "note": "entry 12 measured the gap; the residual after choosing either "
                "candidate is larger than the gap.",
    })
    w.add_data("slope_row", {
        "required_D": fmt(stable["D"]), "required_C": fmt(stable["C"]),
        "candidate_K_eq_1": "0",
        "candidate_K_eq_cos_half_delta": fmt(slope_cos),
        "ratio_required_over_cos": fmt(stable["D"] / slope_cos),
        "convention_spread_rel": fmt(abs(stable["C"] - stable["D"]) / abs(stable["D"])),
        "step_size_sweep": {"rel_steps": STEPS, "D": sweeps["D"], "C": sweeps["C"]},
    })
    w.add_data("candidate_free_consistency", {
        "mean_slope_forced_by_K0_eq_1": fmt(mean_slope),
        "local_slope": fmt(stable["D"]),
        "ratio_local_over_mean": fmt(ratio),
    })
    w.add_data("q0_anchor", {
        "pin": "physical_proton",
        "second_anchor": "ideal_muon, used ONLY as the second point of the "
                         "q-derivative; both share Q_codata exactly, so no "
                         "experimental value is straddled",
        "registered_in": "computations/q0_anchor_manifest.json (physical_proton)",
    })
    w.add_data("scope", {
        "tier": "scope-(a)",
        "c_k_produced": False, "K_determined": False, "q_beta_ppb": 1279,
        "is_a_fit": False,
        "attribution_caveat": "alpha is held at the value THE FORM gives and is "
                              "not itself derived, so a wrong alpha is absorbed "
                              "into K_required. This is a form-level negative on "
                              "the PAIR (alpha, K), not a determination of K.",
    })

    passed = sum(ok)
    print(f"\n  {passed}/{len(ok)} checks passed")
    w.save()
    return 0 if passed == len(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
