import QOU.MathlibExt.CechSameNerve
import QOU.MathlibExt.CechSphereHemispheres

/-!
# Linear-cone pieces of `S²` and bounded boxes inside the hemispheres

Step P3b of the C2 comparison (route R3, surface case).

A **linear-cone piece** of `S²` is the set of unit vectors on which a finite,
nonempty set of linear forms is positive. Each is the sphere slice of an open
convex cone not containing `0`, hence preconnected, and an intersection of
pieces is a piece. So any family of pieces is a `ConnFamily`.

Inside the hemisphere `tfun i > 0` use the coordinates
`u₀ = x₀ / tfun i x`, `u₁ = x₁ / tfun i x`. A **box** `a < u₀ < b`,
`c < u₁ < d` is a linear-cone piece. The core boxes `|u₀|, |u₁| < 3` still
cover `S²` and have the same nerve as the hemispheres, so shrinking the
hemisphere cover to them keeps `H²`.

## Results, all sorry-free

* `lcOpen`, `isPreconnected_lcOpen`, `lcOpen_inf`, `connFamily_of_lc`.
* `box`, `mem_box`, `box_le_hemi`.
* `exists_core`: the core boxes cover `S²`.
* `hemi_core_bijective`: pulling `H²` from the hemispheres to the core boxes is
  a bijection.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
Bean `qou-skn4`.
-/
open CategoryTheory Opposite TopologicalSpace
namespace QOU.CentralExtension.Cech
open CechGerbe

local notation "E3" => EuclideanSpace ℝ (Fin 3)

/-! ### Linear-cone pieces -/

/-- The cone on which every form in `L` is positive. -/
def lcCone (L : Set (E3 →L[ℝ] ℝ)) : Set E3 := {x | ∀ f ∈ L, 0 < f x}

/-- The sphere piece cut out by a finite set of linear forms. -/
def lcOpen (L : Set (E3 →L[ℝ] ℝ)) (hL : L.Finite) : Opens S2 :=
  ⟨{p | ∀ f ∈ L, 0 < f p.1}, by
    have : {p : S2 | ∀ f ∈ L, 0 < f p.1} = ⋂ f ∈ L, {p : S2 | 0 < f p.1} := by
      ext p; simp
    rw [this]
    exact hL.isOpen_biInter fun f _ =>
      isOpen_lt continuous_const (f.continuous.comp continuous_subtype_val)⟩

theorem mem_lcOpen {L : Set (E3 →L[ℝ] ℝ)} {hL : L.Finite} {p : S2} :
    p ∈ lcOpen L hL ↔ ∀ f ∈ L, 0 < f p.1 := Iff.rfl

theorem isPreconnected_lcOpen {L : Set (E3 →L[ℝ] ℝ)} (hL : L.Finite) (hne : L.Nonempty) :
    IsPreconnected ((lcOpen L hL : Opens S2) : Set S2) := by
  have himg : Subtype.val '' ((lcOpen L hL : Opens S2) : Set S2) =
      lcCone L ∩ Metric.sphere 0 1 := by
    ext x; constructor
    · rintro ⟨p, hp, rfl⟩; exact ⟨hp, p.2⟩
    · rintro ⟨hx, hs⟩; exact ⟨⟨x, hs⟩, hx, rfl⟩
  rw [← Topology.IsInducing.subtypeVal.isPreconnected_image, himg]
  refine isPreconnected_cone_inter_sphere ?_ ?_ ?_
  · intro x hx y hy a b ha hb hab f hf
    have hx' := hx f hf; have hy' := hy f hf
    simp only [map_add, map_smul, smul_eq_mul]
    rcases ha.eq_or_lt with h | h
    · subst h; simp at hab; subst hab; simpa using hy'
    · exact add_pos_of_pos_of_nonneg (mul_pos h hx') (mul_nonneg hb hy'.le)
  · obtain ⟨f, hf⟩ := hne
    intro h; have := h f hf; simp at this
  · intro x hx t ht f hf
    simpa [map_smul, smul_eq_mul] using mul_pos ht (hx f hf)

