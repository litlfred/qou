---
# qou-x4nh
title: 'V2 [Part I Foundations Drain]: Fix All L1-L4 Lean, Voice & Anachronism Leaks in Ch 1 (quantum-universes) & Ch 2 (quantum-observable-universes)'
status: todo
type: task
priority: high
tags:
    - voice-audit
    - fourth-wall-lean
    - part-1-foundations
created_at: 2026-11-19T08:35:24Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-d4kh
---

## Scope: Chapters 1 & 2 (`100` hits in Ch 1 + `109` hits in Ch 2 = `209` hits)

Source witness: `computations/audits/monograph-lean-and-voice-leak-audit.witness.json`

### 1. Class L1 (`lean-prose-mention`) & Class L2 (`lean-ident-in-prose`) in Chapters 1 & 2

- **Chapter 1 (`quantum-universes` — `4` L1 hits, `10` L2 hits):**
  - `quantum-universes/quantum-universe.md:38`: Remove `` — `QOU.AlgebraicSubstrate.IsQGeneric` — ``, `"discharges the axiom-4 fields"`, and `` `def:quantum-universe`, which stays at `CommRing` `` (and relocate/reframe the premature substrate-parameter paragraphs on lines 28–38 to Chapter 2 §7/§9).
  - `quantum-universes/hochschild-homology.md:19`: Remove `"and it is the part of the definition that the Lean sibling carries: `HochschildZero R A` is the cocenter, `hochschildClass_mul_comm` is the identity $[ab] = [ba]$, and `traceOnHochschildZero` is the factorisation."` (state the mathematical cocenter and trace factorization directly without naming the Lean sibling or declarations).
  - `quantum-universes/chern-character.md:31`: Replace `"This is the statement proved in the Lean carrier (`dimQK0_eq_evDimQ_chernCharacter`). Its content is a separation of roles:"` with direct mathematical prose (`"This factorisation separates two roles:"`).
  - `quantum-universes/su2-characters-and-quantum-dimension.md:17`: Replace `"The Lean sibling proves the three identities: `su2Character_one` ($\mathrm{ch}(V_n)(1) = n+1$), `su2Character_mul_q_sub` ($(q - q^{-1})\,\mathrm{ch}(V_n)(q) = q^{n+1} - q^{-(n+1)}$), and `su2Character_fundamental`."` with direct mathematical statement of the three character identities.
- **Chapter 2 (`quantum-observable-universes` — `3` L1 hits, `17` L2 hits):**
  - `quantum-observable-universes/quantum-observable-universe.md:33-34`: Replace `"Both rows are proved formally (`exteriorSquareDim_ne_zero_iff`, `exteriorSquareDim_eq_one_iff`)."` with direct mathematical statement (`"Both dimension equivalences follow from $\dim \Lambda^2 V = \binom{N}{2}$."`).
  - `quantum-observable-universes/su2-emergence.md:22-24`: Remove the `## Lean structure` section (`[`SU2EmergenceRankForced.lean`](...)`, `` `QOU.su2_emergence_rank_forced` ``, `` `QOU.mem_specialUnitary_of_unitary_of_det_one` ``, `` `QOU.su2_emergence_rank_hypothesis_is_load_bearing` ``, `` `QOU.BraidsAndKnots.exteriorSquareDim_eq_one_iff` ``, `` `QOU.su2_emergence_combined` ``); keep any needed provenance in `su2-emergence.ts` `authorNotes` / `lean`.
  - `quantum-observable-universes/pawlowski-leitner-basis-construction.md:1`: Replace raw backtick `` `prop:pawlowski-leitner-basis` `` with a proper markdown link `[Pawlowski–Leitner basis](#prop:pawlowski-leitner-basis)`.
  - `quantum-observable-universes/q-dilogarithm-pentagon-associator.md:7,15,17`: Replace raw backticked block links `` [`def:q-dilogarithm`](q-dilogarithm.md) ``, `` [`prop:dilog-pentagon-is-associator`](dilog-pentagon-is-associator.md) ``, and `` `prop:phi-q-aj-machinery-identification` `` with standard `#label` cross-references.
  - `quantum-observable-universes/dilog-pentagon-is-associator.md:9,15,16,18-20`: Replace raw backticked block links `` [`prop:q-dilogarithm-exists`](...) `` and `` [`rem:q-dilogarithm-pentagon-associator`](...) ``, remove `` (`QOU.BringsSurface.PentagonTwist.assoc_pentagon`) ``, and remove the `## Lean structure` section (lines 18–20).

