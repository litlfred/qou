# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: retracting my `C ≤ 23.4`, and measuring the headroom the route actually has

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-p2-trace-split-orders-2026-09-03` · **PR:** #6500 ·
**Tier:** correction of merged content (PR #6469, repeated in five further places), with the
replacement figure measured rather than assumed · **Epic:** `qou-x631`; gap `qou-k5r5`.

## What I claimed, and what is actually true

PR #6469 (merged, `51bc3bd`) introduced this sentence, and five further sites repeat it:

> **Closure arithmetic improves accordingly.** At `θ^{-1}`, `m(n) ≥ m_∞ − C/n > 0` needs only
> `N₀ = ⌈C/m_∞⌉ ≤ 78`, i.e. **`C ≤ 23.4`** — far weaker than the `C ≤ 2.65` a conservative
> `n^{-1/2}` reading demands.

**It is wrong, and the arithmetic in it is fine — which is what made it survive.** Two defects, of
different kinds:

**1. Wrong object.** The `θ^{-1}` rate is the measured decay of
`d(θ) = V_A(θ)/θ² − 8/π²`, the remainder of the **poissonized `Σ|c|` variance**. The quantity that
has to stay positive is the **(CS) margin**

> `m(n) = ρ_P(n) − σ_D(n)/σ_A(n)`

— a **ratio of square roots** of two variances, plus a correlation, at **fixed `n`** rather than at
Poisson parameter `θ`. A rate on one variance's remainder is not a rate on the margin: the ratio,
the square root, and de-poissonization each contribute their own corrections, and **nobody has
propagated the one into the other.** I used the `V_A` rate as a premise about `m(n)`.

**2. Mislabelled the proved bound.** What is actually proved (PR #5929) is

> `|m(n) − m_∞| ≤ C·n^{-1/2}`,

whence `N₀ = (C/m_∞)²` — **squared** — and the requirement is `C ≤ m_∞·√79 = 2.6681`. My sentence
called `2.65` *"a conservative `n^{-1/2}` reading"*. It is not a reading of anything: it is **the**
requirement matching the bound in hand, and it was already recorded as `C_TARGET` in
[`…_constant_C_landscape.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_constant_C_landscape.py),
whose docstring states it explicitly. A corpus-grep of my own epic would have caught this.

## The measurement ([`…_margin_envelope_exponent.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_margin_envelope_exponent.py), exit 0, NO float64)

`m(n)` is computed exactly (`Fraction` covariances over all partitions of `n`; `mpmath` only for the
square roots and display) for `4 ≤ n ≤ 46`, ~33 s.

**Why not fit the exponent from the oscillation's peaks.** `m(n) − m_∞` has sign runs
`n = 4…6` (−), `7…12` (+), `13…15` (−), `16…46` (+). So one local maximum — `n = 14`,
`|dev| = 0.001854` — is the top of a **narrow sub-lobe ~7× below the outer envelope**, and the final
positive run is **double-humped** (peaks at 21 and 38). Consecutive-peak exponents come out
**6.2, −4.7, 0.73**: noise. Hand-dropping the `n=14` sub-lobe to rescue the fit would be choosing
the data to fit, so the running maximum is used instead — it needs no peak classification.

**Running max of `|m − m_∞|·n^p` over the measured window `[N, 46]`.** A *falling* column means `p`
is too small; a *flat* column means `p` is consistent with the data.

| from `N` | `max |dev|·√n` (p = ½) | `max |dev|·n` (p = 1) |
|---|---|---|
| 4 | 0.199865 | 0.399731 |
| 6 | 0.087084 | 0.315118 |
| 10 | 0.0843586 | 0.315118 |
| 13 | **0.0579688** | 0.315118 |
| 20 | 0.0579688 | 0.315118 |
| 30 | 0.0504593 | 0.315118 |

- **`p = ½` falls by ~3.4×.** The proved `n^{-1/2}` shape is **not tight** — the margin decays
  strictly faster.
- **`p = 1` is flat from `N = 6`** at 0.315118 (attained at `n = 39`), i.e. consistent with `n^{-1}`.

