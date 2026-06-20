import Mathlib.Tactic

/-!
# QOU.BraidKnot.frobenius_antipode_unifies — `S(σᵢ) = σᵢ⁻¹` unifies Term-5 + neutron tower

**Synthesis** ([`prop:frobenius-antipode-unifies-chirality-and-tower`](../../../quantum-observable-universe/braids-and-knots/frobenius-antipode-unifies-chirality-and-tower.md)).

*The Term-5 chirality factor and the neutron-tower closure both use
the **Frobenius antipode** `S : σ ↦ σ⁻¹` on `H_n(R, q)`.  `S` is an
anti-homomorphism: `S(ab) = S(b) S(a)`.*

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/frobenius-antipode-unifies-chirality-and-tower.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the Frobenius-antipode synthesis. -/
class FrobeniusAntipodeContext where
  /-- The Hecke algebra `H_n(R, q)`. -/
  A : Type
  /-- Multiplication on `A`. -/
  mul : A → A → A
  /-- The Hecke generator(s) `σᵢ ∈ A`. -/
  sigma : ℕ → A
  /-- The inverse generators `σᵢ⁻¹ ∈ A`. -/
  sigma_inv : ℕ → A
  /-- The Frobenius antipode `S : A → A`. -/
  S : A → A
  /-- Manuscript sub-claim — on generators, the antipode sends
      `σᵢ` to `σᵢ⁻¹`. -/
  claim_antipode_generator : ∀ i, S (sigma i) = sigma_inv i
  /-- Manuscript sub-claim — `S` is an anti-homomorphism:
      `S(a · b) = S(b) · S(a)`. -/
  claim_antipode_antihom : ∀ a b, S (mul a b) = mul (S b) (S a)

/-- **Frobenius antipode is the σ↦σ⁻¹ anti-homomorphism**
    ([`prop:frobenius-antipode-unifies-chirality-and-tower`]). -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/frobenius-antipode-unifies-chirality-and-tower.md
def frobenius_antipode_unifies
    [ctx : FrobeniusAntipodeContext] :
    (∀ i, ctx.S (ctx.sigma i) = ctx.sigma_inv i) ∧
    (∀ a b, ctx.S (ctx.mul a b) = ctx.mul (ctx.S b) (ctx.S a)) :=
  ⟨ctx.claim_antipode_generator, ctx.claim_antipode_antihom⟩

end QOU.BraidKnot
