---
# qou-btvl
title: 'D3: cross-knot DT data — 6_1 + harden 5_2 (import tier; parent qou-rtec)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-08-15T10:52:55Z
---


## Handoff note (2026-08-15, post-completion)

Slope hardening landed (SnapPy normal_boundary_slopes, exact). The OTHER
half of the cross-knot data — #boundary-parabolic connections (R1's
count; 5₂ = 4 literature-recalled, 6₁ = unknown third-knot test point
for dtMax = recursionOrder+1) — is NOT hardenable in this sandbox:
snappy.ptolemy_variety(2,'all').retrieve_solutions() needs
ptolemy.unhyperbolic.org, which 403s through the proxy, and local
Groebner (magma/sage) is unavailable. A network-open or sage-equipped
environment can close it in minutes with the same probe pattern.
