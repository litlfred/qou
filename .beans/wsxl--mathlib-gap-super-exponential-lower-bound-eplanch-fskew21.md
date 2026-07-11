---
# wsxl
title: 'Mathlib-gap: prove the super-exponential lower bound on w_std(k)=E_Planch[f^{lambda/(2,1)}] (closes GAP-A-3 level-selection conditional)'
status: todo
type: task
priority: normal
created_at: 2026-07-11T18:45:00Z
updated_at: 2026-07-11T18:45:00Z
---

## What

Discharge the one open input of `QOU/Mass/LevelSelectionLogarithmic.lean`
(formalized as the conditional GAP-A-3 result in PR #3568, open at time of
seeding): the §3b conjecture class
`TowerGeometricLowerBound` — a super-exponential (a fortiori geometric)
**lower bound** on the branched tower weight

    w_std(k) = Σ_{λ⊢k, λ⊇(2,1)} W_λ · f^{λ/(2,1)} = E_Planch[ f^{λ/(2,1)} ]   (at q=1, ΣW_λ=1)

= the Plancherel-expected number of standard skew tableaux of shape λ/(2,1).
Proving `∀ k, c·r^k ≤ w_std(k)` (r>1, c>0) upgrades `level_geometric_bound` /
`linear_selection_bound` from *conditional* to *unconditional*, so the
level-selection rule k(A) is proved logarithmic (k∝A, k∝bond-count excluded)
outright.

## Status

- **Numerically verified, NOT proved.** Exact-integer, k≤10: successive ratios
  strictly increasing (1.38→2.88, super-exponential / factorial class); q₀
  preserves the class. Witness: `computations/deltalambda/wlambda-wstd-growth-bound.witness.json`
  (probe `wlambda_wstd_growth_bound_probe.py`).
- **Faithful Lean proof = Mathlib gap.** Needs SYT + skew-tableau (`f^{λ/μ}`) +
  Plancherel-measure infrastructure that is not in Mathlib in usable form —
  a multi-session build, NOT a single lemma. Do NOT fabricate an instance
  (audit-dodge; AGENTS.md §"Axiomatization is NOT a Proof").

## Candidate proof route (recorded so a future session need not re-derive)

A Cauchy–Schwarz + falling-factorial identity gives a super-exponential lower
bound WITHOUT full asymptotics:

1. **Identity (single-f):** `Σ_{λ⊢k} f^λ · f^{λ/μ} = (k!/m!)·f^μ`, `m=|μ|`.
   For μ=(2,1): `Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3` (f^{(2,1)}=2, m=3).
   [verified numerically here; standard branching identity.]
2. **Cauchy–Schwarz:** `(Σ_λ f^λ f^{λ/(2,1)})² ≤ (Σ_λ (f^λ)² f^{λ/(2,1)})·(Σ_λ f^{λ/(2,1)})`.
   ⇒ `Σ_λ (f^λ)² f^{λ/(2,1)} ≥ (k!/3)² / (Σ_λ f^{λ/(2,1)})`.
3. **Denominator bound:** `Σ_{λ⊢k} f^{λ/(2,1)}` = #up-paths of length k−3 from (2,1)
   in Young's lattice ≤ ∏_{j=3}^{k-1}(#addable corners of a size-j partition)
   ≤ ∏ O(√j) = O(√(k!)·poly). [needs an addable-corner ≤ c·√j bound.]
4. ⇒ `w_std(k)|_{q=1} = (1/k!)·Σ_λ (f^λ)² f^{λ/(2,1)} ≥ (k!/9)/(√(k!)·poly) = √(k!)/poly`
   → super-exponential. Even a WEAKER geometric bound `c·r^k` suffices for the
   downstream theorem (`level_geometric_bound` only needs `r>1`).

The Mathlib gap is: `f^{λ/μ}` (skew hook-length / SYT count), the branching
identity in step 1, and the addable-corner bound in step 3. A `q≠1` (q-deformed)
version needs `d_q`/`[k]_q!`; but the downstream theorem is stated over generic
`ℝ` with the bound as a hypothesis, so proving the `q=1` (real) bound + the
`q₀`-preserves-class fact (probe-verified) discharges the class instance for the
substrate.

## Files / anchors

- Lean (conditional, PR #3568 — open at seeding, not yet on `main`): `content/quantum-observable-universe/lean/QOU/Mass/LevelSelectionLogarithmic.lean`
- Structural note: `docs/audits/2026-07-11-wlambda-level-selection-log-structural.md`
- Keystone cross-link (C8 gate): `docs/audits/2026-07-11-keystone-wlambda-superexp-necessary-condition.md`
- Probe + witness: `computations/deltalambda/wlambda_wstd_growth_bound_probe.py`

## Definition of done

`TowerGeometricLowerBound (w_std) r c` has a **proved** instance (sorry-free) for
some concrete `r>1, c>0` at the substrate — OR a rigorous symbolic argument that
the corpus accepts in lieu of full Mathlib SYT infra — at which point the GAP-A-3
level-selection conditional theorems become unconditional. Advance only via
genuine derivation; not a fit.
