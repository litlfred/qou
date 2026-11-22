/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLCone
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.Topology.Algebra.Module.FiniteDimension

set_option autoImplicit false

/-!
# Coning a map (issue #8902, Moise build part A, for part B's Schoenflies)

Given cone points `p` (for `S`) and `q` (for `S'`) that see their sets along rays, a map
`f : S → S'` extends radially to the cones: `p + s • (y - p) ↦ q + s • (f y - q)`, and `p ↦ q`.

## What is a DEFINITION here

* `ConeRep p S x s y` — `x = p + s • (y - p)` with `y ∈ S` and `s ∈ (0, 1]`.
* `coneSet p S` — `p` together with every `x` having such a representation.
* `coneFun p q S f` — the radial extension of `f`.

## What is a THEOREM here

* `ConeRep.unique` — the representation is unique when `p ∉ S` and rays from `p` meet `S` at most
  once.
* `coneFun_apex`, `coneFun_eq` — `p ↦ q`, and the radial formula.
* `coneSet_eq` — `coneSet p S = insert p (convexJoin ℝ {p} S)`, the space in `coneComplex_space`.
* `coneFun_eq_of_eqOn`, `coneFun_lineMap_of_eqOn` — if `f = A` (affine) on `convexHull σ`, the cone
  map sends `lineMap p y s` to `lineMap q (A y) s`: it is linear on the cone face.
* `coneFun_mapsTo`, `coneFun_leftInvOn`, `coneFun_invOn` — if `f` and `g` are mutually inverse
  between `S` and `S'`, the cone maps are mutually inverse between the cones; `coneFun_bijOn`.
* `exists_affine_extend` — in finite dimension, an affine map on `affineSpan σ` extends to an
  affine map with any prescribed value at a point off that span.
* `isLinearOn_coneComplex` — **the cone of a PL map is PL**: if `f` is linear on every face of
  `K`, then `coneFun p q K.space f` is linear on every face of `coneComplex K p hp hray`.

* `IsLinearOn.continuousOn` — a map linear on every face of a finite complex is continuous on its
  space; `continuousOn_coneFun` — so the cone of a PL map is continuous on `coneSet p K.space`.

## What is NOT proved here

Continuity of the cone of a merely continuous (non-PL) map; part B only needs the PL case.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- `x = p + s • (y - p)` with `y ∈ S`, `0 < s ≤ 1`. -/
def ConeRep (p : E) (S : Set E) (x : E) (s : ℝ) (y : E) : Prop :=
  y ∈ S ∧ s ∈ Ioc (0 : ℝ) 1 ∧ x = p + s • (y - p)

/-- The cone on `S` with apex `p`. -/
def coneSet (p : E) (S : Set E) : Set E :=
  insert p {x | ∃ s y, ConeRep p S x s y}

lemma ConeRep.ne_apex {p : E} {S : Set E} (hp : p ∉ S) {x : E} {s : ℝ} {y : E}
    (h : ConeRep p S x s y) : x ≠ p := by
  obtain ⟨hy, hs, rfl⟩ := h
  intro he
  have h0 : s • (y - p) = 0 := by simpa using he
  rcases smul_eq_zero.mp h0 with h | h
  · exact hs.1.ne' h
  · exact hp (sub_eq_zero.mp h ▸ hy)

