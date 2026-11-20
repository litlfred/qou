---
# qou-jbbk
title: 'The building-block-knots Jones tables do not hold together: two printed values are unattainable by their own polynomials, and seven rows carry a q^{1-g^2} shift'
status: todo
type: task
priority: normal
tags:
    - observations
    - reorg-2026-10-04
    - knot-theory
    - numerics
created_at: 2026-08-22T06:45:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

Found by `agent:pq_03` on the `observations/` trap-drain and **re-derived
independently in the coordinating session**. Two blocks are involved and they
are inconsistent with each other as well as with the standard invariants:

- [`building-block-knots-table1-data.md`](../folio/quantum-observable-universe/observations/building-block-knots-table1-data.md) — the polynomials
- [`building-block-knots-table5-data.md`](../folio/quantum-observable-universe/observations/building-block-knots-table5-data.md) — their values at `q₀`

## 1. Two printed values are outside the range of the polynomial that is supposed to produce them

This is the strongest form the finding can take, because it needs **no `q₀`
pin at all** — it holds for every real `q > 0`, so no producer-input question
can rescue it.

**Figure-eight.** Table 1 gives `J_{4₁} = q⁻² − q⁻¹ + 1 − q + q²`. Put
`u = q + q⁻¹`, so `q² + q⁻² = u² − 2` and

    J_{4₁} = (u² − 2) − u + 1 = u² − u − 1.

For real `q > 0`, `u ≥ 2` by AM–GM, and `u² − u − 1` is increasing there
(derivative `2u − 1 > 0`), so **`J_{4₁} ≥ 1`, with equality only at `q = 1`**.
Table 5 prints **`0.7854`**, which is below the minimum — and is `π/4` to five
decimals (`0.7853982`).

**Mirror trefoil.** Table 1 gives `J_{3₁^σ} = −q⁴ + q³ + q`. At `q = 1` this is
`1`, with `f′(1) = −4 + 3 + 1 = 0` and `f″(1) = −6 < 0`; and `f′(q) = 1 + 3q² −
4q³` is positive on `(0,1)` (since `4q³ < 4q² < 1 + 3q²` when `q < 1`) and
negative for `q > 1`. So **`1` is the global maximum on `q > 0`**. Table 5
prints **`3.5832`**.

## 2. Five of the six rows in table 5 fail; the sixth is the unknot

Evaluated at the proton pin `q₀ = 1.1099785827513808`, using table 1's own
polynomials:

| row | table 5 | computed at `q₀` |
|---|---|---|
| `0₁` unknot | `1.0000` | `1` — trivially, for any `q` |
| `3₁` | `0.8168` | **0.973370** |
| `3₁^σ` | `3.5832` | **0.959577** (= `J_{3₁}(1/q₀)`, as a mirror should be) |
| `4₁` | `0.7854` | **1.032809** |
| `5₁` | `0.4854` | **0.929906** |
| `L2a1` Hopf | `−2.2662` | **−2.351590** as written |

(The original report said "zero of six reproduce"; the unknot row does
reproduce, trivially. **Five of six** is the accurate count.)

One tell in the printed numbers: `0.8168 + 3.5832 = 4.4000` exactly. The
computed pair sums to `1.932947`. A knot and its mirror satisfy
`J_{K*}(q) = J_K(q⁻¹)`, which the computed pair does satisfy and which places
no constraint anywhere near `4.4`.

## 3. Every torus-knot row past the trefoil carries a spurious `q^{1−g²}` factor

Comparing table 1's exponent ranges against the standard Jones polynomials:

| row | table 1 exponents | standard | shift | `1 − g²` |
|---|---|---|---|---|
| `3₁` (g=1) | `−4 … −1` | `−4 … −1` | **0** | 0 |
| `5₁` (g=2) | `−10 … −5` | `−7 … −2` | **−3** | −3 |
| `7₁` (g=3) | `−18 … −11` | `−10 … −3` | **−8** | −8 |
| `T_{2,9}` (g=4) | `−28 … −19` | `−13 … −4` | **−15** | −15 |

