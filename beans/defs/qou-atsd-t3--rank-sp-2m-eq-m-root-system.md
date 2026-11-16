---
# qou-atsd-t3
title: 'T3: rank Sp(2m)=m — m=1 torus fully pinned (lower + torus-upper + self-centralizing over a field); remaining gap = MAXIMALITY via connected-reductive structure theory (root count)'
status: in-progress
pr: 8203
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-atomicity
created_at: 2026-07-26T00:55:56Z
updated_at: 2026-10-10T07:16:13Z
parent: qou-8lxd
---

DONE (#4285, AtomicityFromSelfDuality.lean, sorry-free) — the m=1 diagonal torus, fully pinned:
- diagEmbedHom + diagEmbedHom_injective: faithful Gm diagonal torus (rank SL2 >= 1, LOWER).
- sl2_diagonal_eq_diagEmbed: a diagonal SL2 matrix IS diag(t,t^-1) => diagonal torus = Gm
  EXACTLY (torus-level UPPER bound; this torus cannot be larger).
- commute_diagMat_imp_diagonal (over a Field): a matrix commuting with a REGULAR
  diag(t,t^-1) (t^2 != 1) is diagonal => the diagonal Gm is SELF-CENTRALIZING (the
  standard maximal-torus criterion). The t^2!=1 hyp records that maximality needs a
  unit of order >2 (true for R/C substrate, false over F2/F3).

OPEN (the genuine wall): concluding rank G <= 1 from self-centralizing needs the
CONNECTED-REDUCTIVE structure theory (self-centralizing torus in connected reductive
= maximal; all maximal tori conjugate; rank = its dimension). This is the root-count /
algebraic-group structure theory Mathlib lacks — the multi-session build. Also: general
m (Sp(2m), rank m); the ≃*-onto-range upgrade.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (2026-11-16, PR #8203)
- [x] Formalized `symplecticShortRootCount`, `symplecticLongRootCount`, `symplecticTotalRootCount`, `symplecticLieDim`, and `symplectic_root_and_dimension_identities` in `folio/quantum-observable-universe/lean/QOU/Eightfold/RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots.lean` + 50-dps mpmath witness (`qou_atsd_t3_symplectic_root_and_dimension_identities`) in PR #8203 (`74a091a53fd300f6f906db42c72c6a5e3e84e7b3`).
