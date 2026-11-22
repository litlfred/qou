import QOU.Mass.KZHolonomy.ConfRegions
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar

/-!
# General position in `Conf_{m+1}(ℂ)`

A configuration is *generic* (`Generic`) if at most one unordered pair of its points has equal
real parts.  The non-generic configurations lie in finitely many real-linear subspaces of real
codimension `2` (two independent real-part equalities), so they have Haar measure zero.  Two
consequences are proved here, by choosing points outside finitely many proper subspaces:

* every ball contains a generic configuration (`exists_generic_mem_ball`);
* two generic configurations `x, y` can be joined through a point `p` of any nonempty open set so
  that both segments `[x, p]` and `[p, y]` consist of generic configurations
  (`exists_generic_segments`).

The second uses, for each pair of pairs, the linear form
`φ_x(z) = L₁(x) L₂(z) − L₂(x) L₁(z)`: it vanishes on the subspace `L₁ = L₂ = 0` and at `x`, so a
segment from `x` that meets the subspace ends in `ker φ_x`.
-/

set_option autoImplicit false

namespace QOU.Mass.KZHolonomy

open Set Complex MeasureTheory Metric

variable {m : ℕ}

/-- The real-linear form `z ↦ re z a − re z b`. -/
noncomputable def tieL (a b : Fin (m + 1)) : (Fin (m + 1) → ℂ) →ₗ[ℝ] ℝ :=
  reLm.comp (LinearMap.proj a) - reLm.comp (LinearMap.proj b)

lemma tieL_apply (a b : Fin (m + 1)) (z : Fin (m + 1) → ℂ) :
    tieL a b z = (z a).re - (z b).re := rfl

/-- Two distinct unordered pairs of distinct indices. -/
def PairPair (m : ℕ) : Type :=
  {q : Fin (m + 1) × Fin (m + 1) × Fin (m + 1) × Fin (m + 1) //
    q.1 ≠ q.2.1 ∧ q.2.2.1 ≠ q.2.2.2 ∧
      ¬ ((q.1 = q.2.2.1 ∧ q.2.1 = q.2.2.2) ∨ (q.1 = q.2.2.2 ∧ q.2.1 = q.2.2.1))}

instance : Finite (PairPair m) := Subtype.finite

/-- At most one unordered pair of points has equal real parts. -/
def Generic (z : Fin (m + 1) → ℂ) : Prop :=
  ∀ q : PairPair m, ¬ (tieL q.1.1 q.1.2.1 z = 0 ∧ tieL q.1.2.2.1 q.1.2.2.2 z = 0)

lemma exists_sep {a b c d : Fin (m + 1)} (hab : a ≠ b) (hcd : c ≠ d)
    (hne : ¬ ((a = c ∧ b = d) ∨ (a = d ∧ b = c))) :
    ∃ e : Fin (m + 1) → ℂ, tieL a b e = 1 ∧ tieL c d e = 0 := by
  by_cases ha : a ≠ c ∧ a ≠ d
  · refine ⟨Pi.single a 1, ?_, ?_⟩
    · simp [tieL_apply, hab.symm]
    · simp [tieL_apply, Ne.symm ha.1, Ne.symm ha.2]
  · by_cases hb : b ≠ c ∧ b ≠ d
    · refine ⟨-Pi.single b 1, ?_, ?_⟩
      · simp [tieL_apply, hab]
      · simp [tieL_apply, Ne.symm hb.1, Ne.symm hb.2]
    · exfalso
      apply hne
      by_cases hac : a = c
      · subst hac
        left; refine ⟨rfl, ?_⟩
        by_contra hbd
        exact hb ⟨fun h => hab h.symm, hbd⟩
      · have had : a = d := by by_contra h; exact ha ⟨hac, h⟩
        subst had
        right; refine ⟨rfl, ?_⟩
        by_contra hbc
        exact hb ⟨hbc, fun h => hab h.symm⟩

/-- Avoiding finitely many proper subspaces inside a nonempty open set. -/
theorem exists_avoid_submodules {ι : Type*} [Finite ι] (K : ι → Submodule ℝ (Fin (m + 1) → ℂ))
    (hK : ∀ i, K i ≠ ⊤) {O : Set (Fin (m + 1) → ℂ)} (hO : IsOpen O) (hne : O.Nonempty) :
    ∃ p ∈ O, ∀ i, p ∉ K i := by
  let μ : Measure (Fin (m + 1) → ℂ) := Measure.addHaar
  have h0 : μ (⋃ i, (K i : Set (Fin (m + 1) → ℂ))) = 0 :=
    measure_iUnion_null fun i => Measure.addHaar_submodule μ _ (hK i)
  have hpos : 0 < μ O := hO.measure_pos μ hne
  by_contra h
  push_neg at h
  have hsub : O ⊆ ⋃ i, (K i : Set (Fin (m + 1) → ℂ)) := fun p hp => mem_iUnion.2 (h p hp)
  have := measure_mono (μ := μ) hsub
  rw [h0] at this
  exact (lt_of_lt_of_le hpos this).ne rfl

/-- The subspace `L₁ = L₂ = 0` of a pair of pairs. -/
noncomputable def tieSub (q : PairPair m) : Submodule ℝ (Fin (m + 1) → ℂ) :=
  LinearMap.ker (tieL q.1.1 q.1.2.1) ⊓ LinearMap.ker (tieL q.1.2.2.1 q.1.2.2.2)

