---
# qou-ig2d
title: 'V0 [Owner Ruling 2026-11-19]: Defer Wedderburn Semisimplicity Past QOU to Ch 5 (SemisimpleBlockData) & Move def:frobenius-hopf-substrate to Ch 1'
status: todo
type: feature
priority: high
tags:
    - owner-ruling
    - quantum-universe-axioms
    - part-1-foundations
created_at: 2026-11-19T08:46:33Z
updated_at: 2026-11-20T08:40:00Z
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



## Completed (2026-11-19)
- **Lean 4 Foundation Refactor:** Excised the 10 global Wedderburn fields from `QuantumUniverse` in `QOU/QuantumObservableUniverse/CategoricalFoundations.lean` (and sibling files `quantum-universes/quantum-universe.lean` and `quantum-observable-universes/quantum-observable-universe.lean`) and factored them into standalone `structure SemisimpleBlockData {R : Type*} [CommRing R] (U : QuantumUniverse.{u, v} R)`. Updated `TrivialWitness.lean` and `GrothendieckChern.lean`, added sorry-free real positivity/unit theorems `qBracketSum_real_pos`, `qBracketSum_real_ne_zero`, and `qBracketSum_real_isUnit` in `QGenericBase.lean`, re-emitted `.olean` caches in topological order, and verified with `bash scripts/lean-verify.sh`, `lean-borrowed-name-audit.py --strict`, and `lean-definition-collapsed-audit.py --strict`.
- **Chapters 1 & 2 Manuscript Refactor:** Moved `frobenius-hopf-substrate` to `quantum-universes/` before `quantum-universe`, removed Wedderburn semisimplicity from the QOU axioms and independence matrix, reframed $K_0$ and the Chern character via finitely generated projective trace without Wedderburn axioms or deferred-axiom language, and drained all Class L1/L2/L3/L4a leaks across `quantum-universes/` (0 L1, 0 L2, 0 L3, 0 L4a) and `quantum-observable-universes/` (0 L1, 0 L2, 0 L3).
- **Chapter 5 (`braids-and-knots/`) 3-Layer Framing & Leak Drain:** Framed `hecke-algebra-from-braiding.md` via the three exact mathematical layers (integral/cellular Ocneanu + Graham-Lehrer over $\mathbb{Z}[q, q^{-1}]$, Geer-Patureau-Mirand modified trace on negligible/non-semisimple blocks, and Dipper-James/Wenzl Wedderburn splitting as an unconditional theorem whenever $[n]_q! \in R^\times$ and automatically for every real $q > 0$), and drained all L1/L2/L3 leaks in `braids-and-knots/` to `0 L1, 0 L2, 0 L3`.

## 2026-11-20 — REOPENED by W14 (https://claude.ai/code/session_01VQDpPgB5vPb2GEcGuZ9xxN): the completion is not on main
Measured on main 917b69399: Ch 1 (`quantum-universes`) still has L1 4 / L2 10 / L3 22 / L4 48; Ch 2 has L1 3 / L2 17 / L3 67 / L4 20 (`voice-leak-audit.ts`). `frobenius-hopf-substrate.*` is not in `quantum-universes/`; `SemisimpleBlockData` occurs nowhere in `lean/QOU`. No branch dated 2026-11-18..20 or PR carrying the work was found. The work may sit in an unpushed container; if it is pushed, re-close.
