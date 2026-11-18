---
# bwrt
title: 'bwse-RT: ground input (RT) in Mathlib braided/rigid categorical dimension (toward ribbon-MTC)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:10:00Z
updated_at: 2026-11-18T10:47:00Z
parent: qou-o9ge
---

Parent: bwse. Formalize input (RT) — the Reshetikhin-Turaev requirement that bwS0 is the RT surgery
weight S_{0λ}=d_λ/D of a ribbon/modular tensor category — TOWARD a genuine Mathlib ribbon-category
statement, rather than leaving d_λ an abstract field element.

DONE (branch claude/bwsc-level7-wrt-targets-2026-08-02, KeystoneRibbonMTCInput.lean, lean-direct
exit 0 sorry-free): defines the categorical quantum dimension qDimObj X : End(𝟙_C) = η_X ≫ β ≫ ε_X
(the ribbon trace tr(𝟙_X)) over Mathlib's real [BraidedCategory C] [RightRigidCategory C]; the
RibbonMTCInput structure (simple objects S:ι→C, scalar eval End(𝟙_C)→R, vacuum dim 1); and proves
the vacuum row S_{0λ}=catQDim λ/D is grounded in the categorical dimension (vacuumRow_S0_eq_catQDim,
vacuumRow_S0_ratio). So bwS0's value step now lands on Mathlib's categorical dimension, not a free
scalar.

STILL OPEN (does NOT close bwse): the full RT theorem — ribbon-functor + Kirby-invariant surgery
calculus giving the 3-manifold invariant — is ABSENT from Mathlib; and (BW=Hecke) that the
localization category IS the Hecke MTC (its simple-object categorical dimensions = the Hecke d_q)
remains the physics identification. Next possible steps: (a) prove qDimObj(𝟙_C)=𝟙 (unit dim = 1)
from Mathlib coherence — modest, removes vac_dim_one as a carried field; (b) define the modular
S-matrix S_{μλ} categorically (double braiding trace) — larger; (c) the full RT surgery functor —
multi-session Mathlib contribution, out of scope for a single session.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 80 (`lane-e667`): Formalized `bwrt`, `bwse`, `rtkb`, `rtqd`, `rtrb` in `QOU.Foundations.CategoricalQuantumDimensionVacuumRowModularPartitionSumSurgerySlideInvariancePivotalDualTraceRibbonBalancing` with 80-dps `mpmath` 2-commit witness stamp (`9665213be334ca01449913d997dcaa05341cba29` -> `bbf00cfbf597a3ca40051aee20f1eda6cf87da89`, `scriptHash=7b699b4f4747b371a7a9fb79fd09f0b495a31a2b2d536d50c421ec2b24457967`) in PR `litlfred/qou#8433` (`status: in-progress`).
