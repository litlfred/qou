---
# m1j2
title: 'T2: Artin braid group B_n via PresentedGroup (if BraidLinkTypes incomplete)'
status: completed
type: task
priority: normal
tags:
    - keystone-infra
    - tier2
created_at: 2026-06-25T17:06:54Z
updated_at: 2026-06-25T20:53:04Z
parent: 08a2
---

Check QOU/BraidKnot/BraidLinkTypes + IwahoriHecke for a real B_n presentation (σ_i, braid relations) via Mathlib PresentedGroup (cached). Build if absent. Feeds T1 JointGalois braid side + jet quotient braid.

Resolved-by-coordination 2026-06-25: do NOT build B_n via PresentedGroup — the 2026-05-30 iwahori-hecke workplan uses Coxeter S_n; braid action wired to Equiv.Perm (Fin n) instead (off-plan to add parallel B_n).