lemma tieSub_ne_top (q : PairPair m) : tieSub q ≠ ⊤ := by
  obtain ⟨hab, hcd, hne⟩ := q.2
  obtain ⟨e, he, -⟩ := exists_sep hab hcd hne
  intro h
  have : e ∈ tieSub q := h ▸ Submodule.mem_top
  have := (Submodule.mem_inf.1 this).1
  rw [LinearMap.mem_ker, he] at this
  exact one_ne_zero this

theorem exists_generic_mem_ball (x : Fin (m + 1) → ℂ) {r : ℝ} (hr : 0 < r) :
    ∃ y ∈ ball x r, Generic y := by
  obtain ⟨y, hy, hK⟩ := exists_avoid_submodules tieSub tieSub_ne_top isOpen_ball
    ⟨x, mem_ball_self hr⟩
  refine ⟨y, hy, fun q h => hK q ?_⟩
  exact Submodule.mem_inf.2 ⟨LinearMap.mem_ker.2 h.1, LinearMap.mem_ker.2 h.2⟩

/-- The form `φ_x = L₁(x) L₂ − L₂(x) L₁`. -/
noncomputable def phiForm (x : Fin (m + 1) → ℂ) (q : PairPair m) :
    (Fin (m + 1) → ℂ) →ₗ[ℝ] ℝ :=
  tieL q.1.1 q.1.2.1 x • tieL q.1.2.2.1 q.1.2.2.2 - tieL q.1.2.2.1 q.1.2.2.2 x • tieL q.1.1 q.1.2.1

lemma phiForm_apply (x : Fin (m + 1) → ℂ) (q : PairPair m) (z : Fin (m + 1) → ℂ) :
    phiForm x q z = tieL q.1.1 q.1.2.1 x * tieL q.1.2.2.1 q.1.2.2.2 z -
      tieL q.1.2.2.1 q.1.2.2.2 x * tieL q.1.1 q.1.2.1 z := rfl

lemma ker_phiForm_ne_top {x : Fin (m + 1) → ℂ} (hx : Generic x) (q : PairPair m) :
    LinearMap.ker (phiForm x q) ≠ ⊤ := by
  obtain ⟨hab, hcd, hne⟩ := q.2
  obtain ⟨e₁, he₁, he₁'⟩ := exists_sep hab hcd hne
  have hne' : ¬ ((q.1.2.2.1 = q.1.1 ∧ q.1.2.2.2 = q.1.2.1) ∨
      (q.1.2.2.1 = q.1.2.1 ∧ q.1.2.2.2 = q.1.1)) := by
    rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
    · exact hne (Or.inl ⟨h1.symm, h2.symm⟩)
    · exact hne (Or.inr ⟨h2.symm, h1.symm⟩)
  obtain ⟨e₂, he₂, he₂'⟩ := exists_sep hcd hab hne'
  intro htop
  have h1 : phiForm x q e₁ = 0 := LinearMap.mem_ker.1 (htop ▸ Submodule.mem_top)
  have h2 : phiForm x q e₂ = 0 := LinearMap.mem_ker.1 (htop ▸ Submodule.mem_top)
  rw [phiForm_apply, he₁, he₁'] at h1
  rw [phiForm_apply, he₂, he₂'] at h2
  apply hx q
  constructor <;> linarith

/-- A segment from a generic `x` to a point off every `ker φ_x` is generic throughout. -/
theorem generic_segment {x p : Fin (m + 1) → ℂ} (hx : Generic x)
    (hp : ∀ q : PairPair m, phiForm x q p ≠ 0) {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    Generic ((1 - t) • x + t • p) := by
  intro q ⟨h1, h2⟩
  have hφw : phiForm x q ((1 - t) • x + t • p) = 0 := by
    rw [phiForm_apply, h1, h2]; ring
  have hφx : phiForm x q x = 0 := by rw [phiForm_apply]; ring
  rw [map_add, map_smul, map_smul, hφx, smul_zero, zero_add, smul_eq_mul] at hφw
  rcases mul_eq_zero.1 hφw with h | h
  · subst h
    simp only [sub_zero, one_smul, zero_smul, add_zero] at h1 h2
    exact hx q ⟨h1, h2⟩
  · exact hp q h

/-- Two generic configurations are joined, through a point of any nonempty open set, by two
segments of generic configurations. -/
theorem exists_generic_segments {x y : Fin (m + 1) → ℂ} (hx : Generic x) (hy : Generic y)
    {O : Set (Fin (m + 1) → ℂ)} (hO : IsOpen O) (hne : O.Nonempty) :
    ∃ p ∈ O, (∀ t ∈ Icc (0 : ℝ) 1, Generic ((1 - t) • x + t • p)) ∧
      ∀ t ∈ Icc (0 : ℝ) 1, Generic ((1 - t) • p + t • y) := by
  obtain ⟨p, hp, hK⟩ := exists_avoid_submodules
    (fun i : PairPair m ⊕ PairPair m => Sum.elim (fun q => LinearMap.ker (phiForm x q))
      (fun q => LinearMap.ker (phiForm y q)) i)
    (fun i => by
      rcases i with q | q
      · exact ker_phiForm_ne_top hx q
      · exact ker_phiForm_ne_top hy q) hO hne
  refine ⟨p, hp, fun t ht => generic_segment hx (fun q h => hK (Sum.inl q) h) ht,
    fun t ht => ?_⟩
  have e : (1 - t) • p + t • y = (1 - (1 - t)) • y + (1 - t) • p := by
    rw [sub_sub_cancel]; exact add_comm _ _
  rw [e]
  exact generic_segment hy (fun q h => hK (Sum.inr q) h) ⟨by linarith [ht.2], by linarith [ht.1]⟩

end QOU.Mass.KZHolonomy
