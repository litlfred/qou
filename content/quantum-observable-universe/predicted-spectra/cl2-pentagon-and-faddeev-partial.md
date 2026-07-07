**Proposition (Boundary closures).**
*The boundary cases of the $\mathrm{Cl}_2$ pentagon identity and the Faddeev-Kashaev quasi-classical limit are unconditional Lean theorems:*

- *(2-boundary)* `Cl_2(0) - Cl_2(0) + Cl_2(0) - Cl_2(0) + Cl_2(0) = 0` establishes the all-zero-input pentagon.
- *(3-boundary)* For every $(q, n)$, $(1 - q) \cdot \log \Phi_n(0; q) - \mathrm{Li}_2(0) = 0$ establishes the boundary case of the Faddeev-Kashaev limit at $x = 0$.

## Lean theorems

See [Table 1](#tbl:cl2-pentagon-and-faddeev-partial-table1-data).

Proofs proceed by direct rewriting, `simp`, `ring`, and `linarith` on the unconditional building blocks `Cl_2_zero` and `faddeev_limit_at_zero`.

## Closed content

The boundary-case identities are proven Lean theorems. Any future proof of the full pentagon or Tauberian limit must agree with these boundaries. This discharges the consistency requirements for the classes `Cl_2_PentagonHolds` and `FaddeevKashaevQuasiClassicalLimit`.

## Remaining content

The general non-boundary cases contain the primary mathematical content:

See [Table 2](#tbl:cl2-pentagon-and-faddeev-partial-table2-data).

Both remain isolated tasks. The §3b-cond scaffolding is structurally complete. The boundary-case identities are closed in Lean. The open content isolates the upstream Mathlib gap.

## Status

Combined with [`prop:bloch-group-quotient-construction`](#prop:bloch-group-quotient-construction), the three Mathlib gaps have the following status:

See [Table 3](#tbl:cl2-pentagon-and-faddeev-partial-table3-data).

This represents the maximum formalization achievable without upstream Lean analysis infrastructure.
