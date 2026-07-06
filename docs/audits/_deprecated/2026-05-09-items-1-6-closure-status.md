> **DEPRECATED on 2026-05-24.** Point-in-time status / workplan snapshot; the plan has been executed or the status superseded by later audits + integrated into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T3 for the deprecation rationale.

# Items 1–6 closure status (2026-05-09, post-PR586)

User asked to close items 1, 2, 3, 5, 6 from the offered list. This
audit records what landed in this branch (`claude/close-items-1-2-3-5-6`)
and what remains tracked but undelivered.

## Item 5 — `Cl_2_DoubleAngle` boundary instances (DELIVERED)

Two new sorry-free boundary checks in
[`upstream-mathlib-additions.lean`](../../content/quantum-observable-universe/descartes-universe/upstream-mathlib-additions.lean):

- `Cl_2_double_angle_at_pi_unconditional` — at `θ = π`, both sides
  reduce to `0` via `Cl_2_periodic` (LHS: `Cl_2(2π) = Cl_2(0) = 0`)
  and `Cl_2_pi` + `Cl_2_zero` (RHS).
- `Cl_2_double_angle_at_pi_half_unconditional` — at `θ = π/2`, the
  identity becomes the tautology `Cl_2(π) = 2·Cl_2(π/2) - 2·Cl_2(π/2)`,
  closed by `Cl_2_pi` and arithmetic.

Both proofs are unconditional (no `[Cl_2_DoubleAngle]` instance
needed); they are the only three boundary points (with `θ = 0`,
already present) at which the double-angle identity collapses to
known closed-form values of `Cl_2`. The full open-locus instance
remains a Mathlib upstream gap (Spence-Lewin functional equation).

## Item 6 — One-voice / dangling-remark sweep (CLEAN)

- `bun run pipeline/find-dangling-remarks.ts`: 465 remarks total,
  442 backed + 23 glossary, **0 dangling**.
- `bun run validate quantum-observable-universe`: **0 issues**.

No fixes required. Snapshot for record.

## Item 1 — α_5 derivation (TRACKED, NOT DELIVERED)

α_5 is currently a fit parameter in
[`shell-correction-term-seven.md`](../../content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.md).
Closure pathway:

1. Run `gb_filtration_jet_tracker.py` with PR #586's H_n ≥ 4
   extension (currently only on `claude/item3-mathlib-tier-a-batch`).
2. For each atom A ∈ {2..6}, compute χ^λ(T_w) at the canonical
   T_w for the height-6 partitions enumerated by
   [`term7_height6_partition_enum.py`](../../computations/term7_height6_partition_enum.py).
3. Sum w_λ · χ^λ(T_w) to evaluate χ_5(T_w) per atom.
4. Fit the single ratio α_5 = (Term-7 contribution) / χ_5 from the
   AME residual; verify constancy across A.

Step 2 requires Hoefsmit seminormal-form characters at non-trivial
braid words — research-grade compute already scaffolded in
[`hoefsmit-seminormal-form.ts`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.ts)
but not yet wired through the tracker.

**Net state**: structural pathway documented, full numerical
delivery is a separate batch.

## Items 2, 3 — Tier-A True-predicate upgrades (TRACKED, NOT DELIVERED)

[`categorical-linking-operation.lean`](../../content/quantum-observable-universe/braids-and-knots/categorical-linking-operation.lean)
and [`hoefsmit-ew-cell-content.lean`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-ew-cell-content.lean)
both contain `def Foo (_) : Prop := True` predicates, conditionally
discharged by `theorem foo_holds := trivial`. The substantive
upgrade — replacing `True` with the actual categorical statement —
requires:

- **Item 2 (linking #3 post-trace multiplicativity)**: the
  pre-trace identity `c^{k₁+k₂} = c^{k₂} ∘ c^{k₁}` is generic
  monoidal-category structure (already noted in the existing
  comment). The post-trace upgrade requires a substrate-specific
  Markov-trace cyclicity identity discharging `tr_M(c^k) =
  tr_M(c^{-k})` modulo a known sign. That cyclicity statement
  lives downstream of `prop:frobenius-gram-matrix`; promoting
  the predicate is theorem-bound on existing scaffolding.

- **Item 3 (Hoefsmit `DisjointStrandPairAssignmentB6`)**: structural
  content is far-commutativity at n = 6, i.e. `σ_1, σ_3, σ_5`
  pairwise commute in B_6 by the `|i - j| ≥ 2` braid axiom.
  Upgrading requires a Lean-level `BraidGroup` formalization
  that exposes the far-commutativity axiom; the manuscript-level
  witness `hoefsmit-ew-cell-content.witness.json` already records
  this as established. Theorem-bound on Mathlib `BraidGroup`
  uptake.

Both upgrades are smaller than they look but require substrate
plumbing (Markov-trace cyclicity, `BraidGroup` predicates) that is
not in scope for a single batched commit.

## Summary

| Item | State | Action |
|------|-------|--------|
| 1 — α_5 derived | Tracked | Pathway documented; needs PR #586 + Hoefsmit χ |
| 2 — Linking #3 post-trace | Tracked | Needs Markov-cyclicity discharge |
| 3 — Hoefsmit assignment | Tracked | Needs `BraidGroup` plumbing |
| 5 — Cl_2 boundary | **Delivered** | 2 new unconditional theorems |
| 6 — Dangling remarks | **Clean** | 0 dangling, 0 validation issues |

Net deliverable: 2 sorry-free Lean theorems + audit snapshot.
