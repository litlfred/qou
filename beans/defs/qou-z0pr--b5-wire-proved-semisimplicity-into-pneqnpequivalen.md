---
# qou-z0pr
title: 'B5: wire proved semisimplicity into PNeqNpEquivalence — replace cited WenzlCriterion class; counting_faithfulness_of_one_lt fully proved modulo complexity citations only'
status: completed
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-08-29T17:53:37Z
---

## 2026-08-29 — CLOSED AS NOT ACHIEVABLE AS WRITTEN (negative result)

The bean asks to 'replace cited WenzlCriterion class; counting_faithfulness_of_one_lt
fully proved modulo complexity citations only'. **That cannot be done, and not for
a fixable reason.** Three measured facts, all verified against main:

1. **The consumer needs ALL ranks.** `counting_faithfulness_of_one_lt`
   instantiates `JonesComplexityCitations`'s `semisimple` parameter at
   `(∀ n, ss n)`. Finitely many proved ranks cannot entail a `∀ n` statement.
   This is not an artifact of the encoding: JVW #P-hardness genuinely needs
   unbounded rank, because the hard link family has unboundedly many strands.

2. **The three proved ranks are on three UNRELATED carrier types** —
   `H2 R q` (AdjoinRoot), `H3A`, `H4A`. There is no uniform object they are
   ranks OF.

3. **The one uniform family was ORPHANED.** `QOU.Hecke.IwahoriHecke` builds
   H_{n+1}(q) for general n as a RingQuot — and was imported by NO file, consumed
   by nothing, with zero isomorphisms to any concrete rank (verified by grep:
   `import QOU.Hecke.IwahoriHecke` had zero hits tree-wide).

## What was delivered instead

`QOU/Hecke/IwahoriHeckeRankOne.lean` (new, sorry-free, lean-direct exit 0,
#print axioms clean): the first consumer of the uniform family, giving the first
point of contact between it and a concrete rank —
`toAdjoinRoot : IwahoriHecke K q 1 →ₐ[K] AdjoinRoot (X²-(q-1)X-q)`
plus `toAdjoinRoot_σ` (non-degeneracy: σ₀ ↦ root) and `root_quad`.

Deliberately NOT claimed to be an isomorphism. The inverse is blocked on a named
Mathlib gap, now tracked as **qou-vu2d**: `AdjoinRoot.liftHom` needs a
commutative target, and there is no `CommRing (FreeAlgebra K (Fin 1))`.

No new class was introduced — discharging a class by adding another that assumes
the same content is the anti-laundering failure.
