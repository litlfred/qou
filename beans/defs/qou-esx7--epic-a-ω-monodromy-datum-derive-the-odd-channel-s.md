---
# qou-esx7
title: A_ω monodromy datum — derive the odd-channel Stokes constant (Qβ/m_n/Δpn trio, 2/7→5/7)
status: in-progress
pr: 8277
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-17T20:20:36Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: A_ω monodromy datum — derive the odd-channel Stokes constant (Qβ/m_n/Δpn trio, 2/7→5/7)


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open. Note that "A_ω = 3" as certified is GGM's q→0 off-diagonal constant (eq 60). The "symmetry constant" form adds nothing (it is a tautology of the GGM sandwich).

Evidence: Story with an empty body. Children and siblings: vr3q, l15q, fgte, dtd3. No result derives the odd-channel Stokes constant; see finding 2 for what "A_ω=3" actually is.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Round 55 Implementation Progress (PR #8277)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8277 (head `8f4f568482d5a937ac700b4605cc7c48271faae8`, Commit 1 `0a62bee9d3e501101e220bcafa8c3a9fee1d0d25`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/StokesMonodromyGGMSandwichAndTrivialFlatConnection.lean` (`ggm_unipotent_sandwich_invariance`)
- **80-dps Witness:** `computations/probes/round55-tau-loop-markov-nucleon-stokes-monodromy.witness.json` (`scriptHash: 1de39a3b3d7c`, `allPassed: true`, `0` raw `float64`)
