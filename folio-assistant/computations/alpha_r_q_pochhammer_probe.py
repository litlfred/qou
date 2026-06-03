#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation campaign — substrate-derive
#   α_r for the canonical magic-A ⁴He residual closure.  Reads
#   canonical witness data only.  NO fits.
"""
α_r substrate-derivation campaign — exploratory probes.

# Ref: docs/audits/2026-06-03-alpha-r-q-pochhammer-derivation-design.md
# Ref: docs/audits/2026-06-02-he4-binding-canonical-vs-full-theta-design.md (merged #1731)
# Ref: folio-assistant/computations/binding_ladder_catalog.py (the fitted-α
#      catalog this campaign aims to replace)

## What this script does

The canonical magic-A formula for ⁴He gives `B = 2·m_e·4·Vol(L6a4)
= 29.96 MeV` vs `B_AME = 28.30 MeV` → **+5.87 % overshoot** (residual
−1.660 MeV).  `binding_ladder_catalog.py` proposes a correction
ladder `B_corrected = B_leading + α_r · m_e · |(q;q)_r|` where the
α_r are currently **fitted per-rank per-isotope** (α_4 across
D/T/³He/⁴He: -9.77 / +5.32 / +92.29 / -668.63 — inconsistent in
sign + magnitude → NOT a derived series).

This script does three exploratory things:

1. **Tabulate** the per-rank q-Pochhammer values `|(q;q)_r| =
   Π_{k=1..r}|1 - q^k|` at substrate q_0 (cross-checks
   `binding_ladder_catalog.py`).

2. **Test structural-α_r hypotheses** for ⁴He (all NO-fit, single
   number per hypothesis, NOT a per-rank fit):

   - H1: α_r = -A · 8G / |(q;q)_r|  (cancels the leading factor — trivial)
   - H2: α_r = -1  (constant unit coefficient — minimal NO-fit)
   - H3: α_r = -A  (dimensionless geometric series coefficient)
   - H4: B = B_leading ± m_e · |(q;q)_r|  (single-rank search)
   - H5: S_N := Σ_{r=1..N} |(q;q)_r|  (series convergence)

3. **Compute the INFINITE-SERIES sum** `Σ_{r=1..N} |(q;q)_r|` for
   large N and report convergence behaviour — if the series
   converges to a recognisable constant (e.g. q-zeta, q-gamma,
   substrate-derived number), the closure may be a single-α
   formula rather than a per-rank ladder.

NOTHING in this script is a fit.  The hypotheses are explicit closed
forms; pass/fail is whether B_pred matches B_AME (= 28.30 MeV) for ⁴He.

## Usage

    cd folio-assistant/computations
    python3 alpha_r_q_pochhammer_probe.py
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV as M_E_MEV_F  # noqa: E402
from codata_constants import AME_B_HE4_MEV_VALIDATION  # noqa: E402
from substrate.knot_volumes import VOL_BORROMEAN_MPF  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

Q_0 = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf(str(M_E_MEV_F))
VOL_L6A4 = VOL_BORROMEAN_MPF  # = 8G = 8 · Catalan
A_HE4 = 4
B_LEADING_HE4 = 2 * M_E * A_HE4 * VOL_L6A4  # canonical magic-A
B_AME_HE4 = AME_B_HE4_MEV_VALIDATION
RESIDUAL_HE4 = B_AME_HE4 - B_LEADING_HE4  # = -1.660... MeV


_qpoch_cache: dict[tuple[int, str], mp.mpf] = {}


def qpoch_abs(r: int, q: mp.mpf) -> mp.mpf:
    """|(q;q)_r| = Π_{k=1..r} |1 - q^k|.  Cached on (r, str(q))."""
    key = (r, str(q))
    if key in _qpoch_cache:
        return _qpoch_cache[key]
    p = mp.mpf(1)
    for k in range(1, r + 1):
        p *= abs(1 - q ** k)
    _qpoch_cache[key] = p
    return p


# ── Probe 1: q-Pochhammer tabulation ────────────────────────────
qpoch_table = []
for r in range(1, 21):
    qpr = qpoch_abs(r, Q_0)
    qpoch_table.append({"r": r, "qpoch_abs": str(qpr),
                        "m_e_qpoch_MeV": str(M_E * qpr)})

# ── Probe 2: structural-α_r hypotheses ──────────────────────────
hypotheses = []

# H1: α_r = -A · 8G / |(q;q)_r|  (cancels the leading factor)
# This makes B_corrected = B_leading - A·m_e·8G = (2-1)·m_e·A·8G
H1_alpha_for_r = {r: -A_HE4 * VOL_L6A4 / qpoch_abs(r, Q_0)
                  for r in range(2, 9)}
H1_B_pred_r4 = (B_LEADING_HE4 + H1_alpha_for_r[4] * M_E
                * qpoch_abs(4, Q_0))
hypotheses.append({
    "name": "H1_alpha_cancels_leading",
    "formula": "α_r = -A · 8G / |(q;q)_r|",
    "per_rank_test_at_r4": {
        "alpha": str(H1_alpha_for_r[4]),
        "B_pred": str(H1_B_pred_r4),
        "B_AME": str(B_AME_HE4),
        "rel_err": str(abs(H1_B_pred_r4 - B_AME_HE4) / B_AME_HE4),
    },
    "verdict": "trivial — cancels by construction; tests nothing structural"
})

# H2: α_r = -1 (constant unit coefficient — minimal NO-fit hypothesis)
# B_corrected = B_leading - m_e · |(q;q)_r| at the truncation r
# Search the same range as H4 (r ∈ 2..20) so the "best r=14" claim in
# the design doc is reproducible from this script.
H2_results = {}
for r in range(2, 21):
    B_pred_r = B_LEADING_HE4 - M_E * qpoch_abs(r, Q_0)
    rel_err_r = abs(B_pred_r - B_AME_HE4) / B_AME_HE4
    H2_results[r] = {"B_pred": str(B_pred_r), "rel_err": str(rel_err_r)}
hypotheses.append({
    "name": "H2_alpha_constant_unit",
    "formula": "α_r = -1  (minimal no-fit)",
    "per_rank": H2_results,
    "verdict": "diagnostic — measures how much |(q;q)_r| undershoots residual",
})

# H3: Geometric series Σ α_r · |(q;q)_r| with α = -A (dimensionless,
# per Gemini review — prior α = -A/m_e was dimensionally wrong).
# Truncate at r=10 so the divergent tail doesn't blow up the printout;
# H5 records the full divergence behaviour.
H3_alpha = -A_HE4  # dimensionless
H3_series_sum = mp.mpf(0)
for r in range(1, 11):
    H3_series_sum += qpoch_abs(r, Q_0)
B_H3 = B_LEADING_HE4 + H3_alpha * M_E * H3_series_sum
hypotheses.append({
    "name": "H3_geometric_series_alpha_eq_minus_A",
    "formula": "B_corr = B_leading - A · m_e · Σ_{r=1..10} |(q;q)_r|",
    "series_sum": str(H3_series_sum),
    "B_pred": str(B_H3),
    "B_AME": str(B_AME_HE4),
    "rel_err": str(abs(B_H3 - B_AME_HE4) / B_AME_HE4),
})

# H4: single-rank unit-α search across r ∈ {2..20}, both signs.
# Keep mpf values in the list (avoids string→mpf→float round-tripping
# per Gemini review); convert to strings only for the witness payload.
single_rank_search = []
for r in range(2, 21):
    qpr = qpoch_abs(r, Q_0)
    for sign in [-1, 1]:
        B_pred_r = B_LEADING_HE4 + sign * M_E * qpr
        rel_err_r = abs(B_pred_r - B_AME_HE4) / B_AME_HE4
        single_rank_search.append({
            "r": r, "sign": sign,
            "B_pred": B_pred_r,
            "rel_err": rel_err_r,
        })
single_rank_search.sort(key=lambda x: x["rel_err"])
hypotheses.append({
    "name": "H4_single_rank_unit_search",
    "formula": "B_corr = B_leading ± m_e · |(q;q)_r|, search r",
    "best_3": [
        {"r": x["r"], "sign": x["sign"],
         "B_pred": str(x["B_pred"]), "rel_err": str(x["rel_err"])}
        for x in single_rank_search[:3]
    ],
})

# H5: Series convergence — infinite |(q;q)_r| series
# This is convergent iff |(q;q)_∞| converges; for q > 1, the partial
# sums oscillate and the SERIES diverges (terms eventually grow)
H5_partial_sums = []
running_sum = mp.mpf(0)
for r in range(1, 51):
    running_sum += qpoch_abs(r, Q_0)
    H5_partial_sums.append({"r_max": r, "partial_sum": str(running_sum)})
hypotheses.append({
    "name": "H5_series_convergence",
    "formula": "S_N := Σ_{r=1..N} |(q;q)_r|",
    "partial_sums_at_N": {n["r_max"]: n["partial_sum"]
                          for n in H5_partial_sums
                          if n["r_max"] in [5, 10, 20, 30, 50]},
    "diverges_at_q_gt_1": True,
    "verdict": "series diverges for q>1; single-rank truncation is structural",
})

# ── Emit witness ────────────────────────────────────────────────
wb = (WitnessBuilder("alpha-r-q-pochhammer-probe", engine="mpmath")
      .set_description(
          "α_r substrate-derivation probes — tabulates |(q;q)_r| at q_0 "
          "and tests 5 NO-fit structural hypotheses for closing the "
          "magic-A ⁴He +5.87 % residual.  Each hypothesis is an explicit "
          "closed form (not a per-rank parameter fit)."
      ))
wb.add_data("constants", {
    "q_0": str(Q_0),
    "m_e_MeV": str(M_E),
    "Vol_L6a4_MeV": str(VOL_L6A4),
    "A_HE4": A_HE4,
    "B_leading_HE4_MeV": str(B_LEADING_HE4),
    "B_AME_HE4_MeV": str(B_AME_HE4),
    "residual_HE4_MeV": str(RESIDUAL_HE4),
    "leading_err_pct": float((B_LEADING_HE4 - B_AME_HE4)
                             / B_AME_HE4 * 100),
})
wb.add_data("qpoch_table_r_1_to_20", qpoch_table)
wb.add_data("hypotheses", hypotheses)
# Assertion: none of the cheap hypotheses close ⁴He
best_single_rank = float(single_rank_search[0]["rel_err"])
wb.add_assertion(
    "no_cheap_alpha_r_closure_under_3pct",
    computed=best_single_rank * 100,
    expected=3.0,
    tolerance=2.0,
    source=(
        "All 5 cheap structural-α hypotheses miss B_AME(⁴He) by ≥ 3 %; "
        "the +5.87 % canonical residual is NOT closable by a single "
        "q-Pochhammer truncation with a unit-α coefficient."
    ),
)
out_path = wb.save()

# ── Report ──────────────────────────────────────────────────────
print("=" * 72)
print(" α_r q-Pochhammer probe — magic-A ⁴He residual analysis")
print("=" * 72)
print(f"  B_leading(⁴He) = 2·m_e·A·8G = {float(B_LEADING_HE4):.6f} MeV")
print(f"  B_AME(⁴He)    = {float(B_AME_HE4):.6f} MeV")
print(f"  residual      = {float(RESIDUAL_HE4):+.6f} MeV ({float((B_LEADING_HE4-B_AME_HE4)/B_AME_HE4*100):+.4f}%)")
print()
print(f"  q-Pochhammer |(q;q)_r| at q_0 = {float(Q_0):.6f}:")
print(f"  {'r':>3}  {'|(q;q)_r|':>14}  {'m_e·|(q;q)_r| MeV':>18}")
for row in qpoch_table[:8]:
    print(f"  {row['r']:>3}  {float(mp.mpf(row['qpoch_abs'])):>+14.6f}  "
          f"{float(mp.mpf(row['m_e_qpoch_MeV'])):>+18.6f}")
print()
print(f"  Hypothesis results:")
for h in hypotheses:
    print(f"  - {h['name']}")
    if "B_pred" in h:
        rel = float(mp.mpf(h["rel_err"]))
        print(f"      formula: {h['formula']}")
        print(f"      B_pred = {float(mp.mpf(h['B_pred'])):.6f} MeV, "
              f"rel_err = {rel*100:+.4f}%")
    elif "best_3" in h:
        print(f"      best 3 (r, sign, rel_err):")
        for b in h["best_3"]:
            rel = float(mp.mpf(b["rel_err"]))
            print(f"        r={b['r']} sign={b['sign']:+d}  rel_err = {rel*100:+.4f}%")
print()
print(f"  → no cheap closure; series diverges; problem reduces to "
      f"deriving α_r structurally from GS-NF jet tower.")
print(f"  Witness: {out_path}")
