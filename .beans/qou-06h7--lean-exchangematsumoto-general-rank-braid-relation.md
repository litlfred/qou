---
# qou-06h7
title: 'Lean: exchange/Matsumoto general-rank braid relation'
status: todo
type: task
priority: normal
created_at: 2026-07-19T02:57:13Z
updated_at: 2026-09-05T16:45:29Z
---

## Measured 2026-09-05 (branch claude/hecke-cyclicity-markov-2026-09-05, PR #6845)

Re-measured against the pinned Mathlib (v4.24.0, the toolchain in
`lean-toolchain`), because an earlier claim of mine — "zero occurrences of
`exchange`/`deletion` in `Mathlib/GroupTheory/Coxeter/`" — was true but weaker
than what is actually there.

`Mathlib/GroupTheory/Coxeter/` is four files: `Basic.lean`, `Length.lean`,
`Inversion.lean`, `Matrix.lean`. Grepping all four case-insensitively for
`exchange|matsumoto|deletion` returns **exactly one line**, and it is
`Basic.lean:78`, inside Mathlib's own TODO list:

    * State and prove Matsumoto's theorem.

So the status is not "Mathlib might have it under another name" — Mathlib
states, in its own file header, that it does not. There is no exchange
property, no deletion condition, no geometric representation, and nothing in
the tree imports `Inversion.lean`.

## What is and is not blocked by this

The *algebra* half of Matsumoto is already proved in this corpus and is not
waiting on anything:
`QOU/IwahoriHecke/BraidWordInvariance.lean` has `heckeWord_eq_of_braidMove`,
its closure `heckeWord_eq_of_braidEquiv`, and `exists_Tw_of_braidEquiv` — the
conditional theorem that produces a well-defined `T_w` **given** the group
half as a named hypothesis. That is the honest form of the deferral.

The *group* half — any two reduced expressions for `w ∈ W` are related by a
chain of braid moves — is what is open, and it is a fact about the Coxeter
group, not about the Hecke algebra. Proving it is Mathlib-scale work
(exchange property → deletion condition → Matsumoto), not a session's task,
and it should be done as a Mathlib contribution rather than in `QOU/`.

**Do NOT reach for this to fix injectivity of the R-matrix action.** At the
`Fin 2` fibre that action is non-injective *by theorem* for `n ≥ 3` (kernel
`ker(H_n ↠ TL_n)`, dimension `n! − Catalan(n)` = 1, 10, 78, 588, 4611, 38890 at
n = 3…8), so no amount of basis machinery makes it injective. Matsumoto buys
the **rank** of `H_n(q)`, which is worth having for its own sake. Recorded in
`QOU/IwahoriHecke/TensorEmbedding.lean` §"What `heckeActionN` does NOT say".
