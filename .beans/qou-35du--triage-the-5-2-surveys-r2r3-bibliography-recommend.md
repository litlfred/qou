---
# qou-35du
title: 'Triage: the 5_2 survey''s R2/R3 bibliography recommendations are much weaker than presented — corpus-grepped'
status: todo
type: task
created_at: 2026-08-18T21:47:15Z
updated_at: 2026-08-18T21:47:15Z
---


## Finding

Corpus-grepped two recommendations from the 2026-08-18 5_2 literature survey
before acting on them. Neither buys what it claims.

**R3 (register Bettin–Drappeau) — premise FALSE, twice.**
1. Nothing is conditional on quantum modularity. The bridge-verdict audit calls
   it "named, literature-established" and "Lean-scaffolded sorry-free"; the
   unification ledger records the row as "Lean-proved sorry-free"
   (`OhtsukiTowerBarParity.lean`). The actual blockers named in that same
   verdict are: smooth Borel sum anchor-blind, anchor-dependent piece is a
   CAL-2 input (Subgoal-2), `A_ω = 3` explicitly open. QMC moves none of them.
2. Wrong QMC anyway. Every conjectural corpus reference is to the **Refined**
   QMC (GGM/GSWZ, the full (x,q)-series matrix). Bettin–Drappeau prove
   **Zagier's**. Strictly weaker; does not discharge the refined statement.
   This is the `da-arity-conflation` shape — same topic, different proposition,
   and a topic-grep cannot separate them.

**R2 (register Ohtsuki 2016) — half-true, motivation contradicted.**
The solo 2016 paper is genuinely unregistered. But the stated reason ("the
corpus reconstructs the κ-ladder by hand") is false: `ohtsuki-takata-2015` IS
registered, `OhtsukiKappaDependence.lean` is 143 lines, there are FOUR audits
named for him, and `references.ts` prose already cites his saddle-point/Borel
analysis. Citation hygiene on one paper, not recovery of missing machinery.

## Disposition

Neither is worth a tranche. Registering both is fine as ordinary bibliography
hygiene when someone is next in `references.ts` — but **no corpus claim may be
re-tiered on the strength of either**, which is what R3 was proposed to do.

## The reusable test

A survey's recommendations are claims about the corpus and get the same
corpus-grep as any other claim. The cheap test that caught both: name the
specific proposition currently carried as conditional, then find it. For R3
there is no such proposition; for R2 the machinery is already present under a
different citation.

Scope doc: `docs/scope/2026-08-18-5two-survey-r2-r3-triage.md`
