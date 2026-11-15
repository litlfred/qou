/-
# The index and sign characters of `H(M, q²)` in the balanced (§7a) normalisation, and
# why `−σ⁻¹` is the image of no braid word

Bean `qou-wkcd` (epic `qou-qs0e`, blocks `qou-hlx7`). Owner decision 3 (2026-11-15):
the well-posedness step of `LeftLineDefinition.neg_flip_ne_braid_image` assumed that an
index character `σ_i ↦ q` exists. This file builds it, so that step is no longer cited.

## Infrastructure that was already there

`QOU.MathlibExt.IwahoriHecke` constructs `H(M, Q)` by generators and relations. It also
builds `indexRep` (`T_i ↦ Q`) and `signRep` (`T_i ↦ −1`) from the universal property.
`QOU.IwahoriHecke.Balanced` rescales to the §7a generators `σ_i = qi · T_i` at
`Q = q²`. This file composes the two.

## Proved here (generic `[CommRing R]`, then an ordered field for positivity)

* `index_sigma`: `χ_+(σ_i) = q`. `index_negCrossing`: `χ_+(σ_i⁻¹) = qi`.
* `sign_sigma`: `χ_−(σ_i) = −qi`. `sign_negCrossing`: `χ_−(σ_i⁻¹) = −q`.
  These are the two roots `q` and `−q⁻¹` of `(x − q)(x + qi) = 0`, realised as
  one-dimensional representations of the whole algebra, not of a single letter.
* `index_wordImage`: a braid word maps to the product of `q` over its positive letters
  and `qi` over its negative letters.
* `wordImage_ne_neg_negCrossing`: over an ordered field with `0 < q`, no braid word's
  image equals `−σ_j⁻¹`, the image of `σ_j` under the eigenline swap. No step is cited.
* `sign_cannot_separate`: the sign character does not give this result. It sends every
  word of even length to a positive value, and `−σ⁻¹` to `q > 0` as well. The index
  character is the one that separates.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [humphreys1990] §7.4 (index and sign representations of the Hecke algebra)
-/
import QOU.IwahoriHecke.BalancedGenerators
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.List

namespace QOU.QuarkState.BalancedIndex

open QOU.MathlibExt.IwahoriHecke QOU.MathlibExt.SkeinRelation QOU.IwahoriHecke.Balanced

section Generic

variable {R : Type*} [CommRing R] {B : Type*} {M : B → B → ℕ} {q qi : R}

/-- **The balanced index character** `σ_i ↦ q`. -/
noncomputable def indexChar (hM : ∀ i j, M i j = M j i) : BalancedHecke M q →ₐ[R] R :=
  indexRep R (q * q) M hM

/-- **The balanced sign character** `σ_i ↦ −qi`. -/
noncomputable def signChar (hM : ∀ i j, M i j = M j i) : BalancedHecke M q →ₐ[R] R :=
  signRep R (q * q) M hM

theorem index_sigma (hM : ∀ i j, M i j = M j i) (hqi : q * qi = 1) (i : B) :
    indexChar hM (sigma M q qi i) = q := by
  unfold indexChar sigma
  rw [map_mul, AlgHom.commutes, indexRep_T, Algebra.algebraMap_self, RingHom.id_apply,
    ← mul_assoc, mul_comm qi q, hqi, one_mul]

theorem sign_sigma (hM : ∀ i j, M i j = M j i) (i : B) :
    signChar hM (sigma M q qi i) = -qi := by
  unfold signChar sigma
  rw [map_mul, AlgHom.commutes, signRep_T, Algebra.algebraMap_self, RingHom.id_apply,
    mul_neg_one]

theorem index_negCrossing (hM : ∀ i j, M i j = M j i) (hqi : q * qi = 1) (i : B) :
    indexChar hM (negCrossing q qi (sigma M q qi i)) = qi := by
  unfold negCrossing
  rw [map_sub, index_sigma hM hqi, AlgHom.commutes, Algebra.algebraMap_self,
    RingHom.id_apply]
  ring

theorem sign_negCrossing (hM : ∀ i j, M i j = M j i) (i : B) :
    signChar hM (negCrossing q qi (sigma M q qi i)) = -q := by
  unfold negCrossing
  rw [map_sub, sign_sigma hM, AlgHom.commutes, Algebra.algebraMap_self, RingHom.id_apply]
  ring

