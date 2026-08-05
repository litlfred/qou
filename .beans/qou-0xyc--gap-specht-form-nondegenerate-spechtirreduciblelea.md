---
# qou-0xyc
title: 'GAP: specht_form_nondegenerate (SpechtIrreducible.lean:823) — specht_gram_orthogonal (Sagan 2.4.7) needed'
status: in-progress
type: task
priority: normal
created_at: 2026-08-05T01:54:57Z
updated_at: 2026-08-05T03:00:00Z
---

## Current status (2026-08-05)

- `specht_gram_diag` (diagonal Gram entry = |C_T|): **PROVED** (sorry-free candidate,
  hand-audit; LSP not available in sandbox). Lines 716–790.
- `specht_gram_orthogonal` (off-diagonal = 0): **one honest sorry** (Sagan 2.4.7 gap).
  Tracked separately in bean `qou-tup9`.
- `specht_form_nondegenerate` (full Gram argument): **fully written** (lines 823–892),
  depends on both gram lemmas. Once `specht_gram_orthogonal` is proved, the whole
  chain becomes sorry-free.

## What is open

`QOU.BraidKnot.SpechtIrreducible.specht_form_nondegenerate` at line 823:
> For `[Field k][CharZero k]` and `μ : YoungDiagram` with `μ.card ≠ 0`,
> `SpechtSubmodule μ ⊓ spechtPerp μ = ⊥`.

## What was attempted

- (1) ℝ shortcut (positive-definiteness over ℝ): DECLINED by owner 2026-07-25 —
  would weaken generic `[Field k][CharZero k]` to ℝ only.
- (2) [UNBLOCKED] Integer Gram matrix of `standardBasis` → corank base-invariant
  across char-0 fields → conclude corank 0 from the ℝ positive-definite case.
  `SpechtStandardBasis.standardBasis` is NOW SORRY-FREE on main (Garnir
  straightening + dominance core both closed).

## Surviving route

Take the ℤ Gram matrix of `standardBasis`, show its rank/corank is
base-invariant across char-0 fields (flatness / universal coefficients), then
conclude corank 0 by specializing to ℝ where `bilinM x x = Σ xd² > 0`.

Needs: a stable-olean session so `SpechtStandardBasis` + `SpechtIrreducible`
dep-cone builds without triggering from-source Mathlib rebuild (~30–60 min).
Use `lake-cache/qou-v4-24-0` restore recipe per `lean-environment-setup.md`.

## Why it matters

`specht_form_nondegenerate` is the sole sorry in `specht_isSimple` (the
body of `specht_isSimple` is already sorry-free, just calls this theorem).
Closing this would make the entire Specht-irreducibility chain sorry-free
(excluding RSK/YoungTableauStandard/JucysMurphy which need upstream Mathlib ports).
