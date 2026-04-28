/-!
# QOU.Organic.MolecularCrossingQuantum — |q+q⁻¹|_mol

The molecular crossing-energy quantum is the nuclear quantum scaled
by the dimensionless factor `α²·(m_e/m_p)`.  This file states the
formula at the level of a real-valued constant; numerical evaluation
is performed by the sympy/mpmath witnesses
`crossing-energy-mol.witness.json` and
`crossing-energy-mol-direct.witness.json`.

## References

- [manuscript] Ch. 10, Proposition `prop:molecular-crossing-quantum`
- [codata2018] CODATA 2018 recommended values, Rev. Mod. Phys. 93 025010
-/

namespace QOU.Organic

/-- The molecular crossing-energy quantum `|q+q⁻¹|_mol` as a function of
    the nuclear quantum `e_nuc`, the fine-structure constant `α`, and
    the electron-to-proton mass ratio `m_e/m_p`. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:molecular-crossing-quantum
def molecularCrossingQuantum (e_nuc α m_ratio : ℝ) : ℝ :=
  α^2 * m_ratio * e_nuc

/-- The scale-separation factor is `α²·(m_e/m_p)`. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:molecular-crossing-quantum
theorem scaleSeparation_factor (α m_ratio : ℝ) :
    molecularCrossingQuantum 1 α m_ratio = α^2 * m_ratio := by
  unfold molecularCrossingQuantum
  ring

/-- Linearity in the nuclear quantum: doubling `|q+q⁻¹|_nuc` doubles
    `|q+q⁻¹|_mol`. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:molecular-crossing-quantum
theorem molecularCrossingQuantum_linear
    (e_nuc α m_ratio c : ℝ) :
    molecularCrossingQuantum (c * e_nuc) α m_ratio
      = c * molecularCrossingQuantum e_nuc α m_ratio := by
  unfold molecularCrossingQuantum
  ring

/-- Positivity: a positive nuclear quantum and positive scale factor
    yield a positive molecular quantum. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:molecular-crossing-quantum
theorem molecularCrossingQuantum_pos
    (e_nuc α m_ratio : ℝ)
    (h_e : 0 < e_nuc) (h_α : 0 < α) (h_m : 0 < m_ratio) :
    0 < molecularCrossingQuantum e_nuc α m_ratio := by
  unfold molecularCrossingQuantum
  positivity

end QOU.Organic
