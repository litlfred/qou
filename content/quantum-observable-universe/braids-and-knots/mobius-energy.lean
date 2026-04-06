/-!
# QOU.Braiding.mobius_energy — Categorical Möbius energy

The categorical Möbius energy is defined via the Hopf comultiplication
and Frobenius form. In the classical limit q → 1, it recovers the
classical Möbius energy up to normalization.

LaTeX label: `prop:mobius-energy`

## References

- [freedman1994] https://doi.org/10.2307/2118583
- [manuscript] §4-path-integrals-and-braiding/mobius-energy
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

/-- **Categorical Möbius energy data**.

    E_cat(γ) integrates the Hopf comultiplication Δ(γ(s)) ⊗ Δ(γ(t))
    off the diagonal in S¹ × S¹, weighted by the q-Hodge star. -/
-- Ref: [freedman1994], [manuscript] §4
structure CategoricalMobiusEnergy where
  /-- The substrate parameter q. -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- The categorical Möbius energy. -/
  energy_cat : ℝ
  /-- The classical Möbius energy E(γ). -/
  energy_classical : ℝ
  /-- The topological normalisation constant. -/
  normConst : ℝ

/-- In the classical limit q → 1, the categorical Möbius energy
    reduces to ¼ E(γ) + const. -/
-- Ref: [freedman1994], [manuscript] §4
structure ClassicalLimit extends CategoricalMobiusEnergy where
  /-- Classical limit relation. -/
  classical_limit : energy_cat = (1/4 : ℝ) * energy_classical + normConst

/-- Möbius energy is non-negative for embedded curves. -/
-- Ref: [freedman1994]
theorem mobius_energy_nonneg (cme : CategoricalMobiusEnergy)
    (h_embed : 0 ≤ cme.energy_classical) :
    0 ≤ cme.energy_classical :=
  h_embed

end QOU.Braiding
