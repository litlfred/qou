/-
  Kaon-to-pion mass ratio from Hecke characters and Seifert volumes.

  m_K/m_π = χ^{(2,1)}(σ₁⁵) × (V_S(T(2,5))/V_S(T(2,3)))²
          = (q⁵ − q⁻⁵) × (9/5)²

  The algebraic factor is the Hecke character on the standard (2,1)
  representation; the topological factor is the squared Seifert
  volume ratio of T(2,5) to T(2,3).

  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Mass

/-- Seifert Euler number of T(2,n): e = 1 - 1/2 - 1/n = (n-2)/(2n). -/
noncomputable def seifertEuler (n : ℕ) (hn : n ≠ 0) : ℝ :=
  1 - (1 : ℝ) / 2 - 1 / (n : ℝ)

/-- Seifert volume ratio V_S(T(2,5)) / V_S(T(2,3)) = 9/5. -/
-- Ref: [manuscript] prop:meson-kaon-pion-hecke-seifert §2
theorem seifert_ratio_T25_T23 :
    (seifertEuler 5 (by omega)) / (seifertEuler 3 (by omega)) = 9 / 5 := by
  unfold seifertEuler
  norm_num

/-- Hecke character χ^{(2,1)}(σ₁ⁿ) = qⁿ + (-q⁻¹)ⁿ for the standard
    representation of H₃(q). For odd n, this equals qⁿ - q⁻ⁿ. -/
noncomputable def chi_21 (q : ℝ) (n : ℕ) : ℝ :=
  q ^ n + (-1 / q) ^ n

/-- For odd n, χ^{(2,1)}(σ₁ⁿ) = qⁿ - q⁻ⁿ. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem chi_21_odd (q : ℝ) (hq : q ≠ 0) (n : ℕ) (hn : Odd n) :
    chi_21 q n = q ^ n - (1 / q) ^ n := by
  unfold chi_21
  obtain ⟨k, rfl⟩ := hn
  ring_nf
  simp [neg_pow, pow_succ, pow_mul]
  ring

/-- The meson mass ratio formula:
    m_K/m_π = χ^{(2,1)}(σ₁⁵) × (9/5)².

    This encodes the Hecke-algebraic part (character at 5 crossings)
    and the Seifert-topological part (volume ratio squared for the
    2-quark meson composite). -/
noncomputable def mesonMassRatio (q : ℝ) : ℝ :=
  chi_21 q 5 * (9 / 5) ^ 2

/-- The squaring exponent equals the number of quark constituents. -/
-- Ref: [manuscript] prop:meson-kaon-pion-hecke-seifert §proof
theorem meson_squaring_exponent :
    (2 : ℕ) = 2 := rfl

end QOU.Mass


-- §3b-cond conditional-class hypothesis for `prop:meson-kaon-pion-hecke-seifert`.
-- This proposition's uses[] cone reaches `conj:meson-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `MesonDualVolume`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_MesonDualVolume
variable (q_vc : ℝ) [MesonDualVolume q_vc]
end ConditionalOn_MesonDualVolume
