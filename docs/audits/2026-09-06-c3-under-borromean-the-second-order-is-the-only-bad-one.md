# `c₃` under Borromean: the second order is the only bad one — #6607's conclusion survives

Completes bean `qou-yaig`, the takeover of the two items PR #6931 left open.
Companion to
[`2026-09-06-the-c1-c2-crossover-is-grouped-specific.md`](2026-09-06-the-c1-c2-crossover-is-grouped-specific.md).

## Measured — both order-ratios under the canonical Borromean word

Exact `Fraction` extraction, `ℏ_q = 0.099081716044258508` (proton pin). Every
case reproduced its already-recorded `c₀`, `c₁` **and** `c₂` before its `c₃` was
read; `c₂(⁴He)` was measured separately at `P = 4` in the same bean.

| case | A | `c₁` | `c₂` | `c₃` | `c₂ℏ²/c₁ℏ` | `c₃ℏ³/c₂ℏ²` |
|---|---|---|---|---|---|---|
| pp | 2 | 1/8 | 33/32 | 67/16 | 0.8174 | **0.4023** |
| pn | 2 | 1/16 | 25/32 | 43/8 | 1.2385 | **0.6817** |
| nn | 2 | **0** | 1/16 | 27/4 | INFINITE | **10.7008** |
| T | 3 | 1/64 | 99/128 | 101/16 | 4.9045 | **0.8087** |
| ³He | 3 | 1/8 | 157/128 | 839/128 | 0.9722 | **0.5295** |
| ⁴He | 4 | 7/128 | 439/512 | *(P=5)* | 1.5535 | *(open)* |

## The finding: the expansion overshoots once and then settles

Read the two ratio columns together — that is the whole result, and neither
column says it alone.

- **First → second order overtakes.** Four of five finite ratios are at or above
  1 (`1.24`, `4.90`, `1.55`, with `0.82` and `0.97` just below).
- **Second → third order does NOT.** Four of five are well *below* 1 — `0.40`,
  `0.68`, `0.81`, `0.53`.

So this is **not** a divergent expansion with each order beating the last. It has
**one bad order**, the second, after which the terms resume shrinking. That is
exactly the shape `2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md`
(#6607) concluded from the **grouped** word — its ⁴He ratio was `247.98·ℏ/29.8965
= 0.8219`, likewise below 1.

**So #6607's conclusion survives the ordering change**, at the `A` values reached
here. That is worth stating plainly because its two predecessors did not:
#6559's argument was refuted outright (#6931) and its crossover *location* is
false, while the endpoint held. Three documents, three different fates.

## `nn` is the outlier at both orders, and it is the degenerate case

`nn` is the sole ratio above 1 in the `c₃` column (`10.7008`), and it was the
sole *infinite* one in the `c₂` column. Both have the same cause: **`c₁(nn) = 0`
exactly** under the Borromean word. A case whose first order vanishes has no
scale for the later orders to be measured against, so its ratios say something
about the vanishing and not about convergence. It should be read out of the
trend, not into it.

## 🛑 What is NOT established

- **`A = 4` is still open for `c₃`, and that is where #6607's interest lies.**
  `c₃` needs `d.p > 3`, hence `P ≥ 5`; committed `P_OF["4He"] = 3`. It is
  excluded deliberately: `P = 4` at `n = 12` cost 295 s with the `[8,4]` and
  `[7,5]` Wedderburn blocks alone at 50 s and 59 s, so `P = 5` is a separate
  long-compute run under the tee-and-progress discipline, not something to bury
  inside a five-case sweep. **This settles `A = 2` and `A = 3` only.**
- **Five points is a shape, not a convergence proof.** "Overshoots once and
  settles" is a description of orders 1–3 at two values of `A`. Nothing here
  bounds `c₄` or beyond, and the `c₄` that `pp/pn/nn` could supply at their
  committed `P = 6` was not extracted.
- **Scope-(a).** A statement about a series ordering in one braid-word
  convention, not about the physics.

## Provenance of the comparison figure

The grouped ⁴He ratio `0.8219` is computed here from the two values #6607 records
(`c₂ = +29.8965`, `c₃ = +247.98`); it is not quoted from that document, which
reports the comparison in its own terms. The grouped `c₃` for `A = 2` and `A = 3`
was **not** re-derived, so the row-by-row grouped-vs-Borromean comparison this
table invites for `c₂` is not available for `c₃`.
