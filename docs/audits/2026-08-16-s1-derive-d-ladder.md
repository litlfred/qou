# S1 — Deriving the Q_β ladder in convention D

**Date:** 2026-08-16
**Branch:** `claude/s1-derive-d-ladder-2026-08-16`
**Status:** IN PROGRESS — scoping. Findings below are provisional until
the probe + Lean land.

Owner instruction: *"derive D ladder"*, following the 2026-08-15 ruling
that convention D (`z_D = q³/(q²+1)`) is canonical and C
(`z_C = √q/(1+q)`) is excised.

## The task, stated precisely

Substituting `z_D` into the existing C-frame ladder is **not** the task.
Registry [§9g](../coordination/ck-dk-canonical-registry.md) measures what
that substitution gives: `c₃ ≈ −974.43` (vs C's `−2.069`), implied
`c₂ ≈ −9.299` (vs `−1.0176`), and an N2/N1 rung ratio of `0.89` — no
convergence. `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free)
makes the mutual exclusivity structural.

So the ladder that convention D supports must be derived from D's own
structure, not transported.

## Scope of this branch

1. State the structural claim about what the ladder's rungs actually are,
   and formalize it before any wide numerical search (formalize-first).
2. Derive the D-frame expansion from `z_D` and the substrate quantities.
3. Tier every coefficient: `proved` / `symbolic-exact` /
   `conditional (+hypothesis)` / `near-match` / `fitted`.
4. If it does not close, report the wall and bean the gap.

## Anti-fit posture

`c₃` in the current implementation is obtained by inverting the
experimental Q-value (`qbeta_utils.c3_target_at`:
`c₃ = (Q_codata/Q_N2 − 1)/u³`). That is a **fit**, in both frames, and is
labelled one throughout this document. Nothing extracted this way is
reported as derived.

## Pin

Proton / experimental pin `q₀ ≈ 1.1099785827513808` throughout, per the
2026-08-07 owner directive. No muon-built cache is read.
