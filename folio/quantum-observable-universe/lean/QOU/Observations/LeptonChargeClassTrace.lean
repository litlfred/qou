/-
# The electron's charge class in PSL(2, ℤ): even trace, and the least-trace pseudo-Anosov words

Thread "Derive the tau lepton's word", second part (2026-11-27). The owner reopened the
universality ruling (`e = Δ, μ = Δ³, τ = Δ⁵`) after it was found to be volume-blind (every central
step keeps the Nielsen–Thurston type), and asked to "work anosov". Audit:
`docs/audits/2026-11-27-tau-lepton-word.md` §Pseudo-Anosov.

`B₃ → SL(2, ℤ)` by `σ₀ ↦ [[1,1],[0,1]]`, `σ₁ ↦ [[1,0],[−1,1]]` (kernel `⟨Δ⁴⟩`; modulo the
centre this is `B₃/Z ≅ PSL(2, ℤ)`). A braid is periodic, reducible or pseudo-Anosov as `|tr|` is
`< 2`, `= 2` or `> 2`.

* `img_mod_two`: reduced mod 2 the image only sees the underlying permutation in `S₃`
  (`SL(2, 𝔽₂) ≅ S₃`).
* `trace_even_of_odd`: **every word of odd length** (the electron's charge class: two-component
  closure, `QOU.BraidKnot.ElectronWordCandidates.numCycles_permOf_of_odd`) **has even trace.**
  So the least-trace pseudo-Anosov `σ₀σ₁⁻¹` (trace 3, its square closes to `4₁`) is not in the
  charge class: it is neutral.
* The charge class ordered by `|tr|`: `Δ` (0, periodic; `trace_delta`), `σ₀` (2, reducible),
  `σ₀²σ₁⁻¹` (4; `trace_mu`), `σ₀⁴σ₁⁻¹` (6; `trace_tau`). `trace_V` records `σ₀σ₁⁻¹` at 3.

Uniqueness of the trace-4 and trace-6 classes and the closure-∪-axis volumes (5.33349, 6.35459;
two classes at trace 8) were measured with SnapPy on words up to length 9; they are not formalised.
This file proves the parity statement and the traces only. No measured value enters.

**Owner ruling 2026-11-27 23:35Z** (card "Least-trace ladder (pseudo-Anosov)", working conjecture):
`e = Δ`, `μ = σ₀²σ₁⁻¹`, `τ = σ₀⁴σ₁⁻¹`. The universality ladder `Δ, Δ³, Δ⁵`
(`QOU.Observations.LeptonUniversalityLadder`) and the other alternatives are kept as backups.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import QOU.BraidsAndKnots.ElectronWordCandidates

namespace QOU.Observations.LeptonChargeClassTrace

set_option linter.unusedSimpArgs false

open QOU.BraidKnot.ElectronWordCandidates

/-- The image of `σᵢ^{±1}` in `SL(2, ℤ)` (`true` = positive crossing). -/
def genZ : Fin 2 → Bool → Matrix (Fin 2) (Fin 2) ℤ
  | 0, true => !![1, 1; 0, 1]
  | 0, false => !![1, -1; 0, 1]
  | 1, true => !![1, 0; -1, 1]
  | 1, false => !![1, 0; 1, 1]

/-- The image of a signed braid word. -/
def imgZ : List (Fin 2 × Bool) → Matrix (Fin 2) (Fin 2) ℤ
  | [] => 1
  | (i, s) :: w => genZ i s * imgZ w

/-- The generators mod 2. -/
def gen2 : Fin 2 → Matrix (Fin 2) (Fin 2) (ZMod 2)
  | 0 => !![1, 1; 0, 1]
  | 1 => !![1, 0; 1, 1]

/-- `S₃ ≅ SL(2, 𝔽₂)`, matched to the generator tables of `ElectronWordCandidates`. -/
def mat2 : S3 → Matrix (Fin 2) (Fin 2) (ZMod 2)
  | .e => 1
  | .t01 => !![1, 1; 0, 1]
  | .t12 => !![1, 0; 1, 1]
  | .r => !![0, 1; 1, 1]
  | .r2 => !![1, 1; 1, 0]
  | .t02 => !![0, 1; 1, 0]

