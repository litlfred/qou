---
# qou-fr7j
title: 'Certify n>=9 triangulations: iterate Fin.prod_univ_succ past Mathlib eight-tetrahedron ceiling'
status: todo
type: task
created_at: 2026-08-15T15:48:26Z
updated_at: 2026-08-15T15:48:26Z
---


Successor to `qou-glhi`, which delivered edge identities for 27 manifolds at shape-field
degrees 2–14 and certified 16 of them as `ShapedTriangulation.SatisfiesEdgeEquations`.

## The limit, stated exactly

`scripts/gen-gluing-lean.py`'s `emit_certification` unfolds `∏ i, …` over `Fin n` with
`Fin.prod_univ_{two..eight}`. **Mathlib provides those and stops at eight.** So every
manifold with `n ≥ 9` tetrahedra gets a comment instead of a certification:

```
-- 9_35: 9 tetrahedra — no `Fin.prod_univ_9` in Mathlib, so the
-- certification template does not apply.  Needs iterated
-- `Fin.prod_univ_succ`.  NOT emitted rather than emitted broken.
```

Currently uncertified for this reason: **9₃₅**, **o9_00000** (both n = 9), **10₁₀₀**
(n = 14). Their standalone edge identities exist and are proved — `GeneratedGluing.lean`
for the first two, `GeneratedGluingHigh.lean` for 10₁₀₀. Only the wrapper is missing.

## What to do

`Fin.prod_univ_succ` iterates to any `n`; the question is whether the resulting goal still
reduces under the template's full `simp`. **Do not assume it does.** `glhi` recorded three
separate failures where the mathematics was right and a *tactic state* was wrong, and two
of them were exactly about `Fin`-indexed matrix applications not reducing:

1. `fin_cases k` leaves `⟨0, ⋯⟩`, on which `Matrix.cons_val_zero` does not fire;
2. there is no `Matrix.cons_val_four`, and `cons_val_succ` does not fire on a literal
   `4 : Fin 5`, so a curated `simp only` silently stops at n ≥ 5 — full `simp` is required.

Both failed with a bare "ring expressions not equal", which reads as a wrong cofactor and
sends you to check arithmetic that was already asserted exact. Expect a third variant of
the same thing here and **dump the goal with `trace_state` early** rather than
re-deriving cofactors.

Cheapest probe: take **9₃₅** (n = 9, one past the ceiling) and try to certify just it by
hand. If that works, generalise the emitter; if it does not, the failure at n = 9 is the
whole finding and 10₁₀₀ at n = 14 will not behave differently.

## Also worth doing while here

**Degrees beyond 14 are untested.** `glhi` predicted a compile-time wall in 7–14 and there
wasn't one — 10₁₀₀ at degree 14, 384 KB, with a 30,193-character cofactor, builds in 131 s.
It also found that cost tracks the **number** of `ring` normalisations rather than the size
of any one, so wide-but-few is cheap. Route 75's reach is the real constraint on what can
be attempted, not Lean's. Worth finding where the actual ceiling is, now that the
predicted one turned out to be imaginary.
