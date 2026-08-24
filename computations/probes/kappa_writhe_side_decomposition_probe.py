#!/usr/bin/env python3
"""kappa_writhe_side_decomposition_probe.py — locate which side of the
residual carries the writhe coefficient κ = b/4.

CONTEXT. The bar-odd (isovector) coefficient of the canonical residual,
b(A) ≈ −1.75 (constant across A=6–12; synthesis audit 2026-06-29), is
conjecturally b = 4κ with 4 = d(writhe)/dT₃ derived from the atom word
(writhe = 4Z; Lean writhe_eq_four_Z). The per-writhe-unit weight κ ≈
−0.437 is the open magnitude (sign derived from the p≠n intra-writhe
seed 3 > 1; simple framing constants pruned as numerology).

Since Δ_λ = B_AME/B_pred, the measured b decomposes exactly:

    b_total = b_AME − b_pred,   b_X = d(log_{q₀} X)/dT₃ at fixed A.

The H1-refutation precedent (2026-06-13, for the bar-EVEN leading term)
found the A-slope lives on the AME side. This probe asks the same
LOCATION question for the bar-ODD b: does the framework's own mirror
asymmetry (the nn interface factor z−h vs pp z in binding_canonical)
supply κ, or is b carried by the experimental Coulomb asymmetry?

METHOD (pure post-processing, no new binding solves): read the
per-member B_pred and B_AME already recorded in
delta-lambda-imme-triplet.witness.json (A=6,8,10,12) and
delta-lambda-imme-quartet.witness.json (A=9, same-T corrected), and
compute the inner mirror slopes on each side. Structural comparison
values (NOT candidates to wire — location diagnostics only):
log_{q₀}(z/(z−h)) = the per-(nn→pp)-interface-swap trace-factor
exponent, and its /4 per-writhe-unit reading.

Not wired; near-match tier; no fit.

Ref: docs/audits/2026-06-29-delta-lambda-residual-synthesis.md
Ref: docs/audits/2026-06-29-delta-lambda-z-correction-writhe.md
Ref: docs/audits/2026-06-13-9b-h1-exponent-location-refuted.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_MP as Q0  # noqa: E402


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q0)); h = q - 1 / q
    lnq = mp.log(q)
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + 1/sqrt q), excised.
    z = q ** 3 / (q ** 2 + 1)
    swap_exponent = mp.log(z / (z - h)) / lnq  # per nn→pp interface swap

    rows = []

    # --- triplets (A = 6, 8, 10, 12): members keyed by T3 = -1, 0, +1 ---
    trip = record_upstream(ROOT / "delta-lambda-imme-triplet.witness.json", _UPSTREAM_RECORDS)
    tdata = trip.get("data", trip)
    for r in tdata["triplets"]:
        A = r["A"]
        m = {int(k): v for k, v in r["members"].items()}
        bp_m, bp_p = m[-1]["B_pred"], m[1]["B_pred"]
        # b_pred: inner mirror slope of log_q0 B_pred over ΔT3 = 2
        b_pred = float(mp.log(mp.mpf(str(bp_p)) / mp.mpf(str(bp_m))) / lnq / 2)
        b_total = r["imme_b_linear"]
        b_ame = b_total + b_pred
        rows.append({"A": A, "source": "triplet", "delta_T3": 2,
                     "b_total": b_total, "b_pred_framework": round(b_pred, 4),
                     "b_AME_experimental": round(b_ame, 4)})

    # --- quartet (A = 9): inner members T3 = ±1/2, same-T corrected ---
    quar = record_upstream(ROOT / "delta-lambda-imme-quartet.witness.json", _UPSTREAM_RECORDS)
    qdata = quar.get("data", quar)
    qq = qdata["quartet"]
    bp_m, bp_p = qq["-0.5"]["B_pred"], qq["0.5"]["B_pred"]
    b_pred9 = float(mp.log(mp.mpf(str(bp_p)) / mp.mpf(str(bp_m))) / lnq)
    b_total9 = qdata["same_T"]["b_linear"]
    rows.append({"A": 9, "source": "quartet(inner, same-T)", "delta_T3": 1,
                 "b_total": b_total9, "b_pred_framework": round(b_pred9, 4),
                 "b_AME_experimental": round(b_total9 + b_pred9, 4)})

    rows.sort(key=lambda r: r["A"])
    print(f"{'A':>3} {'b_total':>9} {'b_pred(FW)':>11} {'b_AME(exp)':>11}")
    for r in rows:
        print(f"{r['A']:>3} {r['b_total']:>9.3f} {r['b_pred_framework']:>11.3f} "
              f"{r['b_AME_experimental']:>11.3f}")

    bp = [r["b_pred_framework"] for r in rows]
    ba = [r["b_AME_experimental"] for r in rows]
    bt = [r["b_total"] for r in rows]
    fw_share = [p / t for p, t in zip(bp, bt)]
    print(f"\n  per-interface-swap trace exponent log_q0(z/(z−h)) = "
          f"{float(swap_exponent):.4f}  (/4 per writhe unit: "
          f"{float(swap_exponent)/4:.4f})")
    print(f"  framework share b_pred/b_total per A: "
          f"{[round(s, 3) for s in fw_share]}")

    # Location verdict: is b carried by the framework side or the AME side?
    fw_dominant = all(abs(p) > abs(a) for p, a in zip(bp, ba))
    ame_dominant = all(abs(a) > abs(p) for p, a in zip(bp, ba))
    if fw_dominant:
        location = ("FRAMEWORK-SIDE: the interface asymmetry in B_pred "
                    "carries |b| — κ is derivable from the canonical trace.")
    elif ame_dominant:
        location = ("AME-SIDE: b is carried by the experimental Coulomb "
                    "asymmetry — deriving κ ≡ deriving the isovector part "
                    "of B_AME (Track-A class), mirroring the H1-refutation "
                    "pattern for the bar-even leading term.")
    else:
        location = ("MIXED: both sides contribute comparably across A — "
                    "κ is a genuine difference coefficient; neither a pure "
                    "word-combinatorics lemma nor purely experimental.")
    print(f"\n  LOCATION: {location}")

    b = WitnessBuilder("kappa-writhe-side-decomposition-probe", output_dir=HERE)
    b.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    b.set_description(
        "Location probe for the writhe coefficient κ = b/4 of the "
        "canonical residual's bar-odd term: exact decomposition "
        "b_total = b_AME − b_pred using the per-member B_pred/B_AME "
        "already recorded in the IMME triplet (A=6,8,10,12) and quartet "
        "(A=9, same-T) witnesses. Answers WHERE κ lives (framework "
        "interface asymmetry z vs z−h, or experimental Coulomb) before "
        "any derivation attempt — the bar-odd analogue of the "
        "2026-06-13 H1 location refutation. Post-processing only; "
        "no fit; not wired.")
    b.add_parameter("q0", fmt(q))
    b.add_parameter("swap_exponent_log_q0_z_over_z_minus_h", fmt(swap_exponent))
    b.add_data("rows", rows)
    b.add_data("framework_share_b_pred_over_b_total",
               [round(s, 4) for s in fw_share])
    b.add_data("location_verdict", location)
    b.add_assertion(
        "b_total_consistent_with_synthesis_band",
        computed=float(sum(bt) / len(bt)),
        expected=-1.75, tolerance=0.15,
        unit="mean b over A=6..12",
        source="2026-06-29-delta-lambda-residual-synthesis.md "
               "(b constant −1.747±0.03; A=9 quartet −1.84)")
    b.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
