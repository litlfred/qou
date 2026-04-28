/-!
# QOU.Organic.C6EnergyComparison — Linear C6 vs. benzene ring

The classical-limit energy difference between the linear C6 chain
and the closed benzene ring: −2 · |q+q⁻¹|_mol.

## References

- [manuscript] Ch. 10, Lemma `lem:c6-energy-comparison`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

namespace QOU.Organic

/-- Energy difference between linear C6 chain and benzene ring,
    parameterised by the threading Alexander weight at q₀ and the
    molecular crossing quantum. -/
-- Ref: [manuscript] Ch. 10, Lemma lem:c6-energy-comparison
def c6EnergyComparison (delta_q0 e_mol : ℝ) : ℝ :=
  (delta_q0 - 5) * e_mol

/-- In the classical limit q → 1 the energy difference is
    `−2 · |q+q⁻¹|_mol`. -/
-- Ref: [manuscript] Ch. 10, Lemma lem:c6-energy-comparison
theorem c6EnergyComparison_classical (e_mol : ℝ) :
    c6EnergyComparison 3 e_mol = -2 * e_mol := by
  unfold c6EnergyComparison; ring

/-- The ring is favoured in the classical limit (energy difference
    is negative when the crossing quantum is positive). -/
-- Ref: [manuscript] Ch. 10, Lemma lem:c6-energy-comparison
theorem ring_favoured_classical (e_mol : ℝ) (h : 0 < e_mol) :
    c6EnergyComparison 3 e_mol < 0 := by
  rw [c6EnergyComparison_classical]
  linarith

end QOU.Organic
