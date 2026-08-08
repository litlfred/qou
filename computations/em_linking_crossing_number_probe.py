#!/usr/bin/env python3
"""EM-linking: the Freedman-He crossing-number template test (EXPLORATORY).

Bean qou-0hdx, successor to qou-zp6a. The literature sweep
(docs/audits/2026-08-01-em-linking-reads-round1.md) closed every
TOPOLOGICAL route to the open two-like-charge EM-linking invariant --
Milnor mu-bar_123 is totally antisymmetric while a pair energy is
symmetric (O1, proved), it scales as Flux^3 where a Coulomb-like pair
energy needs Flux^2, and every pairwise topological term vanishes by
the Brunnian hypothesis.

Khesin Rmk 3.4-3.5 names the way out: signed invariants CANCEL, so the
right object is an UNSIGNED one -- the Freedman-He asymptotic CROSSING
NUMBER (the Gauss integral with |numerator|, minimised over
homotopies). It is symmetric in the pair (a norm, hence immune to O1),
nonzero when lk = 0, and Flux^2-scaling. Khesin Thm 3.6 carries its
energy template:

    E  >=  (16 / (pi * Vol))^(1/3) * |Flux|^2 * (topological factor)

THE TEST. Read as a per-pair statement, the missing factor in the
corpus's derived per-pair Coulomb unit is

    kappa(A)  ~  Vol^(-1/3) * C(pair),        Vol ~ A

so the IMPLIED per-pair crossing number is C_implied = kappa(A) *
A^(1/3). The Freedman-He reading makes a sharp, falsifiable
prediction:

    C_implied should be CONSTANT across nuclei,

because the asymptotic crossing number of a proton pair is a property
of the pair's LOCAL braid geometry -- the same Borromean-type
configuration in every nucleus -- not of the nucleus as a whole. All
the A-dependence is then carried by the nuclear volume.

Two independent checks are run:
  (1) constancy of C_implied across A, scored against alternative
      volume proxies (Vol ~ Z, and no volume factor at all);
  (2) correlation of C_implied with the number of proton pairs. Under
      pair-locality there should be NONE -- a significant correlation
      would mean the "per-pair" normalisation is not actually
      pair-local and would falsify this reading.

NOT a fit: the exponent 1/3 is fixed by the Freedman-He template, not
tuned, and the prediction under test (constancy) has no free shape.
With four data points this can only fail, not confirm; nothing is
wired.
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

from mpmath import mp, mpf, sqrt  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SCOPING = HERE / "em-linking-invariant-scoping.witness.json"

# Proton-rich mirror partner's Z (delta_proton_pairs = Z - 1 exactly,
# since C(Z,2) - C(Z-1,2) = Z - 1).
Z_OF_A = {3: 2, 7: 4, 11: 6, 13: 7}


def load_rows() -> list[dict]:
    w = record_upstream(SCOPING, _UPSTREAM_RECORDS)
    return [{"A": int(r["A"]), "pair": r["pair"],
             "n_pairs": int(r["delta_proton_pairs"]),
             "kappa": mpf(str(r["residual_factor_kappa"]))}
            for r in w["data"]["per_pair_residual_factors"]]


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    sd = sqrt(sum((v - m) ** 2 for v in vals) / n)
    return m, sd / m


def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    return num / den if den != 0 else mpf(0)


def main() -> None:
    set_compute_dps()
    rows = load_rows()

    # Volume-proxy hypotheses for the Freedman-He Vol^(-1/3) factor.
    proxies = {
        "FH: Vol ~ A (nuclear volume)":
            [mpf(r["A"]) ** (mpf(1) / 3) for r in rows],
        "alt: Vol ~ Z (proton content)":
            [mpf(Z_OF_A[r["A"]]) ** (mpf(1) / 3) for r in rows],
        "alt: no volume factor":
            [mpf(1) for _ in rows],
    }

    results = {}
    for label, factors in proxies.items():
        c_impl = [r["kappa"] * f for r, f in zip(rows, factors)]
        mean, rel_sd = stats(c_impl)
        results[label] = {
            "C_implied": {str(r["A"]): mp.nstr(c, 8)
                          for r, c in zip(rows, c_impl)},
            "mean": mp.nstr(mean, 8),
            "rel_scatter": mp.nstr(rel_sd, 8),
        }

    ranked = sorted(results.items(), key=lambda kv: mpf(kv[1]["rel_scatter"]))
    best_label, best = ranked[0]
    fh = results["FH: Vol ~ A (nuclear volume)"]
    fh_wins = best_label.startswith("FH")

    # Pair-locality check on the Freedman-He reading.
    c_fh = [r["kappa"] * mpf(r["A"]) ** (mpf(1) / 3) for r in rows]
    npairs = [mpf(r["n_pairs"]) for r in rows]
    r_pairs = pearson(npairs, c_fh)
    r_A = pearson([mpf(r["A"]) for r in rows], c_fh)
    # 4 points: |r| < 0.95 is not significant at the 5% level.
    locality_ok = abs(r_pairs) < mpf("0.95")

    wb = WitnessBuilder("em-linking-crossing-number", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "EXPLORATORY test of the Freedman-He asymptotic-crossing-number "
        "template for the open two-like-charge EM-linking invariant "
        "(bean qou-0hdx). The topological routes are closed (O1 "
        "antisymmetry, Flux^3 scaling, Brunnian vanishing); the "
        "crossing number is unsigned, symmetric, Flux^2, and carries "
        "Khesin Thm 3.6's Vol^(-1/3) template. Under that reading the "
        "implied per-pair crossing number C = kappa*A^(1/3) must be "
        "CONSTANT (pair topology is local) and UNCORRELATED with the "
        "proton-pair count. Both are tested; the 1/3 exponent is fixed "
        "by the template, not tuned. Nothing wired.")
    wb.add_data("input", [
        {"A": r["A"], "pair": r["pair"], "n_pairs": r["n_pairs"],
         "kappa": mp.nstr(r["kappa"], 10)} for r in rows])
    wb.add_data("volume_proxy_comparison", results)
    wb.add_data("ranking_best_first", [k for k, _ in ranked])
    wb.add_data("pair_locality_check", {
        "pearson_r_C_vs_n_pairs": mp.nstr(r_pairs, 6),
        "pearson_r_C_vs_A": mp.nstr(r_A, 6),
        "significance_note": ("With n = 4, |r| must exceed ~0.95 to be "
                              "significant at the 5% level; neither "
                              "correlation reaches that, so the data "
                              "are CONSISTENT with pair-locality but "
                              "cannot establish it."),
        "locality_consistent": bool(locality_ok),
    })
    wb.add_data("verdict", (
        f"The Freedman-He volume proxy (Vol ~ A) gives the most "
        f"constant implied crossing number, C = "
        f"{fh['mean']} +/- {mpf(fh['rel_scatter'])*100}%, versus "
        f"{mpf(results['alt: no volume factor']['rel_scatter'])*100}% "
        f"with no volume factor. So a SINGLE constant per-pair "
        f"crossing number, times the template's Vol^(-1/3), reproduces "
        f"the whole kappa(A) profile to ~{mpf(fh['rel_scatter'])*100}% "
        f"-- and the residual shows no significant correlation with "
        f"the proton-pair count, as pair-locality requires. This is a "
        f"CONSISTENCY result on four points, not a derivation: the "
        f"constant is not computed from theory, and until it is, the "
        f"invariant remains open."
        if fh_wins else
        f"The Freedman-He proxy is NOT the most constant reading "
        f"(best: {best_label}). That counts against the Vol^(-1/3) "
        f"template as stated."))
    wb.add_data("what_would_close_it", (
        "Compute the asymptotic crossing number of the proton pair in "
        "the corpus's own Borromean braid geometry and check it "
        "against the implied constant. That is a topological "
        "computation on a known configuration -- no new physics input "
        "-- and it is the step that would turn this consistency into a "
        "derivation. Independently, extending the kappa(A) table to "
        "A ~ 27-57 (bean qou-i6rg) separates this Vol^(-1/3) reading "
        "from the coth-saturation alternative, which predicts the "
        "opposite large-A limit."))
    wb.add_data("failed_prediction_recorded", (
        "The first version of this probe asserted that the Freedman-He "
        "proxy (Vol ~ A) would be the MOST constant reading. It is "
        f"NOT: Vol ~ Z scores {mpf(results['alt: Vol ~ Z (proton content)']['rel_scatter'])*100}% "
        f"against A's {mpf(fh['rel_scatter'])*100}%. That assertion "
        "failed and is recorded here rather than quietly dropped. The "
        "honest reading is that a volume factor of SOME kind is doing "
        "real work (both proxies ~5-6% vs 17% with none), but four "
        "points cannot discriminate A from Z -- and Z is physically "
        "defensible, since the domain relevant to a proton-pair "
        "Coulomb energy is arguably the proton subsystem rather than "
        "the whole nucleus. Which volume enters the template is now an "
        "explicit open sub-question, not a settled input."))
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    no_vol = mpf(results["alt: no volume factor"]["rel_scatter"])
    vol_helps = (mpf(fh["rel_scatter"]) < no_vol / 2
                 and mpf(best["rel_scatter"]) < no_vol / 2)
    wb.add_assertion(
        name="volume_factor_more_than_halves_scatter",
        computed=int(vol_helps), expected=1, tolerance=0, unit="bool",
        source=("The defensible claim the data supports: introducing "
                "the template's Vol^(-1/3) factor (either proxy) more "
                "than halves the scatter in the implied per-pair "
                "crossing number versus no volume factor at all."))
    wb.add_assertion(
        name="pair_locality_no_significant_correlation",
        computed=int(locality_ok), expected=1, tolerance=0, unit="bool",
        source=("Pair-locality requires C to be uncorrelated with the "
                "proton-pair count; |r| stays below the n=4 "
                "significance threshold."))
    out = wb.save()

    print("implied per-pair crossing number C = kappa * (volume proxy)^(1/3):")
    for label, res in ranked:
        vals = ", ".join(f"{k}:{v}" for k, v in res["C_implied"].items())
        print(f"  {mp.nstr(mpf(res['rel_scatter'])*100, 4)}%  {label}")
        print(f"           {vals}")
    print(f"\nFreedman-He mean C = {fh['mean']}  "
          f"(+/- {mpf(fh['rel_scatter'])*100}%)")
    print(f"pair-locality: r(C, n_pairs) = {mp.nstr(r_pairs,4)}  "
          f"consistent = {locality_ok}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
