---
# qou-k6ub
title: 'PROVE(lean): atomic_lp_stability.lean — 2 cited sorries [cited bertsimas1997,manuscript,wenzl1990]'
status: in-progress
type: task
priority: normal
tags:
    - paper-qou
    - repo-infra
    - cite-bertsimas1997
    - cite-wenzl1990
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-11-18T07:49:45Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/atomic_lp_stability.lean` (QOU)  ·  2 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_lp_stability.lean

### `bare_is_lp_unstable`  —  line 99  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem bare_is_lp_unstable [ctx : AtomicLPStabilityContext] : ∃ X : ctx.Candidate, ctx.normalised X ∧ ctx.bareVolume X = 0 `
- **Cited:** `[bertsimas1997]`, `[manuscript]`, `[bertsimas1997]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/particle-interactions/atomic-lp-stability.md
- **Tractability:** ∃ a normalised zero-bare-volume candidate (bare instability); feasibility witness over context class.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `dressed_is_lp_stable`  —  line 111  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem dressed_is_lp_stable [ctx : AtomicLPStabilityContext] : ¬ ∃ X : ctx.Candidate, ctx.normalised X ∧ ctx.dressedVolume X = 0 `
- **Cited:** `[bertsimas1997]`, `[wenzl1990]`, `[manuscript]`, `[wenzl1990]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [wenzl1990] Wenzl (1990), *Quantum groups and subfactors of type B, C, and D* — https://doi.org/10.1007/BF02097372
  - [manuscript] quantum-observable-universe/particle-interactions/atomic-lp-stability.md
- **Tractability:** No normalised zero-dressed-volume candidate (dressed stability); positivity over context class.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## Round 83 Progress (PR #8392)
- Branch: `feat/round83-lambdasum-taupos-pairenergy-c1eval-nobranch-43c1`
- Commit 1 (code + probe): `e226ba66ce53cea91430549ce1efc48cd1eeef24`
- Commit 2 (witness): `17c21a76b062fd76e16d4f84b23687e02fc0050c` (`scriptSha256 = 0635fcc96bfd3bd66e7452f9553ce1314e6829b0b1a6b7202ea86d48b4b232a6`)
