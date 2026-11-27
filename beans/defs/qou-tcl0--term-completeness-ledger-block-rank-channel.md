---
# qou-tcl0
title: 'Term completeness: block × rank × channel ledger for mass/binding/decay'
status: todo
type: feature
priority: high
tags:
    - compute-accuracy
    - term-completeness
created_at: 2026-11-27T20:25:00Z
updated_at: 2026-11-27T20:25:00Z
parent: qou-myts
---

Carl 2026-11-27: how do we know we have all the terms in mass/binding/decay; are all reps, characters and partitions covered? Answer (PR #9658): an observable on n = 3A strands is a finite sum over (two-row block k ≤ n/2, i.e. isospin T) × (tensor rank r ≤ min(body count, 2T)) × (channel braid r=0 / flavour r≤1 / em r≤2). Complete iff every entry has a free coefficient; a gap is a named missing summand. Lean QOU/Nuclear/TermCompleteness.lean; audit docs/audits/2026-11-27-term-completeness-ledger.md. Children tcl1..tcl4 are the gaps G1..G4. Done 2026-11-27: braid rank 0 at every n (isEndo_list_prod); flavour ≤1 / EM ≤2 caps derived from the level-2b block set (maxRank_eq_bodyRanks, bodyRank_qdim), citing V* ≅ V and Clebsch–Gordan (not proved). Open: those two citations in Lean.
