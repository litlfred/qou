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

## 2026-08-15 update — #connections CERTIFIED after all (egress workaround)

The ptolemy-DB-firewalled handoff above is RESOLVED for 4₁/5₂: per the
owner's egress hint, the snappy WHEEL itself ships the certified Magma
primary-decomposition outputs (ptolemy/testing_files). Probe
dt_crossknot_connection_count_certified_probe.py: 4₁ = 2 irreducible
(one degree-2 orbit, x²−x+1 = ℚ(√−3)) + 1 abelian = 3; 5₂ = 3 (one
degree-3 orbit, x³+2x²+3x+1, the trace-field cubic) + 1 = 4. R1's
counts are now locally computed, not literature-recalled. Residual:
6₁ has no bundled data — the dtMax=recursionOrder+1 third-knot test
still needs the DB or magma. Pattern documented in the new
.claude/skills/local/sandbox-egress.md skill.
