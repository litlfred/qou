---
# qou-wcff
title: 'GAP: genus-filtration-ideal.lean carries two definitional-tautology decls the vacuity ledger never saw'
status: todo
type: task
created_at: 2026-08-15T22:41:43Z
updated_at: 2026-08-15T22:41:43Z
---

## What

Found while judging the `qou-5r17` derivation-claim candidates (`qou-1tls`).
The prose side is fixed on this branch; this bean is the Lean side, which is
outside that task's remit.

[`content/quantum-observable-universe/brings-surface/genus-filtration-ideal.lean`](../content/quantum-observable-universe/brings-surface/genus-filtration-ideal.lean)
has two `theorem`s whose **docstrings carry the file's non-trivial content**
and whose **statements carry none of it**:

1. `chebyshev_degree_eq_genus` — docstring: *"the polynomial degree of `a_p`
   in `u = s²` equals `(p-1)/2`. This is the non-trivial content: the
   algebraic complexity (Chebyshev degree) equals the topological complexity
   (Seifert genus). Stated as an opaque axiom because the full polynomial ring
   formalization is deferred."* The actual conclusion is
   `seifertGenus_T2p p = (p - 1) / 2`, closed `by intros; rfl`. Since
   `def seifertGenus_T2p (p : ℕ) : ℕ := (p - 1) / 2`, that is
   `(p-1)/2 = (p-1)/2`. `heckeCoeff` and `s` are bound in the statement and
   never appear in the conclusion.

2. `leading_chebyshev_coeff_is_one` — docstring: *"the coefficient of
   `s^{p-1}` (equivalently `u^{(p-1)/2}`) in `heckeCoeff s p` is 1. Stated as
   opaque axiom."* The actual conclusion is the `heckeCoeff` recurrence with
   `- s^(p-1)` added to both sides, closed by `ring`. It is a rearrangement of
   the defining equation and says nothing about a leading coefficient.

## Why it escaped every checker

`lean-vacuity-axiom-audit.ts` keys on **syntactic** tautologies (`: True`,
`X = X := rfl`). These are **definitional** tautologies: `A = B` where `A`
unfolds to `B`. Measured: `genus-filtration-ideal` appears **0 times** in
[`docs/audits/lean-vacuity-review-ledger.json`](../docs/audits/lean-vacuity-review-ledger.json),
and neither decl name appears at all. The file is a content-block sibling, so
it is in scope — it simply does not trip the pattern.

Note also that bean `491r` ("Prove genus_filtration_ideal", 2026-06-23) is
marked **completed** with an empty body, which reads as an all-clear over a
file whose two load-bearing declarations prove nothing.

## Two things to do

- **Instance:** discharge both honestly — state the real proposition (degree
  in `u`, leading coefficient) and prove it, or state it with `sorry` +
  `-- Ref:` per AGENTS.md §1. A docstring that says "stated as an opaque
  axiom" beside a `theorem … := by rfl` is the §1a audit-dodge shape: it is
  strictly worse than an `axiom`, because an `axiom` is visible to
  `#print axioms` and this is not.
- **Checker:** extend the vacuity detector to flag `theorem X : A = B` where
  `A` and `B` are definitionally equal after unfolding the file's own `def`s
  (whnf compare), not only where they are syntactically identical. This is a
  recall gap, not a one-off.
