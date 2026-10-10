---
# qou-ay84
title: 'T3c: Borromean 3-cusp deformation — proton/neutron effective κ and ϑ'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-30T16:59:40Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

The proton is 𝔹₃ (Borromean, 3 cusps, τ=2i per cusp). The deformation space is 6D (3 complex u's), not 2D. At the symmetric point u₁=u₂=u₃=u the binding formula has cross-terms beyond 3×κ_per_cusp. Compute the full NZ Hessian for the Borromean link. Literature: Neumann-Zagier for links, Champanerkar-Kofman-Purcell.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open, well-posed geometry. Absorb qou-mcus here. Its "proton ϑ" comparison target is not determined by data (sign_flip_resolved=False).

Evidence: No commits or probes. The Borromean NZ Hessian is a well-posed computation.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
