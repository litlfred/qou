---
# qou-xcvx
title: 'BLOCKER: retiring DescartesMarkovTrace is blocked by a kernel universe error at the library boundary'
status: todo
type: task
priority: high
created_at: 2026-09-05T06:21:29Z
updated_at: 2026-09-05T06:22:12Z
---

Opened after attempting the refactor `qou-ah2l` scoped. The refactor is NOT
the mechanical job it looked like; it is blocked on one specific error, and
that error is the whole cost.

## The blocker, verbatim

    (kernel) incorrect number of universe levels parameters for
    'QOU.SchurWeyl.SeminormalRep.seminormalRep', #1 expected, #0 provided

Naming `seminormalRep` from
`content/quantum-observable-universe/brings-surface/descartes-knot-eigenbasis.lean`
at `K := ℝ` **elaborates**, and the **kernel** then rejects the definition.

## What was tried

| attempt | result |
|---|---|
| both implicits inferred | kernel universe error on the def; term-mode proof also fails |
| `(μ := ν.1)` | same |
| `(μ := ν.1) (K := ℝ)` | **worse** — supplying `K` explicitly is what drives the universe count to 0 |
| tactic mode, `rw [wtrace_apply]` then `rfl` | `rw` closes the shape; `rfl` fails on two sums printing identically apart from elided proof terms |

## Why §7d does not apply

`seminormalRep` is universe-polymorphic in its field:
`{μ : YoungDiagram} → {K : Type u_1} → [Field K] → …`. This is the
universe-carrying problem of AGENTS.md §7d, but **across a package boundary**
rather than inside one file, so §7d's remedy (name the universes, tie them at
each use site) does not reach it — the parameter belongs to a declaration
elsewhere.

## What this changes about the refactor's cost

`qou-ah2l` closed with "the remaining work is wiring, not derivation", and
listed the element type (`ℝ` vs `Hecke ℝ q q⁻¹ n`) and the summand indexing
(`Fin (n/2+1)` vs Young diagrams) as the two changes. Both of those ARE
mechanical. **This is not**, and it gates them: without naming
`seminormalRep` from the content-block file there is no per-summand component
to replace `trSummand` with.

## What already works and is merged

`descartesWtrace`, `descartesWtrace_markov` (the Markov property at
`z_D = q³/(q²+1)`), `descartesWtrace_one`, and `descartes_notRootOfUnity` —
all off the library, all sorry-free (#6684). Those name `wtrace`, which is
NOT universe-polymorphic in the offending way (`wtrace : (q : ℝ) → …`), which
is exactly why they compile and the per-summand version does not.

**That is the likely route to a fix**: get a monomorphic-at-`ℝ` accessor for
the per-summand component into the library, beside `wtrace`, rather than
naming `seminormalRep` from the content tree. Not attempted.
