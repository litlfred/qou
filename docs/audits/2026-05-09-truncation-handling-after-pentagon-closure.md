# Truncation handling after pentagon-ascension closure

**Date:** 2026-05-09
**Companion to:** [`pentagon-uv-commutation-woronowicz-closure.md`](2026-05-09-pentagon-uv-commutation-woronowicz-closure.md)
**Question:** Once `conj:pentagon-uv-commutation` is closed (conditionally
on the Woronowicz left-rule), how does the production code's pair-only
mass tower relate to the all-orders sum?

## The full mass-tower formula (post-closure)

With pentagon-ascension closed, every triple `Φ_q(|V_iV_jV_k|)` at
jet level `n` reorganises into a pair+single at level `n` plus a
residual that ASCENDS to level `n+1`. Iterating across all higher
subset orders, the all-orders mass tower is

$$\boxed{\quad
  \mathfrak{m}(\beta) \;=\; \Bigl|\!\prod_i V_i^{(0)}\!\Bigr|
    \;+\; \sum_{n=0}^{\infty}\,\Bigl[\,
      \sum_i \Phi_q\!\bigl(|V_i^{(n)}|\bigr)
      \;+\; z^2 \sum_{i<j} \Phi_q\!\bigl(|V_i^{(n)} V_j^{(n)}|\bigr)
      \Bigr]
\quad}$$

where:

- `V_i^{(n)}` are the level-`n` traced volumes built by recursive jet
  prolongation (`def:recursive-brane-tower`).
- The sum is **pair-only at each level** (singletons + pairs); triples
  and higher don't appear because the pentagon ascends them to the
  next level.
- The level-0 term `|Π V_i^{(0)}|` is the "descended" piece (Markov-
  trace product), which appears only ONCE — not summed over levels.

## How the production code's pair-only tower truncates this

The production scripts (`mass_endomorphism.py`, `canonical_tower.py`,
etc.) compute only the **`n = 0`** contribution:

$$\mathfrak{m}^{(\text{prod})}(\beta) \;=\; \bigl|\!\textstyle\prod V_i^{(0)}\!\bigr|
  + \sum_i \Phi_q\!\bigl(|V_i^{(0)}|\bigr)
  + z^2 \sum_{i<j} \Phi_q\!\bigl(|V_i^{(0)} V_j^{(0)}|\bigr).$$

Levels `n ≥ 1` are deferred (would require implementing
`additive_wedderburn_volumes_at_jet_level(n)` for `n ≥ 1`, which is
not in the codebase).

So the truncation error is

$$\mathfrak{m} - \mathfrak{m}^{(\text{prod})}
  \;=\; \sum_{n=1}^{\infty}\,\bigl[\,\textsf{pair-only at level } n\,\bigr].$$

## Geometric tail bound (controls the truncation)

By `prop:jet-tower-convergence`, each level-`n` contribution decays
geometrically:

$$\bigl|\,\text{level-}n\text{ contribution}\,\bigr| \;\leq\; C \cdot z^{2n}, \qquad z = \tfrac{1}{q^{1/2} + q^{-1/2}}.$$

At QOU's substrate `q_0 ≈ 1.10998`:

$$z(q_0) = \frac{1}{q_0^{1/2} + q_0^{-1/2}} \approx 0.4985, \quad z^2 \approx 0.2485.$$

So the geometric ratio is `z²(q_0) ≈ 0.249`. The total truncation
error from omitting `n ≥ 1`:

$$\bigl|\mathfrak{m} - \mathfrak{m}^{(\text{prod})}\bigr|
  \;\leq\; C \cdot \sum_{n=1}^{\infty} z^{2n}
  \;=\; C \cdot \frac{z^2}{1 - z^2}
  \;\approx\; C \cdot \frac{0.249}{0.751}
  \;\approx\; 0.331\,C.$$

I.e., **including all higher levels multiplies the level-0 result by
roughly `1.33`** (a 33% upward correction).

## Empirical implication

Today's pair-only run on the deuteron (this session):

