---
# qou-vu2d
title: 'Mathlib gap: CommRing (FreeAlgebra K (Fin 1)) — blocks inverting the rank-1 Iwahori-Hecke comparison map'
status: todo
type: task
priority: normal
created_at: 2026-08-29T17:53:01Z
updated_at: 2026-08-29T17:53:37Z
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
