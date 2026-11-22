import QOU.MathlibExt.BraidGroup
import Mathlib.Tactic.Group

/-!
# A bond conjugate to its mirror has writhe 0 (issue #8879)

The mirror `σᵢ ↦ σᵢ⁻¹` is an automorphism of the braid group; in the Hecke algebra it is the
bar involution `σᵢ ↦ σᵢ⁻¹, q ↦ q⁻¹` on the braid part. The writhe (`exponentSum`, well defined
on the group) changes sign under it and is constant on conjugacy classes. So a braid conjugate
to its own mirror has writhe `0` (`writhe_eq_zero_of_conj_mirror`). This is a candidate
derivation of the one premise left in the H₂ bond selection (`pure_writhe_zero_bonds`): it trades
"writhe 0" for "the bond is achiral", i.e. invariant under the mirror up to conjugation.

The Borromean step `V³ = (σᵢσᵢ₊₁⁻¹)³` is conjugate to its mirror (`mirror_vPow_three_conj`), so
it meets the premise; `σ₅²` (writhe 2) does not.

No numerical value enters. -- Ref: [leitner2026] prop:ilp-covalent-bond; issue #8879
-/

namespace QOU.Molecular.H2BondMirror

open QOU.MathlibExt.Braid

variable {n : ℕ}

theorem of_eq_σ (i : Fin n) : PresentedGroup.of (rels := braidRelators n) i = σ i := rfl

/-- The Artin braid relation in `BraidGroup n`. -/
theorem braid_rel (i : Fin n) (h : (i : ℕ) + 1 < n) :
    σ i * σ ⟨(i : ℕ) + 1, h⟩ * σ i = σ ⟨(i : ℕ) + 1, h⟩ * σ i * σ ⟨(i : ℕ) + 1, h⟩ := by
  have hr := PresentedGroup.one_of_mem (rels := braidRelators n)
    (x := FreeGroup.of i * FreeGroup.of ⟨(i : ℕ) + 1, h⟩ * FreeGroup.of i *
      (FreeGroup.of ⟨(i : ℕ) + 1, h⟩ * FreeGroup.of i * FreeGroup.of ⟨(i : ℕ) + 1, h⟩)⁻¹)
    (Or.inr ⟨i, h, rfl⟩)
  simp only [map_mul, map_inv] at hr
  exact mul_inv_eq_one.mp hr

/-- Far commutation in `BraidGroup n`. -/
theorem far_comm (i j : Fin n) (h : (i : ℕ) + 2 ≤ (j : ℕ)) : σ i * σ j = σ j * σ i := by
  have hr := PresentedGroup.one_of_mem (rels := braidRelators n)
    (x := FreeGroup.of i * FreeGroup.of j * (FreeGroup.of i)⁻¹ * (FreeGroup.of j)⁻¹)
    (Or.inl ⟨i, j, h, rfl⟩)
  simp only [map_mul, map_inv] at hr
  have : σ i * σ j * (σ i)⁻¹ * (σ j)⁻¹ = 1 := hr
  calc σ i * σ j = (σ i * σ j * (σ i)⁻¹ * (σ j)⁻¹) * (σ j * σ i) := by group
    _ = σ j * σ i := by rw [this, one_mul]

theorem mirror_relators : ∀ r ∈ braidRelators n,
    (FreeGroup.lift fun i : Fin n => (σ i)⁻¹) r = 1 := by
  rintro r (⟨i, j, hij, rfl⟩ | ⟨i, h, rfl⟩)
  · simp only [map_mul, map_inv, FreeGroup.lift_apply_of, inv_inv]
    have hc := far_comm i j hij
    calc (σ i)⁻¹ * (σ j)⁻¹ * σ i * σ j = (σ i)⁻¹ * (σ j)⁻¹ * (σ j * σ i) := by
          rw [← hc]; group
      _ = 1 := by group
  · simp only [map_mul, map_inv, FreeGroup.lift_apply_of]
    have hb := braid_rel i h
    calc (σ i)⁻¹ * (σ ⟨(i : ℕ) + 1, h⟩)⁻¹ * (σ i)⁻¹ *
          (σ ⟨(i : ℕ) + 1, h⟩ * σ i * σ ⟨(i : ℕ) + 1, h⟩)
        = (σ i * σ ⟨(i : ℕ) + 1, h⟩ * σ i)⁻¹ *
          (σ ⟨(i : ℕ) + 1, h⟩ * σ i * σ ⟨(i : ℕ) + 1, h⟩) := by group
      _ = 1 := by rw [hb, inv_mul_cancel]

/-- **The mirror** `σᵢ ↦ σᵢ⁻¹`, as an endomorphism of the braid group. -/
def mirror (n : ℕ) : BraidGroup n →* BraidGroup n := PresentedGroup.toGroup mirror_relators

@[simp] theorem mirror_σ (i : Fin n) : mirror n (σ i) = (σ i)⁻¹ :=
  PresentedGroup.toGroup.of _

/-- **The mirror negates the writhe.** -/
theorem exponentSum_mirror (b : BraidGroup n) :
    exponentSum n (mirror n b) = (exponentSum n b)⁻¹ := by
  have : (exponentSum n).comp (mirror n) = (exponentSum n)⁻¹ := by
    apply PresentedGroup.ext
    intro i
    show exponentSum n (mirror n (σ i)) = (exponentSum n (σ i))⁻¹
    rw [mirror_σ, map_inv]
  exact DFunLike.congr_fun this b

