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
| ⁴He | 4 | 7/128 | 439/512 | **1329/256** | 1.5535 | **0.5999** |

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

## `A = 4` — measured, and #6607's conclusion holds at its own headline case

An earlier revision of this document listed `A = 4` as open, because `c₃` needs
`d.p > 3`, hence `P ≥ 5`, against a committed `P_OF["4He"] = 3`. That run has now
been done (352 s at `P = 5`, under the tee-and-progress discipline), and all
three controls reproduced — `a₀`, `a₁`, and the `c₂ = 439/512` measured
separately at `P = 4`:

    c3(4He) = 1329/256      ratio c3·ℏ³/c2·ℏ² = 0.5999

So the third order does **not** overtake the second at `A = 4` either. That is
#6607's own headline case, and **its conclusion holds under the canonical word**
— its grouped ⁴He ratio was `247.98·ℏ/29.8965 = 0.8219`, likewise below 1.

**The `c₃` column has no `A` trend at all.** `0.4023, 0.6817, 0.8087, 0.5295,
0.5999` across `A = 2, 3, 4` — flat in the 0.4–0.8 band, with no ordering by
`A`. That is a sharper statement than "comparable": the ratio is not drifting
toward 1 as `A` grows.

## `c₄` at all three `A` — the settling is a property of the expansion

The `c₄` that `pp/pn/nn` supply free at their committed `P = 6` has also been
extracted, because the one-bad-order reading otherwise rested on a **single**
step of settling, and one step down is what a fluctuation looks like:

    case      c3          c4        c3ℏ³/c2ℏ²   c4ℏ⁴/c3ℏ³
    pp      67/16     −585/128        0.4023     −0.1081
    pn       43/8      109/192        0.6817      0.0105
    nn       27/4       27/32        10.7008      0.0124

Two consecutive steps down, and the second is a **collapse** rather than a
drift — roughly forty times smaller than the `c₃/c₂` step.

**Extended to `A = 3` and `A = 4`** (465 s at `P = 6`, twelve controls, every
case reproducing its recorded `c₀, c₁, c₂, c₃` first), the `c₄` column is
complete:

| case | A | `c₄` | `c₄ℏ⁴/c₃ℏ³` |
|---|---|---|---|
| pp | 2 | −585/128 | −0.1081 |
| pn | 2 | 109/192 | 0.0105 |
| nn | 2 | 27/32 | 0.0124 |
| T | 3 | 743/384 | 0.0304 |
| ³He | 3 | 10001/1536 | 0.0984 |
| ⁴He | 4 | **43079/6144** | **0.1338** |

Every `A` collapses. So the one-bad-order shape is a property of **the
expansion**, not an artefact of the two-nucleon case — which is what the `A = 2`
result alone could not say.

### 🛑 But do NOT read an `A` trend into this column

The magnitudes *look* like they rise with `A` — `0.0105, 0.0124` at `A = 2`, then
`0.0304, 0.0984`, then `0.1338`. **They do not support that reading**, because
the scatter *within* a single `A` is as large as the variation *across* `A`:

    within A = 2   0.0105 .. 0.1081   10.3x
    across all A   0.0105 .. 0.1338   12.7x

`pp` alone (`−0.1081`) is larger in magnitude than either `A = 3` value and
comparable to `A = 4`'s. So the honest statement is **scatter in a band below
~0.14 with no clean `A` dependence**, not a rise. This differs from the `c₃`
column, which is genuinely flat (`0.4023 … 0.5999`) rather than merely
trendless-with-scatter.

Two things recorded but **not** built on. `pp`'s `c₄ = −585/128` is the **first
negative coefficient** anywhere in this family — one sign, one order, one `A`,
and no claim about what it means. And `nn` **behaves** at order 4 (`0.0124`),
so its degeneracy appears to wash out; also recorded, also not leaned on.

## 🛑 What is NOT established

- **Nothing here bounds `c₅` or beyond.** Four orders at three values of `A` is
  a better-supported shape than four orders at one, but it is still a shape and
  not a convergence proof. A fifth order would need `P ≥ 7` throughout.
- **`pp`'s `c₄` is the only negative coefficient** in the family, and one sign at
  one order at one case is not a pattern. It is also what breaks the apparent
  `A` trend above, so it is doing real work in the argument and should not be
  quietly dropped as an outlier.
- **Scope-(a).** A statement about a series ordering in one braid-word
  convention, not about the physics.

## Provenance of the comparison figure

The grouped ⁴He ratio `0.8219` is computed here from the two values #6607 records
(`c₂ = +29.8965`, `c₃ = +247.98`); it is not quoted from that document, which
reports the comparison in its own terms. The grouped `c₃` for `A = 2` and `A = 3`
was **not** re-derived, so the row-by-row grouped-vs-Borromean comparison this
table invites for `c₂` is not available for `c₃`.
