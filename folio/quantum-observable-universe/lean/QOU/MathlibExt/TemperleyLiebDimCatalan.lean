/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.JimboActionKernel
import QOU.MathlibExt.TemperleyLiebNormalFormSpanning

/-!
# `dim TL_{m+1}(q + q⁻¹) = catalan (m+1)`

This file proves the lower bound `finrank TL ≥ catalan (m+1)`. Combined with
`TemperleyLiebNormalFormSpanning.finrank_le_catalan`, it gives the dimension of the
Temperley–Lieb algebra exactly. The Jones normal forms `NormalIdx.elt` are then a basis.

## Route

1. **A representation of `TL_{m+1}(δ)` on `V^{⊗(m+1)}`, `dim V = 2`, with `δ = q + qi`
   and `q·qi = 1`.** The generator `e_a` acts as the local matrix
   `P := q·1 − Ř` placed at sites `a, a+1`. Here `Ř` is the `sl₂` R-matrix
   `RMatrix.rCheck`, the same matrix the corpus's Jimbo action `heckeActionN` uses.
   * `P² = (q + qi)·P` is a `4 × 4` identity.
   * `P₁P₂P₁ = P₁` and `P₂P₁P₂ = P₂` are `8 × 8` identities. They are transported to
     every adjacent pair of sites by the corpus's three-site embedding
     (`embedPair_eq_embedTriple_left/right`, `embedTriple_mul`), the same way the
     corpus proves `braidAt_braid`.
   * Far commutation is `embedPair_commute`.

   The representation is built over **any commutative ring** with `q·qi = 1`.
2. **Its image contains the image of the Jimbo action**, because
   `Ř = q·1 − P` (`jimbo_mem_range_tlRep`).
3. **Over `ℝ` at generic `q`, that image has dimension `catalan (m+1)`.** This is
   `JimboActionKernel.finrank_range_jimbo_eq_catalan`. So `finrank TL ≥ catalan (m+1)`.

Step 1 makes the Temperley–Lieb relator act by zero directly, by an explicit matrix
identity. No appeal to the trace radical is needed for that step. The trace radical
enters only through the cited dimension of the Jimbo image.
-/

namespace QOU.MathlibExt.TemperleyLiebDimCatalan

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebNormalForm
open QOU.MathlibExt.TemperleyLiebNormalIdxCatalan (card_normalIdx)
open QOU.MathlibExt.TemperleyLiebNormalFormSpanning (span_range_elt_eq_top finrank_le_catalan)
open QOU.SchurWeyl QOU.SchurWeyl.JimboActionKernel

/-! ## Local matrices -/

section Local

variable {R : Type*} [CommRing R] (q qi : R)

/-- The local Temperley–Lieb generator `P = q·1 − Ř` on `V ⊗ V`. -/
def tlLoc : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R :=
  Matrix.of fun a b => (if a = b then q else 0) - rCheck q qi a b

/-- `P ⊗ 1` on `V^{⊗3}`. -/
def tl1 : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun u v => tlLoc q qi (u.1, u.2.1) (v.1, v.2.1) * (if u.2.2 = v.2.2 then 1 else 0)

/-- `1 ⊗ P` on `V^{⊗3}`. -/
def tl2 : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun u v => (if u.1 = v.1 then 1 else 0) * tlLoc q qi (u.2.1, u.2.2) (v.2.1, v.2.2)

variable {q qi}

/-- **Loop relation, locally:** `P² = (q + qi)·P`. -/
theorem tlLoc_sq (hqi : q * qi = 1) : tlLoc q qi * tlLoc q qi = (q + qi) • tlLoc q qi := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [tlLoc, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Prod.ext_iff]
  all_goals linear_combination (-1 : R) * hqi

set_option maxHeartbeats 4000000 in
/-- **Temperley–Lieb relation, locally:** `P₁P₂P₁ = P₁` on `V^{⊗3}`. -/
theorem tl121 (hqi : q * qi = 1) : tl1 q qi * tl2 q qi * tl1 q qi = tl1 q qi := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [tl1, tl2, tlLoc, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff]
  all_goals first
    | linear_combination hqi
    | linear_combination q * hqi
    | linear_combination qi * hqi

set_option maxHeartbeats 4000000 in
/-- **Temperley–Lieb relation, locally:** `P₂P₁P₂ = P₂` on `V^{⊗3}`. -/
theorem tl212 (hqi : q * qi = 1) : tl2 q qi * tl1 q qi * tl2 q qi = tl2 q qi := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [tl1, tl2, tlLoc, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff]
  all_goals first
    | linear_combination hqi
    | linear_combination q * hqi
    | linear_combination qi * hqi

