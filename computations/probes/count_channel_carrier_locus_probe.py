#!/usr/bin/env python3
"""The canonical carriers sit exactly on the count channel's b3 = 0 locus.

CONTEXT.  QOU.Mass.BrunnianBindingChannel is qou-brng's surviving route: for a
Brunnian pair the signed (linking) channel vanishes and the whole mutual energy
is the UNSIGNED count channel

    countChannel(n+, n-, q) = ((n+ + n-)/2) * (q - 1/q),

strictly positive at q > 1 (brunnian_binding_survives). That answers the
linking-number objection -- binding survives where lk = 0. It does not answer
the cumulant objection, and this probe measures the gap.

WHAT IS MEASURED.  Write mu = (n+ + n-)/2 for a carrier's count multiplicity, so
its binding is s*mu*h with h = q - 1/q and s the MeV scale. Then

    b3 = s*h*(mu_triple - 3*mu_pair)

which vanishes iff mu_triple = 3*mu_pair -- the pair-local condition, so
QOU.Mass.CrossingModelPairLocality.b3_eq_zero_of_pairLocal applies. The canonical
carriers satisfy it EXACTLY:

    deuteron  Hopf clasp   n+=2, n-=0  ->  mu = 1
    A=3       L6a4 Borrom. n+=3, n-=3  ->  mu = 3        and 3 = 3 * 1.

THE SCALE CANCELS, so this is zero-parameter: b3/b2 = mu_triple/mu_pair - 3, and
no choice of s or q rescues it.

A NEGATIVE THAT IS *NOT* AVAILABLE, recorded so it is not re-attempted.  The
tempting argument is that mu is a half-integer while the measured ratio
mu_triple/mu_pair = 3.6411239316 is not, so no carrier could work. That is WRONG:
it assumes mu_pair = 1. With mu_pair free, small half-integers get close --
(7, 51/2) lands b3/b2 within 0.27%. So the channel is NOT obstructed; the failure
is the carrier assignment. That makes the burden sharper, not lighter: two free
crossing integers against one measured ratio is a FIT.

NO FREE PARAMETERS in the verdict: every reported miss is a ratio in which s and h
cancel. The exploratory table at the end IS a fit and is labelled as one.

PRECISION.  Exact rational arithmetic for the ratios (Fraction); mpmath only for
the substrate factor h, which cancels from every verdict.
"""
import datetime
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

set_compute_dps()

AME = {"D": F(_ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)), "3H": F(_ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)), "3He": F(_ame_nstr(AME_B_HE3_MEV_VALIDATION, 30))}

# Canonical carrier crossing data (n_plus, n_minus) for the INTER-component
# crossings, per QOU.Mass.BrunnianBindingChannel and the 2026-08-29 owner ruling
# (deuteron = clasp, Vol = 0).
CARRIERS = {"deuteron (Hopf clasp)": (2, 0), "A=3 (L6a4 Borromean)": (3, 3)}


def mult(np_, nn_):
    """Count multiplicity (n+ + n-)/2 -- a half-integer."""
    return F(np_ + nn_, 2)