theorem lcOpen_inf {L L' : Set (E3 →L[ℝ] ℝ)} (hL : L.Finite) (hL' : L'.Finite) :
    lcOpen L hL ⊓ lcOpen L' hL' = lcOpen (L ∪ L') (hL.union hL') := by
  ext p
  simp only [Opens.coe_inf, Set.mem_inter_iff, SetLike.mem_coe, mem_lcOpen, Set.mem_union]
  constructor
  · rintro ⟨h1, h2⟩ f (hf | hf)
    exacts [h1 f hf, h2 f hf]
  · intro h; exact ⟨fun f hf => h f (Or.inl hf), fun f hf => h f (Or.inr hf)⟩

/-- A family of linear-cone pieces. -/
def IsLCFamily {ι : Type} (U : ι → Opens S2) : Prop :=
  ∀ i, ∃ (L : Set (E3 →L[ℝ] ℝ)) (hL : L.Finite), L.Nonempty ∧ U i = lcOpen L hL

theorem connFamily_of_lc {ι : Type} {U : ι → Opens S2} (h : IsLCFamily U) : ConnFamily U := by
  constructor
  · intro i j k
    obtain ⟨L₁, h₁, n₁, e₁⟩ := h i
    obtain ⟨L₂, h₂, -, e₂⟩ := h j
    obtain ⟨L₃, h₃, -, e₃⟩ := h k
    rw [e₁, e₂, e₃, lcOpen_inf, lcOpen_inf]
    exact isPreconnected_lcOpen _ ((n₁.mono Set.subset_union_left).mono Set.subset_union_left)
  · intro i j
    obtain ⟨L₁, h₁, n₁, e₁⟩ := h i
    obtain ⟨L₂, h₂, -, e₂⟩ := h j
    rw [e₁, e₂, lcOpen_inf]
    exact isPreconnected_lcOpen _ (n₁.mono Set.subset_union_left)

/-! ### Boxes in the hemisphere coordinates -/

/-- The four forms cutting out the box `a < u₀ < b`, `c < u₁ < d` in hemisphere `i`. -/
noncomputable def boxForms (i : Fin 4) (a b c d : ℝ) : Set (E3 →L[ℝ] ℝ) :=
  {EuclideanSpace.proj 0 - a • tfun i, b • tfun i - EuclideanSpace.proj 0,
    EuclideanSpace.proj 1 - c • tfun i, d • tfun i - EuclideanSpace.proj 1}

theorem boxForms_finite (i : Fin 4) (a b c d : ℝ) : (boxForms i a b c d).Finite := by
  simp [boxForms]

theorem boxForms_nonempty (i : Fin 4) (a b c d : ℝ) : (boxForms i a b c d).Nonempty :=
  ⟨_, Set.mem_insert _ _⟩

/-- The box `a < u₀ < b`, `c < u₁ < d` in hemisphere `i`. -/
noncomputable def box (i : Fin 4) (a b c d : ℝ) : Opens S2 :=
  lcOpen (boxForms i a b c d) (boxForms_finite i a b c d)

theorem mem_box {i : Fin 4} {a b c d : ℝ} {p : S2} :
    p ∈ box i a b c d ↔ a * tfun i p.1 < p.1 0 ∧ p.1 0 < b * tfun i p.1 ∧
      c * tfun i p.1 < p.1 1 ∧ p.1 1 < d * tfun i p.1 := by
  simp only [box, mem_lcOpen, boxForms, Set.forall_mem_insert, Set.mem_singleton_iff,
    forall_eq, ContinuousLinearMap.sub_apply, ContinuousLinearMap.smul_apply, smul_eq_mul,
    sub_pos]
  exact Iff.rfl

theorem box_isLC {ι : Type} (i : ι → Fin 4) (a b c d : ι → ℝ) :
    IsLCFamily (fun j => box (i j) (a j) (b j) (c j) (d j)) :=
  fun _ => ⟨_, boxForms_finite _ _ _ _ _, boxForms_nonempty _ _ _ _ _, rfl⟩

theorem box_le_hemi {i : Fin 4} {a b c d : ℝ} (hab : a < b) : box i a b c d ≤ hemi i := by
  intro p hp
  obtain ⟨h1, h2, -, -⟩ := mem_box.1 hp
  change 0 < tfun i p.1
  nlinarith

/-! ### The core boxes -/

/-- The core box `|u₀|, |u₁| < 3` of hemisphere `i`. -/
noncomputable def core (i : Fin 4) : Opens S2 := box i (-3) 3 (-3) 3

theorem norm_sq_three (x : E3) : ‖x‖ ^ 2 = x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 := by
  rw [EuclideanSpace.norm_sq_eq]; simp [Fin.sum_univ_three, Real.norm_eq_abs, sq_abs]

theorem tfun_sq_sum (x : E3) :
    tfun 0 x ^ 2 + tfun 1 x ^ 2 + tfun 2 x ^ 2 + tfun 3 x ^ 2 =
      4 * (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) := by
  simp only [tfun_apply, tsgn]; simp; ring

theorem sphere_sq (p : S2) : p.1 0 ^ 2 + p.1 1 ^ 2 + p.1 2 ^ 2 = 1 := by
  have h1 : ‖p.1‖ = 1 := mem_sphere_zero_iff_norm.1 p.2
  rw [← norm_sq_three, h1]; norm_num

/-- Every unit vector has a hemisphere form at least `1/2`. -/
theorem exists_tfun_ge (p : S2) : ∃ i, 1 / 2 ≤ tfun i p.1 := by
  by_contra h
  push_neg at h
  have hs := sphere_sq p
  have hq := tfun_sq_sum p.1
  have hz := tfun_sum p.1
  have h0 := h 0; have h1 := h 1; have h2 := h 2; have h3 := h 3
  have l0 : -3/2 < tfun 0 p.1 := by linarith
  have l1 : -3/2 < tfun 1 p.1 := by linarith
  have l2 : -3/2 < tfun 2 p.1 := by linarith
  have l3 : -3/2 < tfun 3 p.1 := by linarith
  nlinarith [mul_pos (sub_pos.2 h0) (by linarith : (0:ℝ) < tfun 0 p.1 + 3/2),
    mul_pos (sub_pos.2 h1) (by linarith : (0:ℝ) < tfun 1 p.1 + 3/2),
    mul_pos (sub_pos.2 h2) (by linarith : (0:ℝ) < tfun 2 p.1 + 3/2),
    mul_pos (sub_pos.2 h3) (by linarith : (0:ℝ) < tfun 3 p.1 + 3/2)]

/-- **The core boxes cover `S²`.** -/
theorem exists_core (p : S2) : ∃ i, p ∈ core i := by
  obtain ⟨i, hi⟩ := exists_tfun_ge p
  have hs := sphere_sq p
  have a0 : p.1 0 ≤ 1 := by nlinarith [sq_nonneg (p.1 1), sq_nonneg (p.1 2), sq_nonneg (p.1 0 - 1)]
  have b0 : -1 ≤ p.1 0 := by nlinarith [sq_nonneg (p.1 1), sq_nonneg (p.1 2), sq_nonneg (p.1 0 + 1)]
  have a1 : p.1 1 ≤ 1 := by nlinarith [sq_nonneg (p.1 0), sq_nonneg (p.1 2), sq_nonneg (p.1 1 - 1)]
  have b1 : -1 ≤ p.1 1 := by nlinarith [sq_nonneg (p.1 0), sq_nonneg (p.1 2), sq_nonneg (p.1 1 + 1)]
  refine ⟨i, mem_box.2 ⟨?_, ?_, ?_, ?_⟩⟩ <;> linarith

theorem core_le_hemi (i : Fin 4) : core i ≤ hemi i := box_le_hemi (by norm_num)

/-- The unit vector opposite the `m`-th tetrahedron vertex. -/
noncomputable def vpt (m : Fin 4) : S2 :=
  let v : E3 := WithLp.toLp 2 (fun a => - tsgn m a)
  ⟨‖v‖⁻¹ • v, by
    have hv0 : v ≠ 0 := fun h => by
      have := congrArg (fun x : E3 => x 0) h
      fin_cases m <;> simp [v, tsgn] at this
    simp [norm_smul, hv0]⟩

theorem vpt_mem_core {m i : Fin 4} (h : i ≠ m) : vpt m ∈ core i := by
  set v : E3 := WithLp.toLp 2 (fun a => - tsgn m a) with hvdef
  have hv : tfun i v = 1 := by
    simp only [tfun_apply, v, PiLp.toLp_apply]
    linarith [tsgn_dot i m h]
  have hv0 : v ≠ 0 := fun h' => by rw [h', map_zero] at hv; norm_num at hv
  have hk : 0 < ‖v‖⁻¹ := inv_pos.2 (norm_pos_iff.2 hv0)
  have e0 : |v 0| ≤ 1 := by fin_cases m <;> simp [v, tsgn]
  have e1 : |v 1| ≤ 1 := by fin_cases m <;> simp [v, tsgn]
  have ht : tfun i (vpt m).1 = ‖v‖⁻¹ := by
    change tfun i (‖v‖⁻¹ • v) = _; rw [map_smul, hv, smul_eq_mul, mul_one]
  have c0 : (vpt m).1 0 = ‖v‖⁻¹ * v 0 := rfl
  have c1 : (vpt m).1 1 = ‖v‖⁻¹ * v 1 := rfl
  rw [abs_le] at e0 e1
  refine mem_box.2 ⟨?_, ?_, ?_, ?_⟩ <;> rw [ht] <;> [rw [c0]; rw [c0]; rw [c1]; rw [c1]] <;>
    nlinarith

