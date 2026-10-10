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
import sys
from fractions import Fraction
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# PRE-EXISTING PATH BUG, fixed 2026-08-29. `HERE` is `<repo>/computations`, so
# `parents[1]` is the directory ABOVE the repo -- the script globbed
# `<parent>/content`, which does not exist, found zero sidecars, and printed
# "no proof-* sidecar entries found" on every run. It has been reporting nothing
# since at least 2026-06-15, the last date its committed witness was touched
# (and that by a refactor commit, not a run). M1/M2/M4/M5 were not being
# computed at all.
REPO = HERE.parents[0]

from mpmath import mpf  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# `import _precision` does NOT set mp.dps (its own docstring says so) -- it
# stays at mpmath's default 15, which is float64-grade. Set it explicitly.
set_compute_dps()


def _exact(num: int, den: int) -> str:
    """Serialize an exact count-ratio without ever forming a float64.

    Every metric here is a ratio of integer counts -- a pass rate is
    `100*passes/total`, a mean score is `sum/n`, a median is a midpoint of
    integers. These are exactly representable as `Fraction`, so the honest
    route is Fraction -> mpf -> `fmt`, never `float`. The previous code used
    `round(100.0*sum(xs)/len(xs), 1)` and `statistics.mean(...)`, both of which
    land raw float64 in the witness and tripped the raw-float64 ratchet on six
    fields (M1_pass_pct, M2_mean_score, M5_pass_pct across three cohorts).
    """
    f = Fraction(num, den)
    return fmt(mpf(f.numerator) / mpf(f.denominator))


def _short(v, places: int = 3) -> str:
    """Console display only. The witness keeps the full serialized value; a
    60-digit column is unreadable and the table is for a human. Truncates the
    decimal string rather than re-rounding through a float, so this never
    reintroduces the float64 the rest of this module exists to avoid."""
    if v is None:
        return "None"
    t = str(v)
    if "." not in t:
        return t
    head, tail = t.split(".", 1)
    tail = tail.rstrip("0")[:places]
    return f"{head}.{tail}" if tail else head


def _mean_exact(xs: list[Fraction]) -> str:
    """Mean of exact Fractions, still exact: sum/n as one Fraction."""
    total = sum(xs, Fraction(0))
    return _exact(total.numerator, total.denominator * len(xs))


