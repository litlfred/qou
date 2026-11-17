---
# qou-7cmk
title: '§7c mixed-file advisory on MarkovZFullBarCondition.lean (branch-introduced by #5111) — split or justify'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T15:55:00Z
updated_at: 2026-11-17T06:55:30Z
parent: qou-rtxm
---

## What

`scripts/check-sidecars.sh`, run properly scoped during the #5111 merge
pipeline, flags a **branch-introduced §7c mixed-file advisory** on the new
`folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean`
(bean `qou-b3nk`, merged as `4f1cea6223`).

The PR body had claimed "check-sidecars: no §7c flags". That was **false** —
the run had been mis-scoped. Recorded here rather than silently dropped.

## Why it was not fixed at merge time (and why that was defensible)

The §7c harm model is **archimedean `ℝ` leakage across the substrate wall**.
This file has none: the declarations are generic `[CommRing R]`, and the
ordered section is generic too — verified during the merge gate. So the
advisory is about **file organisation** (a single file carrying both the
generic algebra and the `s = √q > 1` substrate-side specialisation), not
about a wrong base ring reaching a downstream consumer.

Splitting a file at merge time, after the Lean had been verified
`lean`-direct exit 0 against its real import cone, would have invalidated
that verification for a cosmetic gain. Deferred deliberately.

## What to do

1. Re-run `scripts/check-sidecars.sh` scoped to the file and read the exact
   advisory line (do not work from this summary).
2. Either **split** — generic `CommRing` bricks
   (`zD_full_bar_covariant`, `barEven_fullBar_forces_classical`) in one
   module, substrate-side field forms (`zC_fails_fullBar`,
   `decayLadder_zC_not_jones`, `decayLadder_zC_threeRow_ne_zero`) in a
   second that imports it — **or** record the justification above in the
   file's docstring so the advisory reads as reviewed rather than missed.
3. Re-verify `lean`-direct exit 0 on both halves (lake-cache restore; never
   a bare `lake build`) and confirm `#print axioms` still shows no `sorryAx`.

## Provenance

Surfaced by the #5111 prepare-merge-auto pipeline, which corrected the PR
body's false claim rather than passing it through. The agent could not file
this bean itself — the `beans` CLI is not installed in that sandbox and
hand-minting IDs risks the documented duplicate-bean failure
(`qou-2ryn`, 14,688 duplicates). Filed by the parent session instead.

## 2026-11-17 — Generic-Ring Bricks of `MarkovZFullBarCondition` (`litlfred/qou#8237`)
- Formalized `zD_cleared_full_bar_covariant` and `barEven_and_fullBar_forces_classical` over generic `CommRingOps R` (zero `ℝ` occurrences) in `folio/quantum-observable-universe/lean/QOU/Foundations/BarConditionHyperbolicSphericalMetric.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `62b14488de4f16d02964a9976964f16ed12bcdcd`, PR [https://github.com/litlfred/qou/pull/8237](https://github.com/litlfred/qou/pull/8237)).
- Kept `status: in-progress` per no-unilateral-closure policy.
