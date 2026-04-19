/-!
# QOU.ObservableSubcategory — Observable subcategory Bun°(P(V))

The observable subcategory: configurations where the degree-0
algebra is non-trivial (Frobenius pairing non-degenerate on A_0).

LaTeX label: `def:observable-subcategory`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.ObservableSubcategory` in jet-horizon.lean

## References
- [manuscript] §9/observable-subcategory
-/

-- Prerequisite types from jet-horizon.lean
-- (not independently compilable; see jet-horizon.lean for full context)

namespace QOU

/-- The observable subcategory Bun°(P(V)): configurations where
    the degree-0 algebra is non-trivial (Frobenius pairing
    non-degenerate on A_0). -/
-- Ref: [manuscript] §9/observable-subcategory
structure ObservableConfig where
  /-- The graded jet algebra. -/
  algebra : GradedJetAlgebra
  /-- There exists a non-trivial degree-0 section. -/
  degree_zero_nontrivial : ∃ (s : algebra.sections 0), s ≠ algebra.zero 0


/-- **def:observable-subcategory** — placeholder stub; full definition TBD. -/
structure ObservableSubcategory where
  witness : ℝ
  witness_pos : 0 < witness
end QOU
