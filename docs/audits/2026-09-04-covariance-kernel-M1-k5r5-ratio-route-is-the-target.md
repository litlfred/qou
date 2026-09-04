# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: bound `ρ_P` and `V_D/V_A`, not three ingredients — 40.5× headroom, and it is nearly lossless

**Date:** 2026-09-04 · **Branch:** `claude/m1-k5r5-envelope-convergence-2026-09-04` ·
**Tier:** measurement + retraction of a claim merged yesterday (#6528) · **Epic:** `qou-x631`; gap `qou-k5r5`.

## The finding

The margin is `m = ρ_P − √(V_D/V_A)`. A rigorous finite-`n` bound can be assembled from bounds on
**three** ingredients (`ρ_P`, `V_D`, `V_A`) or on **two** (`ρ_P` and the ratio `V_D/V_A` as a single
object). Measured at the envelope level, over `n ≥ 16` in a window reaching `n = 46`
([`…_ingredient_envelope_convergence.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_ingredient_envelope_convergence.py),
exit 0, exact `Fraction` covariances over all partitions, NO float64):

| budget, in margin units at the proved `n^{-1/2}` rate | value | waste vs `C_true` | headroom vs `C_target = 2.66812` |
|---|---|---|---|
| `C_ρ` (enters linearly) | 0.0122554 | — | — |
| `C_A` (× `σ_∞/2`) | 0.113046 | — | — |
| `C_D` (× `σ_∞/2`) | 0.162893 | — | — |
| **three-ingredient**: `C_ρ + C_A + C_D` | **0.288194** | 4.972× | **9.258×** |
| `C_ratio` (× `σ_∞/2`) | 0.0536527 | — | — |
| **ratio route**: `C_ρ + C_ratio` | **0.0659081** | **1.137×** | **40.482×** |
| `C_true` = `max |m − m_∞|·√n` | 0.0579688 | 1.000× | 46.027× |

> **The ratio route wastes 1.137× and keeps 40.5 of the 46× headroom.** Bounding `ρ_P` and
> `V_D/V_A` separately and adding is *nearly lossless*.

This is the actionable output: the right analytic target is a rigorous finite-`n` bound on the
**ratio** `V_D/V_A`, together with one on `ρ_P` — not on `V_D` and `V_A` individually, and not a
bespoke argument that keeps `ρ_P` and the σ-ratio coupled.

### The same budget at the `n^{-1}` rate — the smaller of the two levers

Not proved (the proved shape is `n^{-1/2}`, PR #5929), but the envelopes are consistent with it. At
`|m − m_∞| ≤ C'/n` the requirement is `N₀ = C'/m_∞ ≤ 79`, i.e. `C' ≤ m_∞·79 = 23.7147` — a **linear**
relaxation, not a square-root one:

| budget at `p = 1` | value | headroom |
|---|---|---|
| three-ingredient | 1.37319 | 17.27× |
| **ratio route** | **0.352994** | **67.182×** (waste 1.12×) |
| `C'_true` | 0.315118 | 75.257× |

**Order the two levers correctly.** Moving from the three-ingredient budget to the ratio route is
worth **4.37×** at `p = 1/2`; moving from `p = 1/2` to `p = 1` is worth only **1.66×** (40.48 →
67.18). Do the ratio bound first.

*(This table is computed inside the probe rather than assembled by hand from the running-max tables.
Assembling it by hand once, in chat, gave 89× instead of 67.2× — running-max values from two
different `N` were combined. That is the same failure class as the retraction below, which is why the
arithmetic lives in the producer.)*

## Retraction of a claim merged yesterday

[`…-margin-leg-cancellation.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-leg-cancellation.md)
(#6528) states, and the leg-decomposition probe printed on every run:

> *"…bounding the ratio directly **is** the right target and is worth a factor of a few — but not the
> whole composite loss. The rest lives in the **leg-vs-leg** cancellation, which a ratio bound does
> not capture; recovering it needs `ρ_P` and the σ-ratio handled *together*, not two tight bounds
> added."*

**Two tight bounds added cost 1.137×.** There is essentially nothing left in the leg-vs-leg
cancellation to recover.

**Why it is wrong, and the reason is structural rather than arithmetic.** The leg-vs-leg cancellation
ratio `|L_ρ − L_σ|/(|L_ρ| + |L_σ|)` does dip to 0.2238 pointwise — that measurement stands. But a
cancellation between two terms can only cost a budget when the two terms are *comparable*. At the
envelope level they are not: `C_ρ = 0.0123` is **23 %** of `C_ratio = 0.0537`, so discarding the
cancellation between them can cost at most ~1.2× whatever the pointwise dips look like. The
cancellation that genuinely mattered was the *inner* one, `V_D` against `V_A` — and bounding the ratio
captures exactly that one, which is why it recovers almost everything.

## A smaller self-correction in the same direction

#6528 reported the three-ingredient budget as **0.279796** (headroom 9.536×); this reports
**0.288194** (headroom 9.258×). Both are correct and they are different objects:

- 0.279796 = `max_n [ NAIVE(n) · √n ]` — the **sup of the sum**;
- 0.288194 = `C_ρ + C_A + C_D`, each a sup in its own right — the **sum of the sups**.

Sum-of-sups ≥ sup-of-sum, and **the sum of sups is what a per-ingredient proof actually reports**:
each ingredient gets one constant valid for all `n`, and those are then added. So 0.288194 / 9.258× is
the faithful figure and 0.279796 slightly understated it. Quote the former.

## The envelopes are settled — which is what licenses reading these sups as extrapolations

Every headroom figure in this arc assumes the empirical envelopes have settled into decay over the
accessible window rather than still growing. Nothing had checked it. Running maximum of `|Q(n)|·n^p`
from `N` upward (a running max, not consecutive-peak fitting: these sequences oscillate and one lobe
is double-humped, which turned peak-ratio exponents into noise in #6500):

| p | `L_ρ` | `δ_A` | `δ_D` | `δ_R` | margin |
|---|---|---|---|---|---|
| **1/2** | FALLING 0.815 | FALLING 0.730 | FALLING 0.737 | FALLING 0.740 | FALLING 0.650 |
| **1** | FLAT 0.962 | FALLING 0.793 | FALLING 0.801 | FALLING 0.803 | FALLING 0.706 |

(ratio = last/first over the window's final third.) Nothing is RISING, so each sup over the window
**over-estimates** the sup over `n ≥ 79` — the conservative direction. `L_ρ` being FLAT at `p = 1`
says `ρ_P`'s deviation is `Θ(n^{-1})`; the variances decay faster still.

**This does not make any of it a bound.** The window ends at `n = 46` and the constant is required
only for `n ≥ 79` (`n ≤ 78` is certified exhaustively — see below). Every figure here is an
extrapolation and is labelled as one.

## Confirming the `n ≤ 78` premise rather than inheriting it

`C_target = m_∞√79 = 2.66812` presumes exhaustive verification covers `n ≤ 78`. Five sites in the
corpus assert this and **none of them is the artifact** — one of the five is a probe of mine from
yesterday that took the figure from the others. Checked:
`computations/deltalambda/b1-kappa-window-extension.witness.json` (`allPassed: true`, exact `Fraction`
Plancherel summation over every partition, mpmath at 60 dps for the comparison, no float64) certifies
`κ_n ≥ κ = 128/(225π²) > 0` at every `n` in a window extending past `n ≤ 67` to `n = 78`.

**The premise holds and `C ≤ 2.6681` stands.** Recorded because a chain of five mutually-citing
assertions is exactly the shape that survives review while resting on nothing — here it happened to
rest on something.

## Where this leaves the gap

Gap **OPEN**. Requirement unchanged: `C ≤ 2.6681` at the proved `n^{-1/2}` shape. What is now known:

1. The right analytic target is **`ρ_P` and the ratio `V_D/V_A`**, bounded separately and added —
   1.137× lossy, 40.5× headroom. Not three ingredients (9.26×), and not a cancellation-preserving
   argument (which buys ≤ 1.14× over the ratio route and is far harder).
2. The **leading order is already rigorous** for the binding side:
   [`…_VD_ceiling_rigorous.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_VD_ceiling_rigorous.py)
   proves `V_D < 64/(75π²)` by certified interval arithmetic plus an explicit analytic tail majorant,
   using the elementary closed forms `Â_k = 8(−1)^{(k+1)/2}/(π(k²−4))` and
   `Ô_k = (8/π²)[1/k − 1/(2(k−2)) − 1/(2(k+2)) + 1/(2(k−2)²) − 1/(2(k+2)²)]` for
   `V_D = Σ_{k odd ≥ 3} (Ô_k − Â_k)²/k`.
3. So the one open input is the **finite-`n` rate** for that Fourier-side sum — and specifically for
   the *ratio*, which is a different and empirically much better-behaved object than either variance.

**The next step** is a rigorous finite-`n` bound on `V_D/V_A`. Whether the Fourier structure in (2)
extends to a finite-`n` remainder with an explicit constant is not settled here and is not claimed.

## Cross-references

- The budget that this supersedes: [`…-margin-leg-cancellation.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-leg-cancellation.md) (#6528)
- The requirement and the total headroom: [`…-margin-envelope-retraction.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md) (#6500)
- The `n ≤ 78` certification: `wlambda_covariance_epic_B1_kappa_window_extension.py`
- Epic `qou-x631`; gap `qou-k5r5`.