The trefoil, the only row with `g = 1` and therefore shift 0, is the only
correct one. Spans are right in every row (`span J = c` for an alternating
link, and these are alternating with `c = 3, 5, 7, 9`), which is part of why
this survived — and the larger part is that **a shift does not change `J(1)`**,
so all rows still pass the `J(1) = 1` sanity check.

Separately, `T_{3,4} = 8₁₉` is given a six-term polynomial
`q⁻⁷ − q⁻⁶ + q⁻⁵ − 2q⁻⁴ + q⁻³ + q⁻¹`. The Jones polynomial of the `(3,4)`-torus
knot is the three-term `q³ + q⁵ − q⁸` (up to mirror). The printed six-term
polynomial also evaluates to `1` at `q = 1`, so it passes the same check.

## 4. And a volume in the neighbouring table

[`building-block-knots-table3-data.md`](../folio/quantum-observable-universe/observations/building-block-knots-table3-data.md)
gives the Solomon link `L4a1` hyperbolic volume `≈ 6.45`. `L4a1` is the
`(2,4)`-torus link; its complement is Seifert-fibered and admits no hyperbolic
structure, so the volume is **0** — which the adjacent Hopf-link row gets right,
for exactly the same reason. The Whitehead (`3.6639 = 4G`) and Borromean
(`7.3277 = 8G`) rows in that table are correct.

## Disposition

Not attempted here, because it is not a transcription fix. Three separate
questions have to be settled before the tables can be regenerated:

1. **Which convention table 1 is in.** A uniform `q^{1−g²}` factor across the
   torus family is too systematic to be typos; something produced it. Whatever
   that was, it is not the Jones polynomial, and the blocks label it `J(q)`.
2. **What table 5 evaluated.** Its numbers are not table 1's polynomials at any
   pin, and two of them are not attainable by those polynomials at all — so it
   is not a pin-currency defect and must not be filed as one.
3. **Whether anything downstream reads these.** The particle assignments in
   table 1 (`ν`, `e⁻`, `μ⁻`, `τ⁻`, gluon, `8₁₉` as "Hopf² color binding") are
   cited elsewhere in the framework; the polynomials and the particle column
   should be checked for whether they are separable.

The cheap general lesson, worth carrying into other numeric passes: **before
checking a printed invariant against a `q₀` pin, check whether the polynomial
can take that value at all.** The range test is stronger, costs one
substitution, and is independent of which producer wrote the number.

## 2026-08-22 — main landed a mirror fix in the knot-polynomial engine. It does NOT cover this.

46 commits reached `main` while this branch was open, three of them on
knot-polynomial correctness and all naming the same class:

```
03ced1383  fix(homflypt): correct the 2-strand table — it was the mirror, plus a sign
b26356283  lean(qou-7ue5): validate the skein reference — the engine is a MIRROR
01d4fab3d  fix(homflypt): remove the silent spread-0 trap; flag a mirror discrepancy
```

A chirality defect in a knot-invariant engine is close enough to this bean that
someone will reasonably assume it is the same root cause. **Checked: it is not.**

```
J(3_1)(q0)   = 0.97337017
J(3_1)(1/q0) = 0.95957717   <- the mirror
printed pair = 0.8168 / 3.5832
```

Mirroring maps between the two computed values, and neither is a printed one.
For `4_1` it cannot even do that: the figure-eight is **amphichiral**, so its
mirror is identical (`1.0328093` either way) — and the range argument stands
regardless, since `J_{4_1} = u^2 - u - 1 >= 1` for every real `q > 0` while the
table prints `0.7854`. No chirality convention reaches a value the function does
not take.

So the homflypt fix and this bean are **adjacent, not overlapping**. Worth
saying explicitly, because "the engine was returning mirrors" is exactly the
kind of upstream fix that gets assumed to have swept a downstream table, and
these six values would still be wrong afterwards.

`main` touched none of this bean's files (`building-block-knots-table{1,3,5}-data`),
so nothing here is stale.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8480, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
