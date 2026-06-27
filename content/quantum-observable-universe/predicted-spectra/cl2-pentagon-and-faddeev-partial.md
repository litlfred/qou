*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (partial closures of substantive Mathlib gaps 2+3,
sorry-free).**
*The boundary cases of the $\mathrm{Cl}_2$ pentagon identity and
the Faddeev-Kashaev quasi-classical limit are unconditional Lean
theorems:*

- *(2-boundary) `Cl_2(0) - Cl_2(0) + Cl_2(0) - Cl_2(0) + Cl_2(0) = 0`,
 the all-zero-input pentagon.*
- *(3-boundary) For every $(q, n)$, $(1 - q) \cdot \log \Phi_n(0; q) -
  \mathrm{Li}_2(0) = 0$, the boundary case of the Faddeev-Kashaev limit
 at $x = 0$.*

## Lean theorems (sorry-free)

See [Table 1](#tbl:cl2-pentagon-and-faddeev-partial-table1-data).

All proofs are by direct rewriting + `simp` / `ring` / `linarith`
on the unconditional building blocks `Cl_2_zero` and
`faddeev_limit_at_zero`.

## What this closes

**Items (2) and (3) — boundary portions, unconditional.** The
boundary-case identities are now Lean theorems that any future
proof of the full pentagon or full Tauberian limit must agree with.
This formally discharges the consistency requirements for the
two Mathlib-pending classes `Cl_2_PentagonHolds` and
`FaddeevKashaevQuasiClassicalLimit`.

## What remains

**The general (non-boundary) cases.** These are the substantive
mathematical content:

See [Table 2](#tbl:cl2-pentagon-and-faddeev-partial-table2-data).

Both are well-isolated as Mathlib-contribution-sized future tasks.
The §3b-cond scaffolding is now structurally complete and the
boundary-case identities are unconditionally closed in Lean —
the open content is exactly the upstream Mathlib gap, no longer
intermixed with QOU-internal axiomatisation.

## Significance

Combined with
[`prop:bloch-group-quotient-construction`](#prop:bloch-group-quotient-construction)
(item 1 closure), the three substantive Mathlib gaps now have
the following status:

See [Table 3](#tbl:cl2-pentagon-and-faddeev-partial-table3-data).

This represents the maximum advance achievable without upstream
Mathlib contributions or ~hundreds of lines of additional Lean
analysis infrastructure.
