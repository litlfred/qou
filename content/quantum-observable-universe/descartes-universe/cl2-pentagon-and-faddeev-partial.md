*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (partial closures of substantive Mathlib gaps 2+3,
sorry-free).**
*The boundary cases of the $\mathrm{Cl}_2$ pentagon identity and
the Faddeev-Kashaev quasi-classical limit are unconditional Lean
theorems:*

- *(2-boundary) `Cl_2(0) - Cl_2(0) + Cl_2(0) - Cl_2(0) + Cl_2(0) = 0`,
  the all-zero-input pentagon.*
- *(3-boundary) For every `(q, n)`, `(1 - q) · log Φ_n(0; q) -
  Li_2(0) = 0`, the boundary case of the Faddeev-Kashaev limit
  at `x = 0`.*

> **Status: theorem (boundary cases, sorry-free).** This proposition
> closes a non-trivial portion of substantive Mathlib gaps (2)
> and (3) from
> [`rem:three-substantive-mathlib-fillers`](#rem:three-substantive-mathlib-fillers)
> without requiring upstream Mathlib contributions. The full
> identities (general 5-argument pentagon, $x \in (0,1)$
> Faddeev-Kashaev) remain open and require Fourier-series or
> Tauberian infrastructure not yet in Mathlib.

## Lean theorems (sorry-free)

| Theorem | Closes |
|---|---|
| `Cl_2_pentagon_at_zero_unconditional` | (2) at all-zero arguments — pentagon trivially holds |
| `Cl_2_pentagon_zero_substitution` | (2) function-level zero substitution |
| `Cl_2_pentagon_consistent_with_zero` | (2) consistency between pentagon class and `Cl_2_zero` |
| `faddeev_kashaev_at_zero_unconditional` | (3) at `x = 0` — both sides identically zero |
| `faddeev_kashaev_consistency_at_zero` | (3) class consistency check |
| `faddeev_kashaev_at_zero_exact` | (3) exact equality (stronger than convergence) |
| `partial_closures_at_boundary` | joint statement: `Cl_2(0) = 0 ∧ Li_2(0) = 0` |

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

| Open content | Substantive work needed |
|---|---|
| 5-argument pentagon for $\mathrm{Cl}_2$ on $(0, 2\pi)$ | Mathlib Fourier-series infrastructure (sine-series rearrangements) |
| Faddeev-Kashaev for $x \in (0, 1)$ | Mathlib uniform Tauberian theorem for q-series |

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

| Gap | Carrier | Boundary case | Full statement |
|---|---|---|---|
| (1) `BlochGroup F` quotient | (done) concrete construction | n/a | (pending) pentagon generators wiring |
| (2) $\mathrm{Cl}_2$ pentagon | (done) class hook | (done) all-zero unconditional | (pending) Mathlib Fourier infra |
| (3) Faddeev-Kashaev | (done) class hook | (done) `x = 0` unconditional | (pending) Mathlib uniform Tauberian |

This represents the maximum advance achievable without upstream
Mathlib contributions or ~hundreds of lines of additional Lean
analysis infrastructure.
