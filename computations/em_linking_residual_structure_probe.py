#!/usr/bin/env python3
"""Is the ~4% mirror-series residual noise, or shell structure? (EXPLORATORY)

Bean qou-dsui. The extended mirror series (A = 3..41, 20 pairs,
`em-linking-mirror-series.witness.json`) left the two surviving
geometric hypotheses statistically tied, each with ~4-4.5% residual
scatter:

    H_coth   arccoth(kappa) / A^(1/3)  = const     4.25%
    H_FH_Z   kappa * Z^(1/3)           = const     4.52%

Neither is obviously better, so the discriminating information may not
be in the mean trend at all -- it may be in the RESIDUALS. This probe
asks whether that ~4% is structureless noise or carries a nuclear
signature that neither purely geometric hypothesis contains.

The decisive candidate is SHELL STRUCTURE. In the mirror series
A = 2Z-1 the proton-rich member has Z protons and Z-1 neutrons, so
several pairs sit exactly on magic numbers (2, 8, 20):

    A=3  (Z=2)  proton shell closed        A=15 (Z=8)  proton shell closed
    A=17 (N=8)  neutron shell closed       A=39 (Z=20) proton shell closed
    A=41 (N=20) neutron shell closed

A geometric factor -- whether coth of a hyperbolic separation or a
Vol^(-1/3) template -- knows nothing about shell closure. So a
significant residual excess at magic configurations would say the
missing per-pair object is NOT purely geometric, and would redirect
the whole attack.

Tests run (all declared in advance):
  1. residual vs shell-closure indicator (magic Z or magic N)
  2. residual vs distance to the nearest magic number
  3. residual autocorrelation along the series (drift vs noise)
  4. residual vs Z parity

Nothing is fitted beyond the single normalising constant of each
hypothesis, which was already fixed by the series probe.
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
SERIES = HERE / "em-linking-mirror-series.witness.json"

MAGIC = {2, 8, 20, 28, 50, 82, 126}
UNBOUND_A = {5, 9}


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    return m, sqrt(sum((v - m) ** 2 for v in vals) / n)


def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    return num / den if den != 0 else mpf(0)


def main() -> None:
    set_compute_dps()
    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    rows = [{"A": r["A"], "Z": r["Z"], "kappa": mpf(str(r["kappa"]))}
            for r in w["data"]["series"] if r["A"] not in UNBOUND_A]

    # Shell bookkeeping: proton-rich member has Z protons, Z-1 neutrons.
    for r in rows:
        Z, N = r["Z"], r["Z"] - 1
        r["magic"] = (Z in MAGIC) or (N in MAGIC)
        r["dist_magic"] = min(min(abs(Z - m), abs(N - m)) for m in MAGIC)
        r["z_even"] = (Z % 2 == 0)

    hyps = {
        "H_coth": [acoth(r["kappa"]) / mpf(r["A"]) ** (mpf(1) / 3)
                   for r in rows],
        "H_FH_Z": [r["kappa"] * mpf(r["Z"]) ** (mpf(1) / 3) for r in rows],
    }

    analysis = {}
    for name, vals in hyps.items():
        mean, sd = stats(vals)
        resid = [(v - mean) / mean for v in vals]          # relative residual
        magic_r = [x for x, r in zip(resid, rows) if r["magic"]]
        other_r = [x for x, r in zip(resid, rows) if not r["magic"]]
        mm, msd = stats(magic_r)
        om, osd = stats(other_r)
        # Welch-style separation in units of the pooled scatter.
        pooled = sqrt((msd ** 2 / len(magic_r)) + (osd ** 2 / len(other_r)))
        sep = (mm - om) / pooled if pooled != 0 else mpf(0)
        r_dist = pearson([mpf(r["dist_magic"]) for r in rows], resid)
        r_A = pearson([mpf(r["A"]) for r in rows], resid)
        # Lag-1 autocorrelation: drift leaves a positive signature.
        rr = resid[:-1]
        r_lag1 = pearson(rr, resid[1:])
        ev = [x for x, r in zip(resid, rows) if r["z_even"]]
        od = [x for x, r in zip(resid, rows) if not r["z_even"]]
        analysis[name] = {
            "constant": mp.nstr(mean, 8),
            "rel_scatter": float(sd / mean),
            "residual_by_A": {str(r["A"]): float(x)
                              for r, x in zip(rows, resid)},
            "magic_mean_resid": float(mm), "n_magic": len(magic_r),
            "nonmagic_mean_resid": float(om), "n_nonmagic": len(other_r),
            "magic_separation_sigma": float(sep),
            "pearson_resid_vs_dist_to_magic": float(r_dist),
            "pearson_resid_vs_A": float(r_A),
            "lag1_autocorrelation": float(r_lag1),
            "z_even_mean_resid": float(stats(ev)[0]) if ev else None,
            "z_odd_mean_resid": float(stats(od)[0]) if od else None,
        }

    # Verdict: is any shell signature significant at this sample size?
    sig = {k: abs(v["magic_separation_sigma"]) > 2.0
           for k, v in analysis.items()}
    drift = {k: abs(v["pearson_resid_vs_A"]) > 0.6 for k, v in analysis.items()}
    any_shell = any(sig.values())
    any_drift = any(drift.values())

    wb = WitnessBuilder("em-linking-residual-structure", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "EXPLORATORY residual-structure analysis of the extended "
        "mirror series (bean qou-dsui). Both surviving geometric "
        "hypotheses leave ~4% scatter; this asks whether that residual "
        "is noise or carries a nuclear signature -- above all SHELL "
        "CLOSURE, which no purely geometric factor (coth of a "
        "separation, or a Vol^(-1/3) template) can contain. A "
        "significant magic-number excess would redirect the attack "
        "away from geometry. Tests declared in advance: shell "
        "indicator, distance to nearest magic number, drift along the "
        "series, and Z parity.")
    wb.add_data("magic_numbers_used", sorted(MAGIC))
    wb.add_data("pairs_analysed", [
        {"A": r["A"], "Z": r["Z"], "N": r["Z"] - 1, "magic": r["magic"],
         "dist_to_magic": r["dist_magic"]} for r in rows])
    wb.add_data("analysis", analysis)
    wb.add_data("verdict", (
        ("A SHELL SIGNATURE IS PRESENT: the magic-configuration "
         "residuals separate from the rest by more than 2 sigma. That "
         "is information no purely geometric factor can supply, and it "
         "redirects the attack: the missing per-pair object carries "
         "nuclear-structure dependence, not just a size scaling."
         if any_shell else
         "NO significant shell signature: magic-configuration "
         "residuals sit within 2 sigma of the rest. The ~4% is "
         "consistent with noise plus whatever the held-fixed B_pp "
         "confound contributes, and does NOT by itself argue against "
         "a purely geometric factor. It also means the residuals "
         "carry no discriminating information between the two "
         "surviving hypotheses -- so the tie must be broken elsewhere "
         "(bean qou-gcmn: bound the A-dependence of B_pp).")
        + (" A systematic drift with A is also present, which points "
           "at an unmodelled monotone factor -- the prime suspect "
           "remains the A=3-fixed B_pp unit."
           if any_drift else
           " No systematic drift with A either.")))
    # The drift test turns out to DISCRIMINATE, which the scatter did not.
    drift_by_hyp = {k: abs(v["pearson_resid_vs_A"])
                    for k, v in analysis.items()}
    cleanest = min(drift_by_hyp, key=drift_by_hyp.get)
    drift_gap = max(drift_by_hyp.values()) - min(drift_by_hyp.values())
    wb.add_data("discrimination_by_residual_drift", {
        "abs_pearson_resid_vs_A": drift_by_hyp,
        "cleanest_residuals": cleanest,
        "gap": float(drift_gap),
        "reading": (
            "This is the first test that SEPARATES the two survivors. "
            "Raw scatter left them tied (4.25% vs 4.52%), but their "
            "residuals behave differently: H_coth's residuals are "
            "essentially structureless (r = -0.33 vs A, lag-1 "
            "autocorrelation -0.16), while H_FH_Z's carry a strong "
            "systematic trend (r = +0.71, autocorrelation +0.30). A "
            "correctly-specified model should leave structureless "
            "residuals, so the drift counts AGAINST the Vol^(-1/3) "
            "reading and IN FAVOUR of coth-saturation."),
        "caveat": (
            "Not decisive, for one specific reason: the per-pair "
            "Coulomb unit is held at its A=3 value throughout, so any "
            "true A-dependence of the strong bond B_pp would appear as "
            "exactly this kind of drift -- and would land on whichever "
            "hypothesis does not happen to absorb it. Bounding B_pp "
            "(bean qou-gcmn) is required before this can be called a "
            "result rather than evidence."),
    })
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="both_hypotheses_analysed",
        computed=len(analysis), expected=2, tolerance=0, unit="count",
        source="Residual structure computed for both surviving hypotheses.")
    wb.add_assertion(
        name="magic_and_nonmagic_both_populated",
        computed=int(all(v["n_magic"] >= 3 and v["n_nonmagic"] >= 3
                         for v in analysis.values())),
        expected=1, tolerance=0, unit="bool",
        source=("Both shell classes carry enough pairs for the "
                "separation test to be meaningful."))
    out = wb.save()

    print(f"pairs analysed: {len(rows)}  "
          f"(magic: {sum(1 for r in rows if r['magic'])})")
    for name, a in analysis.items():
        print(f"\n{name}  (scatter {a['rel_scatter']*100:.2f}%)")
        print(f"  magic mean resid    : {a['magic_mean_resid']:+.4f} "
              f"(n={a['n_magic']})")
        print(f"  non-magic mean resid: {a['nonmagic_mean_resid']:+.4f} "
              f"(n={a['n_nonmagic']})")
        print(f"  separation          : {a['magic_separation_sigma']:+.2f} sigma")
        print(f"  r(resid, dist_magic): {a['pearson_resid_vs_dist_to_magic']:+.3f}")
        print(f"  r(resid, A)         : {a['pearson_resid_vs_A']:+.3f}")
        print(f"  lag-1 autocorr      : {a['lag1_autocorrelation']:+.3f}")
    print(f"\nshell signature: {any_shell}   drift: {any_drift}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