**So the `n^{-1}` shape I assumed is empirically supported for the margin.** It was still wrong to
report the closure arithmetic as though that were established — and the evidence has a limit worth
stating: over `n ≤ 46` the data **excludes `n^{-1/2}` decisively** but does **not** cleanly separate
`n^{-1}` from a slightly slower power. `|dev|·n` at the outer peaks drifts *up* ~18 % (0.2613 at
`n=9`, 0.2636 at 21, 0.3094 at 38), and the `p=1` column is flat only because its supremum sits at an
interior `n=39` inside every window. Empirical envelope ≠ rigorous constant; that distinction is the
entire content of this gap.

## What this does to the route — it strengthens it

The correction removes a number I had no right to, and the honest replacement is *better news* than
the one it replaces, because it needs no improvement to the proved shape at all:

> Under the **already-proved** `n^{-1/2}` bound, the requirement is `C ≤ 2.6681` while the empirical
> envelope over `n ≥ 13` is `C_emp = 0.0580`. **Headroom: 46×.** (`N₀` at `C_emp` would be `0.037`,
> i.e. closure from `n ≥ 1`.)

A rigorous constant landing **within 46× of the truth** closes M₁>0 for all `n`. That — not the
retracted `C ≤ 23.4` — is the real statement that *a crude bound suffices*, and it is the corpus's
own position: `finite_n_cs_margin.py` already says the remaining requirement is an effective
variance bound *"large enough (leading margin 0.30) that a crude rate suffices"*. My recommendation
in PR #6500's chat that we pivot to a crude bound was therefore **not a new idea** — it restates what
the epic already held, and I should have cited it rather than proposed it.

## Blast radius — every site, and its disposition

| site | status | disposition |
|---|---|---|
| [`…_em_osc_constant_prediction.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_em_osc_constant_prediction.py) docstring | merged #6469 | **rewritten** with both defects named |
| same, printed output line | merged #6469 | **rewritten**; prints the retraction |
| [`…-weight-bug-retraction-retracted.md`](2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md) §closure | merged #6469 | correction block appended |
| same, §Status | merged #6469 | struck and corrected inline |
| [`…-tv-gpp-is-ill-posed.md`](2026-09-03-covariance-kernel-M1-k5r5-tv-gpp-is-ill-posed.md) §Status | merged #6472 | struck, correction block appended |
| [`…-p2-trace-split-refuted.md`](2026-09-03-covariance-kernel-M1-k5r5-p2-trace-split-refuted.md) | **unmerged** (#6500) | struck, correction block appended |
| bean `qou-k5r5` | — | corrected by append |
| bean `qou-tvok` | — | corrected by append |

Audit docs are **annotated, not rewritten** — they are dated records of what was believed, and the
repo's convention is to leave the original text visible with the correction beside it. The probe is
fixed at the producer, since it *prints* the claim on every run.

## What is NOT affected

Everything else from #6469 and #6500 stands and is independent of this arithmetic:

- the `θ^{-1}` rate of `V_A`'s remainder and `c₁ ≈ −0.0678` (measured, reproduces
  `…_tvok_remainder_rate.py` exactly);
- the weight-bug correction itself (`k(k+1)/2` with signed `k` on the shifted lattice);
- P2's refutation, and the `α = 0.429421692` continuum cross-check to 3.3e−10;
- `TV(g″)`'s ill-posedness (`c(ρ) = +∞`).

## Status of `qou-k5r5`

Gap **OPEN**, and better-scoped than before. The remaining step is unchanged in kind and now has a
number attached: produce a **rigorous** `C` in `|m(n) − m_∞| ≤ C·n^{-1/2}` with `C ≤ 2.6681`, against
an empirical envelope of 0.0580 — 46× of slack. That is Bessel(Olver) / sine(Debye) / Airy(BDJ)
constant-tracking, as `constant_C_landscape.py` has said all along.

## Cross-references

- The retracted claim's origin: PR #6469 / [`…-weight-bug-retraction-retracted.md`](2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md)
- The proved `n^{-1/2}` bound: PR #5929; the target constant: `…_constant_C_landscape.py`
- The margin's oscillation: `…_finite_n_cs_margin.py`
- Epic `qou-x631`; gap `qou-k5r5`; child `qou-tvok`.
