---
# qou-2q7r
title: 'Prove UGB reduction_well_founded (Bergman termination), discharging a Diamond-Lemma axiom'
status: in-progress
type: task
priority: high
created_at: 2026-11-20T15:00:00Z
updated_at: 2026-11-20T15:00:00Z
parent: qou-uhx0
---

W12 (session_01VQDpPfS7H7LVPj21tEhkK3), branch `claude/gs-reduction-well-founded-2026-11-20`.

`UGB.GrobnerShirshov.reduction_well_founded` (Basic.lean §6) was an `axiom` citing Bergman 1978 §2. It is true as stated (any ring, any system): a step eliminates `w = a·lm(r)·b` and only changes coefficients strictly below `w`, so the live support (monomials with non-zero coefficient) decreases in the Dershowitz–Manna order on finite sets, which is well-founded because `ord.wf` is.

Done on the branch: `DMLt`, `wellFounded_DMLt`, `liveSupport`, `singleStep_dmLt`, `reduction_well_founded` now a theorem. Signature unchanged, so `normal_form_exists`, `confluence`, `normal_form_unique` and every Hecke consumer lose one axiom with no code change.

Remaining Diamond-Lemma axiom: `local_confluence` (CompositionLemma.lean:83). Not attempted here.
