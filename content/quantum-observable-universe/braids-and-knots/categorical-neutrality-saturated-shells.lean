/-!
# Categorical neutrality of saturated shells (Lean class)

The conjecture asserts that the categorical mass endomorphism `Φ_n`
at level `n ∈ {2, 8, 20, 28, 50, 82, 126}` is a fixed point of the
full-twist action on `H_n(q)`. Equivalently, `Φ_n` is supported on
self-conjugate partitions `λ ⊢ n` (those with content-sum zero).

We axiomatise the conjecture as a `class` per CLAUDE.md §3b: the
typeclass instance is the conjectural input; downstream results
become conditional theorems parameterised on
`[SaturatedShellConjecture n]`.

-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001
-- Ref: [mathas1999] https://doi.org/10.1090/ulect/015
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Set.Finite

namespace QOU.ShellNeutrality

/-- The seven observed magic numbers. -/
def magicSet : Finset ℕ := {2, 8, 20, 28, 50, 82, 126}

/-- A saturated shell is a level `n` whose nucleon count is one of
    the magic numbers. -/
def Saturated (n : ℕ) : Prop := n ∈ magicSet

/-- The mass-endomorphism module at level `n`, abstracted: any type
    with a designated full-twist action and a designated mass
    endomorphism. The conjecture below asks whether the latter is
    fixed by the former at saturated levels.

    Concretely, in the QOU substrate `Endo n` will be instantiated
    as `End (A^⊗n)` in the rigid braided monoidal category `C`, the
    `fullTwist` is the central element `Δ_n²`, and `phi` is the
    global section of the mass functor at level `n`. -/
class MassEndoModule (n : ℕ) where
  /-- The endomorphism algebra at level `n`. -/
  Endo : Type*
  /-- Endomorphism algebras are monoids (composition). -/
  endoMonoid : Monoid Endo
  /-- The image of the full-twist `Δ_n²` in `Endo`. -/
  fullTwist : Endo
  /-- The categorical mass endomorphism `Φ_n`. -/
  phi : Endo

attribute [instance] MassEndoModule.endoMonoid

/-- The conjecture, encoded as a class.

    A `SaturatedShellConjecture n` instance asserts that, at the
    saturated level `n`, the full-twist `Δ_n²` acts trivially on
    `Φ_n` in the endomorphism algebra `Endo n`. The unproved input
    is the existence of the instance; downstream conditional
    theorems are then fully verified by Lean. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
class SaturatedShellConjecture (n : ℕ) extends MassEndoModule n where
  /-- The level `n` lies in the magic set (precondition). -/
  saturated : Saturated n
  /-- The asserted neutrality: full-twist commutes-and-fixes `Φ_n`
      from the left. -/
  neutrality_left : fullTwist * phi = phi
  /-- The asserted neutrality: full-twist commutes-and-fixes `Φ_n`
      from the right. -/
  neutrality_right : phi * fullTwist = phi

/-- Conditional theorem: under the saturated-shell conjecture, the
    full-twist commutes with `Φ_n`. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells §"Statement"
theorem fullTwist_commutes
    (n : ℕ) [c : SaturatedShellConjecture n] :
    c.fullTwist * c.phi = c.phi * c.fullTwist := by
  rw [c.neutrality_left, c.neutrality_right]

/-- Conditional theorem: at a saturated level, two applications of
    the full-twist still leave `Φ_n` invariant — the discrete
    `ℤ`-action of the full-twist factors through the trivial
    representation on `Φ_n`. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells §"Statement"
theorem fullTwist_iter_neutral
    (n : ℕ) [c : SaturatedShellConjecture n] (k : ℕ) :
    c.fullTwist ^ k * c.phi = c.phi := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [pow_succ, mul_assoc, c.neutrality_left]
      exact ih

end QOU.ShellNeutrality
