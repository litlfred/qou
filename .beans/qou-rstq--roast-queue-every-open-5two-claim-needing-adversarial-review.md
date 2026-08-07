---
# qou-rstq
title: 'ROAST QUEUE: every open 5₂ claim needing adversarial review, with what specifically to attack'
status: todo
type: task
priority: high
tags:
    - qbeta
    - 5two
    - review
    - roast
created_at: 2026-08-07T22:05:00Z
updated_at: 2026-08-07T22:05:00Z
parent: 0yqu
---


## Purpose

The 5₂ chain now spans six beans and two Lean files, and **most of it is
verified-not-proved**. This is the index of what is still open, and — more
usefully — **what specifically to attack in each**. A reviewer should be able to
start here.

**Standing status: sum rule verified to 80 dps, unproved.**

## The chain, and where each link actually stands

| link | bean | status | roast target |
|---|---|---|---|
| transport `x=1 → x=−1` | `qou-trns` | branch **pinned**; envelope **true but unformalized** | the envelope theorem is confirmed *numerically* only |
| cyclotomic identity | `qou-8v3k` | reduction, not proof | the `S(x) = S(1) − log²x` integration |
| rationality | `qou-b7cy` | proved **on paper**, via Borel | not formalizable — see `qou-mlbg` |
| numerators `(17,5,−1)` | `qou-fivt` | **derived**, Lean-checked | rests entirely on `qou-rhyp`'s nine hypotheses |
| the nine hypotheses | `qou-rhyp` | **all unproved** | five-term is the real one |
| complex `Li₂` | `qou-clx8`, `qou-ph1k`, `qou-gkco` | open | statement verified true; proof open |

## What to attack, concretely

1. **`qou-rhyp`, the five-term instances.** Everything downstream is a
   `linear_combination` over these. If any of `hA`, `hB`, `hC` is not a genuine
   five-term instance — wrong argument, wrong branch — the whole derivation
   collapses. They were checked numerically to `1e-40`; check the *algebra* of
   the arguments independently.
2. **`qou-trns`, the envelope step.** Confirmed by finite differences, which is
   evidence, not proof. The IFT hypothesis (`min |disc| = 0.348`) was measured on
   a sampled arc — a finer sweep could in principle find a near-collision.
3. **`qou-b7cy`'s "rationality is PROVED".** True modulo Borel's theorem, which
   `qou-mlbg` shows is nowhere near Mathlib. Read that claim as *proved on paper,
   unformalizable*, and check nothing downstream silently upgrades it.
4. **Route 8's `k = 0`.** Now pinned by `g(1) = 0` rather than local constancy —
   stronger, but still assumes continuity of the root branches, which rests on the
   same discriminant sampling as (2).

## ⚠ The recurring failure mode in this work — check for it first

**Principal-vs-continuous `Log` has produced a spurious `2π` three separate
times** (`qou-trns`). Every one looked like a real discrepancy. If a probe here
reports a mismatch that is a multiple of `2π` or `π²`, suspect the branch
convention **before** suspecting the mathematics.

Related, from `qou-b7cy`: a per-embedding formula `V − L(ξ) = iπ·log[(1−w)/w]`
was tried and **is false** — it fails at two of three embeddings while the *sum*
is exact. Sum-level agreement does not imply term-level correctness.

## Known dead ends — do not re-run

* **PSLQ over `[L1, L(w₂), L(q), L(r), L(s)]`** returns `[−4,4,−3,4,3]`, which is
  a linear consequence of the targets and carries **no** information (`qou-fivt`).
* **The Galois/Möbius `T`-orbit** (`1/wₖ = 1 − w_{k+1}`) is real structure, but the
  orbit sum is **irrational** — the 3-cycle alone yields nothing (`qou-fivt`).
* **The `ℂ/2π²ℤ` modulus hypothesis** — refuted; the branch shift is a multiple of
  both moduli (`qou-r7ml`).
* **GGM / GGMW** contain no saddle-sum; `Σⱼ Vⱼ` appears nowhere (`qou-g2wr`).
* **"Formalize Borel first"** is a multi-year programme, not a plan (`qou-mlbg`).

## Two errors formalisation caught that numerics did not

Worth remembering when judging how much to trust the probes:

1. The certificate's **R-labels were permuted** against its coefficients — exact
   rational arithmetic confirmed a *rank* statement blind to which row was which.
2. The **divided form is false in characteristic 7**; `ring` refused it and
   `char_seven_forces` now proves the hypotheses force `3·L1 = 0` there.

## Also open, lower priority

* `qou-mfst` — `lake-manifest.json` still lists `«doc-gen4»` after `qou-dg4x`
  commented the `require` out. Harmless, deliberate, tracked.

## Refs

* parent `qou-0yqu`; PRs #4658 (merged), #4701
