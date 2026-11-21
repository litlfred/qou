/-
  Third-generation meson (φ)-to-pion mass ratio from Hecke characters
  and Seifert volumes.

  m_φ/m_π = χ^{(2,1)}(σ₁⁷) × (V_S(T(2,7))/V_S(T(2,3)))²
          = (q⁷ − q⁻⁷) × (15/7)²   ≈ 7.320

  Parallels prop:meson-kaon-pion-hecke-seifert (the proved kaon). The
  T(2,7) torus formula selects the φ(1020) (s̄s vector) at 2167 ppm — NOT
  the η (which misses by ~8.6×10⁵ ppm). Generic `[Field R]` (§7c): the
  same field-rational identities as the kaon, archimedean evaluation
  (q at q₀) downstream — no ℝ/ℂ here.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Mass.Gen3

variable {R : Type*} [Field R]

/-- Seifert Euler number of T(2,n): e = 1 - 1/2 - 1/n = (n-2)/(2n). -/
noncomputable def seifertEuler (n : ℕ) : R :=
  1 - (1 : R) / 2 - 1 / (n : R)

/-- Seifert volume ratio V_S(T(2,7)) / V_S(T(2,3)) = 15/7, over any field
    in which 2, 3, 7 are invertible. -/
-- Ref: [leitner2026] prop:gen3-meson-phi-hecke-seifert §2
theorem seifert_ratio_T27_T23
    (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (h7 : (7 : R) ≠ 0) :
    (seifertEuler 7 : R) / seifertEuler 3 = 15 / 7 := by
  unfold seifertEuler
  have h37 : ((7 : ℕ) : R) ≠ 0 := by exact_mod_cast h7
  have h33 : ((3 : ℕ) : R) ≠ 0 := by exact_mod_cast h3
  push_cast
  field_simp
  ring

/-- Hecke character χ^{(2,1)}(σ₁ⁿ) = qⁿ + (-q⁻¹)ⁿ for the standard
    representation of H₃(q). -/
noncomputable def chi_21 (q : R) (n : ℕ) : R :=
  q ^ n + (-1 / q) ^ n

/-- For odd n, χ^{(2,1)}(σ₁ⁿ) = qⁿ - q⁻ⁿ. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem chi_21_odd (q : R) (n : ℕ) (hn : Odd n) :
    chi_21 q n = q ^ n - (1 / q) ^ n := by
  unfold chi_21
  rw [show (-1 / q : R) = -(1 / q) from by ring, hn.neg_pow]
  ring

/-- The third-generation meson mass ratio formula:
    m_φ/m_π = χ^{(2,1)}(σ₁⁷) × (15/7)². -/
noncomputable def phiMassRatio (q : R) : R :=
  chi_21 q 7 * (15 / 7) ^ 2

end QOU.Mass.Gen3
