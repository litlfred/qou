---
id: qou-0xyc
title: "GAP: specht_form_nondegenerate (SpechtIrreducible.lean:708) — ℤ Gram matrix corank proof needed"
type: task
status: open
created: 2026-08-04
branch: copilot/eight-fold
---

## What is open

`QOU.BraidKnot.SpechtIrreducible.specht_form_nondegenerate` at line ~708:
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
