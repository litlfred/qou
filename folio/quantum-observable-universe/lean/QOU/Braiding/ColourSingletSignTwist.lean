import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import QOU.BraidsAndKnots.FibreDimensionForcesTL

/-!
# Transported colour singlets see the sign-twisted trace (bean `qou-ni4b`)

**Setting.** `computations/probes/qcd_coideal_gl6_colour/RESULT.md` measured, exactly over
`ℚ(q, c)`, that the colour-singlet sector of a colour carried with the strand is the flavour model
twisted by the Hecke involution `# : σ ↦ −σ⁻¹`, and that its Markov parameter is
`z_D(−q⁻¹) = −1/(q(q²+1))`. Its argument at `q = 1` (the colour singlet `ε` is odd under `P_c`) is
written in prose, not Lean.

This file formalises the **trace-level half** of that argument at `n = 3`, over any commutative
ring, with no numerical input:

* `twist_moments` — if `(y₃, y₂₁, y₁₃)` are the Ocneanu weights of a Markov trace with parameter
  `z` (the three moment equations against the `H₃(q)` character table), then the transposed weights
  `(y₁₃, y₂₁, y₃)` satisfy the same equations with parameter `(q − q⁻¹) − z`. This is the trace
  `tr ∘ #` at the level of weights: `#` sends `σ` to `−σ⁻¹`, and `tr(−σ⁻¹) = h − z` with
  `h = q − q⁻¹` (Hecke relation), while `#(e_λ) = e_λ'`
  (`QOU.BraidKnot.CentralIdempotentInvolution.hashMap_centralIdem`, general `n`).
* `twist_param_of_conventionD` — convention D, `z·[2]_q = q²`, goes to `z'·[2]_q = −q⁻²`, i.e.
  `z' = −1/(q(q²+1))` when `q·q⁻¹ = 1`. That is the fermionic parameter the probe measured.
* `twist_symmetric_weight_eq_zero_of_conventionD` — under D the twisted trace has **zero weight on
  the symmetric block `(3)`**, the mirror image of D's zero on `(1³)`.

**Scope.** This is the trace side only. The representation-theoretic step "the transported
singlet sector *is* the `#`-twist of the flavour model" (sign of `ε` at `q = 1` plus constancy of
`H₃(q)` multiplicities on a Zariski-open set) is still the probe's prose argument. Owner ruling
2026-11-22 (D1 = 3) drops convention D as a colour test, so this file records what the colour
singlets carry; it does not test them against D.
-/

namespace QOU.Braiding.ColourSingletSignTwist

variable {R : Type*} [CommRing R]

/-- **The sign twist on the `n = 3` moment equations.** Transposing the Ocneanu weights and
replacing `z` by `(q − qi) − z` preserves all three equations. No relation `q·qi = 1` is needed. -/
theorem twist_moments (q qi z y₃ y₂₁ y₁₃ : R)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2) :
    y₁₃ + 2 * y₂₁ + y₃ = 1 ∧
    q * y₁₃ + (q - qi) * y₂₁ + (-qi) * y₃ = (q - qi) - z ∧
    q ^ 2 * y₁₃ + (-1) * y₂₁ + qi ^ 2 * y₃ = ((q - qi) - z) ^ 2 := by
  refine ⟨by linear_combination hnorm, ?_, ?_⟩
  · linear_combination (q - qi) * hnorm - hsigma
  · linear_combination (q - qi) ^ 2 * hnorm + hsigmasigma - 2 * (q - qi) * hsigma

/-- **Convention D goes to the fermionic parameter.** If `z·[2]_q = q²` then
`((q − qi) − z)·[2]_q = −qi²`, i.e. `z' = −1/(q(q²+1))` when `q·qi = 1`. -/
theorem twist_param_of_conventionD (q qi z : R) (hzD : z * (q + qi) = q ^ 2) :
    ((q - qi) - z) * (q + qi) = -qi ^ 2 := by
  linear_combination -hzD

/-- **Under convention D the twisted trace kills the symmetric block.** The twisted weight on
`(3)` is the original weight on `(1³)`, which convention D sends to zero
(`threeRow_eq_zero_of_jones_ocneanu`). So the colour-singlet trace sees `(2,1)` and `(1³)` and
not `(3)`. -/
theorem twist_symmetric_weight_eq_zero_of_conventionD [IsDomain R]
    (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hzD : z * (q + qi) = q ^ 2)
    (hb2ne : q + qi ≠ 0)
    (h3ne : (q + qi) ^ 2 - 1 ≠ 0) :
    -- the twisted weight vector is `(y₁₃, y₂₁, y₃)`; its `(3)` entry is `y₁₃`
    y₁₃ = 0 ∧ ((q - qi) - z) * (q + qi) = -qi ^ 2 :=
  ⟨QOU.BraidsAndKnots.threeRow_eq_zero_of_jones_ocneanu q qi z y₃ y₂₁ y₁₃ hqi hnorm hsigma
      hsigmasigma hzD hb2ne h3ne,
    twist_param_of_conventionD q qi z hzD⟩

end QOU.Braiding.ColourSingletSignTwist