def _median_exact(xs: list[int]) -> str:
    """Median of integers, exact. An even-length median is a half-integer, so
    it is a Fraction with denominator 2 -- not a float."""
    ys = sorted(xs)
    n = len(ys)
    if n % 2:
        return _exact(ys[n // 2], 1)
    return _exact(ys[n // 2 - 1] + ys[n // 2], 2)


PASS = {"pass"}
M1_CRIT = "proof-statement-integrity"
M5_CRITS = ("proof-no-bare-sorries", "proof-no-axiom-growth")

# Criteria whose PLATFORM CHECKER is an unconditional `n/a` stub: it reads no
# file and can return no verdict at any commit, under any config, with any
# artefact present. Averaging one into a pass rate contributes 0% BY
# CONSTRUCTION -- the same defect the `field_hash` filter below exists to
# prevent, one level up: not a wrong number but a number about nothing.
#
# Measured 2026-09-27 against platform pin 37a36ce, over 3653 sidecars: both
# are 100.0% `n/a` across every entry since 2026-07-13. `proof-lean-compiles`
# is the control -- same file, same domain, reads a cached artefact, and
# reports real verdicts -- so this is these two checkers, not the sweep.
#
# Owner decision 2026-09-27 (option 2 of bean qou-306p): a metric with a stub
# among its criteria publishes NO number, with the reason recorded, rather
# than a diluted one. Deleting the stub from M5_CRITS instead would silently
# redefine M5 as a one-criterion metric against its own scope doc (§39).
# Remove an entry here only when the upstream checker is implemented or
# retired -- upstream bean folio-assistant-89wq.
STUB_CRITERIA = {
    "proof-no-axiom-growth":
        'checkProofNoAxiomGrowth (qa-checkers-extended.ts:2783) is a bare '
        '`return {result: "n/a", hits: []}`; its one parameter is '
        "underscore-prefixed and unread",
    "proof-build-green":
        'checkProofBuildGreen (qa-checkers-extended.ts:2789) is a bare '
        '`return {result: "n/a", hits: []}`; likewise. Its name reads as '
        '"this block\'s Lean builds" and it has never opened a Lean file',
}

# M5's criteria that cannot report. Non-empty => M5 publishes no number.
M5_STUBS = tuple(c for c in M5_CRITS if c in STUB_CRITERIA)


def iter_first_verdicts():
    """Yield (block, criterion, first_entry, n_entries_until_pass)."""
    # Issue #7642: reports are read where the platform reads them (the results
    # tree first, then the legacy sibling); `f` keeps naming the block by its
    # legacy sibling path so the output's block keys do not change.
    sys.path.insert(0, str(REPO / "scripts" / "lib"))
    import block_qa
    block_qa.warn_if_unfetched("ab_methodology_metrics")
    for broot, src in block_qa.iter_reports(REPO / "folio"):
        f = block_qa.legacy_path(broot)
        try:
            doc = json.loads(src.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        crits = doc.get("criteria")
        if not isinstance(crits, dict):
            continue
        for crit, entries in crits.items():
            if not crit.startswith("proof-") or not isinstance(entries, list):
                continue
            # RESOLVABLE ONLY (2026-08-29). An entry with no `field_hash` records
            # no block version, so it cannot be tied to the content it judged --
            # it is neither confirmable nor refutable, and averaging it produces
            # a number about nothing. Every such entry here comes from the
            # 2026-07 `e62336dabc1` batch ("heuristic agentic redo for proof
            # criteria (full replace)"), which REPLACED the criteria arrays and
            # so destroyed the genuine earlier first-verdicts.
            #
            # Measured consequence, and it is severe: this filter removes 99.7%
            # of M2's input (3286 of 3297) and 99.6% of M1's (1096 of 1100),
            # because taking the FIRST verdict systematically selects the oldest
            # entry -- exactly the one that batch overwrote. M1 and M2 are
            # therefore reported only where the residual sample survives, with
            # `M1_n` / `M2_n` carrying that sample size -- read the n before
            # the rate. CORRECTED 2026-09-27: this comment used to end "are
            # reported as such rather than as a number; see `insufficient` in
            # the witness", and NO SUCH KEY EXISTED -- the witness published
            # `M1_pass_pct` off a single-digit sample with nothing marking it
            # thin. (Deliberately not quoting the n: it drifts with the
            # corpus, and a drifting number in a comment is this repo's most
            # reliable way to manufacture a stale claim.) The key
            # exists now but covers M5 only (STUB_CRITERIA); M1/M2 remain a
            # thin-sample caveat, which is a different and weaker claim than
            # not-computable. Do not widen it without measuring.
            # M5's own filter loss is 0% unhashed, and the cohort axis is
            # intact (3 cohorts survive: 145/983/2404 blocks).
            dated = [e for e in entries
                     if isinstance(e, dict) and e.get("reviewed_at")
                     and e.get("field_hash")]
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
        "blocks": set(), "m1": [], "m2": [], "m4": [], "m5": [],
        # per-criterion split of the m5 population, so the `insufficient`
        # record can evidence the dilution with COUNTS (never a rate -- a
        # rate here would be a substitute M5 by another name).
        "m5_by_crit": defaultdict(list)})
    for r in rows:
        c = cohorts[r["cohort"]]
        c["blocks"].add(r["block"])
        if r["crit"] == M1_CRIT:
            c["m1"].append(r["result"] in PASS)
        if r["crit"].startswith("proof-rater-") and isinstance(r["score"], (int, float)):
            # Build the Fraction from the score's DECIMAL spelling, not from
            # the float. Fraction(0.85) is exactly 0.84999999999999997779...,
            # the true binary64 value -- so the old comment here was right
            # that nothing is invented at THIS step, and wrong about the
            # consequence: _mean_exact then serialises that tail to 60 digits
            # and the witness claims 56 digits of precision for a number a
            # rater typed as "0.85". That is the float64-padding gate's
            # definition of fake precision, and it fired on
            # data.cohort_table[1].M2_mean_score.
            #
            # str() on a float is the shortest repr that round-trips, i.e.
            # the decimal the sidecar author actually wrote, so
            # Fraction(str(0.85)) is Fraction(17, 20) and the mean of the
            # cohort serialises as a short exact decimal. An int score is
            # already exact; keep it as one.
            score = r["score"]
            c["m2"].append(Fraction(score) if isinstance(score, int)
                           else Fraction(str(score)))
        if r["to_green"] is not None:
            c["m4"].append(r["to_green"])
        if r["crit"] in M5_CRITS:
            c["m5"].append(r["result"] in PASS)
            c["m5_by_crit"][r["crit"]].append(r["result"] in PASS)

    def rate(xs):
        """Pass rate as an exact percentage, serialized -- never a float."""
        return _exact(100 * sum(1 for x in xs if x), len(xs)) if xs else None

    table = []
    for month in sorted(cohorts):
        c = cohorts[month]
        table.append({
            "cohort": month,
            "n_blocks": len(c["blocks"]),
            "M1_pass_pct": rate(c["m1"]),
            "M1_n": len(c["m1"]),
            "M2_mean_score": _mean_exact(c["m2"]) if c["m2"] else None,
            "M2_n": len(c["m2"]),
            "M4_median_revisions_to_green": (
                _median_exact(c["m4"]) if c["m4"] else None),
            # None when any M5 criterion is a stub -- see STUB_CRITERIA
            # and `data.insufficient.M5`. `M5_n` still reports the
            # population so a reader can see there IS data and that it is
            # deliberately not aggregated.
            "M5_pass_pct": None if M5_STUBS else rate(c["m5"]),
            "M5_n": len(c["m5"]),
        })

    # Metrics that deliberately publish no number, with the reason. A reader
    # or a downstream aggregator must be able to tell "not reportable" from
    # "reported as zero" WITHOUT reading this source file.
    insufficient = {}
    if M5_STUBS:
        m5_pop = defaultdict(int)
        for month in cohorts:
            for crit, vals in cohorts[month]["m5_by_crit"].items():
                m5_pop[crit] += len(vals)
        insufficient["M5"] = {
            "reported": None,
            "reason": (
                "M5 aggregates " + str(len(M5_CRITS)) + " criteria and "
                + str(len(M5_STUBS))
                + (" of them has" if len(M5_STUBS) == 1 else " of them have")
                + " no checker: an "
                "unconditional `n/a` stub contributes 0 passes by "
                "construction, so any M5 rate is a weighted average of the "
                "real criterion and zero. Reported as insufficient rather "
                "than diluted (owner decision 2026-09-27, bean qou-306p)."
            ),
            "stub_criteria": {c: STUB_CRITERIA[c] for c in M5_STUBS},
            # COUNTS ONLY, deliberately. A per-criterion pass RATE here would
            # be M5 published under another name, which is what this record
            # exists to prevent.
            "first_verdicts_by_criterion": dict(sorted(m5_pop.items())),
            "unblocked_by": "implementing or retiring the upstream checkers",
            "beans": ["qou-306p", "folio-assistant-89wq"],
        }

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
              f"{_short(t['M1_pass_pct']):>9} {t['M1_n']:>5} "
              f"{_short(t['M2_mean_score']):>9} {t['M2_n']:>5} "
              f"{_short(t['M4_median_revisions_to_green']):>7} "
              f"{('insuf' if t['M5_pass_pct'] is None and M5_STUBS else _short(t['M5_pass_pct'])):>9}")

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
                "insufficient": insufficient,
                "caveats": [
                    "M5 publishes no number: one of its two criteria is an unconditional-n/a platform stub (see data.insufficient.M5)",
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
