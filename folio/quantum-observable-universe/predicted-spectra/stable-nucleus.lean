import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Torsion.StableNucleus — Nucleus extremizing the Skein binding Lagrangian

A stable nucleus N(p,n) = p𝔭 ⋈ n𝔫 where (p,n) satisfies
∂L_bind/∂p|_A = 0 (beta-stability line).

LaTeX label: `def:stable-nucleus`

## References
- [leitner2026] §3/stable-nucleus

**Ground ring**: `ℝ` (archimedean realisation). The beta-stability
condition is genuinely archimedean — it uses the strict order
(`a_A > 0`, the `|…| < 2` band) and the real power `A^{2/3}` (the
Coulomb-term scaling), neither of which is meaningful over the
Laurent `R_q` layer. So the structure lives past the
substrate→archimedean wall (§7c) and is stated over `ℝ` at the
evaluation `q ↦ q₀`.
-/

namespace QOU.Torsion

/-- A stable nucleus: multi-nucleon Hopf link on the beta-stability line. -/
-- Ref: [leitner2026] §3/stable-nucleus
structure StableNucleus where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Coulomb coefficient a_C = (q - q⁻¹) · λ_C (archimedean value). -/
  a_C : ℝ
  /-- Pauli asymmetry coefficient (archimedean value). -/
  a_A : ℝ
  /-- a_A is positive. -/
  a_A_pos : 0 < a_A
  /-- Mass number. -/
  A : ℕ := p + n
  /-- Beta-stability condition: p ≈ A / (2 + a_C·A^{2/3}/(2·a_A)). -/
  stability :
    |((p : ℝ) - (A : ℝ) / (2 + a_C * (A : ℝ) ^ (2 / 3 : ℝ) / (2 * a_A)))| < 2

end QOU.Torsion
