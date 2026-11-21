import QOU.MathlibExt.CechNerveValues
import Mathlib.Analysis.Convex.PathConnected

/-!
# Realised simplicial complexes and their linear pieces (route R3, step S3a)

A finite simplicial complex with vertex type `V` and faces `F : Finset (Finset V)`
is realised as `PSpace F`: barycentric points of `ℝ^V` (nonnegative, summing to
`1`) whose support lies in one face. This generalises `Genus4.Space` (vertices
`Fin N`, faces listed by a function) to any finite vertex type, so that the
vertex set can grow under subdivision.

A **linear piece** `piece F S L` is the set of points whose `S`-coordinates are
positive and on which every linear form `ℓ ∈ L` (a coefficient vector) is
positive. It is **admissible** if every form has nonpositive coefficients
outside `S`. Open stars and their intersections are the pieces with `L = ∅`.

## Results, all sorry-free

* `piece_starConvex`, `piece_isPreconnected`: an admissible piece is star-convex
  about the renormalised restriction of any of its points to `S`, hence
  preconnected. (Restricting to `S` can only raise an admissible form.)
* `piece_inter`, `Admissible.union`: pieces are closed under intersection.
* `inter_nonempty_iff`: the stars of a nonempty vertex set `S` meet iff `S` lies
  in a face (the nerve of the star cover is the complex).
* `star`, `connFamily_star`, `stars_cover`: the open-star cover is a
  `ConnFamily` covering the space.

## What this does NOT do

It does not subdivide (`CechEdgeSubdiv`), compare covers, or say anything about a
particular surface; the identification of the genus-4 model with Bring's curve
is a citation, and `hχ` (Poincaré–Hopf) stays a hypothesis downstream.
Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S3/S4
-/
open Topology TopologicalSpace

set_option linter.unusedSectionVars false

namespace QOU.CentralExtension.Cech.PL

variable {V : Type} [Fintype V] [DecidableEq V] (F : Finset (Finset V))

/-- Geometric realisation inside the standard simplex of `ℝ^V`. -/
def Real4 : Set (V → ℝ) :=
  {p | (∀ i, 0 ≤ p i) ∧ ∑ i, p i = 1 ∧ ∃ f ∈ F, ∀ i, 0 < p i → i ∈ f}

