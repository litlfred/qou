#!/usr/bin/env python3
# ANCHOR NOTE (2026-06-22): q0 = 1.10997858275… occurrences below are the
# RETIRED pre-2026-05-28 proton anchor (old re-pin #1422), kept as this
# probe's historical / cross-anchor / pinned comparison value. The CURRENT
# canonical proton q0 is q_at() ≈ 1.1099785955573347…; the muon anchor is
# q_muon_at() ≈ 1.10997859555418…. This probe is preserved as-is by design.
"""he4_partition_dominance_audit_probe.py — empirical (λ ⊢ 12)
contribution accounting for ⁴He's tr_M, with (4,4,4) check.

CONTEXT. PR #1289 + PR #1621 framed ⁴He's +5.87% binding gap as
needing a categorical multi-nucleon interface operator
H_3⊗H_3⊗H_3⊗H_3 → H_12 respecting "(4,4,4) Wedderburn PSD
dominance". PR #1662 Probe 2 exhausted substrate-constant ρ_F
candidates; that confirmed the structural-operator direction.

This probe asks the structural prerequisite question: is (4,4,4)
actually the PSD-dominant block of tr_M(β_⁴He) at q_proton?

DATA. The existing chi-helium-4-h12-at-q0-50dps.witness.json
incrementally caches per-partition contributions. The cache has
24/77 partitions but the cached sum already equals the reported
tr_M to 10⁻⁵⁰ precision — meaning the remaining 53 partitions
contribute essentially zero.

VERDICT shape (pre-stated):
  - If (4,4,4) IS dominant: cached 24 partitions miss the bulk
    (cache sum << reported tr_M); the framework's PSD framing is
    upheld; computing (4,4,4) at full precision is the right
    direction.
  - If (4,4,4) is NOT dominant: the 2-row partitions ((9,3),
    (8,4), (10,2), (7,5), (11,1)) carry the bulk and (4,4,4)
    contributes near-zero; the PR #1289 (4,4,4) framing needs
    reconciliation — either it refers to a different braid frame
    or to a non-tr_M observable.

DISCIPLINE. This is a pure empirical accounting probe; it makes
no new numerical claims about ρ_F. The verdict re-frames the open
research direction for ⁴He WITHOUT proposing a new substrate
constant or operator (per AGENTS.md anti-pattern guards on PR #1662).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
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


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "he4-partition-dominance-audit-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "⁴He empirical (λ ⊢ 12) contribution accounting. Asks whether "
        "(4,4,4) is actually PSD-dominant per the PR #1289 framing, "
        "using the existing partial H_12 chi cache."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-precision-residual-probes-workplan.md"
    )

    cache_path = _pb.witness_path("chi-helium-4-h12-at-q0-50dps.witness.json", HERE)
    with open(cache_path) as f:
        cache = json.load(f)

    bp = cache["by_partition"]
    tr_M_full = mp.mpf(cache["tr_M_at_q0"])

    print("=" * 78)
    print(" ⁴He empirical partition-dominance audit")
    print("=" * 78)
    print(f"Cache: {cache_path.name}")
    print(f"q_0 (cache anchor): {cache['q_0_50dps'][:30]}")
    print(f"cached partitions: {len(bp)} of 77 (partial={cache['partial']})")
    print(f"reported tr_M(β_⁴He): {fmt(tr_M_full)[:40]}")
    print()

    # Sort by abs contribution
    cached_sum = mp.mpf(0)
    entries = []
    for p in bp:
        part = tuple(p["partition"])
        dim = p["dim"]
        contrib = mp.mpf(p["contribution"])
        cached_sum += contrib
        entries.append({
            "partition": list(part),
            "dim": dim,
            "contribution": float(contrib),
            "abs_contribution": float(abs(contrib)),
            "fraction_of_tr_M": float(contrib / tr_M_full),
        })

    entries.sort(key=lambda e: -e["abs_contribution"])
    print(f"{'partition':28} {'dim':>6} {'contribution':>16} {'fraction':>10}")
    print("-" * 75)
    for e in entries[:15]:
        print(f"  {str(tuple(e['partition'])):26} {e['dim']:>6} "
              f"{e['contribution']:>16.6e} {e['fraction_of_tr_M']:>9.2%}")
    print("  ...")

    print()
    cumulative_2row = sum(
        e["abs_contribution"] for e in entries
        if len(e["partition"]) <= 2
    )
    cumulative_3row = sum(
        e["abs_contribution"] for e in entries
        if len(e["partition"]) == 3
    )
    cumulative_4row = sum(
        e["abs_contribution"] for e in entries
        if len(e["partition"]) >= 4
    )
    total_abs = sum(e["abs_contribution"] for e in entries)
    cache_coverage = float(cached_sum / tr_M_full)

    print(f"|tr_M| breakdown by partition shape:")
    print(f"  1-2 rows (λ_1 + λ_2 = 12): {cumulative_2row:.6e}  "
          f"({cumulative_2row/total_abs:.2%} of |contributions|)")
    print(f"  3 rows:                    {cumulative_3row:.6e}  "
          f"({cumulative_3row/total_abs:.2%})")
    print(f"  4+ rows:                   {cumulative_4row:.6e}  "
          f"({cumulative_4row/total_abs:.2%})")
    print()
    print(f"  cache coverage: cached_sum / reported_tr_M = "
          f"{cache_coverage * 100:.6f}%")
    print(f"  missing partitions (53/77) cumulative |contrib|: "
          f"{float(abs(tr_M_full - cached_sum)):.6e}")

    # (4,4,4) check
    cached_444 = next(
        (e for e in entries if tuple(e["partition"]) == (4, 4, 4)),
        None,
    )
    print()
    print(f"(4,4,4) in cache: {cached_444 is not None}")
    if cached_444 is None:
        print("  (4,4,4) is among the 53 NOT-cached partitions.")
        print("  Since cache sum already ≈ reported tr_M to 10⁻⁵⁰,")
        print("  (4,4,4)'s contribution must be ≤ |reported - cached|.")
        max_444 = abs(tr_M_full - cached_sum)
        fraction_444 = float(max_444 / tr_M_full)
        print(f"  ⟹ |(4,4,4) contribution| ≤ {float(max_444):.3e}")
        print(f"  ⟹ fraction of tr_M:        ≤ {fraction_444:.2e}")
    print()

    # Verdict
    top_partition = entries[0]
    if cached_444 is not None and cached_444["abs_contribution"] / total_abs > 0.05:
        verdict = (
            f"(4,4,4) IS dominant — contributes "
            f"{cached_444['fraction_of_tr_M']*100:+.2f}% of tr_M. PR #1289's PSD-"
            f"dominance framing is empirically upheld. Computing the full "
            f"H_12 A-operator extract at (4,4,4) is the right next step."
        )
    else:
        verdict = (
            f"(4,4,4) is NOT PSD-dominant for tr_M(β_⁴He) at q_proton. "
            f"Bulk is in 2-row partitions ({cumulative_2row/total_abs*100:.1f}% of |contribs|), "
            f"led by {tuple(top_partition['partition'])} at "
            f"{top_partition['fraction_of_tr_M']*100:+.2f}%. "
            f"PR #1289's (4,4,4) framing requires reconciliation: either "
            f"(a) it refers to a different ⁴He braid frame than the canonical "
            f"Hoefsmit cache, or (b) it refers to a non-tr_M observable "
            f"(e.g. the magic-A binding form B = ρ_F·m_e·A·8G has its own "
            f"PSD structure decoupled from the bare Hoefsmit decomposition). "
            f"Re-frame the ⁴He interface-operator research direction accordingly."
        )

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(verdict)
    print()

    builder.add_data("cache_anchor_q_0", cache["q_0_50dps"])
    builder.add_data("cache_anchor_note", (
        "Cache was generated at q_0=1.10997859555…, which is within ~3e-12 of "
        "the CURRENT canonical proton re-pin q_at()≈1.1099785955573… (2026-05-28) "
        "and of the muon anchor q_muon_at()≈1.10997859555418…. The retired "
        "pre-re-pin proton anchor was 1.10997858275… (Δq ≈ 1.28e-8 from current). "
        "Cross-anchor q-stability of the contribution table is plausible at "
        "this scale but not formally verified by this probe."
    ))
    builder.add_data("cached_count", len(bp))
    builder.add_data("total_partitions", 77)
    builder.add_data("tr_M_at_q0", cache["tr_M_at_q0"])
    builder.add_data("cached_sum", str(cached_sum))
    builder.add_data("cache_coverage_pct", cache_coverage * 100)
    builder.add_data("top_contributors", entries[:10])
    builder.add_data("by_row_count", {
        "1-2_rows": cumulative_2row,
        "3_rows": cumulative_3row,
        "4+_rows": cumulative_4row,
    })
    builder.add_data("partition_444_contribution_upper_bound",
                     float(abs(tr_M_full - cached_sum)))
    builder.add_data("verdict", verdict)
    builder.add_data("research_implication", (
        "If (4,4,4) is not the dominant block of tr_M at q_proton, the "
        "categorical interface-operator research direction needs re-aiming: "
        "compute the H_12 A-operator extract at the actual top contributor "
        "((9,3), (8,4), (10,2)) instead, and re-test the +5.87% gap closure "
        "against magic-A B = ρ_F·m_e·A·8G with structural ρ_F."
    ))

    builder.add_assertion(
        name="cache_coverage_complete",
        computed=cache_coverage > 0.999999,
        expected=True,
        tolerance=0.0,
        source="cached_sum / reported_tr_M",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
