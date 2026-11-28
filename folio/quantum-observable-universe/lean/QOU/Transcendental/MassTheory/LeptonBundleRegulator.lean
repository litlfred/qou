import QOU.MassTheory.LeptonBundleNahm
import QOU.MassTheory.RaLDeterminant
import QOU.Transcendental.MassTheory.NahmRegulator

/-!
# The regulator of the lepton-bundle and `RᵃL` Bloch classes

Bean `qou-35a8`. The Nahm classes of the `R²L` (`μ`) and `R⁴L` (`τ`) bundles
(`LeptonBundleNahm`) and the Neumann–Zagier classes of the whole `RᵃL` family
(`NeumannZagierBloch`, `RaLSymplectic`, `RaLDeterminant`) are algebraic: they are
defined over any field of characteristic zero, and their membership in the Bloch
group is proved there with no analysis.

This file is where they meet a transcendental function. It evaluates them under the
Bloch–Wigner regulator `D : P(ℂ) →+ ℝ` (`NahmRegulator.regulator`, induced by the
proved five-term relation), and nothing else:

* `regulator_nahmClass`, `regulator_nzClass`: the regulator of a Nahm or
  Neumann–Zagier class is `∑ᵢ D(zᵢ)`, for any solution over `ℂ`.
* `regulator_muClass`: `D(1/2 + y) + 2·D(y)` at a root of `2y² − 3y + 2 = 0`.
* `regulator_tauClass`: `2·D(A(s)) + D(B(s)) + 2·D(s)` at a root of
  `s³ − 6s² + 8s − 4 = 0`, with `A(s) = 1/2 + s − s²/4`, `B(s) = 2s − s²`.
* `regulator_raClass`: for every `a ≥ 3`, the Bloch class `det B • Σ[z]` has
  regulator `det B · ∑ᵢ D(zᵢ)` with `det B ≠ 0`, `|det B| = 2(a − 2)`.

The regulator is a single evaluation, not a limit, so no `[Coev E]` instance is spent
here. No numerical volume and no empirical value appears; the comparison with a
volume belongs with a located cut of each `D(zᵢ)` and is not stated here.
-/

namespace QOU.Archimedean.LeptonBundleRegulator

open QOU.Archimedean.PreArchimedeanBloch QOU.Archimedean.NahmBlochBridge
open QOU.Archimedean.NeumannZagierBloch QOU.Archimedean.LeptonBundleNahm
open QOU.Archimedean.NahmRegulator QOU.Archimedean.FiveTermProof QOU.MathlibExt

noncomputable section

variable {ι : Type*} [Fintype ι]

/-- **The regulator of a Nahm class** is the sum of `D` over its shapes. -/
theorem regulator_nahmClass {A : Matrix ι ι ℤ} (s : NahmSolution ℂ ι A) :
    regulator (nahmClass s) = ∑ i, blochD (s.w i : ℂ) := by
  rw [nahmClass, nahmSum, QuotientAddGroup.mk_sum, map_sum]
  exact Finset.sum_congr rfl fun i _ => regulator_mk_gen (s.w i).ne_zero (s.ne_one i)

/-- **The regulator of a Neumann–Zagier class** is the sum of `D` over its shapes. -/
theorem regulator_nzClass {A B : Matrix ι ι ℤ} (s : NZSolution ℂ ι A B) :
    regulator (nzClass s) = ∑ i, blochD (s.w i : ℂ) := by
  rw [nzClass, nzSum, QuotientAddGroup.mk_sum, map_sum]
  refine Finset.sum_congr rfl fun i _ => regulator_mk_gen (s.w i).ne_zero ?_
  intro h
  have := (s.w' i).ne_zero
  rw [s.hw' i, h, sub_self] at this
  exact this rfl

/-- **The `μ` regulator.** -/
theorem regulator_muClass {y : ℂ} (hy : 2 * y ^ 2 - 3 * y + 2 = 0) :
    regulator (nahmClass (muSolution hy)) = blochD (1 / 2 + y) + 2 * blochD y := by
  rw [regulator_nahmClass, Fin.sum_univ_three]
  simp [muSolution, mkU]
  ring

/-- **The `τ` regulator.** -/
theorem regulator_tauClass {s : ℂ} (hs : s ^ 3 - 6 * s ^ 2 + 8 * s - 4 = 0) :
    regulator (nahmClass (tauSolution hs)) =
      2 * blochD (tauA s) + blochD (tauB s) + 2 * blochD s := by
  rw [regulator_nahmClass, Fin.sum_univ_five]
  simp [tauSolution, mkU]
  ring

/-- **The `RᵃL` regulator**, every `a ≥ 3`: the Bloch class `det B • Σ[z]` has
regulator `det B · ∑ᵢ D(zᵢ)`, and `det B ≠ 0`. -/
theorem regulator_raClass {a : ℕ} (h3 : 3 ≤ a)
    (s : NZSolution ℂ (Fin (a + 1)) (NeumannZagierBloch.raA a) (NeumannZagierBloch.raB a)) :
    regulator ((NeumannZagierBloch.raB a).det • nzClass s) =
        ((NeumannZagierBloch.raB a).det : ℝ) * ∑ i, blochD (s.w i : ℂ) ∧
      (NeumannZagierBloch.raB a).det ≠ 0 := by
  refine ⟨?_, RaLDeterminant.raB_det_ne_zero h3⟩
  rw [map_zsmul, regulator_nzClass, zsmul_eq_mul]

end

end QOU.Archimedean.LeptonBundleRegulator
