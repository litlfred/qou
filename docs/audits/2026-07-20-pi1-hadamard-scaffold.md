# PI-1 — Hadamard factorization scaffold (Mathlib gap survey + brick roadmap)

**Date:** 2026-07-20 **Bean:** `qou-n4pv` (epic `qou-lbth`, pentagon-infra)
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**File:** `content/quantum-observable-universe/lean/QOU/Mathlib/HadamardFactorization.lean`
**Blocks:** the `PentagonRigidity.uniqueUpToScalar` entire leg (see
`docs/audits/2026-07-20-pentagon-entire-leg.md`).

## Why this theorem

The residual leg of `uniqueUpToScalar` reduces (PR #4120 +
`MeromorphicSameOrder.lean`) to: the canonical minimal Faddeev solution
`phiBProd` is selected among all `phiBProd·(elliptic)` multiples by a
growth/minimality principle. That principle is a special case of the **Hadamard
factorization theorem** — an entire function of finite order `ρ` equals
`exp(g)·∏ₙ Eₚ(z/aₙ)` with genus `p ≤ ρ` and `deg g ≤ ρ`. No elliptic factor can
appear because the product is canonical and `g` is a polynomial.

## Mathlib v4.24.0 gap survey (grep-confirmed)

**Mathlib HAS:**
- `Analysis/Complex/JensenFormula.lean` — Jensen's formula (the zero-counting input).
- `Analysis/Complex/ValueDistribution/{Characteristic,Counting,Proximity}Function.lean`,
  `FirstMainTheorem.lean` — Nevanlinna theory (partial).
- `Analysis/Complex/Liouville.lean`, `Analysis/Analytic/{Order,IsolatedZeros}.lean`,
  `Analysis/Meromorphic/{Order,TrailingCoefficient}.lean` — order of zeros/poles.
- Infinite products: `Multipliable`/`HasProd`/`∏'`, `MultipliableUniformlyOn.lean`,
  `SpecialFunctions/Log/Summable.lean` — the log-summability product criterion.
- `Complex.exp` (nonvanishing, entire), `Polynomial`.
- `Analysis/Complex/Hadamard.lean` — **the three-lines theorem, NOT factorization.**

**Mathlib LACKS (the gap):**
- The **Weierstrass primary factor** `Eₚ(z) = (1−z)·exp(∑_{k≤p} zᵏ/k)`.
- **Order of growth** `ρ` of an entire function; **genus**; **exponent of
  convergence** of the zero set.
- The **canonical product** `∏ₙ Eₚ(z/aₙ)` and its convergence theorem.
- **Hadamard's factorization theorem** itself.

So the gap is the entire Weierstrass-product → Hadamard chain; the ingredients
(Jensen, Nevanlinna, log-summable products, analytic order) are present but
uncombined.

## What landed here (PI-1)

Proved **sorry-free** (elementary first bricks):
- `weierstrassFactor p z` — the definition.
- `weierstrassFactor_apply_zero` : `Eₚ(0) = 1`.
- `weierstrassFactor_genus_zero` : `E₀(z) = 1 − z`.
- `weierstrassFactor_eq_zero_iff` : `Eₚ(z) = 0 ↔ z = 1` (exp nonvanishing).
- `differentiable_weierstrassFactor` : each `Eₚ` is entire (`fun_prop`).
- Definitions `IsEntireOfOrderLE f ρ` (finite order via `‖f z‖ ≤ A·exp(C·‖z‖^ρ)`)
  and `IsGenus a p` (minimal `p` with `∑ ‖aₙ‖^{−(p+1)}` summable).

Stated **precisely, cited `sorry`** (NOT vacuous, NOT axiomatized-as-proved):
- `norm_one_sub_weierstrassFactor_le` — Weierstrass estimate `‖1−Eₚ(z)‖ ≤ ‖z‖^{p+1}`
  for `‖z‖ ≤ 1` (convergence-critical).
- `multipliable_canonicalProduct` — canonical product convergence given genus ≤ p.
- `hadamard_factorization` — **the stated-open core**.

## Tractable-brick roadmap

| Brick | Statement | Difficulty | Depends on |
|-------|-----------|-----------|-----------|
| PI-2 | `norm_one_sub_weierstrassFactor_le` | medium | nonneg-coeff series `Eₚ = 1 − ∑_{k>p} aₖzᵏ`, `aₖ ≥ 0`, `∑ aₖ = 1` |
| PI-3 | `multipliable_canonicalProduct` | medium | PI-2 + `Summable.multipliable` / log-summability |
| PI-4 | order/genus: `genus ≤ ρ`, exponent-of-convergence ≤ order | medium-hard | Jensen's formula (present) + counting |
| PI-5 | `hadamard_factorization` (the core) | hard, multi-week | PI-2..4 + Nevanlinna + Borel–Carathéodory |

PI-2 and PI-3 are the natural next independent PRs (pure Weierstrass-factor
analysis, no Nevanlinna). PI-5 is the deep theorem and the true unlock for the
pentagon leg.

## Verification note

Local `lean`-direct verification requires the whole `Analysis` cone, which is
**absent** from the QOU olean cache (`lake-cache/qou-v4-24-0` is a partial
758-olean algebra/combinatorics build with **zero** `Mathlib/Analysis` oleans).
The cone was built from pinned mathlib source in-session (node22 present; `npm
ci` for ProofWidgets JS succeeded; `lake exe cache get` is network-blocked but
the source build is not) — the same route recorded in `MeromorphicSameOrder.lean`.
CI carries full mathlib. The three `sorry`s are the stated-open bricks above; the
rest checks sorry-free.
