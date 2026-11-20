## Lean theorems

See [Table 1](#tbl:cl2-pentagon-and-faddeev-partial-table1-data).

Proofs proceed by direct rewriting, `simp`, `ring`, and `linarith` on the unconditional building blocks `Cl_2_zero` and `faddeev_limit_at_zero`.

## Closed content

The boundary-case identities are proven Lean theorems. Any future proof of the full pentagon or Tauberian limit must agree with these boundaries. This discharges the consistency requirements for the classes `Cl_2_PentagonHolds` and `FaddeevKashaevQuasiClassicalLimit`.

## Remaining content

The general non-boundary cases contain the primary mathematical content:

See [Table 2](#tbl:cl2-pentagon-and-faddeev-partial-table2-data).

Both remain isolated tasks. The conditional-class scaffolding is structurally complete. The boundary-case identities are closed in Lean. The open content isolates the upstream Mathlib gap.

## Status

Combined with [Concrete construction of $B(F)$ as `FreeAbelianGroup ⧸ pentagonSubgroup`](#prop:bloch-group-quotient-construction), the three Mathlib gaps have the following status:

See [Table 3](#tbl:cl2-pentagon-and-faddeev-partial-table3-data).

This represents the maximum formalization achievable without upstream Lean analysis infrastructure.