/-- The realised complex. -/
abbrev PSpace := {p : V → ℝ // p ∈ Real4 F}

/-- Value of the linear form with coefficient vector `ℓ`. -/
def lf (ℓ p : V → ℝ) : ℝ := ∑ w, ℓ w * p w

/-- A **linear piece** of the ambient simplex. -/
def pieceA (S : Finset V) (L : Set (V → ℝ)) : Set (V → ℝ) :=
  {p | p ∈ Real4 F ∧ (∀ v ∈ S, 0 < p v) ∧ ∀ ℓ ∈ L, 0 < lf ℓ p}

/-- A **linear piece** of the realised complex. -/
def piece (S : Finset V) (L : Set (V → ℝ)) : Set (PSpace F) :=
  {x | (∀ v ∈ S, 0 < x.1 v) ∧ ∀ ℓ ∈ L, 0 < lf ℓ x.1}

/-- Every form has nonpositive coefficients outside `S`. -/
def Admissible (S : Finset V) (L : Set (V → ℝ)) : Prop := ∀ ℓ ∈ L, ∀ w ∉ S, ℓ w ≤ 0

theorem Admissible.union {S S' : Finset V} {L L' : Set (V → ℝ)} (h : Admissible S L)
    (h' : Admissible S' L') : Admissible (S ∪ S') (L ∪ L') := by
  rintro ℓ (hℓ | hℓ) w hw
  · exact h ℓ hℓ w fun hS => hw (Finset.mem_union_left _ hS)
  · exact h' ℓ hℓ w fun hS => hw (Finset.mem_union_right _ hS)

theorem admissible_empty (S : Finset V) : Admissible S (∅ : Set (V → ℝ)) := fun _ h => h.elim

theorem piece_inter (S S' : Finset V) (L L' : Set (V → ℝ)) :
    piece F S L ∩ piece F S' L' = piece F (S ∪ S') (L ∪ L') := by
  ext x
  simp only [piece, Set.mem_inter_iff, Set.mem_setOf_eq, Finset.mem_union, Set.mem_union]
  constructor
  · rintro ⟨⟨h1, h2⟩, h3, h4⟩
    exact ⟨fun v hv => hv.elim (h1 v) (h3 v), fun ℓ hℓ => hℓ.elim (h2 ℓ) (h4 ℓ)⟩
  · rintro ⟨h1, h2⟩
    exact ⟨⟨fun v hv => h1 v (Or.inl hv), fun ℓ hℓ => h2 ℓ (Or.inl hℓ)⟩,
      fun v hv => h1 v (Or.inr hv), fun ℓ hℓ => h2 ℓ (Or.inr hℓ)⟩

theorem piece_image (S : Finset V) (L : Set (V → ℝ)) :
    Subtype.val '' piece F S L = pieceA F S L := by
  ext p; constructor
  · rintro ⟨x, hx, rfl⟩; exact ⟨x.2, hx⟩
  · rintro ⟨hp, hS⟩; exact ⟨⟨p, hp⟩, hS, rfl⟩

/-- The renormalised restriction of `p` to `S`. -/
noncomputable def proj (S : Finset V) (p : V → ℝ) : V → ℝ :=
  fun w => if w ∈ S then p w / ∑ u ∈ S, p u else 0

theorem lf_proj (S : Finset V) (ℓ p : V → ℝ) :
    lf ℓ (proj S p) = (∑ w ∈ S, ℓ w * p w) / ∑ u ∈ S, p u := by
  unfold lf proj
  simp only [mul_ite, mul_zero]
  rw [Finset.sum_ite_mem, Finset.univ_inter, div_eq_mul_inv, Finset.sum_mul]
  refine Finset.sum_congr rfl fun w _ => ?_
  ring

theorem lf_split (S : Finset V) (ℓ p : V → ℝ) :
    lf ℓ p = ∑ w ∈ S, ℓ w * p w + ∑ w ∈ Finset.univ.filter (· ∉ S), ℓ w * p w := by
  unfold lf
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (· ∈ S)]
  congr 1
  rw [Finset.filter_mem_eq_inter, Finset.univ_inter]

theorem proj_mem {S : Finset V} {L : Set (V → ℝ)} (hS : S.Nonempty) (hL : Admissible S L)
    {p : V → ℝ} (hp : p ∈ pieceA F S L) : proj S p ∈ pieceA F S L := by
  obtain ⟨⟨hp0, hp1, f, hf, hpf⟩, hpS, hpL⟩ := hp
  have hs : 0 < ∑ u ∈ S, p u := Finset.sum_pos (fun u hu => hpS u hu) hS
  refine ⟨⟨fun i => ?_, ?_, f, hf, fun i hi => ?_⟩, fun v hv => ?_, fun ℓ hℓ => ?_⟩
  · unfold proj; split_ifs
    · exact div_nonneg (hp0 i) hs.le
    · exact le_rfl
  · unfold proj
    simp_rw [div_eq_mul_inv]
    rw [Finset.sum_ite_mem, Finset.univ_inter, ← Finset.sum_mul, mul_inv_cancel₀ hs.ne']
  · unfold proj at hi
    split_ifs at hi with h
    · exact hpf i (hpS i h)
    · exact (lt_irrefl _ hi).elim
  · simp only [proj, if_pos hv]; exact div_pos (hpS v hv) hs
  · rw [lf_proj]
    apply div_pos _ hs
    have h1 := hpL ℓ hℓ
    rw [lf_split S] at h1
    have h2 : ∑ w ∈ Finset.univ.filter (· ∉ S), ℓ w * p w ≤ 0 :=
      Finset.sum_nonpos fun w hw => mul_nonpos_of_nonpos_of_nonneg
        (hL ℓ hℓ w (Finset.mem_filter.1 hw).2) (hp0 w)
    linarith

theorem proj_pos_mem {S : Finset V} {p : V → ℝ} {w : V} (h : 0 < proj S p w) : w ∈ S := by
  by_contra hw; simp [proj, hw] at h

/-- An admissible piece is star-convex about the restriction of any of its points. -/
theorem piece_starConvex {S : Finset V} {L : Set (V → ℝ)}
    {c : V → ℝ} (hc : c ∈ pieceA F S L) (hcS : ∀ w, 0 < c w → w ∈ S) :
    StarConvex ℝ c (pieceA F S L) := by
  obtain ⟨⟨hc0, hc1, -, -, -⟩, hcpos, hcL⟩ := hc
  intro p ⟨⟨hp0, hp1, g, hg, hpg⟩, hpS, hpL⟩ a b ha hb hab
  have hlin : ∀ ℓ : V → ℝ, lf ℓ (a • c + b • p) = a * lf ℓ c + b * lf ℓ p := by
    intro ℓ; unfold lf
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, mul_add, Finset.sum_add_distrib,
      Finset.mul_sum]
    congr 1 <;> exact Finset.sum_congr rfl fun _ _ => by ring
  have hpos : ∀ x y : ℝ, 0 < x → 0 < y → 0 < a * x + b * y := by
    intro x y hx hy
    rcases ha.eq_or_lt with h | h
    · subst h; have : b = 1 := by linarith
      subst this; simpa using hy
    · exact add_pos_of_pos_of_nonneg (mul_pos h hx) (mul_nonneg hb hy.le)
  refine ⟨⟨fun i => ?_, ?_, g, hg, fun i hi => ?_⟩, fun v hv => ?_, fun ℓ hℓ => ?_⟩
  · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    exact add_nonneg (mul_nonneg ha (hc0 i)) (mul_nonneg hb (hp0 i))
  · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, hc1, hp1]; linarith
  · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul] at hi
    by_cases hu : 0 < c i
    · exact hpg i (hpS i (hcS i hu))
    · by_cases hpi : 0 < p i
      · exact hpg i hpi
      · exfalso
        have h1 : c i = 0 := le_antisymm (not_lt.mp hu) (hc0 i)
        have h2 : p i = 0 := le_antisymm (not_lt.mp hpi) (hp0 i)
        rw [h1, h2] at hi; simp at hi
  · simpa only [Pi.add_apply, Pi.smul_apply, smul_eq_mul] using hpos _ _ (hcpos v hv) (hpS v hv)
  · rw [hlin]; exact hpos _ _ (hcL ℓ hℓ) (hpL ℓ hℓ)

