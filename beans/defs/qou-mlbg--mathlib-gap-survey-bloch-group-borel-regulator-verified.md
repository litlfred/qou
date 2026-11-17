---
# qou-mlbg
title: 'Mathlib gap SURVEY (verified): Bloch group, Borel regulator, polylogarithm — and why Route 9 is not formalizable'
status: in-progress
type: task
priority: normal
tags:
    - 5two
    - reorg-2026-10-04
    - lean
    - mathlib-gap
    - bloch-group
created_at: 2026-08-07T18:05:00Z
updated_at: 2026-10-04T15:21:31Z
parent: qou-n4nr
---


## Why this bean exists

`qou-b7cy` (Route 9) says the rationality of the 5₂ cyclotomic identity is
**proved** — via `ξ = 2[w] + [−w] ∈ B(F)`, `F = ℚ(ζ₇)⁺` totally real, Borel ⟹
`B(F)` torsion ⟹ Rogers `L(ξ) ∈ π²ℚ`.

That is proved **on paper, citing a classical theorem**. It is *not* formalizable,
and this bean records exactly how far from formalizable it is — **measured, not
asserted**, against Mathlib rev `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`
(the rev `folio/quantum-observable-universe/lean/lakefile.toml` pins).

## The survey — 6,996 Mathlib `.lean` files

| searched | files matching |
|---|---|
| `Bloch` | **0** |
| `Borel regulator` / `borelRegulator` | **0** |
| `Polylog` / `polylog` | **0** |
| `dilog` / `Dilog` | **1**, and it is a *docstring aside* |
| `Rogers` | **0** |
| `Steinberg` | **0** |
| `Clausen` / `Lobachevsky` | **3**, all false positives |
| `*KTheory*` path | **none — the directory does not exist** |

Details on the near-misses, so nobody re-checks them:

* The single `dilog` hit is
  `Mathlib/Analysis/SpecialFunctions/Integrals/LogTrigonometric.lean:12`, a
  comment reading "involves the dilogarithm, this can be seen as computing
  special values of `Li₂`". **There is no `Li₂`.**
* The `Clausen` hits are the author name *Claus Clausen* on
  `Probability/Distributions/Exponential.lean` and *Clausen–Scholze* condensed
  mathematics. **There is no Clausen function `Cl₂`.**
* `Lobachevsky` : zero.

**What DOES exist and is usable:** exterior powers —
`Mathlib/LinearAlgebra/ExteriorPower`, `Mathlib/LinearAlgebra/ExteriorAlgebra`,
`Mathlib/Algebra/Category/ModuleCat/ExteriorPower.lean`. So the *target* of the
`δ : ℤ[F♭] → ∧²F*` map has infrastructure. That is the only piece present.

## ⚠ FALSE FRIEND — do not be misled by bean `el8w`

`el8w` is **Borel *resummation*** (transform + sum, Watson/Nevanlinna–Sokal),
status `completed`. That is an entirely different Borel from the Borel of
*Borel's theorem on the rank of K-theory of number fields*. The name collision
is a trap; `el8w` contributes nothing here.

Likewise `cj2d5` (`BorelZagierQouVolumes`) is a §3b conjecture carrier on the
**volume** side (Zagier conjecture, `ζ_F(2)` via Bloch–Wigner `D`). Adjacent, and
**not** the real-part statement Route 9 needs. Same real-part-vs-volume caveat
that `qou-g2wr` closed the literature on.

## 🔥 The roast — "formalize Borel first" is not a plan

Say it plainly: **anyone who reads `qou-b7cy` and concludes "so we formalize
Borel's theorem and then Route 9 goes through in Lean" has misread the cost.**
That path needs, at minimum:

1. A polylogarithm — Mathlib has none, not even `Li₂` on ℝ. (QOU has its own;
   see `qou-ph1k` / `qou-gkco`.)
2. The Rogers dilogarithm and its five-term functional equation.
3. The pre-Bloch group, the `δ` map, and the Bloch group `B(F)`.
4. Algebraic K-theory of number fields, `K₃`, and Borel's rank theorem.

