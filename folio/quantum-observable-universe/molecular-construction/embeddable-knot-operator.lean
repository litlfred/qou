import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# `QOU.Molecular.EmbeddableKnotOperator` — embeddable knot operator binding

An embeddable knot operator carries an overlap weight `w ∈ (0,1]` fixed by the
embedding direction relative to the bond axis (axial `σ`-channel `w = 1`,
transverse `π`-channel `w = w⊥ < 1`). Its binding contribution scales the
un-embedded channel binding `E₀` by `w`. An order-`k` bond is one axial channel
plus `k-1` transverse channels, giving total binding `E₀·(1 + (k-1)·w⊥)`.

Algebraic content over a commutative ring; the `(0,1]` constraint on `w` is an
archimedean specialisation handled downstream.

-- Ref: [leitner2026] molecular-construction/embeddable-knot-operator
-/

namespace QOU.Molecular

variable {R : Type*} [CommRing R]

/-- Binding contribution of an embeddable knot operator: un-embedded channel
binding `E₀` scaled by the geometric overlap weight `w`. -/
def embeddableBinding (E0 w : R) : R := E0 * w

/-- An axial (`σ`-type) channel has overlap weight `1`, so its binding is the
full un-embedded channel binding. -/
theorem embeddableBinding_axial (E0 : R) : embeddableBinding E0 1 = E0 := by
  unfold embeddableBinding; ring

/-- Order-`k` bond binding: one axial channel (`w = 1`) plus `k-1` transverse
channels of weight `w⊥`, i.e. `E₀·(1 + (k-1)·w⊥)`. -/
def multipleBond_binding (E0 wperp : R) (k : ℕ) : R :=
  E0 * (1 + ((k : R) - 1) * wperp)

/-- A first-order bond (`k = 1`, a single axial channel) has binding `E₀`. -/
theorem multipleBond_binding_one (E0 wperp : R) :
    multipleBond_binding E0 wperp 1 = E0 := by
  unfold multipleBond_binding; push_cast; ring

end QOU.Molecular
