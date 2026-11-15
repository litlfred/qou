---
# qou-zezz
title: 'A_ω route 1: GGM 3d-index of 4₁ — tetrahedron-index q-series, integer Stokes candidates (dup of #3805 authorized)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-17T20:20:36Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-17 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** Route 1 delivered: the exact tetrahedron index and the 4₁ total 3d-index (DGG anchor 4.20 reproduced 2026-10-10). The "integer Stokes candidate" read-off is the dictionary question in qou-3ent/bvgw.

Evidence: `qbeta-g3-tetrahedron-index-exact.witness.json` (3/3: triality, cross-implementation, substrate) and the 4₁ assembly (see 8j0d, re-run reproduced) both landed. Commit `c45c6ab1de` created the route.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
