---
# qou-yt29
title: 'GAP: categorical-linking-operation.lean still carries LkMultiplicative / LkTraceCutSymmetric := True and a global instance canonical (outside the SM sweep''s file list)'
status: todo
type: task
tags:
    - lean
    - gap
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-09-03T09:08:30Z
parent: qou-ggdk
---

Class A (hygiene) defect found but NOT fixed by the SM-surface Lean sweep (bean qou-08zf, 2026-09-03) because the file is outside that sweep's file list. mass-theory/categorical-linking-operation.lean defines LkMultiplicative and LkTraceCutSymmetric as Prop := True, proves them by trivial, and installs a GLOBAL instance canonical : CategoricalLinkingOperation R q — so conj:categorical-linking-operation is discharged for free (AGENTS.md §1a / §3b-tax, proof-claims-unencoded). The previous inlined copy in categorical-higgs-mechanism.lean has been DROPPED (not propagated); the Higgs carrier now states its linking input as MassEigenstateCountThree lk.

FIX: state the post-trace multiplicativity and the trace-cut symmetry as content-bearing predicates over the substrate algebra and the Markov trace (the file already has class MarkovTraceCyclic and the conditional lemmas trace_cut_cyclicity_step etc.), remove the global instance, keep the three genuinely proved properties as theorems, and register the carrier in docs/audits/lean-vacuity-review-ledger.json. Verify lean-direct.
