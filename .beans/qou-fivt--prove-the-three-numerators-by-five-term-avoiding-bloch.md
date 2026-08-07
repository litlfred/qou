---
# qou-fivt
title: 'Prove the three numerators 17, 5, −1 by five-term/Abel — the route that AVOIDS the Bloch group'
status: todo
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - lean
created_at: 2026-08-07T18:05:00Z
updated_at: 2026-08-07T18:05:00Z
parent: 0yqu
---


## The target

From `qou-b7cy` (Route 9), verified at 100 dps with residuals `~1e-101`, with
`wₖ = 1 + 2cos(2πk/7)` a root of `w³ − 2w² − w + 1`:

    Re[2L(wₖ) + L(−wₖ)]  =  mₖ · π²/42  =  (mₖ/7) · L(1),    m = (17, 5, −1)

`L` = Rogers dilogarithm. `Σ mₖ = 21`, `21/42 = 1/2`, which is Route 8's target
and hence the 5₂ sum rule. Denominator `42` verified minimal (all `d < 400` at
`1e-60`).

**Prove these three values.** That is the entire remaining mathematical content
of the sum rule.

## Why this bean, and not "formalize Borel"

`qou-mlbg` surveys Mathlib at the pinned rev and finds **zero** files mentioning
Bloch groups, the Borel regulator, polylogarithms, Rogers, or Steinberg, and no
`KTheory` directory at all. The Bloch–Borel argument of `qou-b7cy` is
*explanatory*: it tells you the values are rational and why. **It is not a path
to a Lean proof** — item 4 of that bean's roast (algebraic K-theory of number
fields + Borel's rank theorem) is a multi-year Mathlib project.

This route needs strictly less:

* a **real** `Li₂` on the relevant range — **QOU already has one**
  (`QOU.Archimedean.LiTwo`, with `LiTwo_reflection'` sorry-free on `(0,1)`),
* the Rogers `L` and its functional equations,
* no Bloch group, no K-theory, no Borel.

## What is already in hand

* **Reflection** `L(z) + L(1−z) = L(1) = π²/6` — the QOU `LiTwo_reflection'` is
  exactly this shape on `(0,1)`.
* **Duplication** `L(z²) = 2L(z) + 2L(−z)` — verified exactly per embedding
  (`qou-b7cy`), so `2L(w) + L(−w) = L(w) + ½L(w²)`. Either form may be the
  easier target.
* **The algebraic relation** `(1 − w)²(1 + w) = w²`, now **Lean-proved
  sorry-free** in `QOU/QBeta/FiveTwoCyclotomicBloch.lean` (`bloch_key`), and in
  the sharp form `bloch_poly`: the relation *is* the minimal polynomial. This is
  exactly the shape that generates Y-system / Frenkel–Szenes dilogarithm
  identities, which is the natural source of `mₖ/7` values.
* `w`, `1−w`, `1+w` are all **units** of `ℚ(ζ₇)⁺` (norms `−1, −1, +1`), with
  minimal polynomials `w³−2w²−w+1`, `u³−u²−2u+1`, `v³−5v²+6v−1` — the latter two
  Lean-proved (`minpoly_one_sub`, `minpoly_one_add`).

## ⚠ Branch care — do not skip

Only `w₂ = 0.5549…` lies in `(0,1)`. `w₁ = 2.2469… > 1` and `w₃ = −0.8019… < 0`,
so `Li₂` there is off the standard Rogers range and the *real part* is what the
identity is about. Any five-term manipulation must track which branch each term
sits on. **Related recorded failure:** in `qou-b7cy` a per-embedding formula
`V − L(ξ) = iπ·log[(1−w)/w]` was tried and is **FALSE** — it fails at two of the
three embeddings on exactly these grounds, while the *sum* is exact. Expect the
same trap here.

## Suggested attack

1. Reduce `2L(w) + L(−w)` to `L(w) + ½L(w²)` by duplication, then rewrite `w²`
   as `(1−w)²(1+w)` and look for a five-term configuration in `w`, `1−w`, `1+w`
   — all units, all with known minimal polynomials.
2. Compare against the classical level-7 ladder literature (Watson's identities;
   Loxton; the `A₂`/Y-system tables). Denominators of `7` in units of `L(1)` are
   that literature's signature. **`qou-g2wr` established GGM/GGMW do NOT contain
   this** — look at the ladder literature, not the resurgence papers.
3. Only after a paper proof exists, formalize — and note the branch handling will
   need the complex `Li₂` unless the argument is arranged to stay real, which is
   worth designing for from the start (it would dodge `qou-ph1k`/`qou-gkco` too).

## Honest prior

Nine routes tried on the parent bean; seven refuted, two reductions. This is the
first target that is a **finite, explicit, classical-shaped** statement rather
than an opaque constant — but "classical-shaped" is not "done", and the branch
structure is exactly where the last two attempts broke.

**Sum rule status: verified to 80 dps, unproved.**

## Refs

* parent `qou-0yqu`; `qou-b7cy` (Route 9), `qou-8v3k` (Route 8), `qou-mlbg` (the gap survey)
* `QOU/QBeta/FiveTwoCyclotomicBloch.lean` — the Lean-proved algebra
* PR #4658
