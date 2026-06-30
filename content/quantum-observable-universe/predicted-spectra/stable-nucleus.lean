import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Torsion.StableNucleus — Nucleus extremizing the Skein binding Lagrangian

A stable nucleus N(p,n) = p𝔭 ⋈ n𝔫 where (p,n) satisfies
∂L_bind/∂p|_A = 0 (beta-stability line).

LaTeX label: `def:stable-nucleus`

## References
- [manuscript] §3/stable-nucleus

**Ground ring.** The combinatorial data (p, n, A) is integer; the
beta-stability condition is the **archimedean realisation** (§7c) over
`ℝ` — it uses division, the real power `A^{2/3}` (`Real.rpow`), and the
ordering `< 2`, none of which live on the formal ground ring
`R_q = ℤ[q, q⁻¹]`. The coefficients `a_C, a_A` are the real evaluations
`ι : R_q → ℝ, q ↦ q₀` of the Coulomb / Pauli-asymmetry scales.
-/

namespace QOU.Torsion

/-- A stable nucleus: multi-nucleon Hopf link on the beta-stability line. -/
-- Ref: [manuscript] §3/stable-nucleus
structure StableNucleus where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Coulomb coefficient a_C = (q - q⁻¹) · λ_C (real evaluation). -/
  a_C : ℝ
  /-- Pauli asymmetry coefficient (real evaluation). -/
  a_A : ℝ
  /-- Mass number. -/
  A : ℕ := p + n
  /-- Beta-stability condition: p ≈ A / (2 + a_C·A^{2/3}/(2·a_A)). -/
  stability :
    |((p : ℝ) - (A : ℝ) / (2 + a_C * (A : ℝ) ^ ((2 : ℝ) / 3) / (2 * a_A)))| < 2

end QOU.Torsion
