import QOU.MassTheory.WhiteheadBlochClass
import QOU.Transcendental.MassTheory.NahmRegulator
import QOU.Transcendental.MassTheory.CatalanClausenBridge
import QOU.Transcendental.MassTheory.WhiteheadVolumeCatalan

/-!
# The regulator of the Whitehead class is `4G = Vol(L5a1)`

`WhiteheadBloch.whiteheadClass i = 4[i]` lies in `B(ℂ)` (pre-Archimedean, proved there).
Under the Bloch–Wigner regulator,

  `D(4[i]) = 4 D(e^{iπ/2}) = 4 Cl₂(π/2) = 4G`,

which is the corpus's `WhiteheadVolume.vol_L5a1` (`regulator_whiteheadClass_eq_vol`).
So the Whitehead class is a nonzero element of `B(ℂ)`, with no `⊗ ℚ`. A single
evaluation of `D`, no limit, no `[Coev E]` instance, no numerical value.

The identification of `4[i]` with the class of the Whitehead complement uses the
octahedral decomposition, which is cited, not formalised.

-- Ref: [thurston1978] The geometry and topology of three-manifolds
-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-/

namespace QOU.Archimedean.WhiteheadRegulator

open Complex QOU.Archimedean QOU.Archimedean.NahmRegulator QOU.Archimedean.WhiteheadBloch
open QOU.Archimedean.FiveTermProof QOU.MathlibExt

noncomputable section

theorem I_eq_exp : I = exp ((Real.pi / 2 : ℝ) * I) := by
  rw [Complex.ofReal_div, Complex.ofReal_ofNat, Complex.exp_pi_div_two_mul_I]

/-- **The Whitehead regulator.** `D(4[i]) = 4·Cl₂(π/2)`. -/
theorem regulator_whiteheadClass :
    regulator (whiteheadClass I) = 4 * Cl_2 (Real.pi / 2) := by
  have h1 : I ≠ 1 := by
    intro h; have := congrArg Complex.im h; simp at this
  rw [whiteheadClass, map_nsmul, regulator_mk_gen Complex.I_ne_zero h1]
  conv_lhs => rw [I_eq_exp]
  rw [QOU.Archimedean.Cl2PentagonFromBlochWigner.blochD_exp]
  simp [nsmul_eq_mul]

/-- **`D(4[i]) = 4G = Vol(L5a1)`.** -/
theorem regulator_whiteheadClass_eq_vol :
    regulator (whiteheadClass I) = WhiteheadVolume.vol_L5a1 := by
  rw [regulator_whiteheadClass, WhiteheadVolume.vol_L5a1, catalan_G_eq_Cl_2_pi_div_two]

theorem whiteheadClass_I_mem_blochGroup :
    whiteheadClass I ∈ PreArchimedeanBloch.BlochGroup ℂ :=
  whiteheadClass_mem_blochGroup Complex.I_sq two_ne_zero

theorem regulator_whiteheadClass_pos : 0 < regulator (whiteheadClass I) := by
  rw [regulator_whiteheadClass_eq_vol]; exact WhiteheadVolume.vol_L5a1_pos

end

end QOU.Archimedean.WhiteheadRegulator
