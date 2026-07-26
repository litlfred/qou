---
# qou-z2ma
title: 'G5: growth => hbdd wiring => faddeevPhi_proportional_of_bounded_ratio'
status: in-progress
type: task
priority: normal
created_at: 2026-07-26T01:17:32Z
updated_at: 2026-07-26T03:10:08Z
blocked_by:
    - qou-zt8v
---

G5 CRUX DONE (MeromorphicPuncturedBounded.lean): the removable-singularity extension is proved -- meromorphicOrderAt_nonneg_of_bounded_punctured (local order lemma) + norm_le_of_bounded_on_punctured (punctured-bound-everywhere => global hbdd). This bridges G4's dense-locus raw-ratio bound to the capstone's everywhere-hbdd. REMAINING (assembly-level, NO Mathlib gap): (i) phiBProd zeros isolated [from order != top, PR #4225]; (ii) hr_ratio [toMeromorphicNFOn = ratio off poles, normal-form API]; (iii) honest MeromorphicOn Phi_1 hypothesis for the arbitrary second solution. Then call faddeevPhi_proportional_of_bounded_ratio.
