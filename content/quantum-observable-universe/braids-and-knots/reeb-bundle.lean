/-
  Reeb bundle over the exceptional divisor.

  The Reeb bundle ℛ_p is the Hopf fibration S³ → 𝒮_p ≅ S²
  with connection determined by the q-Reeb vector field ξ_q.
  It is the principal U(1)-bundle whose total space is the
  arena for all braiding (Hecke generator evaluation).

  ## References
  - [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

import Mathlib.Topology.FiberBundle.Basic

namespace QOU

/-- The Reeb bundle over an exceptional divisor 𝒮_p.
    This is the Hopf fibration S³ → S² ≅ 𝒮_p equipped with
    the q-Reeb vector field as connection. -/
structure ReebBundle (q : ℝ) where
  /-- The exceptional divisor (base space) -/
  base : ExceptionalDivisor
  /-- The substrate parameter controlling the connection holonomy -/
  substrate : q > 1
  /-- The holonomy of the Reeb connection around a fibre generator
      equals exp(2πi / [2]_q) where [2]_q = q + q⁻¹ -/
  holonomy : ℝ := Real.exp (2 * Real.pi / (q + q⁻¹))

-- TODO: Reeb bundle formalization requires ExceptionalDivisor (Ch 6 §2)
-- Ref: [manuscript] Ch 6 §2

end QOU
