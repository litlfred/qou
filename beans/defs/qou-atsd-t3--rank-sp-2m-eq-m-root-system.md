---
# qou-atsd-t3
title: 'T3: rank Sp(2m)=m — m=1 torus fully pinned (lower + torus-upper + self-centralizing over a field); remaining gap = MAXIMALITY via connected-reductive structure theory (root count)'
status: in-progress
type: task
priority: normal
parent: qou-atsd
created_at: 2026-07-26T00:55:56Z
updated_at: 2026-07-26T00:55:56Z
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
