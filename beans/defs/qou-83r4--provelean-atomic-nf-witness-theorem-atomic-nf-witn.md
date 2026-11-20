---
# qou-83r4
title: 'PROVE(lean): atomic_nf_witness — theorem atomic_nf_witness (ctx : AtomicNfWitnessContext) : (∀ π : ℕ, ctx.Phi_1 ctx.pi_star [cited manuscript]'
status: todo
type: task
priority: normal
tags:
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/atomic_nf_witness.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_nf_witness.lean

### `atomic_nf_witness`  —  line 90  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem atomic_nf_witness (ctx : AtomicNfWitnessContext) : (∀ π : ℕ, ctx.Phi_1 ctx.pi_star ≤ ctx.Phi_1 π) ∧ (∀ p : ℕ, ctx.Phi_1_electron ctx.electron_pos_star ≤ ctx.Phi_1_electron p) ∧ (∀ k : ℕ, ctx.gb_converges k) ∧ (∀ a : ℕ, a ≤ 9 → ctx.NF_no_strip a) ∧ ctx.F_Pauli = |ctx.trAlt / ctx.net| `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/particle-interactions/atomic-nf-witness.ts
- **Tractability:** GS convergence + Φ-minimality witness for the atomic normal form; repo GS/optimisation infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8296, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
