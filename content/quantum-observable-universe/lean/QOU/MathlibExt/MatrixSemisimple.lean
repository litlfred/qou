import Mathlib.Data.Matrix.Action
import Mathlib.RingTheory.SimpleModule.Basic
import Mathlib.Tactic

/-!
# QOU.MathlibExt.MatrixSemisimple — matrix rings over a division ring are semisimple

Fills (the division-ring case of) Mathlib's `proof_wanted
IsSemisimpleRing.matrix` (`RingTheory/SimpleModule/Basic.lean`), the
gap blocking the Prop-level semisimplicity corollaries of the QOU
Wedderburn ladder (`HeckeH2Wedderburn`, `HeckeH3Wedderburn`).

Route (bean `qou-5mrn`):

1. **Transitivity** — over a division ring `K`, any nonzero vector
   reaches any vector under the `Matrix.mulVec` action
   (`exists_smul_eq`): the explicit matrix `w ⬝ (eᵢ (v i)⁻¹)ᵀ` does it.
2. **Column-module simplicity** — hence `n → K` is a simple
   `Matrix n n K`-module (`instIsSimpleModule_vec`).
3. **Column decomposition** — the regular module `Matrix n n K`
   decomposes `Matrix`-linearly into its columns
   (`columnsEquiv : Matrix n n K ≃ₗ[Matrix n n K] (n → (n → K))`).
4. **Assembly** — the coordinate submodules of the Pi module are
   simple with join `⊤`, so the Pi module is semisimple
   (`sSup_simples_eq_top_iff_isSemisimpleModule`), and the regular
   module inherits it along `columnsEquiv`
   (`IsSemisimpleModule.congr`): **`IsSemisimpleRing (Matrix n n K)`**.

The empty-index case is handled separately (the matrix ring is then a
subsingleton, whose submodule lattice is trivially complemented).

Upstream candidate: statements and names follow Mathlib conventions so
the content can be PR'd against the `proof_wanted` upstream.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.MathlibExt.MatrixSemisimple

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]
variable {K : Type*} [DivisionRing K]

/-- **Transitivity of the matrix action (sorry-free):** over a division
    ring, any nonzero vector reaches any vector. -/
theorem exists_smul_eq {v : n → K} (hv : v ≠ 0) (w : n → K) :
    ∃ A : Matrix n n K, A • v = w := by
  obtain ⟨i, hi⟩ : ∃ i, v i ≠ 0 := by
    by_contra h
    push_neg at h
    exact hv (funext h)
  refine ⟨Matrix.of fun a b => if b = i then w a * (v i)⁻¹ else 0, ?_⟩
  funext a
  simp only [smul_eq_mulVec, mulVec, dotProduct, Matrix.of_apply]
  rw [Finset.sum_eq_single i]
  · rw [if_pos rfl, mul_assoc, inv_mul_cancel₀ hi, mul_one]
  · intro b _ hb
    rw [if_neg hb, zero_mul]
  · intro h
    exact absurd (Finset.mem_univ i) h

/-- **The column module is simple (sorry-free):** `n → K` is a simple
    `Matrix n n K`-module for nonempty `n`. -/
instance instIsSimpleModule_vec [Nonempty n] :
    IsSimpleModule (Matrix n n K) (n → K) where
  exists_pair_ne := by
    refine ⟨⊥, ⊤, fun h => ?_⟩
    have h1 : (fun _ => (1 : K)) ∈ (⊤ : Submodule (Matrix n n K) (n → K)) :=
      Submodule.mem_top
    rw [← h, Submodule.mem_bot] at h1
    exact one_ne_zero (congrFun h1 (Classical.arbitrary n))
  eq_bot_or_eq_top N := by
    by_cases hN : N = ⊥
    · exact Or.inl hN
    · refine Or.inr ?_
      obtain ⟨v, hvN, hv⟩ := (Submodule.ne_bot_iff N).mp hN
      rw [Submodule.eq_top_iff']
      intro w
      obtain ⟨A, hA⟩ := exists_smul_eq hv w
      exact hA ▸ N.smul_mem A hvN

/-- **Column decomposition of the regular module (sorry-free):** the
    matrix ring, as a left module over itself, is the finite product of
    its columns. -/
def columnsEquiv :
    Matrix n n K ≃ₗ[Matrix n n K] (n → (n → K)) where
  toFun A := fun j i => A i j
  invFun c := Matrix.of fun i j => c j i
  left_inv A := rfl
  right_inv c := rfl
  map_add' A B := rfl
  map_smul' B A := by
    funext j i
    show (B * A) i j = (B • fun i => A i j) i
    simp only [smul_eq_mulVec, Matrix.mul_apply, mulVec, dotProduct]

/-- **Matrix rings over a division ring are semisimple (nonempty index,
    sorry-free)** — the core of Mathlib's `proof_wanted
    IsSemisimpleRing.matrix` in the division-ring case. -/
theorem isSemisimpleRing_of_nonempty [Nonempty n] :
    IsSemisimpleRing (Matrix n n K) := by
  have hPi : IsSemisimpleModule (Matrix n n K) (n → (n → K)) := by
    rw [← sSup_simples_eq_top_iff_isSemisimpleModule]
    rw [eq_top_iff]
    intro c _
    have hc : c = ∑ j, LinearMap.single (Matrix n n K) (fun _ => n → K) j (c j) := by
      funext i
      simp [LinearMap.single_apply, Finset.sum_apply, Pi.single_apply,
        Finset.sum_ite_eq, Finset.mem_univ]
    rw [hc]
    refine Submodule.sum_mem _ fun j _ => ?_
    refine Submodule.mem_sSup_of_mem (s := _) ?_
      (LinearMap.mem_range_self _ (c j))
    have hinj : Function.Injective
        (LinearMap.single (Matrix n n K) (fun _ : n => n → K) j) :=
      fun a b hab => by
        simpa [LinearMap.single_apply] using congrFun hab j
    exact IsSimpleModule.congr (LinearEquiv.ofInjective _ hinj).symm
  exact hPi.congr (columnsEquiv (n := n) (K := K))

/-- The empty-index matrix ring is a subsingleton, hence trivially
    semisimple (sorry-free). Note that this is intentionally trivial
    (the empty matrix ring is vacuously semisimple) and is needed as
    a base case. -/
theorem isSemisimpleRing_of_isEmpty [IsEmpty n] :
    IsSemisimpleRing (Matrix n n K) := by
  have hsub : Subsingleton (Matrix n n K) :=
    ⟨fun A B => by ext i j; exact (IsEmpty.false i).elim⟩
  have : Subsingleton (Submodule (Matrix n n K) (Matrix n n K)) :=
    ⟨fun P Q => by
      ext x
      rw [Subsingleton.elim x (0 : Matrix n n K)]
      simp⟩
  exact sSup_simples_eq_top_iff_isSemisimpleModule.mp (Subsingleton.elim _ _)

/-- **`IsSemisimpleRing (Matrix n n K)` over a division ring
    (sorry-free)** — Mathlib's `proof_wanted IsSemisimpleRing.matrix`,
    division-ring case, all index types. -/
instance instIsSemisimpleRing_matrix : IsSemisimpleRing (Matrix n n K) := by
  cases isEmpty_or_nonempty n with
  | inl h => exact isSemisimpleRing_of_isEmpty
  | inr h => exact isSemisimpleRing_of_nonempty

end QOU.MathlibExt.MatrixSemisimple
