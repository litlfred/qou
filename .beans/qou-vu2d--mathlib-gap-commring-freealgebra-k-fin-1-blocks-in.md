---
# qou-vu2d
title: 'Mathlib gap: CommRing (FreeAlgebra K (Fin 1)) — blocks inverting the rank-1 Iwahori-Hecke comparison map'
status: scrapped
type: task
priority: normal
created_at: 2026-08-29T17:53:01Z
updated_at: 2026-08-29T18:13:51Z
---

## The gap, exactly

`AdjoinRoot.liftHom` requires a **commutative** target. `IwahoriHecke K q 1`
(= H2(q), the RingQuot of FreeAlgebra K (Fin 1) by the Hecke quadratic) carries
only `Ring`. `RingQuot` inherits `CommRing` **solely** from a `CommRing` base
(Mathlib/Algebra/RingQuot.lean:362), and Mathlib has NO
`CommRing (FreeAlgebra K (Fin 1))` — no instance, and no
`FreeAlgebra K (Fin 1) ≃ₐ[K] K[X]` to transport one along (measured 2026-08-29).

## Why it matters

It is the ONLY thing blocking the inverse of
`QOU.Hecke.IwahoriHecke.toAdjoinRoot` (new, sorry-free, this branch), which
would give the first isomorphism between the uniform general-n Iwahori-Hecke
family and a concrete rank object. Supply commutativity and the rank-1
identification `IwahoriHecke K q 1 ≅ K[X]/(X²-(q-1)X-q)` follows immediately,
and semisimplicity transports from the proved H2 result.

## Scope

Small, self-contained, independently worthwhile as a Mathlib contribution, and
far better specified than 'the T_w basis'. Free algebra on a ONE-element
generating set is commutative — the content is an equiv to the polynomial ring.

## What it does NOT buy

Nothing about P!=NP. `counting_faithfulness_of_one_lt` needs `(∀ n, ss n)`;
no finite set of ranks entails that. See qou-z0pr and
docs/audits/2026-08-29-pneqnp-gap-inventory-refresh.md §3.2.

## 2026-08-29 — SCRAPPED: my premise was wrong, the inverse is BUILT

This bean claimed the rank-1 inverse was blocked on a missing
`CommRing (FreeAlgebra K (Fin 1))`. **Every factual statement in it is true and
the conclusion drawn from them is false.** It IS true that:
`AdjoinRoot.liftHom` requires a commutative target; `IwahoriHecke K q 1` carries
only `Ring`; `RingQuot` inherits `CommRing` solely from a `CommRing` base; and
Mathlib has no `CommRing (FreeAlgebra K (Fin 1))`.

**But `AdjoinRoot.liftHom` is not the only way out of an `AdjoinRoot`.** Mathlib
carries `Polynomial.eval₂AlgHom'`, which evaluates into a NONCOMMUTATIVE algebra
given only that scalars commute with the chosen element (`Algebra.commutes`
supplies exactly that), and `Ideal.Quotient.liftₐ` descends it through the
quotient. Composing the two builds the inverse with no commutativity hypothesis
anywhere.

Landed sorry-free in QOU/Hecke/IwahoriHeckeRankOne.lean:
`evalSigma`, `evalSigma_heckePoly`, `fromAdjoinRoot`, `fromAdjoinRoot_root`,
`rankOneEquiv : IwahoriHecke K q 1 ≃ₐ[K] AdjoinRoot (X²-(q-1)X-q)`, and
`commute_rankOne` — commutativity of H₂(q) falls out as a COROLLARY of the
isomorphism rather than being a prerequisite for it. All 9 decls #print axioms
clean.

**The lesson, which is the durable part:** 'this construction, via this API, does
not go through' is a scope-(a) negative about a route. It is not a structural
exclusion and must not be written down as one. No invariant forbade the inverse;
only the obvious lemma did not apply. Recorded in the file's own docstring as a
retraction so the next reader sees it.
