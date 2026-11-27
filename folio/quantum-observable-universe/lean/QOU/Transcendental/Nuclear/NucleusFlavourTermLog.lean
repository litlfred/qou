import QOU.Nuclear.NucleusFlavourTerm
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The `A`-nucleon flavour term with `ℓ = Real.log` (archimedean)

Behind the transcendental boundary (bean `qou-dk7p`): the generic results of
`QOU.Nuclear.NucleusFlavourTerm` hold for any logarithm-like map; this module instantiates
`ℓ = Real.log`, so the nucleon cell is `δ = 2E₀·log q`, the `K`-weight cell of ruling A.
-/

namespace QOU.Nuclear.NucleusFlavourTerm

open Matrix

/-- `Real.log` is logarithm-like. -/
theorem logLike_real_log : LogLike (Real.log : ℝ → ℝ) :=
  fun _ _ hx hy => Real.log_mul hx hy

/-- **One β step along an isobar, at any `A`, lowers the flavour mass by `2E₀·log q`.** -/
theorem flavourMass_beta_step_log {A : ℕ} {ι : Type*} [Fintype ι]
    (E₀ : ℝ) {q : ℝ} (hq : q ≠ 0) (W : Fin 2 → Matrix ι ι ℝ) (X : Fin A → Matrix ι ι ℝ)
    (hcell : ∀ i, (W 0 * X i).trace = q ^ 2 * (W 1 * X i).trace)
    (hn : ∀ i, (W 1 * X i).trace ≠ 0) (c c' : Fin A → Fin 2) (h : protons c' = protons c + 1) :
    flavourMass E₀ Real.log (tauNuc W c X) - flavourMass E₀ Real.log (tauNuc W c' X)
      = 2 * E₀ * Real.log q :=
  flavourMass_beta_step E₀ logLike_real_log hq W X hcell hn c c' h

end QOU.Nuclear.NucleusFlavourTerm
