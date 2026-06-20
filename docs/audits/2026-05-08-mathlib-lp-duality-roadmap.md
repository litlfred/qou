# Mathlib LP-duality wiring — roadmap

**Date:** 2026-05-08
**Scope:** Survey Mathlib4's current LP-duality state and propose
a wiring roadmap for the two `sorry`s in
[`confinement-nf-partial-proof.lean`](../../content/quantum-observable-universe/braids-and-knots/confinement-nf-partial-proof.lean)
(`strong_duality`, `complementary_slackness`).

**Status:** Research-grade scope, deferred. This doc identifies
the Mathlib API surface to consume and an effort estimate; the
actual Lean wiring is a separate PR (likely 1–2 weeks).

## Current state in Mathlib4

Mathlib4 (May 2026) **does not** ship a packaged "finite LP strong
duality" theorem. The closest available API:

| Module | Provides |
|---|---|
| [`Mathlib.Analysis.Convex.Cone.InnerDual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Cone/InnerDual.html) | **Farkas' lemma** for proper cones (geometric interpretation via hyperplane separation); inner-dual self-duality (`(C*)* = C` for closed pointed cones) |
| `Mathlib.Analysis.Convex.Cone.Pointed` | Pointed convex cones, closure properties |
| `Mathlib.Analysis.Convex.Cone.Proper` | Proper cones (closed + pointed); the canonical setting for conic-LP duality |
| `Mathlib.LinearAlgebra.Matrix.LinearProgramming` | (NOT YET LANDED — ⚠️ no LP strong-duality theorem in Mathlib master) |
| `Mathlib.Analysis.Convex.Combination` | Convex hulls, Carathéodory's theorem |
| `Mathlib.Analysis.Inner.Hahn`, `Mathlib.Topology.Order.Lattice` | Hahn–Banach separation, lattice operations |

**Key absence:** no theorem of the form
`(bounded ∧ feasible) → primal_obj = dual_obj` for our finite-dim
LP setting. The conic-Farkas + inner-dual machinery is the
**foundation** but the LP-specific assembly is missing.

## Wiring path (research-grade)

### Step 1: Restate `OperatorSelectionLP` as a conic program

Our LP from `confinement-nf-partial-proof.lean`:

```lean
structure OperatorSelectionLP where
  Λ : Type
  finite : Finite Λ
  ...

opaque primal_obj : OperatorSelectionLP → ℝ
opaque dual_obj : OperatorSelectionLP → ℝ
opaque active_set : (lp : OperatorSelectionLP) → Set lp.Λ
opaque tight : (lp : OperatorSelectionLP) → lp.Λ → Prop
```

Restate as a conic program with:
- A primal cone $C \subset \mathbb{R}^{|\Lambda|}$ (Wedderburn-block
  positivity)
- A dual cone $C^* \subset \mathbb{R}^{|\Lambda|}$ (LP shadow prices)
- Linear objective and constraints

**Effort:** Refactor `OperatorSelectionLP` to expose primal/dual
cones as `ProperCone ℝ (Λ →₀ ℝ)`. Touches the existing structure
on `confinement-nf-partial-proof.lean` — needs sibling-PR
coordination with #564 owner.

### Step 2: Discharge `dualityGapZero` via Farkas + inner-dual

Strong duality reduces to: for any feasible primal/dual pair,
`primal_obj ≤ dual_obj` (weak duality, easy) **and** the
optimum is attained on the boundary of both cones (hard part —
requires Farkas-derived alternative theorem).

Mathlib's [`Mathlib.Analysis.Convex.Cone.InnerDual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Cone/InnerDual.html)
provides the **Farkas alternative** in conic form, but applying
it to our finite LP requires:

1. Show the primal feasible set is a non-empty polyhedron (uses
   `OperatorSelectionLP.feasible_holds`).
2. Show the primal is bounded above on this polyhedron (uses
   `bounded_holds`).
3. Apply Farkas to extract a dual-feasible point with
   `dual_obj = primal_obj`.

**Effort:** ~50–80 lines of Lean using `InnerDual.lean` API.

### Step 3: Discharge `complementarySlackness` via the Farkas certificate

Complementary slackness drops out of strong duality + the explicit
form of the Farkas certificate (the dual variable $y$ satisfies
$y_\lambda > 0 \iff$ primal constraint at $\lambda$ is tight).

**Effort:** ~30 lines of Lean if Step 2 lands the right
certificate; otherwise ~80 lines.

### Total estimate

**1–2 weeks** of focused Lean development by someone fluent in
Mathlib's `Convex.Cone.*` API. Out of scope for a single session.

## Interim: §3b-cond hypothesis class

The interim solution (landed in this PR via
[`def:lp-duality-hypothesis-class`](../../content/quantum-observable-universe/braids-and-knots/lp-duality-hypothesis-class.md))
relocates the two `sorry`s from free-standing top-level theorems
in `confinement-nf-partial-proof.lean` to **two fields of a class
trivial-model**, with proper `-- Ref: [schrijver1986theory]`
citations per AGENTS.md §1.

When the Mathlib wiring lands, the interim class instance can be
swapped for a `mathlibModel` that discharges both fields
unconditionally — zero edits to consumer code.

## Recommended owner

This task fits naturally into **#565 F11 scope** (CI workflow + LP
gating) or a **standalone Mathlib-wiring PR**. It does NOT fit into
#572 (this PR's branch), which is scoped to crystal-R-matrix
follow-ups from #567.

## Cross-references

- [`def:lp-duality-hypothesis-class`](../../content/quantum-observable-universe/braids-and-knots/lp-duality-hypothesis-class.md) — interim §3b-cond class
- [`prop:confinement-nf-partial-proof`](../../content/quantum-observable-universe/braids-and-knots/confinement-nf-partial-proof.md) — consumer (two `sorry`s)
- [`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md) — LP definition
- [Mathlib `Cone.InnerDual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Cone/InnerDual.html) — Farkas + inner-dual
- [Schrijver (1986). Theory of Linear and Integer Programming](https://www.wiley.com/en-us/Theory+of+Linear+and+Integer+Programming-p-9780471982326) — §7.2 + §7.4 are the target results

Sources:
- [Mathlib4: Mathlib.Analysis.Convex.Cone.InnerDual](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Cone/InnerDual.html)
- [Strong Duality — Burke, Math 407, UW](https://sites.math.washington.edu/~burke/crs/407/lectures/L9-strong-duality.pdf)
- [Complementary Slackness — Anstee, UBC](https://personal.math.ubc.ca/~anstee/math340/340complementaryslackness.pdf)