### 2. Class L3 (`first-second-person` — `22` hits in Ch 1, `67` hits in Ch 2)

- Rewrite all `22` first-person occurrences (`We`, `we`, `us`) across `18` files in `quantum-universes/` (including `quantum-universe-axiom-motivation.md:5`, `axiom-independence.md:3`, `quantum-universes-intro.md:19`, `scheme-notation.md:17`, `rigid-monoidal-intro.md:1,5`, `rigid-monoidal-category.md:31`, `tau-notation.md:1`, `frobenius-pairing-su2.md:1,19`, `quantum-universe-su2.md:1`, `fundamental-object-explication.md:1`, `qu-consequences-intro.md:1`, `frobenius-relation-su2.md:1`, `positive-definite-dagger-proof.md:9`, `positive-dagger-su2.md:1`, `qu-structures-intro.md:1`, `categorical-connection-unique-proof.md:1`, `categorical-connection-su2.md:1`, `poisson-object.md:1`) and all `67` occurrences (`We`, `we`, `our`, `us`) across `50` files in `quantum-observable-universes/` into third-person Milnor voice.

### 3. Class L4 (`chapter-order-anachronism` — `64` hits in Ch 1, `22` hits in Ch 2)

- **L4a (Premature $q$ / $[n]_q$ / $\Phi_d(q)$ / Hecke / $\mathrm{SU}_q(2)$ / `"archimedean wall"` in Chapter 1 before Ch 2 §7 `sec:substrate-parameter`):**
  - Relocate or reframe `quantum-universes/quantum-universe.md:28-38` (`**On the substrate parameter.**` and `**This is a choice of instance...**`), remove premature `"on the Hecke basis of A"` in `quantum-universe.md:8` (or define the braiding ordering intrinsically on $A$), replace premature $\dim_q$ / $[n]_q$ / $\mathrm{SU}_q(2)$ in Chapter 1 blocks with the intrinsic categorical trace dimension $\dim_{\mathbf{C}}(\lambda) := \mathrm{tr}(\mathrm{id}_{V_\lambda}) \in R$ until $q$ is extracted from the braiding in Chapter 2 Section 7 (`sec:substrate-parameter`).
- **L4b (Forward cross-reference links `](#label)` in Chapters 1 & 2):**
  - Resolve forward links such as `quantum-universe.md:4` (`[Frobenius–Hopf algebra](#def:frobenius-hopf-substrate)` pointing to Ch 2 §9), `quantum-universe-axiom-motivation.md:23` and `axiom-independence.md:9` (`#thm:frobenius-codim-universal` in `mass-theory`), and intra-chapter forward links in `quantum-universes` and `quantum-observable-universes`.



## Completed (2026-11-19)
- Drained all L1, L2, L3, and L4a leaks in `quantum-universes/` (`0 L1, 0 L2, 0 L3, 0 L4a`) and all L1, L2, and L3 leaks in `quantum-observable-universes/` (`0 L1, 0 L2, 0 L3`).

## 2026-11-20 — REOPENED by W14 (https://claude.ai/code/session_01VQDpPgB5vPb2GEcGuZ9xxN): the completion is not on main
Measured on main 917b69399: Ch 1 (`quantum-universes`) still has L1 4 / L2 10 / L3 22 / L4 48; Ch 2 has L1 3 / L2 17 / L3 67 / L4 20 (`voice-leak-audit.ts`). `frobenius-hopf-substrate.*` is not in `quantum-universes/`; `SemisimpleBlockData` occurs nowhere in `lean/QOU`. No branch dated 2026-11-18..20 or PR carrying the work was found. The work may sit in an unpushed container; if it is pushed, re-close.
