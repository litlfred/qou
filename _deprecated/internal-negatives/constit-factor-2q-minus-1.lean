/-
Constit-side per-Z step factor in the canonical-atom Markov trace
categorically equals 2q − 1 at the substrate point q_0
(to 0.033 % rel. err. — empirically, Phase 5g).

Empirical at the substrate point q_0 (Phase 5g categorical scan, 50 dps):

  measured per-Z constit factor    = 1.220358
  candidate (2q - 1) at q_0        = 1.219957
  rel. diff                        = 0.0329 %

This is a CONJECTURE: the closed form (2q - 1) matches empirically
to 0.033 %, which is conjecturally an O(h^4) higher-order term but
not yet proven exact.  The class `ConstitFactor2qMinus1`
axiomatises the identity at the substrate point in the
§3b-cond pattern (see AGENTS.md §3b-cond).  Downstream theorems
consuming `[ConstitFactor2qMinus1]` derive unconditional Lean
theorems modulo this single conjectural input.

Numerical witness (Phase 5g, 50 dps):

  constit factor at q_0                 = 1.220358
  (2 * q_0 - 1)                          = 1.219957
  rel. err                               = 3.29e-4

Ref: [jones1987] Hecke algebra representations of braid groups
Ref: [wenzl1988] Hecke algebras of type A_n and subfactors
Ref: conj:constit-factor-2q-minus-1.md
Ref: prop:interface-knot-markov-z.md (companion: interface factor z)
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.GroupPower.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

/-- The Hecke skein parameter: h := q − q⁻¹. -/
noncomputable def hecke_h_constit (q : ℝ) : ℝ :=
  q - q⁻¹

/-- The conjectured constit-side per-Z step factor at q (real),
    evaluated as the leading-order Hecke deformation of the unit
    doubled: `2q − 1`. -/
noncomputable def constit_factor_2q_minus_1 (q : ℝ) : ℝ :=
  2 * q - 1

/-- **§3b-cond class axiomatisation** of the constit-side per-Z
    step factor's closed-form identity at the substrate point.

    The class hypothesises that the empirically-measured per-Z
    step factor in the disjoint Hecke product (CONSTIT only, no
    interface generators) at the substrate point q_0 equals
    `2q − 1` to leading order, with an `O(h^4)` correction term.

    Downstream theorems consuming `[ConstitFactor2qMinus1 q]`
    derive unconditional Lean theorems modulo this single
    conjectural input. -/
class ConstitFactor2qMinus1 (q : ℝ) where
  /-- The empirically-measured per-Z constit factor. -/
  rho_constit_empirical : ℝ
  /-- The closed-form identity: ρ^constit = (2q − 1) at the
      substrate point.  Empirically holds to 0.033% rel. err.
      (Phase 5g); the residual is conjecturally `O(h^5)` with
      unit coefficient (Phase 5k.1 at q_0).  The class axiomatises
      the leading-order identity; the higher-order structure is
      research target. -/
  rho_constit_eq_2q_minus_1 :
    rho_constit_empirical = constit_factor_2q_minus_1 q

/-- **Theorem (conditional on ConstitFactor2qMinus1).**

    For any substrate q satisfying the class hypothesis, the per-Z
    constit factor in the canonical-atom Markov trace equals the
    leading-order Hecke deformation `(2q − 1)`. -/
-- Ref: [manuscript] conj:constit-factor-2q-minus-1
theorem rho_constit_eq_closed_form
    (q : ℝ) [inst : ConstitFactor2qMinus1 q] :
    inst.rho_constit_empirical = constit_factor_2q_minus_1 q :=
  inst.rho_constit_eq_2q_minus_1

/-- **Companion identity (combined per-Z τ_M factor).**

    Combining the constit-side conjecture with the interface-knot
    factor `z = 1 / (q^{1/2} + q^{-1/2})` from
    `prop:interface-knot-markov-z` (positive σ generator) gives the
    per-Z step at the **full τ_M** level:

      τ_M(β_K^{Z+1, N}) / τ_M(β_K^{Z, N})
        = z · (2q − 1) + O(h^4)
        = (2q − 1) / (q^{1/2} + q^{-1/2}) + O(h^4)

    This is the substrate-derived "Z-step factor" at the τ_M level,
    living in a different spectral channel of H_n(q) than the
    `|Δ_λ*|`-level conjecture `α ≈ [3]_q² · cosh(h)` of
    `conj:alpha-cosh-h-z-step-correction`. -/
noncomputable def full_tau_M_Z_step_leading
    (q : ℝ) (hq : 0 < q) : ℝ :=
  (2 * q - 1) / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- **Non-bar-symmetry of the constit-side closed form.**

    Unlike `[3]_q² · cosh(h)` (bar-symmetric: invariant under
    q ↦ q⁻¹), the candidate `2q − 1` is NOT bar-symmetric:

      (2q − 1) at q⁻¹  =  2q⁻¹ − 1  =  (2 − q) / q  ≠  2q − 1

    at q ≠ 1.  This reflects the chirality of the constit-side
    measurement: each Z-step adds a specific (proton-side) 3-strand
    block, breaking the q ↔ q⁻¹ symmetry that the symmetric-channel
    `cosh(h)` extraction preserves. -/
-- Ref: [manuscript] conj:constit-factor-2q-minus-1 §"Bar-symmetry"
theorem constit_factor_not_bar_symmetric
    (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    constit_factor_2q_minus_1 (q⁻¹) ≠ constit_factor_2q_minus_1 q := by
  unfold constit_factor_2q_minus_1
  intro h
  -- 2*q⁻¹ - 1 = 2*q - 1  ⇒  q⁻¹ = q
  have h2 : q⁻¹ = q := by linarith
  -- Multiply both sides of h2 by q to get q² = 1 (since q ≠ 0)
  have hq_ne : q ≠ 0 := ne_of_gt hq
  have h3 : q * q = 1 := by
    have hmul : q⁻¹ * q = q * q := by rw [h2]
    rw [inv_mul_cancel₀ hq_ne] at hmul
    linarith
  -- Factor q² - 1 = (q - 1)(q + 1) = 0 → q = 1 or q = -1
  have hexpand : (q - 1) * (q + 1) = q * q - 1 := by ring
  have h4 : (q - 1) * (q + 1) = 0 := by rw [hexpand]; linarith
  rcases mul_eq_zero.mp h4 with h5 | h5
  · -- q = 1, contradicts hq1
    exact hq1 (by linarith)
  · -- q = -1, contradicts q > 0
    linarith

end QOU.BraidKnot
