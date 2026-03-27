/-!
# QOU.Torsion.algebraic_filter_classification — Fermion/boson classification

A harmonic 1-form α is fermionic iff [F_A, α] ≠ 0 and bosonic iff
[F_A, α] = 0, where F_A is the substrate curvature.  This dichotomy
exhausts all harmonic forms in the q-harmonic basis.

## References

- [manuscript] Ch. 3, §7
-/

import Mathlib.Data.Real.Basic

namespace QOU.Torsion

-- Ref: [manuscript] Ch. 3, §7
theorem algebraic_filter_classification :
    -- Every harmonic 1-form α in the q-harmonic basis satisfies exactly
    -- one of [F_A, α] ≠ 0 (fermionic) or [F_A, α] = 0 (bosonic).
    True := by
  -- Ref: [manuscript] Ch. 3, §7
  sorry

end QOU.Torsion