/-- **The cone representation is unique.** -/
theorem ConeRep.unique {p : E} {S : Set E} (hray : RaysMeetOnce p S) (hp : p ∉ S) {x : E}
    {s s' : ℝ} {y y' : E} (h : ConeRep p S x s y) (h' : ConeRep p S x s' y') :
    s = s' ∧ y = y' := by
  have hne := h.ne_apex hp
  obtain ⟨hy, hs, rfl⟩ := h
  obtain ⟨hy', hs', he⟩ := h'
  have hyy := eq_of_cone_coords hray hy hy' hs.1.le hs'.1.le he hne
  subst hyy
  refine ⟨?_, rfl⟩
  have h2 : (s - s') • (y - p) = 0 := by
    rw [sub_smul, sub_eq_zero]
    exact add_left_cancel he
  rcases smul_eq_zero.mp h2 with h3 | h3
  · exact sub_eq_zero.mp h3
  · exact absurd (sub_eq_zero.mp h3 ▸ hy) hp

open Classical in
/-- **The cone of a map**: `p + s • (y - p) ↦ q + s • (f y - q)` and `p ↦ q`. -/
noncomputable def coneFun (p q : E) (S : Set E) (f : E → E) (x : E) : E :=
  if h : ∃ sy : ℝ × E, ConeRep p S x sy.1 sy.2 then q + h.choose.1 • (f h.choose.2 - q) else q

lemma coneFun_eq {p q : E} {S : Set E} {f : E → E} (hray : RaysMeetOnce p S) (hp : p ∉ S)
    {x : E} {s : ℝ} {y : E} (h : ConeRep p S x s y) :
    coneFun p q S f x = q + s • (f y - q) := by
  have hex : ∃ sy : ℝ × E, ConeRep p S x sy.1 sy.2 := ⟨(s, y), h⟩
  rw [coneFun, dif_pos hex]
  obtain ⟨h1, h2⟩ := ConeRep.unique hray hp hex.choose_spec h
  rw [h1, h2]

lemma coneFun_apex {p q : E} {S : Set E} {f : E → E} (hp : p ∉ S) :
    coneFun p q S f p = q := by
  rw [coneFun, dif_neg]
  rintro ⟨sy, h⟩
  exact h.ne_apex hp rfl

/-- The image of a cone representation. -/
lemma ConeRep.map {p q : E} {S S' : Set E} {f : E → E} (hf : MapsTo f S S') {x : E} {s : ℝ}
    {y : E} (h : ConeRep p S x s y) : ConeRep q S' (q + s • (f y - q)) s (f y) :=
  ⟨hf h.1, h.2.1, rfl⟩

theorem coneFun_mapsTo {p q : E} {S S' : Set E} {f : E → E} (hray : RaysMeetOnce p S)
    (hp : p ∉ S) (hf : MapsTo f S S') : MapsTo (coneFun p q S f) (coneSet p S) (coneSet q S') := by
  rintro x (rfl | ⟨s, y, h⟩)
  · rw [coneFun_apex hp]
    exact mem_insert _ _
  · rw [coneFun_eq hray hp h]
    exact Or.inr ⟨s, f y, h.map hf⟩

theorem coneFun_leftInvOn {p q : E} {S S' : Set E} {f g : E → E} (hray : RaysMeetOnce p S)
    (hp : p ∉ S) (hray' : RaysMeetOnce q S') (hq : q ∉ S') (hf : MapsTo f S S')
    (hgf : LeftInvOn g f S) : LeftInvOn (coneFun q p S' g) (coneFun p q S f) (coneSet p S) := by
  rintro x (rfl | ⟨s, y, h⟩)
  · rw [coneFun_apex hp, coneFun_apex hq]
  · rw [coneFun_eq hray hp h, coneFun_eq hray' hq (h.map hf), hgf h.1, h.2.2]

/-- **Mutually inverse maps cone to mutually inverse maps.** -/
theorem coneFun_invOn {p q : E} {S S' : Set E} {f g : E → E} (hray : RaysMeetOnce p S)
    (hp : p ∉ S) (hray' : RaysMeetOnce q S') (hq : q ∉ S') (hf : MapsTo f S S')
    (hg : MapsTo g S' S) (hinv : InvOn g f S S') :
    InvOn (coneFun q p S' g) (coneFun p q S f) (coneSet p S) (coneSet q S') :=
  ⟨coneFun_leftInvOn hray hp hray' hq hf hinv.1,
    coneFun_leftInvOn hray' hq hray hp hg hinv.2⟩

/-- **The cone of a bijection is a bijection of the cones.** -/
theorem coneFun_bijOn {p q : E} {S S' : Set E} {f g : E → E} (hray : RaysMeetOnce p S)
    (hp : p ∉ S) (hray' : RaysMeetOnce q S') (hq : q ∉ S') (hf : MapsTo f S S')
    (hg : MapsTo g S' S) (hinv : InvOn g f S S') :
    BijOn (coneFun p q S f) (coneSet p S) (coneSet q S') :=
  (coneFun_invOn hray hp hray' hq hf hg hinv).bijOn (coneFun_mapsTo hray hp hf)
    (coneFun_mapsTo hray' hq hg)

/-- The cone set is the cone space `insert p (convexJoin ℝ {p} S)` of `coneComplex_space`. -/
theorem coneSet_eq (p : E) (S : Set E) : coneSet p S = insert p (convexJoin ℝ {p} S) := by
  ext x
  rw [coneSet, mem_insert_iff, mem_insert_iff, mem_convexJoin]
  constructor
  · rintro (rfl | ⟨s, y, hy, hs, rfl⟩)
    · exact Or.inl rfl
    · refine Or.inr ⟨p, rfl, y, hy, ?_⟩
      rw [segment_eq_image']
      exact ⟨s, Ioc_subset_Icc_self hs, rfl⟩
  · rintro (rfl | ⟨a, ha, y, hy, hx⟩)
    · exact Or.inl rfl
    rw [mem_singleton_iff] at ha
    subst ha
    rw [segment_eq_image'] at hx
    obtain ⟨b, hb, rfl⟩ := hx
    rcases hb.1.lt_or_eq with hb0 | rfl
    · exact Or.inr ⟨b, y, hy, ⟨hb0, hb.2⟩, rfl⟩
    · exact Or.inl (by simp)

/-- **The cone of a map is linear on cone faces**: if `f` agrees with an affine `A` on the hull of
`σ ⊆ S`, then on the hull of `insert p σ` the cone map is `p + s • (y - p) ↦ q + s • (A y - q)`,
i.e. it sends the convex combination `(1 - s) p + s y` to `(1 - s) q + s (A y)`. -/
theorem coneFun_eq_of_eqOn {p q : E} {S : Set E} {f : E → E} (hray : RaysMeetOnce p S)
    (hp : p ∉ S) {σ : Set E} (hσ : convexHull ℝ σ ⊆ S) {A : E →ᵃ[ℝ] E}
    (hA : EqOn f A (convexHull ℝ σ)) {y : E} (hy : y ∈ convexHull ℝ σ) {s : ℝ}
    (hs : s ∈ Icc (0 : ℝ) 1) : coneFun p q S f (p + s • (y - p)) = q + s • (A y - q) := by
  rcases hs.1.lt_or_eq with hs0 | rfl
  · rw [coneFun_eq hray hp ⟨hσ hy, ⟨hs0, hs.2⟩, rfl⟩, hA hy]
  · simp [coneFun_apex hp]

/-- The same statement in `lineMap` form. -/
theorem coneFun_lineMap_of_eqOn {p q : E} {S : Set E} {f : E → E} (hray : RaysMeetOnce p S)
    (hp : p ∉ S) {σ : Set E} (hσ : convexHull ℝ σ ⊆ S) {A : E →ᵃ[ℝ] E}
    (hA : EqOn f A (convexHull ℝ σ)) {y : E} (hy : y ∈ convexHull ℝ σ) {s : ℝ}
    (hs : s ∈ Icc (0 : ℝ) 1) :
    coneFun p q S f (AffineMap.lineMap p y s) = AffineMap.lineMap q (A y) s := by
  rw [AffineMap.lineMap_apply_module', AffineMap.lineMap_apply_module', add_comm,
    coneFun_eq_of_eqOn hray hp hσ hA hy hs, add_comm]

section Extend

variable {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- **Affine extension off an affine span**: in finite dimension, an affine map `A` extends from
`affineSpan σ` to an affine map taking any prescribed value `q` at a point `p ∉ affineSpan σ`. -/
theorem exists_affine_extend [FiniteDimensional ℝ E] {σ : Set E} {p : E}
    (hp : p ∉ affineSpan ℝ σ) (A : E →ᴬ[ℝ] F) (q : F) :
    ∃ B : E →ᴬ[ℝ] F, B p = q ∧ EqOn B A (affineSpan ℝ σ) := by
  rcases σ.eq_empty_or_nonempty with rfl | ⟨y0, hy0⟩
  · refine ⟨ContinuousAffineMap.const ℝ E q, rfl, fun x hx => ?_⟩
    simp only [AffineSubspace.span_empty, SetLike.mem_coe] at hx
    exact absurd hx (AffineSubspace.notMem_bot ℝ E x)
  have hy0' : y0 ∈ affineSpan ℝ σ := mem_affineSpan ℝ hy0
  have hv : p - y0 ∉ (affineSpan ℝ σ).direction := fun h =>
    hp ((AffineSubspace.vsub_right_mem_direction_iff_mem hy0' p).mp h)
  obtain ⟨φ, hφv, hφW⟩ :=
    (affineSpan ℝ σ).direction.exists_dual_map_eq_bot_of_notMem hv inferInstance
  set L : E →ₗ[ℝ] F := (((φ (p - y0))⁻¹ • φ : Module.Dual ℝ E)).smulRight (q - A p) with hLdef
  have hLc : Continuous L := LinearMap.continuous_of_finiteDimensional L
  have hLp : L (p - y0) = q - A p := by
    rw [hLdef, LinearMap.smulRight_apply, LinearMap.smul_apply, smul_eq_mul,
      inv_mul_cancel₀ hφv, one_smul]
  have hL0 : ∀ x ∈ affineSpan ℝ σ, L (x - y0) = 0 := by
    intro x hx
    have hw : x - y0 ∈ (affineSpan ℝ σ).direction := AffineSubspace.vsub_mem_direction hx hy0'
    have h0 : φ (x - y0) = 0 := by
      have := Submodule.mem_map_of_mem (f := φ) hw
      rw [hφW] at this
      simpa using this
    simp [hLdef, h0]
  refine ⟨⟨A.toAffineMap + (L.toAffineMap - AffineMap.const ℝ E (L y0)), ?_⟩, ?_, ?_⟩
  · change Continuous fun x => A x + (L x - L y0)
    exact A.cont.add (hLc.sub continuous_const)
  · change A p + (L p - L y0) = q
    rw [← map_sub, hLp]
    abel
  · intro x hx
    change A x + (L x - L y0) = A x
    rw [← map_sub, hL0 x hx, add_zero]

end Extend

/-- **The cone of a PL map is PL**: if `f` is linear on every face of `K`, the cone map is linear
on every face of the cone complex. -/
theorem isLinearOn_coneComplex [DecidableEq E] [FiniteDimensional ℝ E]
    {K : Geometry.SimplicialComplex ℝ E} {p q : E} (hp : p ∉ K.space)
    (hray : RaysMeetOnce p K.space) {f : E → E} (hf : IsLinearOn K f) :
    IsLinearOn (coneComplex K p hp hray) (coneFun p q K.space f) := by
  intro s hs
  rcases mem_coneComplex_faces.mp hs with hs | ⟨σ, hσ | rfl, rfl⟩
  · obtain ⟨A, hA⟩ := hf s hs
    refine ⟨A, fun x hx => ?_⟩
    have hxK := K.convexHull_subset_space hs hx
    rw [coneFun_eq hray hp (s := 1) (y := x) ⟨hxK, ⟨one_pos, le_rfl⟩, by simp⟩]
    simp [hA hx]
  · obtain ⟨A, hA⟩ := hf σ hσ
    have hσK := K.convexHull_subset_space hσ
    obtain ⟨B, hBp, hBA⟩ := exists_affine_extend (notMem_affineSpan_of_rays hray hp hσK) A q
    refine ⟨B, fun x hx => ?_⟩
    rw [Finset.coe_insert, mem_convexHull_insert_iff] at hx
    rcases hx with rfl | ⟨y, hy, b, hb, rfl⟩
    · rw [coneFun_apex hp, hBp]
    rw [coneFun_eq_of_eqOn (A := A.toAffineMap) hray hp hσK (fun z hz => hA hz) hy hb]
    have e1 : B.toAffineMap y = A y := hBA (convexHull_subset_affineSpan _ hy)
    have e2 : B.toAffineMap p = q := hBp
    have h1 : B (p + b • (y - p)) = B.toAffineMap (AffineMap.lineMap p y b) := by
      rw [AffineMap.lineMap_apply_module', add_comm]; rfl
    rw [h1, AffineMap.apply_lineMap, AffineMap.lineMap_apply_module', e1, e2]
    change q + b • (A y - q) = b • (A y - q) + q
    abel
  · refine ⟨ContinuousAffineMap.const ℝ E q, fun x hx => ?_⟩
    simp only [insert_empty_eq, Finset.coe_singleton, convexHull_singleton,
      mem_singleton_iff] at hx
    subst hx
    rw [coneFun_apex hp]
    rfl

/-- A map linear on every face of a finite complex is continuous on its space. -/
theorem IsLinearOn.continuousOn {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {K : Geometry.SimplicialComplex ℝ E} {f : E → F} (hf : IsLinearOn K f)
    (hK : K.faces.Finite) : ContinuousOn f K.space := by
  have : Finite K.faces := hK.to_subtype
  have hsp : K.space = ⋃ s : K.faces, convexHull ℝ ((s : Finset E) : Set E) := by
    ext x
    simp [Geometry.SimplicialComplex.space]
  rw [hsp]
  refine (locallyFinite_of_finite _).continuousOn_iUnion
    (fun s => s.1.finite_toSet.isCompact_convexHull.isClosed) fun s => ?_
  obtain ⟨A, hA⟩ := hf s.1 s.2
  exact A.cont.continuousOn.congr hA

/-- **The cone of a PL map is continuous on the cone.** -/
theorem continuousOn_coneFun [DecidableEq E] [FiniteDimensional ℝ E]
    {K : Geometry.SimplicialComplex ℝ E} {p q : E} (hp : p ∉ K.space)
    (hray : RaysMeetOnce p K.space) {f : E → E} (hf : IsLinearOn K f) (hK : K.faces.Finite) :
    ContinuousOn (coneFun p q K.space f) (coneSet p K.space) := by
  rw [coneSet_eq, ← coneComplex_space (hp := hp) (hray := hray)]
  exact (isLinearOn_coneComplex (q := q) hp hray hf).continuousOn
    (coneComplex_faces_finite (hp := hp) (hray := hray) hK)

end QOU.MathlibExt.PL
