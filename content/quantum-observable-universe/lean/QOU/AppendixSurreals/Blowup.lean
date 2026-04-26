import QOU.AppendixSurreals.Basic

/-!
# QOU.AppendixSurreals.Blowup — Named infinite/infinitesimal surreals

The first infinite surreal `ω` and the first positive infinitesimal
`ε = 1/ω` live as members of the `SurrealField` typeclass (see
`Basic.lean`).  This module derives the basic relations.

The full theory of named infinities (`ω², ω^ω`, hyperseries) is
substantial [@conway1976; @ehrlich2012] and is left to mathlib's
ordinal-arithmetic development.  Here we only need the named
endpoints used by the appendix's blow-up calculus.

## References

- [conway1976] Conway, *On Numbers and Games*, §0.
- [ehrlich2012] Ehrlich, *The absolute arithmetic continuum*,
  Bull. Symbolic Logic 18 (2012) 1–45.
  https://doi.org/10.2178/bsl/1327328438

LaTeX label: `def:surreal-blowup-calculus`
-/

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- Alias for the `SurrealField.omegaSurreal` member, for
    convenience in downstream files. -/
-- Ref: [conway1976] §0
-- Ref: [ehrlich2012] Theorem 12.5 (every ordinal embeds in 𝐍𝐨)
abbrev omegaSurreal : K := SurrealField.omegaSurreal

/-- `ω` is greater than every natural number. -/
-- Ref: [conway1976] §0
theorem omegaSurreal_gt_natCast (n : ℕ) :
    (n : K) < omegaSurreal K :=
  SurrealField.omegaSurreal_gt_natCast n

/-- `ω` is positive. -/
theorem omegaSurreal_pos : (0 : K) < omegaSurreal K := by
  have : (0 : K) < (omegaSurreal K) :=
    lt_of_le_of_lt (le_refl 0)
      (omegaSurreal_gt_natCast K 0 |>.trans_eq (by simp))
  exact this

/-- `ω` is non-zero. -/
theorem omegaSurreal_ne_zero : omegaSurreal K ≠ 0 :=
  ne_of_gt (omegaSurreal_pos K)

/-- The **first positive infinitesimal** `ε := 1/ω`. -/
-- Ref: [conway1976] §0
noncomputable def epsilonSurreal : K :=
  (omegaSurreal K)⁻¹

/-- `ε` is positive. -/
theorem epsilonSurreal_pos : (0 : K) < epsilonSurreal K := by
  unfold epsilonSurreal
  exact inv_pos.mpr (omegaSurreal_pos K)

/-- `ε * ω = 1`. -/
@[simp]
theorem epsilonSurreal_mul_omegaSurreal :
    epsilonSurreal K * omegaSurreal K = 1 := by
  unfold epsilonSurreal
  exact inv_mul_cancel₀ (omegaSurreal_ne_zero K)

/-- `ω * ε = 1`. -/
@[simp]
theorem omegaSurreal_mul_epsilonSurreal :
    omegaSurreal K * epsilonSurreal K = 1 := by
  unfold epsilonSurreal
  exact mul_inv_cancel₀ (omegaSurreal_ne_zero K)

/-- `ε` is infinitesimal. -/
theorem epsilonSurreal_isInfinitesimal :
    SurrealField.IsInfinitesimal (epsilonSurreal K) := by
  intro r hr
  -- Strategy: pick natural n > 1/r.  Then 1/n < r, and ω > n implies
  -- ε = 1/ω < 1/n in K, and 1/n = ofReal (1/n) < ofReal r.
  have hε_pos : (0 : K) < epsilonSurreal K := epsilonSurreal_pos K
  rw [abs_of_pos hε_pos]
  -- Archimedean: exists natural n > 1/r.
  have hinv_pos : (0 : ℝ) < 1 / r := one_div_pos.mpr hr
  obtain ⟨n, hn_lt⟩ := exists_nat_gt (1 / r)
  -- hn_lt : 1/r < n
  have hn_pos_real : (0 : ℝ) < n := lt_of_lt_of_le hinv_pos hn_lt.le
  have hn_pos_nat : 0 < n := by exact_mod_cast hn_pos_real
  -- In K: ω > n, so 1/ω < 1/n (both positive).
  have hω_gt_n : (n : K) < omegaSurreal K := omegaSurreal_gt_natCast K n
  have hn_pos_K : (0 : K) < (n : K) := by exact_mod_cast hn_pos_nat
  have hω_pos : (0 : K) < omegaSurreal K := omegaSurreal_pos K
  -- ε = ω⁻¹; want ε < (n : K)⁻¹.
  have hinv_lt : (omegaSurreal K)⁻¹ < ((n : K)⁻¹) := by
    apply inv_lt_inv_of_lt hn_pos_K hω_gt_n
  -- (n : K)⁻¹ = ofReal (1/n : ℝ).
  have hnK_eq : (n : K) = SurrealField.ofReal ((n : ℝ)) := by
    rw [← map_natCast SurrealField.ofReal n]
  have hninv_eq : ((n : K)⁻¹) = SurrealField.ofReal (1 / n : ℝ) := by
    rw [hnK_eq, ← map_inv₀]
    congr 1
    rw [one_div]
  -- Final chain: ε = ω⁻¹ < (n : K)⁻¹ = ofReal (1/n) < ofReal r.
  have hε_eq : epsilonSurreal K = (omegaSurreal K)⁻¹ := rfl
  rw [hε_eq, hninv_eq] at hinv_lt
  have h1n_lt_r : (1 / n : ℝ) < r := by
    rw [div_lt_iff hn_pos_real]
    rw [lt_div_iff hr] at hn_lt
    linarith
  have hofmono := SurrealField.ofReal_strictMono h1n_lt_r
  linarith [hinv_lt, hofmono]

end QOU.AppendixSurreals
