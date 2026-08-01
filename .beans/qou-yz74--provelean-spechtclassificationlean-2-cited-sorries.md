---
# qou-yz74
title: 'PROVE(lean): SpechtClassification.lean — 2 cited sorries [cited james1984representation,sagan2001]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-james1984representation
    - cite-sagan2001
created_at: 2026-08-01T23:31:03Z
updated_at: 2026-08-01T23:31:03Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/SpechtClassification.lean` (QOU)  ·  2 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtClassification.lean

### `spechtIso_imp_dom_both`  —  line 454  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem spechtIso_imp_dom_both {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν) (_hiso : IsRepIso (k := k) (spechtRep (k := k) μ) (spechtRepOn (k := k) h)) : partitionDom μ ν ∧ partitionDom ν μ `
- **Cited:** `[james1984representation]`, `[james1984representation]`
  - [james1984representation] James, Kerber (1984), *The Representation Theory of the Symmetric Group* — (no DOI/URL)
- **Tractability:** Specht iso ⇒ mutual dominance of the two diagrams; repo Specht classification.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `specht_exhausts_irreducibles`  —  line 494  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem specht_exhausts_irreducibles {n : ℕ} {W : Type} [AddCommGroup W] [Module k W] (ρ : Representation k (Perm (Fin n)) W) (_hsimple : IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule) : ∃ (μ : YoungDiagram) (h : Specht.nOf μ = n), IsRepIso (k := k) ρ ((spechtRep (k := k) μ).comp (trans`
- **Cited:** `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Every simple k[S_n]-module is a Specht module (exhaustion); repo Specht classification + Wedderburn count.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
