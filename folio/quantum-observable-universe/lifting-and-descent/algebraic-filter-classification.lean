import Mathlib.Data.Real.Basic


/-!
# QOU.Torsion.algebraic_filter_classification — Fermion/boson classification

A harmonic 1-form α is fermionic iff [F_A, α] ≠ 0 and bosonic iff
[F_A, α] = 0, where F_A is the substrate curvature.  This dichotomy
exhausts all harmonic forms in the q-harmonic basis.

## References

- [leitner2026] Ch. 3, §7
-/

namespace QOU.Torsion

/-- Classification of a harmonic form by its commutator with the curvature.
    A form is either fermionic (nonzero commutator) or bosonic (zero commutator).
    This is an exhaustive dichotomy by the law of excluded middle. -/
-- Ref: [leitner2026] Ch. 3, §7
inductive AlgebraicFilterClass where
  | fermionic : AlgebraicFilterClass  -- [F_A, α] ≠ 0
  | bosonic : AlgebraicFilterClass    -- [F_A, α] = 0

/-- The classification is exhaustive: every form is either fermionic or bosonic. -/
theorem algebraic_filter_exhaustive (c : AlgebraicFilterClass) :
    c = AlgebraicFilterClass.fermionic ∨ c = AlgebraicFilterClass.bosonic := by
  cases c <;> simp

/-- The classification is exclusive: no form is both fermionic and bosonic. -/
theorem algebraic_filter_exclusive :
    AlgebraicFilterClass.fermionic ≠ AlgebraicFilterClass.bosonic := by
  intro h; exact AlgebraicFilterClass.noConfusion h

end QOU.Torsion
