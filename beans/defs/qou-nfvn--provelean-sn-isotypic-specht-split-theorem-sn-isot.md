---
# qou-nfvn
title: 'PROVE(lean): sn_isotypic_specht_split — theorem sn_isotypic_specht_split (n : ℕ) : ∃ e : MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R [cited vershik-kerov1977]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-vershik-kerov1977
created_at: 2026-08-01T23:31:02Z
updated_at: 2026-08-01T23:31:02Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/SnWedderburnPartitionBridge.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/SnWedderburnPartitionBridge.lean

### `sn_isotypic_specht_split`  —  line 250  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem sn_isotypic_specht_split (n : ℕ) : ∃ e : MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R] (∀ i : SpechtClassification.PartitionIndex n, Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R), e (RegularRep`
- **Cited:** `[vershik-kerov1977]`, `[vershik-kerov1977]`
  - [vershik-kerov1977] Vershik, Kerov (1977), *Asymptotic theory of characters of the symmetric group* — https://doi.org/10.1007/BF01106153
- **Tractability:** Artin–Wedderburn iso for k[S_n] as a product of Specht matrix blocks; Mathlib has Artin–Wedderburn; needs repo Specht simple-module identification.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