theorem pieceA_isPreconnected {S : Finset V} {L : Set (V → ℝ)} (hS : S.Nonempty)
    (hL : Admissible S L) : IsPreconnected (pieceA F S L) := by
  rcases (pieceA F S L).eq_empty_or_nonempty with h | ⟨p, hp⟩
  · rw [h]; exact isPreconnected_empty
  · exact ((piece_starConvex F (proj_mem F hS hL hp) fun w h => proj_pos_mem h).isPathConnected
      (proj_mem F hS hL hp)).isConnected.isPreconnected

/-- **Admissible pieces are preconnected.** -/
theorem piece_isPreconnected {S : Finset V} {L : Set (V → ℝ)} (hS : S.Nonempty)
    (hL : Admissible S L) : IsPreconnected (piece F S L) := by
  rw [← Topology.IsInducing.subtypeVal.isPreconnected_image, piece_image]
  exact pieceA_isPreconnected F hS hL

/-! ### Stars -/

noncomputable def unif (S : Finset V) : V → ℝ :=
  fun v => if v ∈ S then ((S.card : ℝ))⁻¹ else 0

theorem unif_sum {S : Finset V} (hS : S.Nonempty) : ∑ v, unif S v = 1 := by
  unfold unif
  rw [Finset.sum_ite_mem, Finset.univ_inter, Finset.sum_const, nsmul_eq_mul]
  have : (S.card : ℝ) ≠ 0 := by exact_mod_cast hS.card_pos.ne'
  field_simp

