---
# qou-wiub
title: 'GAP: A=3 amplitude E — local Stokes route walled; derive E from the GLOBAL Birkhoff connection matrix'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T19:14:47Z
updated_at: 2026-10-04T15:19:39Z
parent: qou-v2om
---

Local Stokes/resurgence route WALLED (branch claude/deltalambda-stokes-amplitude-e-2026-08-08, StokesAmplitudeE.lean sorry-free, lean-direct exit 0, no sorryAx). Single-slope carrier (C1 at infinity, pure isoclinic) gives RSZ isoformal dim 0 so E=0 (no lift, scope-b); multi-slope leaves E free (surjective). Therefore E's value is NOT in local Stokes data. Next honest step: construct the GLOBAL 0-to-infinity Birkhoff / q-monodromy connection matrix (theta-valued) of the C1 module via the DRSZ recipe (library/equations-aux-q-differences/Equations_aux_q-differences.pdf s3.3) and read E off it. This is NOT local Stokes data and is un-started (PR 4790 W2 successor). See docs/audits/2026-08-08-stokes-amplitude-e-local-wall.md and the no-instance class GlobalBirkhoffSuppliesAmplitude. Anti-fit stands: pinning E to r* is a fit, not a derivation.

### Progress (Round 74 — PR litlfred/qou#8322)
- Formalized in PR `litlfred/qou#8322` (`feat/round74-kashaev-stokes3-stokesamp-ohtsukinz-pauli-43c1`, Commit 1 `82ec77a3b69cc6d79a85c01e64b63d422fa51c45`, Head `d13ffedea3175ba61da12a5b2abf5cf08d471608`, `scriptHash: 79ed375a0246`).
