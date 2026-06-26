import Mathlib.Tactic

/-!
# QOU.BraidKnot.confined_knot_binding

Canonical Lean for content block
[`prop:confined-knot-binding`](../../../quantum-observable-universe/braids-and-knots/confined-knot-binding.md).

The substantive, parameter-free content of the `.md` proof is the
**extremal cancellation** of the symmetric crossing: for the
proton–neutron symmetric mixing `½(σ + σ⁻¹)`, i.e. crossing
parameters `(c, d) = (1, −H_A/2)` with `H_A = q − q⁻¹`, the symmetric
and alternating one-dimensional Wedderburn channels cancel exactly,
so the binding volume is carried entirely by the standard
representation.

This file derives that cancellation **directly** over `ℝ`
(archimedean specialisation per AGENTS.md §7c — only `q ≠ 0` is
needed for the `q⁻¹` in `χ_alt`).  The previous encoding axiomatised
a binding-energy tautology `E_bind = |tr_M(β)|·m_e·ρ_K` as a class
field and projected it (`:= ⟨ctx.claim_i, ctx.claim_ii⟩`); that was a
vacuous self-assuming projection and is removed.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/confined-knot-binding.md
-/

namespace QOU.BraidKnot

/-- The Hecke deformation parameter `H_A = q − q⁻¹`. -/
noncomputable def heckeHA (q : ℝ) : ℝ := q - q⁻¹

/-- Symmetric-channel character of a crossing `(c, d)`:
`χ_sym(c, d) = c·q + d`. -/
noncomputable def chiSym (q c d : ℝ) : ℝ := c * q + d

/-- Alternating-channel character of a crossing `(c, d)`:
`χ_alt(c, d) = −c/q + d`. -/
noncomputable def chiAlt (q c d : ℝ) : ℝ := -c / q + d

/-- **Symmetric-channel value at the symmetric crossing.**
At `(c, d) = (1, −H_A/2)`, `χ_sym = (q² + 1)/(2q)`. -/
-- Ref: [manuscript] prop:confined-knot-binding (extremal cancellation)
theorem chiSym_symmetric_crossing (q : ℝ) (hq : q ≠ 0) :
    chiSym q 1 (-(heckeHA q) / 2) = (q ^ 2 + 1) / (2 * q) := by
  unfold chiSym heckeHA
  field_simp
  ring

/-- **Alternating-channel value at the symmetric crossing.**
At `(c, d) = (1, −H_A/2)`, `χ_alt = −(q² + 1)/(2q)`. -/
-- Ref: [manuscript] prop:confined-knot-binding (extremal cancellation)
theorem chiAlt_symmetric_crossing (q : ℝ) (hq : q ≠ 0) :
    chiAlt q 1 (-(heckeHA q) / 2) = -(q ^ 2 + 1) / (2 * q) := by
  unfold chiAlt heckeHA
  field_simp
  ring

/-- **Extremal cancellation of the symmetric crossing.**

For the symmetric mixing `(c, d) = (1, −H_A/2)`, the symmetric and
alternating one-dimensional channels are negatives of each other, so
`χ_sym + χ_alt = 0`.  Since the Wedderburn weights of the two
one-dimensional irreps coincide (`W_sym = W_alt`, both `= q²/(q⁴ +
4q² + 1)`), the weighted contribution `W_sym·χ_sym + W_alt·χ_alt`
vanishes — the binding volume is carried entirely by the standard
representation. -/
-- Ref: [manuscript] prop:confined-knot-binding (W_sym·χ_sym + W_alt·χ_alt = 0)
theorem confined_knot_extremal_cancellation (q : ℝ) (hq : q ≠ 0) :
    chiSym q 1 (-(heckeHA q) / 2) + chiAlt q 1 (-(heckeHA q) / 2) = 0 := by
  unfold chiSym chiAlt heckeHA
  field_simp
  ring

/-- **Weighted extremal cancellation** with equal one-dimensional
Wedderburn weights `W_sym = W_alt = W`.

Because the two one-dimensional channels carry the same Plancherel
weight, the weighted sum factors as `W · (χ_sym + χ_alt)`, which
vanishes by `confined_knot_extremal_cancellation`. -/
-- Ref: [manuscript] prop:confined-knot-binding (W_sym = W_alt ⇒ weighted sum = 0)
theorem confined_knot_weighted_cancellation (q W : ℝ) (hq : q ≠ 0) :
    W * chiSym q 1 (-(heckeHA q) / 2) + W * chiAlt q 1 (-(heckeHA q) / 2) = 0 := by
  rw [← mul_add, confined_knot_extremal_cancellation q hq, mul_zero]

end QOU.BraidKnot