theorem mat2_gmul (i : Fin 2) (p : S3) : mat2 (S3.gmul i p) = gen2 i * mat2 p := by
  fin_cases i <;> cases p <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [mat2, gen2, S3.gmul, Matrix.mul_apply, Fin.sum_univ_two] <;> decide

theorem genZ_mod_two (i : Fin 2) (s : Bool) :
    (genZ i s).map (Int.castRingHom (ZMod 2)) = gen2 i := by
  fin_cases i <;> cases s <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [genZ, gen2] <;> decide

/-- **Mod 2 the image is the permutation.** -/
theorem img_mod_two (w : List (Fin 2 × Bool)) :
    (imgZ w).map (Int.castRingHom (ZMod 2)) = mat2 (permS (w.map Prod.fst)) := by
  induction w with
  | nil => simp [imgZ, permS, mat2, Matrix.map_one]
  | cons x w ih =>
    obtain ⟨i, s⟩ := x
    simp only [imgZ, List.map_cons, permS]
    rw [Matrix.map_mul, genZ_mod_two, ih, mat2_gmul]

theorem trace_mat2_odd : ∀ p ∈ S3.all, p.isOdd = true → Matrix.trace (mat2 p) = 0 := by
  intro p _ hp
  cases p <;> simp [S3.isOdd] at hp <;>
    simp [mat2, Matrix.trace_fin_two] <;> decide

/-- **Odd words have even trace in `SL(2, ℤ)`.** -/
theorem trace_even_of_odd (w : List (Fin 2 × Bool)) (hw : w.length % 2 = 1) :
    ((Matrix.trace (imgZ w) : ℤ) : ZMod 2) = 0 := by
  have h1 : ((Matrix.trace (imgZ w) : ℤ) : ZMod 2) =
      Matrix.trace ((imgZ w).map (Int.castRingHom (ZMod 2))) := by
    simp [Matrix.trace_fin_two]
  rw [h1, img_mod_two]
  apply trace_mat2_odd _ (mem_all _)
  rw [isOdd_permS]
  simp [hw]

/-- Hence no word of the charge class has trace `±3`, so none is conjugate to `σ₀σ₁⁻¹`. -/
theorem trace_ne_three_of_odd (w : List (Fin 2 × Bool)) (hw : w.length % 2 = 1) :
    Matrix.trace (imgZ w) ≠ 3 ∧ Matrix.trace (imgZ w) ≠ -3 := by
  have h := trace_even_of_odd w hw
  constructor <;> intro h3 <;> rw [h3] at h <;> revert h <;> decide

/-! ### The charge-class ladder by `|tr|` -/

/-- `Δ = σ₀σ₁σ₀`: trace 0 (periodic). -/
theorem trace_delta : Matrix.trace (imgZ [(0, true), (1, true), (0, true)]) = 0 := by
  simp [imgZ, genZ, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]

/-- `σ₀²σ₁⁻¹`: trace 4 (pseudo-Anosov). -/
theorem trace_mu : Matrix.trace (imgZ [(0, true), (0, true), (1, false)]) = 4 := by
  simp [imgZ, genZ, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]

/-- `σ₀⁴σ₁⁻¹`: trace 6 (pseudo-Anosov). -/
theorem trace_tau :
    Matrix.trace (imgZ [(0, true), (0, true), (0, true), (0, true), (1, false)]) = 6 := by
  simp [imgZ, genZ, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]

/-- `σ₀σ₁⁻¹` (the photon's chiral vertex): trace 3, the least pseudo-Anosov; even length. -/
theorem trace_V : Matrix.trace (imgZ [(0, true), (1, false)]) = 3 := by
  simp [imgZ, genZ, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]

end QOU.Observations.LeptonChargeClassTrace
