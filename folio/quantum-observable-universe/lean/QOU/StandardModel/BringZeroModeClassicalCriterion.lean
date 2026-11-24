/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Field.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Bring `Σ₄` Zero-Mode `q → 1` Dichotomy: Modular-Defect vs Static-Charge Coupling (`qou-vexf`)

Formalizes the electromagnetic half of `NF-P6` (bean `qou-vexf`, addressing `qou-aemx` and
`qou-az9l`) over a generic field `K` (§7c, zero `ℝ`, zero empirical literals, zero `sorry`):

For an inverse electromagnetic coupling ansatz `α⁻¹(q) = Z_top + T(q)` (`α(q) = (Z_top + T(q))⁻¹`,
where in Form B `Z_top = b₁(Σ₄) / Area(Σ₄) = 8/(12π)` and `α⁻¹(1) = 90 + 8/(12π) ≠ 0` stays
finite and nonzero at `q = 1`), classical vanishing of electromagnetic mass splittings at `q = 1`
(`m_p = m_n` at `q = 1`, `qou-az9l`) splits into **two mutually exclusive algebraic regimes**:

1. **Regime I — Modular-Defect Charge Coupling (`modularDefect_em_vanishes_at_one`):**
   Charge operators enter via the Cartan modular defect `Δν_X(q) = (F_X - F_X⁻¹)/2`, which satisfies
   `Δν_X = 0` at the classical point `F_X = 1`. Consequently, both self-energy `α(1) · Δν_X(1)²`
   and pair energy `α(1) · Δν_A(1) · Δν_B(1)` vanish identically at `q = 1` **even when
   `α⁻¹(1) = Z_top + T(1)` is finite and `α(1) ≠ 0`** (reconciling Form B's finite `90 + 8/(12π)`
   classical limit with `m_p = m_n` at `q = 1`).

2. **Regime II — Static Rational Charge Coupling (`staticCharge_incompatible_with_finite_alphaInv`):**
   Charge operators enter as `q`-independent nonzero scalars `Q_A ≠ 0, Q_B ≠ 0`
   (`V_static(q) = α(q) · Q_A · Q_B`). Then `V_static(1) = 0 ↔ α(1) = 0`, which is **impossible**
   whenever `α⁻¹(1) = Z_top + T(1)` is a finite nonzero field element (`(Z_top + T(1))⁻¹ ≠ 0`).

-- Ref: [leitner2026] beans qou-vexf, qou-aemx, qou-az9l, qou-qzvs
-/

namespace QOU.AlphaEM.BringZeroModeClassicalCriterion

section GenericField

variable {K : Type*} [Field K]

/-- Inverse electromagnetic coupling `α⁻¹ = Z_top + T_tower`. -/
def alphaInvAnsatz (zTop towerVal : K) : K := zTop + towerVal

/-- Electromagnetic coupling `α = (Z_top + T_tower)⁻¹`. -/
def alphaAnsatz (zTop towerVal : K) : K := (alphaInvAnsatz zTop towerVal)⁻¹

/-- Modular Cartan charge defect `Δν(F_X) = (F_X - F_X⁻¹) / 2`. -/
def modularChargeDefect (fX : K) : K := (fX - fX⁻¹) / 2

/-- Pair electromagnetic energy in the modular-defect regime: `α · Δν(F_A) · Δν(F_B)`. -/
def emPairModular (zTop towerVal fA fB : K) : K :=
  alphaAnsatz zTop towerVal * modularChargeDefect fA * modularChargeDefect fB

/-- Pair electromagnetic energy in the static-charge regime: `α · Q_A · Q_B`. -/
def emPairStatic (zTop towerVal qA qB : K) : K :=
  alphaAnsatz zTop towerVal * qA * qB

/-- At the classical point `F_X = 1`, `Δν(1) = 0`. -/
theorem modularChargeDefect_one : modularChargeDefect (1 : K) = 0 := by
  unfold modularChargeDefect
  simp

/-- Away from `q = 1`, for `F_X = q^{2Q}`, `Δν(q) + Δν(q⁻¹) = 0` (exact bar-oddness). -/
theorem modularChargeDefect_inv (fX : K) :
    modularChargeDefect fX⁻¹ = -modularChargeDefect fX := by
  unfold modularChargeDefect
  rw [inv_inv]
  ring

/-- **Regime I (Modular-Defect Compatibility with Finite Form B at `q = 1`):**
at `F_A = 1` (or `F_B = 1`), `emPairModular zTop towerVal 1 1 = 0` **for every `zTop` and
`towerVal`**, even when `alphaInvAnsatz zTop towerVal ≠ 0` so `alphaAnsatz zTop towerVal ≠ 0`. -/
theorem modularDefect_em_vanishes_at_one (zTop towerVal : K) :
    emPairModular zTop towerVal 1 1 = 0 ∧
      (alphaInvAnsatz zTop towerVal ≠ 0 → alphaAnsatz zTop towerVal ≠ 0) := by
  refine ⟨?_, fun hne => inv_ne_zero hne⟩
  unfold emPairModular
  rw [modularChargeDefect_one, mul_zero]

/-- **Regime II (Static-Charge Dichotomy):** for nonzero static charges `qA ≠ 0` and `qB ≠ 0`,
`emPairStatic zTop towerVal qA qB = 0` **if and only if** `alphaAnsatz zTop towerVal = 0`. -/
theorem staticCharge_em_vanishes_iff_alpha_zero (zTop towerVal qA qB : K)
    (hqA : qA ≠ 0) (hqB : qB ≠ 0) :
    emPairStatic zTop towerVal qA qB = 0 ↔ alphaAnsatz zTop towerVal = 0 := by
  unfold emPairStatic
  rw [mul_assoc, mul_eq_zero]
  simp [mul_ne_zero hqA hqB]

/-- **Incompatibility of Static Nonzero Charges with a Finite Nonzero `q = 1` Inverse Coupling:**
if `alphaInvAnsatz zTop towerVal ≠ 0` (such as Form B's `190 + 8/(12π)`), then for any `qA ≠ 0` and
`qB ≠ 0`, `emPairStatic zTop towerVal qA qB ≠ 0`. -/
theorem staticCharge_incompatible_with_finite_alphaInv (zTop towerVal qA qB : K)
    (hfin : alphaInvAnsatz zTop towerVal ≠ 0) (hqA : qA ≠ 0) (hqB : qB ≠ 0) :
    emPairStatic zTop towerVal qA qB ≠ 0 := by
  intro hzero
  have ha0 := (staticCharge_em_vanishes_iff_alpha_zero zTop towerVal qA qB hqA hqB).mp hzero
  exact inv_ne_zero hfin ha0

end GenericField

end QOU.AlphaEM.BringZeroModeClassicalCriterion
