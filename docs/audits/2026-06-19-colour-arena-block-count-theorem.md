# Colour-arena missed-block COUNT theorem — formalize-first (2026-06-19)

**Branch:** `claude/serene-cerf-j4d339` (PR #2500). Owner-directed item 1 of "1 2 3".
**Discipline:** formalize-first (§3.3), tiered status, critical-distance, **no fit**.
**Upgrades:** [`2026-06-16-keystone-arena-is-full-hecke-not-su3.md`](2026-06-16-keystone-arena-is-full-hecke-not-su3.md)
(#2406) from an empirical observation to a structural theorem at the block-count level.

## The claim being upgraded

The production nuclear-mass trace is the **full Hecke / Wenzl principal specialization**
`s_λ(1, q, q², …)`, nonzero for **every** partition `λ`. A finite colour arena `ℂ^N`
realizes the `N`-variable specialization `s_λ(1, q, …, q^{N−1})`, which by the **Schur
row-bound**

> `s_λ(x₁, …, x_N) = 0 ⟺ rows(λ) > N`

vanishes on every partition with more than `N` rows. So a finite `ℂ^N` **misses** the
trace content carried by the `>N`-row Wedderburn blocks. The #2406 audit records the
*weighted* miss-share growing with the mass number `A`:

| nucleus | `A` | weighted miss vs full Hecke (SU_q(3), `N=3`) |
|---|---|---|
| (small) | — | `0.2%` |
| (mid) | — | `1.1%` |
| ⁴He | 4 | `3.4%` |
| ⁵He | 5 | `6.0%` (prior-session profile) |

**Two/three data points are not a theorem.** This audit records what *is*.

## What is PROVABLE (the block-count backbone) — THEOREM

Verifier: [`docs/audits/scripts/colour_arena_missed_block_count.py`](scripts/colour_arena_missed_block_count.py)
(exit 0, `n ≤ 14`, `N ∈ {2,3,4}`). Lean (sorry-free):
[`QOU/BraidsAndKnots/ColourArenaBlockCount.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ColourArenaBlockCount.lean).

Write `#missed(n, N) = #{λ ⊢ n : rows(λ) > N}` (the blocks a colour-`ℂ^N` arena kills).

- **B1 — row-bound** `s_λ(N vars) = 0 ⟺ rows(λ) > N` (verified `n=5,6`; classical
  [macdonald1995] I.3). This is the **premise** that turns "rows > N" into "killed by
  `ℂ^N`".
- **B2 — injection lower bound** `#missed(n, N) ≥ p(n − N − 1)`, via
  `appendUnitRows N : μ ↦ μ ++ (1^{N+1})` — appending `N+1` unit rows (extend the
  first column downward by `N+1` boxes). The witness is **canonical**
  (weakly-decreasing) since every part of `μ` is `≥ 1`. Every `μ ⊢ (n−N−1)` maps to
  a distinct `λ ⊢ n` with `rows(λ) = rows(μ) + (N+1) > N`.
  *Lean:* `appendUnitRows_length`, `appendUnitRows_sum`, `appendUnitRows_missed`,
  `appendUnitRows_injective`, bundled as `missedEmbedding` / `missedEmbedding_injective`.
- **B3 — monotone in n** `#missed(n, N) ≤ #missed(n+1, N)`, via `λ ↦ add one box to
  row 1` (preserves row count, `+1` to size, injective).
- **B4 — unbounded** `#missed(n, N) → ∞` (immediate from B2: `p(n−N−1) → ∞`).
- **B5 — captured fraction `→ 0`** `#{rows ≤ N}/p(n) → 0` for every fixed `N`
  (partitions into `≤ N` rows are `Θ(n^{N−1})`; `p(n)` is super-polynomial).

Observed counts (verifier), the **monotone, unbounded** missed-block growth:

```
   n  |  N=2   N=3   N=4   | p(n)        captured frac (N=2): 0.667 → 0.059
   3  |    1     0     0   |    3        captured frac (N=3): 1.000 → 0.178
   6  |    7     4     2   |   11        captured frac (N=4): 1.000 → 0.348
  10  |   36    28    19   |   42
  14  |  127   111    88   |  135
```

**Verdict:** *no finite `N` captures the full-Hecke trace for all `A`* is now a
theorem (block-count level), not an extrapolation from 2–3 nuclei. The nucleus braid
sits at `n = 3A`, so the missed-block count grows monotonically and without bound in `A`.

## What stays EMPIRICAL (and why that is correct)

The literal **weighted** miss-share monotonicity `3.4% (⁴He) → 6.0% (⁵He)` is **not**
formalized and should **not** be stated as a theorem. It depends on:

1. **q₀** — the principal-specialization weights `s_λ(1, q₀, q₀², …)` evaluate at the
   substrate anchor (fibre-level / archimedean, per the Im(q) two-level rule).
2. **the nucleus-specific braid** `β_A` — the characters `χ_λ(β_A)` carry **signs** that
   oscillate with the braid word; a heavier nucleus is a different braid, not a
   refinement of the lighter one.

So the weighted share is the **weighted face** of the count backbone, not a corollary of
it. Enshrining "weighted miss is monotone in A" as structure would be a fit (a refuted-
shape risk in reverse). The count backbone B1–B5 is the rigorous content; the percentages
illustrate it numerically at the physical anchors. (Mirror of the honest split in the
sibling [`2026-06-19-delta-lambda-exponent-keystone-formalize-first.md`](2026-06-19-delta-lambda-exponent-keystone-formalize-first.md):
provable arithmetic core vs conjectural/contested bridge.)

## Consequence for the keystone (item 3 link)

This gives **C6 ("full support — all `p(n)` partitions, no selection rule") of
[`2026-06-16-keystone-index-necessary-conditions.md`](2026-06-16-keystone-index-necessary-conditions.md)
teeth**: the support is not merely full but *unboundedly* full for any finite arena, so a
candidate geometric index reproducing `W_λ` must carry **all** `p(3A)` blocks — a
finite-dimensional (finite-`N` colour) Sasakian is ruled out *quantitatively*, not just
by the single `3.4%` data point. The infinite-dimensional construction itself stays
owner-gated (subgoal-2 decline, 2026-05-08); this audit only tightens the necessary
conditions it must satisfy.

## Net

`no finite colour arena` is now a block-count theorem (B1–B5, Lean sorry-free for B2–B5,
B1 cited + numerically verified). The weighted percentage is its empirical face and is
deliberately **not** promoted to a theorem. The geometric keystone is unaffected and
remains open.
