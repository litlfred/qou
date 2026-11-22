import QOU.Mass.KZHolonomy.KZForm
import Mathlib.Analysis.NormedSpace.Connected
import Mathlib.LinearAlgebra.Complex.FiniteDimensional

/-!
# The ordered configuration space of `ℂ` is path-connected

For `z, w ∈ Conf_n(ℂ)` the complex line `λ ↦ z + λ (w − z)` meets the collision locus in at
most one point per pair `a ≠ b` (the pair difference is affine in `λ` and nonzero at `λ = 0`).
The complement of a countable set in `ℂ` is path-connected (`ℂ` has real rank `2`), and it
contains `0` and `1`, so `z` and `w` are joined inside `Conf_n(ℂ)`.
-/

set_option autoImplicit false

namespace QOU.Mass.KZHolonomy

open Set

/-- The pair difference along the complex line through `z` and `w`. -/
private lemma subsingleton_collision {n : ℕ} {z w : Fin n → ℂ} (hz : z ∈ confSet n) {a b : Fin n}
    (hab : a ≠ b) :
    {l : ℂ | (z + l • (w - z)) a = (z + l • (w - z)) b}.Subsingleton := by
  intro l hl l' hl'
  simp only [mem_setOf_eq, Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul] at hl hl'
  have hne : z a - z b ≠ 0 := sub_ne_zero.mpr fun h => hab (hz h)
  have key : (l - l') * ((w a - z a) - (w b - z b)) = 0 := by linear_combination hl - hl'
  rcases mul_eq_zero.mp key with h | h
  · exact sub_eq_zero.mp h
  · exfalso; apply hne; linear_combination hl - l * h

theorem isPathConnected_confSet (n : ℕ) : IsPathConnected (confSet n) := by
  have hne : (confSet n).Nonempty := ⟨fun k => ((k : ℕ) : ℂ), fun a b h => by
    simpa [Fin.ext_iff] using h⟩
  obtain ⟨z₀, hz₀⟩ := hne
  refine ⟨z₀, hz₀, fun {w} hw => ?_⟩
  set L : ℂ → Fin n → ℂ := fun l => z₀ + l • (w - z₀) with hL
  set B : Set ℂ := ⋃ p : Fin n × Fin n, ⋃ (_ : p.1 ≠ p.2), {l | L l p.1 = L l p.2}
  have hB : B.Countable :=
    countable_iUnion fun p => countable_iUnion fun hp =>
      (subsingleton_collision (w := w) hz₀ hp).countable
  have hrank : 1 < Module.rank ℝ ℂ := by
    rw [Complex.rank_real_complex]; norm_num
  have hpc : IsPathConnected Bᶜ := hB.isPathConnected_compl_of_one_lt_rank hrank
  have hmem : ∀ l ∈ Bᶜ, L l ∈ confSet n := by
    intro l hl a b hab
    by_contra hne
    exact hl (mem_iUnion.mpr ⟨(a, b), mem_iUnion.mpr ⟨hne, hab⟩⟩)
  have h0 : (0 : ℂ) ∈ Bᶜ := by
    intro h
    obtain ⟨p, h⟩ := mem_iUnion.mp h
    obtain ⟨hp, h⟩ := mem_iUnion.mp h
    exact hp (hz₀ (by simpa [hL] using h))
  have h1 : (1 : ℂ) ∈ Bᶜ := by
    intro h
    obtain ⟨p, h⟩ := mem_iUnion.mp h
    obtain ⟨hp, h⟩ := mem_iUnion.mp h
    exact hp (hw (by simpa [hL] using h))
  have hLc : Continuous L := by fun_prop
  have hj := (hpc.image hLc).joinedIn (L 0) ⟨0, h0, rfl⟩ (L 1) ⟨1, h1, rfl⟩
  have e0 : L 0 = z₀ := by simp [hL]
  have e1 : L 1 = w := by simp [hL]
  rw [e0, e1] at hj
  exact hj.mono (by rintro _ ⟨l, hl, rfl⟩; exact hmem l hl)

instance (n : ℕ) : PathConnectedSpace (confSet n) :=
  isPathConnected_iff_pathConnectedSpace.mp (isPathConnected_confSet n)

end QOU.Mass.KZHolonomy