/-- `Ř = q·1 − P`. -/
theorem rCheck_eq_tlLoc :
    rCheck q qi = algebraMap R _ q + (-1 : R) • tlLoc q qi := by
  ext a b
  simp only [tlLoc, Matrix.add_apply, Matrix.smul_apply, Matrix.of_apply,
    Matrix.algebraMap_matrix_apply, Algebra.algebraMap_self, RingHom.id_apply, smul_eq_mul]
  ring

end Local

/-! ## The representation of `TL_{m+1}(q + qi)` on `V^{⊗(m+1)}` -/

section Rep

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-- `P` at the sites `a, a+1` of `V^{⊗(m+1)}`. -/
def tlGen (a : Fin m) : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  embedPair a.castSucc a.succ (tlLoc q qi)

theorem cs_ne_succ (a : Fin m) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

variable {q qi}

theorem tlGen_sq (hqi : q * qi = 1) (a : Fin m) :
    tlGen q qi a * tlGen q qi a = algebraMap R _ (q + qi) * tlGen q qi a := by
  rw [tlGen, embedPair_mul (cs_ne_succ a), tlLoc_sq hqi, embedPair_smul, Algebra.smul_def]

/-- Both Temperley–Lieb relations for an adjacent pair `b = a + 1`. -/
theorem tlGen_adj (hqi : q * qi = 1) (a b : Fin m) (hab : a.val + 1 = b.val) :
    tlGen q qi a * tlGen q qi b * tlGen q qi a = tlGen q qi a ∧
      tlGen q qi b * tlGen q qi a * tlGen q qi b = tlGen q qi b := by
  have hij : a.castSucc ≠ a.succ := cs_ne_succ a
  have hik : a.castSucc ≠ b.succ := by simp [Fin.ext_iff]; omega
  have hjk : a.succ ≠ b.succ := by simp [Fin.ext_iff]; omega
  have hb : b.castSucc = a.succ := by simp [Fin.ext_iff]; omega
  have h1 : tlGen q qi a = embedTriple a.castSucc a.succ b.succ (tl1 q qi) :=
    embedPair_eq_embedTriple_left hik hjk _
  have h2 : tlGen q qi b = embedTriple a.castSucc a.succ b.succ (tl2 q qi) := by
    rw [tlGen, hb]
    exact embedPair_eq_embedTriple_right hij hik _
  rw [h1, h2, embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk,
    embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk, tl121 hqi, tl212 hqi]
  exact ⟨rfl, rfl⟩

theorem tlGen_comm (a b : Fin m) (h : ¬ adjFin a b) :
    tlGen q qi a * tlGen q qi b = tlGen q qi b * tlGen q qi a := by
  by_cases hab : a = b
  · subst hab; rfl
  · have hv : a.val ≠ b.val := fun hc => hab (Fin.ext hc)
    have h1 : ¬ (a.val + 1 = b.val) := fun hc => h (Or.inl hc)
    have h2 : ¬ (b.val + 1 = a.val) := fun hc => h (Or.inr hc)
    exact embedPair_commute (cs_ne_succ a) (cs_ne_succ b)
      (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega)
      (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) _ _

variable (q qi m)

/-- **The Temperley–Lieb representation** `TL_{m+1}(q + qi) → End(V^{⊗(m+1)})`, over any
commutative ring with `q·qi = 1`. -/
noncomputable def tlRep (hqi : q * qi = 1) :
    TLFin R (q + qi) m →ₐ[R] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  lift R (q + qi) adjFin (tlGen q qi) (tlGen_sq hqi)
    (fun a b hab => by
      rcases hab with h | h
      · exact (tlGen_adj hqi a b h).1
      · exact (tlGen_adj hqi b a h).2)
    (fun a b h => tlGen_comm a b h)

variable {q qi m}

@[simp] theorem tlRep_e (hqi : q * qi = 1) (a : Fin m) :
    tlRep q qi m hqi (e R (q + qi) adjFin a) = tlGen q qi a :=
  lift_e _ _ _ _ _ _ _ _

/-- The braiding of strand `a` is `q − tlRep (e_a)`. -/
theorem strandBraid_eq (hqi : q * qi = 1) (a : Fin m) :
    strandBraid q qi a
      = tlRep q qi m hqi (algebraMap R _ q + (-1 : R) • e R (q + qi) adjFin a) := by
  rw [map_add, map_smul, AlgHom.commutes, tlRep_e, tlGen, strandBraid, braidAt,
    rCheck_eq_tlLoc, embedPair_add, embedPair_smul, embedPair_algebraMap (cs_ne_succ a)]

