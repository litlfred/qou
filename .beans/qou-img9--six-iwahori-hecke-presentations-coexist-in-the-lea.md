---
# qou-img9
title: Six Iwahori-Hecke presentations coexist in the Lean tree
status: todo
type: task
created_at: 2026-08-30T04:13:13Z
updated_at: 2026-08-30T04:13:13Z
---

Measured 2026-08-30 with

    grep -rn "def IwahoriHecke\|structure IwahoriHecke\|abbrev IwahoriHecke" --include=*.lean content/

| declaration | file | shape |
|---|---|---|
| `IwahoriHecke W R q` | `QOU/IwahoriHecke/Defn.lean` | quotient over `Set.univ : Set W` — the `qou-b5gu` defect: it imposes the quadratic relation on **every** group element, but `T_w` satisfies it only when `ℓ(w) = 1` |
| `IwahoriHeckeQuot` | `QOU/IwahoriHecke/Quotient.lean` | the underlying quotient of the above |
| `IwahoriHeckeOfSn` | `QOU/IwahoriHecke/TypeA.lean` | type-A specialisation of the above |
| `IwahoriHeckeAlgebra n R` | `QOU/BraidKnot/IwahoriHeckeAPI.lean` | a `structure`, not a quotient |
| `IwahoriHecke K q n` | `QOU/Hecke/IwahoriHecke.lean` | `RingQuot` on `Fin n` generators — what PR #6053's `T_w` programme builds on |
| `HeckeAlgebra R q M` | `QOU/MathlibExt/IwahoriHeckeAlgebra.lean` | general Coxeter matrix, ℕ-indexed type A, with `lift` / `hom_ext` / `exists_unique_lift` (PR #6055) |

Found while answering a sibling's coordination comment on #6053, which named two
of the six and asked whether the `Set.univ` one should be repaired or retired.

## Why this matters beyond tidiness

Conventions differ across them. `QOU/Hecke/IwahoriHecke.lean` uses
`σ² = (q−1)σ + q`, i.e. Iwahori normalisation `(σ − q)(σ + 1) = 0`. AGENTS.md
§7a states the corpus convention as the Hecke-skein `σ² = (q − q⁻¹)σ + 1`.
Those are different normalisations, related by `σ_skein = q⁻¹ σ_Iwahori` at
`Q = q²`. So a result proved against one presentation is not automatically a
result about the object the paper names, and nothing currently flags a
cross-presentation citation.

`QOU/MathlibExt/HeckeIwahoriConventionBridge.lean` (#6055) crosses one such
pair. There is no map between the other presentations at all.

## Recommendation (judgement, not a finding)

Retire rather than repair the `Set.univ` family. Re-indexing
`QOU/IwahoriHecke/Defn.lean` by simple reflections produces a *seventh* correct
presentation rather than removing a wrong one; `QOU/Hecke/IwahoriHecke.lean`
already is that object for type A, and `QOU/MathlibExt/IwahoriHeckeAlgebra.lean`
already is it for a general Coxeter matrix. Before retiring, count the
downstream consumers of each — not done here.

Not started. No consolidation attempted on any branch.
