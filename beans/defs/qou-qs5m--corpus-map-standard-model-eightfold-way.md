---
# qou-qs5m
title: 'Corpus map: existing connections to the Standard Model and the eightfold way'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-15T09:30:00Z
parent: qou-qs0e
---

Survey every corpus connection to the SM gauge group, hypercharge, weak isospin, generations, anomaly cancellation, flavour SU(3) / eightfold way (octet, decuplet, Gell-Mann-Okubo), SU(6), Schur-Weyl / q-Schur-Weyl, and the `appendix-standard-model/` chapter. Classify each: proved / conditional / conjecture / prose / fitted, with citations. Output: an audit doc the other qs* beans build on.

## 2026-11-15 — map written (PR #7823)
`docs/audits/2026-11-15-standard-model-eightfold-way-corpus-map.md`. Top drift: g_A fitted but marked RESOLVED (`hadron-half-life-verification.md:22`, `AxialCoupling.lean:215-217`); generation count 4/3/2/3 unresolved; quantum Schur-Weyl "not formalised" stale (N=2 proved in JimboActionKernel); anomaly cancellation and SU(6) absent. Owner decision on drift fixes framed in §12. Path 0 (corpus_search) not run - MCP down.

## 2026-11-15 — owner ruling D2 = option 2 ("fix g_A and schur-weyl ... as recommended")
Applied in PR #7823: `hadron-half-life-verification.md` item 3 re-scoped from RESOLVED to "not derived; selected among three colour averages"; `schur-weyl-eightfold.md` + cheat sheet :546 now cite JimboActionKernel for the N=2 half. Sidecars NOT refreshed: qa-sweep fails to load at the pinned platform (`Cannot find module ../../cat-harness/schemas/kg/cat-harness`). Hand render-check only.