end Rep

/-! ## The image of the Jimbo action lies in the image of the TL representation -/

section Image

variable {K : Type*} [Field K]

theorem jimbo_mem_range_tlRep (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo q hq m x ∈ AlgHom.range (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq)) := by
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective K (HeckeRel K q q⁻¹ m) x
  let φ := (jimbo q hq m).comp (RingQuot.mkAlgHom K (HeckeRel K q q⁻¹ m))
  have hle : Algebra.adjoin K (Set.range (FreeAlgebra.ι K))
      ≤ (AlgHom.range (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq))).comap φ := by
    refine Algebra.adjoin_le ?_
    rintro _ ⟨i, rfl⟩
    show jimbo q hq m (Hecke.σ K q q⁻¹ m i)
      ∈ AlgHom.range (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq))
    rw [jimbo_σ, strandBraid_eq (mul_inv_cancel₀ hq)]
    exact ⟨_, rfl⟩
  rw [FreeAlgebra.adjoin_range_ι] at hle
  exact hle (Algebra.mem_top : y ∈ ⊤)

end Image

/-! ## The dimension -/

section Dimension

variable {R : Type*} [CommRing R]

/-- `TL_{m+1}(δ)` is a finite module over any commutative ring. -/
theorem finite_tlFin (δ : R) (m : ℕ) : Module.Finite R (TLFin R δ m) :=
  Module.finite_def.mpr
    (Submodule.fg_def.mpr ⟨_, Set.finite_range _, span_range_elt_eq_top δ m⟩)

/-- **The lower bound.** Over `ℝ` at a real `q ≠ 0` that is not a root of unity (and
`q²` is not one), `catalan (m+1) ≤ finrank TL_{m+1}(q + q⁻¹)`. -/
theorem catalan_le_finrank (q : ℝ) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) :
    catalan (m + 1) ≤ Module.finrank ℝ (TLFin ℝ (q + q⁻¹) m) := by
  haveI := finite_tlFin (q + q⁻¹) m
  rw [← finrank_range_jimbo_eq_catalan q hq hq2 hgen m]
  have hle : LinearMap.range (jimbo q hq m).toLinearMap
      ≤ LinearMap.range (tlRep q q⁻¹ m (mul_inv_cancel₀ hq)).toLinearMap := by
    rintro _ ⟨x, rfl⟩
    obtain ⟨y, hy⟩ := jimbo_mem_range_tlRep q hq m x
    exact ⟨y, hy⟩
  exact (Submodule.finrank_mono hle).trans (LinearMap.finrank_range_le _)

/-- **`dim TL_{m+1}(q + q⁻¹) = catalan (m+1)`**, over `ℝ`, at a real `q ≠ 0` that is not a
root of unity (and `q²` is not one). -/
theorem finrank_eq_catalan (q : ℝ) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) :
    Module.finrank ℝ (TLFin ℝ (q + q⁻¹) m) = catalan (m + 1) :=
  le_antisymm (finrank_le_catalan _ m) (catalan_le_finrank q hq hq2 hgen m)

/-- **The Jones normal forms are linearly independent** under the same hypotheses. -/
theorem linearIndependent_elt (q : ℝ) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) :
    LinearIndependent ℝ (NormalIdx.elt (m := m) (R := ℝ) (q + q⁻¹)) :=
  linearIndependent_of_top_le_span_of_card_eq_finrank
    (span_range_elt_eq_top (q + q⁻¹) m).ge
    (by rw [card_normalIdx, finrank_eq_catalan q hq hq2 hgen m])

/-- **The Jones normal forms are a basis of `TL_{m+1}(q + q⁻¹)`.** -/
noncomputable def normalBasis (q : ℝ) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) :
    Module.Basis (NormalIdx m) ℝ (TLFin ℝ (q + q⁻¹) m) :=
  Module.Basis.mk (linearIndependent_elt q hq hq2 hgen m) (span_range_elt_eq_top (q + q⁻¹) m).ge

@[simp] theorem normalBasis_apply (q : ℝ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (m : ℕ) (p : NormalIdx m) :
    normalBasis q hq hq2 hgen m p = NormalIdx.elt (q + q⁻¹) p :=
  Module.Basis.mk_apply _ _ _

end Dimension

end QOU.MathlibExt.TemperleyLiebDimCatalan
