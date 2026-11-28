import QOU.InformationTheory.HochschildH1

/-!
# QOU.Information.BlockRigidity — derivations and automorphisms respect the blocks

Human statement (`prop:block-rigidity`). Let `A` be an associative algebra over a
commutative ring `R`, and let `z ∈ A` be a central idempotent (`z² = z`, `z` commutes
with everything). Then:

1. every derivation `D` of `A` kills `z`, so `D (z a) = z D(a)` and `D` maps the block
   `z A` into itself (`derivation_centralIdempotent_eq_zero`,
   `derivation_mul_centralIdempotent`);
2. every algebra automorphism sends central idempotents to central idempotents
   (`algEquiv_centralIdempotent`);
3. every inner automorphism `x ↦ u x u⁻¹` fixes every central element, so an
   automorphism that moves a central element is not inner (`conj_central`,
   `not_inner_of_moves_central`).

For a split semisimple Hecke algebra the central primitive idempotents are the
Wedderburn block units, so (1) says no derivation mixes blocks, and (3) says the only
way an automorphism can fail to be inner at the level of the centre is by permuting
blocks. Base ring generic (§7c): no field, no characteristic, no `ℝ`.
-/

namespace QOU.Information

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- `z` is a **central idempotent**: `z * z = z` and `z` commutes with every element. -/
def IsCentralIdempotent (z : A) : Prop := z * z = z ∧ ∀ a : A, Commute z a

/-- **Every derivation kills every central idempotent.** From `D z = D(z²) = 2 z D z`,
    multiplying by `z` gives `z D z = 2 z D z`, so `z D z = 0` and `D z = 0`. -/
theorem derivation_centralIdempotent_eq_zero {D : A →ₗ[R] A} (hD : IsDerivation D)
    {z : A} (hz : IsCentralIdempotent z) : D z = 0 := by
  obtain ⟨e, hc⟩ := hz
  have h : D z = z * D z + z * D z := by
    have h0 := hD z z
    rw [e, ← (hc (D z)).eq] at h0
    exact h0
  have h2 : z * D z = z * D z + z * D z := by
    calc z * D z = z * (z * D z + z * D z) := by rw [← h]
      _ = (z * z) * D z + (z * z) * D z := by rw [mul_add, mul_assoc]
      _ = z * D z + z * D z := by rw [e]
  have h3 : z * D z = 0 := by
    calc z * D z = (z * D z + z * D z) - z * D z := by abel
      _ = z * D z - z * D z := by rw [← h2]
      _ = 0 := sub_self _
  rw [h, h3, add_zero]

/-- **A derivation commutes with multiplication by a central idempotent**, so it maps
    the block `z A` into itself. -/
theorem derivation_mul_centralIdempotent {D : A →ₗ[R] A} (hD : IsDerivation D)
    {z : A} (hz : IsCentralIdempotent z) (a : A) : D (z * a) = z * D a := by
  rw [hD, derivation_centralIdempotent_eq_zero hD hz, zero_mul, zero_add]

/-- **Automorphisms permute central idempotents.** -/
theorem algEquiv_centralIdempotent (φ : A ≃ₐ[R] A) {z : A} (hz : IsCentralIdempotent z) :
    IsCentralIdempotent (φ z) := by
  refine ⟨?_, fun a => ?_⟩
  · rw [← map_mul, hz.1]
  · obtain ⟨b, rfl⟩ := φ.surjective a
    show φ z * φ b = φ b * φ z
    rw [← map_mul, ← map_mul, (hz.2 b).eq]

/-- **Inner automorphisms fix central elements**: `u z u⁻¹ = z`. -/
theorem conj_central {z : A} (hz : ∀ a : A, Commute z a) (u : Aˣ) :
    (u : A) * z * ((u⁻¹ : Aˣ) : A) = z := by
  rw [← (hz u).eq, mul_assoc, Units.mul_inv, mul_one]

/-- **An automorphism that moves a central element is not inner.** -/
theorem not_inner_of_moves_central (φ : A ≃ₐ[R] A) {z : A} (hz : ∀ a : A, Commute z a)
    (hmove : φ z ≠ z) : ¬ ∃ u : Aˣ, ∀ x : A, φ x = (u : A) * x * ((u⁻¹ : Aˣ) : A) := by
  rintro ⟨u, hu⟩
  exact hmove (by rw [hu]; exact conj_central hz u)

end QOU.Information
