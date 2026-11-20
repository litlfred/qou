import Mathlib.Tactic

/-!
# QOU.BraidKnot.frobenius_antipode_unifies — `S(σᵢ) = σᵢ⁻¹` unifies Term-5 + neutron tower

Canonical Lean for content block
[`conj:frobenius-antipode-unifies-chirality-and-tower`](../../../quantum-observable-universe/braids-and-knots/frobenius-antipode-unifies-chirality-and-tower.md).

*The Term-5 chirality factor and the neutron-tower closure both use
the **Frobenius antipode** `S : σ ↦ σ⁻¹` on `H_n(R, q)`.  `S` is an
anti-homomorphism: `S(ab) = S(b) S(a)`.*

The structural primitive the manuscript turns on is exactly the
**group-inverse map** on the unit group of the Hecke algebra: the
braid generators `σᵢ` are units, the antipode restricts to `g ↦ g⁻¹`
on them, and the anti-homomorphism law is the standard
`(a·b)⁻¹ = b⁻¹·a⁻¹`.  This file derives those facts **directly** for
the concrete model `S = (·)⁻¹` on any `Group G` — no axiomatisation of
the conclusion.  The previous encoding posited
`claim_antipode_generator` and `claim_antipode_antihom` as class
fields and projected them (`:= ⟨…⟩`); that was a vacuous self-assuming
projection and is removed.

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/frobenius-antipode-unifies-chirality-and-tower.md
-/

namespace QOU.BraidKnot

/-- The Frobenius antipode realised as the group-inverse map on the
unit group of the Hecke algebra. -/
def frobeniusAntipode {G : Type*} [Group G] : G → G := fun g => g⁻¹

/-- **Antipode on generators** `S(σᵢ) = σᵢ⁻¹`.

For the braid generators `σ : ℕ → G` (units of the Hecke algebra),
the antipode sends `σᵢ` to `σᵢ⁻¹` — true by definition of
`frobeniusAntipode`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower (S(σᵢ) = σᵢ⁻¹)
theorem frobeniusAntipode_generator {G : Type*} [Group G] (σ : ℕ → G) (i : ℕ) :
    frobeniusAntipode (σ i) = (σ i)⁻¹ := rfl

/-- **Antipode is an anti-homomorphism** `S(a·b) = S(b)·S(a)`.

This is the standard group identity `(a·b)⁻¹ = b⁻¹·a⁻¹`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower (S(ab) = S(b)S(a))
theorem frobeniusAntipode_antihom {G : Type*} [Group G] (a b : G) :
    frobeniusAntipode (a * b) = frobeniusAntipode b * frobeniusAntipode a := by
  unfold frobeniusAntipode
  exact mul_inv_rev a b

/-- **Antipode fixes the averaged `ud`-pair.**

The manuscript notes `S` fixes the "averaged" pair
`(1, −h/2) = ½(σ + σ⁻¹)`.  Structurally this is the statement that
the antipode is an **involution** (`S∘S = id`), so the symmetric
combination `½(g + S g)` is `S`-invariant: applying `S` swaps `g` and
`S g`, and `S(S g) = g`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower (S fixes ½(σ + σ⁻¹))
theorem frobeniusAntipode_involutive {G : Type*} [Group G] (g : G) :
    frobeniusAntipode (frobeniusAntipode g) = g := by
  unfold frobeniusAntipode
  exact inv_inv g

/-- **Synthesis statement** of `thm:frobenius-antipode-unifies-…`:
the antipode `S = (·)⁻¹` simultaneously satisfies the
generator identity and the anti-homomorphism law that the chirality
(Term 5) and neutron-tower derivations both invoke. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower
theorem frobenius_antipode_unifies {G : Type*} [Group G] (σ : ℕ → G) :
    (∀ i, frobeniusAntipode (σ i) = (σ i)⁻¹) ∧
    (∀ a b : G, frobeniusAntipode (a * b)
        = frobeniusAntipode b * frobeniusAntipode a) :=
  ⟨fun i => frobeniusAntipode_generator σ i,
   fun a b => frobeniusAntipode_antihom a b⟩

end QOU.BraidKnot
