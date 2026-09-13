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

Cited values (prop:he4-two-row-dominance), against the chi cache as
regenerated 2026-09-06 (qou-92u9, owner ruling "regen"):
    tr_M(β_⁴He)(q_0) = 0.0112374176598
    top-5 binding-receptive blocks by |c_λ| (all in Λ²(12)):
        (12) 85.398%, (9,3) 64.406%, (11,1) -40.890%,
        (8,4) -31.659%, (10,2) 11.461%
        top-5 cumulative: 233.814% of |tr_M| by MAGNITUDE,
                           88.715% SIGNED  -- see below, they differ now
    also in the stratum: (6,6) 8.652%, (7,5) 2.633%
    sign rep (1¹²) vanishes
    formal claim: two-row stratum ratio ≥ 0.80 (computed: exactly 1).

SUPERSEDED, kept because the gap is the point (pre-2026-09-06 cache):
tr_M = 0.160974145442, a factor R_quark = 14.3248 above the current
value; (9,3) 29.0%, (8,4) 23.6%, (10,2) 13.5%, (7,5) 10.3%,
(11,1) 10.2%; top-5 cumulative 91.130%; trivial rep 5.962%. Two
contributions have since flipped SIGN ((11,1) and (8,4)), and the
trivial rep went from 5.962% to leading the ranking at 85.398%.

NOTE on "86.6%": that proposition headline figure belongs to the same
superseded generation and no longer names anything computed here. The
two-row stratum ratio is now exactly 1, and the top-5 cumulative has
split into two distinct quantities -- the producer sums MAGNITUDES
(233.814%) while the block's table rows are SIGNED (88.715%). While
every block was positive the two coincided at 91.130 and nothing named
the difference; two blocks are now negative and they do not. Both are
emitted, under distinct names. Bean qou-85wn.

