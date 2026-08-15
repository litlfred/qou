---
# qou-pjx4
title: sigma^2 unbinding is framing-dependent; even-NEGATIVE stacking unbinds after writhe normalisation (scope-a, magnitudes still 6-9x)
status: todo
type: task
created_at: 2026-08-15T23:24:55Z
updated_at: 2026-08-15T23:24:55Z
---


## The finding

`InterfaceScalar.lean::stacked_crossing_gt_one` gives `sigma^2` the interface
scalar `mu = h*z + 1 = 1.12809 > 1`, and
[`2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`](../docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md)
reads it as the corpus's **only** route to an unbound channel — projectors give
`mu < 1` always (`mu_sum_eq_one`), so unbinding requires leaving the convex
decomposition of `1`.

That reading uses the **raw** `mu`. `_bond_type_L` — the production path —
applies the writhe normalisation, equivalently `mu_eff = mu*(1-h)^(e/2)`.
Since the normalisation is what makes the invariant Markov-invariant, an
unbinding claim true for `mu` and false for `mu_eff` is a property of the braid
**word**, not the link.

| power | `mu_raw` | `mu_eff` | unbound raw | unbound eff |
|---|---|---|---|---|
| +2 | 1.128089 | 0.892250 | yes | **no** |
| +4 | 1.305482 | 0.816691 | yes | **no** |
| −2 | 0.915617 | 1.157632 | no | **yes** |
| −4 | 0.871253 | 1.392700 | no | **yes** |
| −6 | 0.864968 | 1.748114 | no | **yes** |
| −8 | 0.896487 | 2.290712 | no | **yes** |

**10 of 16 verdicts flip.** Every positive power is bound after normalisation;
the even negative powers are unbound. Unbinding is **relocated**, not lost, and
the sign of the unbinding crossing is opposite to the corpus's reading.

## Scope — (a), narrow

- `stacked_crossing_gt_one` is `1 < h*z+1` for `0 < z,h`: arithmetic, **stands**.
- Unbinding is **not** excluded — it is available at even negative powers.
- Even-negative stacking is **not** proposed as the physical interface.
  `sigma^-2` gives `B_eff = -0.613 MeV` vs nature's `pp ~ -0.1`, `nn ~ -0.1`,
  `pn 1S0 ~ -0.066`: right sign, **6–9x too large**.
- Odd negative powers past −5 are not uniformly interpretable: `sigma^-7` has
  `mu = -0.1508 < 0`, so `B = -alpha*ln(mu)` is undefined.

## Two corrections to my own work in one probe

1. I first reported "the writhe normalisation kills unbinding entirely." **False**
   — it relocates it.
2. The cause was a hand-derived recurrence for negative powers that was wrong
   (`mu(-2) = 0.7438`; correct `0.9156`, since
   `sigma^-2 = (sigma-h)^2 = -h*sigma + 1 + h^2`). It produced a plausible-looking
   but spurious "unbinding at −4 only" pattern. The probe now multiplies in the
   2-dim subalgebra and **asserts `sigma * sigma^-1 = 1`**, so that error class
   aborts instead of printing a believable table.

## Open question this raises

The corpus assigns `pp = sigma` (`d = 0`) and `nn = sigma^-1` (`d = -h`). If
unbinding lives at even *negative* stacking, the natural next question is whether
the three physically-unbound channels (pp, nn, pn 1S0) sit at negative stacked
powers while the deuteron (pn 3S1) does not — i.e. whether the bound/unbound
split is a **writhe-parity** statement. Not tested; the magnitudes above say it
would not close quantitatively as-is.
