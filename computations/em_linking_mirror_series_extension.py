#!/usr/bin/env python3
"""Extend the kappa(A) mirror series to A ~ 41 — the discriminating test.

Bean qou-i6rg (with qou-8aed). Three hypotheses for the open
two-like-charge EM-linking invariant were left tied on the four light
mirror pairs (A <= 13), because they are numerically close there:

  H_coth   kappa = coth(alpha), alpha ~ A^(1/3)   -> kappa SATURATES at 1
  H_FH_A   Freedman-He template, Vol ~ A          -> kappa ~ A^(-1/3) -> 0
  H_FH_Z   Freedman-He template, Vol ~ Z          -> kappa ~ Z^(-1/3) -> 0

*** WARRANT WITHDRAWN for the two H_FH hypotheses (see
em_linking_fh_link_bound_correction.py). The Vol^(-1/3) they are named
for is Khesin Thm 3.6, the SINGLE-knotted-torus bound. The Freedman-He
LINK bound that actually applies to a Borromean configuration
(Komendarczyk eq. 43) carries (pi/16)^(1/4) -- a pure constant -- and NO
volume factor. So "Freedman-He template" is a misattribution: these are
bare power laws with no literature backing. The scoring below is
unchanged and still worth having as a description of the data; what
changes is that a good H_FH score no longer counts as structural
support. ***

They diverge at large A and in opposite directions, so extending the
mirror series settles them. No new theory is required -- only more AME
data, which the corpus already carries in the qou-mass per-Z isotope
witnesses (`reference_MeV_50dps`). Nothing here is fitted: the
per-pair Coulomb unit and the exponents are all fixed in advance.

Mirror series: A = 2Z - 1, comparing (Z, N=Z-1) against (Z-1, N=Z).
The proton-rich member is the less bound one; the split is
B(Z-1) - B(Z), and the number of extra proton pairs is exactly
C(Z,2) - C(Z-1,2) = Z - 1.

Validation: the four light pairs must reproduce the published kappa
values of `em-linking-invariant-scoping.witness.json` -- an end-to-end
check that this independent extraction agrees with the original.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt, acoth  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ISO = ROOT / "qou-mass/src/qou_mass/data/isotopes"
SCOPING = HERE / "em-linking-invariant-scoping.witness.json"

# Raise precision before the constant below, not only in main(): it is built
# at import time, and at mpmath's default 15 dps this 30-digit literal would
# be frozen at 53 bits — half its digits discarded. Idempotent, so the call in
# main() is unaffected.
set_compute_dps()

# Per-pair Coulomb unit tanh(ln q0)*B_pp with the JUNE 2026 diproton bond
# B_pp = 2.28608834 MeV (docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md).
# It is NOT the current corpus value: charge-coulomb-tn3he-derived.witness.json and
# mirror-pair-coulomb-sign-correction.witness.json now give B_pp = 2.12836095,
# unit 0.2212723003, after E0 moved. Kept deliberately (owner, 2026-11-15) so the
# published kappa of em-linking-invariant-scoping.witness.json still validate:
# swapping it raises every kappa by 7.41 % and leaves the hypothesis ranking
# unchanged. The bond is on the single-crossing interface letters, which the
# gamma-gamma ruling superseded; the redo waits on a gamma-gamma word (#7876).
PER_PAIR_UNIT = mpf("0.237670225314853041078773435698")


def binding(Z: int, A: int):
    f = ISO / f"canonical-isotope-witness-Z{Z:02d}.witness.json"
    if not f.exists():
        return None
    for r in json.loads(f.read_text())["data"]["rows"]:
        if r["A"] == A:
            v = r.get("reference_MeV_50dps")
            return mpf(str(v)) if v is not None else None
    return None


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    return m, sqrt(sum((v - m) ** 2 for v in vals) / n) / m


def main() -> None:
    set_compute_dps()
    rows, skipped = [], []
    for Z in range(2, 33):                     # A = 3 .. 63
        A = 2 * Z - 1
        b_hi, b_lo = binding(Z, A), binding(Z - 1, A)
        if b_hi is None or b_lo is None:
            skipped.append({"A": A, "Z": Z, "why": "AME entry absent"})
            continue
        split = b_lo - b_hi
        if split <= 0:
            skipped.append({"A": A, "Z": Z,
                            "why": f"non-positive split ({mp.nstr(split,6)})"})
            continue
        n_pairs = Z - 1
        kappa = (split / n_pairs) / PER_PAIR_UNIT
        rows.append({"A": A, "Z": Z, "n_pairs": n_pairs,
                     "split_MeV": split, "kappa": kappa})

    # End-to-end validation against the published light-pair values.
    published = {int(r["A"]): mpf(str(r["residual_factor_kappa"]))
                 for r in record_upstream(SCOPING, _UPSTREAM_RECORDS)
                 ["data"]["per_pair_residual_factors"]}
    val = {}
    max_dev = mpf(0)
    for r in rows:
        if r["A"] in published:
            dev = abs(r["kappa"] - published[r["A"]]) / published[r["A"]]
            val[str(r["A"])] = {"recomputed": mp.nstr(r["kappa"], 8),
                                "published": mp.nstr(published[r["A"]], 8),
                                "rel_dev": mp.nstr(dev, 8)}
            max_dev = max(max_dev, dev)

    # Physically-motivated exclusion, declared in advance rather than
    # chosen from the residuals: A = 5 (5He/5Li) and A = 9 (9Be/9B) are
    # particle-UNBOUND systems, so their tabulated "binding energy" is a
    # resonance parameter, not a bound-state observable. They do not
    # belong in a bound-state analysis. Both fits are reported.
    UNBOUND_A = {5, 9}
    bound_rows = [r for r in rows if r["A"] not in UNBOUND_A]

    def score(rs):
        h = {
            "H_FH_A: kappa * A^(1/3) const": [
                r["kappa"] * mpf(r["A"]) ** (mpf(1) / 3) for r in rs],
            "H_FH_Z: kappa * Z^(1/3) const": [
                r["kappa"] * mpf(r["Z"]) ** (mpf(1) / 3) for r in rs],
            "H_coth: arccoth(kappa) / A^(1/3) const": [
                acoth(r["kappa"]) / mpf(r["A"]) ** (mpf(1) / 3) for r in rs],
        }
        out = {}
        for name, vals in h.items():
            m, sd = stats(vals)
            out[name] = {"constant": mp.nstr(m, 8),
                         "rel_scatter": mp.nstr(sd, 8)}
        return out

    scores_bound = score(bound_rows)
    ranked_bound = sorted(scores_bound.items(),
                          key=lambda kv: mpf(kv[1]["rel_scatter"]))

    # Score the three hypotheses over the FULL series.
    hyps = {
        "H_FH_A: kappa * A^(1/3) const": [
            r["kappa"] * mpf(r["A"]) ** (mpf(1) / 3) for r in rows],
        "H_FH_Z: kappa * Z^(1/3) const": [
            r["kappa"] * mpf(r["Z"]) ** (mpf(1) / 3) for r in rows],
        "H_coth: arccoth(kappa) / A^(1/3) const": [
            acoth(r["kappa"]) / mpf(r["A"]) ** (mpf(1) / 3)
            if r["kappa"] > 1 else None for r in rows],
    }
    scores = {}
    for name, vals in hyps.items():
        if any(v is None for v in vals):
            n_bad = sum(1 for v in vals if v is None)
            scores[name] = {
                "rel_scatter": None,
                "note": (f"UNDEFINED for {n_bad} of {len(vals)} pairs: "
                         "kappa <= 1, where arccoth diverges. H_coth "
                         "requires kappa > 1 everywhere (it models kappa "
                         "as coth of a real separation, which is always "
                         "> 1) -- so kappa dropping to or below 1 "
                         "FALSIFIES it outright."),
            }
            continue
        m, sd = stats(vals)
        scores[name] = {"constant": mp.nstr(m, 8),
                        "rel_scatter": mp.nstr(sd, 8)}

    ranked = sorted([(k, v) for k, v in scores.items()
                     if v.get("rel_scatter") is not None],
                    key=lambda kv: mpf(kv[1]["rel_scatter"]))
    kmin = min(r["kappa"] for r in rows)
    kmax = max(r["kappa"] for r in rows)
    coth_alive = kmin > 1

    wb = WitnessBuilder("em-linking-mirror-series", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "The discriminating test for the open two-like-charge "
        "EM-linking invariant (bean qou-i6rg): extends the kappa(A) "
        "mirror series from A <= 13 to the full A = 2Z-1 ladder using "
        "the corpus's own AME reference binding energies, and scores "
        "the three tied hypotheses (coth-saturation, Freedman-He with "
        "Vol ~ A, Freedman-He with Vol ~ Z) over the extended range "
        "where they diverge. Nothing fitted: the per-pair Coulomb unit "
        "and all exponents are fixed in advance. Includes an "
        "end-to-end validation that the recomputed light-pair kappa "
        "values reproduce the published ones.")
    wb.add_data("WARRANT_WITHDRAWN_H_FH", {
        "affects": ["H_FH_A: kappa * A^(1/3) const",
                    "H_FH_Z: kappa * Z^(1/3) const"],
        "why": ("The Vol^(-1/3) these are named for is Khesin Thm 3.6, "
                "the SINGLE-knotted-torus bound. The Freedman-He LINK "
                "bound that applies to a multi-component Borromean "
                "configuration (Komendarczyk arXiv:0808.1533v1 eq. 43) "
                "carries (pi/16)^(1/4), a pure constant, and NO volume "
                "factor. Calling these 'the Freedman-He template' was a "
                "misattribution."),
        "consequence": ("H_FH_A and H_FH_Z are BARE POWER LAWS with no "
                        "literature backing -- the bar the anti-fit "
                        "discipline sets, which they no longer clear. "
                        "The scores below are unchanged and remain a "
                        "valid DESCRIPTION of the data; what changes is "
                        "that a good H_FH score no longer counts as "
                        "structural support. This does not make H_coth "
                        "correct -- it removes its rival's warrant."),
        "see": "em-linking-fh-link-bound-correction.witness.json",
    })
    wb.add_data("series", [
        {"A": r["A"], "Z": r["Z"], "n_pairs": r["n_pairs"],
         "ame_split_MeV": mp.nstr(r["split_MeV"], 8),
         "kappa": mp.nstr(r["kappa"], 8)} for r in rows])
    wb.add_data("skipped", skipped)
    wb.add_data("validation_vs_published", val)
    wb.add_data("hypothesis_scores_all_pairs", scores)
    wb.add_data("hypothesis_scores_bound_only", scores_bound)
    wb.add_data("unbound_exclusion", {
        "excluded_A": sorted(UNBOUND_A),
        "why": ("5He/5Li and 9B are particle-unbound; their tabulated "
                "binding energies are resonance parameters, not "
                "bound-state observables. Declared in advance, not "
                "selected from residuals; both fits reported."),
        "n_bound": len(bound_rows), "n_all": len(rows),
    })
    wb.add_data("ranking_best_first", [k for k, _ in ranked])
    wb.add_data("ranking_best_first_bound_only",
                [k for k, _ in ranked_bound])
    wb.add_data("kappa_range", {"min": mp.nstr(kmin, 8),
                                "max": mp.nstr(kmax, 8),
                                "n_pairs_in_series": len(rows)})
    wb.add_data("verdict", (
        (f"kappa stays above 1 across the series (min "
         f"{mp.nstr(kmin,6)}), so H_coth is not falsified outright; "
         f"the ranking is {[k for k,_ in ranked]}."
         if coth_alive else
         f"kappa FALLS TO {mp.nstr(kmin,6)} <= 1 within the series. "
         "H_coth is FALSIFIED: it models kappa as coth of a real "
         "hyperbolic separation, which is strictly > 1, so it cannot "
         "reach the observed values at any separation. The "
         "saturation reading is dead and the Freedman-He power-law "
         "family survives.")
        + " Note the per-pair Coulomb unit is held at its A=3 value "
          "throughout, as in the original scoping probe; any "
          "A-dependence of the underlying strong bond B_pp is "
          "therefore absorbed into kappa and remains a confound."))
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="reproduces_published_light_kappas",
        computed=mp.nstr(max_dev, 8), expected="0", tolerance="2e-3",
        unit="relative deviation",
        source=("End-to-end check: this independent extraction from the "
                "qou-mass isotope witnesses reproduces the published "
                "kappa values for the four original mirror pairs. "
                "Tolerance is 2e-3, not machine-level: the qou-mass "
                "isotope table and the original scoping probe draw on "
                "AME tabulations that differ at the 4th decimal "
                "(max observed deviation ~4e-4). That floor is "
                "recorded rather than tuned away, and is far below "
                "the ~7% scatter the hypotheses are judged on."))
    wb.add_assertion(
        name="series_extended_beyond_A13",
        computed=int(max(r["A"] for r in rows)), expected=63, tolerance=0,
        unit="max A",
        source="The series now reaches the A ~ 41 discrimination regime.")
    out = wb.save()

    print(f"mirror series ({len(rows)} pairs; skipped {len(skipped)}):")
    for r in rows:
        print(f"  A={r['A']:2d} Z={r['Z']:2d}  pairs={r['n_pairs']:2d}  "
              f"split={mp.nstr(r['split_MeV'],7):>9}  "
              f"kappa={mp.nstr(r['kappa'],6)}")
    print(f"\nkappa range: {mp.nstr(kmin,6)} .. {mp.nstr(kmax,6)}")
    print("\nhypothesis scores, ALL pairs (lower scatter = better):")
    for name, s in scores.items():
        if s.get("rel_scatter") is None:
            print(f"  ---     {name}\n          {s['note'][:90]}...")
        else:
            print(f"  {mp.nstr(mpf(s['rel_scatter']) * 100, 4):>7}%  "
                  f"{name}  (const {s['constant']})")
    print("\nhypothesis scores, BOUND pairs only (A=5,9 excluded as unbound):")
    for name, s in sorted(scores_bound.items(),
                          key=lambda kv: mpf(kv[1]["rel_scatter"])):
        print(f"  {mp.nstr(mpf(s['rel_scatter']) * 100, 4):>7}%  {name}  "
              f"(const {s['constant']})")
    print(f"\nvalidation max deviation: {mp.nstr(max_dev, 4)}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
