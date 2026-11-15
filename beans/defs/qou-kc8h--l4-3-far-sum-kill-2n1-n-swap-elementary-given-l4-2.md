---
# qou-kc8h
title: 'L4-3: Far-sum kill + (2n+1)->N swap (elementary given L4-2)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:36:11Z
updated_at: 2026-11-15T18:10:00Z
parent: qou-r9ih
---

RE-SCOPED 2026-08-19 -- grep MathlibExt/ and the 18-file Kashaev* lane BEFORE
writing anything.  The generic quadrature + Gaussian infra this brick would
reach for already exists on main.  Audit:
docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md

## 2026-11-15 — completed (owner tap "Close all four")
The Whitehead link volume conjecture is proved unconditionally in Lean:
`QOU.Knot.FigureEightVolume.whiteheadLink_volume_conjecture`
(`QOU/Knot/WhiteheadVolumeConjectureUnconditional.lean`), via
`instance vdVWhiteheadLemma4_holds` and `instance whiteheadInnerGaussianModel`
(`QOU/Knot/WhiteheadInnerGaussianProof.lean`). Commit d67ea11bef, PR #7913.
`#print axioms`: propext, Classical.choice, Quot.sound only. Scope: J_N(W) is
van der Veen's Lemma 1 sum formula (cited). Deriving that formula is now open
work, tracked separately (owner asked 2026-11-15T18:09Z).
