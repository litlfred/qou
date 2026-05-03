# τ̂_n Lean scaffold audit — zero sorrys; gap is Python realisation

**Date:** 2026-05-03
**Branch:** `claude/tau-hat-n-lean-audit`
**Goal:** audit the existing Lean scaffold for τ̂_n and identify the
most tractable `sorry` to discharge (PR #531 follow-up).

## Verdict: **all three τ̂_n Lean files are already sorry-free.**

The full Lean scaffold for the descent involution + jet prolongation
+ recursive brane tower stack is fully proved at the abstract level.
Nothing to discharge.

| File | Lines | Decls | `sorry` count |
|---|---:|---:|---:|
| `content/quantum-observable-universe/lifting-and-descent/recursive-brane-tower.lean` | 44 | 1 structure | **0** |
| `content/quantum-observable-universe/lifting-and-descent/descent-involution.lean` | 43 | 1 structure + 1 theorem | **0** |
| `content/quantum-observable-universe/lifting-and-descent/jet-prolongation.lean` | 86 | 1 structure + 1 theorem | **0** |

## What's there

### `RecursiveBraneTower` (recursive-brane-tower.lean:26)

A typeclass packaging:
- `level : ℕ → Type*` — the level-n module
- `ascent  : ∀ n, level n →ₗ[R] level (n+1)` — ℓ_n
- `descent : ∀ n, level (n+1) →ₗ[R] level n` — 𝔡_{n+1}
- `retraction : ∀ n, descent n ∘ ascent n = id` — the splitting axiom

### `DescentInvolution` (descent-involution.lean:26) + idempotence theorem

A typeclass with `tau := ascent ∘ descent` defined explicitly.
Then `DescentInvolution.tau_idem` (descent-involution.lean:38–41)
proves `τ ∘ τ = τ` via `ext x; simp [tau, comp_apply, retraction]` —
exactly the calculation in `descent-involution.md` lines 21–30.

### `JetProlongation` (jet-prolongation.lean:39) + observability theorem

A categorical typeclass packaging J¹(A) = A ⊗ Ω¹(A) with the
inherited Frobenius–Hopf structure, plus
`jet_prolongation_preserves_observability` (line 74) proving that
adjoint vanishing on A passes to J¹(A).

## Where the actual gap lives

The Lean scaffold is **abstract**: it defines structures and proves
their general properties. What is **not** in the scaffold is any
**concrete instance** at q = q₀ for a specific Hecke algebra (e.g.
`H_3(q₀)` for the proton).

Concretely, to compute level-1 Φ_q for the proton and unblock Phase
A.3 of issue #522, what's needed is:

1. **A concrete `RecursiveBraneTower` instance** with
   `level 0 = H_3(q₀)`, the explicit ascent ℓ_0 (canonical
   inclusion via the unit section), and the explicit descent 𝔡_1
   (the retraction).
2. **A concrete `DescentInvolution` instance** built from #1, giving
   τ̂_0 as a finite-dimensional linear map.
3. **A `JetProlongation` instance** at A=1 — the categorical
   structure on H_3(q₀) ⊗ Ω¹(H_3(q₀)) — required for the pentagon
   q-factor theorem on the transient block.

These instances are **Python-realisable** (the linear-algebra parts;
finite-dim, mpmath-friendly) and **Lean-formalisable** (would need
Mathlib's `LinearAlgebra` + the QOU `FrobeniusHopfData` instance for
H_n(q)). Neither is currently in the codebase.

## Tractable-discharge candidates: NONE

Scanned all three files for `sorry`s. None exist. The audit's
secondary goal (discharge the most tractable sorry) is **vacuously
satisfied** — there are no candidates.

## Recommendation

**Phase A.3 is not blocked on Lean discharges.** It's blocked on
**a concrete Python realisation** at A=1, plus optionally an
explicit Lean instance.

The most actionable next steps are:

1. (parallel sibling task) **τ̂_0 proton-scale numerical realisation**
   in Python — building H_3(q₀) ⊗ Ω¹(H_3(q₀)), computing τ̂_0 as a
   matrix, verifying idempotence, splitting End(A_1) into
   eigenspaces. (Currently in a sibling worktree.)
2. (later) **Lean instance discharge** — once the Python realisation
   confirms the structure works numerically, formalise the H_3(q₀)
   instance of `RecursiveBraneTower`. Builds on Mathlib's
   `LinearAlgebra` + the existing `QOU.FrobeniusHopfData` infra.

## Files

- Audit memo: this file
- Witness: [`folio-assistant/computations/tau-hat-n-lean-scaffold-audit.witness.json`](../../folio-assistant/computations/tau-hat-n-lean-scaffold-audit.witness.json)
- Scaffolds audited (no changes):
  - [`recursive-brane-tower.lean`](../../content/quantum-observable-universe/lifting-and-descent/recursive-brane-tower.lean)
  - [`descent-involution.lean`](../../content/quantum-observable-universe/lifting-and-descent/descent-involution.lean)
  - [`jet-prolongation.lean`](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation.lean)

## Status

**Audit-complete-no-sorrys.** The Lean scaffold is in good shape; the
real Phase A.3 work is the concrete Python instance (sibling task in
progress).
