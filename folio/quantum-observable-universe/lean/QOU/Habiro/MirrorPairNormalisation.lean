/-
# Mirror-pair differencing: why coefficient-subtraction is only conditionally valid

`_habiro_coefficient_extract.mirror_pair_diff` originally formed the mirror
difference by subtracting **Habiro coefficients**:

    Σ Δaₘ·(u;u)ₘ  =  p_X − p_Y  =  d_X·t_X − d_Y·t_Y

where `p = d · t` is the denominator-cleared numerator of a trace `t`. That is
proportional to `t_X − t_Y` only when `d_X = d_Y`. Under trace convention C the
mirror partners happened to share a denominator, so the shortcut was silently
valid; under convention D they do not — measured on all seven canonical pairs —
and the cyclotomic multiplicities collapsed to zero.

This file proves the two facts that separate those regimes, plus the classical-
point coincidence that makes `Φ₁ = q − 1` divide a *correctly* formed difference.
Everything is over a generic `CommRing` (§7c): no ordering, no `ℝ`, no
archimedean input is needed for any of it.

Ref: [leitner2026] bean qou-0ndb; docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md
-/
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

namespace QOU.Habiro.MirrorPair

variable {R : Type*}

/-- **The valid regime.** With a shared denominator, differencing the
denominator-cleared numerators is differencing the traces, scaled by that
common denominator. Cyclotomic multiplicities of the result therefore differ
from those of `t_X − t_Y` only by the multiplicities of `d`. This is why the
convention-C computation gave the right answer despite taking the shortcut. -/
theorem coeffDiff_of_common_denom [CommRing R] (d tX tY : R) :
    d * tX - d * tY = d * (tX - tY) := by
  ring

/-- **The broken regime, exactly.** At any point where the two traces agree,
the coefficient-difference collapses to the *denominator gap* times the common
trace value. It retains no information about the traces at all. -/
theorem coeffDiff_at_coincidence [CommRing R] (dX dY t : R) :
    dX * t - dY * t = (dX - dY) * t := by
  ring

/-- Consequently, at a coincidence point the coefficient-difference vanishes
**iff** the denominators agree there or the common trace value is zero. -/
theorem coeffDiff_eq_zero_iff [CommRing R] [NoZeroDivisors R] (dX dY t : R) :
    dX * t - dY * t = 0 ↔ dX = dY ∨ t = 0 := by
  rw [coeffDiff_at_coincidence]
  rw [mul_eq_zero, sub_eq_zero]

/-- **The failure.** Differing denominators at a coincidence point force the
coefficient-difference to be *nonzero* precisely where the true difference
vanishes. This is the measured `Φ₁ = 0`: the p−n coefficient-difference
evaluated to `6` at `u = 1`, where the trace difference is `0`. -/
theorem coeffDiff_ne_zero_at_coincidence [CommRing R] [NoZeroDivisors R]
    (dX dY t : R) (hd : dX ≠ dY) (ht : t ≠ 0) :
    dX * t - dY * t ≠ 0 := by
  rw [coeffDiff_at_coincidence]
  exact mul_ne_zero (sub_eq_zero.not.mpr hd) ht

/-- **The classical-point mirror coincidence.** Write a closed-form trace as
`τ_p^Z · τ_n^N · c^n` — the shape `_build_closed_form` produces, with `c` the
common value of every interface factor. Measured at `q = 1`: all three
interface kinds (`z`, `z − h`, `z − h/2`) equal `1/2`, and `τ_p = τ_n = 1/2`.

Given only `τ_p = τ_n` and an interface count invariant under `(Z,N) ↦ (N,Z)`
(both verified), the mirror partners coincide. This is *why* `(q − 1)` divides
a correctly formed mirror difference — and it is a statement about the
classical point alone, requiring no ordering on `R`. -/
theorem mirror_trace_eq_of_tau_eq [CommMonoid R]
    (τp τn c : R) (h : τp = τn) (Z N n : ℕ) :
    τp ^ Z * τn ^ N * c ^ n = τp ^ N * τn ^ Z * c ^ n := by
  subst h
  -- after `subst` both factors are `τp`; `CommMonoid` is too weak for `ring`,
  -- so commute the two powers explicitly.
  rw [mul_comm (τp ^ Z) (τp ^ N)]

/-- The coincidence stated as a vanishing difference: the object whose
divisibility by `Φ₁ = q − 1` is being asserted. -/
theorem mirror_traceDiff_eq_zero_of_tau_eq [CommRing R]
    (τp τn c : R) (h : τp = τn) (Z N n : ℕ) :
    τp ^ Z * τn ^ N * c ^ n - τp ^ N * τn ^ Z * c ^ n = 0 := by
  rw [mirror_trace_eq_of_tau_eq τp τn c h Z N n, sub_self]

end QOU.Habiro.MirrorPair