NOTE on "two-row": IsTwoRow is `length ≤ 2`, so the ONE-row partition
(12) is in Λ²(12). "All top-5 are two-row" is true with (12) leading;
it is not a claim that the trivial rep was excluded.

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
#
# CORRECTED 2026-08-23 (bean qou-bm4i). These held the block's ORIGINAL table,
# which this producer then contradicted on every row -- allPassed had been
# false since the witness was first written, while the block carried
# `computation.status: "verified"` and nothing compared the two.
#
# This is NOT re-baselining a red run green. The diagnosis was checked first:
# re-running reproduces the committed witness byte-for-byte, the Hoefsmit
# characters chi^lambda AGREE with the old table to 3+ digits, and only
# y_lambda differed -- by a NON-UNIFORM factor (2.66 to 4.04), so a different
# weight formula, not a normalisation. Per AGENTS.md the three weight families
# y_lambda / w_lambda / w~_lambda are distinct at q != 1 and must not be
# conflated; the old table appears to have used another one under the y_lambda
# label. The block's prose was corrected to the computed values, and these
# constants track the block, so the cross-check stays live for future drift.
# REGENERATED 2026-09-06 (beans qou-85wn / qou-92u9). The
# intra-nucleon confinement core of `atom_braid_word_3A` went from
# GROUPED to alternating (`intra_order="borromean"`) on the
# 2026-09-05 owner ruling (bean qou-hu1f), and the chi cache was
# regenerated under the follow-up ruling. The trace fell by exactly
# the 4He factor R_quark = 14.3248; two blocks flipped sign; the
# ordering changed. The stratum ratio is unchanged (exactly 1) and
# so is y_lambda, which depends only on the partition and q.
# Superseded generations, so a reader meeting them can date them:
#   pre-2026-08-23  (9,3) 29.0  (8,4) 23.6  (10,2) 13.5 ... ratio 86.6 %
#   2026-08-23      (9,3) 29.617 (8,4) 22.452 (10,2) 15.407 ... ratio 1
# All seven nonzero blocks are listed now, not six.
CITED_PCT = {
    (12,): 85.398,
    (9, 3): 64.406,
    (11, 1): -40.890,
    (8, 4): -31.659,
    (10, 2): 11.461,
    (6, 6): 8.652,
    (7, 5): 2.633,
}
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# The two cumulatives are DIFFERENT QUANTITIES since 2026-09-05
# (they coincided at 91.130 while every block was positive).
CITED_TOP5_ABS_PCT = mp.mpf("233.814")     # sum of |c_lambda|
CITED_TOP5_SIGNED_PCT = mp.mpf("88.715")   # sum of the table rows
CITED_TR_M = mp.mpf("0.011237417659767421564199549374410607269662696081262")


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
        "|tr_M|. Reproduces tr_M = 0.0112374176598, the top-5 "
        "binding-receptive blocks by |c_λ| (all in Λ²(12), which is "
        "length ≤ 2 and so contains the one-row (12)): (12) 85.398%, "
        "(9,3) 64.406%, (11,1) -40.890%, (8,4) -31.659%, "
        "(10,2) 11.461%; top-5 cumulative 233.814% by magnitude and "
        "88.715% signed -- distinct since two blocks went negative. "
        "The sign rep (1¹²) vanishes, and the two-row stratum ratio is "
        "exactly 1, satisfying the ≥ 80% claim of "
        "prop:he4-two-row-dominance. Superseded pre-2026-09-06 figures "
        "(tr_M 0.160974145442, trivial rep 5.96%, top-5 cum 91.1%) are "
        "recorded in the producer docstring; bean qou-85wn."
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
            signed_pct = v["contribution"] / abs_tr_M * 100
            per_block.append({
                "partition": list(part),
                "dim": v["dim"],
                "y_lambda": mp.nstr(v["y_lambda"], 8),
                "chi_lambda": mp.nstr(v["chi_lambda"], 8),
                "contribution": mp.nstr(v["contribution"], 12),
                "pct_of_abs_tr_M": float(pct),
                # SIGNED share. Identical to the line above until the
                # 2026-09-05 intra-ordering ruling, because every block
                # was positive; two are now negative, so the two figures
                # diverge and the content block's table shows THIS one
                # (bean qou-85wn).
                "signed_pct_of_abs_tr_M": mp.nstr(signed_pct, 8),
                "is_two_row": part in set(TWO_ROW),
            })

        # Top-5 cumulative (the headline "86.6%" figure).
        top5 = ranked[:5]
        top5_sum = mp.fsum(abs(v["contribution"]) for _, v in top5)
        top5_cum_pct = top5_sum / abs_tr_M * 100
        # The SIGNED cumulative, which is what summing the content
        # block's table rows gives. The two agreed exactly (91.130)
        # while every block was positive; post-2026-09-05 they are
        # 233.814 (absolute) against 88.715 (signed). Emitting one
        # alone would make the block and its own producer disagree
        # by a factor of 2.6 with nothing naming the difference.
        top5_signed_sum = mp.fsum(v["contribution"] for _, v in top5)
        top5_signed_cum_pct = top5_signed_sum / abs_tr_M * 100
        top5_all_two_row = all(p in set(TWO_ROW) for p, _ in top5)

        # Trivial and sign rep.
        trivial_pct = abs(by_part[(12,)]["contribution"]) / abs_tr_M * 100
        sign_part = tuple([1] * 12)
        sign_contrib = abs(by_part.get(sign_part, {}).get(
            "contribution", mp.mpf(0)))

        print(f"  tr_M(β_⁴He)(q_0)      = {mp.nstr(tr_M, 12)}  "
              f"[cited {mp.nstr(CITED_TR_M, 12)}]")
        print(f"  |tr_M|                 = {mp.nstr(abs_tr_M, 12)}")
        print(f"  two-row stratum sum    = {mp.nstr(two_row_sum, 12)}")
        print(f"  two-row stratum ratio  = {mp.nstr(two_row_ratio, 8)} "
              f"(full Λ²; ≥0.80 claim)")
        print(f"  top-5 cumulative |.|   = {mp.nstr(top5_cum_pct, 6)}%  "
              f"[cited {float(CITED_TOP5_ABS_PCT)}%]  "
              f"(all two-row: {top5_all_two_row})")
        print(f"  top-5 cumulative signed= "
              f"{mp.nstr(top5_signed_cum_pct, 6)}%  "
              f"[cited {float(CITED_TOP5_SIGNED_PCT)}%]")
        print(f"  trivial rep (12)       = {mp.nstr(trivial_pct, 4)}%  "
              f"[cited {float(CITED_PCT[(12,)])}%]")
        print(f"  sign rep (1¹²)         = {mp.nstr(sign_contrib, 4)}  "
              f"[cited 0]")
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
        w.add_data("top5_signed_cumulative_pct",
                   mp.nstr(top5_signed_cum_pct, 12))
        w.add_data("top5_all_two_row", top5_all_two_row)
        w.add_data("trivial_rep_pct", float(trivial_pct))
        w.add_data("sign_rep_abs_contribution", float(sign_contrib))
        w.add_data("per_block_ranked", per_block)

        # ── Cross-check assertions vs cited values ────────────────
        w.add_assertion(
            name="tr_M_at_q0",
            computed=abs_tr_M,
            expected=CITED_TR_M,
            tolerance=5e-7,
            source=(
                "prop:he4-two-row-dominance cites tr_M(β_⁴He)(q_0) = "
                "0.0112374176598 (canonical Markov trace, Σ_{λ⊢12} y_λ "
                "χ^λ), re-pinned to the 2026-09-06 chi regeneration "
                "(qou-92u9); the pre-regeneration 0.160974145442 was a "
                "factor R_quark = 14.3248 higher"
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
            computed=top5_cum_pct,
            expected=CITED_TOP5_ABS_PCT,
            tolerance=0.2,
            source=(
                "prop:he4-two-row-dominance: the five blocks of largest "
                "|c_lambda|, summed in MAGNITUDE. Not the figure the "
                "block's table adds up to -- see the signed assertion "
                "below (bean qou-85wn)."
            ),
        )
        w.add_assertion(
            name="top5_signed_cumulative_pct",
            computed=top5_signed_cum_pct,
            expected=CITED_TOP5_SIGNED_PCT,
            tolerance=0.2,
            source=(
                "prop:he4-two-row-dominance: 'The five blocks of "
                "largest magnitude sum to 88.715%.' This is the sum of "
                "the block's table ROWS, which are signed; two are "
                "negative since the 2026-09-05 intra-ordering ruling."
            )
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
            computed=trivial_pct,
            expected=85.398,
            tolerance=0.15,
            source=("prop:he4-two-row-dominance: trivial rep (12) "
                    "85.398% -- it LEADS the ranking post-regeneration; "
                    "the ~2.9% this cited is pre-2026-09-06"),
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
            # SIGNED, matching the content block's table. `abs` here
            # would silently pass a sign flip -- and two blocks flipped
            # on 2026-09-05 (bean qou-85wn).
            pct = v["contribution"] / abs_tr_M * 100
            w.add_assertion(
                name=f"pct_block_{'_'.join(map(str, part))}",
                computed=pct,
                expected=cited,
                tolerance=0.15,
                source=(
                    f"prop:he4-two-row-dominance table: λ={part} carries "
                    f"{cited}% of |tr_M| (signed)"
                ),
            )

    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("helium-4"))

    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
