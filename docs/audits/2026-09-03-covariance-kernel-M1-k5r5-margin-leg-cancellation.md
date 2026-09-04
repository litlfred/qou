# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: two cancellations in the margin, and what they forbid

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-rigorous-C-2026-09-03` · **PR:** #6528 ·
**Tier:** measurement + correction of a claim made earlier in the same PR · **Epic:** `qou-x631`; gap `qou-k5r5`.

## The finding

The margin deviation splits **exactly** — this is a rearrangement, not an asymptotic:

> `m(n) − m_∞ = [ρ_P(n) − ρ_∞] − [√(V_D/V_A)(n) − σ_ratio,∞] =: L_ρ(n) − L_σ(n)`

Computed from exact `Fraction` covariances over all partitions of `n` for `4 ≤ n ≤ 40`
([`…_margin_leg_decomposition.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_margin_leg_decomposition.py),
exit 0, 10 s, NO float64), the identity closes to `0.0` at every `n`.

**There are two cancellations, and together they constrain the shape of any rigorous proof.**

### Cancellation 1 — between the legs

`|L_ρ − L_σ| / (|L_ρ| + |L_σ|)` over `n ≥ 16`: **min 0.2238, max 1.0**. At its worst the two legs
cancel to 22 % of their sum — a **4.5× loss** if they are bounded separately and added.

### Cancellation 2 — inside `L_σ`, between `V_D` and `V_A`

Linearising `√(V_D/V_A) ≈ σ_∞(1 + (δ_D − δ_A)/2)` with `δ_X` the relative deviation of `V_X/n²`
(prediction tracks `L_σ` to a few percent — the residual is the second-order term):

| n | `δ_A` | `δ_D` | `δ_D − δ_A` | `|δ_D|+|δ_A|` | inner cancel |
|---|---|---|---|---|---|
| 12 | −0.11768 | −0.13625 | −0.018574 | 0.25393 | 0.0732 |
| 24 | −0.061753 | −0.087413 | −0.025660 | 0.14917 | 0.1720 |
| 36 | −0.037244 | −0.058810 | −0.021565 | 0.096054 | 0.2245 |
| 40 | −0.036893 | −0.058358 | −0.021465 | 0.095251 | 0.2254 |

`δ_D` and `δ_A` carry the **same sign** and largely cancel in the difference: ratio **0.108–0.226**
over `n ≥ 16`, a further **4.4–9.3× loss** if `V_D` and `V_A` are bounded independently.

### What that costs — measured, after an overstatement of mine in this same PR

**First version of this section, and it was wrong:** *"Multiplying the two, a budget that bounds `ρ_P`,
`V_D` and `V_A` separately and adds via the triangle inequality can overshoot the true deviation by
roughly an order of magnitude — against the 46× total headroom, that is most of the available room. So
the rigorous argument must be built to PRESERVE these cancellations… a constraint on the shape of the
proof."*

**The defect: I multiplied two worst cases instead of measuring the composite.** The two cancellations
are not independent, and their worst cases fall at different `n`, so the product double-counts.

