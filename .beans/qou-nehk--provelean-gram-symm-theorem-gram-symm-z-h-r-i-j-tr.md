---
# qou-nehk
title: 'PROVE(lean): gram_symm — theorem gram_symm (z h : R) : ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-22T09:34:22Z
parent: qou-k1mq
---

**File:** `QOU/Machinery/MarkovTraceH4.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceH4.lean

### `gram_symm`  —  line 185  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem gram_symm (z h : R) : ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j) (e i)) `
- **Cited:** `[manuscript]`
  - [manuscript] §mass-theory
- **Tractability:** trM(ab)=trM(ba) cyclicity over the H4 normal-form multiplication; concrete algebra, heavy but repo-internal (candidate decide/ring).
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.


## STALE — the cited sorry no longer exists (verified 2026-08-22)

Closed on evidence, not on work done under this bean. The target was
`gram_symm` at `QOU/Machinery/MarkovTraceH4.lean:185`, catalogued as 1 cited
sorry on 2026-08-01. On `main` today that file has **zero** real `sorry`, and
its own header says why:

> `QOU.Machinery.MarkovTraceH4Gram` from `gram_symm` over the 576-entry ...
> `trM_cyclic_of_gram_symm` below is **kept**: it is the sorry-free reduction
> ... `BilinearTraceCyclicity.cyclic_of_gram_symm`.

i.e. the sorry was discharged by the 576-entry Gram closure and the reduction
through `BilinearTraceCyclicity`, not left open. Whole cluster is sorry-free:
`MarkovTraceH4`, `H4Cyclicity`, `H4GeneratorAction`, `HeckeH4RepDecomp`,
`BilinearTraceRepBasis`, `BilinearTraceCyclicity` — 0 real `sorry` in all six.

**What is still open is a different thing, and is already tracked elsewhere.**
`HeckeH4RepDecomp.trM4_gram_symm_of_markov_basis` is a *conditional* result:
Gram symmetry follows from the 24 basis-level Markov identities carried as the
explicit hypothesis `hbasis`. That file states this itself and names the owner —
`qou-x64l` step 4. Conditional-proved is not premise-established, so do not read
"the cluster is sorry-free" as "the Wedderburn route is unconditional". The
enumerated 576-entry route IS unconditional; the structural one is not yet.
