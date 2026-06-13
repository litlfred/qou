*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (upstream Mathlib additions — first-attempt
contributions toward the four open Mathlib gaps).**

User: "work on adding". The Lean file
[`upstream-mathlib-additions.lean`](upstream-mathlib-additions.lean)
provides three real Mathlib-targeted additions, each sorry-free:

See [Table 1](#tbl:upstream-mathlib-additions-table1-data).

## What this advances

**(A) Towards `Real.dilog`/`Complex.dilog` Mathlib contribution.**
The `complexLiTwo` definition is a concrete `tsum`-based dilogarithm
that could be upstreamed to Mathlib as a starting point. With
absolute-convergence proofs added (Mathlib has `Summable` for
geometric-style series; the $1/k^2$ factor makes the series summable
on the closed unit disk), this becomes a candidate Mathlib PR.

**(B) Towards full `BlochWigner` Mathlib contribution.** The
`blochWigner` definition uses Mathlib's existing `Complex.log` and
`Complex.arg` infrastructure. Proving the standard 5-term pentagon
identity for `blochWigner` would close substantive gap (2) — that
proof is now reduced to (i) the absolute-convergence proof for
`complexLiTwo` and (ii) the Spence-style functional equation for
`Re(Li_2)` and `Im(Li_2)`. Both are well-defined Mathlib targets.

**(C) Towards Cl_2 functional equations.** The reflection
`Cl_2(-θ) = -Cl_2(θ)` is now a sorry-free Lean theorem proved
directly from `Real.sin_neg` and `tsum_neg`. This is the simplest
Cl_2 functional equation; the proof technique extends to other
identities (`Cl_2(θ + 2π) = Cl_2(θ)` periodicity, etc.) by
analogous `tsum` rearrangements.
## Significance

The §3b-cond chain now has **two unconditional functional
identities** (`Cl_2_neg`, `complexLiTwo_zero`, `blochWigner_zero`)
plus concrete Lean definitions for `complexLiTwo` and
`blochWigner`. This converts the previously-axiomatic
"Mathlib gap" into specific, named Lean targets that can be
upstreamed individually.
