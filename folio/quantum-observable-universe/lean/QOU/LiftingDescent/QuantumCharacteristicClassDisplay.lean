import Mathlib.Algebra.Group.Basic


/-!
# QOU.LiftingDescent.QuantumCharacteristicClassDisplay

Authoritative library home for the `QuantumCharacteristicClass`
structure, previously defined only inside the content-object display
snippet `lifting-and-descent/quantum-characteristic-classes.lean`.
Relocated here (2026-06-09 axiom audit) so the companion
`quantum-characteristic-classes-unique.lean` display file can `import`
the real structure and carry a genuinely type-checked uniqueness
statement.

## References

- [yekutieli2010] Central Extensions of Gerbes
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

/-- A quantum characteristic class at level `n`: the obstruction to
    extending the gerbe from level `n` to level `n+1`. -/
-- Ref: [yekutieli2010] §4, [leitner2026] §3
structure QuantumCharacteristicClass where
  /-- Level in the brane tower. -/
  level : ℕ
  /-- The obstruction space (representing `H²(𝒮, ℬ)`). -/
  ObstructionSpace : Type*
  /-- The obstruction space is an additive abelian group. -/
  [addCommGroup : AddCommGroup ObstructionSpace]
  /-- The obstruction value `κₙ ∈ H²(𝒮, ℬ)`. -/
  kappa : ObstructionSpace
-- NOTE: the content display snippet carried a redundant
-- `zero : ObstructionSpace := (0 : ObstructionSpace)` field whose
-- default never type-checked (instance synthesis at the default site);
-- it duplicated `AddCommGroup.zero` and is dropped in this authoritative
-- relocation.  `isUnobstructed` uses `(0 : qcc.ObstructionSpace)` directly.

/-- The extension is unobstructed iff `κₙ = 0`. -/
def isUnobstructed (qcc : QuantumCharacteristicClass) : Prop :=
  haveI := qcc.addCommGroup
  qcc.kappa = (0 : qcc.ObstructionSpace)

end QOU
