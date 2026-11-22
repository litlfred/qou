import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Basic


/-!
# QOU.QuantumCharacteristicClasses — Yekutieli obstruction classes

Each transition Aₙ ↪ A_{n+1} defines a central extension of gerbes.
The quantum characteristic classes κₙ are the obstruction classes
in H²(𝒮, ℬ) that measure whether the gerbe extends.

The obstruction at level 0 equals the Euler class of the Reeb bundle;
under the trace map, κ₀ ↦ χ(A) = tr(id_A).

## References

- [yekutieli2010] Central Extensions of Gerbes
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

/-- A quantum characteristic class at level n: the obstruction to
    extending the gerbe from level n to level n+1.

    When κₙ = 0, the extension is unobstructed and the brane tower
    continues; non-vanishing κₙ indicates topological charge.

    LaTeX: `\label{def:quantum-characteristic-classes}` -/
-- Ref: [yekutieli2010] §4, [leitner2026] §3
structure QuantumCharacteristicClass where
  /-- Level in the brane tower. -/
  level : ℕ
  /-- The obstruction space (representing H²(𝒮, ℬ)). -/
  ObstructionSpace : Type*
  /-- The obstruction space is an additive abelian group. -/
  [addCommGroup : AddCommGroup ObstructionSpace]
  /-- The obstruction value κₙ ∈ H²(𝒮, ℬ). -/
  kappa : ObstructionSpace

/-- Expose the obstruction space's group structure to instance resolution. -/
instance (qcc : QuantumCharacteristicClass) : AddCommGroup qcc.ObstructionSpace :=
  qcc.addCommGroup

/-- The extension is unobstructed iff κₙ = 0. -/
def QuantumCharacteristicClass.isUnobstructed (qcc : QuantumCharacteristicClass) : Prop :=
  qcc.kappa = (0 : qcc.ObstructionSpace)

/-- The full sequence of quantum characteristic classes for a brane tower. -/
structure QuantumCharacteristicSequence where
  /-- The common obstruction space. -/
  ObstructionSpace : Type*
  /-- The obstruction space is an additive abelian group. -/
  [addCommGroup : AddCommGroup ObstructionSpace]
  /-- The obstruction class at each level. -/
  kappa : ℕ → ObstructionSpace
  /-- The Euler characteristic χ(A) = tr(id_A). -/
  eulerChar : ObstructionSpace
  /-- κ₀ equals the Euler class. -/
  kappa_zero_euler : kappa 0 = eulerChar
  /-- Jet corrections at level n live in a complementary subgroup, so they
      do not cancel κ₀: the correction at each level is independent of the
      base obstruction. Encoded: if κₙ ≠ 0 then κ_{n+1} ≠ 0 (persistence). -/
  corrections_persistent : ∀ n,
    kappa n ≠ (0 : ObstructionSpace) →
    kappa (n + 1) ≠ (0 : ObstructionSpace)

/-- Expose the sequence's obstruction-space group structure to resolution. -/
instance (qcs : QuantumCharacteristicSequence) : AddCommGroup qcs.ObstructionSpace :=
  qcs.addCommGroup

/-- If κ₀ ≠ 0 and corrections are complementary, then κₙ ≠ 0 for all n.

    This is the perpetual obstruction property: the Euler class cannot
    be cancelled by jet corrections at any level.

    **Re-scoped 2026-11-15 (owner decision, PR #7747, bean `qou-lx8f`).**
    This is a valid conditional: the conclusion holds whenever the
    persistence hypothesis does. It does not apply to the Kummer tower of
    Bring's surface, where the obstruction vanishes for `n ∣ χ = -6` and
    persists only for `n ∤ 6`; the "complementary subgroups" argument for
    persistence there is withdrawn (item 3 of `thm:qu-to-qou` is now the
    degree condition). -/
-- Ref: [leitner2026] §3
theorem QuantumCharacteristicSequence.perpetual
    (qcs : QuantumCharacteristicSequence)
    (h_nontorsion : qcs.kappa 0 ≠ (0 : qcs.ObstructionSpace))
    (h_persistent : ∀ n,
      qcs.kappa n ≠ (0 : qcs.ObstructionSpace) →
      qcs.kappa (n + 1) ≠ (0 : qcs.ObstructionSpace)) :
    ∀ n, qcs.kappa n ≠ (0 : qcs.ObstructionSpace) := by
  intro n
  induction n with
  | zero => exact h_nontorsion
  | succ n ih => exact h_persistent n ih

end QOU
