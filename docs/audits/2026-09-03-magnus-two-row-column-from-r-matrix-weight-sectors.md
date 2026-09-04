# The two-row column of the gauge-invariant curvature from R-matrix weight sectors (qou-o6ov)

**Date:** 2026-09-03
**Directive (owner):** "go" — beyond hooks, with the now-canonical algebra-element object.
**Scope:** scope-(a); one exact positive; no MeV, no fit, nothing wired.
**Probe:** [`magnus_two_row_weight_sector_probe.py`](../../computations/deltalambda/magnus_two_row_weight_sector_probe.py)
**Follows:** #6432 (two-row characters reduce to the 2-dim R-matrix, germ does not), #6445
(`Ω₂^P` is an algebra element), #6464/#6480/#6520 (the hook column via reduced Burau).

## The question

The hook column of the projector curvature `Ω₂^P = (4/[2]_q²)Σ_a[σ_a,σ_{a+1}]` reduces to the
`(n−1)`-dim reduced Burau (#6464) and decays by a sharp bound (#6520). Two-row shapes `(n−k,k)` are
the next family. #6432 found their **characters** collapse exactly onto the 2-dim `U_q(sl₂)`
R-matrix by Schur–Weyl — but only as the weighted sum `Σ_k (n−2k+1)·tr_{(n−k,k)}`, and the *germ*
missed by 6.5% because it is not an algebra element. Is there a **per-irrep** two-row handle for
`Ω₂^P`?

## The handle — weight sectors

The R-matrix `Ř` on `ℂ²⊗ℂ²` is **weight-preserving**: `00 → q·00`, `11 → q·11`,
`01 → (q−q⁻¹)·01 + 10`, `10 → 01`. It never changes the number of up-spins, so every Hecke element
acts **block-diagonally** on the up-spin sectors `W_k ⊂ (ℂ²)^⊗n` (`k` up-spins, `dim C(n,k)`).
Schur–Weyl, `(ℂ²)^⊗n = ⊕_{k'} V_{n−2k'} ⊗ (n−k',k')`, puts exactly one weight vector of `V_{n−2k'}`
in `W_k` iff `k' ≤ k` (for `k ≤ n/2`), so `tr_{W_k}(g) = Σ_{k'≤k} tr_{(n−k',k')}(g)` and therefore,
**for every Hecke element `g`**,

```
tr_{(n−k,k)}(g) = tr_{W_k}(g) − tr_{W_{k−1}}(g),      dim(n−k,k) = C(n,k) − C(n,k−1).
```

Each two-row irrep trace is a difference of two blocks of size `C(n,k)`, built directly from the
fixed 4×4 `Ř` on bitstrings — no seminormal machinery, and the building block is `n`-independent.
This is the two-row analogue of the hooks' reduced-Burau reduction, and it reaches the *curvature*
precisely because `Ω₂^P` is an algebra element (#6445).

## Result (A = 2, 3; exact mpf, dps 140)

Against the direct seminormal traces, for every `k = 0 … ⌊n/2⌋`:

| A | (a) plain `tr_{(n−k,k)}(ρ)` | (b) `tr_{(n−k,k)}(ρ·Ω₂^P)` | dims match `C(n,k)−C(n,k−1)` |
|---|---|---|---|
| 2 | worst `|Δ_rel|` 1.4e-138 | worst 9.7e-140 | 1, 5, 9, 5 ✓ |
| 3 | worst 1.6e-139 | worst 1.6e-139 | 1, 8, 27, 48, 42 ✓ |

Both **exact to the dps floor**. The germ would fail (b) — that is what #6432 measured (6.5%);
`Ω₂^P` passes because its trace is a character.

The two-row decay column it yields, `|tr_{(n−k,k)}(ρΩ₂^P)|/dim` vs `b(λ) = k`:

| A | k = 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 2 | 8.12 | 1.93 | 1.63 | — |
| 3 | 33.6 | 8.67 | 4.00 | 1.70 |

Monotone decreasing in `k` at both A (the `k = 0` trivial rep is exactly 0).

## What this buys, and what it does not

- **A per-irrep two-row handle for the curvature, from a 2-dim object.** Blocks of size `C(n,k)`
  (largest at A=3 is `C(9,4) = 126`) instead of the `2^n` tensor space of #6432, and no seminormal
  construction at all. Together with #6464 the two largest families of the decay are now both
  reduced to small, `n`-independent building blocks.
- **The formal core is trace additivity over an invariant direct sum** — if `g` preserves each
  `U_{k'}` in `W_k = ⊕_{k'≤k} U_{k'}` then `tr_{U_k}(g) = tr_{W_k}(g) − tr_{W_{k−1}}(g)`. That is a
  one-line consequence of `LinearMap.trace` on a direct sum and does not earn a Lean file; the
  substantive content — that the R-matrix sectors decompose this way — is `U_q(sl₂)` Schur–Weyl,
  outside Mathlib, exactly as the seminormal hook identity was in #6480.
- **A decay bound for two-rows is the next step, and it is not the hook bound.** The hook bound
  worked term by term on a single `e_j`. The two-row trace is a **difference** of two sector traces;
  a per-sector triangle inequality bounds it by `|tr_{W_k}| + |tr_{W_{k−1}}|`, which does not decay
  in `k` (the `W_{k−1}` term carries the previous sector). The bound must respect the difference
  structure — e.g. via the sector *restriction* `W_{k−1} ↪ W_k` (the sl₂ lowering map intertwines
  the Hecke action) so that the difference is a trace on the *cokernel*. Not attempted here.

## Honest limits

- **A = 2, 3.** The identity is structural (weight preservation + Schur–Weyl), general in `n`; the
  decay figures are measured.
- **Gauge-invariant object only.** `Ω₂^P`; the seminormal germ has no such reduction (#6432, #6434).
- **No bound yet for two-rows.** The handle is established; the decay theorem for this column is
  the follow-on.

## Bottom line

The two-row column of the gauge-invariant curvature is carried **exactly** by up-spin sector
differences of the 2-dim R-matrix — `tr_{(n−k,k)}(ρ·Ω₂^P) = tr_{W_k} − tr_{W_{k−1}}`, verified to
~1e-139 at A = 2, 3 for both the plain characters and the curvature. Hooks (reduced Burau, #6464)
and two-rows (R-matrix sectors) are now both reduced to small `n`-independent objects; the two-row
decay *bound* must respect the difference structure and is the next handle.
