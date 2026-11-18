import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# Lever-1 kernel trace τ — quantum-integer (bar-even) form + SL₂ transfer structure

The lever-1 binding kernel trace has the proved closed form (`Lever1Tau.tau_kernel_closed_form`,
PRs #2767/#2755)

    τ(q) = 3(3q⁴ + 8q² + 3) / (4q(q+1)²).

This file records three structural facts about the prolongation operator `M`
(`a_D^(n+2) = τ a_D^(n+1) − a_D^(n)`) — the z2bn third probe (PF-monodromy synthesis).

**Base-ring discipline (§7c) — `M` is NOT inherently over `ℝ`.** Each statement is given over the
weakest ring that admits it, matching the substrate→archimedean wall:

1. `transfer_det_one` — over **any `CommRing R`**: the depth-2 transfer matrix `!![τ,-1;1,0]` has
   **det = 1**, so `M ∈ SL₂(R)`. Trace-agnostic, no ordering, no division — `M ∈ SL₂` is ring-universal.
2. `tau_quantum_integer_form` / `tau_bar_even` — over **any field `K` with `q,(q+1),2` invertible**
   (e.g. `K = ℚ(q)`, the Hecke fraction field): **τ is a rational function of the quantum integer
   `[2]_q = q+q⁻¹` alone**, `τ = 3(3[2]²+2)/(4([2]+2))`, hence **bar-even** `τ(q⁻¹)=τ(q)`. Here `q` is a
   **formal** variable and `q ↦ q⁻¹` is the bar-involution of the Hecke base ring `ℤ[q,q⁻¹]` — this is
   the *fibre / categorical* level, no `ℝ` needed. A classical-jet trace has no reason to collapse onto
   `[2]_q`, so the `[2]_q`-form is the Hecke / q-difference fingerprint.
3. **Hyperbolicity is the only archimedean piece.** With `τ > 2` (`Lever1Tau.tauAnchor_gt_two`, an
   **order** statement living over `ℝ`) the *archimedean evaluation* `M(q₀) ∈ SL₂(ℝ)` is **hyperbolic**
   (`λ₊ > 1` — the seed kernel's extensivity; the physical `lw` grows super-geometrically past `λ₊`,
   #2752). So `M ∈ SL₂(ℤ[q,q⁻¹])` at the fibre level (bar-even, q formal); `SL₂(ℝ)` is *only* the
   evaluation at the substrate `q₀` where the ordering `τ>2` lives. The topological Picard–Fuchs
   monodromy is `SL₂(ℤ)` (integer trace, parabolic `trace = 2` at the `I₁` nodal fibres of the
   squarefree-Δ color curve); since `τ ∉ ℤ` (even `τ(1)=21/8`), `M` is **not** that arithmetic monodromy.

See `computations/substrate/z2bn_pf_monodromy_synthesis.py` and the audit
`docs/audits/2026-06-25-z2bn-pf-monodromy-synthesis.md`.
-/

namespace QOU.Mass.TauQuantumInteger

/-- **`M ∈ SL₂(R)` over ANY commutative ring** — the depth-2 transfer matrix `!![τ,-1;1,0]` has
`det = 1` (so eigenvalues multiply to 1, sum to the trace). Trace-agnostic and ring-universal: no
ordering and no division are used, so this is *not* an `ℝ`-statement. -/
theorem transfer_det_one {R : Type*} [CommRing R] (t : R) :
    Matrix.det !![t, -1; 1, 0] = 1 := by
  rw [Matrix.det_fin_two_of]; ring

/-- **τ is a rational function of the quantum integer `[2]_q = q + q⁻¹` alone:**
`τ(q) = 3(3[2]² + 2)/(4([2]+2))`. Stated over **any field `K`** with `q, q+1, 2` invertible (e.g.
`K = ℚ(q)`, the Hecke fraction field) — *not* `ℝ`. The proved closed form `3(3q⁴+8q²+3)/(4q(q+1)²)`
collapses onto `[2]_q`, the Hecke / q-difference fingerprint. -/
theorem tau_quantum_integer_form {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hq1 : q + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2)
      = 3 * (3 * (q + q⁻¹) ^ 2 + 2) / (4 * ((q + q⁻¹) + 2)) := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by ring
    rw [e]; exact mul_ne_zero h2 h2
  have hb : (q + q⁻¹) + 2 ≠ 0 := by
    intro h0
    have key : (q + q⁻¹ + 2) * q = (q + 1) ^ 2 := by field_simp; ring
    rw [h0, zero_mul] at key
    exact pow_ne_zero 2 hq1 key.symm
  have hden1 : 4 * q * (q + 1) ^ 2 ≠ 0 :=
    mul_ne_zero (mul_ne_zero h4 hq) (pow_ne_zero 2 hq1)
  have hden2 : 4 * ((q + q⁻¹) + 2) ≠ 0 := mul_ne_zero h4 hb
  rw [div_eq_div_iff hden1 hden2]
  field_simp
  ring

/-- **τ is bar-even: `τ(q⁻¹) = τ(q)`** (invariant under the Hecke bar-involution `q ↦ q⁻¹`), over any
field `K` with `q, q+1, 2` invertible. Immediate consequence of the `[2]_q` form. -/
theorem tau_bar_even {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hq1 : q + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    3 * (3 * (q⁻¹) ^ 4 + 8 * (q⁻¹) ^ 2 + 3) / (4 * (q⁻¹) * ((q⁻¹) + 1) ^ 2)
      = 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2) := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by ring
    rw [e]; exact mul_ne_zero h2 h2
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  have hqi1 : q⁻¹ + 1 ≠ 0 := by
    intro h0
    apply hq1
    have key : (q⁻¹ + 1) * q = 1 + q := by field_simp
    rw [h0, zero_mul] at key
    rw [add_comm] at key
    exact key.symm
  have hden1 : 4 * q⁻¹ * (q⁻¹ + 1) ^ 2 ≠ 0 :=
    mul_ne_zero (mul_ne_zero h4 hqi) (pow_ne_zero 2 hqi1)
  have hden2 : 4 * q * (q + 1) ^ 2 ≠ 0 :=
    mul_ne_zero (mul_ne_zero h4 hq) (pow_ne_zero 2 hq1)
  rw [div_eq_div_iff hden1 hden2]
  field_simp
  ring

/-- Vanishing difference form of `tau_quantum_integer_form`. -/
theorem tau_quantum_integer_form_sub_eq_zero {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hq1 : q + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2)
      - 3 * (3 * (q + q⁻¹) ^ 2 + 2) / (4 * ((q + q⁻¹) + 2)) = 0 := by
  rw [tau_quantum_integer_form q hq hq1 h2, sub_self]

end QOU.Mass.TauQuantumInteger
