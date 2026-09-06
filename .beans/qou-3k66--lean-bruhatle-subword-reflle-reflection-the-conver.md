---
# qou-3k66
title: 'Lean: BruhatLe (subword) -> ReflLe (reflection) — the converse bridge'
status: todo
type: task
created_at: 2026-09-06T11:10:51Z
updated_at: 2026-09-06T11:10:51Z
---

## What is open

The two standard Bruhat orders, and only one direction between them:

* **subword** — `QOU.Machinery.CoxeterBruhat.BruhatLe`: some reduced word for `w`
  has a subword multiplying to `u`. This is what the corpus proves everything
  about.
* **reflection-generated** — `QOU.IwahoriHecke.BruhatReflection.ReflLe`: `w` is
  reached from `u` by right multiplication by reflections, each step increasing
  length. This is Mathas' / Dipper–James' `⊵`.

`bruhatLe_of_reflLe : ReflLe → BruhatLe` is **proved** (2026-09-06). **The
converse is not**, and it is what a consumer citing Mathas Prop 3.7 (`s ⊵ t ↔
d(s) ⊵ d(t)`) needs for the `↔`.

## 🛑 The obstacle is NOT the lifting property — I said it was and was wrong

`BruhatReflection.lean`'s first draft recorded the blocker as the lifting
property. Lifting was then proved in that same file and the converse still did
not follow, so the diagnosis was false. Do not re-derive from it.

What actually blocks it: the induction on `ℓ(w)` wants an intermediate `v` with
`ReflStep v w` and `u ≤ v`. The natural candidate is `v = π (ω.eraseIdx j)` for
an index `j` the subword skips, and `reflStep_of_eraseIdx` confirms that IS a
downward reflection step. But `ω.eraseIdx j` is **not reduced**, so a subword of
it does not witness `BruhatLe u v` — the definition quantifies over reduced
words.

## The missing statement

> A subword of an **arbitrary** (not necessarily reduced) word for `w` still
> gives `u ≤ w`.

With that, the induction closes. Two plausible routes, neither attempted:

1. Induct on `|ω| − ℓ(π ω)`, replacing a non-reduced `ω` by a reduced sublist
   (`CoxeterDeletion.exists_reduced_sublist'`) while tracking the subword — the
   difficulty is that the deletion `exists_deletion` performs need not respect
   the subword.
2. Prove it directly by induction on the `List.Sublist` derivation, using
   `lifting` at each cons step.

## What already exists to build on

All in `QOU/IwahoriHecke/` and `QOU/Machinery/`, all sorry-free:
`subword_property`, `bruhatLe_trans`, `bruhatLe_antisymm`, `lifting`,
`bruhatLe_mul_simple_of_isRightDescent`, `reflStep_of_eraseIdx`,
`exists_reduced_sublist'`, `matsumoto` / `matsumoto_An`.

## Consumer

A sibling arc (PR #6932, Murphy / Mathas Cor 3.8) is the only known consumer and
is unblocked WITHOUT this if it only uses `⊵` on the hypothesis side. Coordinate
before starting — asked on PR #6894, not yet answered.
