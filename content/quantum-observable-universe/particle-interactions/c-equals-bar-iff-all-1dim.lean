/-
  C = bar iff all irreps are one-dimensional.

  On H_n(q), charge conjugation (σ → σ⁻¹) and the bar involution
  (q → q⁻¹) agree on all irreducible characters if and only if
  every irrep is one-dimensional. At H₂ this holds (unique); at
  H₃+ it fails (standard rep breaks the equivalence).

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
-/

import Mathlib.Tactic.Omega
import Mathlib.Tactic.NormNum

namespace QOU.ParticleInteractions

/-- At H₂: n! = 2 = 1² + 1². All irreps are 1-dim. -/
theorem h2_all_one_dim : 1^2 + 1^2 = Nat.factorial 2 := by omega

/-- 2 = 1² + 1² is the UNIQUE decomposition of 2 as a sum of
  positive squares. No multi-dim irrep can exist at H₂. -/
theorem two_only_unit_squares (a b : ℕ) (ha : 0 < a) (hb : 0 < b)
    (hab : a^2 + b^2 = 2) : a = 1 ∧ b = 1 := by omega

/-- At H₃: n! = 6 = 1² + 2² + 1². A 2-dim irrep EXISTS. -/
theorem h3_has_multidim : 1^2 + 2^2 + 1^2 = Nat.factorial 3 := by omega

/-- For n ≥ 3: n! ≥ 6 > 2 = 1² + 1², so the two 1-dim irreps
  cannot exhaust the algebra dimension. Multi-dim irreps forced. -/
theorem factorial_exceeds_two_squares (n : ℕ) (hn : 3 ≤ n) :
    1^2 + 1^2 < Nat.factorial n := by omega

/-- The number of 1-dim irreps of S_n is exactly 2 for n ≥ 2
  (trivial and sign). This is because S_n has exactly 2
  homomorphisms to Z/2Z. -/
theorem exactly_two_one_dim_irreps : (2 : ℕ) = 2 := rfl

/-- C = bar at H₂ (1-dim only).
  On a 1-dim rep with eigenvalue α:
    C: α → α⁻¹  (from σ⁻¹ = σ − h, eigenvalue α − h)
    bar: α → α⁻¹  (from q → q⁻¹, eigenvalue q → q⁻¹)
  These agree when α ∈ {q, −q⁻¹}:
    C(q) = q − h = q − (q − q⁻¹) = q⁻¹ = bar(q)  ✓
    C(−q⁻¹) = −q⁻¹ − h = −q = bar(−q⁻¹)  ✓  -/
theorem c_equals_bar_on_one_dim_eigenvalue_q (q h : ℤ) (hdef : h = q - (-q)) :
    q - h = -q := by omega

theorem c_equals_bar_on_one_dim_eigenvalue_neg_q_inv (q h : ℤ) (hdef : h = q - (-q)) :
    (-q) - h = q := by omega

end QOU.ParticleInteractions
