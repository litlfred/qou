#!/usr/bin/env python3
"""Probe — ⁴He Model B canonical hyperbolic knot survey.

Per `docs/audits/2026-05-12-1ppb-implementation-plan.md` §P1.E:

    "Suggest: produce a witness `model-b-he4-knot-survey.witness.json`
     that computes τ_M for each candidate above and lists the
     match-to-AME ranking, then present to owner for selection."

Model B encodes a nucleus as a single canonical hyperbolic knot in
the minimum-strand braid group.  For {D, T, ³He} the standing
assignments are 6_2, 8_11, L6a4 respectively (manual historical
volume-match, see `r5_full_canonical_knot_solver.py` HISTORICAL_BENCHMARKS).
⁴He is open.

This probe computes the Markov trace τ_M(β) at q_0 for a panel of
plausible ⁴He Model B candidates, in both Plancherel and
Wenzl-Schur conventions, and ranks them against AME(⁴He) = 28.30 MeV
using the plan's plausibility window τ_M ∈ [0.05, 0.5].

The kernel is the same `tr_M_sdp` used by
`probe_sdp_canonical_paper_formula.py` (Hoefsmit seminormal +
cached `BlockCache`); see memory "low-strand τ_M kernel".

This is a SURVEY witness: it does not select the canonical ⁴He
Model B knot.  Owner input is required to pick from the ranking.

Output: model-b-he4-knot-survey.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from probe_sdp_canonical_paper_formula import tr_M_sdp  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import json


# ── ⁴He Model B candidate knots ──────────────────────────────────────
# All candidates are 3-strand braids (n_0=3).  Braid words are
# SnapPy canonical (or the alternating L6a4 word used elsewhere on
# this branch); see `chirality_braid_average.py` and
# `_deprecated/hyperbolic-knot-db-extended.witness.json`.
#
# Plan §P1.E enumerates three primary candidates:
#   - L6a4 (Borromean) — already used for ³He, risks degenerate assignment
#   - 8_18             — 4-bridge symmetric, 4-fold symmetry matching α
#   - Brunnian 4-link  — matches [+1,-1,+1,-1] sign pattern, no canonical
#                        braid word in hand at the time of this survey
#
# We also include 8_17 (high-volume amphichiral neighbour of 8_18) and
# 10_123 = T(5,2)-like (highest-volume hyperbolic 10-crossing 3-braid
# in the on-disk db) for context.
HE4_CANDIDATES = [
    {
        "name": "L6a4 (Borromean, ³He twin)",
        "n_0": 3,
        "braid_word": [1, -2, 1, -2, 1, -2],
        "crossings": 6,
        "volume": 8.0,            # 8 · Catalan, well-known
        "rationale": (
            "Already used for ³He; included to quantify the "
            "degenerate-assignment risk."
        ),
    },
    {
        "name": "8_17 (high-volume amphichiral)",
        "n_0": 3,
        "braid_word": [-1, 2, -1, -1, 2, 2, -1, 2],
        "crossings": 8,
        "volume": 10.985907606284815,
        "rationale": (
            "Amphichiral neighbour of 8_18 with comparable hyperbolic "
            "volume; included as a control."
        ),
    },
    {
        "name": "8_18 (4-bridge symmetric)",
        "n_0": 3,
        "braid_word": [1, -2, 1, -2, 1, -2, 1, -2],
        "crossings": 8,
        "volume": 12.350906209158198,
        "rationale": (
            "Plan candidate: 4-fold symmetric, hyperbolic volume "
            "≈12.35, structurally compatible with the α-particle "
            "4-fold symmetry."
        ),
    },
    {
        "name": "10_123 (T(5,2)-like, max-volume 3-braid in db)",
        "n_0": 3,
        "braid_word": [-1, 2, -1, 2, -1, 2, -1, 2, -1, 2],
        "crossings": 10,
        "volume": 17.085709482982857,
        "rationale": (
            "Highest-volume hyperbolic 10-crossing 3-braid in the "
            "on-disk db; included as an upper-volume reference point."
        ),
    },
]

# AME 2020 binding for ⁴He (MeV).  Listed in the plan §1 / M0 table.
B_AME_HE4_MEV = 28.30

# Plausibility window from plan §P1.E: τ_M at q_0 should fall in
# [0.05, 0.5] for the candidate to plausibly match the multi-term
# decomposition of B(⁴He).
TAU_M_WINDOW = (0.05, 0.5)


def get_wenzl_table(n_0: int) -> dict | None:
    """Load Wenzl-Schur weights y_λ at q_0 for partitions of n_0."""
    here = Path(__file__).parent
    yw = json.loads((here / "y-lambda-wenzl-witness.json").read_text())
    if str(n_0) not in yw["tables_by_n"]:
        return None
    return {
        tuple(w["partition"]): float(w["y_lambda_numeric"])
        for w in yw["tables_by_n"][str(n_0)]["weights"]
    }


def main() -> None:
    print("=" * 92)
    print("⁴He Model B canonical hyperbolic knot survey")
    print(f"  q_0 = {Q0_FLOAT}   m_e = {M_E_MEV} MeV")
    print(f"  AME(⁴He) = {B_AME_HE4_MEV} MeV")
    print(f"  Plausibility window: τ_M ∈ [{TAU_M_WINDOW[0]}, {TAU_M_WINDOW[1]}]")
    print("=" * 92)
    print()

    rows = []
    for cand in HE4_CANDIDATES:
        n_0 = cand["n_0"]
        bw = cand["braid_word"]
        wenzl = get_wenzl_table(n_0)

        tr_P, tr_W, per_lam = tr_M_sdp(n_0, bw, wenzl)

        # T1 (atomic mass-trace term) under each convention.
        t1_P = M_E_MEV * abs(tr_P)
        t1_W = M_E_MEV * abs(tr_W)

        in_window_P = TAU_M_WINDOW[0] <= abs(tr_P) <= TAU_M_WINDOW[1]
        in_window_W = TAU_M_WINDOW[0] <= abs(tr_W) <= TAU_M_WINDOW[1]

        row = {
            "name": cand["name"],
            "n_0": n_0,
            "braid_word": bw,
            "crossings": cand["crossings"],
            "volume": cand["volume"],
            "tr_M_plancherel": tr_P,
            "tr_M_wenzl_schur": tr_W,
            "abs_tr_M_plancherel": abs(tr_P),
            "abs_tr_M_wenzl_schur": abs(tr_W),
            "T1_plancherel_MeV": t1_P,
            "T1_wenzl_schur_MeV": t1_W,
            "in_window_plancherel": in_window_P,
            "in_window_wenzl_schur": in_window_W,
            "rationale": cand["rationale"],
            "per_lambda": per_lam,
        }
        rows.append(row)

        print(f"  {cand['name']}  (n_0={n_0}, cross={cand['crossings']}, "
              f"vol={cand['volume']:.4f})")
        print(f"    braid = {bw}")
        print(f"    τ_M Plancherel  = {tr_P:>+10.6f}  |τ_M|={abs(tr_P):.6f}  "
              f"T1 = {t1_P:>9.4f} MeV  in_window={in_window_P}")
        print(f"    τ_M Wenzl-Schur = {tr_W:>+10.6f}  |τ_M|={abs(tr_W):.6f}  "
              f"T1 = {t1_W:>9.4f} MeV  in_window={in_window_W}")
        print()

    # Rank by plausibility: prefer candidates in-window under
    # Wenzl-Schur (Markov-invariant, paper-canonical), tie-break by
    # closeness of |τ_M| to the geometric mean of the window.
    import math
    target = math.sqrt(TAU_M_WINDOW[0] * TAU_M_WINDOW[1])

    def rank_key(r: dict) -> tuple:
        return (
            0 if r["in_window_wenzl_schur"] else 1,
            abs(math.log(max(r["abs_tr_M_wenzl_schur"], 1e-30)) - math.log(target)),
        )

    ranking = sorted(rows, key=rank_key)
    print("=" * 92)
    print("RANKING (Wenzl-Schur convention, in-window first, log-distance to "
          f"target |τ_M|≈{target:.4f}):")
    for i, r in enumerate(ranking, 1):
        marker = "✓" if r["in_window_wenzl_schur"] else "✗"
        print(f"  {i}. [{marker}] {r['name']}  |τ_M|={r['abs_tr_M_wenzl_schur']:.6f}  "
              f"T1={r['T1_wenzl_schur_MeV']:.3f} MeV")
    print("=" * 92)
    print("OWNER DECISION REQUIRED: select canonical ⁴He Model B knot from "
          "the ranking above.  The survey is Markov-invariant under "
          "Wenzl-Schur but does not encode any non-trace constraints "
          "(symmetry group, bridge index, chirality compatibility with the "
          "[+1,-1,+1,-1] sign pattern).  See plan §P1.E.")
    print("=" * 92)

    summary = {
        "ranking_wenzl_schur": [
            {
                "rank": i,
                "name": r["name"],
                "abs_tr_M_wenzl_schur": r["abs_tr_M_wenzl_schur"],
                "in_window": r["in_window_wenzl_schur"],
                "T1_wenzl_schur_MeV": r["T1_wenzl_schur_MeV"],
            }
            for i, r in enumerate(ranking, 1)
        ],
        "any_in_window_wenzl_schur": any(r["in_window_wenzl_schur"] for r in rows),
        "any_in_window_plancherel": any(r["in_window_plancherel"] for r in rows),
        "B_AME_he4_MeV": B_AME_HE4_MEV,
        "tau_m_window": list(TAU_M_WINDOW),
    }

    w = (
        WitnessBuilder("model-b-he4-knot-survey", engine="python")
        .set_description(
            "Survey τ_M(β) at q_0 for ⁴He Model B candidate knots "
            "{L6a4, 8_17, 8_18, 10_123} in B_3 under both Plancherel "
            "and Wenzl-Schur Markov-trace conventions, ranked against "
            "AME(⁴He)=28.30 MeV with plausibility window τ_M ∈ "
            "[0.05, 0.5] from the plan §P1.E.  Survey-only — does "
            "not select the canonical knot; owner input required."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", float(Q0_FLOAT))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("B_AME_he4_MeV", B_AME_HE4_MEV)
        .add_parameter("tau_m_window_lower", TAU_M_WINDOW[0])
        .add_parameter("tau_m_window_upper", TAU_M_WINDOW[1])
        .add_data("candidates", rows)
        .add_data("summary", summary)
        .add_caveat(
            "Survey-only.  τ_M is Markov-invariant by construction, but "
            "the plausibility window τ_M ∈ [0.05, 0.5] is heuristic "
            "(plan §P1.E) — derived from the multi-term decomposition "
            "of B(⁴He)=28.30 MeV under the assumption that T1 is one "
            "of several comparable contributions.  No selection is "
            "made by this survey.  The Brunnian 4-component link "
            "candidate enumerated in the plan is not included because "
            "no canonical braid word is in hand at the time of this "
            "survey."
        )
        .add_caveat(
            "All candidates are 3-strand braids.  4-strand candidates "
            "(genuine 4-component links, B_4 hyperbolic knots) would "
            "require extending the Hoefsmit cache to H_4 and the "
            "Wenzl-Schur table is already available at n=4."
        )
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
