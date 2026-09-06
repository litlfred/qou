---
# qou-3k66
title: 'Lean: BruhatLe (subword) -> ReflLe (reflection) — the converse bridge'
status: todo
type: task
priority: normal
created_at: 2026-09-06T11:10:51Z
updated_at: 2026-09-06T12:01:42Z
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


## 🛑 CORRECTION 2026-09-06 — the "missing statement" recorded above is FALSE, and it was mine

This bean stated the blocker as:

> A subword of an **arbitrary** (not necessarily reduced) word for `w` still
> gives `u ≤ w`.

**That is not merely unproved. It is false**, and the counterexample is one
line: `π [i, i] = 1` while `π [i] = sᵢ`, and `[i] <+ [i, i]`. The claim would
give `sᵢ ≤ 1`, which `bruhatLe_one_iff` turns into `sᵢ = 1`, contradicting
`ℓ(sᵢ) = 1`.

Formalized as `QOU.IwahoriHecke.BruhatReflection.not_forall_bruhatLe_of_sublist`
rather than left as prose, because it is a plausible thing to reach for and the
prose form of it stood in the file for one commit. Both "route 1" and "route 2"
listed above route through it and are therefore **dead**; do not attempt them.

**This is the SECOND wrong diagnosis I have written for this same converse.**
The first was "the blocker is the lifting property" — lifting was then proved in
the same file and the converse still did not follow.

## Where the difficulty actually sits

Induct on `ℓ(w)`, with `ω = ω₁ ++ [s]` reduced for `w`, and split the reduced
witness `ω'` for `u`:

* `ω' <+ ω₁` — then `u ≤ w·s`, the IH gives `u ≤ᵣ w·s`, and `w·s →ᵣ w` is one
  reflection step. **This branch closes.**
* `ω' = a ++ [s]` — then `u·s ≤ w·s` and the IH gives `u·s ≤ᵣ w·s`. What is
  needed is `u ≤ᵣ w`, i.e. an **upward lifting property for `≤ᵣ`**:

  > if `x ≤ᵣ y` and `s` is a right ASCENT of both `x` and `y`, then
  > `x·s ≤ᵣ y·s`.

  **This is the open statement.** It is not the lifting property already proved
  (that one is about `≤` and a right *descent*).

## What is already proved toward it

`BruhatReflection.reflStep_mul_simple` — the **single-step** case of that upward
lifting, sorry-free: if `y = x·t` is one upward reflection step and `s` is an
ascent of both, then `x·s → y·s` is one too, via the conjugate reflection
`s t s`, with `ℓ(x·s) = ℓ(x)+1 < ℓ(y)+1 = ℓ(y·s)`.

**What fails is the chain.** A `ReflLe` is a `ReflTransGen`; nothing forces `s`
to remain an ascent at the intermediate elements, and `ReflStep` is not defined
for a descent. Closing that is the whole remaining problem.
