---
# qou-4khc
title: 'Assess: is the TQFT claim a cobordism functor or a braided-category analogy'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T18:08:47Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-ddmn
---

MEASURED (subagent + own verification). NO COBORDISM FUNCTOR EXISTS: grep cobordism|bordism|Cob over the whole non-Mathlib Lean tree = 4 hits, ALL docstring comments in Elaboration.lean, ZERO declarations. No Cob(n), no symmetric monoidal functor to Vect, no Atiyah axioms. NO S-MATRIX / NO MODULARITY: every 'modular data' object is a vacuum row S0 : iota -> R DEFINED as d/D, so 'S0 = d/D' is rfl not a theorem; no two-index S, non-degeneracy never stated. ObservableMTC class = {level : N, level_ge : level >= 3, braiding_nonsymmetric} — no simples, no fusion, no finiteness, no twist. jones_markov_trace_exists is an AXIOM over HeckeAlgebraData that carries NO Hecke relation and NO braid relation; corpus's own markov_axioms_vacuous_of_weight_zero proves those axioms admit tr_M == 0. DECISIVE q0 POINT: the corpus itself states (root-of-unity-truncation.md:30) that generic q>1 gives INFINITELY MANY simples (not an MTC) and that the QOU axiom FORBIDS q a root of unity — so MTC/anyon structure is excluded by the framework's own axiom, and KeystoneRootsToQ0Bridge proves both horns closed, sorry-free. VERIFIED MYSELF: massEnergyEquivalence (mass-energy-equivalence.lean:59) is E = E*(q-1)^2*(q-1)^-2 i.e. E=E, discharged by field_simp, with categoricalMass DEFINED as E*(q-1)^2 — .md says the proof 'proceeds via the Reshetikhin-Turaev invariant'. WHAT IS REAL: MathlibExt/MarkovMoves.lean (Markov equivalence + SEPARATING writheParity invariant, sorry-free, generic CommRing, header disclaims Markov's theorem); Machinery/MarkovTraceOnHecke.lean H3 (genuine Ocneanu/Wenzl tr_M on the 6-dim GB normal-form basis, cyclicity by ring); MathlibExt/Ribbon.lean (correct Joyal-Street ribbon axioms — but only ever instantiated at theta=id, the CLASSICAL case). VERDICT: real Hecke/Markov-trace mathematics; TQFT is a name, not a construction.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8443)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityReadoutPartitionWeightBraidedTraceSurfaceGenusPolarizationPair.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_2djn_2joi_4khc_51l1_8ava_probe.witness.json` (`Commit 1` = `76eb5ed3bb589e3c0713062c1916ff3df6e16b60`, `HEAD` = `bd4d50a998e0b0519e966f309ff7ef17c810abac`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8443, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Verdict still holds on main: no Lean declaration named Cob/Bordism; `tqft-context.md` still says "grounded in TQFT" and "the associated 3d TQFT"; `root-of-unity-truncation.md` still says generic q > 1 has infinitely many simples (not modular). Superseded sub-finding: `massEnergyEquivalence` (E = E) was withdrawn 2026-11-15 (`mass-energy-equivalence.lean` header, bean qou-078y). Scoping edit proposed (audit §6 item 2), awaiting owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).
