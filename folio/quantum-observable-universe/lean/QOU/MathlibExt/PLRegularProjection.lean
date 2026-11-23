/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLGenericSlide
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar

set_option autoImplicit false

/-!
# Regular projections of polygonal links (issue #8902, stage 3)

**Every polygonal link in `ℝ³` is Δ-equivalent to one whose projection to the plane
`(x, y, z) ↦ (x, y)` is regular** (`PolygonalLink.exists_deltaEquiv_isRegularProj`).

The projection is fixed. The proof moves the vertices one at a time, each by a small generic
slide (`Shape.Simple.exists_slide`, `PLGenericSlide.lean`), into general position.

## What is a DEFINITION here

* `pr : ℝ³ →ₗ ℝ²` — the vertical projection `x ↦ (x 0, x 1)`.
* `Coll p q r` — three points of the plane are collinear: `det (q - p, r - p) = 0`.
* `PolygonalLink.IsRegularProj L` — the classical regular projection (Reidemeister;
  Burde–Zieschang, *Knots*, 1.12): every point of the plane has **at most two** preimages on
  the link, and **no vertex** shares its image with another point of the link. These two
  conditions force finitely many double points, each a transverse crossing of two edges away
  from the vertices; that consequence is not needed below and is not stated.
* `Shape.GenPos W S` — general position of the vertices in a set `S` of slots: their images are
  distinct, no three are collinear, and no three edges with all endpoints in `S` have images
  through a common point.

## What is a THEOREM here

* `Shape.GenPos.isRegularProj` — general position of all vertices implies a regular
  projection.
* `Shape.GenPos.exists_step` — one more vertex can be put in general position by a
  Δ-equivalence: the new position avoids finitely many proper affine subspaces of `ℝ³`
  (Lebesgue-null, `MeasureTheory.Measure.addHaar_affineSubspace`) inside the ball given by
  `exists_slide`, and a ball has positive measure.
* `PolygonalLink.exists_deltaEquiv_isRegularProj` — **the theorem of stage 3**.

## What is NOT proved here

* That the double points are finitely many and transverse (true, see above, not stated).
* Diagrams, and the comparison of the diagrams of two regular projections (stages 4–5).
* Nothing here uses or cites a theorem of PL topology; the only external input is Mathlib's
  measure theory (a proper affine subspace of `ℝ³` is Lebesgue-null).
-/

namespace QOU.MathlibExt.PL

open Set MeasureTheory

/-! ## The projection and collinearity in the plane -/

/-- **The vertical projection** `ℝ³ → ℝ²`, `x ↦ (x 0, x 1)`. -/
noncomputable def pr : R3 →ₗ[ℝ] ℝ × ℝ := (LinearMap.proj 0).prod (LinearMap.proj 1)

@[simp] lemma pr_apply (x : R3) : pr x = (x 0, x 1) := rfl

/-- The determinant of two vectors of the plane. -/
def det2 (u v : ℝ × ℝ) : ℝ := u.1 * v.2 - u.2 * v.1

/-- **Three points of the plane are collinear.** -/
def Coll (p q r : ℝ × ℝ) : Prop := det2 (q - p) (r - p) = 0

lemma Coll.swap₁₂ {p q r : ℝ × ℝ} (h : Coll p q r) : Coll q p r := by
  unfold Coll det2 at *
  simp only [Prod.fst_sub, Prod.snd_sub] at *
  linear_combination -h

lemma Coll.swap₂₃ {p q r : ℝ × ℝ} (h : Coll p q r) : Coll p r q := by
  unfold Coll det2 at *
  linear_combination -h

lemma Coll.rot {p q r : ℝ × ℝ} (h : Coll p q r) : Coll q r p := h.swap₁₂.swap₂₃

lemma Coll.rot' {p q r : ℝ × ℝ} (h : Coll p q r) : Coll r p q := h.rot.rot

/-- A point of a segment is collinear with its endpoints. -/
lemma coll_of_mem_segment {p q y : ℝ × ℝ} (hy : y ∈ segment ℝ p q) : Coll p q y := by
  obtain ⟨a, b, -, -, hab, rfl⟩ := hy
  obtain rfl : a = 1 - b := by linarith
  unfold Coll det2
  simp only [Prod.fst_sub, Prod.snd_sub, Prod.fst_add, Prod.snd_add, Prod.smul_fst,
    Prod.smul_snd, smul_eq_mul]
  ring