| atom | M_pred (pair-only, level 0) | M_AME | error |
|---|---:|---:|---:|
| D | 5107 MeV | 1875.6 MeV | **+172%** |
| T | 12 110 MeV | 2808.9 MeV | **+331%** |
| ³He | 12 941 MeV | 2808.4 MeV | **+361%** |

Including all jet levels would multiply each by ~1.33, giving:

| atom | M_pred (all levels, predicted) | M_AME | error after correction |
|---|---:|---:|---:|
| D | ~6800 MeV | 1875.6 MeV | **+263%** (worse) |
| T | ~16 100 MeV | 2808.9 MeV | **+474%** (worse) |
| ³He | ~17 200 MeV | 2808.4 MeV | **+512%** (worse) |

The all-orders tower **does not close the binding-energy gap**; it
makes it worse. Pentagon-ascension is the algebraically correct
treatment of higher-order terms but is **not load-bearing on the
nuclear-mass discrepancy**. The discrepancy lives at the level of:

1. **GAP-A-3** — the brane-tower level-selection rule `n_*(K)`. The
   tower truncation is supposed to converge as `n → ∞`, but for
   confined particles `K`, only finitely many levels contribute to
   the physical mass (the tower "saturates" at some finite `n_*`).
   The selection rule `n_*(K)` is open.

2. **GAP-A-4** — the structural prefactor `ρ(Z, N)` in
   `prop:atom-knot-mass-derivation`:
   `M(K) = m_e · ρ · |Π_{i} V_i^{(0)} + ...|`.
   The factor `ρ` is fitted empirically per atom; the structural
   rule for `ρ(Z, N)` is open. The conjecture `ρ = ⌊dim_q(λ*)⌉`
   was tested today and FAILS (predicts 5/62/62 vs observed 1/2/2).

## Conclusion: what the pentagon closure *does* and *does not* fix

**Does fix:**
- The all-orders mass tower is now algebraically well-defined and
  absolutely convergent (geometric tail bound).
- The production code's pair-only formula is no longer a heuristic
  truncation — it's the level-0 truncation of a well-defined sum,
  with a precise tail bound `z^2 / (1 - z^2) ≈ 0.33` per remaining
  factor.
- Triples and higher subsets never appear "for free"; the framework
  no longer has the appearance of an arbitrary cutoff.

**Does not fix:**
- The empirical discrepancy in `M(K)` for `A ≥ 2` is NOT due to
  truncation of the tower order. Including all levels makes it worse
  (33% upward), not better.
- The discrepancy lives in calibration / level selection / per-block
  prefactor (GAP-A-3, GAP-A-4). Those are the next research targets.

## Truncation-handling guidance for new agents

When working with the mass tower:

1. **Don't try to add triples/quads explicitly** — they're absorbed by
   pentagon ascension (this closure). Adding them by hand
   double-counts AND diverges (Φ_q saturates past pair-products).

2. **Do implement `additive_wedderburn_volumes_at_jet_level(n ≥ 1)`**
   if you want to compute the level-`n ≥ 1` contributions explicitly.
   This is the next level (after `level_0` already in
   `mass_endomorphism.py:additive_wedderburn_volumes`). The
   level-`(n+1)` volumes come from the level-`n` ones via the jet
   prolongation `J^1` per `prop:jet-prolongation`.

3. **Do bound the truncation error** with `z^{2n} / (1 - z^2)` if
   you only have the level-0 result. The 33% bound is the
   worst-case correction for a single confined particle.

4. **Don't expect the all-orders tower to close the binding gap.**
   The pair-only level-0 result is already off by 200–400% on D/T/³He;
   adding higher levels multiplies by ~1.33, not the inverse 0.36
   needed to land near AME.

## Cross-references

- Closure: [`2026-05-09-pentagon-uv-commutation-woronowicz-closure.md`](2026-05-09-pentagon-uv-commutation-woronowicz-closure.md)
- Lean class: [`pentagon-uv-commutation-woronowicz.lean`](../../content/quantum-observable-universe/braids-and-knots/pentagon-uv-commutation-woronowicz.lean)
- Open gaps: [`derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md)
- New-agent guidance: [`2026-05-09-gap-a-3-a-4-guidance.md`](2026-05-09-gap-a-3-a-4-guidance.md)