Item 4 alone is a multi-year Mathlib project. **This is not a route to a Lean
proof of the sum rule; it is a research programme with a different subject.**

The correct reading of Route 9 is narrower and still worth having: it explains
*why* the value is rational and tells you what kind of object you are looking at.
It does **not** put the sum rule within reach of Lean.

## What IS reachable in Lean today

Only the algebra, which is why it was split out into
`QOU/QBeta/FiveTwoCyclotomicBloch.lean`: the two Route-8 Vieta products and
`bloch_poly` / `bloch_key` (the identity `(1−w)²(1+w) − w² = w³ − 2w² − w + 1`,
which is the minimal polynomial *identically*, hence a `linear_combination`
one-liner). Those are done and sorry-free. Everything above them is not.

## Next step

**Do not open a Borel-formalization bean.** See `qou-fivt` for the route that
avoids the Bloch group entirely — proving the three numerators `17, 5, −1`
directly from five-term/Abel relations, which needs only a real `Li₂` and the
Rogers functional equations, both of which are within reach.

## Refs

* `qou-b7cy` (Route 9), `qou-8v3k` (Route 8), parent `qou-0yqu`
* `qou-ph1k`, `qou-gkco` — the existing complex-`Li₂` Mathlib-gap beans
* PR #4658

---

## ⚠ CORRECTION 2026-08-07 — the survey's conclusion was too broad

The counts above are right: Mathlib has **no** `Li₂`, no Bloch group, no Borel
regulator. But I drew a wider conclusion than the data supported — that the
`B₂`-Fourier half of Route 10 therefore needed new infrastructure. **It does not.
Mathlib already has it**, and searching for `Polylog`/`dilog` was the wrong query.

`Mathlib/NumberTheory/ZetaValues.lean`:

```lean
theorem hasSum_one_div_nat_pow_mul_cos {k : ℕ} (hk : k ≠ 0) {x : ℝ}
    (hx : x ∈ Icc (0:ℝ) 1) :
    HasSum (fun n : ℕ => 1 / (n:ℝ) ^ (2*k) * Real.cos (2*π*n*x))
      ((-1)^(k+1) * (2*π)^(2*k) / 2 / (2*k)! *
        (Polynomial.map (algebraMap ℚ ℝ) (Polynomial.bernoulli (2*k))).eval x)
```

At `k = 1` the constants collapse to exactly `π²`:

    (−1)²·(2π)²/2/2! = 4π²/4 = π²,   so   Σₙ cos(2πnx)/n² = π²·B₂(x)

which **is** `Re Li₂(ζ₇^k) = π²·B₂(k/7)` — Route 10's gate G2 — with `x = k/7 ∈ [0,1]`.

### Why this matters

`Re Li₂` on the unit circle **is** that cosine series, so this half of Route 10
is formalizable **today, from Mathlib, without any `Li₂` at all**. It does not
depend on `qou-clx8`, `qou-ph1k`, or `qou-gkco`.

### The methodological lesson, worth more than the fact

The original survey searched for the **objects** (`Polylog`, `dilog`, `Rogers`,
`Bloch`) and concluded from their absence. But Mathlib often has the **content**
under a different name — here, a Fourier/Bernoulli theorem in `NumberTheory`,
nowhere near a file about polylogarithms. **Search for the statement you need,
not for the name you would have given it.** The zero-counts above remain
accurate; treat them as "these names are absent", not "this mathematics is
absent".

`Mathlib.NumberTheory.ZetaValues` is, incidentally, already an import of
`QOU/Archimedean/DilogReflection.lean` — so it is in the corpus's dependency
cone already.

## Progress Update (PR litlfred/qou#8231)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8231 (`513987e80ae041a6d8bc835ffbdda5371ccac289`, scriptCommitSha `9bd895c1b028c3d1abf67e3de52aeade9e9e5ccc`)
- **Summary**: Added `LiTwo_reflection_diff_symm` and `LiTwo_sum_sub_two_LiTwo_half` in `QOU/Archimedean/DilogReflection.lean`, verified by 80-dps mpmath probe `hyperbolic_planck_oneloop_qint_dilog_probe.py` (`scriptHash: 83d59661279d`).
