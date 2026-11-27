import QOU.StandardModel.IotaOddTrace

/-!
# The electron word in `H₃(q)`: a single phase on the trivial block

Electron `σ₀σ₁σ₀` (owner ruling: `σ₀σ₁σ₀ ∈ B₃`, Hopf closure). In the hook
representation its trace is `0`, so for any block weights `(w₃, w₂₁, w₁₁₁)`
its trace is `w₃·q³ + w₁₁₁·(−q⁻¹)³`. With `w₁₁₁ = 0` (convention D) it is
`w₃·q³`: one modulus times one power of `q`, the power being the writhe `3`.

The words used by the mass formula, Borromean `(σ₀σ₁⁻¹)³` and figure-eight
`(σ₀σ₁⁻¹)²`, have exponent sum `0`, so the `(1, 0, −1)` functional
`τ = χ_(3) − χ_(1³)` (the α_em functional) vanishes on them for every `q`.
-/

namespace QOU.AlphaEM.ElectronWord

open Matrix QOU.AlphaEM.IotaOdd

variable {K : Type*} [Field K]

/-- `σ₀σ₁σ₀`. -/
def electron : List Letter := [(0, true), (1, true), (0, true)]

/-- `(σ₀σ₁⁻¹)³`, the Borromean core. -/
def borromean : List Letter :=
  [(0, true), (1, false), (0, true), (1, false), (0, true), (1, false)]

/-- `(σ₀σ₁⁻¹)²`, the figure-eight knot. -/
def figureEight : List Letter := [(0, true), (1, false), (0, true), (1, false)]

theorem electron_hook_trace (q : K) (hq : q ≠ 0) :
    (hookWord q electron).trace = 0 := by
  simp [hookWord, electron, hookLetter, hookGen, Matrix.trace, Fin.sum_univ_two]
  field_simp
  ring

/-- **The electron's block trace is `w₃ q³ + w₁₁₁ (−q⁻¹)³`, whatever `w₂₁` is.** -/
theorem electron_block_trace (q : K) (hq : q ≠ 0) (w3 w21 w111 : K) :
    w3 * symWord q electron + w21 * (hookWord q electron).trace
      + w111 * altWord q electron = w3 * q ^ 3 + w111 * (-q⁻¹) ^ 3 := by
  rw [electron_hook_trace q hq]
  simp [symWord, altWord, electron, symLetter, altLetter]
  ring

/-- **α_em functional on the electron:** `τ(σ₀σ₁σ₀) = q³ + q⁻³`. -/
theorem electron_tau (q : K) :
    symWord q electron - altWord q electron = q ^ 3 + q⁻¹ ^ 3 := by
  simp [symWord, altWord, electron, symLetter, altLetter]
  ring

/-- **τ vanishes on the Borromean core** (exponent sum `0`). -/
theorem borromean_tau (q : K) (hq : q ≠ 0) :
    symWord q borromean - altWord q borromean = 0 := by
  simp [symWord, altWord, borromean, symLetter, altLetter]
  field_simp
  ring

/-- **τ vanishes on the figure-eight word** (exponent sum `0`). -/
theorem figureEight_tau (q : K) (hq : q ≠ 0) :
    symWord q figureEight - altWord q figureEight = 0 := by
  simp [symWord, altWord, figureEight, symLetter, altLetter]
  field_simp
  ring

end QOU.AlphaEM.ElectronWord
