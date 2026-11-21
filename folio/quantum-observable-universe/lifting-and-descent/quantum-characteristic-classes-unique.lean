import QOU.Basic
import QOU.LiftingDescent.QuantumCharacteristicClassDisplay


/-!
# QOU.QuantumCharClasses.unique — uniqueness of quantum characteristic classes

κ_n uniquely determined as a cohomology class by Giraud classification.

LaTeX: `\label{prop:quantum-characteristic-classes-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton QuantumCharacteristicClass`, which is **false**:
the structure has free fields (`level : ℕ` alone already separates
instances; `ObstructionSpace` and `kappa` are also data), so distinct
terms exist — e.g. `level = 0` vs `level = 1`.

This file now imports the relocated `QuantumCharacteristicClass`
structure (`QOU.LiftingDescent.QuantumCharacteristicClassDisplay`) and
**proves** — with no axiom — extensionality: classes at the same tower
level with the same obstruction space, group structure, and
obstruction value coincide.  The narrative's stronger claim (κ_n
unique *as a cohomology class*, up to cohomologous Čech cocycles)
needs a cocycle-level representation with a coboundary relation, which
the structure does not yet carry; encoding `H²(𝒮, ℬ)` as an actual
quotient is the open structure refactor.

## References

- [leitner2026] §5-lifting-and-descent/quantum-characteristic-classes-unique
- [yekutieli2010] https://doi.org/10.1016/j.aim.2010.07.008
-/

namespace QOU

/-- **Uniqueness of quantum characteristic classes (proved
    extensionality).**

    Two `QuantumCharacteristicClass` terms at the same brane-tower
    level with the same obstruction space, additive-group structure,
    and obstruction value are equal.  Replaces a false
    `Subsingleton QuantumCharacteristicClass` axiom (`level` alone
    separates instances); the cohomology-quotient classification is
    the open refactor. -/
-- Ref: [yekutieli2010] https://doi.org/10.1016/j.aim.2010.07.008
theorem QuantumCharClasses.unique
    (q₁ q₂ : QuantumCharacteristicClass)
    (hlevel : q₁.level = q₂.level)
    (hspace : q₁.ObstructionSpace = q₂.ObstructionSpace)
    (hinst : HEq q₁.addCommGroup q₂.addCommGroup)
    (hkappa : HEq q₁.kappa q₂.kappa) : q₁ = q₂ := by
  cases q₁
  cases q₂
  subst hlevel
  subst hspace
  rw [heq_iff_eq] at hinst hkappa
  subst hinst
  subst hkappa
  rfl

end QOU
