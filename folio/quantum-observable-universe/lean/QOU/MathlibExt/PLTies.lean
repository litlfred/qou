/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLSlice

set_option autoImplicit false

/-!
# Ties of PL functions of time (issue #8902, stage 2: PL isotopy ⇒ Δ-equivalence)

The vertices of the moving link are slice endpoints, which are PL functions of time
(`PLSlice`). Two of them can only start or stop coinciding at finitely many times.

## What is a THEOREM here

* `IsPL.exists_finset_eventually_zero_iff` — for a PL `f : ℝ → ℝ` there is a finite set `F` such
  that off `F` the condition `f = 0` is locally constant.
* `IsPL.exists_finset_eventually_eq_iff` — the same for `f = g` with `f`, `g` PL.

## What is NOT proved here

* The exact-image polygons between event times, and the gluing at event times.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

lemma clm_real_apply (φ : ℝ →L[ℝ] ℝ) (x : ℝ) : φ x = x * φ 1 := by
  rw [← smul_eq_mul, ← φ.map_smul, smul_eq_mul, mul_one]

/-- **A polyhedron in `ℝ` is a neighbourhood of each of its points except finitely many.** -/
lemma polySet_mem_nhds_of_ne {κ : Type} [Fintype κ] (φ : κ → ℝ →L[ℝ] ℝ) (r : κ → ℝ) {t : ℝ}
    (ht : ∀ j, φ j t ≤ r j) (hne : ∀ j, t ≠ r j / φ j 1) :
    {x | ∀ j, φ j x ≤ r j} ∈ 𝓝 t := by
  have : {x : ℝ | ∀ j, φ j x ≤ r j} = ⋂ j, {x | φ j x ≤ r j} := by ext; simp
  rw [this, Filter.iInter_mem]
  intro j
  by_cases h0 : φ j 1 = 0
  · apply Filter.univ_mem'
    intro x
    have := ht j
    rw [clm_real_apply, h0, mul_zero] at this
    simp only [mem_setOf_eq]
    rw [clm_real_apply, h0, mul_zero]
    exact this
  · have hlt : φ j t < r j := by
      refine lt_of_le_of_ne (ht j) (fun heq => hne j ?_)
      rw [clm_real_apply] at heq
      field_simp
      linarith
    exact Filter.mem_of_superset ((isOpen_lt (φ j).continuous continuous_const).mem_nhds hlt)
      (fun x (hx : φ j x < r j) => show φ j x ≤ r j from hx.le)

/-- **The zero status of a PL function of time changes at finitely many times.** -/
theorem IsPL.exists_finset_eventually_zero_iff {f : ℝ → ℝ} (hf : IsPL f) :
    ∃ F : Finset ℝ, ∀ t ∉ F, ∀ᶠ s in 𝓝 t, (f s = 0 ↔ f t = 0) := by
  classical
  have hcont := hf.continuous
  obtain ⟨ι, _, K, A, hK, hcov, hEq⟩ := hf
  choose κ hκ φ r hKr using hK
  let root : ι → ℝ := fun i => -(A i 0) / (A i).contLinear 1
  let F : Finset ℝ :=
    (Finset.univ.biUnion fun i => Finset.univ.image fun j => r i j / φ i j 1) ∪
      Finset.univ.image root
  refine ⟨F, fun t ht => ?_⟩
  have hmem : t ∈ ⋃ i, K i := hcov ▸ mem_univ t
  obtain ⟨i, hi⟩ := mem_iUnion.1 hmem
  have hKt : K i ∈ 𝓝 t := by
    rw [hKr i] at hi ⊢
    refine polySet_mem_nhds_of_ne (φ i) (r i) hi (fun j hj => ht ?_)
    exact Finset.mem_union_left _ (Finset.mem_biUnion.2
      ⟨i, Finset.mem_univ _, Finset.mem_image.2 ⟨j, Finset.mem_univ _, hj.symm⟩⟩)
  set m := (A i).contLinear 1
  have hform : ∀ s, A i s = A i 0 + s * m := fun s => by
    have h := (A i).contLinear_map_vsub s 0
    rw [vsub_eq_sub, vsub_eq_sub, sub_zero, clm_real_apply] at h
    linarith
  have hev : ∀ᶠ s in 𝓝 t, f s = A i 0 + s * m :=
    Filter.mem_of_superset hKt (fun s hs => (hEq i hs).trans (hform s))
  have hft : f t = A i 0 + t * m := (hEq i (mem_of_mem_nhds hKt)).trans (hform t)
  by_cases hm : m = 0
  · filter_upwards [hev] with s hs
    rw [hs, hft, hm]
    simp
  · have hne : f t ≠ 0 := by
      rw [hft]
      intro h0
      apply ht
      refine Finset.mem_union_right _ (Finset.mem_image.2 ⟨i, Finset.mem_univ _, ?_⟩)
      show -(A i 0) / m = t
      field_simp
      linarith
    filter_upwards [hcont.continuousAt.eventually_ne hne] with s hs
    exact ⟨fun h => absurd h hs, fun h => absurd h hne⟩

/-- **Two PL functions of time start or stop agreeing at finitely many times.** -/
theorem IsPL.exists_finset_eventually_eq_iff {f g : ℝ → ℝ} (hf : IsPL f) (hg : IsPL g) :
    ∃ F : Finset ℝ, ∀ t ∉ F, ∀ᶠ s in 𝓝 t, (f s = g s ↔ f t = g t) := by
  obtain ⟨F, hF⟩ := (hf.sub hg).exists_finset_eventually_zero_iff
  refine ⟨F, fun t ht => (hF t ht).mono fun s hs => ?_⟩
  simpa [sub_eq_zero] using hs

end QOU.MathlibExt.PL
