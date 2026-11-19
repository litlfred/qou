import QOU.Infra.BorelRank
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.Tactic

/-!
# Borel partial resolution of the keystone sharpness target

Compiled formalisation of `prop:borel-partial-resolution`.

Proves:
1. Parity-independent rank `r₂` for totally imaginary fields (`r₁ = 0`), positivity
   `1 ≤ borelRankPredicted n r1 r2` whenever `1 ≤ r2`, and the explicit Bring-natural
   number field ranks (`ℚ(ζ₆)` rank `1`, `ℚ(ζ₅)` rank `2`, `ℚ(i)` rank `1`, `ℚ(√5)` ranks `2`/`0`).
2. Rational regulator lower bound: any injective `ℚ`-linear regulator `K_ind →ₗ[ℚ] V`
   whose image is contained in a finite-dimensional target subspace `W ≤ V` forces
   `Module.finrank ℚ K_ind ≤ Module.finrank ℚ W`.
3. Arithmetic parity unfolding `borel_partial`.
-/

namespace QOU.AppendixSurreals.BorelPartialResolution

open QOU.Infra.BorelRank

/-- Totally imaginary fields (`r₁ = 0`) have parity-independent Borel rank `r₂`. -/
theorem borelRankPredicted_totally_imaginary (n r2 : ℕ) :
    borelRankPredicted n 0 r2 = r2 := by
  unfold borelRankPredicted
  split_ifs <;> omega

/-- Whenever a number field has at least one complex conjugate pair (`1 ≤ r₂`),
    its Borel rank is at least `1` at every depth `n`. -/
theorem borelRankPredicted_pos_of_r2_pos (n r1 : ℕ) {r2 : ℕ} (hr2 : 1 ≤ r2) :
    1 ≤ borelRankPredicted n r1 r2 := by
  unfold borelRankPredicted
  split_ifs <;> omega

/-- Explicit Borel ranks for the Bring-natural number fields in Table 1:
    - `ℚ(ζ₆) = ℚ(√-3)` (`r₁ = 0, r₂ = 1`): rank `1` at every `n` (in particular `n = 2`),
    - `ℚ(ζ₅)` (`r₁ = 0, r₂ = 2`): rank `2` at every `n` (in particular `n = 2, 3`),
    - `ℚ(i)` (`r₁ = 0, r₂ = 1`): rank `1` at every `n`,
    - `ℚ(√5)` (`r₁ = 2, r₂ = 0`): rank `2` at even `n` (`n = 2`), rank `0` at odd `n` (`n = 3`). -/
theorem bring_natural_borel_ranks :
    borelRankPredicted 2 0 1 = 1 ∧
    borelRankPredicted 3 0 1 = 1 ∧
    borelRankPredicted 2 0 2 = 2 ∧
    borelRankPredicted 3 0 2 = 2 ∧
    cyclotomicBorelRank 5 3 = 2 ∧
    borelRankPredicted 2 2 0 = 2 ∧
    borelRankPredicted 3 2 0 = 0 := by
  unfold cyclotomicBorelRank borelRankPredicted
  decide

/-- Injectivity of the rationalised regulator `reg : K_ind →ₗ[ℚ] P` preserves `finrank`:
    `finrank ℚ (range reg) = finrank ℚ K_ind`. -/
theorem finrank_regulator_range_eq
    {K_ind P : Type*} [AddCommGroup K_ind] [Module ℚ K_ind]
    [AddCommGroup P] [Module ℚ P]
    (reg : K_ind →ₗ[ℚ] P) (hinj : Function.Injective reg) :
    Module.finrank ℚ (LinearMap.range reg) = Module.finrank ℚ K_ind :=
  (LinearEquiv.ofInjective reg hinj).symm.finrank_eq

/-- Borel lower bound on the archimedean period image `W ≤ P`: if `reg : K_ind →ₗ[ℚ] P`
    is injective with `range reg ≤ W` and `W` is finite-dimensional over `ℚ`, then
    `finrank ℚ K_ind ≤ finrank ℚ W`. -/
theorem borel_regulator_finrank_lower_bound
    {K_ind P : Type*} [AddCommGroup K_ind] [Module ℚ K_ind]
    [AddCommGroup P] [Module ℚ P]
    (reg : K_ind →ₗ[ℚ] P) (hinj : Function.Injective reg)
    (W : Submodule ℚ P) [FiniteDimensional ℚ W]
    (hsub : LinearMap.range reg ≤ W) :
    Module.finrank ℚ K_ind ≤ Module.finrank ℚ W := by
  rw [← finrank_regulator_range_eq reg hinj]
  exact Submodule.finrank_mono hsub

/-- **Definitional unfolding of `borelRankPredicted`** (`prop:borel-partial-resolution`,
    arithmetic core). `borelRankPredicted n r1 r2` evaluates to `r1 + r2` for even `n` and
    `r2` for odd `n`. -/
theorem borel_partial (n r1 r2 : ℕ) :
    borelRankPredicted n r1 r2 =
        (if n % 2 = 0 then r1 + r2 else r2) := by
  rfl

end QOU.AppendixSurreals.BorelPartialResolution
