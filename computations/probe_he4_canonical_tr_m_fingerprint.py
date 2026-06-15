#!/usr/bin/env python3
# polynomial_q_not_applicable: consumes the pre-computed numerical
# χ^λ(β_⁴He) cache at q_0 (50 dps) and forms the two-row stratum
# ratio; no q-polynomial / symbolic arithmetic of its own.
"""⁴He two-row Wedderburn-stratum dominance of the canonical tr_M.

Emits `he4-canonical-tr-m-block-fingerprint.witness.json` for
`prop:he4-two-row-dominance`.

Reads the per-partition contributions c_λ(q_0) = y_λ(q_0)·χ^λ_q(β_⁴He)
from the full 77-partition numerical Hoefsmit cache
`chi-helium-4-h12-at-q0-50dps.witness.json` (produced by
`chi_at_q0_via_hoefsmit_mpfr.py helium-4`, 50 dps), where β_⁴He =
`atom_braid_word_3A(2, 2)` is the canonical ⁴He atomic braid on
H_12(q) (47 crossings, 3 interfaces: pp@gen2, pn@gen5, nn@gen8).

The Markov trace is the full sum tr_M(β_⁴He)(q_0) = Σ_{λ⊢12} c_λ.
The two-row stratum (def:two-row-stratum)

    Λ²(12) = {(12),(11,1),(10,2),(9,3),(8,4),(7,5),(6,6)}

carries the fraction

    |Σ_{λ ∈ Λ²(12)} c_λ| / |tr_M(β_⁴He)|.

Cited values (prop:he4-two-row-dominance):
    tr_M(β_⁴He)(q_0) = 0.05534835
    top-5 binding-receptive blocks (all two-row):
        (9,3) 29.0%, (8,4) 23.6%, (10,2) 13.5%, (7,5) 10.3%, (11,1) 10.2%
        top-5 cumulative = 86.5%
    trivial rep (12) = 2.9%; sign rep (1¹²) sub-1e-9
    formal claim: two-row stratum ratio ≥ 0.80.

NOTE on "86.6%": the proposition headline figure 86.6% is the TOP-5
cumulative (= 86.5% here); the FULL 7-member two-row stratum Λ²(12)
ratio is ~92.7%. Both satisfy the ≥ 80% claim. This witness records
both the full-stratum ratio and the top-5 cumulative explicitly.

Upstream: `chi-helium-4-h12-at-q0-50dps.witness.json` (must be
complete — 77/77 partitions, partial=false).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from partition_utils import hook_lengths  # noqa: E402
from q_parameter import Q as Q_0_FLOAT  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
import math  # noqa: E402

UPSTREAM = "chi-helium-4-h12-at-q0-50dps.witness.json"

# Λ²(12): partitions of 12 with at most two parts (def:two-row-stratum).
TWO_ROW = [
    (12,), (11, 1), (10, 2), (9, 3), (8, 4), (7, 5), (6, 6),
]

# Cited per-block percentages (prop:he4-two-row-dominance table).
CITED_PCT = {
    (9, 3): 29.0,
    (8, 4): 23.6,
    (10, 2): 13.5,
    (7, 5): 10.3,
    (11, 1): 10.2,
    (12,): 2.9,
}
CITED_TR_M = mp.mpf("0.05534835")


def main() -> int:
    set_compute_dps(50)

    w = WitnessBuilder(
        "he4-canonical-tr-m-block-fingerprint",
        engine="python+mpmath",
    )
    w.set_description(
        "⁴He two-row Wedderburn-stratum dominance of the canonical "
        "Markov trace. Sums the per-partition contributions c_λ = "
        "y_λ(q_0)·χ^λ_q(β_⁴He) over the full 77 partitions of 12 "
        "(canonical word atom_braid_word_3A(2,2), 50 dps Hoefsmit), "
        "and forms the two-row stratum ratio |Σ_{λ∈Λ²(12)} c_λ| / "
        "|tr_M|. Reproduces tr_M = 0.05534835, the top-5 binding-"
        "receptive blocks (all two-row: (9,3) 29.0%, (8,4) 23.6%, "
        "(10,2) 13.5%, (7,5) 10.3%, (11,1) 10.2%; top-5 cum 86.5%), "
        "the trivial-rep 2.9% and sub-1e-9 sign rep, and verifies the "
        "two-row stratum ≥ 80% claim of prop:he4-two-row-dominance."
    )
    w.set_content_block("prop:he4-two-row-dominance")

    body = w.add_upstream(HERE / UPSTREAM)

    if body.get("partial", False):
        n_done = len(body.get("by_partition", []))
        print(f"  ✗ Upstream cache is PARTIAL ({n_done}/77 partitions). "
              f"Run `python3 chi_at_q0_via_hoefsmit_mpfr.py helium-4` to "
              f"complete it before producing this witness.")
        return 2

    # The chi-cache upstream was slimmed to {partition, chi_lambda} per
    # entry (the dim / y_lambda / contribution fields were derivable and
    # dropped in a schema slim-down). Recompute them here:
    #   dim          = f^λ via the hook-length formula (exact integer)
    #   y_lambda     = Wenzl weight at q_0 (50-dps precomputed hot path
    #                  in wedderburn_jones_markov.y_lambda_at)
    #   contribution = y_λ(q_0) · χ^λ_q(β_⁴He)   (Frobenius pairing)
    n_strands = 12
    y_at_q0 = y_lambda_at(n_strands, Q_0_FLOAT)
    fact_n = math.factorial(n_strands)

    with mp.workdps(50):
        by_part = {}
        for entry in body["by_partition"]:
            part = tuple(entry["partition"])
            hooks = hook_lengths(part)
            dim = fact_n // math.prod(hooks)
            y_lam = mp.mpf(str(y_at_q0[part]))
            chi_lam = mp.mpf(entry["chi_lambda"])
            by_part[part] = {
                "dim": dim,
                "y_lambda": y_lam,
                "chi_lambda": chi_lam,
                "contribution": y_lam * chi_lam,
            }

        n_parts = len(by_part)
        if n_parts != 77:
            print(f"  ✗ Expected 77 partitions, cache has {n_parts}. Abort.")
            return 2

        # Full Markov trace = Σ_λ c_λ.
        tr_M = mp.fsum(v["contribution"] for v in by_part.values())
        abs_tr_M = abs(tr_M)

        # Two-row stratum numerator.
        two_row_sum = mp.fsum(
            by_part[p]["contribution"] for p in TWO_ROW if p in by_part
        )
        missing_two_row = [p for p in TWO_ROW if p not in by_part]
        if missing_two_row:
            print(f"  ✗ Missing two-row partitions in cache: "
                  f"{missing_two_row}. Abort.")
            return 2
        two_row_ratio = abs(two_row_sum) / abs_tr_M

        # Per-block percentages of |tr_M|, ranked.
        ranked = sorted(
            by_part.items(),
            key=lambda kv: abs(kv[1]["contribution"]),
            reverse=True,
        )
        per_block = []
        for part, v in ranked:
            pct = abs(v["contribution"]) / abs_tr_M * 100
            per_block.append({
                "partition": list(part),
                "dim": v["dim"],
                "y_lambda": mp.nstr(v["y_lambda"], 8),
                "chi_lambda": mp.nstr(v["chi_lambda"], 8),
                "contribution": mp.nstr(v["contribution"], 12),
                "pct_of_abs_tr_M": float(pct),
                "is_two_row": part in set(TWO_ROW),
            })

        # Top-5 cumulative (the headline "86.6%" figure).
        top5 = ranked[:5]
        top5_sum = mp.fsum(abs(v["contribution"]) for _, v in top5)
        top5_cum_pct = top5_sum / abs_tr_M * 100
        top5_all_two_row = all(p in set(TWO_ROW) for p, _ in top5)

        # Trivial and sign rep.
        trivial_pct = abs(by_part[(12,)]["contribution"]) / abs_tr_M * 100
        sign_part = tuple([1] * 12)
        sign_contrib = abs(by_part.get(sign_part, {}).get(
            "contribution", mp.mpf(0)))

        print(f"  tr_M(β_⁴He)(q_0)      = {mp.nstr(tr_M, 12)}  "
              f"[cited 0.05534835]")
        print(f"  |tr_M|                 = {mp.nstr(abs_tr_M, 12)}")
        print(f"  two-row stratum sum    = {mp.nstr(two_row_sum, 12)}")
        print(f"  two-row stratum ratio  = {mp.nstr(two_row_ratio, 8)} "
              f"(full Λ²; ≥0.80 claim)")
        print(f"  top-5 cumulative       = {mp.nstr(top5_cum_pct, 6)}%  "
              f"[cited 86.5%]  (all two-row: {top5_all_two_row})")
        print(f"  trivial rep (12)       = {mp.nstr(trivial_pct, 4)}%  "
              f"[cited 2.9%]")
        print(f"  sign rep (1¹²)         = {mp.nstr(sign_contrib, 4)}  "
              f"[cited sub-1e-9]")
        print()
        print("  Top-5 binding-receptive blocks:")
        for part, v in top5:
            pct = abs(v["contribution"]) / abs_tr_M * 100
            print(f"    {str(part):<10} dim={v['dim']:>4}  "
                  f"c_λ={mp.nstr(v['contribution'], 6):>14}  "
                  f"{float(pct):5.1f}%")

        # ── Witness data ──────────────────────────────────────────
        w.add_parameter("q_0", body.get("q_0_50dps"))
        w.add_parameter("Z", 2)
        w.add_parameter("N", 2)
        w.add_parameter("A", 4)
        w.add_parameter("n_strands", 12)
        w.add_parameter("n_partitions", n_parts)
        w.add_parameter("dps", 50)
        w.add_parameter(
            "canonical_word", "atom_braid_word_3A(2, 2) — 47 crossings, "
            "interfaces pp@gen2 pn@gen5 nn@gen8")
        w.add_parameter(
            "two_row_stratum",
            [list(p) for p in TWO_ROW])

        w.add_data("tr_M_at_q0", mp.nstr(tr_M, 30))
        w.add_data("abs_tr_M_at_q0", mp.nstr(abs_tr_M, 30))
        w.add_data("two_row_stratum_sum", mp.nstr(two_row_sum, 30))
        w.add_data("two_row_stratum_ratio", float(two_row_ratio))
        w.add_data("top5_cumulative_pct", float(top5_cum_pct))
        w.add_data("top5_all_two_row", top5_all_two_row)
        w.add_data("trivial_rep_pct", float(trivial_pct))
        w.add_data("sign_rep_abs_contribution", float(sign_contrib))
        w.add_data("per_block_ranked", per_block)

        # ── Cross-check assertions vs cited values ────────────────
        w.add_assertion(
            name="tr_M_at_q0",
            computed=float(abs_tr_M),
            expected=float(CITED_TR_M),
            tolerance=5e-7,
            source=(
                "prop:he4-two-row-dominance cites tr_M(β_⁴He)(q_0) = "
                "0.05534835 (canonical Markov trace, Σ_{λ⊢12} y_λ χ^λ)"
            ),
        )
        # Record the ≥ 0.80 claim as a 0/1 boolean assertion (a bare
        # equality check on the ratio would false-fail; the formal
        # claim is an inequality, so we assert the inequality holds).
        w.add_assertion(
            name="two_row_stratum_ge_80pct",
            computed=1 if two_row_ratio >= mp.mpf("0.80") else 0,
            expected=1,
            tolerance=0,
            source=(
                f"prop:he4-two-row-dominance formal claim: two-row "
                f"stratum ratio ≥ 0.80 (computed {float(two_row_ratio):.4f})"
            ),
        )
        w.add_assertion(
            name="top5_cumulative_pct",
            computed=float(top5_cum_pct),
            expected=86.5,
            tolerance=0.2,
            source=(
                "prop:he4-two-row-dominance: top-5 binding-receptive "
                "blocks carry 86.5% cumulative (the headline 86.6% "
                "figure)"
            ),
        )
        w.add_assertion(
            name="top5_all_two_row",
            computed=1 if top5_all_two_row else 0,
            expected=1,
            tolerance=0,
            source="all top-5 binding-receptive blocks lie in Λ²(12)",
        )
        w.add_assertion(
            name="trivial_rep_pct",
            computed=float(trivial_pct),
            expected=2.9,
            tolerance=0.15,
            source="prop:he4-two-row-dominance: trivial rep (12) ~ 2.9%",
        )
        w.add_assertion(
            name="sign_rep_sub_1e9",
            computed=1 if sign_contrib < mp.mpf("1e-9") else 0,
            expected=1,
            tolerance=0,
            source="prop:he4-two-row-dominance: sign rep (1¹²) sub-1e-9",
        )
        # Per-block percentage cross-checks (cited table).
        for part, cited in CITED_PCT.items():
            v = by_part[part]
            pct = abs(v["contribution"]) / abs_tr_M * 100
            w.add_assertion(
                name=f"pct_block_{'_'.join(map(str, part))}",
                computed=float(pct),
                expected=cited,
                tolerance=0.15,
                source=(
                    f"prop:he4-two-row-dominance table: λ={part} carries "
                    f"{cited}% of |tr_M|"
                ),
            )

    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("helium-4"))

    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
