/-!
# QOU.BraidKnot.BarInvolution (definition block)

Canonical Lean infrastructure for the bar-involution on the
Iwahori–Hecke algebra `H_n(q)` and its `P_avg`/`P_skew`
projections.

This file is the `def:bar-involution` content block's Lean
sibling, providing the abstract `class BarInvolution R` interface
and the `IsBarSymmetric` / `IsBarAntiSymmetric` predicates that
downstream blocks consume.

The substantive theorems (Hoefsmit-Quantum-2 identity,
`c_5` closed form via quantum-2, classical limit `c_5(1) = -5/4`)
live in [c5-involution-leibniz-decomposition.lean](c5-involution-leibniz-decomposition.lean) — they are *proved
there*, no `sorry`. This file holds only the abstract
infrastructure they consume.

This duplicates `BarInvolution` from
[bar-symmetric-three-layer-synthesis.lean](bar-symmetric-three-layer-synthesis.lean) intentionally
during the transition: once both blocks land on main, downstream
consumers can choose either canonical import.
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Defs
-- Ref: [manuscript] def:bar-involution
-- Ref: [manuscript] prop:bar-symmetric-three-layer-synthesis
-- Ref: [wenzl1988] doi:10.1007/BF01404457
-- Ref: [hoefsmit1974]

namespace QOU.BraidKnot.BarInvolutionDef

/-- The bar-involution `σ ↦ σ⁻¹` / `q ↦ q⁻¹` on a generic
    commutative ring (typically the coefficient field
    `ℤ[q^{±1/2}, (q-q⁻¹)⁻¹]` or its archimedean specialisation
    `ℝ`). Records the four ring-involution axioms. -/
class BarInvolution (R : Type*) [CommRing R] where
  bar : R → R
  bar_involutive : ∀ x, bar (bar x) = x
  bar_add : ∀ x y, bar (x + y) = bar x + bar y
  bar_mul : ∀ x y, bar (x * y) = bar x * bar y
  bar_one : bar 1 = 1
  bar_zero : bar 0 = 0

/-- Predicate: `x` is bar-symmetric (bar-even). -/
def IsBarSymmetric {R : Type*} [CommRing R] [BarInvolution R] (x : R) : Prop :=
  BarInvolution.bar x = x

/-- Predicate: `x` is bar-anti-symmetric (bar-odd). -/
def IsBarAntiSymmetric {R : Type*} [CommRing R] [BarInvolution R] (x : R) : Prop :=
  BarInvolution.bar x = -x

/-- `P_avg = (1 + bar)/2`. Requires `2 ≠ 0` in `R`. -/
noncomputable def barSymmetricProjection {R : Type*} [Field R] [BarInvolution R]
    (x : R) : R := (x + BarInvolution.bar x) / 2

/-- `P_skew = (1 - bar)/2`. Requires `2 ≠ 0` in `R`. -/
noncomputable def barSkewProjection {R : Type*} [Field R] [BarInvolution R]
    (x : R) : R := (x - BarInvolution.bar x) / 2

/-- Every element decomposes as `x = P_avg(x) + P_skew(x)`. -/
theorem decompose {R : Type*} [Field R] [BarInvolution R] (x : R) :
    x = barSymmetricProjection x + barSkewProjection x := by
  unfold barSymmetricProjection barSkewProjection
  ring

end QOU.BraidKnot.BarInvolutionDef