Measured directly
([`…_naive_budget_closes_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_naive_budget_closes_probe.py),
exit 0, NO float64), comparing the true deviation `|m(n) − m_∞|` against the naive bound
`|L_ρ| + (σ_∞/2)(|δ_D| + |δ_A|)` — exactly what a proof gets if it reports one constant per ingredient
and adds them:

| quantity | value |
|---|---|
| pointwise `LOSS = NAIVE/TRUE`, `n ≥ 16` | 4.141 … 25.59 (max at `n = 16`) |
| `C_true = max TRUE·√n` | **0.0579688** (at `n = 22`) |
| `C_naive = max NAIVE·√n` | **0.279796** (at `n = 22`) |
| envelope loss `C_naive/C_true` | **4.8267×** |
| headroom left, naive budget | **9.5359×** (`C_target/C_naive`, `C_target = 2.66812`) |

The pointwise loss *does* reach 25.6× — but at `n = 16`, where `TRUE` is anomalously small
(`0.0017666`, a near-crossing), and that `n` does not govern the envelope. **The envelope loss is
4.83×, not an order of magnitude.**

> **So preserving the cancellations is an OPTIMISATION worth ~5×, not a structural requirement.** The
> triangle inequality alone does **not** exclude the easy route: it leaves **9.54×** of the 46×
> headroom. The earlier "constraint on the shape of the proof" is withdrawn.

**What remains genuinely open** is whether a *rigorous* per-ingredient constant fits in that 9.54×.
Every constant above is an **empirical sup over `n ≤ 40`**, and a rigorous constant must hold for all
`n`, so `C_naive = 0.2798` is a **floor** on what the easy route would report — enough to *exclude* the
easy route had it exceeded 2.6681, not enough to establish it. It does not.

### So what should be bounded?

The cancellation says: not `V_D` and `V_A` separately. The natural candidate is the **ratio
`V_D/V_A` as one object**. Measured (exact, not the linearisation) against `(V_D/V_A)_∞ = σ_∞² =
0.461869183`:

| n | `|δ_A|` | `|δ_D|` | `|δ_ratio|` | gain vs `δ_D` |
|---|---|---|---|---|
| 18 | 0.062293 | 0.085562 | 0.024814 | 3.448 |
| 24 | 0.061753 | 0.087413 | 0.027349 | 3.196 |
| 36 | 0.037244 | 0.058810 | 0.022400 | 2.625 |
| 40 | 0.036893 | 0.058358 | 0.022288 | 2.618 |

**Gain over `n ≥ 16`: 2.61× to 4.85×.** So bounding the ratio directly *is* the right target and is
worth a factor of a few — but not the whole 4.83× composite loss. The rest lives in the **leg-vs-leg**
cancellation, which a ratio bound does not capture; recovering it needs `ρ_P` and the σ-ratio handled
*together*, not two tight bounds added.

Stated so the next attempt does not spend its effort on the ratio alone and expect the whole factor
back — and, equally, so it does not conclude it *must* do either. 4.83× out of 46× still leaves 9.54×.

## Correction to a claim earlier in this same PR

Earlier in #6528 I concluded, from the poissonized large-θ ingredients, that **"`ρ_P` is the bigger
leg and `V_A` the small one"**, and recommended budgeting with `ρ_P` as the binding constraint.

**That is wrong.** It compared `ρ_P`'s *full* deviation (`0.1329/θ`) against only the **`V_A` part**
of the σ-ratio leg (`0.003251/√θ`) — **`V_D` was never in the comparison.** Measured here at fixed
`n` with exact arithmetic, `|L_σ|` exceeds `|L_ρ|` by **4× to 700×**:

| n | 6 | 12 | 18 | 24 | 30 | 36 | 40 |
|---|---|---|---|---|---|---|---|
| `|L_ρ|/|L_σ|` | 1.885 | 0.152 | 0.127 | 0.0222 | 0.243 | 0.00148 | 0.0269 |

So the **σ-ratio leg dominates**, and `V_D` — not `ρ_P`, not `V_A` — is the binding ingredient.

**What survives from that earlier commit:** the conversion `C_margin,A = 0.41922·C_A` and the ~821×
headroom on the `V_A` leg. Both are correct statements *about the `V_A` leg*. What was wrong is the
claim about where the binding constraint sits.

**Why the two measurements disagreed** is worth keeping: one is poissonized and asymptotic (θ), the
other exact and finite-`n`. They should be quoted separately — but the disagreement here is not the
θ↔n difference, it is the omitted `V_D` term, which no de-poissonization could account for.

## The pattern this session, stated plainly

Four corrections in one day, and **all four are one error**: comparing quantities that belong to
different objects.

| # | claim | defect |
|---|---|---|
| 1 | `C ≤ 23.4` (#6500) | `V_A`'s rate used as a premise about the margin |
| 2 | `~17×` short (#6528) | relative error on `V_A` vs an absolute margin |
| 3 | `C_A` vs `C ≤ 2.668` | phrasing only — verdict was unit-correct (no number derived) |
| 4 | "`ρ_P` is the binding leg" (#6528) | `ρ_P`'s full deviation vs only part of the other leg |
| 5 | "cancellations cost ~an order of magnitude" (this doc, above) | **product of two worst cases** instead of the measured composite (4.83×) |

Each time the arithmetic *within* each object was right, which is what let them through. The guard
already recorded — *"`V_A`, `σ_A`, `σ_D/σ_A` and `m` are four different objects; write the conversion
down"* — is necessary but was not sufficient: #4 was not a missing conversion factor but a **missing
term**. The stronger guard: **before comparing two quantities, enumerate everything that feeds each
one, and check the lists match.**

**#5 is a different failure and needs its own guard.** It compares nothing; it *combines*. Two
correctly-measured worst-case ratios were multiplied into a composite that was never measured, and the
product came out ~2× too pessimistic because the two effects are not independent and peak at different
`n`. The guard: **a bound composed from other bounds is a hypothesis, not a measurement — measure the
composite before quoting it, especially when the quoted number is about to change a recommendation.**
Here it did: it turned an optimisation worth 5× into a claimed constraint on the shape of the proof.

## Status of `qou-k5r5`

Gap **OPEN**. The requirement is unchanged (`C ≤ 2.6681` at the proved `n^{-1/2}` shape, empirical
envelope 0.0580). What is newly known:

1. The binding ingredient is **`V_D`** — not `ρ_P`, not `V_A`.
2. The two cancellations cost a per-ingredient budget **4.83×** at the envelope level, leaving
   **9.54×** headroom. Preserving them is an optimisation, **not** a requirement on the proof's shape.
3. So the **easy route is not excluded**, and the live question is narrower than it was this morning:
   *can a rigorous per-ingredient bound on `ρ_P`, `V_D` and `V_A` land within 9.54× of the empirical
   sups?* That is a question about the looseness of a Debye/Olver-style argument, and it is the one
   the next attempt should answer first, because it is cheaper than building a cancellation-preserving
   proof and it decides whether that harder proof is needed at all.

## Cross-references

- Total headroom and the corrected requirement: PR #6500 / [`…-margin-envelope-retraction.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md)
- The unit error and the `C_A` conversion: [`…-pointwise-shortfall-recomputed.md`](2026-09-03-covariance-kernel-M1-k5r5-pointwise-shortfall-recomputed.md)
- The rigorous `V_D` ceiling (leading order): `…_VD_ceiling_rigorous.py`
- Epic `qou-x631`; gap `qou-k5r5`.
