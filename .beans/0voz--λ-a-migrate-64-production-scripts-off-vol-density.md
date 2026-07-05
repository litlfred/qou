---
# 0voz
title: 'λ_A: migrate ~64 production scripts off vol_density_borromean → vol_density_per_block'
status: completed
type: task
created_at: 2026-06-24T01:21:10Z
updated_at: 2026-07-05T05:05:00Z
---


## BLOCKER (2026-06-24)

Mechanical swap `λ_A → vol_density_per_block` breaks absolute masses to
−57% (per-knot `tr_M` undershoots: m_p 406 vs 938). λ_A is a fit (+2.96%)
but per-knot is *worse* for absolute mass; true ρ≈2.46 is underived
(GAP-A-4). Safe migration is gated on deriving the per-knot density rule,
NOT a find-replace. Dashboard (diagnostic, shows both) already done.
See `docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`
§critical-nuance.

> **Resolved 2026-07-05 (swarm 1).** Migration already substantially complete; literal 'borromean→per_block' target superseded by the 2026-06-24 owner ruling (per_block is binding-ratios-only; absolute mass routes via canonical_mass facade). Inventory audit + docstring redirect merged in PR #3340.
