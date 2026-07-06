# Per-block c_k^(λ) extraction rule — framework's dim_q² hypothesis falsified; uniform-rule alternative ALSO fails at q_0

**Date:** 2026-05-19
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user direction "2 y" (per-block c_k^(λ) extraction rule). This audit tests the framework's hypothesis from `per-wedderburn-block-c5-c6.md` and the proposed "uniform rule" alternative.

## ⚠ Retraction notice (2026-05-19, evening update)

This audit's original §"Correct rule" section claimed that `c_k = Σ_λ y_λ · c_k^(λ)` with **uniform** `c_k^(λ) ≡ c_k` is the correct rule. **That claim is partially retracted.**

Verified empirically at q_0 across c_2..c_7 in `computations/qbeta/qbeta_per_block_uniform_rule_verify.py` (commit `9146e85f3`):

- The uniform rule works **at q=1** (where Σ y_λ = 1 by Plancherel measure).
- **At q_0 the rule FAILS for all c_k tested** (c_2 through c_7): `Σ y_λ(q_0) ≈ 0.71907 ≠ 1`, so the y_λ-weighted sum of uniform c_k^(λ) = c_k gives `0.719·c_k`, off by ~28%.
- With **normalised** y_λ/Σ y_μ (Plancherel-renormalised), the rule becomes **tautological** — true by construction with no mathematical content.

**Stronger conclusion**: there's **NO non-trivial uniform-per-block c_k decomposition** consistent at q_0. The earlier "correct rule" framing was too optimistic.

The §"Falsification of dim_q² hypothesis" section below remains valid. The framework's `per-wedderburn-block-c5-c6.md` hypothesis is falsified; no replacement rule is known.

## Framework's stated hypothesis (FALSIFIED)

From `content/quantum-observable-universe/braids-and-knots/per-wedderburn-block-c5-c6.md`:

$$
c_k(q_0) \;=\; \sum_{\lambda \vdash 3}\; \dim_q^2(V_\lambda) \cdot c_k^{(\lambda)}(q_0)
$$

**Test at c_3 = J_Hopf(q=1) = −2:** If c_3^(λ) is set to the per-block LO ε^1 coefficient (-2, -1, -2) per `rem:per-block-hopf-jones-absorption-pattern`, the sum is:

$$
1 \cdot (-2) \;+\; 4 \cdot (-1) \;+\; 1 \cdot (-2) \;=\; -8 \;\neq\; -2
$$

**Hypothesis is falsified at c_3.** Even with other per-block assignments (LO/dim, etc.), no simple closed-form choice of c_k^(λ) with dim_q² weighting reproduces c_3 = -2.

## Correct rule

Tested 5 candidate (weighting, per-block) combinations. Only one reproduces c_3:

| Rule | Weighting | c_k^(λ) | Sum at c_3 | Match? |
|------|-----------|---------|-----------:|:------:|
| A | dim_q² | LO ε^1 = (-2, -1, -2) | -8 | ✗ |
| **B** | **y_λ** | **uniform J_Hopf(q=1) = -2** | **-2** | **✓** |
| C | y_λ | LO/dim = (-2, -1/2, -2) | -1 | ✗ |
| D | dim_q | uniform -1 | -4 | ✗ |
| E | y_λ | LO ε^1 = (-2, -1, -2) | -4/3 | ✗ |

**Rule B works because Σ_λ y_λ = 1 at q=1** (Plancherel-like normalisation), so a uniform per-block c_k^(λ) = c_k reproduces the global c_k:

$$
c_k \;=\; \sum_\lambda y_\lambda \cdot c_k^{(\lambda)} \quad \text{with} \quad c_k^{(\lambda)} = c_k \text{ for all } \lambda
$$

## Interpretation

The per-block c_k^(λ) is **block-independent at this level** — the precision-ladder rung's value is a global property, not Wedderburn-decomposable. The per-block structure enters at a DIFFERENT level: in the χ_λ(T_β)(q) character function, where LO ε^1 = (-2, -1, -2) **is** a non-trivial per-block decomposition (per `rem:per-block-hopf-jones-absorption-pattern`).

**Two different "per-block decompositions":**

