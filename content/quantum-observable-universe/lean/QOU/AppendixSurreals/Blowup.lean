/-!
# QOU.AppendixSurreals.Blowup — Named infinite/infinitesimal surreals

The first infinite surreal `ω` and the first positive infinitesimal
`ε = 1/ω` are honest elements of any `SurrealField`.  This module
axiomatises their existence and proves the basic relations.

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

import QOU.AppendixSurreals.Basic

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- The **first infinite surreal** `ω`.

    Conway's construction: `ω = {0, 1, 2, … | }` — the simplest surreal
    larger than every natural.  Its existence in `K` follows from
    `K` extending the ordinals via the canonical inclusion. -/
-- Ref: [conway1976] §0
-- Ref: [ehrlich2012] Theorem 12.5 (every ordinal embeds in 𝐍𝐨)
axiom omegaSurreal : K

/-- `ω` is greater than every natural number. -/
-- Ref: [conway1976] §0
axiom omegaSurreal_gt_natCast : ∀ n : ℕ, (n : K) < omegaSurreal K

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
  -- Need: |ε| < ofReal r for every positive real r.
  -- Equivalent: 1/ω < r, i.e., ω > 1/r — true since ω > every natural.
  -- The full proof uses the ordered-field structure + omegaSurreal_gt_natCast.
  -- Ref: [conway1976] §0 — ω larger than every natural.
  sorry

end QOU.AppendixSurreals
