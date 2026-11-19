---
# qou-ig2d
title: 'V0 [Owner Ruling 2026-11-19]: Defer Wedderburn Semisimplicity Past QOU to Ch 5 (SemisimpleBlockData) & Move def:frobenius-hopf-substrate to Ch 1'
status: in-progress
type: feature
priority: high
tags:
    - owner-ruling
    - quantum-universe-axioms
    - part-1-foundations
created_at: 2026-11-19T08:46:33Z
updated_at: 2026-11-19T08:46:33Z
parent: qou-d4kh
---

## Owner Ruling (2026-11-19)

**"Deferring Wedderburn semisimplicity past QOU to Chapter 5."**

Cross-linked beans: `qou-d4kh` (parent epic), `qou-x4nh` (*V2 Part I Foundations Drain*).

---

## Architectural Decisions & Execution Plan

1. **Lean 4 Refactor (`CategoricalFoundations.lean`, `TrivialWitness.lean`, `GrothendieckChern.lean`, `QGenericBase.lean`, plus sibling `.lean` files):**
   - Remove the 10 global finite Wedderburn fields (`blocks`, `blocksFintype`, `centralIdem`, `centralIdem_idem`, `centralIdem_orthogonal`, `centralIdem_complete`, `frobWeight`, `frobWeight_isUnit`, `dimQ`, `dimQ_isUnit`) from `QuantumUniverse` (so neither `QuantumUniverse` nor `QuantumObservableUniverse` imposes global finite Wedderburn semisimplicity on all of $A$, allowing infinite Peter–Weyl coordinate algebras such as $\mathcal{O}(\mathrm{SU}(2))$ and nilpotent jet thickenings to satisfy the QU/QOU axioms directly).
   - Define `structure SemisimpleBlockData {R : Type*} [CommRing R] (U : QuantumUniverse.{u, v} R)` in `QOU/QuantumObservableUniverse/CategoricalFoundations.lean` carrying those exact orthogonal central idempotent + unit `frobWeight`/`dimQ` fields for any finite semisimple substrate or $n$-strand Hecke quotient slice $H_n(q)$.
   - Update `TrivialWitness.lean` (providing both the 3-axiom `QuantumUniverse` witness and its `SemisimpleBlockData` instance), `GrothendieckChern.lean` (taking `(W : SemisimpleBlockData U)` on the block-basis definitions/theorems), `QGenericBase.lean`, and all chapter sibling `.lean` files (`quantum-universes/quantum-universe.lean`, `quantum-observable-universes/quantum-observable-universe.lean`, `quantum-universes/chern-character.lean`, `quantum-universes/grothendieck-group-of-a-qou.lean`, etc.).

2. **Move `def:frobenius-hopf-substrate` to Chapter 1 Before `def:quantum-universe`:**
   - Move `frobenius-hopf-substrate.{md,ts,lean,qa.json,jsonld}` from `quantum-observable-universes/` into `quantum-universes/` and wire `"frobenius-hopf-substrate"` into `quantum-universes.ts` right before `"quantum-universe"` in `sec:quantum-universe`, eliminating the cross-chapter forward reference at `quantum-universe.md:4`.

3. **3-Axiom `def:quantum-universe` & Deferral of Cyclotomic Generic Ring to Chapter 5 (`braids-and-knots`):**
   - Update `quantum-universes/quantum-universe.md` to state the 3 axioms (**Temporal braiding**, **Frobenius–Hopf substrate action**, **Symmetric Frobenius trace** + $\Omega^1(A)$), removing Axiom 4 and relocating the cyclotomic generic ring $R = \mathbb{Z}[q, q^{-1}][\Phi_d(q)^{-1} : d \ge 2]$ discussion to Chapter 5 (`braids-and-knots`) where Hecke Wedderburn semisimplicity and $[m]_q$ unit conditions are introduced.
   - Update Chapter 1 consumers (`quantum-universe-axiom-motivation.md`, `quantum-universe-exists.md`, `axiom-independence.md`, `grothendieck-group-of-a-qou.md`, `chern-character.md`) and drain all Class L1, Class L2, and Ch-1 Class L3 leaks in Chapters 1 and 2.
