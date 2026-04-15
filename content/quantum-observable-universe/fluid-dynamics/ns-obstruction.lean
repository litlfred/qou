/-!
# QOU.FluidDynamics.NSObstruction — NS obstruction class NS(A)

The NS obstruction class NS(A) ∈ H³_loc(A, θ) is obtained by evaluating the
Yekutieli obstruction tower of the q-Navier–Stokes system at q = 1.  It is
the obstruction to lifting the q-NS solution from brane level n to level n + 1
in the limit q → 1.  NS(A) = 0 iff the quantum universe is NS-regular.

LaTeX label: `def:ns-obstruction`

## References

- [manuscript] Ch 10 §2

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic

namespace QOU.FluidDynamics

/-- The NS obstruction class NS(A): the obstruction to lifting the
    q-Navier–Stokes solution through the brane tower in the q → 1 limit.

    NS(A) = 0  ⟺  the quantum universe is NS-regular (global regularity)
    NS(A) ≠ 0  ⟺  finite-time blowup of smooth solutions -/
-- Ref: [manuscript] Ch 10 §2
structure NSObstruction where
  /-- The Euler characteristic χ(A) of the quantum universe. -/
  eulerChar : ℤ
  /-- The obstruction class, abstractly an element of H³_loc(A, θ). -/
  -- Ref: [manuscript] Ch 10 §2
  obstructionClass : ℤ
  /-- The obstruction vanishes iff the Euler characteristic vanishes. -/
  -- Ref: [manuscript] Ch 10 §2
  obstruction_iff_euler : obstructionClass = 0 ↔ eulerChar = 0

end QOU.FluidDynamics
