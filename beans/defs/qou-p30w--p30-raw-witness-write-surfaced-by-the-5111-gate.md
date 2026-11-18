---
# qou-p30w
title: 'P30 raw-witness-write surfaced by the #5111 gate (pre-existing, not branch-introduced)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T15:56:00Z
updated_at: 2026-10-04T15:21:57Z
parent: qou-5vkl
---

## What

The #5111 merge gate's properly-scoped `scripts/check-sidecars.sh` run also
surfaced a **pre-existing P30 raw-witness-write** — a producer writing a
witness directly instead of going through `WitnessBuilder`.

**Not branch-introduced.** It predates `qou-b3nk`'s work and was correctly
left untouched at merge time rather than folded into an unrelated PR.

## Why it matters

`WitnessBuilder` is what stamps the provenance the staleness machinery reads
(`commitSha`, `scriptHash`) and what routes serialization through
`_precision.fmt` — the NO-FLOAT64 discipline's chokepoint. A raw write
bypasses both, so such a witness can carry float64 into the tree and can go
stale invisibly. Compare the existing rollup bean `1j39`
("Integration: I-infra-no-witnessbuilder-P30 batch port") — **check whether
this instance is already inside that batch before doing anything**; if so,
close this as a duplicate pointer rather than porting twice.

## What to do

1. Re-run `scripts/check-sidecars.sh` on the relevant path and capture the
   exact P30 line — file and producer (this bean deliberately does not name
   one from memory; the gate output is the source of truth).
2. Corpus-grep it against bean `1j39`'s batch scope.
3. If not already covered: port the producer to `WitnessBuilder`, re-run it
   (tee the log per the long-compute discipline), and confirm
   `scripts/precision-gates.sh` NEW-dirty stays 0.

## Provenance

Surfaced by the #5111 prepare-merge-auto pipeline. The agent could not file
this bean itself (no `beans` CLI in that sandbox; hand-minting IDs risks the
documented duplicate-bean failure). Filed by the parent session.

Also flagged by that pipeline and **left standing on `main`, not from that
branch**: `computations/rho-k-co-casimir-extended.witness.json` regressed
3 → 4 raw float64 fields (Δ_λ co-Casimir domain). Proved main-side by
byte-comparison against `origin/main`. Separate domain — needs its own owner.
