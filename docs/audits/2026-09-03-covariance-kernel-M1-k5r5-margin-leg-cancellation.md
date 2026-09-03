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

### What that forbids

Multiplying the two, a budget that bounds `ρ_P`, `V_D` and `V_A` separately and adds via the triangle
inequality can overshoot the true deviation by **roughly an order of magnitude** — against the **46×**
total headroom (PR #6500), that is most of the available room.

> **So the rigorous argument must be built to PRESERVE these cancellations, not to bound the three
> ingredients independently.** That is a constraint on the *shape* of the proof, not merely on its
> constants — and it is the first such constraint this arc has measured.

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
worth a factor of a few — but **not** the full order of magnitude the two cancellations are jointly
worth. The rest lives in the **leg-vs-leg** cancellation, which a ratio bound does not capture;
recovering it needs `ρ_P` and the σ-ratio handled *together*, not two tight bounds added.

Stated explicitly so the next attempt does not spend its effort on the ratio alone and expect the
whole factor back.

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

Each time the arithmetic *within* each object was right, which is what let them through. The guard
already recorded — *"`V_A`, `σ_A`, `σ_D/σ_A` and `m` are four different objects; write the conversion
down"* — is necessary but was not sufficient: #4 was not a missing conversion factor but a **missing
term**. The stronger guard: **before comparing two quantities, enumerate everything that feeds each
one, and check the lists match.**

## Status of `qou-k5r5`

Gap **OPEN**. The requirement is unchanged (`C ≤ 2.6681` at the proved `n^{-1/2}` shape, empirical
envelope 0.0580). What is newly known: the binding ingredient is **`V_D`**, and the proof must keep
the `ρ_P`/`σ` and `V_D`/`V_A` cancellations intact rather than bounding ingredients separately.

## Cross-references

- Total headroom and the corrected requirement: PR #6500 / [`…-margin-envelope-retraction.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md)
- The unit error and the `C_A` conversion: [`…-pointwise-shortfall-recomputed.md`](2026-09-03-covariance-kernel-M1-k5r5-pointwise-shortfall-recomputed.md)
- The rigorous `V_D` ceiling (leading order): `…_VD_ceiling_rigorous.py`
- Epic `qou-x631`; gap `qou-k5r5`.
