# The `c₁`/`c₂` crossover is grouped-specific — #6559's central finding does not survive the Borromean ruling

**Corrects two merged documents of mine**, and completes step 4 of bean
`qou-j1e5`. Beans `qou-j1e5` / `qou-hu1f` / `qou-brng`.

## What changed underneath these documents

`7db032fb48` (owner ruling, bean `qou-hu1f`) changed `atom_braid_word_3A`'s
default intra-nucleon ordering from `grouped` to `borromean`. The `c_k` in
[`2026-09-03-c1-leading-order-vs-uic-flatness.md`](2026-09-03-c1-leading-order-vs-uic-flatness.md),
[`2026-09-04-c2-does-not-continue-the-cancellation.md`](2026-09-04-c2-does-not-continue-the-cancellation.md)
and
[`2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md`](2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md)
are the `ℏ_q`-expansion coefficients of `Δtr` — **the same objects** as the
`c1_*` defs in `QOU.MassTheory.PairwiseChainLeadingOrder`. They all move, and
`c₁(⁴He)` moves by a factor of **37**, from `259/128` to `7/128`.

## Measured — the crossover table under both orderings

Re-running `c1_leading_coefficient_derived_probe` on `main` (525 s, complete)
gives the Borromean coefficients. Weighted by `ℏ_q = 0.099081716044258508`
(proton pin), the ratio `c₂·ℏ² / c₁·ℏ` that #6559 was built on:

| case | A | `c₁` grouped | `c₂` grouped | **ratio** | `c₁` borro | `c₂` borro | **ratio** |
|---|---|---|---|---|---|---|---|
| pp | 2 | 19/8 | 357/32 | 0.4654 | 1/8 | 33/32 | **0.8174** |
| pn | 2 | 37/16 | 403/32 | 0.5396 | 1/16 | 25/32 | **1.2385** |
| nn | 2 | 9/4 | 217/16 | 0.5972 | **0** | 1/16 | **INFINITE** |
| T | 3 | 163/64 | 3285/128 | 0.9984 | 1/64 | 99/128 | **4.9045** |
| ³He | 3 | 85/32 | 3451/128 | 1.0057 | 1/8 | 157/128 | **0.9722** |
| ⁴He | 4 | 259/128 | 15307/512 | 1.4639 | 7/128 | 439/512 | **1.5535** |

## The finding: #6559's argument was carried entirely by the ordering

**#6559's headline** was that the ratio column is *monotone through 1*:

```
A = 2   0.465, 0.540, 0.597     second order is about half the first
A = 3   0.998, 1.006            the two orders are EQUAL
A = 4   1.464                   second order EXCEEDS the first by half
```

and it concluded *"the `ℏ_q` expansion crosses over between A = 3 and A = 4 and
stops being an expansion"*.

**Under the canonical Borromean word none of that holds.** The column is
`0.817, 1.239, ∞, 4.905, 0.972` — not monotone, not ordered by `A`, and already
at or past 1 at `A = 2`.

Three specific claims fail:

1. **"At A = 2 this looks like an expansion should."** It does not: `pn` is
   already `1.24` and `nn` is infinite.
2. **"Two independent cases agreeing to 0.8 %, so it is signal, not scatter."**
   The two `A = 3` cases are `4.905` and `0.972` — a factor of **5** apart. That
   0.8 % agreement was the load-bearing evidence for reading the `A = 3` row as
   a crossing, and it is gone.
3. **"The crossover is driven by `c₁` falling, not `c₂` rising."** The mechanism
   claim is moot once the pattern it explains is absent.

**`nn` is the sharpest case and is not a large ratio but an undefined one.**
`c₁(nn) = 0` exactly under the Borromean word, so there is no first order for a
second order to be compared against. A ratio test cannot be applied at all
there.

## What is NOT established

- ~~**The `A = 4` crossover is unsettled, not refuted.**~~ **🛑 SETTLED
  2026-09-06 — bean `qou-yaig`, and the answer splits in two.** This bullet said
  `c₂(⁴He)` was untested because the committed `P_OF["4He"] = 3` returns `None`.
  It has now been measured at `P = 4` (295 s):

      c2(4He) borromean = 439/512      ratio c2·ℏ² / c1·ℏ = 1.5535

  The **endpoint fact SURVIVES**: at `A = 4` the second order does exceed the
  first, and by *more* than under grouped (1.4639). The **location does NOT**:
  "crosses over *between* `A = 3` and `A = 4`" also requires the ratio to be
  below 1 underneath, and under Borromean it is already `4.9045` at `T` (`A = 3`)
  and `1.2385` at `pn` (`A = 2`). There is no crossing *there*.

  Three controls passed before the new number was trusted — `a₀ = 7/128` against
  the derived floor two ways, and `a₁ = 7/128` against the `c₁(⁴He)` of #6931,
  which **independently confirms the one row that PR's own probe could only
  assert circularly**.
- ~~**`c₃` is not re-measured at all.**~~ **🛑 SETTLED 2026-09-06 — bean
  `qou-yaig`
  ([`2026-09-06-c3-under-borromean-the-second-order-is-the-only-bad-one.md`](2026-09-06-c3-under-borromean-the-second-order-is-the-only-bad-one.md)).**
  Measured across all six cases (`pp 67/16`, `pn 43/8`, `nn 27/4`, `T 101/16`,
  `³He 839/128`, `⁴He 1329/256`; and at fourth order `c₄`: `pp -585/128`,
  `pn 109/192`, `nn 27/32`, `T 743/384`, `³He 10001/1536`, `⁴He 43079/6144`).
  #6607's conclusion that order 3 shrinks relative to order 2 (`c₃·ℏ³ / c₂·ℏ²`
  = `0.4023, 0.6817, 10.7008, 0.8087, 0.5295, 0.5999`) **survives** on the five
  cases where `c₁ ≠ 0` — the second order is an isolated jump caused by small
  Borromean `c₁`, not the onset of divergence.
- **This says nothing about the physics.** Scope-(a). It is a statement about
  which of two braid-word conventions a series-ordering argument was computed
  in.

## What survives, and it is not nothing

The **`c₀` floor is ordering-invariant** — `a0 = c0` passes under both orderings
in every case (`1/8` at `A = 2`, `3/32` at `A = 3`, `7/128` at `A = 4`). So the
classical-floor result those documents rest on is untouched; it is only the
`ℏ_q^1` and `ℏ_q^2` structure above it that moves.

And the sibling conclusion in `PairwiseChainLeadingOrder.lean` — that the
pairwise chain over-counts, and by `24/7` at ⁴He — **survives and is now
proved** rather than measured (`chain_over_atom_He4_of_letters`, sorry-free).
The two results were always independent; this is a reminder that "the ordering
changed" does not imply "everything downstream fell over".

## My share of this

I wrote #6559 and #6607. Both were computed on `main`'s then-default ordering
without pinning it, which is the same defect `qou-j1e5` records for the probe
itself — and I documented that defect in #6905 and #6919 while leaving my own
earlier documents unrevisited. The corpus-grep discipline is about not
re-deriving what exists; this is its mirror, and it has no checklist: **when a
convention you depend on is ruled, go back through what you wrote under the old
one.**
