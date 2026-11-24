import Mathlib.Data.Matrix.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# A weight-shifting insertion has zero sector trace; a weight-diagonal one reads its weight

This is the step of audit §28 that the probe measured and this file proves for every `q`.

Setting. A finite basis `ι` (for the six-strand space, the `2⁶` bit strings) carries a weight
`w : ι → W` (for audit §28, the pair of `u`-counts on the two blocks). The readout of an insertion
`X` on the sector `w = a` is `Σ_{w s = a} c s · (A * X) s s`, where `A` collects the sector
weight `c` (here `K^{⊗6}`), the nucleon cores and nothing that changes the weight.

* `sectorTrace_eq_zero_of_shift`: if `A` preserves the weight and `X` changes it on every
  nonzero entry (as `e_i f_j` and `f_i e_j` do across the two blocks), the readout is `0`.
* `sectorTrace_diag`: if `X` is diagonal with entries `f (w s)` (as `Σ_{i∈A, j∈B} h_i h_j`
  is, with `f (a, b) = (2T₃^A)(2T₃^B)`), the readout is `f a` times the readout of `1`.

Together they give the Gaudin pair shift `ΔE = T_X / T_1 = 2 T₃^A T₃^B` for the rational
`sl(2)` coupling on every sector, for every `q`, and for any weight-preserving core. Whether
the Jimbo core preserves the weight is the separate entrywise fact `jimbo_weight_preserving`
below: every nonzero entry of `Ř` keeps the number of `u` bits.
-/

namespace QOU.QBeta.WeightShift

open Matrix

variable {ι R W : Type*} [Fintype ι] [DecidableEq ι] [CommRing R] [DecidableEq W]

/-- Sector readout `Σ_{w s = a} c s · M s s`. -/
def sectorTrace (w : ι → W) (a : W) (c : ι → R) (M : Matrix ι ι R) : R :=
  ∑ s ∈ Finset.univ.filter (fun s => w s = a), c s * M s s

omit [DecidableEq ι] in
theorem diag_mul_eq_zero_of_shift (w : ι → W) (A X : Matrix ι ι R)
    (hA : ∀ s t, w s ≠ w t → A s t = 0) (hX : ∀ s t, w s = w t → X s t = 0) (s : ι) :
    (A * X) s s = 0 := by
  rw [Matrix.mul_apply]
  refine Finset.sum_eq_zero fun t _ => ?_
  by_cases h : w s = w t
  · rw [hX t s h.symm, mul_zero]
  · rw [hA s t h, zero_mul]

omit [DecidableEq ι] in
theorem sectorTrace_eq_zero_of_shift (w : ι → W) (a : W) (c : ι → R) (A X : Matrix ι ι R)
    (hA : ∀ s t, w s ≠ w t → A s t = 0) (hX : ∀ s t, w s = w t → X s t = 0) :
    sectorTrace w a c (A * X) = 0 := by
  unfold sectorTrace
  refine Finset.sum_eq_zero fun s _ => ?_
  rw [diag_mul_eq_zero_of_shift w A X hA hX s, mul_zero]

theorem sectorTrace_diag (w : ι → W) (a : W) (c : ι → R) (A : Matrix ι ι R) (f : W → R) :
    sectorTrace w a c (A * Matrix.diagonal (fun s => f (w s))) =
      f a * sectorTrace w a c A := by
  unfold sectorTrace
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun s hs => ?_
  rw [Finset.mem_filter] at hs
  rw [Matrix.mul_diagonal, hs.2]
  ring

omit [DecidableEq ι] in
theorem sectorTrace_add (w : ι → W) (a : W) (c : ι → R) (M N : Matrix ι ι R) :
    sectorTrace w a c (M + N) = sectorTrace w a c M + sectorTrace w a c N := by
  unfold sectorTrace
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun s _ => ?_
  simp only [Matrix.add_apply]
  ring

omit [DecidableEq ι] in
theorem sectorTrace_smul (w : ι → W) (a : W) (c : ι → R) (r : R) (M : Matrix ι ι R) :
    sectorTrace w a c (r • M) = r * sectorTrace w a c M := by
  unfold sectorTrace
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun s _ => ?_
  simp only [Matrix.smul_apply, smul_eq_mul]
  ring

/-- The rational Gaudin pair term `½·D + (E + F)`, with `D` weight-diagonal and `E`, `F`
weight-shifting, reads `½ f a` times the readout of the core. -/
theorem gaudin_readout (w : ι → W) (a : W) (c : ι → R) (A E F : Matrix ι ι R) (f : W → R)
    (half : R) (hA : ∀ s t, w s ≠ w t → A s t = 0)
    (hE : ∀ s t, w s = w t → E s t = 0) (hF : ∀ s t, w s = w t → F s t = 0) :
    sectorTrace w a c (A * (half • Matrix.diagonal (fun s => f (w s)) + (E + F))) =
      half * f a * sectorTrace w a c A := by
  rw [Matrix.mul_add, sectorTrace_add, Matrix.mul_add, sectorTrace_add,
    sectorTrace_eq_zero_of_shift w a c A E hA hE, sectorTrace_eq_zero_of_shift w a c A F hA hF,
    Matrix.mul_smul, sectorTrace_smul, sectorTrace_diag]
  ring

/-- The Jimbo braiding on two strands, `[[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]` on the
basis `00, 01, 10, 11`, over any commutative ring. -/
def jimbo (q h : R) : Fin 4 → Fin 4 → R := fun r c =>
  match r, c with
  | 0, 0 => q | 1, 2 => 1 | 2, 1 => 1 | 2, 2 => h | 3, 3 => q | _, _ => 0

/-- Number of `u` bits (zeros) in a two-strand basis state. -/
def uCount : Fin 4 → ℕ
  | 0 => 2 | 1 => 1 | 2 => 1 | 3 => 0

/-- Every nonzero entry of `Ř` keeps the number of `u` bits. -/
theorem jimbo_weight_preserving (q h : R) (r c : Fin 4) (hrc : uCount r ≠ uCount c) :
    jimbo q h r c = 0 := by
  fin_cases r <;> fin_cases c <;> simp_all [uCount, jimbo]

end QOU.QBeta.WeightShift
