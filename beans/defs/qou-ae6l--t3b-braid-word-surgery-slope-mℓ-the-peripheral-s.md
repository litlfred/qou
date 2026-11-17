---
# qou-ae6l
title: 'T3b: braid word → surgery slope (m,ℓ) — the peripheral structure map'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-30T16:59:40Z
updated_at: 2026-11-17T06:36:38Z
pr: 8228
parent: qou-avtq
---

For a braid word β ∈ B_n with closure K = β̂, the peripheral structure of π₁(S³∖K) gives a specific (meridian, longitude) pair. The braid word determines a specific representation in π₁, hence a specific effective slope. How does the Hecke algebra representation at q₀ select the slope? Writhe gives framing but not the 2D winding. Literature: Burde-Zieschang peripheral systems, Riley representations, Culler-Shalen theory.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open, and independent of the S_leak data. Note that its motivation (matching T4 ϑ) is evidence-unreliable (see qou-4kgh).

Evidence: No commits or probes reference it. This is a pure-math question (peripheral system → slope) that does not depend on the S data.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Round 51 Formalization & 50-dps Witness (PR #8228)
- [x] **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/QBeta/BraidPeripheralSlopeMap.lean` (`peripheralSlopeMap_zero`, `peripheralSlopeMap_comp`, `peripheralSlopeMap_inv`, `peripheralSlopeMap_preserves_intersection`, `peripheralSlopeMap_preserves_bezout`, `meridianFilling_writhe_invariant_and_zero_longitude_iff`, `markovStabilization_compensation_iff`, `corpusKnot_blackboard_zero_surgery_slopes`).
- [x] **50-dps Witness:** `computations/probes/round51-two-loop-flat-torus-theta-weight-and-peripheral-slope.witness.json` (`scriptHash: 879cd7fbcdb2`, `scriptCommitSha: bffc9aa954100eaed1adf1a81eb35fe56e86a5f2`).
- [x] **PR:** `litlfred/qou#8228` (`https://github.com/litlfred/qou/pull/8228`, head SHA `8335ad54a1e5c4f7a61669fed19de6b0184f0a4d`).
- [ ] **Reviewer-separated closure:** Kept at `status: in-progress`.
