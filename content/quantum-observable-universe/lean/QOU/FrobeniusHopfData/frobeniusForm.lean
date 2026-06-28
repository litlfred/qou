import Mathlib.Logic.Function.Basic

/-!
# QOU.FrobeniusHopfData.frobeniusForm

Canonical Lean declaration for content block at
[`quantum-observable-universe/quantum-universes/frobenius-pairing.ts`](quantum-observable-universe/quantum-universes/frobenius-pairing.ts).

The `lean.ref` URI `qou:QOU.FrobeniusHopfData.frobeniusForm` resolves to
`FrobeniusForm` below.

The manuscript claim — that the Frobenius pairing `∫_A ∘ μ` is
non-degenerate (induces an iso `A ≅ A^∨`) iff the snake identities
hold — is irreducibly abstract over the opaque categorical objects `A`,
`A^∨` and the opaque iso predicate `is_iso`.  No faithful Mathlib
structure reduces it (it would require the full rigid-monoidal snake-
identity apparatus on the specific quantum universe), so this is
pattern C of the vacuity-fix playbook: the context class carries the
pairing data and `FrobeniusForm` **names** the conditional conjecture
as a `Prop` (honestly *not asserted* — no `theorem … := ctx.claim_*`
self-assuming projection; an instance discharging it is the open claim).
-/

namespace QOU.FrobeniusHopfData

/-- Pairing data for the `frobeniusForm` claim. -/
class FrobeniusFormContext where
  /-- Categorical object `A`. -/
  A : Type
  /-- Dual object `A^∨`. -/
  A_dual : Type
  /-- The Frobenius-pairing-induced map `A → A^∨`. -/
  pairing : A → A_dual
  /-- Predicate: the pairing is non-degenerate, i.e. `pairing` is
      an isomorphism (the snake-identity / iso content). -/
  is_iso : Prop

/-- **Manuscript statement** (non-degeneracy of the Frobenius pairing),
named as a `Prop`:

Let `(𝐂, A, τ)` be a [quantum universe](#def:quantum-universe) with
multiplication `μ : A ⊗ A → A` and Frobenius form `∫_A : A → 𝟏`.  The
Frobenius pairing `∫_A ∘ μ` is *non-degenerate* — inducing an iso
`A ≅ A^∨` (`is_iso`) — **iff** it is bijective as the underlying map
(the snake identities, with a coevaluation `η̃ : 𝟏 → A ⊗ A` such that
both snake composites equal `id_A`).

This is the §3b "name the conditional conjecture" disposition (pattern
C): `FrobeniusForm ctx` is the proposition the manuscript conjectures
for the pairing data `ctx`; the open state is honestly represented by
the absence of an instance.  It is *not* a self-assuming projection. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-universes/frobenius-pairing.ts
def FrobeniusForm (ctx : FrobeniusFormContext) : Prop :=
    ctx.is_iso ↔ Function.Bijective ctx.pairing

end QOU.FrobeniusHopfData
