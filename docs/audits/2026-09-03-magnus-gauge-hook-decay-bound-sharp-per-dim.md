# The hook column of the gauge-invariant curvature decays: a sharp per-dimension bound (qou-o6ov)

**Date:** 2026-09-03
**Directive (owner):** "go" — bound the hook closed form in `j` from the Burau spectrum.
**Scope:** scope-(a); one rigorous positive + one crude negative; no MeV, no fit, nothing wired.
**Probe:** [`magnus_gauge_hook_decay_bound_probe.py`](../../computations/deltalambda/magnus_gauge_hook_decay_bound_probe.py)
**Lean:** [`MagnusHookDecayBound.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MagnusHookDecayBound.lean) (three lemmas; verification status is recorded in the PR body, not asserted here)
**Follows:** #6464 (closed form), #6480 (its Lean statement).

## The question

#6464 gave the hook column of the projector curvature a reduced-Burau closed form,
```
tr_hook(ρ·Ω₂^P) = T_j · Σ_a [ e_j(μ⁺_a) − e_j(μ⁻_a) ],   T_j = (4/[2]_q²)·q^{(L+2)(1−j)},   j = n−k,
```
`μ^±_a` the Burau spectra of the words `ρσ_aσ_{a+1}`, `ρσ_{a+1}σ_a`. For hooks `b(λ) = n−λ₁ = j`,
so a bound decreasing in `j` **is** the hook-column decay theorem the arc wants. Does the closed
form yield one?

## Two bounds, from `|e_j| ≤ …` applied term by term

- **Crude (spectral radius):** `|e_j(μ)| ≤ C(n−1,j)·rʲ`, `r = max|μ|` over all `2(ngen−1)` matrices
  ⇒ `B_j = T_j·2(ngen−1)·C(n−1,j)·rʲ`.
- **Sharp (triangle inequality):** `|e_j(μ)| ≤ e_j(|μ|)` — the elementary symmetric function of the
  *moduli* ⇒ `B'_j = T_j·Σ_a [e_j(|μ⁺_a|) + e_j(|μ⁻_a|)]`.

## Results (A = 2, 3; exact mpf, dps 140)

**Both bounds hold** at both A (`|tr| ≤ B_j` and `|tr| ≤ B'_j` for every `j`). The closed form
re-verifies against the direct seminormal trace: interior `|Δ_rel| ≤ 8.9e-139`, endpoint
`|Δ_abs| ≤ 2e-141` (an earlier "✗" was my own relative-error denominator at the two exact-zero
endpoints, not a mismatch).

**The crude bound does NOT decay from `j = 1`.** `B_j ∝ C(n−1,j)·dʲ` with `d = q^{−(L+2)}·r` is a
binomial hump peaking near `j ≈ (n−1)·d/(1+d)` — `j = 2` at A=2, `j = 4` at A=3 — and it is loose
by 10–10³. The structural reason is worth stating: **`r ≈ q^L`** (`r/q^L = 1.006, 1.10`), i.e. the
dominant Burau eigenvalue of a positive word of length `L` is `≈ q^L`, so the twist `q^{−(L+2)(j−1)}`
*exactly cancels it* and `d ≈ q^{−2}·(r/q^L) = 0.82, 0.90`. The decay must live in the
**subdominant** spectrum, which a spectral-radius bound throws away.

**The sharp bound per dimension is strictly decreasing at both A** — the result:

| A | `B'_j / C(n−1,j)`, `j = 0 … n−1` | monotone ↓ | tightness `max_j |tr|/B'_j` |
|---|---|---|---|
| 2 | 107.5, 44.3, 17.1, 6.12, 1.99, 0.583 | **yes, all j** | 0.23 |
| 3 | 657.7, 289.8, 123.0, 50.2, 19.7, 7.39, 2.65, 0.903, 0.292 | **yes, all j** | 0.13 |

So `|tr_hook(ρ·Ω₂^P)| / dim_hook ≤ B'_j / C(n−1,j)`, a strictly decreasing function of `b(λ) = j`,
with the bound within a factor 4–8 of the actual. The Burau moduli of `W = ρ^V` fall off
geometrically (`8.66, 6.12, 3.56, 3.56, 2.00` at A=2; ratio ≈ 0.71–0.77 per step at both A) — not
"one dominant, rest tiny" — and it is that geometric falloff, kept by `e_j(|μ|)`, that drives the
per-`j` decay.

**Two honest observations about the raw quantities.** Raw `B'_j` (not per dim) is monotone at A=2
but has a single bump `j = 1 → 2` at A=3 — and so does the *actual* raw `|tr|` (269 → 371 → 74), so
the bound is tracking a real feature, not being loose. And the actual `|tr|/dim` at A=3 has a small
tail wiggle (`j = 5 → 6`: 0.142 → 0.176) beneath the monotone bound. The theorem-shaped statement is
about the bound; the actual sits under it.

## What is formalized

`MagnusHookDecayBound.lean`, over a generic linearly ordered commutative ring (the ordering is
what `|·|` needs — the §7c archimedean-side specialisation, in its own file so
`MagnusHookExteriorPower` stays bare `CommRing`):

- `abs_esymm_le_esymm_abs` — `|e_j(μ)| ≤ e_j(|μ|)` (triangle inequality on the `esymm` sum).
- `abs_sum_esymm_sub_le` — across the commutator sum.
- `abs_mul_sum_esymm_sub_le` — with the twist scalar: `|c·Σ_a(…)| ≤ |c|·Σ_a(…)`, which is `B'_j`.

Composed with `trace_mul_curvature_eq_of_word_traces` (#6480), the left side is
`|tr_hook(ρ·Ω₂^P)|`. These are the *only* inequalities the sharp bound uses.

## Honest limits

- **The monotonicity of `B'_j/C(n−1,j)` is measured, not proved.** It is a property of the actual
  Burau moduli at A = 2, 3, not a theorem for arbitrary spectra. The lemmas reduce "the hook column
  decays" to a statement about one list of moduli per commutator member — which the probe checks.
- **A = 2, 3 only.** The geometric falloff of the moduli is what one would test at A = 4.
- **Gauge-invariant object only.** This is `Ω₂^P`; the seminormal germ has no such closed form
  (#6432, #6434). Nothing wired, no witness.

## Bottom line

The reduced-Burau closed form turns the hook-column decay into a bound: the crude spectral-radius
version fails (a binomial hump — the twist cancels the dominant eigenvalue `≈ q^L`, so only the
subdominant spectrum can decay), but the sharp triangle-inequality version `B'_j = T_j·Σ e_j(|μ|)`
**holds and is strictly decreasing per dimension at both A**, within a factor 4–8 of the actual.
The one inequality it needs, `|e_j(μ)| ≤ e_j(|μ|)`, is stated in Lean with its two corollaries.