def main():
    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q

    b2 = AME["D"]
    bbar3 = (AME["3H"] + AME["3He"]) / 2
    b3 = bbar3 - 3 * b2
    measured_ratio = b3 / b2

    print("count channel = mu * h,   mu = (n+ + n-)/2,   h = q - 1/q\n")
    print(f"  h at q0 = {mp.nstr(h, 12)}   (cancels from every verdict below)\n")

    rows = []
    for name, (npv, nnv) in CARRIERS.items():
        m = mult(npv, nnv)
        rows.append({"carrier": name, "n_plus": npv, "n_minus": nnv,
                     "count_multiplicity": str(m)})
        print(f"  {name:<24} n+={npv} n-={nnv}   mu = {m}")

    mu_p = mult(*CARRIERS["deuteron (Hopf clasp)"])
    mu_t = mult(*CARRIERS["A=3 (L6a4 Borromean)"])
    model_ratio = mu_t / mu_p - 3

    print(f"\n  mu_triple / mu_pair = {mu_t}/{mu_p} = {mu_t / mu_p}"
          f"   -> exactly 3, the pair-local locus")
    print(f"  model  b3/b2 = mu_t/mu_p - 3 = {model_ratio}")
    print(f"  MEASURED b3/b2               = {float(measured_ratio):.10f}")
    print(f"  => the model supplies NONE of the measured b3 (miss = 100%)")

    # Exact-match counts: an artifact of the quoted AME digits, shown to be dismissed.
    need = bbar3 / b2
    print(f"\n  required mu_triple/mu_pair = {need} = {float(need):.10f}")
    print(f"  exact-match crossing counts n(pair)={need.denominator},"
          f" n(triple)={need.numerator} -- ABSURD, and an artifact of the")
    print("  quoted AME digits, so it proves nothing. The real question is how")
    print("  close SMALL carriers get:\n")

    # EXPLORATORY (a fit): how close can small half-integer multiplicities get?
    cands = []
    for twop in range(1, 25):
        mp_ = F(twop, 2)
        ideal = mp_ * need
        for twot in {math.floor(2 * ideal), math.ceil(2 * ideal)}:
            if twot < 1:
                continue
            mt_ = F(twot, 2)
            pred = mt_ / mp_ - 3
            if pred <= 0:
                continue
            rel = abs(pred - measured_ratio) / measured_ratio
            cands.append((rel, twop, twot, mp_, mt_, pred))
    cands.sort()
    print(f"  {'n(pair)':>8} {'n(triple)':>10} {'b3/b2':>10} {'rel err':>10}"
          "   [EXPLORATORY -- this is a FIT, 2 integers vs 1 ratio]")
    fits = []
    for rel, twop, twot, mp_, mt_, pred in cands[:5]:
        fits.append({"n_pair": twop, "n_triple": twot,
                     "mu_pair": str(mp_), "mu_triple": str(mt_),
                     "b3_over_b2": f"{float(pred):.8f}",
                     "rel_err": f"{float(rel):.6f}"})
        print(f"  {twop:>8} {twot:>10} {float(pred):>10.6f} {float(rel)*100:>9.3f}%")

    best_rel = cands[0][0] if cands else None

    # READING (b): the FULL mutual energy. The deuteron is a Hopf clasp with
    # lk = +-1 -- NOT Brunnian -- so its signed channel is live and
    # brunnian_energy_is_count_channel does not apply to it. Using the count
    # channel for it (reading (a) above) is already a stretch; this is the
    # honest alternative, and it is worse.
    def full(np_, nn_):
        return np_ * q - nn_ / q

    full_pair = full(2, 0)
    full_triple = full(3, 3)
    full_ratio = full_triple / full_pair - 3
    closed = -3 * (q + 1 / q) / (2 * q)
    closed_agrees = abs(full_ratio - closed) < mpf(10) ** (-(mp.dps - 10))

    print("\n  READING (b) -- FULL mutual energy (the deuteron is NOT Brunnian,")
    print("                 so dropping its signed channel is unjustified):")
    print(f"    Hopf  (2,0) -> {mp.nstr(full_pair, 10)}"
          f"    L6a4 (3,3) -> {mp.nstr(full_triple, 10)}")
    print(f"    b3/b2 = {mp.nstr(full_ratio, 10)} = -3(q+1/q)/(2q)"
          f"   closed form agrees: {closed_agrees}")
    print(f"    WRONG SIGN, and negative for EVERY q > 0 "
          f"(QOU.Mass.CountChannelCarrierLocus.fullEnergy_b3_neg)")
    print(f"\n  So the two readings BRACKET the measurement from below:")
    print(f"    (a) count-only  =  0")
    print(f"    (b) full energy = {mp.nstr(full_ratio, 10)}")
    print(f"    measured        = +{float(measured_ratio):.10f}")

    assertions = [
        {"name": "the canonical carriers land EXACTLY on the pair-local locus "
                 "(mu_triple = 3 * mu_pair)",
         "passed": bool(mu_t == 3 * mu_p)},
        {"name": "so the count channel predicts b3 = 0 on those carriers",
         "passed": bool(model_ratio == 0)},
        {"name": "the measured b3/b2 is strictly positive, so the miss is total",
         "passed": bool(measured_ratio > 0)},
        {"name": "the scale cancels: the verdict uses only multiplicities, no s "
                 "and no h",
         "passed": bool(model_ratio == mu_t / mu_p - 3)},
        {"name": "the half-integer quantisation argument does NOT obstruct the "
                 "channel -- some small carrier pair gets within 1%",
         "passed": bool(best_rel is not None and best_rel < F(1, 100))},
        {"name": "READING (b): the full-energy reading has the WRONG SIGN, and "
                 "its closed form -3(q+1/q)/(2q) is negative for every q > 0",
         "passed": bool(full_ratio < 0 and closed_agrees)},
        {"name": "the two readings BRACKET the measurement from below -- both "
                 "are <= 0 while the measured b3/b2 is positive, so the failure "
                 "is not a matter of picking the wrong channel",
         "passed": bool(full_ratio < 0 and model_ratio == 0
                        and measured_ratio > 0)},
    ]

    ok = all(a["passed"] for a in assertions)
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The count channel of QOU.Mass.BrunnianBindingChannel, evaluated on "
            "the framework's own carriers, predicts b3 = 0. The Borromean L6a4 "
            "count multiplicity (3) is exactly three times the Hopf clasp's (1), "
            "which is the pair-local condition, so b3 vanishes identically "
            "against a measured b3/b2 = 0.6411239316. The MeV scale and the "
            "substrate factor h both cancel, so no reparametrisation rescues it. "
            "The channel itself is NOT obstructed -- small half-integer "
            "multiplicities reach the measured ratio to 0.27% -- so the failure "
            "is the carrier assignment, and any carrier that reaches b3 does so "
            "as a fit unless its crossing numbers are derived."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "h_substrate_factor": mp.nstr(h, 20),
        "free_parameters": 0,
        "carriers": rows,
        "model_b3_over_b2_reading_a_count_only": str(model_ratio),
        "model_b3_over_b2_reading_b_full_energy": mp.nstr(full_ratio, 14),
        "reading_b_closed_form": "-3(q+1/q)/(2q), negative for every q>0",
        "measured_b3_over_b2": f"{float(measured_ratio):.12f}",
        "required_multiplicity_ratio": f"{float(need):.12f}",
        "exact_match_counts": {"n_pair": need.denominator,
                               "n_triple": need.numerator,
                               "note": "artifact of the quoted AME digits; "
                                       "not a physical statement"},
        "exploratory_small_carriers_THIS_IS_A_FIT": fits,
        "assertions": assertions,
        "scope": (
            "(a) on the conjunction {count channel, Hopf pair, Borromean triple}. "
            "It excludes NO ingredient: the count channel survives, "
            "brunnian_binding_survives is untouched, and the Brunnian mechanism "
            "remains the only thing that lets binding exist at lk = 0. What is "
            "excluded is that THESE TWO CARRIERS with THIS CHANNEL reproduce b3."),
        "caveats": [
            "The half-integer quantisation argument is NOT a valid obstruction "
            "and is recorded here so it is not re-attempted: it assumes "
            "mu_pair = 1, and with mu_pair free small carriers get within 0.27%.",
            "The exploratory table is a FIT -- two free crossing integers against "
            "one measured ratio. It is included to show the channel has room, not "
            "as a candidate. A carrier reaching b3 earns nothing unless its "
            "crossing numbers are derived.",
            "The crossing data (Hopf n+=2/n-=0, L6a4 n+=n-=3) is read from "
            "BrunnianBindingChannel's own sub-question-1 text and the 2026-08-29 "
            "owner ruling. If a different carrier is canonical, the verdict "
            "changes and this probe should be re-run rather than quoted.",
            "b2 is the deuteron and is NOT Brunnian (clasp, Vol = 0 per the owner "
            "ruling), so the two carriers are of different types. That is what "
            "makes the 3-to-1 coincidence a coincidence rather than a theorem.",
        ],
        "lean": ("QOU/Mass/CountChannelCarrierLocus.lean "
                 "(7 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/pair-locality-shortfall.witness.json",
            "probes/aggregator-convexity-divided-difference.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies; carrier crossing data "
                  "from QOU.Mass.BrunnianBindingChannel",
    }
    out = _HERE / "count-channel-carrier-locus.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    # P30: add the staleness provenance (scriptHash / commitSha /
    # engine) that a hand-rolled dump cannot get from build().
    # The q0Anchor lines just below own the anchor decision and run
    # after this, so their value stands.
    _WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python")
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    witness["q0Anchor"] = _q0a
    if _q0v:
        witness["q0Value"] = _q0v
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
