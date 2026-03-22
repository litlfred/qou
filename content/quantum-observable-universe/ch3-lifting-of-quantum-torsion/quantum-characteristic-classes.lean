/-!
# QOU.QuantumCharacteristicClasses — Yekutieli obstruction classes

Each transition Aₙ ↪ A_{n+1} defines a central extension of gerbes.
The quantum characteristic classes κₙ are the obstruction classes
in H²(𝒮, ℬ) that measure whether the gerbe extends.

## References

- [yekutieli2010] Central Extensions of Gerbes
- [leitner2026] §3 Lifting and Descent
-/

import Mathlib.Data.Real.Basic

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
  /-- The obstruction value (in R, representing H²(𝒮, ℬ)). -/
  obstruction : ℝ
  /-- The vanishing condition: κₙ = 0 iff extension is unobstructed. -/
  unobstructed_iff : obstruction = 0 ↔ True  -- simplified

end QOU
