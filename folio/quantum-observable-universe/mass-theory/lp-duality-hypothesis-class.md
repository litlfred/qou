**Definition (Finite LP duality hypothesis class).**
*The finite LP strong-duality and complementary-slackness theorems are encapsulated in the hypothesis class:*

```lean
class HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where
  dualityGapZero       : lp.duality_gap = 0
  complementarySlackness :
    ∀ (λ : lp.Λ), λ ∈ lp.active_set ↔ lp.tight λ
```

This isolates standard LP-theory proofs—currently awaiting a full finite-dimensional linear-programming library—into explicit conditional fields. Downstream deductions assume this hypothesis class explicitly. When the unconditional finite-dimensional duality library is connected, a direct model substitution discharges the class requirements without altering any downstream mathematical commitments.
