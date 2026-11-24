/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLStar
import BraidKnotOctonion.PLBarycentric

set_option autoImplicit false

/-!
# PL balls and spheres, and the cone on a sphere (issue #8902, Moise build A)

## What is a DEFINITION here

* `PLHomeomorphic X Y` — finite complexes `K`, `L` with `K.space = X`, `L.space = Y`, and
  mutually inverse maps `f : X → Y`, `g : Y → X` with `f` linear on the faces of `K` and `g`
  linear on the faces of `L`.
* `simplexBoundarySet τ` — the union of the hulls of the nonempty proper subsets of `τ`.
* `IsPLBall n X` — `X` is PL homeomorphic to the hull of an affinely independent `τ ⊆ E` with
  `n + 1` points.
* `IsPLSphere n X` — `X` is PL homeomorphic to `simplexBoundarySet τ` for an affinely
  independent `τ ⊆ E` with `n + 2` points.
* `simplexComplex τ`, `simplexBoundary τ` — the complexes of the nonempty (proper) subsets.

## What is a THEOREM here

* `simplexComplex_space`, `simplexBoundary_space` — their spaces are `convexHull τ` and
  `simplexBoundarySet τ`.
* `bary_notMem_simplexBoundarySet`, `raysMeetOnce_bary_simplexBoundarySet`,
  `pointCone_bary_simplexBoundarySet` — the barycentre `b` of `τ` is off the boundary, rays from
  `b` meet it once, and the cone from `b` on the boundary is `convexHull τ`.
* `isPLBall_convexHull`, `isPLSphere_simplexBoundarySet` — the models are a ball and a sphere.
* `IsPLSphere.isPLBall_pointCone` — **the cone on a PL `n`-sphere is a PL `(n+1)`-ball**: if
  `IsPLSphere n S`, `p ∉ S` and rays from `p` meet `S` at most once, then
  `IsPLBall (n + 1) (pointCone p S)`.
-/

namespace QOU.MathlibExt.PL

open Set Geometry Finset

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **PL homeomorphic**, realised simplicially on both sides. -/
def PLHomeomorphic (X Y : Set E) : Prop :=
  ∃ (K L : SimplicialComplex ℝ E) (f g : E → E), K.faces.Finite ∧ L.faces.Finite ∧
    K.space = X ∧ L.space = Y ∧ IsLinearOn K f ∧ IsLinearOn L g ∧ MapsTo f X Y ∧
    MapsTo g Y X ∧ InvOn g f X Y

/-- The boundary of the simplex on `τ`. -/
def simplexBoundarySet (τ : Finset E) : Set E :=
  ⋃ s ∈ {s : Finset E | s.Nonempty ∧ s ⊂ τ}, convexHull ℝ (s : Set E)

/-- **PL `n`-ball.** -/
def IsPLBall (n : ℕ) (X : Set E) : Prop :=
  ∃ τ : Finset E, τ.card = n + 1 ∧ AffineIndependent ℝ ((↑) : τ → E) ∧
    PLHomeomorphic X (convexHull ℝ (τ : Set E))

/-- **PL `n`-sphere.** -/
def IsPLSphere (n : ℕ) (X : Set E) : Prop :=
  ∃ τ : Finset E, τ.card = n + 2 ∧ AffineIndependent ℝ ((↑) : τ → E) ∧
    PLHomeomorphic X (simplexBoundarySet τ)

section Model

variable {τ : Finset E} (hτ : AffineIndependent ℝ ((↑) : τ → E))

/-- The complex of the nonempty subsets of `τ`. -/
def simplexComplex : SimplicialComplex ℝ E where
  faces := {s | s.Nonempty ∧ s ⊆ τ}
  empty_notMem h := Finset.not_nonempty_empty h.1
  indep h := hτ.mono (Finset.coe_subset.mpr h.2)
  down_closed hs hts ht := ⟨Finset.nonempty_iff_ne_empty.mpr ht, hts.trans hs.2⟩
  inter_subset_convexHull hs ht :=
    (hτ.convexHull_inter (Finset.coe_subset.mpr hs.2) (Finset.coe_subset.mpr ht.2)).ge