theorem unif_pos {S : Finset V} {v : V} (hv : v ∈ S) : 0 < unif S v := by
  have : 0 < (S.card : ℝ) := by exact_mod_cast Finset.card_pos.mpr ⟨v, hv⟩
  simp [unif, hv, this]

theorem unif_nonneg (S : Finset V) (v : V) : 0 ≤ unif S v := by
  unfold unif; split_ifs <;> positivity

theorem unif_pos_mem {S : Finset V} {v : V} (h : 0 < unif S v) : v ∈ S := by
  by_contra hv; simp [unif, hv] at h

theorem unif_mem {S : Finset V} (hS : S.Nonempty) {f : Finset V} (hf : f ∈ F) (hSf : S ⊆ f) :
    unif S ∈ Real4 F :=
  ⟨unif_nonneg S, unif_sum hS, f, hf, fun _ hi => hSf (unif_pos_mem hi)⟩

/-- Nerve: the stars of `S` meet iff `S` lies in a face. -/
theorem inter_nonempty_iff {S : Finset V} (hS : S.Nonempty) :
    (piece F S ∅).Nonempty ↔ ∃ f ∈ F, S ⊆ f := by
  constructor
  · rintro ⟨x, hx, -⟩
    obtain ⟨-, -, f, hf, hpf⟩ := x.2
    exact ⟨f, hf, fun v hv => hpf v (hx v hv)⟩
  · rintro ⟨f, hf, hSf⟩
    exact ⟨⟨unif S, unif_mem F hS hf hSf⟩, fun v hv => unif_pos hv, fun _ h => h.elim⟩

/-- The open star of a vertex. -/
def star (v : V) : Opens (PSpace F) :=
  ⟨{x | 0 < x.1 v}, isOpen_lt continuous_const ((continuous_apply v).comp continuous_subtype_val)⟩

theorem mem_star {v : V} {x : PSpace F} : x ∈ star F v ↔ 0 < x.1 v := Iff.rfl

theorem stars_cover (x : PSpace F) : ∃ v, x ∈ star F v := by
  by_contra h; push_neg at h
  have : ∑ i, x.1 i ≤ 0 := Finset.sum_nonpos fun i _ => not_lt.mp (h i)
  rw [x.2.2.1] at this; linarith

theorem star_inter2 (i j : V) :
    ((star F i ⊓ star F j : Opens (PSpace F)) : Set (PSpace F)) = piece F {i, j} ∅ := by
  ext x; simp [star, piece]

theorem star_inter3 (i j k : V) :
    ((star F i ⊓ star F j ⊓ star F k : Opens (PSpace F)) : Set (PSpace F)) =
      piece F {i, j, k} ∅ := by
  ext x; simp [star, piece, and_assoc]

theorem star_inter4 (i j k l : V) :
    ((star F i ⊓ star F j ⊓ star F k ⊓ star F l : Opens (PSpace F)) : Set (PSpace F)) =
      piece F {i, j, k, l} ∅ := by
  ext x; simp [star, piece, and_assoc]

/-- **The open-star cover is a `ConnFamily`.** -/
theorem connFamily_star : ConnFamily (star F) where
  pre3 i j k := by
    rw [star_inter3]; exact piece_isPreconnected F (by simp) (admissible_empty _)
  pre2 i j := by
    rw [star_inter2]; exact piece_isPreconnected F (by simp) (admissible_empty _)

end QOU.CentralExtension.Cech.PL
