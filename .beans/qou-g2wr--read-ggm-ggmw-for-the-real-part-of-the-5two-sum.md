---
# qou-g2wr
title: 'Read GGM 2012.00062 / GGMW 2111.04763 for the REAL part of the 5₂ sum rule'
status: todo
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - 5two
    - literature
created_at: 2026-08-07T15:20:00Z
updated_at: 2026-08-07T15:20:00Z
parent: 0yqu
---


## What is open

`qou-0yqu` names **GGM (2012.00062)** and **GGMW (2111.04763)** twice as "the
realistic direct sources … which compute precisely these `Vⱼ`, and are already
in `uploads/`" — and **neither has been read for the sum rule.** Broadhurst was
read (2026-08-07 b); these were not.

## Why they are the right target and not another dead literature lead

The disc −23 literature (Zagier, Zagier–Gangl, Browkin–Gangl) evaluates
**`ζ_F(2)` via the Bloch–Wigner `D`** — the **imaginary / volume** side. Our sum
rule is the **real part** (Chern–Simons / second-regulator side). So the
classical ladders are *adjacent, not a drop-in* — this is the caveat recorded
prominently in `qou-0yqu` and in PR #4658, and it is correct.

GGM/GGMW are different: they compute the **`Vⱼ` themselves**, not just `ζ_F(2)`.
The corpus already has deep machinery ported from GGM — the whole 4₁ Stokes lane
is complete and GGM §6.1's 5₂ curve is Lean-proved
(`FiveTwoSaddleCurve.lean`). So this is an **internal seam**, not a cold read.

## What to look for, specifically

1. Any closed form or functional equation for `Re V` (not `|Im V| = Vol`, which
   the corpus already reproduces to 1e-10).
2. The **modulus/lattice** convention for `V` — GGM is the source of the
   `ℂ/2π²ℤ` statement the corpus carries. Confirm it and get the exact
   normalization. **This directly feeds `qou-r7ml`.**
3. Whether `Σⱼ Vⱼ` (or its real part) appears as a total-index / Stokes-data
   identity, which is where a `−3π²/2` would naturally come from.

## Watch for

The corpus's own over-claim trap: `|Im V(σ1)| = Vol(5₂)` and
`ι_12(0) = Vol(5₂)/π` are **already established**. Finding those again is not
progress on the sum rule — it is the volume side, which Route 2 showed carries
no information about our identity. Only a **real-part** statement counts.

## Refs

* parent: `qou-0yqu`; ledger `docs/coordination/1ppq-qbeta.md` (GGM entries
  2026-07-18 onward)
* `uploads/` — both papers present
* PR #4658
