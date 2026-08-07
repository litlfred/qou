---
# qou-r7ml
title: 'Route 7: retry the enhanced-dilogarithm reading at the corpus modulus ℂ/2π²ℤ'
status: in-progress
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - 5two
created_at: 2026-08-07T15:20:00Z
updated_at: 2026-08-07T15:20:00Z
parent: 0yqu
---


## What is open

Route 6 (`qou-0yqu`, 2026-08-07 night) tested Zagier's **enhanced dilogarithm**

    D̃(ẑ) = Li₂(z) + ½·u·v    on   X̃ = {(u,v) : eᵘ + eᵛ = 1}

against the 5₂ sum rule and refuted it **scope-(a)**: no integer branch offset
matches, residual exactly `πi(2b+k)u − b²π²`, leaving
`Σⱼ Re D̃(yⱼ) = π²/2 − (2/3)πθ` with `πθ ∉ π²ℚ`.

`D̃` is valued in **`ℂ/(π²/2)ℤ`** — Zagier's modulus.

**But the corpus has independently established, for these exact `Vⱼ`, that
`V` is `ℂ/2π²ℤ`-valued** (`docs/coordination/1ppq-qbeta.md`, 2026-07-18, GGM
§6.1 5₂ port; σ3-pair positions are lattice representatives). That is a
**factor-4 different modulus** from the one Route 6 imported.

Route 6's refutation is **scope-(a)** and explicitly declines to exclude "a
formulation at a different covering point or Bloch element". The corpus's own
`2π²` lattice is exactly such a candidate and **was never tried**.

## Why it is worth trying

* `−3π²/2 = −(3/4)·2π²` — the sum-rule target is a **quarter-lattice point** of
  the corpus modulus. Either the mechanism or a coincidence; cheap to tell apart.
* Route 6's residual `πi(2b+k)u − b²π²` has a `b²π²` term. Under a `2π²` modulus
  the admissible `b` are constrained differently than under `π²/2`, so the
  offset search Route 6 ran does **not** transfer — it must be redone.
* The relevant torsion fact is already Lean-proved on this branch:
  `d[yⱼ]` is **3-torsion**, not zero (`three_smul_wedge_eq_zero`). A correct
  formulation has to track that; note `3 | 3π²/2` in the obvious way.

## How to test it — cheap, before any Lean

Numerical, against the existing 80-dps data. Search integer branch offsets under
the `2π²` lattice and check whether `Σⱼ Re D̃(yⱼ)` lands on `−3π²/2` for some
admissible assignment. **Control required**: run the same search on the control
cubics (`y³−y²+2y−1`, and the four `Πy = 1` controls from `qou-0yqu`). If a
match appears on the controls too, it is bookkeeping, not 5₂ arithmetic — the
same trap that killed Route 2.

## Prior art / do not redo

* Route 6's setup, roots on `2u = 3v + 2πik`, and its exact residual — reuse the
  algebra, change only the modulus.
* `Σⱼ D(yⱼ) = 0` is automatic (Route 2). The **individual** value is not:
  `3·D(y₊) = Vol(5₂)` to 20 digits (#4666). Do not re-derive either.

## Honest prior

Six routes tried, six not closing. This is the seventh and it is a **retry of a
refuted route with one parameter changed** — the base rate for that is poor.
Kill it fast on the controls if it does not separate 5₂ from them.

## Refs

* parent: `qou-0yqu`; ledger `docs/coordination/1ppq-qbeta.md`
* `QOU/QBeta/FiveTwoSaddleCurve.lean` — `u0_cubic_discriminant`, sorry-free
* Zagier, *The Dilogarithm Function* §II.1 B — `uploads/fulltext.pdf`
* PR #4658
