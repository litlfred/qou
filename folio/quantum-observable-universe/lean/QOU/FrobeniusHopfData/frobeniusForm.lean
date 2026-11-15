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

/-- **Non-degeneracy of the Frobenius pairing**, at the level this model
can state it.

Let `(𝐂, A, τ)` be a [quantum universe](#def:quantum-universe) with
multiplication `μ : A ⊗ A → A` and Frobenius form `∫_A : A → 𝟏`.  The
manuscript claim is that the Frobenius pairing `∫_A ∘ μ` is
*non-degenerate* — inducing an iso `A ≅ A^∨` — **iff** it is bijective as
the underlying map (the snake identities, with a coevaluation
`η̃ : 𝟏 → A ⊗ A` whose two snake composites are `id_A`).

**Only the bijectivity half is stated here, and the loss is deliberate.**
`FrobeniusFormContext` models `A` and `A_dual` as plain `Type` and the
pairing as a plain function, so there is no categorical iso in scope to
put on the other side of the `↔`.  Stating bijectivity alone is weaker
than the manuscript claim and is what this model supports.

**The categorical half is now BUILT** — see
`QOU/FrobeniusHopfData/FrobeniusPairingCategorical.lean`, added 2026-09-07.
It states non-degeneracy over a monoidal category as the existence of a
coevaluation satisfying both snake identities *against the pairing the data
carries*, and `exactPairing_of_nondegenerate` turns that into Mathlib's
`ExactPairing`.  `#print axioms` on it reports **no axioms at all** — not
even `propext`.  The manuscript's non-degeneracy condition simply *is*
Mathlib's `ExactPairing`; what was missing was the right model, not
infrastructure.

That file does **not** assert the manuscript's *equivalence* with
bijectivity: that needs a faithful fibre functor `τ` reflecting
isomorphisms, and is deliberately left unstated.

**Why this docstring first said otherwise** (corrected 2026-09-07;
this paragraph first said it "needs the rigid-monoidal apparatus", which
implies a Mathlib gap that does not exist).  Mathlib carries
`CategoryTheory.Monoidal.Rigid` at the pinned revision — `ExactPairing`,
`rightDualIso` (`Rigid/Basic.lean:541`) and three further files, verified
on disk rather than recalled.  What is missing is local: this class does
not model a category at all.  Restating the two-sided claim means
re-modelling `FrobeniusFormContext` over a `MonoidalCategory` with an
`ExactPairing`, which Mathlib supports.  Cf.
`docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §U6, which
records that `Monoidal/Rigid/` and `Monoidal/Braided/` are present while
pivotal / spherical / ribbon are not.

**What was here until 2026-09-07, and why it went.**  The class carried
`is_iso : Prop` — a field typed with the *universe* `Prop`, so it held a
proposition as data — and this `def` read `ctx.is_iso ↔ Function.Bijective
ctx.pairing`.  The docstring called that the §3b pattern-C disposition,
resting on "the open state is honestly represented by the absence of an
instance".  That mechanism did not hold: the instance is one line, because
the instance chooses `is_iso`.  Measured, `lean`-direct exit 0:

    example (X Y : Type) (p : X → Y) : ∃ ctx : FrobeniusFormContext,
        FrobeniusForm ctx :=
      ⟨{ A := X, A_dual := Y, pairing := p,
         is_iso := Function.Bijective p }, Iff.rfl⟩

So the old `FrobeniusForm` held for **every** pairing datum and asserted
nothing.  The `example` below shows the replacement is refutable, which
is the property the old form could not offer. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-universes/frobenius-pairing.ts
def FrobeniusForm (ctx : FrobeniusFormContext) : Prop :=
    Function.Bijective ctx.pairing

/-- The statement has content: it is FALSE for some pairing data.

    This is what the previous form could not offer. With `is_iso : Prop`
    free, `FrobeniusForm` was `ctx.is_iso ↔ Function.Bijective ctx.pairing`
    and an instance existed for *every* pairing data — measured, not
    argued:

        ⟨{ A := X, A_dual := Y, pairing := p,
           is_iso := Function.Bijective p }, Iff.rfl⟩

    compiles for arbitrary `X`, `Y`, `p` (`lean`-direct exit 0,
    2026-09-07). So the pattern-C honesty mechanism the docstring above
    relied on — "the open state is honestly represented by the absence of
    an instance" — did not hold: the instance was one line. -/
example : ¬ FrobeniusForm { A := Bool, A_dual := Unit, pairing := fun _ => () } := by
  intro h
  have hbad : (true : Bool) = false := h.1 rfl
  exact Bool.noConfusion hbad

end QOU.FrobeniusHopfData
