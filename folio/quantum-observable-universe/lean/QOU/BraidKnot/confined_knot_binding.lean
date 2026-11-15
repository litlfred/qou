import Mathlib.Algebra.Ring.Units
import Mathlib.Algebra.Ring.Invertible
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

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

This file derives that cancellation **directly** over a generic
commutative ring (per AGENTS.md §7c).  The previous encoding axiomatised
a binding-energy tautology `E_bind = |tr_M(β)|·m_e·ρ_K` as a class
field and projected it (`:= ⟨ctx.claim_i, ctx.claim_ii⟩`); that was a
vacuous self-assuming projection and is removed.

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/confined-knot-binding.md
-/

namespace QOU.BraidKnot

/-! §7c: the cancellation below is **exact in `q`** — `χ_sym + χ_alt = 0` at
`(c, d) = (1, −H_A/2)` — and needs only a commutative ring in which `q` is a
unit (carried as `q : Rˣ`, so `↑q⁻¹` is a `Units` coercion) and `2` is
invertible (the `H_A/2` halving, written `⅟(2 : R)`).  Invertibility of `2`,
not characteristic zero and not archimedean: no ordering, radical or `Real.*`
construct appears, so the statements hold over `ℤ[1/2][q, q⁻¹]` and the
archimedean evaluation at `q_0` happens downstream. -/

variable {R : Type*} [CommRing R] [Invertible (2 : R)]

/-- The Hecke deformation parameter `H_A = q − q⁻¹`. -/
def heckeHA (q : Rˣ) : R := (q : R) - (↑q⁻¹ : R)

/-- Symmetric-channel character of a crossing `(c, d)`:
`χ_sym(c, d) = c·q + d`. -/
def chiSym (q : Rˣ) (c d : R) : R := c * (q : R) + d

/-- Alternating-channel character of a crossing `(c, d)`:
`χ_alt(c, d) = −c·q⁻¹ + d`. -/
def chiAlt (q : Rˣ) (c d : R) : R := -c * (↑q⁻¹ : R) + d

/-- **Symmetric-channel value at the symmetric crossing.**
At `(c, d) = (1, −H_A/2)`, `χ_sym = (q² + 1)/(2q)`, written division-free as
`(q² + 1)·⅟2·q⁻¹`. -/
-- Ref: [leitner2026] prop:confined-knot-binding (extremal cancellation)
theorem chiSym_symmetric_crossing (q : Rˣ) :
    chiSym q 1 (-(heckeHA q) * ⅟(2 : R))
      = ((q : R) ^ 2 + 1) * ⅟(2 : R) * (↑q⁻¹ : R) := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  unfold chiSym heckeHA
  linear_combination (-(q : R) * ⅟(2 : R)) * hq + (-(q : R)) * h2

/-- **Alternating-channel value at the symmetric crossing.**
At `(c, d) = (1, −H_A/2)`, `χ_alt = −(q² + 1)/(2q)`, written division-free as
`−((q² + 1)·⅟2·q⁻¹)`. -/
-- Ref: [leitner2026] prop:confined-knot-binding (extremal cancellation)
theorem chiAlt_symmetric_crossing (q : Rˣ) :
    chiAlt q 1 (-(heckeHA q) * ⅟(2 : R))
      = -(((q : R) ^ 2 + 1) * ⅟(2 : R) * (↑q⁻¹ : R)) := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  unfold chiAlt heckeHA
  linear_combination ((q : R) * ⅟(2 : R)) * hq + (↑q⁻¹ : R) * h2

/-- **Extremal cancellation of the symmetric crossing.**

For the symmetric mixing `(c, d) = (1, −H_A/2)`, the symmetric and
alternating one-dimensional channels are negatives of each other, so
`χ_sym + χ_alt = 0`.  Since the Wedderburn weights of the two
one-dimensional irreps coincide (`W_sym = W_alt`, both `= q²/(q⁴ +
4q² + 1)`), the weighted contribution `W_sym·χ_sym + W_alt·χ_alt`
vanishes — the binding volume is carried entirely by the standard
representation. -/
-- Ref: [leitner2026] prop:confined-knot-binding (W_sym·χ_sym + W_alt·χ_alt = 0)
theorem confined_knot_extremal_cancellation (q : Rˣ) :
    chiSym q 1 (-(heckeHA q) * ⅟(2 : R))
      + chiAlt q 1 (-(heckeHA q) * ⅟(2 : R)) = (0 : R) := by
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  unfold chiSym chiAlt heckeHA
  linear_combination (-((q : R) - (↑q⁻¹ : R))) * h2

/-- **Weighted extremal cancellation** with equal one-dimensional
Wedderburn weights `W_sym = W_alt = W`.

Because the two one-dimensional channels carry the same Plancherel
weight, the weighted sum factors as `W · (χ_sym + χ_alt)`, which
vanishes by `confined_knot_extremal_cancellation`. -/
-- Ref: [leitner2026] prop:confined-knot-binding (W_sym = W_alt ⇒ weighted sum = 0)
theorem confined_knot_weighted_cancellation (q : Rˣ) (W : R) :
    W * chiSym q 1 (-(heckeHA q) * ⅟(2 : R))
      + W * chiAlt q 1 (-(heckeHA q) * ⅟(2 : R)) = 0 := by
  rw [← mul_add, confined_knot_extremal_cancellation q, mul_zero]

end QOU.BraidKnot
