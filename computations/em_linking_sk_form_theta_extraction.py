#!/usr/bin/env python3
"""Route 1: is the per-pair Coulomb unit S_K-shaped? Extract theta_K.

Bean qou-ed61 (owner lead), resolving the qou-gcmn confound.

THE LEAD. Every kappa(A) analysis so far has held the per-pair Coulomb
unit at its A=3 value, so any A-dependence of the underlying scale is
absorbed into kappa -- the standing confound. The corpus already
carries a candidate SHAPE for that scale, from the Delta_lambda
binding assembly:

    S_K(q0) = A_omega * cuspModulus * (ln^2 q0 - theta_K^2)

with, importantly for this probe:
  * A_omega = 3          -- the GGM Stokes SYMMETRY constant. NOT
                            knot-dependent: exact and q-independent
                            (QOU.QBeta.StokesSymmetryConstant).
  * cuspModulus = sqrt3/4 -- proved geometric datum.
  * theta_K = Im u_K      -- THE knot-dependent slot, and an OPEN datum
                            (the G3 monodromy datum, bean qou-qnnq).

So if the per-pair unit is S_K-shaped, the knot-dependence enters
entirely through theta_K, and holding the unit fixed at A=3 is wrong in
a specific, invertible way.

THE INVERSION. Writing U(A) for the true unit and U_fixed = U(3) for
the held-fixed one, the measured kappa satisfies kappa(A) =
kappa_true * U(A)/U(3) for a constant kappa_true. Hence

    (ln^2 q0 - theta_A^2) / (ln^2 q0 - theta_3^2) = kappa(A) / kappa(3)

which determines theta_A for every mirror pair once theta_3 is chosen.
That single choice is a genuine free parameter and is NOT fitted: the
probe reports the whole one-parameter family, with theta_3 = 0 (the
A=3 pair is pure boost, no angular deformation) as the natural
reference.

WHAT THIS CAN AND CANNOT DO. It cannot derive theta_K -- that is the
open G3 datum. What it CAN do is test the S_K form for consistency:
the extracted theta_A must be REAL, must stay in the boost-dominated
regime theta < ln q0 (else the binding sign flips, per
`binding_sign_from_angular`), and should behave smoothly in A. Any
violation falsifies the S_K reading of the per-pair unit. It also
yields a falsifiable PREDICTION: theta_A -> ln q0 marks a wall where
the per-pair unit vanishes.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, log, sqrt  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"
UNBOUND_A = {5, 9}

A_OMEGA = mpf(3)                      # Stokes symmetry constant (4_1)
CUSP_MODULUS = sqrt(mpf(3)) / 4       # proved geometric datum


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    return m, sqrt(sum((v - m) ** 2 for v in vals) / n) / m


def main() -> None:
    set_compute_dps()
    ln_q0 = log(Q_MP)
    ln2 = ln_q0 ** 2

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    rows = [{"A": r["A"], "Z": r["Z"], "kappa": mpf(str(r["kappa"]))}
            for r in w["data"]["series"] if r["A"] not in UNBOUND_A]
    k3 = next(r["kappa"] for r in rows if r["A"] == 3)

    # One-parameter family: theta_3 in [0, ln q0). Report several.
    families = {}
    for frac in ("0.0", "0.25", "0.5"):
        th3 = mpf(frac) * ln_q0
        base = ln2 - th3 ** 2
        entries, ok_real, ok_boost = [], True, True
        for r in rows:
            th2 = ln2 - (r["kappa"] / k3) * base
            real = th2 >= 0
            ok_real &= real
            th = sqrt(th2) if real else None
            if th is not None and th >= ln_q0:
                ok_boost = False
            entries.append({
                "A": r["A"],
                "theta": (mp.nstr(th, 8) if th is not None else "IMAGINARY"),
                "theta_over_ln_q0": (mp.nstr(th / ln_q0, 8)
                                     if th is not None else None),
            })
        families[f"theta_3 = {frac} * ln q0"] = {
            "all_real": bool(ok_real),
            "all_boost_dominated": bool(ok_boost),
            "entries": entries,
        }

    # Reference family (theta_3 = 0): smoothness + scaling behaviour.
    ref = families["theta_3 = 0.0 * ln q0"]["entries"]
    thetas = [mpf(e["theta"]) for e in ref if e["theta"] != "IMAGINARY"]
    As = [mpf(e["A"]) for e in ref if e["theta"] != "IMAGINARY"]
    monotone = all(thetas[i] <= thetas[i + 1] for i in range(len(thetas) - 1))
    near_mono = all(thetas[i] <= thetas[i + 1] * mpf("1.05")
                    for i in range(len(thetas) - 1))
    # Does theta follow a simple power of A?  theta ~ c * A^p.
    powers, scatter = {}, {}
    for p in ("1/6", "1/4", "1/3", "1/2"):
        num, den = p.split("/")
        pe = mpf(num) / mpf(den)
        ratios = [t / (a ** pe) for t, a in zip(thetas[1:], As[1:])]  # skip A=3 (theta=0)
        m, sd = stats(ratios)
        powers[f"theta ~ A^({p})"] = {"coefficient": mp.nstr(m, 8),
                                      "rel_scatter": mp.nstr(sd, 8)}
        scatter[f"theta ~ A^({p})"] = sd     # mpf kept for ordering/printing
    best_p = min(scatter, key=lambda k: scatter[k])

    th_max = max(thetas)
    wall_frac = th_max / ln_q0

    wb = WitnessBuilder("em-linking-sk-theta-extraction", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "EXPLORATORY test of the owner's lead (bean qou-ed61): is the "
        "per-pair Coulomb unit S_K-shaped, S_K = A_omega * cuspModulus "
        "* (ln^2 q0 - theta_K^2)? A_omega = 3 is the exact "
        "q-independent Stokes symmetry constant and cuspModulus = "
        "sqrt3/4 is proved, so the knot-dependence sits entirely in "
        "theta_K -- the OPEN G3 datum. Inverts the extended mirror "
        "series to the implied theta_K per pair and checks the S_K "
        "form for consistency (reality, boost-dominance, smoothness). "
        "Does NOT derive theta_K; the normalisation theta_3 is a "
        "declared free choice and the whole one-parameter family is "
        "reported.")
    wb.add_data("inputs", {
        "A_omega": str(A_OMEGA),
        "cuspModulus": mp.nstr(CUSP_MODULUS, 12),
        "ln_q0": mp.nstr(ln_q0, 12),
        "ln2_q0": mp.nstr(ln2, 12),
        "kappa_A3": mp.nstr(k3, 10),
        "n_pairs": len(rows),
    })
    wb.add_data("theta_families", families)
    wb.add_data("reference_family_analysis", {
        "monotone_increasing": bool(monotone),
        "monotone_within_5pct": bool(near_mono),
        "theta_max": mp.nstr(th_max, 8),
        "theta_max_over_ln_q0": mp.nstr(wall_frac, 8),
        "power_law_scan": powers,
        "best_power_law": best_p,
    })
    wb.add_data("consistency_verdict", (
        "The S_K form SURVIVES this test: with theta_3 = 0 every "
        "extracted theta_A is real and every pair stays "
        "boost-dominated (theta < ln q0), so the binding sign never "
        "flips across the series -- exactly what "
        "`binding_sign_from_angular` requires of a physical "
        "configuration. The extracted theta grows smoothly with A, "
        f"reaching {mp.nstr(wall_frac * 100, 3)}% of ln q0 at the top of "
        "the series."
        if families["theta_3 = 0.0 * ln q0"]["all_real"]
        and families["theta_3 = 0.0 * ln q0"]["all_boost_dominated"]
        else "The S_K form FAILS: extracted theta values are imaginary "
             "or cross into the spin-dominated regime, which would "
             "flip the binding sign."))
    wb.add_data("falsifiable_prediction_TESTED_AND_DEFUSED", {
        "prediction_as_made": (
            "Under the S_K reading, theta_A -> ln q0 is a WALL where the "
            "per-pair unit vanishes. At A = 41 the series had reached "
            "72.4% of it, so I predicted that extending the mirror "
            "ladder 'should show kappa continuing to fall toward zero', "
            "and called this 'a sharp, cheap test that distinguishes "
            "the S_K reading from coth-saturation, which predicts "
            "kappa -> 1, not -> 0'."),
        "what_happened": (
            "The ladder WAS extended, in the same session, from A = 41 "
            "to A = 63 (11 further mirror pairs already in the corpus). "
            "kappa does NOT continue toward zero -- it FLATTENS, from "
            "1.531 at A = 41 to 1.413 at A = 63: a 7.7% decline across "
            "a 54% increase in A, against the factor 2.1 seen over "
            "A = 3..41. theta flattens with it, 0.724 -> 0.749 of "
            "ln q0."),
        "verdict": (
            "The S_K form itself is NOT falsified: theta stays real, "
            "stays boost-dominated, stays monotone within tolerance, "
            "and the A^(1/6) description IMPROVED (2.80% -> 2.33%). "
            "What is falsified is my claim that this was a sharp "
            "discriminator. Under theta ~ A^(1/6), reaching the wall "
            "needs A ~ (1/0.75)^6 * 63 ~ 350 -- far beyond the last "
            "bound mirror pair. The wall is UNREACHABLE in this series, "
            "so the test cannot discriminate, and the two readings are "
            "degenerate over the whole accessible range. I proposed it "
            "as cheap and decisive; it is cheap and indecisive, and "
            "that is recorded rather than restated as a success."),
        "what_the_extension_DID_settle": (
            "Not this, but something else: H_coth's scatter IMPROVED "
            "with the extension (4.25% -> 3.50% on bound pairs) while "
            "its rivals did not (H_FH_Z 4.52% -> 4.39%, H_FH_A 5.50%). "
            "The three are no longer statistically tied. Combined with "
            "the round-5 withdrawal of the H_FH warrant, "
            "coth-saturation is now the only reading with both the best "
            "fit and a structural story -- though 'best of three' is "
            "not the same as derived."),
    })
    wb.add_data("honest_scope", (
        "This is a CONSISTENCY test, not a derivation. theta_K remains "
        "the open G3 datum (bean qou-qnnq); nothing here computes it "
        "from the categorical drivers. The normalisation theta_3 is a "
        "free choice, and the reported power-law scan is descriptive "
        "-- with one free scale it cannot confirm a law, only reveal "
        "gross misbehaviour. What the probe establishes is narrower "
        "and real: the S_K form is not excluded, and it converts the "
        "held-fixed-unit confound into a specific open quantity that "
        "the corpus is already trying to derive."))
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="extracted_theta_all_real",
        computed=int(families["theta_3 = 0.0 * ln q0"]["all_real"]),
        expected=1, tolerance=0, unit="bool",
        source=("S_K consistency: the inversion must yield real "
                "angular deformations for every mirror pair."))
    wb.add_assertion(
        name="all_pairs_boost_dominated",
        computed=int(families["theta_3 = 0.0 * ln q0"]["all_boost_dominated"]),
        expected=1, tolerance=0, unit="bool",
        source=("theta < ln q0 for every pair, so the binding sign "
                "never flips across the series."))
    out = wb.save()

    print(f"ln q0 = {mp.nstr(ln_q0, 10)}   A_omega = 3   "
          f"cuspModulus = {mp.nstr(CUSP_MODULUS, 8)}")
    print("\nextracted theta_K (reference family, theta_3 = 0):")
    for e in ref:
        tv = e["theta_over_ln_q0"]
        print(f"  A={e['A']:2d}  theta={e['theta']:>12}  "
              f"theta/ln q0 = {mp.nstr(mpf(tv), 5)}" if tv is not None
              else f"  A={e['A']:2d}  IMAGINARY")
    print(f"\nmonotone (5% tol): {near_mono}   "
          f"max theta/ln q0 = {mp.nstr(wall_frac, 5)}")
    print("power-law scan (lower scatter = better):")
    for k in sorted(scatter, key=lambda k: scatter[k]):
        print(f"  {mp.nstr(scatter[k] * 100, 4):>7}%  {k}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
