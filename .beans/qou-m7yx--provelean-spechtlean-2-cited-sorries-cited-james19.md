---
# qou-m7yx
title: 'PROVE(lean): Specht.lean — 2 cited sorries [cited james1984representation,sagan2001]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-james1984representation
    - cite-sagan2001
created_at: 2026-08-01T23:31:02Z
updated_at: 2026-08-01T23:31:02Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/Specht.lean` (QOU)  ·  2 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/Specht.lean

### `specht_finrank_eq_numSYT`  —  line 313  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem specht_finrank_eq_numSYT {k : Type} [Field k] (μ : YoungDiagram) : Module.finrank k (SpechtSubmodule (k := k) μ) = QOU.BraidKnot.numSYT μ `
- **Cited:** `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** dim S^μ = #SYT μ; the standard-basis core is now sorry-free in-repo — needs wiring, no Mathlib gap.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `specht_isSimple`  —  line 328  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem specht_isSimple {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) (hμ : μ.card ≠ 0) : -- nonempty diagram; ℕ-nonemptiness, not ring ordering (§7c-clean) ∀ N : Submodule k (Mtab (k := k) μ), N ≤ SpechtSubmodule (k := k) μ → (∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ N, Mtab.rep μ σ x ∈ N) → N `
- **Cited:** `[james1984representation]`
  - [james1984representation] James, Kerber (1984), *The Representation Theory of the Symmetric Group* — (no DOI/URL)
- **Tractability:** Specht module is simple in char 0 (James submodule theorem); repo Specht theory, self-contained.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
