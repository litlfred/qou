---
# qou-0nr6
title: 'GAP: Radó triangulation of X/G with branch values as vertices (yslf step 1)'
status: todo
type: task
priority: low
tags:
    - mathlib-gap
    - bring-foundations
created_at: 2026-11-27T22:05:08Z
updated_at: 2026-11-27T22:16:41Z
parent: qou-6qbv
blocking:
    - qou-yslf
---

Split out of qou-yslf on 2026-11-27. Every compact Riemann surface (here X/G) has a finite triangulation, refinable so a given finite set (the branch values) are vertices. Radó 1925; Mathlib has no triangulations of surfaces. Also needed: the combinatorial Euler characteristic equals 2 - 2g for the analytic genus g (surface homology, also absent from Mathlib). Open. No axiom or class may stand in for it.



2026-11-27: now a BACKUP route. By owner ruling (map-first) the chi = -6 chain starts from the finite Bring map (QOU/BringsSurface/BringMapChain.lean) and the smooth surface is a model of the map, so the chain does not need this bean.
