import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# α_EM Habiro element: bar-involution fixed point + special values

The α_EM next-order factor is the **Habiro element**
`H(q) = [2]_q · (1 − h²·α)`, where `[2]_q = q + q⁻¹` and
`h = q − q⁻¹` is the Hecke differential (PR #1511,
`prop:em-coupling-bring-zero-mode`).

This file formalises the **fibre-level** structural facts about `H`
that hold over a *generic commutative ring* — i.e. with `q` a formal
variable and **no reality or archimedean assumption** (per AGENTS.md
"Im(q) at fibre vs observable level", the Habiro element lives at the
fibre/categorical level where the operative symmetry is the bar
involution `q ↦ q⁻¹`, not a reality constraint).

Working with `q` and its inverse `qi` as independent ring variables
subject to `q · qi = 1` keeps everything inside `CommRing` + a single
`q·qi = 1` rewrite — no `ℝ`, no ordering, no complex numbers.

1. **Bar-involution fixed point.** `H` is invariant under the bar
   involution `q ↦ q⁻¹` (swap `q ↔ qi`): `H(qi, q, α) = H(q, qi, α)`.
   This is the clean charge-conjugation-symmetric sector the Q_β
   scaling map must occupy (PR #1602); `H` lies *entirely* in it.
2. **Special values.** `H(1) = 2` (the classical `α/(4π)` leading
   term) and `H(−1) = −2` (the bar / charge-conjugation mode). These
   are the `ζ_1` and `ζ_2` root-of-unity evaluations — real, generic.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/


namespace QOU.BraidKnot

variable {R : Type*} [CommRing R]

/-- The α_EM **Habiro element** `H = [2]_q · (1 − h²·α)` written with
`q` and its inverse `qi` as independent variables (subject to
`q · qi = 1` where that identity is needed). `[2]_q = q + qi`,
`h = q − qi`, so `H = (q + qi)·(1 − (q − qi)²·α)`. Generic `CommRing`:
no reality, no archimedean evaluation. -/
def alphaEmHabiro (q qi α : R) : R :=
  (q + qi) * (1 - (q - qi)^2 * α)

/-- **Bar-involution fixed point.** `H` is invariant under the bar
involution `q ↦ q⁻¹` (swapping `q ↔ qi`):
`H(qi, q, α) = H(q, qi, α)`. The proof is pure `ring` — the swap fixes
`q + qi` and squares away the sign in `(q − qi)²`. This is the
fibre-level (formal-variable) statement; no reality is used. -/
theorem alphaEmHabiro_bar_invariant (q qi α : R) :
    alphaEmHabiro qi q α = alphaEmHabiro q qi α := by
  unfold alphaEmHabiro
  ring

/-- **Special value `H(ζ_1) = H(1) = 2`** (the classical leading term
giving `α/(4π)`). At `q = qi = 1`: `[2]_q = 2`, `h = 0`, so `H = 2`. -/
theorem alphaEmHabiro_at_one (α : R) :
    alphaEmHabiro 1 1 α = 2 := by
  unfold alphaEmHabiro
  ring

/-- **Special value `H(ζ_2) = H(−1) = −2`** (the bar / charge-
conjugation mode). At `q = qi = −1`: `[2]_q = −2`, `h = 0`, so
`H = −2`. -/
theorem alphaEmHabiro_at_neg_one (α : R) :
    alphaEmHabiro (-1) (-1) α = -2 := by
  unfold alphaEmHabiro
  ring

/-- **Exact modular zero `H(ζ_4) = 0`** at a fourth root of unity (`ζ² = -1`, so
`ζ⁻¹ = -ζ` and `[2]_{ζ_4} = ζ + (-ζ) = 0`), structural dual of the `𝔔_β` modular pole. -/
theorem alphaEmHabiro_at_zeta4 (ζ α : R) :
    alphaEmHabiro ζ (-ζ) α = 0 := by
  unfold alphaEmHabiro
  ring

/-- At any fourth root of unity `ζ` satisfying `ζ ^ 2 = -1`, `ζ * (-ζ) = 1` (confirming `-ζ`
is the multiplicative inverse `ζ⁻¹`) and `H(ζ, -ζ, α) = 0`. -/
theorem alphaEmHabiro_zeta4_inv_and_zero (ζ α : R) (hζ : ζ ^ 2 = -1) :
    ζ * (-ζ) = 1 ∧ alphaEmHabiro ζ (-ζ) α = 0 := by
  refine ⟨?_, alphaEmHabiro_at_zeta4 ζ α⟩
  calc ζ * (-ζ) = -(ζ ^ 2) := by ring
    _ = -(-1) := by rw [hζ]
    _ = 1 := by ring

end QOU.BraidKnot
