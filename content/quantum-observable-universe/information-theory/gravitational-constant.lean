/-!
# QOU.Information.gravitationalConstant — Gravitational constant from information geometry

The gravitational constant G(q) := c_q³ · ℏ_q / S_cell(q) where
S_cell = (q-1)²/q³ is the cumulative jet tower entropy.  In Planck
units, G_Planck = 1 identically for all q > 1.

LaTeX label: `def:gravitational-constant`

## References
- [jacobson1995] https://doi.org/10.1103/PhysRevLett.75.1260
- [bekenstein1981] https://doi.org/10.1103/PhysRevD.23.287
- [manuscript] §9/gravitational-constant
-/

import Mathlib.Algebra.Field.Basic

namespace QOU.Information

/-- Cumulative jet tower entropy: S_cell(q) = (q - 1)² / q³. -/
-- Ref: [manuscript] §9/gravitational-constant
noncomputable def cellEntropy {k : Type*} [Field k] (q : k) : k :=
  (q - 1) ^ 2 / (q * q * q)

/-- **Gravitational constant** at substrate parameter q.

    G(q) := c_q³ · ℏ_q / S_cell(q)

    where c_q = 1/(q-1), ℏ_q = (q-1)/q, and S_cell = (q-1)²/q³. -/
-- Ref: [jacobson1995] Thermodynamics of Spacetime: The Einstein Equation — see content/schema/references.ts
-- Ref: [manuscript] §9/gravitational-constant
noncomputable def gravitationalConstant {k : Type*} [Field k] (q : k)
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) : k :=
  let c := 1 / (q - 1)
  let hbar := (q - 1) / q
  let s_cell := (q - 1) ^ 2 / (q * q * q)
  c ^ 3 * hbar / s_cell

/-- In Planck units, the gravitational constant is identically 1
    for all q > 1: G_Planck = G(q) · (ℏ_q / c_q)² = 1. -/
-- Ref: [manuscript] §9/gravitational-constant
theorem gravitational_planck_eq_one {k : Type*} [Field k] (q : k)
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    gravitationalConstant q hq0 hq1 * ((q - 1) / q / (1 / (q - 1))) ^ 2 = 1 := by
  -- Ref: [manuscript] §9/gravitational-constant
  -- G(q) = c³·ℏ/S_cell = q²/(q-1)⁴
  -- (ℏ/c)² = ((q-1)/q / (1/(q-1)))² = ((q-1)²/q)²
  -- G · (ℏ/c)² = q²/(q-1)⁴ · (q-1)⁴/q² = 1
  unfold gravitationalConstant
  simp only
  field_simp [hq0, sub_ne_zero.mpr hq1]
  ring

end QOU.Information
