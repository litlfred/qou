#!/usr/bin/env python3
"""Low-isotope sign-flip diagnostic — does B_E error track inter-nucleon
channel counts?

## Question

PR #1063 frames the +2.89 % m_p / m_n residual as a *single* refinement
gap inside `VolDensity(𝓑₃)`. That hypothesis predicts every isotope
overshoots by the same fractional amount. The low-isotope witness
table shows otherwise:

| Atom | Z | N | A | err_pct | inter-nucleon ops |
|------|---|---|---|---------|-------------------|
|  p   | 1 | 0 | 1 |  +2.89% | none              |
|  n   | 0 | 1 | 1 |  +2.89% | none              |
|  ²H  | 1 | 1 | 2 |  +1.09% | 1 pn              |
|  ³H  | 1 | 2 | 3 |  -0.16% | 1 pn, 1 nn        |
|  ³He | 2 | 1 | 3 |  -2.97% | 1 pp, 1 pn        |
|  ⁴He | 2 | 2 | 4 |  +5.87% | 1 pp, 1 pn, 1 nn  |

Sign flips → the residual is NOT a uniform VolDensity scale gap. This
script quantifies the channel-count vs error relationship and emits a
witness JSON for downstream audits + the coordination comment on PR
#1063.

## What it computes

For each low-isotope row in `low-isotope-mass-table.witness.json`:
  1. Tally inter-nucleon operators by channel (`pp` / `nn` / `pn`).
  2. Compute candidate scalar predictors:
       - `n_inter` = pp + nn + pn (total inter-nucleon arcs)
       - `signed_h_weight` = 0·pp + (-h)·nn + (-h/2)·pn at q₀
         (the actual sum of the σ + d·𝟙 d-coefficients per channel)
  3. Regress `err_pct` against each predictor (Pearson r + linear fit).
  4. Report which (if any) predictor explains the sign-flip pattern.

## Why it matters

If `err_pct` ≈ α + β · n_inter or ≈ α + β · signed_h_weight with
high r², the per-isotope inter-nucleon channel assignment is the
load-bearing miscalibration, NOT the single-knot VolDensity(𝓑₃)
refinement. That would falsify PR #1063's framing for the
low-isotope cluster and redirect R&D toward the categorical
backing of the pp/pn/nn channel assignment rule (see
`isotope_record_schema.py` lines 176-178: those labels assert
σ for pp, σ⁻¹ for nn, σ_avg for pn — without a Lean `prop:`
block formalising the choice).

## Output

Emits `low-isotope-sign-flip-diagnostic.witness.json` with per-isotope
channel counts, Pearson correlations, and a verdict string.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import fmt, set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

set_compute_dps()

INPUT_WITNESS = _pb.witness_path("low-isotope-mass-table.witness.json", HERE)
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)


def _mpf(x):
    """Coerce a witness field to mpf. Upstream witnesses serialize numbers as
    STRINGS under the NO-FLOAT64 discipline (`_precision.fmt`), so `err_pct`
    arrives as `"-1.234"`, not as a float. Reading it without this coercion is
    what broke this producer: `sum(ys)` raised
    `TypeError: unsupported operand type(s) for +: 'int' and 'str'`."""
    return x if isinstance(x, mp.mpf) else mp.mpf(str(x))


def _pearson_r(xs, ys):
    """Pearson correlation coefficient in mpf. Returns NaN if degenerate.

    mpf, not float: AGENTS.md ("PROBES ARE NOT EXEMPT", 2026-08-18) bans
    aggregating a sample in float64 -- `sum()`/`** 0.5` over a list of floats
    accumulates error across the sample, and this function's output is an
    ARGUMENT (an r^2 that decides a verdict), not a display value."""
    n = len(xs)
    if n < 2:
        return mp.nan
    xs = [_mpf(x) for x in xs]
    ys = [_mpf(y) for y in ys]
    mx = mp.fsum(xs) / n
    my = mp.fsum(ys) / n
    num = mp.fsum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = mp.sqrt(mp.fsum((x - mx) ** 2 for x in xs))
    deny = mp.sqrt(mp.fsum((y - my) ** 2 for y in ys))
    if denx == 0 or deny == 0:
        return mp.nan
    return num / (denx * deny)


def _linear_fit(xs, ys):
    """Returns (slope, intercept, R2) for y = slope*x + intercept, in mpf."""
    r = _pearson_r(xs, ys)
    if not (r == r):  # NaN check
        return mp.nan, mp.nan, mp.nan
    n = len(xs)
    xs = [_mpf(x) for x in xs]
    ys = [_mpf(y) for y in ys]
    mx = mp.fsum(xs) / n
    my = mp.fsum(ys) / n
    cov = mp.fsum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    var = mp.fsum((x - mx) ** 2 for x in xs) / n
    if var == 0:
        return mp.nan, mp.nan, mp.nan
    slope = cov / var
    intercept = my - slope * mx
    return slope, intercept, r ** 2


def _count_channels(knot_ops: list[dict]) -> dict[str, int]:
    """Count inter-nucleon ops by channel."""
    counts = {"pp": 0, "pn": 0, "nn": 0}
    for op in knot_ops:
        if op.get("op_type") != "inter-nucleon":
            continue
        ch = op.get("interface_channel")
        if ch in counts:
            counts[ch] += 1
    return counts


def main() -> int:
    if not INPUT_WITNESS.exists():
        print(f"FATAL: input witness missing: {INPUT_WITNESS}", file=sys.stderr)
        print("       run `python3 low_isotope_mass_table.py` first.",
              file=sys.stderr)
        return 1

    src = record_upstream(INPUT_WITNESS, _UPSTREAM_RECORDS)
    rows_in = src["data"]["rows"]
    # 🛑 PROTON PIN (migrated 2026-08-29, bean `qou-cds3`). AGENTS.md
    # §"q₀ anchor convention": the experimental (proton) anchor is the default
    # for all production compute, and the owner authorisation recorded there
    # covers this sweep ("we want proton unless for an explicit reason ... fix
    # all, even if not visible").
    #
    # This read `q-pinning-50-digit.witness.json` -> `derived_50_digit.q`, the
    # MUON value, which NO manifest entry and NO `QOU_Q0_ANCHOR` could reach: a
    # direct read of the anchor-defining witness computes at muon whatever the
    # configuration says. The two pins differ by 11.54 ppb, the μ–p substrate
    # tension itself.
    #
    # The upstream record is KEPT — that witness remains the canonical 3-CAL
    # (muon) pin document, it is simply no longer the source of this
    # computation's q₀. Idiom copied from `alpha/alpha_k_jones_markov_h12.py`.
    record_upstream(Q_PIN, _UPSTREAM_RECORDS)
    from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON  # noqa: E402
    q = mp.mpf(_Q50_PROTON)
    # mpf, not float(): this feeds `signed_h_weight`, which is regressed
    # against err_pct below -- a computation, not a display (AGENTS.md
    # "PROBES ARE NOT EXEMPT").
    h_q0 = q - 1 / q  # h = q - 1/q at substrate

    # Per-isotope rows
    rows_out = []
    for r in rows_in:
        if r.get("err_pct") is None:
            # Skip rows that have no prediction (e.g. ⁵Li, ⁶Li until
            # wired in a follow-up commit).
            continue
        ch = _count_channels(r["knot_operators"])
        n_inter = ch["pp"] + ch["pn"] + ch["nn"]
        # Sum of d-coefficients: pp contributes 0, pn contributes -h/2
        # per op, nn contributes -h per op (per isotope_record_schema.py
        # CrossingType conventions: SIGMA=(1,0), AVERAGED=(1,-h/2),
        # SIGMA_INV=(1,-h)).
        signed_h_weight = (
            0 * ch["pp"]
            + (-h_q0 / 2) * ch["pn"]
            + (-h_q0) * ch["nn"]
        )
        rows_out.append({
            "Z": r["Z"], "N": r["N"], "A": r["A"],
            "atom_label": _atom_label(r["Z"], r["N"]),
            # Coerced ONCE here, so every downstream comparison and regression
            # sees a number. Upstream serializes these as strings under the
            # NO-FLOAT64 discipline, which is what broke this producer.
            "err_pct": _mpf(r["err_pct"]),
            "err_MeV": _mpf(r["err_MeV"]),
            "prediction_type": r.get("prediction_type", "binding_energy"),
            "channels_pp": ch["pp"],
            "channels_pn": ch["pn"],
            "channels_nn": ch["nn"],
            "n_inter_total": n_inter,
            "signed_h_weight": signed_h_weight,
        })

    # Regress err_pct against each candidate predictor
    err_pcts = [r["err_pct"] for r in rows_out]
    n_inters = [mp.mpf(r["n_inter_total"]) for r in rows_out]
    h_weights = [r["signed_h_weight"] for r in rows_out]

    slope_n, intercept_n, r2_n = _linear_fit(n_inters, err_pcts)
    slope_w, intercept_w, r2_w = _linear_fit(h_weights, err_pcts)

    # Verdict
    if r2_n > 0.8 or r2_w > 0.8:
        verdict = (
            "STRONG correlation between err_pct and inter-nucleon channel "
            "counts/weights — the per-isotope error is dominated by the "
            "channel-assignment layer, NOT by a single-knot VolDensity(𝓑₃) "
            "refinement.  This FALSIFIES the PR #1063 framing for the "
            "low-isotope cluster.  R&D should redirect to the categorical "
            "backing of the pp/pn/nn channel assignment (no `prop:` block "
            "currently formalises the rule)."
        )
    elif r2_n > 0.5 or r2_w > 0.5:
        verdict = (
            "MODERATE correlation between err_pct and inter-nucleon channel "
            "counts/weights.  Single-knot VolDensity(𝓑₃) refinement alone "
            "(PR #1063) cannot account for the sign-flips; partial "
            "channel-assignment effects are at play.  Both refinements "
            "needed."
        )
    else:
        verdict = (
            "WEAK correlation between err_pct and inter-nucleon channel "
            "counts/weights.  Sign-flips are NOT explained by simple "
            "linear channel models.  More complex predictor (per-channel "
            "ratio, closure-topology dependence, or non-linear weighting) "
            "required.  PR #1063 framing not directly falsified by this "
            "diagnostic; needs deeper investigation."
        )

    # KLR-positivity cross-check
    klr_pos_violations = [
        r for r in rows_out
        # _mpf, not float(): this sign test CLASSIFIES a row into the
        # KLR-positivity violation list whose count is recorded in the
        # witness, so it is an argument, not a display.  AGENTS.md
        # ("PROBES ARE NOT EXEMPT") permits float() only inside an f-string.
        if _mpf(r.get("err_pct", 0)) < 0
        and r["prediction_type"] == "binding_energy"
    ]

    w = WitnessBuilder("low-isotope-sign-flip-diagnostic", engine="python")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Per-isotope diagnostic correlating B_E (or mass) error against "
        "inter-nucleon channel counts (pp / pn / nn) and the signed "
        "h-weight sum.  Tests whether the +2.89 % residual is uniform "
        "(PR #1063 single-knot VolDensity refinement framing) or whether "
        "channel-assignment effects drive sign-flips across the "
        "low-isotope sequence.  KLR-positivity (observables ≥ 0) is "
        "checked separately; sign-flips in PREDICTION error are not a "
        "KLR violation per se (the underlying tr_M values remain "
        "positive) but they DO indicate weighting miscalibration."
    )
    w.add_parameter("input_witness", INPUT_WITNESS.name)
    w.add_parameter("q_0_at_50dps", str(q))
    w.add_parameter("h_q0", str(h_q0))
    w.add_parameter("channel_d_coefficients",
                    "pp:0, pn:-h/2, nn:-h (per isotope_record_schema.py "
                    "CrossingType: SIGMA=(1,0), AVERAGED=(1,-h/2), "
                    "SIGMA_INV=(1,-h))")
    w.add_data("per_isotope", rows_out)
    w.add_data("linear_fit_err_pct_vs_n_inter", {
        "slope": slope_n,
        "intercept_pct": intercept_n,
        "R_squared": r2_n,
    })
    w.add_data("linear_fit_err_pct_vs_signed_h_weight", {
        "slope": slope_w,
        "intercept_pct": intercept_w,
        "R_squared": r2_w,
    })
    w.add_data("klr_positivity_check", {
        "trace_level_violations": [],  # all tr_M > 0 by construction
        "prediction_error_sign_flips": [
            {
                "atom": r["atom_label"],
                "err_pct": fmt(r["err_pct"]),
                "interpretation": (
                    "UNDER-prediction (err < 0) → missing positive "
                    "contributions OR over-weighted negative channels"
                    if r["err_pct"] < 0 else
                    "OVER-prediction (err > 0) → extra positive contributions "
                    "OR under-weighted negative channels"
                ),
            }
            for r in rows_out
        ],
        "n_under_predictions": sum(1 for r in rows_out if r["err_pct"] < 0),
        "n_over_predictions": sum(1 for r in rows_out if r["err_pct"] > 0),
    })
    w.add_data("verdict", verdict)
    w.add_caveat(
        "This diagnostic is purely empirical/statistical — it correlates "
        "observed prediction error against structural channel counts to "
        "surface miscalibration patterns.  It does NOT introduce any new "
        "calibration or fit.  A high R² indicates WHERE the miscalibration "
        "lives (channel weights vs VolDensity refinement); the FIX must "
        "still come from a categorical derivation, not from this regression."
    )
    w.add_assertion(
        "diagnostic_emitted_for_all_isotopes_with_predictions",
        computed=len(rows_out) > 0,
        expected=True,
        tolerance=0,
        unit="rows",
        source="low-isotope-mass-table.witness.json projection",
    )

    out = w.save()
    print(f"Witness emitted: {out.name}")
    print()
    print(f"  R² (err_pct vs n_inter)         = {r2_n:.4f}  slope={slope_n:+.4f}")
    print(f"  R² (err_pct vs signed_h_weight) = {r2_w:.4f}  slope={slope_w:+.4f}")
    print()
    print(f"  Verdict: {verdict[:80]}...")
    print()
    print(f"  KLR sign-flip summary:")
    print(f"    under-predictions: {sum(1 for r in rows_out if r['err_pct'] < 0)}")
    print(f"    over-predictions:  {sum(1 for r in rows_out if r['err_pct'] > 0)}")
    return 0


def _atom_label(Z: int, N: int) -> str:
    """Short label for the row."""
    if (Z, N) == (1, 0):
        return "p"
    if (Z, N) == (0, 1):
        return "n"
    if (Z, N) == (1, 1):
        return "²H"
    if (Z, N) == (1, 2):
        return "³H"
    if (Z, N) == (2, 1):
        return "³He"
    if (Z, N) == (2, 2):
        return "⁴He"
    if (Z, N) == (3, 2):
        return "⁵Li"
    if (Z, N) == (3, 3):
        return "⁶Li"
    return f"(Z={Z}, N={N})"


if __name__ == "__main__":
    sys.exit(main())
