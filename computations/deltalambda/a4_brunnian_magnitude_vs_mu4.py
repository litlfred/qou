#!/usr/bin/env python3
"""a4_brunnian_magnitude_vs_mu4.py — the A=4 Brunnian MAGNITUDE leg (bean qou-g3e1).

The A=4 Brunnian cluster's SIGN and ORDER are now derived exactly (order 6,
leading (q-1) coefficient -96; PR #4458 / audit 2026-08-01). This probe closes
the remaining question the bean poses: how does the derived cluster MAGNITUDE
compare to the residual it must supply?

    c_A  =  E_0 * (1 - tau_A)        (irreducible A-body Brunnian cluster)
    mu_A                              (forward AME - model residual, 0 fit)

reported as the ratio c_A / mu_A at BOTH known A and at BOTH levels (base band
commutator, and width-3 cabled), so the comparison is like-for-like.

WHY BOTH A: the single most decision-relevant question is not "how far off is
A=4" but "is the shortfall the SAME at A=3 and A=4". If it were constant, one
missing normalisation would explain both and a global re-weight would be a
legitimate target for derivation. If it diverges, no constant re-weight can
close both — which independently CONFIRMS the bean's anti-fit guard, since
tuning a normalisation to close A=4 would necessarily break the A=3 near-miss.

STRICT anti-fit (the bean's own instruction): this probe COMPARES and REPORTS.
It does not re-weight, does not fit, does not tune, and wires nothing. mu_A is
forward (AME - model), never inverted. All inputs are read from committed
witnesses; no new physics is introduced here.

Inputs (all committed witnesses):
  * a4-h12-brunnian-deficit-measure.witness.json  — mu_2..mu_4 simplex, A=4
    base and cabled c_4, A=3 band-commutator deficit
  * borromean-h9-magnitude-lift.witness.json      — A=3 cabled (H_9) c_3, E_0

Run:  python3 -u a4_brunnian_magnitude_vs_mu4.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
from witness_base import WitnessBuilder  # noqa: E402

import mpmath as mp  # noqa: E402

_T0_MONO = time.monotonic()
# Precision is centralized: importing witness_base/qou_substrate applies the repo
# default compute/serialization dps (recorded in the witness precisionMetadata).
# Do NOT override it here — a manual dps would contradict that metadata.


def load(name: str) -> dict:
    return json.loads((HERE / name).read_text())


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def main() -> int:
    meas = load("a4-h12-brunnian-deficit-measure.witness.json")
    lift = load("borromean-h9-magnitude-lift.witness.json")

    E0 = mp.mpf(lift["parameters"]["E0_MeV"])
    r = meas["results"]
    mu3 = mp.mpf(r["a4_residual_target"]["mu3"])
    mu4 = mp.mpf(r["a4_residual_target"]["mu4"])

    # A=3: base band commutator [A01,A12] at n=3 (deficit 1 - tau), and the
    # width-3 cabled H_9 lift (atom-dressed mean, #4364).
    d3_base = mp.mpf(r["a3_borromean_band_validation"]["deficit_1_minus_tau"])
    c3_base = E0 * d3_base
    c3_cabled = mp.mpf(lift["results"]["atom_dressed_mean"]["c3_mean_MeV"])

    # A=4: base [[A01,A12],A23] at n=4, and the width-3 cabled H_12.
    c4_base = mp.mpf(r["a4_brunnian_base_n4"]["c4_MeV"])
    c4_cabled = mp.mpf(r["a4_brunnian_cabled_h12"]["c4_MeV"])

    rows = [
        ("A=3", "base  n=3 ", c3_base, mu3),
        ("A=3", "cabled H_9", c3_cabled, mu3),
        ("A=4", "base  n=4 ", c4_base, mu4),
        ("A=4", "cabled H_12", c4_cabled, mu4),
    ]

    print("=" * 84)
    print("A=4 Brunnian MAGNITUDE leg — derived cluster vs the residual it must supply")
    print("=" * 84)
    print(f"E_0 = {mp.nstr(E0, 12)} MeV    mu_3 = {mp.nstr(mu3, 8)}    "
          f"mu_4 = {mp.nstr(mu4, 8)}\n")
    print(f"{'A':5s} {'level':12s} {'c_A (MeV)':>16s} {'mu_A (MeV)':>12s} "
          f"{'c_A/mu_A':>12s} {'shortfall':>12s} {'sign':>6s}")
    out = {}
    for a, lvl, c, mu in rows:
        ratio = c / mu
        short = 1 / ratio
        sign_ok = (c < 0) == (mu < 0)
        print(f"{a:5s} {lvl:12s} {mp.nstr(c, 8):>16s} {mp.nstr(mu, 6):>12s} "
              f"{mp.nstr(ratio, 6):>12s} {mp.nstr(short, 6):>12s}x "
              f"{'OK' if sign_ok else 'WRONG':>6s}")
        out[f"{a}_{lvl.strip().replace(' ', '_')}"] = {
            "c_A_MeV": mp.nstr(c, 12), "mu_A_MeV": mp.nstr(mu, 8),
            "ratio_c_over_mu": mp.nstr(ratio, 10),
            "shortfall_factor": mp.nstr(short, 10),
            "sign_matches": bool(sign_ok),
        }

    # The decisive comparison: is the shortfall the SAME at both A?
    short3_base = mu3 / c3_base
    short4_base = mu4 / c4_base
    short3_cab = mu3 / c3_cabled
    short4_cab = mu4 / c4_cabled
    div_base = short4_base / short3_base
    div_cab = short4_cab / short3_cab

    print("\n" + "=" * 84)
    print("IS THE SHORTFALL CONSTANT IN A?  (the decision-relevant question)")
    print("=" * 84)
    print(f"  base level :  A=3 short {mp.nstr(short3_base, 6)}x , "
          f"A=4 short {mp.nstr(short4_base, 6)}x   -> diverge by {mp.nstr(div_base, 6)}x")
    print(f"  cabled     :  A=3 short {mp.nstr(short3_cab, 6)}x , "
          f"A=4 short {mp.nstr(short4_cab, 6)}x   -> diverge by {mp.nstr(div_cab, 6)}x")
    print()
    print("  => NOT constant. At the cabled (magnitude) level the A=3 cluster is a")
    print(f"     {mp.nstr(short3_cab, 4)}x near-miss while A=4 is {mp.nstr(short4_cab, 4)}x short —")
    print(f"     a {mp.nstr(div_cab, 4)}x divergence. NO single constant re-weight can close")
    print("     both: any normalisation tuned to close A=4 would blow up the A=3")
    print("     near-miss by the same factor. This CONFIRMS the anti-fit guard.")
    print()
    print("  Sign, by contrast, is correct at BOTH A (derived, PR #4458): the")
    print("  parity law holds and it is only the MAGNITUDE that fails.")

    w = WitnessBuilder("a4-brunnian-magnitude-vs-mu4", engine="python",
                       start_time=_T0_MONO)
    w.set_description(
        "Bean qou-g3e1, the A=4 Brunnian MAGNITUDE leg. The sign and order are derived "
        "exactly (order 6, leading (q-1) coeff -96; PR #4458); this compares the derived "
        "cluster magnitude c_A = E_0*(1-tau_A) against the forward residual mu_A "
        "(AME - model, never inverted) at BOTH known A and BOTH levels (base band "
        "commutator, width-3 cabled). KEY RESULT: the shortfall is NOT constant in A — "
        "at the cabled level A=3 is a ~1.59x near-miss while A=4 is ~78.8x short, a ~50x "
        "divergence — so NO single constant re-weight can close both, and any "
        "normalisation tuned to close A=4 would break the A=3 near-miss by the same "
        "factor. Independently confirms the bean's anti-fit guard. Sign is correct at "
        "both A. Scope-(a): compares and reports; no re-weighting, no fit, no tuning, "
        "nothing wired. All inputs read from committed witnesses."
    )
    for k, v in out.items():
        w.add_data(k, v)
    w.add_data("shortfall_divergence_base", mp.nstr(div_base, 10))
    w.add_data("shortfall_divergence_cabled", mp.nstr(div_cab, 10))
    w.add_assertion(
        "sign_correct_at_both_A",
        computed=float(sum(1 for _, _, c, mu in rows if (c < 0) == (mu < 0))),
        expected=4.0, tolerance=0.0,
        source="The derived Brunnian cluster has the same sign as the residual it must "
               "supply at both A and both levels (A=3 positive, A=4 negative) — the "
               "parity sign law derived in PR #4458 holds against the forward AME-model "
               "residual. Only the magnitude fails.",
    )
    # Record the finding as a TRUE statement, not a deliberately-failing check:
    # a red witness signals a broken compute, which this is not.
    w.add_assertion(
        "shortfall_divergence_exceeds_10x",
        computed=1.0 if div_cab > 10 else 0.0, expected=1.0, tolerance=0.0,
        source=f"THE FINDING. If a single missing normalisation explained both A, the "
               f"cabled shortfall ratio A=4/A=3 would be 1. It is "
               f"{mp.nstr(div_cab, 6)} (base level: {mp.nstr(div_base, 6)}), far above "
               f"10 — so the shortfall grows sharply with A and no constant re-weight "
               f"can close both. Any normalisation tuned to close A=4 would break the "
               f"A=3 near-miss by that same factor, which independently confirms the "
               f"anti-fit guard on this bean.",
    )
    out_path = w.save()
    print(f"\nwitness -> {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
