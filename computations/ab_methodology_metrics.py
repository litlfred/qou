#!/usr/bin/env python3
# EXPLORATORY v1 — sidecar-only slice of the A/B methodology metrics.
# Scope doc: docs/workplans/2026-06-11-ab-methodology-metrics-scope.md
# v1 defaults (owner default accepted 2026-06-11): proofs-only criteria
# (prefix "proof-"), aggregate tables only.  M3 (sorry-citation at first
# commit) and deleted-block survivorship need the git-history walk —
# deferred to v2 and stated as a coverage caveat in the witness.
"""A/B methodology metrics v1 — first-draft proof quality over time.

Reads every content/**/*.qa.json sidecar (append-only, hash-stamped),
takes the FIRST verdict per (block, criterion) by `reviewed_at`, and
reports per-month cohorts:

  M1  first-verdict pass rate of proof-statement-integrity
  M2  first-verdict mean score of scored proof-rater-* criteria
  M4  revisions-to-green: entries until first pass (median per cohort)
  M5  first-verdict pass rate of proof-no-bare-sorries / no-axiom-growth

Adoption dates are DETECTED (min reviewed_at per criterion corpus-wide),
never hand-picked.  Cohort key: month of the block's earliest proof-*
verdict (proxy for block creation until the v2 git walk).

Outputs `ab-methodology-metrics.witness.json`.
"""
from __future__ import annotations

import _path_bridge as _pb  # noqa: F401, E402 — substrate module bridge
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
REPO = HERE.parents[1]

PASS = {"pass"}
M1_CRIT = "proof-statement-integrity"
M5_CRITS = ("proof-no-bare-sorries", "proof-no-axiom-growth")


def iter_first_verdicts():
    """Yield (block, criterion, first_entry, n_entries_until_pass)."""
    for f in sorted((REPO / "content").rglob("*.qa.json")):
        try:
            doc = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        crits = doc.get("criteria")
        if not isinstance(crits, dict):
            continue
        for crit, entries in crits.items():
            if not crit.startswith("proof-") or not isinstance(entries, list):
                continue
            dated = [e for e in entries
                     if isinstance(e, dict) and e.get("reviewed_at")]
            if not dated:
                continue
            dated.sort(key=lambda e: e["reviewed_at"])
            to_green = next(
                (i + 1 for i, e in enumerate(dated)
                 if str(e.get("result", "")).lower() in PASS),
                None,
            )
            yield str(f.relative_to(REPO)), crit, dated[0], to_green


def main() -> int:
    adoption = {}                 # criterion -> earliest reviewed_at
    block_first = {}              # block -> earliest proof verdict date
    rows = []
    for block, crit, first, to_green in iter_first_verdicts():
        ts = first["reviewed_at"]
        adoption[crit] = min(adoption.get(crit, ts), ts)
        block_first[block] = min(block_first.get(block, ts), ts)
        rows.append({
            "block": block, "crit": crit, "ts": ts,
            "result": str(first.get("result", "")).lower(),
            "score": (first.get("score") or {}).get("value")
            if isinstance(first.get("score"), dict) else first.get("score"),
            "to_green": to_green,
        })

    if not rows:
        print("no proof-* sidecar entries found — nothing to report")
        return 1

    for r in rows:
        r["cohort"] = block_first[r["block"]][:7]   # YYYY-MM of the block

    cohorts = defaultdict(lambda: {
        "blocks": set(), "m1": [], "m2": [], "m4": [], "m5": []})
    for r in rows:
        c = cohorts[r["cohort"]]
        c["blocks"].add(r["block"])
        if r["crit"] == M1_CRIT:
            c["m1"].append(r["result"] in PASS)
        if r["crit"].startswith("proof-rater-") and isinstance(r["score"], (int, float)):
            c["m2"].append(float(r["score"]))
        if r["to_green"] is not None:
            c["m4"].append(r["to_green"])
        if r["crit"] in M5_CRITS:
            c["m5"].append(r["result"] in PASS)

    def rate(xs):
        return round(100.0 * sum(xs) / len(xs), 1) if xs else None

    table = []
    for month in sorted(cohorts):
        c = cohorts[month]
        table.append({
            "cohort": month,
            "n_blocks": len(c["blocks"]),
            "M1_pass_pct": rate(c["m1"]),
            "M1_n": len(c["m1"]),
            "M2_mean_score": round(statistics.mean(c["m2"]), 3) if c["m2"] else None,
            "M2_n": len(c["m2"]),
            "M4_median_revisions_to_green": statistics.median(c["m4"]) if c["m4"] else None,
            "M5_pass_pct": rate(c["m5"]),
        })

    crit_counts = defaultdict(int)
    for r in rows:
        crit_counts[r["crit"]] += 1
    top_crits = sorted(crit_counts.items(), key=lambda kv: -kv[1])[:10]

    print("=" * 74)
    print(" A/B methodology metrics v1 — first-draft proof quality by cohort")
    print("=" * 74)
    print(f"\n sidecar first-verdicts: {len(rows)} across "
          f"{len(block_first)} blocks, {len(crit_counts)} proof criteria")
    print("\n adoption dates (detected, earliest first verdict per criterion):")
    for crit, ts in sorted(adoption.items(), key=lambda kv: kv[1])[:10]:
        print(f"   {ts[:10]}  {crit}")
    print("\n top criteria by first-verdict count:")
    for crit, n in top_crits:
        print(f"   {n:>5}  {crit}")
    print(f"\n {'cohort':>8} {'blocks':>7} {'M1 pass%':>9} {'(n)':>5} "
          f"{'M2 score':>9} {'(n)':>5} {'M4 med':>7} {'M5 pass%':>9}")
    for t in table:
        print(f" {t['cohort']:>8} {t['n_blocks']:>7} "
              f"{str(t['M1_pass_pct']):>9} {t['M1_n']:>5} "
              f"{str(t['M2_mean_score']):>9} {t['M2_n']:>5} "
              f"{str(t['M4_median_revisions_to_green']):>7} "
              f"{str(t['M5_pass_pct']):>9}")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "ab-methodology-metrics",
        {
            "description": (
                "EXPLORATORY v1 A/B methodology metrics: first-verdict "
                "proof-quality aggregates per monthly cohort from the "
                "append-only .qa.json sidecars (proofs-only, aggregates "
                "only).  Adoption dates detected from data.  v2 adds the "
                "git-history walk (M3 sorry-citation at first commit, "
                "deleted-block survivorship) and model-version "
                "stratification via the session archive."
            ),
            "exploratory": True,
            "scope_doc": "docs/workplans/2026-06-11-ab-methodology-metrics-scope.md",
            "data": {
                "n_first_verdicts": len(rows),
                "n_blocks": len(block_first),
                "adoption_dates": dict(sorted(adoption.items())),
                "criteria_counts": dict(top_crits),
                "cohort_table": table,
                "caveats": [
                    "cohort key is the block's earliest proof verdict (proxy for creation until the v2 git walk)",
                    "M3 + survivorship deferred to v2",
                    "model-version stratification deferred to v2 (needs #2115 archive metadata)",
                ],
            },
        },
        script_path=__file__,
        engine="python",
    )
    out_path = builder.save()
    print(f"\n  Wrote {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
