---
# qou-y7ea
title: Drain the 13 q-codifferential axioms to a LinearMap-bundled structure
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T12:09:52Z
updated_at: 2026-10-04T15:12:24Z
parent: qou-6qbv
---

## What was there

`content/quantum-observable-universe/quantum-observable-universes/q-codifferential-formula-prop.lean`
carried **13 `axiom` declarations** — the largest single concentration of
`[manuscript]`-cited axioms in the corpus (12 of the 59 pure-manuscript
axioms measured in the 2026-09-03 cited-not-proved witness). They split
three ways:

- **structure, not claims** (5): `DiffForm : Type u`, its `AddCommMonoid`
  and `Module` instances, and the two bilinearity axioms on `websterInner`;
- **data** (7): the six geometric operators plus `d_q`;
- **claims** (3 adjointness relations + `adjoint_exists_unique'` +
  `d_q_decomposition'`).

## What it is now

One `structure ContactFormAlgebra R F` over `[AddCommGroup F] [Module R F]`,
with the pairing typed `F →ₗ[R] F →ₗ[R] R` and the operators `F →ₗ[R] F`.
**Zero axioms**; every declaration `#print axioms` to `[propext, Quot.sound]`.

- The 5 structure axioms are discharged by the Mathlib binders and by
  `LinearMap` being bilinear by construction — which also deletes the four
  helper lemmas (`hzl`/`hzr`/`hsl`/`hsr`) the old proof derived by hand.
- `d_q` + `d_q_decomposition'` become one `def` whose decomposition is `rfl`.
- The 3 adjointness relations become structure fields; the main theorem
  genuinely *derives* the closed form from them (§3b-cond item 5 — not a
  self-assuming projection).

## The finding

`axiom adjoint_exists_unique'` quantified over an **arbitrary function**
`L : DiffForm R → DiffForm R`, not a linear map, and asserted `∃!` with no
non-degeneracy hypothesis. Both halves are wrong and both are now Lean-proved
wrong rather than merely argued:

- `additive_of_hasAdjoint` — having an adjoint forces `α ↦ ⟨L α, β⟩` to be
  additive, because `⟨α, L* β⟩` is. So an adjoint for *every* function forces
  the pairing to see every function as additive. Contrapositive:
  `not_hasAdjoint_of_not_additive`.
- `degenerate_adjoint_not_unique` — in the zero-pairing model (a genuine
  `ContactFormAlgebra`), every function is an adjoint of `d`, so over a
  nontrivial module the adjoint is not unique. Scope-(b): a model of
  everything else in which the `∃!` is false.

Repaired uniqueness is `δq_unique`, under the hypothesis it actually needs
(right non-degeneracy) — and `degenerate_not_nondegenerate` shows that
hypothesis is not free.

## Residual gap, stated

No **geometric** `ContactFormAlgebra` is constructed (Tanaka–Webster
connection on a strictly pseudoconvex CR manifold, or the Markov-trace
pairing over `ℤ[q,q⁻¹]`). The theorems are conditional on being handed one,
and that is visible in every signature. `#print axioms` reads clean because
the gap moved into the hypotheses — which is the improvement, and is not the
same as the geometry having been built.

## Verification

`lean`-direct **exit 0** against the real import cone; `#print axioms` clean
on all 9 declarations. Zero consumers: the 11 other files matching
`d_classical` / `DiffForm` were checked one by one and every hit is an
unrelated field of `CategoricalQExtDeriv` or the word "classical" in another
context — nothing imports `QOU.QuantumGeometry`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
