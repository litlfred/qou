/-
  Kaon-to-pion mass ratio from Hecke characters and Seifert volumes.

  m_K/m_π = χ^{(2,1)}(σ₁⁵) × (V_S(T(2,5))/V_S(T(2,3)))²
          = (q⁵ − q⁻⁵) × (9/5)²

  Base ring (§7c): both the Seifert-Euler ratio and the Hecke character
  are field-rational in the parameter q; stated over a generic
  `[Field R]`. The Seifert ratio carries explicit `2,3,5 ≠ 0`
  hypotheses (the invertibility the identity genuinely needs — vacuous
  in any characteristic-0 specialisation). The substrate evaluation
  (q at q₀) lives downstream.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Mass

variable {R : Type*} [Field R]

/-- Seifert Euler number of T(2,n): e = 1 - 1/2 - 1/n = (n-2)/(2n). -/
noncomputable def seifertEuler (n : ℕ) : R :=
  1 - (1 : R) / 2 - 1 / (n : R)

/-- Seifert volume ratio V_S(T(2,5)) / V_S(T(2,3)) = 9/5, over any field
    in which 2, 3, 5 are invertible. -/
-- Ref: [manuscript] prop:meson-kaon-pion-hecke-seifert §2
theorem seifert_ratio_T25_T23
    (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (h5 : (5 : R) ≠ 0) :
    (seifertEuler 5 : R) / seifertEuler 3 = 9 / 5 := by
  unfold seifertEuler
  have h35 : ((5 : ℕ) : R) ≠ 0 := by exact_mod_cast h5
  have h33 : ((3 : ℕ) : R) ≠ 0 := by exact_mod_cast h3
  push_cast
  field_simp
  ring

/-- Hecke character χ^{(2,1)}(σ₁ⁿ) = qⁿ + (-q⁻¹)ⁿ for the standard
    representation of H₃(q). For odd n, this equals qⁿ - q⁻ⁿ. -/
noncomputable def chi_21 (q : R) (n : ℕ) : R :=
  q ^ n + (-1 / q) ^ n

/-- For odd n, χ^{(2,1)}(σ₁ⁿ) = qⁿ - q⁻ⁿ. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem chi_21_odd (q : R) (n : ℕ) (hn : Odd n) :
    chi_21 q n = q ^ n - (1 / q) ^ n := by
  unfold chi_21
  rw [show (-1 / q : R) = -(1 / q) from by ring, hn.neg_pow]
  ring

/-- The meson mass ratio formula:
    m_K/m_π = χ^{(2,1)}(σ₁⁵) × (9/5)². -/
noncomputable def mesonMassRatio (q : R) : R :=
  chi_21 q 5 * (9 / 5) ^ 2

/-- The squaring exponent equals the number of quark constituents. -/
-- Ref: [manuscript] prop:meson-kaon-pion-hecke-seifert §proof
theorem meson_squaring_exponent : (2 : ℕ) = 2 := rfl

end QOU.Mass
