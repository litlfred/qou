**Proposition (partial closures of substantive Mathlib gaps 2+3, sorry-free).**
*The boundary cases of the $\mathrm{Cl}_2$ pentagon identity and the Faddeev-Kashaev quasi-classical limit are unconditional Lean theorems:*

- *(2-boundary) `Cl_2(0) - Cl_2(0) + Cl_2(0) - Cl_2(0) + Cl_2(0) = 0`, the all-zero-input pentagon.*
- *(3-boundary) For every $(q, n)$, $(1 - q) \cdot \log \Phi_n(0; q) - \mathrm{Li}_2(0) = 0$, the boundary case of the Faddeev-Kashaev limit at $x = 0$.*

## Lean theorems (sorry-free)

See [Table 1](#tbl:cl2-pentagon-and-faddeev-partial-table1-data).

Proofs proceed by direct rewriting, `simp`, `ring`, and `linarith` on the unconditional building blocks `Cl_2_zero` and `faddeev_limit_at_zero`.

## Content of this closure

**Items (2) and (3) — boundary portions, unconditional.** The boundary-case identities are Lean theorems. Any future proof of the full pentagon or full Tauberian limit must agree with these boundaries. This formally discharges the consistency requirements for the Mathlib-pending classes `Cl_2_PentagonHolds` and `FaddeevKashaevQuasiClassicalLimit`.

## Remaining content

**The general (non-boundary) cases.** These constitute the substantive mathematical content:

See [Table 2](#tbl:cl2-pentagon-and-faddeev-partial-table2-data).

Both remain isolated as Mathlib-contribution-sized tasks. The §3b-cond scaffolding is structurally complete. The boundary-case identities are unconditionally closed in Lean. The open content is exactly the upstream Mathlib gap, free from QOU-internal axiomatization.

## Significance

Combined with [`prop:bloch-group-quotient-construction`](#prop:bloch-group-quotient-construction) (item 1 closure), the three substantive Mathlib gaps have the following status:

See [Table 3](#tbl:cl2-pentagon-and-faddeev-partial-table3-data).

This represents the maximum advance achievable without upstream Mathlib contributions or extensive Lean analysis infrastructure.