/-- The complex of the nonempty proper subsets of `τ`. -/
def simplexBoundary : SimplicialComplex ℝ E where
  faces := {s | s.Nonempty ∧ s ⊂ τ}
  empty_notMem h := Finset.not_nonempty_empty h.1
  indep h := hτ.mono (Finset.coe_subset.mpr h.2.subset)
  down_closed hs hts ht := ⟨Finset.nonempty_iff_ne_empty.mpr ht, hts.trans_ssubset hs.2⟩
  inter_subset_convexHull hs ht :=
    (hτ.convexHull_inter (Finset.coe_subset.mpr hs.2.subset)
      (Finset.coe_subset.mpr ht.2.subset)).ge

theorem simplexBoundary_space : (simplexBoundary hτ).space = simplexBoundarySet τ := rfl

theorem simplexComplex_space (hne : τ.Nonempty) :
    (simplexComplex hτ).space = convexHull ℝ (τ : Set E) := by
  apply Set.Subset.antisymm
  · exact iUnion₂_subset fun s hs => convexHull_mono (Finset.coe_subset.mpr hs.2)
  · exact fun x hx => SimplicialComplex.mem_space_iff.mpr ⟨τ, ⟨hne, subset_rfl⟩, hx⟩

lemma simplexComplex_faces_finite : (simplexComplex hτ).faces.Finite :=
  (τ.powerset.finite_toSet).subset fun _ hs => Finset.mem_coe.mpr (Finset.mem_powerset.mpr hs.2)

lemma simplexBoundary_faces_finite : (simplexBoundary hτ).faces.Finite :=
  (τ.powerset.finite_toSet).subset fun _ hs =>
    Finset.mem_coe.mpr (Finset.mem_powerset.mpr hs.2.subset)

end Model

theorem simplexBoundarySet_subset (τ : Finset E) :
    simplexBoundarySet τ ⊆ convexHull ℝ (τ : Set E) :=
  iUnion₂_subset fun _ hs => convexHull_mono (Finset.coe_subset.mpr hs.2.subset)

/-- Coordinates over `τ` of a point of the hull of `s ⊆ τ`, vanishing off `s`. -/
theorem exists_coords [DecidableEq E] {τ s : Finset E} (hs : s ⊆ τ) {x : E}
    (hx : x ∈ convexHull ℝ (s : Set E)) :
    ∃ α : E → ℝ, (∀ v ∈ τ, 0 ≤ α v) ∧ (∀ v ∈ τ, v ∉ s → α v = 0) ∧ ∑ v ∈ τ, α v = 1 ∧
      x = ∑ v ∈ τ, α v • v := by
  obtain ⟨w, hw0, hw1, rfl⟩ := Finset.mem_convexHull'.mp hx
  have hinter : τ ∩ s = s := Finset.inter_eq_right.mpr hs
  refine ⟨fun v => if v ∈ s then w v else 0, fun v _ => ?_, fun v _ hv => if_neg hv, ?_, ?_⟩
  · dsimp only
    split_ifs with h
    · exact hw0 v h
    · exact le_rfl
  · rw [Finset.sum_ite_mem, hinter, hw1]
  · simp_rw [ite_smul, zero_smul]
    rw [Finset.sum_ite_mem, hinter]

section Bary

variable {τ : Finset E}

