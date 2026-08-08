---
# qou-mfst
title: 'INFRA: lake-manifest.json still lists doc-gen4 after qou-dg4x commented the require out'
status: todo
type: task
priority: low
tags:
    - lean
    - infra
    - lakefile
---


## What

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
