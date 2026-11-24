/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

/-!
# The `q`-exterior derivative does not change the CR structure

On functions, `d_q f = q⁻¹ df + (1 - q⁻¹) (ξ f) Θ` (block `q-codifferential-formula`).
Pointwise this is a linear form on the tangent space `V`. This file shows, over any field:

* `dq_horizontal`: on the contact distribution `ker Θ`, `d_q f = q⁻¹ df`;
* `dq_cr_iff`: for any endomorphism `J` preserving `ker Θ` and any scalar `c`, the
  condition `d_q f (J v) = c · d_q f (v)` on `ker Θ` holds iff `df (J v) = c · df (v)`
  on `ker Θ`. With `c = i` this is the tangential Cauchy–Riemann equation, so `d_q` and
  `d` have the same CR functions.

The contact form `Θ`, the distribution `ker Θ` and `J` are inputs and are not modified,
so `d_q` selects no deformed CR structure; it only rescales the horizontal differential.
This answers the proposal that `d_q` produces a squashed (Rossi-type) CR sphere.

No `sorry`.

## References
- [leitner2026] §2 Quantum observable universes.
-/

namespace QOU.QuantumObservableUniverse.QExteriorCR

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- The pointwise `q`-differential of a function: `q⁻¹ df + (1 - q⁻¹) (ξ f) Θ`. -/
def dq (q : K) (Θ df : V →ₗ[K] K) (ξf : K) : V →ₗ[K] K :=
  q⁻¹ • df + ((1 - q⁻¹) * ξf) • Θ

theorem dq_apply (q : K) (Θ df : V →ₗ[K] K) (ξf : K) (v : V) :
    dq q Θ df ξf v = q⁻¹ * df v + (1 - q⁻¹) * ξf * Θ v := by
  simp [dq, smul_eq_mul]

/-- On the contact distribution, `d_q f = q⁻¹ df`. -/
theorem dq_horizontal (q : K) (Θ df : V →ₗ[K] K) (ξf : K) (v : V) (hv : Θ v = 0) :
    dq q Θ df ξf v = q⁻¹ * df v := by
  rw [dq_apply, hv, mul_zero, add_zero]

/-- `d_q` and `d` satisfy the same horizontal `J`-condition, so they have the same CR
functions: the CR structure `(ker Θ, J)` is unchanged. -/
theorem dq_cr_iff (q : K) (hq : q ≠ 0) (Θ df : V →ₗ[K] K) (ξf : K) (J : V →ₗ[K] V)
    (hJ : ∀ v, Θ v = 0 → Θ (J v) = 0) (c : K) :
    (∀ v, Θ v = 0 → dq q Θ df ξf (J v) = c * dq q Θ df ξf v) ↔
      (∀ v, Θ v = 0 → df (J v) = c * df v) := by
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  constructor
  · intro h v hv
    have h' := h v hv
    rw [dq_horizontal q Θ df ξf _ (hJ v hv), dq_horizontal q Θ df ξf v hv] at h'
    apply mul_left_cancel₀ hqi
    rw [h']; ring
  · intro h v hv
    rw [dq_horizontal q Θ df ξf _ (hJ v hv), dq_horizontal q Θ df ξf v hv, h v hv]
    ring

end QOU.QuantumObservableUniverse.QExteriorCR
