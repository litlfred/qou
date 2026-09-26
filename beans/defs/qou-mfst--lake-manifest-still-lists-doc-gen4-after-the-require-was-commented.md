---
# qou-mfst
title: 'INFRA: lake-manifest.json still lists doc-gen4 after qou-dg4x commented the require out — FIXED ON MAIN'
status: completed
type: task
priority: low
tags:
    - lean
    - infra
    - lakefile
created_at: 2026-09-04T21:50:32Z
updated_at: 2026-09-26T11:03:24Z
---

## RESOLVED 2026-08-08 — fixed on main, not by me

Re-checked against `origin/main` at `ea0a74245e`:

```sh
git show origin/main:content/quantum-observable-universe/lean/lake-manifest.json \
  | grep -c 'doc-gen4'      # 0
```

`«doc-gen4»` and its transitive deps `UnicodeBasic`, `BibtexQuery`, `MD4Lean`
are gone from the manifest. The "To fix" below — regenerate and diff the pins,
confirming nothing but the doc-gen4 group moved — is exactly what happened:
checked against the same diff, **Mathlib's rev did not move**, so the
requirement that no unrelated pin churn was met.

Closing as done. Nothing was owed by this lane.

## ⚠ Second instance of the same process failure — this is the lesson

This bean was about to ship in a PR with `status: todo`, describing a live
problem that main had **already fixed**. That is the *second* time in one
session; `qou-lkrd` did the same thing, asserting 22 `lake build` errors in two
modules that current main compiles clean.

Both have the same cause, and it is not "forgot to fetch". It is structural:

> **A bean written on a long-lived branch is a claim about the base that branch
> was cut from, and it silently ages into a claim about `main`.** Nothing in the
> bean records which base it was measured against, so by the time it ships the
> reader has no way to know it is stale — and neither does the author.

The fix is cheap and belongs in the bean format, not in anyone's discipline:
**state the base sha in the bean when recording a measurement**, and re-check
any `todo` infra bean against fresh `main` immediately before it ships. Both
beans corrected here now carry their measurement base explicitly.

## What (as originally recorded — the drift it describes is now gone)

`qou-dg4x` re-commented the `doc-gen4` `[[require]]` in
`content/quantum-observable-universe/lean/lakefile.toml`, but left
`lake-manifest.json` alone. The manifest still lists `«doc-gen4»` and its
transitive deps `UnicodeBasic`, `BibtexQuery`, `MD4Lean`, so lockfile and
lakefile now disagree.

## Why it was left

Deliberate, and recorded at the time:

* the build is **unaffected** — verified, `lake build QOU.QBeta.FiveTwoCyclotomicBloch`
  green at 707 jobs with the require commented and the manifest stale;
* the docs workflow runs `lake update doc-gen4` immediately after enabling the
  block, which reconciles the lockfile itself;
* regenerating the manifest risks churning **unrelated package pins** — and it was
  found on a PR about the 5₂ sum rule, where that would be scope creep.

## To fix

Regenerate deliberately and **diff the pins**, confirming nothing but the
doc-gen4 group moved. Do not do it as a side effect of another change.

## Refs

* `qou-dg4x` (the fix that created this drift, and why it stopped there)
