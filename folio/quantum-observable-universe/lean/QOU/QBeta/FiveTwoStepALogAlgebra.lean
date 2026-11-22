import QOU.QBeta.FiveTwoSaddleSumRule

/-!
# 5₂ sum rule, Step A — the log-algebra identity `V − 3ℒ`

For a root `y` of `y³ − 2y² + 3y − 1` (equivalently `y² = (1−y)³`), let
`u₀ = log y`, `v₀ = log(1−y)` (principal branches). `branch_data_of_cubic`
gives an integer `ε` with `2u₀ − 3v₀ = 2πi·ε`. Lift the logarithms to
`u = u₀ + 2πi·m`, `v = v₀ + 2πi·n` with `2m − 3n = −ε`, so that `2u = 3v`.
With

    ℒ = (Li₂(y) − 2πi·n·u₀) + u·v/2 − π²/6,
    V = 3·Li₂(y) + (u₀ + bπi)²,

Step A is the identity

    V − 3ℒ = 2(b+ε)πi·u₀ − b²π² + 4π²m² + π²/2.

`Li₂(y)` is an opaque complex number `L` and cancels: this is pure ring
algebra over `ℂ` plus the branch relation. Nothing about the dilogarithm is
used.

-- Ref: [leitner2026] 5₂ saddle sum rule (QOU/QBeta/FiveTwoSaddleSumRule.lean)
-/

namespace QOU.QBeta.FiveTwo

open Complex

/-- **Step A, abstract form.** Any `u₀ v₀ L b : ℂ` and integers `ε m n` with
the branch relation `2u₀ − 3v₀ = 2πi·ε` and the lift condition `2m − 3n = −ε`
satisfy `V − 3ℒ = 2(b+ε)πi·u₀ − b²π² + 4π²m² + π²/2`. -/
theorem stepA_identity (u₀ v₀ L b : ℂ) (ε m n : ℤ)
    (hbranch : 2 * u₀ - 3 * v₀ = (ε : ℂ) * (2 * (Real.pi : ℂ) * I))
    (hmn : 2 * m - 3 * n = -ε) :
    let u := u₀ + 2 * (Real.pi : ℂ) * I * m
    let v := v₀ + 2 * (Real.pi : ℂ) * I * n
    let ℒ := (L - 2 * (Real.pi : ℂ) * I * n * u₀) + u * v / 2 - (Real.pi : ℂ) ^ 2 / 6
    let V := 3 * L + (u₀ + b * (Real.pi : ℂ) * I) ^ 2
    V - 3 * ℒ
      = 2 * (b + ε) * (Real.pi : ℂ) * I * u₀ - b ^ 2 * (Real.pi : ℂ) ^ 2
        + 4 * (Real.pi : ℂ) ^ 2 * (m : ℂ) ^ 2 + (Real.pi : ℂ) ^ 2 / 2 := by
  intro u v ℒ V
  have hmnC : (2 : ℂ) * m - 3 * n = -ε := by exact_mod_cast hmn
  -- v₀ eliminated via the branch relation; `n` via the lift condition
  have hv₀ : v₀ = (2 * u₀ - (ε : ℂ) * (2 * (Real.pi : ℂ) * I)) / 3 := by
    linear_combination (-1 / 3 : ℂ) * hbranch
  have hn : (n : ℂ) = (2 * m + ε) / 3 := by linear_combination (-1 / 3 : ℂ) * hmnC
  simp only [V, ℒ, u, v, hv₀, hn]
  linear_combination (b ^ 2 * (Real.pi : ℂ) ^ 2 - 4 * (Real.pi : ℂ) ^ 2 * (m : ℂ) ^ 2) * I_sq

/-- **Step A at the 5₂ saddle data.** For each root `y` of
`y³ − 2y² + 3y − 1`, with `ε` the integer from `branch_data_of_cubic`
(`2·log y − 3·log(1−y) = 2πi·ε`), every lift `(m, n)` with `2m − 3n = −ε`,
every `b`, and every value `L` standing in for `Li₂(y)`:
`V − 3ℒ = 2(b+ε)πi·log y − b²π² + 4π²m² + π²/2`. -/
theorem stepA_of_cubic {y : ℂ} (hcubic : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0) :
    ∃ ε : ℤ, 2 * Complex.log y - 3 * Complex.log (1 - y)
        = (ε : ℂ) * (2 * (Real.pi : ℂ) * I) ∧
      ∀ (L b : ℂ) (m n : ℤ), 2 * m - 3 * n = -ε →
        let u₀ := Complex.log y
        let u := u₀ + 2 * (Real.pi : ℂ) * I * m
        let v := Complex.log (1 - y) + 2 * (Real.pi : ℂ) * I * n
        let ℒ := (L - 2 * (Real.pi : ℂ) * I * n * u₀) + u * v / 2
          - (Real.pi : ℂ) ^ 2 / 6
        let V := 3 * L + (u₀ + b * (Real.pi : ℂ) * I) ^ 2
        V - 3 * ℒ
          = 2 * (b + ε) * (Real.pi : ℂ) * I * u₀ - b ^ 2 * (Real.pi : ℂ) ^ 2
            + 4 * (Real.pi : ℂ) ^ 2 * (m : ℂ) ^ 2 + (Real.pi : ℂ) ^ 2 / 2 := by
  have hsq : y ^ 2 = (1 - y) ^ 3 := (cubic_iff_sq_eq_cube y).mp hcubic
  have hy : y ≠ 0 := by
    rintro rfl; norm_num at hcubic
  have hy1 : (1 : ℂ) - y ≠ 0 := by
    intro h
    have : y = 1 := by linear_combination -h
    subst this; norm_num at hcubic
  obtain ⟨ε, hε⟩ := branch_data_of_cubic hy hy1 hsq
  exact ⟨ε, hε, fun L b m n hmn =>
    stepA_identity (Complex.log y) (Complex.log (1 - y)) L b ε m n hε hmn⟩

end QOU.QBeta.FiveTwo