theorem connFamily_hemi : ConnFamily hemi := ⟨pre3_hemi, pre2_hemi⟩

theorem connFamily_core : ConnFamily core :=
  connFamily_of_lc (box_isLC (ι := Fin 4) id (fun _ => -3) (fun _ => 3) (fun _ => -3) (fun _ => 3))

/-- **Shrinking the hemispheres to the core boxes keeps `H²`.** -/
theorem hemi_core_bijective {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G]
    [DiscreteTopology G] :
    Function.Bijective (H2.pull (𝒜 := contPresheaf S2 G) (U := hemi) (Equiv.refl (Fin 4))
      (fun j => homOfLE (core_le_hemi j))) := by
  refine sameNerve_pull_bijective (Equiv.refl _) core_le_hemi connFamily_hemi connFamily_core
    (fun i j k _ => ?_) (fun i j k l h => ?_)
  · obtain ⟨l, hi, hj, hk⟩ := exists_fourth i j k
    exact (n3_iff _ _ _ _).2 ⟨vpt l, vpt_mem_core hi.symm, vpt_mem_core hj.symm,
      vpt_mem_core hk.symm⟩
  · obtain ⟨t, h1, h2, h3, h4⟩ := (n4_iff _ _ _ _ _).1 h
    obtain ⟨m, hm⟩ := hemi_no_quad t
    have ne : ∀ a : Fin 4, t ∈ hemi a → a ≠ m := fun a ha e => hm (e ▸ ha)
    exact (n4_iff _ _ _ _ _).2 ⟨vpt m, vpt_mem_core (ne _ h1), vpt_mem_core (ne _ h2),
      vpt_mem_core (ne _ h3), vpt_mem_core (ne _ h4)⟩

end QOU.CentralExtension.Cech