/-- **A braid conjugate to its mirror has writhe `0`.** -/
theorem writhe_eq_zero_of_conj_mirror (b c : BraidGroup n) (h : mirror n b = c * b * c⁻¹) :
    exponentSum n b = 1 := by
  have h1 := exponentSum_mirror b
  rw [h, map_mul, map_mul, map_inv, mul_comm (exponentSum n c), mul_assoc,
    mul_inv_cancel, mul_one] at h1
  have h2 : Multiplicative.toAdd (exponentSum n b) = -Multiplicative.toAdd (exponentSum n b) := by
    conv_lhs => rw [h1]
    rfl
  have h3 : Multiplicative.toAdd (exponentSum n b) = 0 := by omega
  simpa using congrArg Multiplicative.ofAdd h3

/-! ## The Borromean step is conjugate to its mirror -/

/-- The chiral vertex `Vᵢ = σᵢσᵢ₊₁⁻¹`. -/
def vertex (i : Fin n) (h : (i : ℕ) + 1 < n) : BraidGroup n := σ i * (σ ⟨(i : ℕ) + 1, h⟩)⁻¹

/-- Group-theoretic core: if `aba = bab` then `(a⁻¹b)³` is conjugate to `(ab⁻¹)³`, by
`c = (aba)⁻¹ b⁻¹`. -/
theorem conj_core {G : Type*} [Group G] (a b : G) (hb : a * b * a = b * a * b) :
    (a⁻¹ * b) ^ 3 = ((a * b * a)⁻¹ * b⁻¹) * (a * b⁻¹) ^ 3 * ((a * b * a)⁻¹ * b⁻¹)⁻¹ := by
  obtain ⟨Δ, hΔ⟩ : ∃ Δ, Δ = a * b * a := ⟨_, rfl⟩
  rw [← hΔ]
  -- conjugation by `Δ` swaps `a` and `b`
  have ha : Δ * a * Δ⁻¹ = b := by
    rw [mul_inv_eq_iff_eq_mul, hΔ]
    calc a * b * a * a = b * a * b * a := by rw [hb]
      _ = b * (a * b * a) := by group
  have hbb : Δ * b * Δ⁻¹ = a := by
    rw [mul_inv_eq_iff_eq_mul, hΔ]
    calc a * b * a * b = a * (b * a * b) := by group
      _ = a * (a * b * a) := by rw [hb]
  have h1 : Δ * (a⁻¹ * b) * Δ⁻¹ = b⁻¹ * a := by
    rw [show Δ * (a⁻¹ * b) * Δ⁻¹ = (Δ * a * Δ⁻¹)⁻¹ * (Δ * b * Δ⁻¹) by group, ha, hbb]
  have hc : Δ * (a⁻¹ * b) ^ 3 * Δ⁻¹ = (b⁻¹ * a) ^ 3 := by rw [← conj_pow, h1]
  have hcyc : (b⁻¹ * a) ^ 3 = b⁻¹ * (a * b⁻¹) ^ 3 * b := by
    simp only [pow_succ, pow_zero, one_mul]; group
  calc (a⁻¹ * b) ^ 3 = Δ⁻¹ * (Δ * (a⁻¹ * b) ^ 3 * Δ⁻¹) * Δ := by group
    _ = Δ⁻¹ * (b⁻¹ * (a * b⁻¹) ^ 3 * b) * Δ := by rw [hc, hcyc]
    _ = (Δ⁻¹ * b⁻¹) * (a * b⁻¹) ^ 3 * (Δ⁻¹ * b⁻¹)⁻¹ := by group

/-- **`Vᵢ³` is conjugate to its mirror.** The conjugator is `Δ⁻¹ σᵢ₊₁⁻¹`, `Δ = σᵢσᵢ₊₁σᵢ`. -/
theorem mirror_vPow_three_conj (i : Fin n) (h : (i : ℕ) + 1 < n) :
    ∃ c, mirror n (vertex i h ^ 3) = c * vertex i h ^ 3 * c⁻¹ := by
  refine ⟨(σ i * σ ⟨(i : ℕ) + 1, h⟩ * σ i)⁻¹ * (σ ⟨(i : ℕ) + 1, h⟩)⁻¹, ?_⟩
  rw [show mirror n (vertex i h ^ 3) = ((σ i)⁻¹ * σ ⟨(i : ℕ) + 1, h⟩) ^ 3 by
    simp [vertex, map_pow]]
  exact conj_core (σ i) (σ ⟨(i : ℕ) + 1, h⟩) (braid_rel i h)

/-- **`σᵢ²` is not conjugate to its mirror** (its writhe is `2`), so the achirality premise
excludes the `σ₅²` bond that the 2026-11-21 probe left ahead of `V³`. -/
theorem sq_not_conj_mirror (i : Fin n) :
    ¬ ∃ c, mirror n (σ i ^ 2) = c * σ i ^ 2 * c⁻¹ := by
  rintro ⟨c, hc⟩
  have h := writhe_eq_zero_of_conj_mirror _ _ hc
  rw [map_pow, exponentSum_σ] at h
  exact absurd h (by decide)

end QOU.Molecular.H2BondMirror

