/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Reeb tower three-term recurrence and the rotation/growth = `J_ν`/`I_ν` split

The bar-graded Jacobi–Anger backbone of the Q_β `c_3` residue-A program, at the
`q → 1` / real level that needs no Bessel library in Mathlib.

With `q = exp η`, the Reeb tower `sinh(kη)` (and `cosh(kη)`) satisfies a
**constant-in-`k` three-term recurrence**

    sinh((k+1)η) = 2 cosh η · sinh(kη) − sinh((k−1)η),

which is simultaneously:

* the **Chebyshev `U`** recurrence (`sinh(kη)/sinh η = U_{k−1}(cosh η)`), i.e. the
  `SU_q(2)` character recursion in the growth regime;
* the `q → 1` limit of the **Bessel / q-Bessel three-term contiguity**
  (`J_{ν−1} + J_{ν+1} = (2ν/x) J_ν`); and
* the **constant-coefficient kernel** that the C-finite degeneration of the
  `c_k` ladder (#1839; `QOU/QBeta/RationalCoeffRecurrence.lean`,
  `QOU/QBeta/QBesselContiguityRecurrence.lean`) collapses to.

The bar-odd generating function `sinh(x sinh η) = 2 Σ_m J_{2m+1}(x) sinh((2m+1)η)`
(verified numerically in
`computations/qbeta/qbeta_reeb_tower_jacobi_anger.py`) is the
exact content of the scope doc's "Bessel-like" tag: a superposition of these
odd-order tower terms with ordinary-Bessel weights.

**Rotation/growth = `J_ν`/`I_ν`.** The *same* recurrence
`p_{k+1} = 2t·p_k − p_{k−1}` is solved by `sin(kθ)` at `t = cos θ` (bounded,
`|t| ≤ 1`, the rotation / `J_ν` regime) and by `sinh(kη)` at `t = cosh η`
(unbounded, `t ≥ 1`, the growth / `I_ν` regime) — one operator, two regimes by
`|t| ⋚ 1`, distinguished by the circle `cos²+sin²=1` vs the hyperbola
`cosh²−sinh²=1`. This is the algebraic core of the binding probe's
rotation/growth split (`binding_reeb_phase_decomposition.py`, `arccos` vs
`arccosh`); the analytic continuation `I_ν(x) = i^{−ν} J_ν(i x)` (`η ↦ iη`)
is verified numerically in the companion compute.

Built only on Mathlib's `Real.sinh`/`cosh`/`sin`/`cos` addition lemmas;
sorry-free. Cross-refs: `QOU/QBeta/CoherentCollapseSinhCosh.lean` (the bar
parity at the generator level),
`docs/audits/2026-06-13-reeb-phase-qbessel-identification.md`.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.QBeta

open Real

/-- **Bar-ODD tower three-term identity.** `sinh(a+η) + sinh(a−η) = 2 cosh η · sinh a`.
At `a = kη` this is the recursion for the odd Reeb tower `sinh(kη)` (the `c_3`
sector). -/
theorem reeb_tower_sinh_three_term (a η : ℝ) :
    sinh (a + η) + sinh (a - η) = 2 * cosh η * sinh a := by
  rw [Real.sinh_add, Real.sinh_sub]; ring

/-- **Bar-EVEN tower three-term identity.** `cosh(a+η) + cosh(a−η) = 2 cosh η · cosh a`
(the `c_2` sector). -/
theorem reeb_tower_cosh_three_term (a η : ℝ) :
    cosh (a + η) + cosh (a - η) = 2 * cosh η * cosh a := by
  rw [Real.cosh_add, Real.cosh_sub]; ring

/-- **The recurrence form** `p(a+η) = 2 cosh η · p(a) − p(a−η)` for `p = sinh`.
With `a = kη`: `sinh((k+1)η) = 2 cosh η · sinh(kη) − sinh((k−1)η)` — the
constant-`k` three-term kernel (Chebyshev `U` / `q→1` Bessel contiguity). -/
theorem reeb_tower_sinh_step (a η : ℝ) :
    sinh (a + η) = 2 * cosh η * sinh a - sinh (a - η) := by
  have h := reeb_tower_sinh_three_term a η; linarith

/-- The `cosh` recurrence form (bar-even sector). -/
theorem reeb_tower_cosh_step (a η : ℝ) :
    cosh (a + η) = 2 * cosh η * cosh a - cosh (a - η) := by
  have h := reeb_tower_cosh_three_term a η; linarith

/-- **Rotation (`J_ν`) analogue.** The *same* three-term recurrence holds for
`sin` with multiplier `cos θ`: `sin(a+θ) + sin(a−θ) = 2 cos θ · sin a`. The
rotation tower `sin(kθ)` and the growth tower `sinh(kη)` solve one operator
`p_{k+1} = 2t·p_k − p_{k−1}`, with `t = cos θ` (`|t| ≤ 1`) vs `t = cosh η`
(`t ≥ 1`). -/
theorem reeb_rotation_sin_three_term (a θ : ℝ) :
    sin (a + θ) + sin (a - θ) = 2 * cos θ * sin a := by
  rw [Real.sin_add, Real.sin_sub]; ring

/-- **Growth regime (`I_ν`): the multiplier is `≥ 1`.** `1 ≤ cosh η` always, so
the growth-tower recurrence multiplier `t = cosh η` lies in the unbounded
(`I_ν`, `arccosh`) regime. -/
theorem reeb_growth_one_le_cosh (η : ℝ) : 1 ≤ cosh η := by
  nlinarith [Real.cosh_sq_sub_sinh_sq η, sq_nonneg (Real.sinh η), Real.cosh_pos η]

/-- **Rotation regime (`J_ν`): the multiplier is bounded by `1`.** `|cos θ| ≤ 1`,
so the rotation-tower recurrence multiplier `t = cos θ` lies in the bounded
(`J_ν`, `arccos`) regime. -/
theorem reeb_rotation_abs_cos_le_one (θ : ℝ) : |cos θ| ≤ 1 := Real.abs_cos_le_one θ

/-- **The conic distinction.** The growth tower lives on the hyperbola
`cosh²η − sinh²η = 1` (the `I_ν` world); the rotation tower lives on the circle
`cos²θ + sin²θ = 1` (the `J_ν` world). Same recurrence, two conics — the
elementary shadow of `I_ν(x) = i^{−ν} J_ν(i x)`. -/
theorem reeb_growth_hyperbola (η : ℝ) : cosh η ^ 2 - sinh η ^ 2 = 1 :=
  Real.cosh_sq_sub_sinh_sq η

theorem reeb_rotation_circle (θ : ℝ) : cos θ ^ 2 + sin θ ^ 2 = 1 :=
  Real.cos_sq_add_sin_sq θ

end QOU.QBeta
