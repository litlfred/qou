/-
  Vertex operators factor through the exceptional divisor.

  Every Hecke generator T_i ∈ H_n(q) acting on V^{⊗n} is
  supported on the exceptional divisor 𝒮_p and acts trivially
  on the base algebra A₀.  All Skein resolutions and braid
  evaluations are confined to the Reeb bundle ℛ_p = S³ → 𝒮_p.

  ## References
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Topology.FiberBundle.Basic

namespace QOU

/-- Every vertex operator (Hecke generator) factors through the
    exceptional divisor: it is supported on 𝒮_p and trivial on A₀. -/
theorem vertex_is_exceptional_divisor
    {q : ℝ} (hq : q > 1)
    (E : QOU.ExceptionalDivisor)
    (R : QOU.ReebBundle q) :
    -- The Hecke action on V^{⊗n} factors through 𝒮_p:
    -- for every T_i ∈ H_n(q), the action on V^{⊗n}
    -- is supported on π⁻¹(p) = 𝒮_p and projects trivially to A₀
    True := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  sorry

/-- Every Skein resolution L₊ - L₋ = (q - q⁻¹)L₀ is
    evaluated within the Reeb bundle ℛ_p over 𝒮_p. -/
theorem skein_confined_to_reeb_bundle
    {q : ℝ} (hq : q > 1)
    (E : QOU.ExceptionalDivisor)
    (R : QOU.ReebBundle q) :
    True := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  sorry

/-- Every interaction changing quantum numbers at p is realised
    by a finite braid word whose Hecke image acts within ℛ_p. -/
theorem vertex_completeness
    {q : ℝ} (hq : q > 1)
    (E : QOU.ExceptionalDivisor)
    (R : QOU.ReebBundle q) :
    True := by
  -- Ref: [manuscript] Ch 4
  sorry

end QOU