/-- **Two segments meet in at most one point**, unless the first one's line contains both
endpoints of the second. -/
lemma coll_of_two_mem {p₁ p₂ p₃ p₄ y y' : ℝ × ℝ} (hne : y ≠ y')
    (hy₁ : y ∈ segment ℝ p₁ p₂) (hy₂ : y ∈ segment ℝ p₃ p₄)
    (hy₁' : y' ∈ segment ℝ p₁ p₂) (hy₂' : y' ∈ segment ℝ p₃ p₄) :
    Coll p₁ p₂ p₃ ∧ Coll p₁ p₂ p₄ := by
  have h1 := coll_of_mem_segment hy₁
  have h2 := coll_of_mem_segment hy₁'
  obtain ⟨a, b, -, -, hab, rfl⟩ := hy₂
  obtain ⟨a', b', -, -, hab', rfl⟩ := hy₂'
  obtain rfl : a = 1 - b := by linarith
  obtain rfl : a' = 1 - b' := by linarith
  have hb : b' - b ≠ 0 := by
    intro h
    obtain rfl : b' = b := by linarith
    exact hne rfl
  unfold Coll det2 at *
  simp only [Prod.fst_sub, Prod.snd_sub, Prod.fst_add, Prod.snd_add, Prod.smul_fst,
    Prod.smul_snd, smul_eq_mul] at *
  constructor
  · apply (mul_eq_zero.mp _).resolve_right hb
    linear_combination b' * h1 - b * h2
  · apply (mul_eq_zero.mp _).resolve_right hb
    linear_combination -(1 - b') * h1 + (1 - b) * h2

/-- Two segments from a common endpoint `p` in non-collinear directions meet only in `p`. -/
lemma eq_of_mem_segment_of_not_coll {p q r y : ℝ × ℝ} (h : ¬ Coll p q r)
    (hy : y ∈ segment ℝ p q) (hy' : y ∈ segment ℝ p r) : y = p := by
  obtain ⟨a, b, -, -, hab, rfl⟩ := hy
  obtain ⟨a', b', -, -, hab', he⟩ := hy'
  obtain rfl : a = 1 - b := by linarith
  obtain rfl : a' = 1 - b' := by linarith
  have hb : b = 0 := by
    by_contra hb
    apply h
    unfold Coll det2
    have e1 := congrArg Prod.fst he
    have e2 := congrArg Prod.snd he
    simp only [Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul] at e1 e2
    simp only [Prod.fst_sub, Prod.snd_sub]
    apply (mul_eq_zero.mp _).resolve_left hb
    linear_combination -(r.2 - p.2) * e1 + (r.1 - p.1) * e2
  subst hb
  simp

/-- `pr` is injective on a segment whose endpoints have different images. -/
lemma eq_of_pr_eq_of_mem_segment {p q x y : R3} (hpq : pr p ≠ pr q)
    (hx : x ∈ segment ℝ p q) (hy : y ∈ segment ℝ p q) (h : pr x = pr y) : x = y := by
  obtain ⟨a, b, -, -, hab, rfl⟩ := hx
  obtain ⟨a', b', -, -, hab', rfl⟩ := hy
  obtain rfl : a = 1 - b := by linarith
  obtain rfl : a' = 1 - b' := by linarith
  have hb : b = b' := by
    by_contra hb
    apply hpq
    have hb' : b - b' ≠ 0 := sub_ne_zero.mpr hb
    simp only [map_add, map_smul, pr_apply, Prod.mk.injEq] at h ⊢
    simp only [Prod.smul_mk, Prod.mk_add_mk, smul_eq_mul, Prod.mk.injEq] at h
    constructor
    · have := (mul_eq_zero.mp (show (b - b') * (q 0 - p 0) = 0 by linear_combination h.1)).resolve_left hb'
      linarith
    · have := (mul_eq_zero.mp (show (b - b') * (q 1 - p 1) = 0 by linear_combination h.2)).resolve_left hb'
      linarith
  rw [hb]

lemma pr_mem_segment {p q x : R3} (hx : x ∈ segment ℝ p q) :
    pr x ∈ segment ℝ (pr p) (pr q) := by
  obtain ⟨a, b, ha, hb, hab, rfl⟩ := hx
  exact ⟨a, b, ha, hb, hab, by simp only [map_add, map_smul]⟩

/-! ## Null sets of `ℝ³` -/

/-- The linear form `z ↦ det (w, pr z)`. -/
noncomputable def lineForm (w : ℝ × ℝ) : R3 →ₗ[ℝ] ℝ := w.1 • LinearMap.proj 1 - w.2 • LinearMap.proj 0

lemma lineForm_apply (w : ℝ × ℝ) (z : R3) : lineForm w z = det2 w (pr z) := by
  simp [lineForm, det2]

lemma lineForm_ne_zero {w : ℝ × ℝ} (hw : w ≠ 0) : lineForm w ≠ 0 := by
  intro h
  apply hw
  have h0 := LinearMap.congr_fun h (Pi.single 0 1)
  have h1 := LinearMap.congr_fun h (Pi.single 1 1)
  simp [lineForm] at h0 h1
  exact Prod.ext h1 h0

/-- A proper affine subspace through `p` with direction `S ≠ ⊤` is null. -/
lemma volume_affine_null (p : R3) {S : Submodule ℝ R3} (hS : S ≠ ⊤) :
    volume {c : R3 | c - p ∈ S} = 0 := by
  have : {c : R3 | c - p ∈ S} = (AffineSubspace.mk' p S : Set R3) := by
    ext c; simp [AffineSubspace.mem_mk', vsub_eq_sub]
  rw [this]
  apply Measure.addHaar_affineSubspace
  intro h
  apply hS
  have := congrArg AffineSubspace.direction h
  rwa [AffineSubspace.direction_mk', AffineSubspace.direction_top] at this

lemma volume_kernel_null (p : R3) {φ : R3 →ₗ[ℝ] ℝ} (hφ : φ ≠ 0) :
    volume {c : R3 | φ (c - p) = 0} = 0 :=
  volume_affine_null p (S := LinearMap.ker φ) (fun h => hφ (LinearMap.ker_eq_top.mp h))

/-- **The points `c` whose image is collinear with two distinct image points are null.** -/
lemma volume_coll_null {P : R3} {q : ℝ × ℝ} (h : pr P ≠ q) :
    volume {c : R3 | Coll (pr P) q (pr c)} = 0 := by
  have hw : q - pr P ≠ 0 := sub_ne_zero.mpr h.symm
  refine measure_mono_null (fun c hc => ?_) (volume_kernel_null P (lineForm_ne_zero hw))
  simp only [mem_setOf_eq] at hc ⊢
  rw [map_sub, lineForm_apply, lineForm_apply]
  unfold Coll at hc
  unfold det2 at hc ⊢
  simp only [Prod.fst_sub, Prod.snd_sub] at hc ⊢
  linear_combination hc

/-- A span of two vectors is a proper subspace of `ℝ³`. -/
lemma span_pair_ne_top (u w : R3) : Submodule.span ℝ {u, w} ≠ ⊤ := by
  intro h
  have h1 : Set.finrank ℝ ({u, w} : Set R3) ≤ 2 := by
    have := finrank_range_le_card (R := ℝ) ![u, w]
    simpa [Set.pair_comm] using this
  unfold Set.finrank at h1
  rw [h, finrank_top, Module.finrank_fin_fun] at h1
  omega

lemma volume_span_null (p u w : R3) :
    volume {c : R3 | c - p ∈ Submodule.span ℝ {u, w}} = 0 :=
  volume_affine_null p (span_pair_ne_top u w)

/-- Outside a null set there are points arbitrarily close to any point. -/
lemma exists_near_not_mem {x : R3} {ε : ℝ} (hε : 0 < ε) {B : Set R3} (hB : volume B = 0) :
    ∃ c, dist c x < ε ∧ c ∉ B := by
  by_contra h
  push_neg at h
  have hsub : Metric.ball x ε ⊆ B := fun c hc => h c (Metric.mem_ball.mp hc)
  exact (Metric.measure_ball_pos volume x hε).ne' (measure_mono_null hsub hB)

/-! ## Regular projections and general position -/

/-- **A regular projection** (Reidemeister; Burde–Zieschang 1.12) for the vertical projection
`pr`: every point of the plane has at most two preimages on the link, and a vertex is the only
point of the link over its image. -/
def PolygonalLink.IsRegularProj (L : PolygonalLink R3) : Prop :=
  (∀ x ∈ L.carrier, ∀ y ∈ L.carrier, ∀ z ∈ L.carrier, pr x = pr y → pr x = pr z →
      x = y ∨ x = z ∨ y = z) ∧
    ∀ i (j : Fin ((L.comp i).n + 1)), ∀ x ∈ L.carrier, pr x = pr ((L.comp i).v j) →
      x = (L.comp i).v j

namespace Shape

variable {σ : Shape}

/-- The image in the plane of the edge in slot `e`. -/
def pe (W : σ.Slot → R3) (e : σ.Slot) : Set (ℝ × ℝ) := segment ℝ (pr (W e)) (pr (W (nx e)))

lemma pr_mem_pe {W : σ.Slot → R3} {e : σ.Slot} {x : R3} (hx : x ∈ edgeW W e) :
    pr x ∈ pe W e :=
  pr_mem_segment hx

/-- **General position of the vertices in `S`**: distinct images, no three images collinear,
and no three edges with all endpoints in `S` whose images share a point. -/
structure GenPos (W : σ.Slot → R3) (S : Set σ.Slot) : Prop where
  inj : ∀ t ∈ S, ∀ u ∈ S, t ≠ u → pr (W t) ≠ pr (W u)
  noncoll : ∀ t ∈ S, ∀ u ∈ S, ∀ v ∈ S, t ≠ u → t ≠ v → u ≠ v →
    ¬ Coll (pr (W t)) (pr (W u)) (pr (W v))
  notriple : ∀ e f g : σ.Slot, e ∈ S → nx e ∈ S → f ∈ S → nx f ∈ S → g ∈ S → nx g ∈ S →
    e ≠ f → e ≠ g → f ≠ g → ∀ y, y ∈ pe W e → y ∈ pe W f → y ∈ pe W g → False

lemma genPos_empty (W : σ.Slot → R3) : GenPos W ∅ :=
  ⟨by simp, by simp, by simp⟩

variable {W : σ.Slot → R3}

/-- **General position of all vertices gives a regular projection.** -/
theorem GenPos.isRegularProj (hW : Simple W) (hG : GenPos W univ) :
    (link W hW).IsRegularProj := by
  have hedge : ∀ e, pr (W e) ≠ pr (W (nx e)) := fun e =>
    hG.inj e trivial (nx e) trivial (nx_ne e).symm
  refine ⟨fun x hx y hy z hz hxy hxz => ?_, fun i j x hx hxv => ?_⟩
  · rw [link_carrier] at hx hy hz
    obtain ⟨e, hxe⟩ := mem_iUnion.mp hx
    obtain ⟨f, hyf⟩ := mem_iUnion.mp hy
    obtain ⟨g, hzg⟩ := mem_iUnion.mp hz
    by_cases hef : e = f
    · rw [← hef] at hyf
      exact Or.inl (eq_of_pr_eq_of_mem_segment (hedge e) hxe hyf hxy)
    by_cases heg : e = g
    · rw [← heg] at hzg
      exact Or.inr (Or.inl (eq_of_pr_eq_of_mem_segment (hedge e) hxe hzg hxz))
    by_cases hfg : f = g
    · rw [← hfg] at hzg
      exact Or.inr (Or.inr (eq_of_pr_eq_of_mem_segment (hedge f) hyf hzg (hxy.symm.trans hxz)))
    exact (hG.notriple e f g trivial trivial trivial trivial trivial trivial hef heg hfg (pr x)
      (pr_mem_pe hxe) (hxy ▸ pr_mem_pe hyf) (hxz ▸ pr_mem_pe hzg)).elim
  · show x = W ⟨i, j⟩
    have hxv' : pr x = pr (W ⟨i, j⟩) := hxv
    rw [link_carrier] at hx
    obtain ⟨e, hxe⟩ := mem_iUnion.mp hx
    by_cases h1 : (⟨i, j⟩ : σ.Slot) = e
    · exact eq_of_pr_eq_of_mem_segment (hedge e) hxe
        (by rw [h1]; exact left_mem_edgeW e) hxv'
    by_cases h2 : (⟨i, j⟩ : σ.Slot) = nx e
    · exact eq_of_pr_eq_of_mem_segment (hedge e) hxe
        (by rw [h2]; exact right_mem_edgeW e) hxv'
    exfalso
    have hc := coll_of_mem_segment (pr_mem_pe hxe)
    rw [hxv'] at hc
    exact hG.noncoll e trivial (nx e) trivial ⟨i, j⟩ trivial (nx_ne e).symm (Ne.symm h1)
      (Ne.symm h2) hc

variable {S : Set σ.Slot}

/-- In general position, the images of two distinct edges meet in at most one point. -/
lemma GenPos.pe_inter_unique (hG : GenPos W S) {e f : σ.Slot} (he : e ∈ S) (hne : nx e ∈ S)
    (hf : f ∈ S) (hnf : nx f ∈ S) (hef : e ≠ f) {y y' : ℝ × ℝ} (hy : y ∈ pe W e)
    (hyf : y ∈ pe W f) (hy' : y' ∈ pe W e) (hyf' : y' ∈ pe W f) : y = y' := by
  by_contra hne'
  obtain ⟨h3, h4⟩ := coll_of_two_mem hne' hy hyf hy' hyf'
  by_cases h1 : f = nx e
  · refine hG.noncoll e he (nx e) hne (nx f) hnf (nx_ne e).symm ?_ ?_ h4
    · rw [h1]; exact (nx_nx_ne e).symm
    · exact fun h => hef (nx_injective h)
  · exact hG.noncoll e he (nx e) hne f hf (nx_ne e).symm hef (Ne.symm h1) h3

/-- In general position, a vertex of `S` whose image is on the image of an edge is one of the
edge's endpoints. -/
lemma GenPos.incident (hG : GenPos W S) {e x : σ.Slot} (he : e ∈ S) (hne : nx e ∈ S)
    (hx : x ∈ S) (h : pr (W x) ∈ pe W e) : x = e ∨ x = nx e := by
  by_contra hc
  push_neg at hc
  exact hG.noncoll e he (nx e) hne x hx (nx_ne e).symm (Ne.symm hc.1) (Ne.symm hc.2)
    (coll_of_mem_segment h)

/-- **One more vertex in general position.** If the vertices in `S` are in general position
and `b ∉ S`, then a Δ-equivalent link has the vertices in `insert b S` in general position; only
the vertex `b` moves. -/
theorem GenPos.exists_step (hW : Simple W) (hG : GenPos W S) {b : σ.Slot} (hb : b ∉ S) :
    ∃ (W' : σ.Slot → R3) (h' : Simple W'),
      DeltaEquiv (link W hW) (link W' h') ∧ GenPos W' (insert b S) := by
  classical
  obtain ⟨ε, hε, hslide⟩ := hW.exists_slide b
  -- the bad positions for `c`
  let BA : Set R3 := ⋃ t : σ.Slot, {c | t ∈ S ∧ pr c = pr (W t)}
  let BB : Set R3 := ⋃ t : σ.Slot, ⋃ u : σ.Slot,
    {c | t ∈ S ∧ u ∈ S ∧ t ≠ u ∧ Coll (pr c) (pr (W t)) (pr (W u))}
  let BC : Set R3 := ⋃ x : σ.Slot, ⋃ e : σ.Slot, ⋃ f : σ.Slot,
    {c | (x ∈ S ∧ (x = nx b ∨ x = pv b) ∧ e ∈ S ∧ nx e ∈ S ∧ f ∈ S ∧ nx f ∈ S ∧ e ≠ f) ∧
      ∃ y ∈ pe W e, y ∈ pe W f ∧ y ∈ segment ℝ (pr c) (pr (W x))}
  let BD : Set R3 :=
    {c | c - W b ∈ Submodule.span ℝ {W (pv b) - W b, W (nx b) - W b}} ∪
      {c | c - W b ∈ Submodule.span ℝ {W (nx b) - W b, W (nx (nx b)) - W b}} ∪
      {c | c - W b ∈ Submodule.span ℝ {W (pv b) - W b, W (pv (pv b)) - W b}}
  have hBA : volume BA = 0 := by
    refine measure_iUnion_null fun t => ?_
    by_cases ht : t ∈ S
    · have hφ : (LinearMap.proj (R := ℝ) (φ := fun _ : Fin 3 => ℝ) 0) ≠ 0 := by
        intro h
        have := LinearMap.congr_fun h (Pi.single 0 1)
        simp at this
      refine measure_mono_null (fun c hc => ?_) (volume_kernel_null (W t) hφ)
      have := congrArg Prod.fst hc.2
      simp only [pr_apply] at this
      simp [this]
    · exact measure_mono_null (fun c hc => absurd hc.1 ht) measure_empty
  have hBB : volume BB = 0 := by
    refine measure_iUnion_null fun t => measure_iUnion_null fun u => ?_
    by_cases htu : t ∈ S ∧ u ∈ S ∧ t ≠ u
    · exact measure_mono_null (fun c hc => hc.2.2.2.rot)
        (volume_coll_null (hG.inj t htu.1 u htu.2.1 htu.2.2))
    · exact measure_mono_null (fun c hc => absurd ⟨hc.1, hc.2.1, hc.2.2.1⟩ htu) measure_empty
  have hBC : volume BC = 0 := by
    refine measure_iUnion_null fun x => measure_iUnion_null fun e => measure_iUnion_null fun f => ?_
    by_cases hcond : x ∈ S ∧ (x = nx b ∨ x = pv b) ∧ e ∈ S ∧ nx e ∈ S ∧ f ∈ S ∧ nx f ∈ S ∧ e ≠ f
    · obtain ⟨hx, hxb, he, hne, hf, hnf, hef⟩ := hcond
      by_cases hK : ∃ p, p ∈ pe W e ∧ p ∈ pe W f
      · obtain ⟨p, hpe, hpf⟩ := hK
        have hpx : pr (W x) ≠ p := by
          intro h
          rcases hG.incident he hne hx (h ▸ hpe) with h1 | h1 <;>
            rcases hG.incident hf hnf hx (h ▸ hpf) with h2 | h2
          · exact hef (h1.symm.trans h2)
          · rcases hxb with hxb | hxb
            · have : f = b := nx_injective (h2.symm.trans hxb)
              exact hb (this ▸ hf)
            · have : nx e = b := by rw [← h1, hxb, nx_pv]
              exact hb (this ▸ hne)
          · rcases hxb with hxb | hxb
            · have : e = b := nx_injective (h1.symm.trans hxb)
              exact hb (this ▸ he)
            · have : nx f = b := by rw [← h2, hxb, nx_pv]
              exact hb (this ▸ hnf)
          · exact hef (nx_injective (h1.symm.trans h2))
        refine measure_mono_null (fun c hc => ?_) (volume_coll_null hpx)
        obtain ⟨-, y, hye, hyf, hyc⟩ := hc
        have hyp : y = p := hG.pe_inter_unique he hne hf hnf hef hye hyf hpe hpf
        rw [hyp] at hyc
        exact (coll_of_mem_segment hyc).rot
      · refine measure_mono_null (fun c hc => ?_) measure_empty
        obtain ⟨-, y, hye, hyf, -⟩ := hc
        exact absurd ⟨y, hye, hyf⟩ hK
    · exact measure_mono_null (fun c hc => absurd hc.1 hcond) measure_empty
  have hBD : volume BD = 0 :=
    measure_union_null (measure_union_null (volume_span_null _ _ _) (volume_span_null _ _ _))
      (volume_span_null _ _ _)
  obtain ⟨c, hc, hcB⟩ := exists_near_not_mem hε (B := BA ∪ BB ∪ BC ∪ BD)
    (measure_union_null (measure_union_null (measure_union_null hBA hBB) hBC) hBD)
  have hcA : ∀ t ∈ S, pr c ≠ pr (W t) := fun t ht h =>
    hcB (Or.inl (Or.inl (Or.inl (mem_iUnion.mpr ⟨t, ht, h⟩))))
  have hcB' : ∀ t ∈ S, ∀ u ∈ S, t ≠ u → ¬ Coll (pr c) (pr (W t)) (pr (W u)) := fun t ht u hu htu h =>
    hcB (Or.inl (Or.inl (Or.inr (mem_iUnion.mpr ⟨t, mem_iUnion.mpr ⟨u, ht, hu, htu, h⟩⟩))))
  have hcC : ∀ x e f, x ∈ S → (x = nx b ∨ x = pv b) → e ∈ S → nx e ∈ S → f ∈ S → nx f ∈ S →
      e ≠ f → ∀ y ∈ pe W e, y ∈ pe W f → y ∈ segment ℝ (pr c) (pr (W x)) → False :=
    fun x e f hx hxb he hne hf hnf hef y hye hyf hyc =>
      hcB (Or.inl (Or.inr (mem_iUnion.mpr ⟨x, mem_iUnion.mpr ⟨e, mem_iUnion.mpr
        ⟨f, ⟨hx, hxb, he, hne, hf, hnf, hef⟩, y, hye, hyf, hyc⟩⟩⟩)))
  have hS1 : c - W b ∉ Submodule.span ℝ {W (pv b) - W b, W (nx b) - W b} := fun h =>
    hcB (Or.inr (Or.inl (Or.inl h)))
  have hS2 : c - W b ∉ Submodule.span ℝ {W (nx b) - W b, W (nx (nx b)) - W b} := fun h =>
    hcB (Or.inr (Or.inl (Or.inr h)))
  have hS3 : c - W b ∉ Submodule.span ℝ {W (pv b) - W b, W (pv (pv b)) - W b} := fun h =>
    hcB (Or.inr (Or.inr h))
  obtain ⟨h', hΔ⟩ := hslide c hc hS1 hS2 hS3
  refine ⟨Function.update W b c, h', hΔ, ?_⟩
  -- the new positions
  set W' := Function.update W b c with hW'
  have hW't : ∀ t, t ≠ b → W' t = W t := fun t ht => Function.update_of_ne ht _ _
  have hW'b : W' b = c := Function.update_self _ _ _
  have memS : ∀ t, t ∈ insert b S → t ≠ b → t ∈ S := fun t ht htb =>
    (mem_insert_iff.mp ht).resolve_left htb
  have hnxb : nx b ∈ S → True := fun _ => trivial
  -- old and new edges
  have old : ∀ e, e ∈ insert b S → nx e ∈ insert b S → e ≠ b → nx e ≠ b →
      e ∈ S ∧ nx e ∈ S ∧ pe W' e = pe W e := fun e he hne h1 h2 =>
    ⟨memS e he h1, memS _ hne h2, by simp only [pe, hW't e h1, hW't _ h2]⟩
  have new : ∀ e, e ∈ insert b S → nx e ∈ insert b S → ¬ (e ≠ b ∧ nx e ≠ b) →
      ∃ x, x ∈ S ∧ pe W' e = segment ℝ (pr c) (pr (W x)) ∧
        ((e = b ∧ x = nx b) ∨ (e = pv b ∧ x = pv b)) := by
    intro e he hne h
    by_cases h1 : e = b
    · refine ⟨nx b, memS _ (h1 ▸ hne) (h1 ▸ nx_ne b), ?_, Or.inl ⟨h1, rfl⟩⟩
      rw [h1]
      simp only [pe, hW'b, hW't _ (nx_ne b)]
    · have h2 : nx e = b := by
        by_contra h2; exact h ⟨h1, h2⟩
      have h3 : e = pv b := nx_eq_iff.mp h2
      refine ⟨pv b, h3 ▸ memS e he h1, ?_, Or.inr ⟨h3, rfl⟩⟩
      rw [h3]
      simp only [pe, nx_pv, hW'b, hW't _ (pv_ne b)]
      exact segment_symm ℝ _ _
  -- one new edge and two old ones
  have aux1 : ∀ e f g, e ∈ insert b S → nx e ∈ insert b S → ¬ (e ≠ b ∧ nx e ≠ b) →
      f ∈ insert b S → nx f ∈ insert b S → f ≠ b → nx f ≠ b →
      g ∈ insert b S → nx g ∈ insert b S → g ≠ b → nx g ≠ b → f ≠ g →
      ∀ y, y ∈ pe W' e → y ∈ pe W' f → y ∈ pe W' g → False := by
    intro e f g he hne hen hf hnf hf1 hf2 hg hng hg1 hg2 hfg y hye hyf hyg
    obtain ⟨x, hx, hpe, hxb⟩ := new e he hne hen
    obtain ⟨hfS, hnfS, hpf⟩ := old f hf hnf hf1 hf2
    obtain ⟨hgS, hngS, hpg⟩ := old g hg hng hg1 hg2
    rw [hpe] at hye
    rw [hpf] at hyf
    rw [hpg] at hyg
    refine hcC x f g hx ?_ hfS hnfS hgS hngS hfg y hyf hyg hye
    rcases hxb with ⟨-, h⟩ | ⟨-, h⟩
    · exact Or.inl h
    · exact Or.inr h
  -- two new edges and an old one
  have aux2 : ∀ e f g, e ∈ insert b S → nx e ∈ insert b S → ¬ (e ≠ b ∧ nx e ≠ b) →
      f ∈ insert b S → nx f ∈ insert b S → ¬ (f ≠ b ∧ nx f ≠ b) →
      g ∈ insert b S → nx g ∈ insert b S → g ≠ b → nx g ≠ b → e ≠ f →
      ∀ y, y ∈ pe W' e → y ∈ pe W' f → y ∈ pe W' g → False := by
    intro e f g he hne hen hf hnf hfn hg hng hg1 hg2 hef y hye hyf hyg
    obtain ⟨x, hx, hpe, hxb⟩ := new e he hne hen
    obtain ⟨x', hx', hpf, hxb'⟩ := new f hf hnf hfn
    obtain ⟨hgS, hngS, hpg⟩ := old g hg hng hg1 hg2
    have hxx : x ≠ x' := by
      rintro rfl
      rcases hxb with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> rcases hxb' with ⟨h3, h4⟩ | ⟨h3, h4⟩
      · exact hef (h1.trans h3.symm)
      · exact nx_ne_pv b (h2.symm.trans h4)
      · exact nx_ne_pv b (h4.symm.trans h2)
      · exact hef (h1.trans h3.symm)
    rw [hpe] at hye
    rw [hpf] at hyf
    rw [hpg] at hyg
    have hy := eq_of_mem_segment_of_not_coll (hcB' x hx x' hx' hxx) hye hyf
    rw [hy] at hyg
    exact hcB' g hgS (nx g) hngS (nx_ne g).symm (coll_of_mem_segment hyg).rot'
  refine ⟨?_, ?_, ?_⟩
  · intro t ht u hu htu
    by_cases htb : t = b
    · have hub : u ≠ b := fun h => htu (htb.trans h.symm)
      rw [htb, hW'b, hW't u hub]
      exact hcA u (memS u hu hub)
    · by_cases hub : u = b
      · rw [hub, hW'b, hW't t htb]
        exact (hcA t (memS t ht htb)).symm
      · rw [hW't t htb, hW't u hub]
        exact hG.inj t (memS t ht htb) u (memS u hu hub) htu
  · intro t ht u hu v hv htu htv huv
    by_cases htb : t = b
    · have hub : u ≠ b := fun h => htu (htb.trans h.symm)
      have hvb : v ≠ b := fun h => htv (htb.trans h.symm)
      rw [htb, hW'b, hW't u hub, hW't v hvb]
      exact hcB' u (memS u hu hub) v (memS v hv hvb) huv
    by_cases hub : u = b
    · have hvb : v ≠ b := fun h => huv (hub.trans h.symm)
      rw [hub, hW'b, hW't t htb, hW't v hvb]
      exact fun h => hcB' t (memS t ht htb) v (memS v hv hvb) htv h.swap₁₂
    by_cases hvb : v = b
    · rw [hvb, hW'b, hW't t htb, hW't u hub]
      exact fun h => hcB' t (memS t ht htb) u (memS u hu hub) htu h.rot'
    rw [hW't t htb, hW't u hub, hW't v hvb]
    exact hG.noncoll t (memS t ht htb) u (memS u hu hub) v (memS v hv hvb) htu htv huv
  · intro e f g he hne hf hnf hg hng hef heg hfg y hye hyf hyg
    by_cases oe : e ≠ b ∧ nx e ≠ b <;> by_cases of : f ≠ b ∧ nx f ≠ b <;>
      by_cases og : g ≠ b ∧ nx g ≠ b
    · obtain ⟨heS, hneS, hpe⟩ := old e he hne oe.1 oe.2
      obtain ⟨hfS, hnfS, hpf⟩ := old f hf hnf of.1 of.2
      obtain ⟨hgS, hngS, hpg⟩ := old g hg hng og.1 og.2
      rw [hpe] at hye
      rw [hpf] at hyf
      rw [hpg] at hyg
      exact hG.notriple e f g heS hneS hfS hnfS hgS hngS hef heg hfg y hye hyf hyg
    · exact aux1 g e f hg hng og he hne oe.1 oe.2 hf hnf of.1 of.2 hef y hyg hye hyf
    · exact aux1 f e g hf hnf of he hne oe.1 oe.2 hg hng og.1 og.2 heg y hyf hye hyg
    · exact aux2 f g e hf hnf of hg hng og he hne oe.1 oe.2 hfg y hyf hyg hye
    · exact aux1 e f g he hne oe hf hnf of.1 of.2 hg hng og.1 og.2 hfg y hye hyf hyg
    · exact aux2 e g f he hne oe hg hng og hf hnf of.1 of.2 heg y hye hyg hyf
    · exact aux2 e f g he hne oe hf hnf of hg hng og.1 og.2 hef y hye hyf hyg
    · -- three new edges: impossible, there are only two
      obtain ⟨x, -, -, hxe⟩ := new e he hne oe
      obtain ⟨x', -, -, hxf⟩ := new f hf hnf of
      obtain ⟨x'', -, -, hxg⟩ := new g hg hng og
      rcases hxe with ⟨h1, -⟩ | ⟨h1, -⟩ <;> rcases hxf with ⟨h2, -⟩ | ⟨h2, -⟩ <;>
        rcases hxg with ⟨h3, -⟩ | ⟨h3, -⟩
      all_goals first
        | exact hef (h1.trans h2.symm)
        | exact heg (h1.trans h3.symm)
        | exact hfg (h2.trans h3.symm)

/-- **Every finite set of slots can be put in general position** by a Δ-equivalence. -/
theorem exists_genPos (hW : Simple W) (T : Finset σ.Slot) :
    ∃ (W' : σ.Slot → R3) (h' : Simple W'),
      DeltaEquiv (link W hW) (link W' h') ∧ GenPos W' ↑T := by
  classical
  induction T using Finset.induction_on with
  | empty => exact ⟨W, hW, Relation.EqvGen.refl _, by simpa using genPos_empty W⟩
  | @insert b T hb ih =>
    obtain ⟨W₁, h₁, hΔ₁, hG₁⟩ := ih
    obtain ⟨W₂, h₂, hΔ₂, hG₂⟩ := hG₁.exists_step h₁ (S := ↑T) (by exact_mod_cast hb)
    exact ⟨W₂, h₂, Relation.EqvGen.trans _ _ _ hΔ₁ hΔ₂, by rw [Finset.coe_insert]; exact hG₂⟩

end Shape

/-- **Stage 3 of issue #8902.** Every polygonal link in `ℝ³` is Δ-equivalent to a polygonal
link whose vertical projection is regular. -/
theorem PolygonalLink.exists_deltaEquiv_isRegularProj (L : PolygonalLink R3) :
    ∃ L' : PolygonalLink R3, DeltaEquiv L L' ∧ L'.IsRegularProj := by
  classical
  obtain ⟨W, h, hΔ, hG⟩ := Shape.exists_genPos L.simple_posOf (Finset.univ)
  rw [Finset.coe_univ] at hG
  exact ⟨_, (L.link_posOf ▸ hΔ :), hG.isRegularProj h⟩

end QOU.MathlibExt.PL
