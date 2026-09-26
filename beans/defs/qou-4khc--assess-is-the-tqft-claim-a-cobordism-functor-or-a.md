---
# qou-4khc
title: 'Assess: is the TQFT claim a cobordism functor or a braided-category analogy'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T18:08:47Z
updated_at: 2026-09-14T18:12:49Z
---

MEASURED (subagent + own verification). NO COBORDISM FUNCTOR EXISTS: grep cobordism|bordism|Cob over the whole non-Mathlib Lean tree = 4 hits, ALL docstring comments in Elaboration.lean, ZERO declarations. No Cob(n), no symmetric monoidal functor to Vect, no Atiyah axioms. NO S-MATRIX / NO MODULARITY: every 'modular data' object is a vacuum row S0 : iota -> R DEFINED as d/D, so 'S0 = d/D' is rfl not a theorem; no two-index S, non-degeneracy never stated. ObservableMTC class = {level : N, level_ge : level >= 3, braiding_nonsymmetric} — no simples, no fusion, no finiteness, no twist. jones_markov_trace_exists is an AXIOM over HeckeAlgebraData that carries NO Hecke relation and NO braid relation; corpus's own markov_axioms_vacuous_of_weight_zero proves those axioms admit tr_M == 0. DECISIVE q0 POINT: the corpus itself states (root-of-unity-truncation.md:30) that generic q>1 gives INFINITELY MANY simples (not an MTC) and that the QOU axiom FORBIDS q a root of unity — so MTC/anyon structure is excluded by the framework's own axiom, and KeystoneRootsToQ0Bridge proves both horns closed, sorry-free. VERIFIED MYSELF: massEnergyEquivalence (mass-energy-equivalence.lean:59) is E = E*(q-1)^2*(q-1)^-2 i.e. E=E, discharged by field_simp, with categoricalMass DEFINED as E*(q-1)^2 — .md says the proof 'proceeds via the Reshetikhin-Turaev invariant'. WHAT IS REAL: MathlibExt/MarkovMoves.lean (Markov equivalence + SEPARATING writheParity invariant, sorry-free, generic CommRing, header disclaims Markov's theorem); Machinery/MarkovTraceOnHecke.lean H3 (genuine Ocneanu/Wenzl tr_M on the 6-dim GB normal-form basis, cyclicity by ring); MathlibExt/Ribbon.lean (correct Joyal-Street ribbon axioms — but only ever instantiated at theta=id, the CLASSICAL case). VERDICT: real Hecke/Markov-trace mathematics; TQFT is a name, not a construction.