lemma bary_eq_sum (τ : Finset E) : bary τ = ∑ v ∈ τ, ((τ.card : ℝ))⁻¹ • v := by
  rw [bary, Finset.smul_sum]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma sum_card_inv (hne : τ.Nonempty) : ∑ _v ∈ τ, ((τ.card : ℝ))⁻¹ = 1 := by
  rw [Finset.sum_const, nsmul_eq_mul, mul_inv_cancel₀ (Nat.cast_ne_zero.mpr hne.card_pos.ne')]

/-- A point strictly between the barycentre and the hull is off the boundary. -/
theorem notMem_boundary_aux [DecidableEq E] (hτ : AffineIndependent ℝ ((↑) : τ → E))
    {x y : E} (hx : x ∈ simplexBoundarySet τ) (hy : y ∈ convexHull ℝ (τ : Set E)) {t : ℝ}
    (ht0 : 0 ≤ t) (ht1 : t < 1) : x ≠ bary τ + t • (y - bary τ) := by
  intro hxe
  obtain ⟨s, ⟨hsne, hsτ⟩, hxs⟩ := mem_iUnion₂.mp hx
  obtain ⟨w, hwτ, hws⟩ := Finset.exists_of_ssubset hsτ
  have hne : τ.Nonempty := hsne.mono hsτ.subset
  obtain ⟨α, -, hα0, hα1, hαx⟩ := exists_coords hsτ.subset hxs
  obtain ⟨μ, hμ0, -, hμ1, hμy⟩ := exists_coords (subset_refl τ) hy
  set c : ℝ := ((τ.card : ℝ))⁻¹ with hc
  have hcpos : 0 < c := inv_pos.mpr (Nat.cast_pos.mpr hne.card_pos)
  have hβ1 : ∑ v ∈ τ, ((1 - t) * c + t * μ v) = 1 := by
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, hμ1, sum_card_inv hne]
    ring
  have hβx : x = ∑ v ∈ τ, ((1 - t) * c + t * μ v) • v := by
    rw [hxe, bary_eq_sum, hμy]
    simp_rw [add_smul, mul_smul, Finset.sum_add_distrib, ← Finset.smul_sum, ← hc]
    module
  have key := coords_unique hτ hα1 hβ1 (hαx.symm.trans hβx) w hwτ
  rw [hα0 w hwτ hws] at key
  have : 0 < (1 - t) * c + t * μ w :=
    add_pos_of_pos_of_nonneg (mul_pos (by linarith) hcpos) (mul_nonneg ht0 (hμ0 w hwτ))
  linarith

theorem bary_notMem_simplexBoundarySet [DecidableEq E]
    (hτ : AffineIndependent ℝ ((↑) : τ → E)) : bary τ ∉ simplexBoundarySet τ := by
  intro h
  refine notMem_boundary_aux hτ h (simplexBoundarySet_subset τ h) le_rfl zero_lt_one ?_
  simp

/-- **Rays from the barycentre meet the boundary once.** -/
theorem raysMeetOnce_bary_simplexBoundarySet [DecidableEq E]
    (hτ : AffineIndependent ℝ ((↑) : τ → E)) :
    RaysMeetOnce (bary τ) (simplexBoundarySet τ) := by
  intro x hx y hy t ht h
  rcases lt_trichotomy t 1 with ht1 | rfl | ht1
  · exact absurd (by rw [← h]; abel) (notMem_boundary_aux hτ hx
      (simplexBoundarySet_subset τ hy) ht.le ht1)
  · rw [one_smul] at h
    exact sub_left_injective h
  · refine absurd ?_ (notMem_boundary_aux hτ hy (simplexBoundarySet_subset τ hx)
      (inv_nonneg.mpr ht.le) (inv_lt_one_of_one_lt₀ ht1))
    rw [h, smul_smul, inv_mul_cancel₀ ht.ne', one_smul]
    abel

/-- **The cone from the barycentre on the boundary is the simplex.** -/
theorem pointCone_bary_simplexBoundarySet [DecidableEq E]
    (hτ : AffineIndependent ℝ ((↑) : τ → E)) (hne : τ.Nonempty) :
    pointCone (bary τ) (simplexBoundarySet τ) = convexHull ℝ (τ : Set E) := by
  rw [pointCone_eq]
  apply Set.Subset.antisymm
  · refine insert_subset (bary_mem_convexHull hne) ?_
    exact convexJoin_subset (singleton_subset_iff.mpr (bary_mem_convexHull hne))
      (simplexBoundarySet_subset τ) (convex_convexHull ℝ _)
  intro z hz
  by_cases hzb : z = bary τ
  · exact Or.inl hzb
  right
  obtain ⟨μ, hμ0, -, hμ1, hμz⟩ := exists_coords (subset_refl τ) hz
  set c : ℝ := ((τ.card : ℝ))⁻¹ with hc
  have hm : (0 : ℝ) < τ.card := Nat.cast_pos.mpr hne.card_pos
  obtain ⟨w0, hw0τ, hw0⟩ := τ.exists_min_image μ hne
  -- the minimum coordinate is below the barycentric one
  have hlt : μ w0 < c := by
    by_contra hge
    push_neg at hge
    have hall : ∀ v ∈ τ, μ v - c = 0 := by
      refine (Finset.sum_eq_zero_iff_of_nonneg fun v hv => ?_).mp ?_
      · linarith [hw0 v hv]
      · rw [Finset.sum_sub_distrib, hμ1, hc, sum_card_inv hne, sub_self]
    refine hzb ?_
    rw [hμz, bary_eq_sum]
    exact Finset.sum_congr rfl fun v hv => by rw [← hc, sub_eq_zero.mp (hall v hv)]
  set s : ℝ := 1 - τ.card * μ w0 with hs
  have hcm : (τ.card : ℝ) * c = 1 := mul_inv_cancel₀ hm.ne'
  have hspos : 0 < s := by
    have := mul_lt_mul_of_pos_left hlt hm
    linarith
  have hs1 : s ≤ 1 := by
    have := mul_nonneg hm.le (hμ0 w0 hw0τ)
    linarith
  set γ : E → ℝ := fun v => c + s⁻¹ * (μ v - c) with hγ
  have hγ0 : γ w0 = 0 := by
    rw [hγ]
    dsimp only
    have hc' : c = s⁻¹ * (c * s) := by field_simp
    have hcs : c * s = c - μ w0 := by rw [hs, mul_sub, mul_one, ← mul_assoc, mul_comm c,
      hcm, one_mul]
    rw [hcs] at hc'
    linarith
  have hγnn : ∀ v ∈ τ, 0 ≤ γ v := by
    intro v hv
    rw [← hγ0]
    simp only [hγ]
    have := mul_le_mul_of_nonneg_left (sub_le_sub_right (hw0 v hv) c)
      (inv_nonneg.mpr hspos.le)
    linarith
  have hγ1 : ∑ v ∈ τ, γ v = 1 := by
    simp only [hγ]
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_sub_distrib, hμ1, hc,
      sum_card_inv hne, sub_self, mul_zero, add_zero]
  set y : E := ∑ v ∈ τ, γ v • v with hy
  have hyz : y = bary τ + s⁻¹ • (z - bary τ) := by
    rw [hy, hμz, bary_eq_sum]
    simp only [hγ]
    simp_rw [add_smul, mul_smul, Finset.sum_add_distrib, ← Finset.smul_sum, sub_smul,
      Finset.sum_sub_distrib, ← hc]
  -- `y` lies on the face `τ.erase w0`
  have hsumE : ∑ v ∈ τ.erase w0, γ v = 1 := by
    rw [← hγ1, ← Finset.sum_erase_add _ _ hw0τ, hγ0, add_zero]
  have hyE : y = ∑ v ∈ τ.erase w0, γ v • v := by
    rw [hy, ← Finset.sum_erase_add _ _ hw0τ, hγ0, zero_smul, add_zero]
  have hEne : (τ.erase w0).Nonempty :=
    Finset.nonempty_of_sum_ne_zero (by rw [hsumE]; exact one_ne_zero)
  have hyB : y ∈ simplexBoundarySet τ := by
    refine mem_iUnion₂.mpr ⟨τ.erase w0, ⟨hEne, Finset.erase_ssubset hw0τ⟩, ?_⟩
    rw [Finset.mem_convexHull']
    exact ⟨γ, fun v hv => hγnn v (Finset.mem_of_mem_erase hv), hsumE, hyE.symm⟩
  rw [mem_convexJoin]
  refine ⟨bary τ, mem_singleton _, y, hyB, ?_⟩
  rw [segment_eq_image']
  refine ⟨s, ⟨hspos.le, hs1⟩, ?_⟩
  show bary τ + s • (y - bary τ) = z
  rw [hyz, add_sub_cancel_left, smul_smul, mul_inv_cancel₀ hspos.ne', one_smul]
  abel

end Bary

theorem PLHomeomorphic.refl {X : Set E} {K : SimplicialComplex ℝ E} (hK : K.faces.Finite)
    (hX : K.space = X) : PLHomeomorphic X X := by
  have hid : IsLinearOn K id := fun _ _ =>
    ⟨(ContinuousLinearMap.id ℝ E).toContinuousAffineMap, fun _ _ => rfl⟩
  exact ⟨K, K, id, id, hK, hK, hX, hX, hid, hid, mapsTo_id _, mapsTo_id _,
    ⟨fun _ _ => rfl, fun _ _ => rfl⟩⟩

theorem isPLBall_convexHull {n : ℕ} {τ : Finset E} (hcard : τ.card = n + 1)
    (hτ : AffineIndependent ℝ ((↑) : τ → E)) : IsPLBall n (convexHull ℝ (τ : Set E)) :=
  ⟨τ, hcard, hτ, PLHomeomorphic.refl (simplexComplex_faces_finite hτ)
    (simplexComplex_space hτ (Finset.card_pos.mp (by omega)))⟩

theorem isPLSphere_simplexBoundarySet {n : ℕ} {τ : Finset E} (hcard : τ.card = n + 2)
    (hτ : AffineIndependent ℝ ((↑) : τ → E)) : IsPLSphere n (simplexBoundarySet τ) :=
  ⟨τ, hcard, hτ, PLHomeomorphic.refl (simplexBoundary_faces_finite hτ)
    (simplexBoundary_space hτ)⟩

/-- **The cone on a PL `n`-sphere is a PL `(n + 1)`-ball.** -/
theorem IsPLSphere.isPLBall_pointCone [DecidableEq E] [FiniteDimensional ℝ E] {n : ℕ}
    {S : Set E} {p : E} (hS : IsPLSphere n S) (hp : p ∉ S) (hray : RaysMeetOnce p S) :
    IsPLBall (n + 1) (pointCone p S) := by
  obtain ⟨τ, hcard, hτ, K, L, f, g, hK, hL, hKS, hLS, hf, hg, hfm, hgm, hinv⟩ := hS
  subst hKS
  have hne : τ.Nonempty := Finset.card_pos.mp (by omega)
  have hb : bary τ ∉ L.space := hLS ▸ bary_notMem_simplexBoundarySet hτ
  have hrayb : RaysMeetOnce (bary τ) L.space := hLS ▸ raysMeetOnce_bary_simplexBoundarySet hτ
  have hT : convexHull ℝ (τ : Set E) = pointCone (bary τ) L.space := by
    rw [hLS, pointCone_bary_simplexBoundarySet hτ hne]
  rw [← hLS] at hfm hgm hinv
  refine ⟨τ, by omega, hτ, coneComplex K p hp hray, coneComplex L (bary τ) hb hrayb,
    coneFun p (bary τ) K.space f, coneFun (bary τ) p L.space g,
    coneComplex_faces_finite (hp := hp) (hray := hray) hK,
    coneComplex_faces_finite (hp := hb) (hray := hrayb) hL, ?_, ?_,
    isLinearOn_coneComplex hp hray hf, isLinearOn_coneComplex hb hrayb hg, ?_, ?_, ?_⟩
  · rw [coneComplex_space, ← pointCone_eq]
  · rw [coneComplex_space, ← pointCone_eq, hT]
  · rw [hT]
    exact coneFun_mapsTo hray hp hfm
  · rw [hT]
    exact coneFun_mapsTo hrayb hb hgm
  · rw [hT]
    exact coneFun_invOn hray hp hrayb hb hfm hgm hinv

end QOU.MathlibExt.PL
