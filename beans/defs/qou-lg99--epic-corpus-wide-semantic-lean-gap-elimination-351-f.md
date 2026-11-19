---
# qou-lg99
title: 'Epic: Corpus-Wide Semantic Lean Gap Elimination (351 flagged provable blocks + 5 conjecture refs across LG-1..LG-8)'
status: open
type: epic
priority: high
created_at: 2026-11-19T19:55:00Z
updated_at: 2026-11-19T19:55:00Z
---

Eliminate all semantic Lean gaps across the 741 wired provable blocks (312 tiny <=30L scalar/projection stubs, 78 ContextClass wrappers where Mathlib provides native structures, 16 OpaquePropField carriers) plus the 5 conjectures missing `lean.ref`, verified via `lean-verify.sh` / `lean-direct-cone.sh -B`, `lean-vacuity-axiom-audit.ts`, and blind 3-way Round-Trip Auditing (`RT-1`, `RT-2`, `RT-3`).