1. **χ_λ-level decomposition** (real, verified): the character difference χ_λ(β_n − β_p) factors per block, with LO ε^1 = -2, -1, -2 absorbed by dimension-scaling Hopf-Jones.
2. **c_k^(λ)-level decomposition** (trivial at this level): c_k^(λ) = c_k uniformly; no further per-block structure at the precision-ladder coefficient level.

The framework's scaffolding in `per-wedderburn-block-c5-c6.md` conflated these. Its `c_k = Σ dim_q²·c_k^(λ)` hypothesis was speculative and fails the c_3 = -2 test.

## What the per-block structure actually does

The per-block χ_λ closed forms (Hopf-Jones absorption pattern) explain WHY c_k takes specific values at each rung, by tracking how the Markov-trace difference τ_M(β_n − β_p) decomposes into Wedderburn-block contributions. But the GLOBAL precision-ladder coefficient c_k = c_k^(λ) for each block is the SAME number.

This matches the framework's c_3 derivation: **the 2-strand sub-braid argument** (Fact 3 of `q-beta-c3-hopf-three-fold-markov.md`) gives the **single** Hopf-Jones value −2 at q=1, applied uniformly. The per-block decomposition (-2, -1, -2) explains the categorical mechanism but doesn't change the global c_k.

## Recommended next steps

1. **Update `per-wedderburn-block-c5-c6.md`** to reflect that `c_k = Σ_λ y_λ · c_k^(λ)` with uniform c_k^(λ) = c_k. This is a content-block correction.
2. **Lean class instance**: the `PerWedderburnBlockC5C6` class can now have its `defaultPerWedderburnBlockC5C6` instance enriched — with uniform c_k^(λ) = global c_k, both residuals trivially close (no per-block fine-tuning needed).
3. **The OPEN structural question** remains: why do c_4, c_5, c_6, c_7 take their specific empirical values? The per-block decomposition doesn't simplify this; the categorical RULE for higher c_k still requires the Khovanov-Rozansky or KLR-canonical-basis machinery (Paths 2, 3 of the closure roadmap).

## Cross-references

- [`content/quantum-observable-universe/braids-and-knots/per-wedderburn-block-c5-c6.md`](../../content/quantum-observable-universe/braids-and-knots/per-wedderburn-block-c5-c6.md) — framework's hypothesis (needs correction per this audit)
- [`content/quantum-observable-universe/braids-and-knots/per-block-hopf-jones-absorption-pattern.md`](../../content/quantum-observable-universe/braids-and-knots/per-block-hopf-jones-absorption-pattern.md) — per-block χ_λ LO ε^1 = (-2, -1, -2) pattern
- [`content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md) — Fact 3, c_3 derivation
- [`docs/audits/2026-05-19-qbeta-ladder-closure-path.md`](2026-05-19-qbeta-ladder-closure-path.md) — closure-path roadmap for higher c_k

## 2026-05-19 (late evening) — additional y_λ correction

Further discovery during the Path 2 link-Markov-closure exploration:
**y_λ(q=1) is NOT the Plancherel measure (1/6, 2/3, 1/6).** Computed
symbolically from `markov_weights_symbolic.solve_y_lambda(3)`, the
actual values at q=1 are:

| irrep | y_λ(q=1) |
|-------|---------:|
| V_(3) | **1/2** |
| V_(2,1) | **1/4** |
| V_(1,1,1) | **0** |
| **Σ** | **3/4** |

The Wenzl-bridge weights y_λ DON'T sum to 1 even at q=1 — they sum to
3/4. The sign rep V_(1,1,1) **contributes nothing** at q=1.

This further INVALIDATES the earlier "uniform rule trivially works at
q=1 because Σ y_λ(1) = 1" framing. Both Σ y_λ(q_0) ≈ 0.719 AND Σ
y_λ(1) = 0.75 fail the rule (off by 28% and 25% respectively).

**Empirical numerology status confirmed.** Without a first-principles
extraction rule, c_4..c_7 ARE empirical pattern-matches. The framework
proves only c_3 = -2 via Fact 3.

The remaining research-grade paths for c_4..c_7 first-principles:
1. Khovanov-Rozansky polynomial of typed-braid Markov-closure at
   finite q (~1 week+ of focused compute)
2. KLR canonical-basis trace formula (research project scale)

Both beyond single-session scope. **This session establishes the
negative result that per-block decomposition is NOT the route.**
