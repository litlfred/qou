import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Basic

/-!
# QOU.ObservableSubcategory — Observable subcategory Bun°(P(V))

The observable subcategory: configurations where the degree-0
algebra is non-trivial (Frobenius pairing non-degenerate on A_0).

LaTeX label: `def:observable-subcategory`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.ObservableSubcategory` in jet-horizon.lean

## References
- [leitner2026] §9/observable-subcategory
-/

-- Prerequisite type mirrored from the `QOU.JetHorizon` library module so this
-- co-location extract compiles standalone. The canonical definition lives in
-- `folio/quantum-observable-universe/lean/QOU/JetHorizon.lean` (Lake-built
-- under the `qou` package); this copy keeps the file independently checkable by
-- `lean`-direct without depending on the (uncached) library olean.

namespace QOU

/-- Prerequisite type — canonical decl: `QOU.GradedJetAlgebra` in
    `QOU/JetHorizon.lean`. A graded jet algebra: type family indexed by
    degree k ∈ ℕ, with sections at each degree. -/
-- Ref: [leitner2026] def:graded-jet-algebra
structure GradedJetAlgebra where
  /-- The type of sections at degree k. -/
  sections : ℕ → Type*
  /-- The zero section at each degree. -/
  zero : ∀ k, sections k

/-- The observable subcategory Bun°(P(V)): configurations where
    the degree-0 algebra is non-trivial (Frobenius pairing
    non-degenerate on A_0). -/
-- Ref: [leitner2026] §9/observable-subcategory
structure ObservableConfig where
  /-- The graded jet algebra. -/
  algebra : GradedJetAlgebra
  /-- There exists a non-trivial degree-0 section. -/
  degree_zero_nontrivial : ∃ (s : algebra.sections 0), s ≠ algebra.zero 0

end QOU
