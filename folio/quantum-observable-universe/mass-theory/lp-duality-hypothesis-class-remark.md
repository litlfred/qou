In Lean the two conditions are recorded as the fields of a hypothesis class:

```lean
class HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where
  dualityGapZero       : lp.duality_gap = 0
  complementarySlackness :
    ∀ (λ : lp.Λ), λ ∈ lp.active_set ↔ lp.tight λ
```

This isolates standard LP-theory proofs—currently awaiting a full finite-dimensional LP Mathlib module—into cleanly defined conditional fields. Consumer proofs pull this hypothesis class instead of bare `sorry` tags. When the formal Mathlib support lands, a trivial model substitution will unconditionally discharge the class requirements without altering any downstream mathematical commitments.
