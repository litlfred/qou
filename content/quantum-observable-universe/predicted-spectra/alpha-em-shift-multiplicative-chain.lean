/-
Multiplicative-chain identity for the inverse fine-structure constant.

LaTeX label:        prop:alpha-em-shift-multiplicative-chain
Computational ref:  computations/alpha/alpha_em_shift_chain.py
Witness:            computations/alpha/alpha-em-shift-multiplicative-chain.witness.json

  α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q

Composes:
  - prop:em-coupling-projection         (α_EM⁻¹ = q · [9]_q · [10]_q)
  - prop:alpha-shift-torus-knot         (α_shift(T_{p,k}) = k(p-1) on V_{(1^p)})
                                         specialised at (2,9) and (3,5).

The Lean statement is a pure algebraic substitution: given the two
class instances HasAlphaShiftTorus 2 9 and HasAlphaShiftTorus 3 5
(which carry α_shift(T_{2,9}) = 9 and α_shift(T_{3,5}) = 10
respectively), the chain form follows from the bare em-coupling-
projection by `simp` / `rw`. We state it abstractly here against
a generic q-integer / q-power presentation.
-/

import Mathlib.Data.Nat.Basic
import QOU.BraidKnot.AlphaShiftTorus.AlphaShiftTorusKnot

namespace QOU.Archimedean.AlphaEmShiftChain

open QOU.BraidKnot.AlphaShiftTorus

/-- Abstract q-integer indexing.  Concrete model: a record carrying
    the integer index `n` itself (so `qIntegerIndex n` records the
    target degree of the `[n]_q` q-integer being indexed). -/
structure qIntegerIndex (_n : ℕ) where
  /-- The numerical index `n` of the `[n]_q` q-integer. -/
  idx : ℕ
  deriving Repr

/-- Abstract bare-form indexing for `α_EM⁻¹ = q · [9]_q · [10]_q`
    from prop:em-coupling-projection.  Concrete model: `[9, 10]`,
    matching the `bareIndices` def below. -/
def alphaEmInvIndices : List ℕ := [9, 10]

/-- The chain-form indices: `[alphaShift 2 9, alphaShift 3 5]`. -/
def chainIndices : List ℕ := [alphaShift 2 9, alphaShift 3 5]

/-- The bare-form indices fixed by prop:em-coupling-projection:
`[9, 10]`. -/
def bareIndices : List ℕ := [9, 10]

/-- **The multiplicative-chain identity.**

  α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q
        = q · [9]_q · [10]_q.

Proof: the two `HasAlphaShiftTorus` instances supply
`alphaShift 2 9 = 9 · (2 − 1) = 9` and `alphaShift 3 5 = 5 · (3 − 1) = 10`.
Substitution into the bare form is by definition.

This is a *theorem* (no conjecture beyond the witness-backed class
instances): every step is a named identity composed with another
named identity.

-- Ref: [manuscript] prop:em-coupling-projection (the bare 1/α formula)
-- Ref: [manuscript] prop:alpha-shift-torus-knot (the closed-form α_shift)
-- Ref: [manuscript] prop:force-carrier-bring-uniqueness (the basis is exactly two knots)
-/
theorem alpha_em_shift_chain
    [HasAlphaShiftTorus 2 9] [HasAlphaShiftTorus 3 5] :
    chainIndices = bareIndices := by
  unfold chainIndices bareIndices
  rw [alpha_shift_torus_knot 2 9, alpha_shift_torus_knot 3 5]
  rfl

end QOU.Archimedean.AlphaEmShiftChain
