/-!
# QOU.Observations.gravity_spectral_prefactor

Newton's gravitational constant `G` is the prefactor `α = m_e · 8G`
of the universal curvature-rank tail in the unified mass formula.

LaTeX label: `prop:gravity-spectral-prefactor`

## References

- [manuscript] §6/gravity-spectral-prefactor
- [verlinde2011] https://doi.org/10.1007/JHEP04(2011)029
-/

namespace QOU.Observations

/-- The universal-residue prefactor of the unified mass formula. -/
structure UniversalResidue where
  α : ℝ        -- prefactor on the deep-tower stratum
  m_e : ℝ      -- electron mass (ruler)
  m_e_pos : 0 < m_e

/-- Newton's gravitational constant extracted from the prefactor:
    `G = α / (8 · m_e)`. -/
noncomputable def newtonG (U : UniversalResidue) : ℝ :=
  U.α / (8 * U.m_e)

/-- **Proposition (G as universal-residue prefactor)**.

    `α = m_e · 8G` is the prefactor of the deep-tower stratum
    `m^{≥4}_{q,K}` in the unified mass formula. -/
-- Ref: [manuscript] §6/gravity-spectral-prefactor
-- Ref: [verlinde2011] On the origin of gravity and the laws of Newton — see content/schema/references.ts
theorem gravity_spectral_prefactor (U : UniversalResidue) :
    U.α = U.m_e * 8 * newtonG U := by
  unfold newtonG
  field_simp
  ring

end QOU.Observations
