---
# 29r5
title: 'Remap stale imports: models-of-qous (5) + lifting-and-descent (5) + braids-and-knots (5) siblings'
status: completed
type: task
priority: normal
created_at: 2026-06-30T23:32:53Z
updated_at: 2026-07-05T05:05:00Z
---


> **Resolved 2026-07-05 (swarm 1).** Mathlib import remaps applied + Lean-verified (0 stale imports remain). Merged in PR #3337.

## 2026-07-03 — session diagnosis: import layer solved, all 12 remain deep-broken (reverted per #3191 precedent)

Validated 7-module remap table (targets confirmed against the v4.24.0 cache):
  BigOperators.Group.Finset → .Basic | GroupPower.Basic → Group.Basic |
  Order.Ring.Lemmas → Order.Ring.Basic | Data.Int.Defs → Data.Int.Basic |
  Geometry.Manifold.SmoothManifoldWithCorners → Geometry.Manifold.IsManifold.Basic |
  LinearAlgebra.Basic → LinearAlgebra.Span.Basic | Tactic.Omega → Mathlib.Tactic
Plus corpus-wide: Topology.ContinuousFunction.Basic → Topology.ContinuousMap.Basic (18 files).
Parse micro-fix (verified, re-revealed next layer): /-- doc comment on
`noncomputable section` is illegal — demote to /- (quantum-dilogarithm.lean:34,
skein-resolution-obstruction.lean:44).

Post-remap first errors (all still RED — remaps REVERTED, ship only with full drains):
  instanton / irreducible-connection / self-dual-curvature :: invalid field notation (API drift)
  main-commutative-diagram-proof / q-yang-mills-levi :: function expected (API drift)
  brane-boundary-structure :: simp made no progress (78:4)
  quantum-dilogarithm :: failed to synthesize (45:7, after parse fix)
  descent-lemma :: failed to synthesize (31:11)
  chi-sym-alt-closed-form :: dependsOnNoncomputable (42:4)
  chi-std-pernucleon-closed-form :: kernel invalid declaration (40:11)
  skein-resolution-obstruction :: linarith failed (110:59, after parse fix)
  frobenius-lepton-meson-bridge :: omega could not prove (21:64)

Requires: restored lake-cache (2026-07-02 reseed: 859 QOU + full-library oleans;
LEAN_PATH must include content/quantum-observable-universe/lean/.lake/build/lib/lean).
Next session: drain file-by-file (remap + proof repair + verify green), 2-4 files per tranche.
