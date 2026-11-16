import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
-- Ref: [leitner2026] Ch. 7, §ns-regular-qou
-- NS-regular quantum observable universe

/-- Data of a quantum universe as used by the NS-regularity classification of
    the sibling `.md`: the substrate parameter `q > 1` and the Euler
    characteristic `χ(A) = tr(κ₀) = deg e(ξ)` of the Reeb bundle `ξ` on the
    spectral surface `S`.

    **Global surface class (2026-11-15, owner decision Q-VO9T-2 = 1, beans
    `qou-nzyr`, `qou-hjl0`).** An intermediate version defined `NS(A)` as the
    restriction `κ₀|_Σ ∈ H²(Σ, 𝓑)` to a one-dimensional collision curve `Σ`,
    which vanishes identically (`H²(Σ, ·) = 0`, item 3 of
    `thm:ns-singularity-descartes`). Per owner ruling Q-VO9T-2 = 1 (matching
    `QOU.FluidDynamics.qou_ns_in_qou`), `NS(A)` is the **global** surface Euler
    class `e(ξ) ∈ H²(S, ℤ) ≅ ℤ`, represented by its degree `χ(A)`. Thus
    `IsNSRegular` (`NS(A) = 0`) holds iff `χ(A) = 0`, and `IsNSSingular`
    (`NS(A) ≠ 0`) holds iff `χ(A) ≠ 0`.

    **Scope (framework model correspondence).** `IsNSRegular` and `IsNSSingular`
    are internal categorical labels for `e(ξ)` on `S`. They do not assert a
    deductive theorem about the classical unforced 3D Navier–Stokes PDE on `ℝ³`
    or `𝕋³` (Tao's averaged-NS barrier, J. Amer. Math. Soc. 29 (2016), 601–674;
    `docs/audits/2026-10-12-ns-v3-tao-barrier.md`). -/
structure NSRegularQOU where
  /-- Substrate parameter q > 1. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- The Euler characteristic `χ(A) = tr(κ₀) = deg e(ξ)` of the categorical data. -/
  chi : ℤ

namespace NSRegularQOU

/-- The global surface NS obstruction `NS(A) := e(ξ) ∈ H²(S, ℤ) ≅ ℤ`,
    identified with its degree `χ(A)`. -/
def nsObstruction (U : NSRegularQOU) : ℤ := U.chi

/-- Categorical NS-regularity label: the global Euler class vanishes. -/
def IsNSRegular (U : NSRegularQOU) : Prop := U.nsObstruction = 0

/-- Categorical NS-singularity label: the global Euler class is non-zero. -/
def IsNSSingular (U : NSRegularQOU) : Prop := U.nsObstruction ≠ 0

theorem isNSRegular_iff_chi_eq_zero (U : NSRegularQOU) :
    U.IsNSRegular ↔ U.chi = 0 := Iff.rfl

theorem isNSSingular_iff_chi_ne_zero (U : NSRegularQOU) :
    U.IsNSSingular ↔ U.chi ≠ 0 := Iff.rfl

theorem not_isNSRegular_iff_isNSSingular (U : NSRegularQOU) :
    ¬ U.IsNSRegular ↔ U.IsNSSingular := by rfl

end NSRegularQOU
