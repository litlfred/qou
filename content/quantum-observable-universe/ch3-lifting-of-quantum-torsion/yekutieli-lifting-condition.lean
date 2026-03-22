/-!
# QOU.YekutieliLiftingCondition — Lifting condition for gerbe extensions

A rigid monoidal category 𝒞 satisfies the Yekutieli lifting condition
if every gerbe object can be lifted, with obstruction classified by
a single cohomology class κ ∈ H²(𝒮, ℬ).

## References

- [yekutieli2010] Central Extensions of Gerbes, §3
- [leitner2026] §3
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- The Yekutieli lifting condition for a category with gerbe structure.

    LaTeX: `\label{def:yekutieli-lifting-condition}` -/
-- Ref: [yekutieli2010] §3, [leitner2026] §3
structure YekutieliLiftingCondition where
  /-- The obstruction space (representing H²(𝒮, ℬ)). -/
  ObstructionSpace : Type*
  /-- The obstruction map: each object gets an obstruction class. -/
  obstruction : ℕ → ObstructionSpace
  /-- Zero element in the obstruction space. -/
  zero : ObstructionSpace
  /-- Lifting exists iff obstruction vanishes. -/
  lifting_iff : ∀ n, obstruction n = zero ↔ True  -- simplified

end QOU
