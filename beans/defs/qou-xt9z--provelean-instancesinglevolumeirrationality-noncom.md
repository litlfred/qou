---
# qou-xt9z
title: 'PROVE(lean): instance:SingleVolumeIrrationality — noncomputable instance : SingleVolumeIrrationality  [cited manuscript]'
status: scrapped
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:01Z
updated_at: 2026-10-04T15:22:35Z
parent: qou-k1mq
---

**File:** `QOU/Archimedean/SingleVolumeIrrationality.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Archimedean/SingleVolumeIrrationality.lean

### `instance:SingleVolumeIrrationality`  —  line 57  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `noncomputable instance : SingleVolumeIrrationality `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/archimedean-universe/single-volume-irrationality.ts
- **Tractability:** Irrationality of a single hyperbolic volume; transcendence result outside Mathlib's current reach.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.

## Verdict CONFIRMED 2026-08-31 (audit: docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md)

Individuated with the other thirteen. For THIS item the boilerplate verdict is right: the named
theory is genuinely absent from Mathlib and is genuinely required. Kept as-is.

Recorded because the same verdict was WRONG on several siblings; "confirmed" here means checked,
not merely un-revisited.



## Reasons for Scrapping

Duplicate of `cj21f` (work-plan reorganisation 2026-10-04). Evidence: [M] 'PROVE(lean): instance:SingleVolumeIrrationality' (under qou-k1mq) and 'Conjecture carrier: SingleVolumeIrrationality' (under b9cj, §3b) target the same Lean class; keep the §3b carrier as the P2 
Content is untouched; only this work item is closed.
