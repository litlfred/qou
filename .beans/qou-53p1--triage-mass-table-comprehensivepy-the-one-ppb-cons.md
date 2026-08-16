---
# qou-53p1
title: Triage mass_table_comprehensive.py — the one ppb consumer that timed out unchecked
status: todo
type: task
priority: normal
created_at: 2026-08-16T01:49:31Z
updated_at: 2026-08-16T02:28:26Z
---

## Triage answer: NOT broken. Slow — and hiding something much worse.

Last unchecked consumer from the `mass_table_ppb` port (qou-3wqg / qou-hqjf).
It timed out at 120 s during the consumer sweep, so it was unknown whether it
was merely slow or broken the way the four binding-family producers were.

**It runs to completion, rc=0, 14,972 rows.** But getting that answer turned up
three findings, and the third is the one that matters.

## 1. The ppb correction never reaches it — the upstream is declared, not read

```
mt_ppb_path = _pb.witness_path("mass-table-ppb.witness.json", HERE)
mt_ppb_data = None
if mt_ppb_path.exists():
    mt_ppb_data = builder.add_upstream(mt_ppb_path)     # L406
```

`mt_ppb_data` has **two stores and zero loads** (checked by AST walk, not by
eye). Every `B_pred_MeV` in the output comes from this producer's own
`sym_binding` / `qclt_binding` / `binding_canonical` paths. So the corrected
deuteron prediction does not reach this consumer at all — the provenance edge
claims a dependency the code does not have.

The `alpha_cluster_binding` call site is also safe: it already wraps
`float(r["B_pred_MeV"])`, so qou-hqjf changing that return type to mpf does
not break it.

That closes the question this bean was opened for.

## 2. It is ~11.5x slower than its own recorded baseline

    committed witness   durationMs    57,274   (14,972 rows,  261 rows/s)
    measured today      durationMs   656,759   (14,972 rows,   23 rows/s)

Same enumeration, and the producer takes **no CLI flags**, so there is exactly
one invocation to compare. `t_start = time.monotonic()` sits at the top of
`main()` above the row loop, so the baseline covers the full computation — I
checked, because a duration that only measured the final write would have made
this a non-finding.

**Not caused by this session.** A/B at `d7274ddc0` (pre-merge) vs current main,
150 s budget each: 5663 vs 5642 rows. Noise. I had suspected my own
`set_compute_dps()` additions raising global `mp.dps` to 70 via the lazy
`alpha.alpha_cluster_recursion` import inside the row loop — measured, wrong.

`engineVersion` moved `mpmath 1.3.0 -> 1.4.1` between the two runs. That is the
best remaining candidate and it is **untested** — it would affect every mpmath
producer in the repo, not just this one, so it is worth an hour from whoever
picks it up. Bisecting the code path instead needs `git fetch --unshallow`:
the witness's own `commitSha` (85da4f43133) is not reachable in this shallow
clone.

## 3. THE ONE THAT MATTERS — the committed witness is 5 weeks stale, and every row differs

`computedAt: 2026-07-07`. Regenerating today changes **14,970 of 14,972 rows**
in both `m_symbolic_MeV` and `B_pred_MeV`. These are not precision tails:

     atom      B_AME   B_pred OLD   B_pred NEW   err% OLD   err% NEW
        D     2.2245       3.5423       2.0715    +59.239     -6.877
        T     8.4818       8.4732       5.5149     -0.102    -34.980
      7Li    39.2445      23.0623      15.0515    -41.234    -61.647
      16O   127.6190      54.6043      35.4496    -57.213    -72.222

Mixed, not a scale factor: the deuteron gets much BETTER (+59% -> -6.9%) while
everything A>=3 gets much WORSE. Tritium's error moves from -0.1% to -35%.

Two readings, and I cannot tell which from the numbers alone:
  (a) a code change since 2026-07-07 broke the binding path, and the stale
      witness has been masking it for five weeks; or
  (b) the methodology changed deliberately and nobody regenerated.

Either way the published 10 MB table is not what the code computes, and
**nothing catches it**: regeneration takes 11 minutes, no gate runs it, and the
witness-staleness workflow is dispatch-only by owner directive (2026-06-30
Actions-billing). Four audit docs cite values from the stale copy
(`2026-08-09-canonical-ordering-dof-production-impact.md`,
`2026-08-09-ordering-loose-ends-a3-helper-and-missing-he-rows.md`,
`2026-06-01-vol-density-derivation-trace.md`,
`2026-05-24-65-isotope-mass-table-audit.md`).

### I did NOT commit the regenerated witness

Deciding which of the two tables is correct is a physics call, not a triage
outcome, and it would also move this file's raw-float64 count (it is in the
qou-mnrd baseline). The regenerated file is preserved out-of-tree at:

    <session scratchpad>/mass-table-comprehensive.REGENERATED-2026-08-16.witness.json

so whoever adjudicates does not have to spend another 11 minutes.

## Smaller things found in passing, none fixed

- **All upstream provenance is discarded.** The output has no
  `upstream_witness_hashes` key at all, despite `add_upstream(mt_ppb_path)` at
  L406 and ~15,000 `record_upstream(...)` calls at L205.
  `builder.add_upstream_records(_UPSTREAM_RECORDS)` runs at **L363**, before
  the row loop that fills `_UPSTREAM_RECORDS`. Checked whether this ordering
  bug was systemic across the `record_upstream` port (453b2a868, 86a218eb3):
  a textual-order scan found 0 other producers, but textual order is the wrong
  test here (collection happens inside a function called later), so that scan
  proves nothing and a real check is still owed.
- **Stale description.** Claims "all nuclei from proton (A=1) through 12C
  (A=12) ... A >= 5 flagged as 'not yet computed'". The data is 14,972 rows,
  A=1..418, Z=0..118.
- **Every row emits a DeprecationWarning** — `atom_per_generator_volumes` uses
  H_3 Wedderburn weights where H_{3A} are correct
  (docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md). ~15,000 warnings per
  run, and it affects every published row.

## Next

Finding 3 needs an owner decision before anything is committed. Findings 1 and
the L363 ordering bug are both small, mechanical, and safe to fix — but fixing
1 means deciding whether the ppb upstream should be *read* or the declaration
*dropped*, which is again not mine to pick unilaterally.
