import QOU.MathlibExt.MarkovBondRule
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.BraidKnot.algebraic_quantum_volume_specialization — conjecture carrier

No content block references this module; it was an orphan sibling of
`def:algebraic-quantum-volume` (`mass-theory/algebraic-quantum-volume.md`),
which defines `Vol_alg(W) := tr_M(W)` under convention D.

**Conjecture (owner, 2026-11-20, bean `qou-6qbv`).** Until 2026-11-20 this file
carried a context class whose free fields were projected back out by a `def`.
Two defects besides the projection:

* claim (i) pinned the Markov parameter to `1/(√q₀ + 1/√q₀)`, which is
  **convention C**, excised on 2026-08-15. Convention D, `z = q³/(q² + 1)`, is
  now used, stated over a generic field per §7c. The parameter is
  `QOU.MathlibExt.MarkovBondRule.markovZ`, reused rather than restated: a local
  `QOU.BraidKnot.markovZD` here collided by name with the `ℝ`-valued one in
  `MarkovConventionSeparation` and `QBetaCanonicalMarkovWeightsDerived`, so no
  module could import this file together with either (bean `qou-961o`);
* claims (ii)/(iii) read `∀ β, ∃ c, Vol β = c · J β`, letting `c` depend on
  `β`, which holds whenever `J β ≠ 0` and says almost nothing.

## What is stated now

`AlgebraicQuantumVolumeSpecialization Vol J` is the β-**uniform** Jones route:
one nonzero constant `c` with `Vol β = c · J β` for every braid. No instance is
supplied.

## What is proved

* `markovZ_mul_qtwo`: the convention-D defining relation `z · (q + q⁻¹) = q²`.
* `jones_alexander_proportional`: the old file asserted a Jones route and an
  Alexander route side by side. If both held β-uniformly, the Jones and
  Alexander values would be proportional on every braid, so the two invariants
  could not be independent. The routes are therefore alternatives, not
  simultaneous specialisations of one `Vol`.
-/

namespace QOU.BraidKnot

/-- The convention-D defining relation `z · (q + q⁻¹) = q²`, for the shared
convention-D parameter `QOU.MathlibExt.MarkovBondRule.markovZ`. -/
theorem markovZ_mul_qtwo {R : Type*} [Field R] {q : R} (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    QOU.MathlibExt.MarkovBondRule.markovZ q * (q + q⁻¹) = q ^ 2 := by
  unfold QOU.MathlibExt.MarkovBondRule.markovZ
  field_simp

/-- **Conjecture (Jones route).** The substrate evaluation `Vol β` of the
algebraic quantum volume is a fixed nonzero multiple of the Jones value `J β`,
uniformly in the braid `β`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/algebraic-quantum-volume
-- Ref: [jones1987] Jones, "Hecke algebra representations of braid groups and link polynomials", Ann. Math. 126 (1987)
class AlgebraicQuantumVolumeSpecialization {Braid R : Type*} [Field R]
    (Vol J : Braid → R) : Prop where
  jones_route : ∃ c : R, c ≠ 0 ∧ ∀ β, Vol β = c * J β

/-- A Jones route and an Alexander route holding together, β-uniformly, force the
Jones and Alexander values to be proportional on every braid. -/
theorem jones_alexander_proportional {Braid R : Type*} [Field R]
    {Vol J Δ : Braid → R} {c₁ c₂ : R} (hc₂ : c₂ ≠ 0)
    (hJ : ∀ β, Vol β = c₁ * J β) (hΔ : ∀ β, Vol β = c₂ * Δ β) :
    ∀ β, Δ β = (c₁ / c₂) * J β := by
  intro β
  have h := (hΔ β).symm.trans (hJ β)
  field_simp
  rw [mul_comm]; exact h

end QOU.BraidKnot
