---
# qou-jbfx
title: 'Provable once infra exists: the LES results and what each would buy'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:14:28Z
updated_at: 2026-10-04T15:26:00Z
parent: 08a2
---

Blocked on `qou-pan0`. Recorded now so the payoff is costed **before** anyone
builds infrastructure, not after.

## 1. GB-filtration spectral sequence collapses at E₂  — needs algebraic SS

The one the corpus actually claims (`S-GB-spectral-collapse`). Once `E_r` pages
exist over `HomologicalComplex`, `CollapsesAt 2` becomes a theorem about the
Gröbner filtration rather than a class hypothesis discharged by `PUnit`
(`qou-fngs`).

**What it buys:** `E_2 = E_∞` means the associated graded of the filtration
*is* the answer — the Wedderburn block decomposition computes the thing with no
higher corrections. Every "vanishing" claim downstream becomes "the differential
out of this bidegree is zero", which is checkable per cell.

## 2. Homotopy LES of `SU(2) → SU(3) → S⁵`  — needs fibration LES

**What it buys, honestly: less than it looks.** `qou-ko4g` shows `SU(2)` is not
normal in `SU(3)`, so there is no extension to compute; the fibration is a
statement about *spaces*, and gives `π₃SU(3) ≅ π₃SU(2) ≅ ℤ` and `π₅SU(3) ≅ ℤ`.
Useful for instanton number / Chern–Simons level bookkeeping, **not** for
getting colour out of the tetraplectic triad. Costed low deliberately.

## 3. Seidel-style exact triangle for the twist  — needs symplectic topology

The real prize and the one that is decades away. `library/arxiv-math-0105186v2/0105186v2.pdf`
(Seidel, *A long exact sequence for symplectic Floer cohomology*) gives

    HF(L₀,L₁) → HF(L₀, τ_L L₁) → HF(L₀,L) ⊗ HF(L,L₁) → [1]

for `τ_L` the Dehn twist along a Lagrangian sphere.

**What it buys:** the error term is **supported on the sphere**. That is
localised obstruction control — twisting changes cohomology by something you
can compute at one place, and if `HF(L₀,L) = 0` the twist acts invertibly.
That is the shape the framework wants for its own twist `[M_i,M_j] = 2M_k`.

**The usable half is available today**: item 5 of `qou-ko4g` is the abstract
exact-triangle vanishing lemma — same bookkeeping, pure homological algebra, no
Floer theory. Build the reasoning pattern there; swap in real Floer cohomology
if it ever exists.

## 4. `G₂/SO(4)` and `G₂/SU(3) = S⁶` in one frame  — needs octonions/G₂

**What it buys:** the two structures the corpus juggles are the two subgroups of
G₂ giving its two homogeneous spaces, with `8 + 6 = 14`. That dimension count is
provable today (`qou-ko4g`); the *geometry* needs G₂. The corpus has `S⁶` and
**no mention of `G₂/SO(4)`** — so this is the missing half of the picture, not a
refinement of it.

## Round 90 Lean 4 + 80-dps Witness Formalization (PR #8481)
- Module: `QOU.Foundations.MachineryConjectureCarrierRegistryThreeBatchDefectDrainDoubleCentralizerBalanceLongExactSequencePayoffParallelogramArgumentPrinciple`
- Commit 1 (code + probe): `a9f0f1224d140032ab84905edb79a825b0ec07fe`
- Commit 2 (`.witness.json`): `2e6c78442e063cad6ad9aa9c49b55c365f4be789`
- PR: https://github.com/litlfred/qou/pull/8481