/-- The image of a braid word: a list of (generator, sign) pairs, `true` = positive
crossing `σ_i`, `false` = negative crossing `σ_i⁻¹`. -/
noncomputable def letter (q qi : R) (p : B × Bool) : BalancedHecke M q :=
  if p.2 then sigma M q qi p.1 else negCrossing q qi (sigma M q qi p.1)

noncomputable def wordImage (q qi : R) (w : List (B × Bool)) : BalancedHecke M q :=
  (w.map (letter (M := M) q qi)).prod

/-- **A braid word maps to `q^{#pos} qi^{#neg}`** under the index character. -/
theorem index_wordImage (hM : ∀ i j, M i j = M j i) (hqi : q * qi = 1)
    (w : List (B × Bool)) :
    indexChar hM (wordImage (M := M) q qi w)
      = (w.map fun p => if p.2 then q else qi).prod := by
  induction w with
  | nil => simp [wordImage]
  | cons p t ih =>
    simp only [wordImage, List.map_cons, List.prod_cons, map_mul] at ih ⊢
    rw [ih]
    congr 1
    unfold letter
    split_ifs
    · exact index_sigma hM hqi p.1
    · exact index_negCrossing hM hqi p.1

/-- Under the sign character a braid word maps to a product of `−qi` and `−q`. -/
theorem sign_wordImage (hM : ∀ i j, M i j = M j i) (w : List (B × Bool)) :
    signChar hM (wordImage (M := M) q qi w)
      = (w.map fun p => if p.2 then -qi else -q).prod := by
  induction w with
  | nil => simp [wordImage]
  | cons p t ih =>
    simp only [wordImage, List.map_cons, List.prod_cons, map_mul] at ih ⊢
    rw [ih]
    congr 1
    unfold letter
    split_ifs
    · exact sign_sigma hM p.1
    · exact sign_negCrossing hM p.1

end Generic

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  {B : Type*} {M : B → B → ℕ} {q qi : K}

/-- **`−σ_j⁻¹` is the image of no braid word** (positive parameter). The index
character sends every braid word to a positive number and `−σ_j⁻¹` to `−qi < 0`. -/
theorem wordImage_ne_neg_negCrossing (hM : ∀ i j, M i j = M j i) (hqi : q * qi = 1)
    (hq : 0 < q) (w : List (B × Bool)) (j : B) :
    wordImage (M := M) q qi w ≠ -negCrossing q qi (sigma M q qi j) := by
  intro h
  have hqi_pos : 0 < qi := by
    have : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
    rw [this]; exact inv_pos.mpr hq
  have hpos : 0 < indexChar hM (wordImage (M := M) q qi w) := by
    rw [index_wordImage hM hqi]
    apply List.prod_pos
    intro x hx
    obtain ⟨p, -, rfl⟩ := List.mem_map.mp hx
    split_ifs
    · exact hq
    · exact hqi_pos
  rw [h, map_neg, index_negCrossing hM hqi] at hpos
  exact absurd hpos (not_lt.mpr (neg_nonpos.mpr hqi_pos.le))

/-- **The sign character cannot replace the index character.** The two-letter word
`σ_i σ_i` and `−σ_j⁻¹` both have positive sign value. -/
theorem sign_cannot_separate (hM : ∀ i j, M i j = M j i) (hqi : q * qi = 1) (hq : 0 < q)
    (i j : B) :
    0 < signChar hM (wordImage (M := M) q qi [(i, true), (i, true)]) ∧
      signChar hM (-negCrossing q qi (sigma M q qi j)) > 0 := by
  have hqi_pos : 0 < qi := by
    have : qi = q⁻¹ := eq_inv_of_mul_eq_one_right hqi
    rw [this]; exact inv_pos.mpr hq
  refine ⟨?_, ?_⟩
  · rw [sign_wordImage hM]
    simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, if_true, mul_one]
    exact mul_pos_of_neg_of_neg (neg_neg_of_pos hqi_pos) (neg_neg_of_pos hqi_pos)
  · rw [map_neg, sign_negCrossing hM]; simp; exact hq

end Ordered

end QOU.QuarkState.BalancedIndex
