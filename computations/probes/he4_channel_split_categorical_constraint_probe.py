#!/usr/bin/env python3
"""he4_channel_split_categorical_constraint_probe.py — Item B of
PR #1688: structural channel-split rule for the ⁴He +5.87% gap.

CONTEXT.
PR #1675 Item 3 verdict: localizing the +5.87% gap to a single
trace-dominant channel ((9,3)) is underdetermined. Σ_λ frac_λ·ρ_F^λ
= ρ_F_req = 1.889 is one equation in many unknowns.

conj:psd-trace-orthogonality (content/quantum-observable-universe/
mass-theory/conj-psd-trace-orthogonality.md) gives a CATEGORICAL
structural constraint: the binding-energy gap lives in the trace-
dominant family (2-row partitions), NOT in PSD-dominant family
(rectangular like (4,4,4), (3,3,3,3)). This pins which channels
can carry ρ_F deviation from the postulated 2.

PROPOSED CATEGORICAL CONSTRAINT (hypothesis to test):

  HC1 (uniform-on-trace-dominant): ρ_F^λ = ρ_F^* for all λ in the
       trace-dominant family (top contributors to tr_M), ρ_F^λ = 2
       for all others. Solve for ρ_F^* such that the y_λ·χ_λ-
       weighted sum gives ρ_F_req = 1.889.

  HC2 (k-channel-localized): ρ_F^λ = ρ_F^* for the top k channels
       (sorted by |y_λ·χ_λ|), 2 elsewhere. Test k = 1, 2, 3, 5, 8.

  HC3 (bar-conjugate-symmetric): ρ_F^λ = ρ_F^{λᵀ} (bar-symmetric
       paired channels share ρ_F^λ value). Tests whether the
       structural bar-involution discipline pins the split.

For each hypothesis, compute the required ρ_F^* and check if it's
a recognizable substrate quantity. Cross-reference with the bar-
involution sign-pattern at A=4 (conj:psd-trace-orthogonality says
(4,4,4) and (3,3,3,3) are bar-paired, with deeper PSD-obstruction
on (3,3,3,3)).

DISCIPLINE. Structural-analysis probe; does NOT propose a new
substrate constant. Verdict identifies which hypothesis (HC1/HC2/
HC3) gives the cleanest structural ρ_F^* (close to 2 with simple
modulation), and reports if NONE work.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1 catch-up, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "he4-channel-split-categorical-constraint-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "⁴He +5.87% channel-split categorical constraint per "
        "conj:psd-trace-orthogonality. Tests 3 hypotheses (HC1/HC2/HC3) "
        "for the structural rule pinning which ρ_F^λ deviate from 2."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-02-yekutieli-A2-qbeta-mn-he4-workplan.md"
    )

    cache_path = _pb.witness_path("chi-helium-4-h12-at-q0-50dps.witness.json", HERE)
    with open(cache_path) as f:
        cache = json.load(f)
    tr_M = mp.mpf(cache["tr_M_at_q0"])
    bp = cache["by_partition"]

    m_e = mp.mpf(str(M_E_MEV))
    A = 4
    G = mp.catalan
    B_AME = mp.mpf("28.295674")
    rho_F_postulated = mp.mpf(2)
    rho_F_required = B_AME / (m_e * A * 8 * G)
    gap_rho_F = rho_F_postulated - rho_F_required

    print("=" * 78)
    print(" ⁴He channel-split categorical constraint probe")
    print("=" * 78)
    print(f"  ρ_F postulated     = {fmt(rho_F_postulated)[:25]}")
    print(f"  ρ_F required       = {fmt(rho_F_required)[:25]}")
    print(f"  gap                = {fmt(gap_rho_F)[:25]}")
    print()

    # Build sorted contribution table
    entries = []
    for p in bp:
        part = tuple(p["partition"])
        y = mp.mpf(p["y_lambda"])
        chi = mp.mpf(p["chi_lambda"])
        contrib = y * chi
        entries.append({
            "partition": part,
            "rows": len(part),
            "y": y,
            "chi": chi,
            "contribution": contrib,
            "fraction": contrib / tr_M,
        })
    entries.sort(key=lambda e: -abs(e["contribution"]))

    # HC1: uniform-on-trace-dominant
    # Sum_λ frac_λ · ρ_F^λ = ρ_F_req
    # If ρ_F^λ = ρ_F^* on trace-dominant, ρ_F^λ = 2 on PSD-dominant
    # frac_TD · ρ_F^* + frac_PSD · 2 = ρ_F_req
    # ρ_F^* = (ρ_F_req - 2 · frac_PSD) / frac_TD
    # Define trace-dominant := 2-row partitions, PSD-dominant := else
    trace_dominant_idx = [i for i, e in enumerate(entries) if e["rows"] <= 2]
    other_idx = [i for i, e in enumerate(entries) if e["rows"] > 2]

    frac_TD = sum(entries[i]["fraction"] for i in trace_dominant_idx)
    frac_other = sum(entries[i]["fraction"] for i in other_idx)
    print(f"HC1: uniform-on-trace-dominant (≤ 2-row partitions)")
    print(f"  trace-dominant fraction of tr_M: {float(frac_TD)*100:.2f}%")
    print(f"  other fraction:                  {float(frac_other)*100:.2f}%")
    rho_F_star_HC1 = (rho_F_required - rho_F_postulated * frac_other) / frac_TD
    print(f"  ρ_F^*(trace-dominant) = "
          f"{fmt(rho_F_star_HC1)[:25]}")
    print(f"  deviation from 2:     "
          f"{float(rho_F_star_HC1 - rho_F_postulated):.6f}")
    print()

    # HC2: top-k localized
    print(f"HC2: top-k channel-localized correction")
    print(f"  {'k':>3} {'top channels':<30} {'fraction':>12} {'ρ_F^* needed':>16}")
    hc2_results = []
    for k in [1, 2, 3, 5, 8]:
        top_k = entries[:k]
        frac_k = sum(e["fraction"] for e in top_k)
        frac_rest = 1 - frac_k
        rho_F_star_k = (rho_F_required - rho_F_postulated * frac_rest) / frac_k
        top_str = ",".join(str(tuple(e["partition"])) for e in top_k)[:30]
        print(f"  {k:>3} {top_str:<30} {float(frac_k)*100:>11.2f}% "
              f"{float(rho_F_star_k):>16.6f}")
        hc2_results.append({
            "k": k,
            "top_partitions": [list(e["partition"]) for e in top_k],
            # No float(): every one of these is mpf all the way from
            # `fmt`-printed working precision above. The casts were at the
            # RECORD site only, so the witness was the one place the
            # precision did not reach.
            "fraction_of_tr_M": frac_k,
            "rho_F_star_required": rho_F_star_k,
            "deviation_from_2": rho_F_star_k - 2,
        })
    print()

    # HC3: bar-conjugate-symmetric pairs
    print(f"HC3: bar-conjugate-symmetric channel pairs")
    # Group entries by conjugate-pair (λ, λᵀ); compute pair-aggregated
    # contributions. (4,4,4) ↔ (3,3,3,3) is the canonical pair at A=4.

    def transpose(p):
        if not p:
            return ()
        rows = len(p)
        max_col = max(p)
        return tuple(sum(1 for r in p if r >= c) for c in range(1, max_col + 1))

    # Pair partitions: skip self-conjugate; track pairs by canonical key
    pair_dict = {}
    self_conjugate = []
    for e in entries:
        part = e["partition"]
        partT = transpose(part)
        if part == partT:
            self_conjugate.append(e)
            continue
        key = tuple(sorted([part, partT]))
        if key not in pair_dict:
            pair_dict[key] = []
        pair_dict[key].append(e)

    print(f"  {'pair (λ, λᵀ)':<40} {'pair fraction':>15} {'individual fracs':<30}")
    print("-" * 90)
    pairs_summary = []
    cached_parts = set(tuple(e["partition"]) for e in entries)
    for key, es in sorted(pair_dict.items(),
                          key=lambda kv: -sum(abs(e["fraction"]) for e in kv[1])):
        pair_frac = sum(e["fraction"] for e in es)
        # Note: pair may have only ONE entry cached (other in missing 53)
        other_in_pair = key[0] if key[0] not in {tuple(e["partition"]) for e in es} else key[1]
        if len(es) == 1:
            note = f"(half-pair; {other_in_pair} not cached)"
        else:
            note = ""
        indiv = ",".join(f"{float(e['fraction']):.4f}" for e in es)
        print(f"  {str(key):<40} {float(pair_frac)*100:>14.2f}% {indiv} {note}")
        pairs_summary.append({
            "pair": [list(p) for p in key],
            "n_cached_in_pair": len(es),
            "fraction_total": pair_frac,
        })
    print()
    print(f"  Self-conjugate (λ = λᵀ): "
          f"{[tuple(e['partition']) for e in self_conjugate]}")
    print()

    # HC3 verdict: if top trace-dominant pairs are exactly the cached
    # half-pairs (the other half being in the missing 53 with near-zero
    # contribution), then the bar-involution paired structure is
    # asymmetric — only one half of each pair carries weight.
    # Such an asymmetry would CONSTRAIN the channel split: ρ_F^λ on
    # the cached half varies; ρ_F^λᵀ on the uncached half stays = 2.

    # Compute: how many top-8 contribution pairs are half-cached?
    top_pair_keys = []
    for e in entries[:8]:
        part = e["partition"]
        partT = transpose(part)
        if part == partT:
            continue
        key = tuple(sorted([part, partT]))
        top_pair_keys.append(key)
    half_cached_count = sum(
        1 for k in set(top_pair_keys)
        if (k[0] in cached_parts) != (k[1] in cached_parts)
    )
    print(f"Top-8 trace-dominant bar-pair status:")
    print(f"  Total distinct pairs in top-8: {len(set(top_pair_keys))}")
    print(f"  Half-cached (asymmetric) pairs: {half_cached_count}")
    print()

    # Verdict
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if half_cached_count == len(set(top_pair_keys)):
        verdict = (
            f"HC3 STRUCTURAL CONSTRAINT IDENTIFIED — all {half_cached_count} "
            f"top trace-dominant bar-pairs are HALF-CACHED: only one of "
            f"(λ, λᵀ) appears in the trace-dominant family, the other "
            f"is in the uncached 53-partition tail (contribution ≤ 4e-51 "
            f"by PR #1675 Probe 2 accounting). This bar-asymmetric "
            f"distribution is the CATEGORICAL CONSTRAINT that pins the "
            f"channel split:\n\n"
            f"  RULE: ρ_F^λ varies on cached trace-dominant partitions; "
            f"ρ_F^λᵀ = 2 on uncached bar-paired transposes.\n\n"
            f"Under HC1 (uniform-on-trace-dominant), ρ_F^* = "
            f"{float(rho_F_star_HC1):.6f} (deviation "
            f"{float(rho_F_star_HC1 - 2):.4f} from 2). Whether this "
            f"value has a substrate identification needs a separate "
            f"PSLQ / categorical-derivation probe."
        )
    else:
        verdict = (
            f"HC3 MIXED — only {half_cached_count}/{len(set(top_pair_keys))} "
            f"top-8 pairs are half-cached. The bar-involution structure "
            f"does NOT cleanly pin the channel split via half-pair "
            f"asymmetry alone. Under HC1, ρ_F^* = "
            f"{float(rho_F_star_HC1):.6f} on trace-dominant. Further "
            f"categorical constraints needed (e.g. Plancherel weight "
            f"hierarchy, or bar-symmetric vs bar-antisymmetric sector "
            f"discrimination)."
        )
    print(verdict)
    print()

    builder.add_data("rho_F_postulated", rho_F_postulated)
    builder.add_data("rho_F_required", rho_F_required)
    builder.add_data("gap_rho_F", gap_rho_F)
    builder.add_data("HC1_uniform_trace_dominant", {
        "trace_dominant_fraction": frac_TD,
        "rho_F_star": rho_F_star_HC1,
        "deviation_from_2": rho_F_star_HC1 - 2,
    })
    builder.add_data("HC2_top_k_localized", hc2_results)
    builder.add_data("HC3_bar_pairs", pairs_summary)
    builder.add_data("HC3_top_8_pair_half_cached_count", half_cached_count)
    builder.add_data("HC3_top_8_distinct_pairs",
                     len(set(top_pair_keys)))
    builder.add_data("self_conjugate_partitions_cached",
                     [list(e["partition"]) for e in self_conjugate])
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        name="rho_F_required_matches_AME_he4",
        computed=abs(float(rho_F_required) - 1.8892) < 1e-3,
        expected=True,
        tolerance=mp.mpf(0),
        source="B_AME / (m_e · 4 · 8G)",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
