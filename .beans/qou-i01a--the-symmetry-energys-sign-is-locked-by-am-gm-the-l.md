---
# qou-i01a
title: 'The symmetry energy''s sign is locked by AM-GM: the log-sum wants a geometric mean and the construction delivers an arithmetic one'
status: completed
type: task
priority: normal
created_at: 2026-09-05T08:25:28Z
updated_at: 2026-09-05T08:32:25Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Follows PRs #6777 and
#6783; unifies `qou-q7ga`, `qou-y2np` and the sibling's
`pn-bond-cannot-be-extremal.md` (merged 2026-09-04).

## The reduction

A bond sum is additive in `L = -log b`. For ANY graph and ANY proton/neutron
assignment, with `E = E_pp + E_pn + E_nn`,

    Sigma = (L_pp+L_nn)/2 . E  +  (L_pp-L_nn)/2 . (E_pp - E_nn)  +  delta . E_pn
    delta = L_pn - (L_pp+L_nn)/2

Holding `E` and the imbalance fixed, `Sigma` is affine in `E_pn` with slope
`delta`. A symmetric nucleus maximises `E_pn`, an asymmetric one minimises it, so
the law binds symmetric nuclei more -- the SEMF sign -- exactly when
`delta > 0`. **No layout, graph or scale enters.**

And `delta > 0` is exactly `b_pn < sqrt(b_pp b_nn)`: the log-additive law
compares against a GEOMETRIC mean. The construction delivers an ARITHMETIC one.

## Three exact facts

| quantity | closed form | value at q0 |
|---|---|---:|
| geometric mean | `1/[2]_q` | 0.497290545605 |
| arithmetic mean | `[2]_q/2 - 1/[2]_q` | 0.508155… |
| AM - GM | `([2]_q^2-4)/(2[2]_q) = h^2/(2[2]_q)` | 0.010867342144 |

`h = q - 1/q` is the Hecke parameter itself, so **the AM-GM gap IS the
deformation**. That is `qou-q7ga`'s "the q-deformation is net-negative on
binding" with a mechanism rather than a measurement.

## The crossing weight, and how far off the corpus is

`b_pn = w.b_pp + (1-w).b_nn` with a convex `w` (the sibling's result; verified
numerically here as `0 < w < 1`, not assumed). With the pinned
`b_pp = q^2/[2]_q`, `b_nn = q^-2/[2]_q`:

    delta <= 0   <=>   w >= 1/(q^2 + 1)

    threshold 1/(q0^2+1) = 0.448018144974
    corpus    w          = 0.500343927702   ( = 1/2 + delta_flavour/4 to 6 dp )
    ratio                = 1.1168           -> 11.7 % ABOVE, wrong sign

`1/(q^2+1)` is `1/2` at `q = 1` and strictly below it for every `q > 1`: **the
deformation moves the threshold down and the construction holds the weight at a
half.** So no re-derivation of `q` rescues an equal-weight p-n bond.

## And `qou-y2np`'s bar branch is this family's endpoints

`delta(w=0) = +2 log q0 = +0.20868144063904` and `delta(w=1) = -2 log q0`,
matching that bean's exact figure. Its "one bit" is two points of a continuum,
and the continuum has a derived crossing between them -- which is the finer
object and the one a repair has to hit.

## Artifacts

- `content/quantum-observable-universe/lean/QOU/Hecke/SymmetrySignAmGm.lean`,
  registered in `QOU.lean`. 7 decls, all `[propext, Classical.choice,
  Quot.sound]`, `lean`-direct exit 0, no warnings: `delta_nonpos_iff`,
  `sqrt_mul_le_midpoint`, `delta_midpoint_nonpos`, `crossing_weight`,
  `convex_strictMono`, `crossing_lt_half`, `am_sub_gm_eq`.
- `computations/qbeta/qbeta_symmetry_sign_is_am_gm_locked_probe.py` (9/9,
  40 dps, float64-guard clean).

## What is NOT claimed, and where a successor picks up

The **power**. Turning `E_pn` into the SEMF's `(N-Z)^2/A` needs a well-mixed
assignment (`E_pn ~ 2E.ZN/A^2`), which is a mean-field MODEL. The corpus's
canonical layout is segregated, with `E_pn = 1` and no symmetry term at all. The
sign result needs none of that; the power does.

**Open:** derive the convex weight `w` rather than inherit it. It is `1/2 +
delta_flavour/4` because `d_pn` is built as a centred average of `d_pp` and
`d_nn`; nothing derives that the centring should be at a half. If a derivation
put it below `1/(q^2+1)` the symmetry energy would appear with the SEMF sign for
free. **`w = 1/(q^2+1)` is a target to check a future derivation AGAINST, never
a criterion to search ON.**

## 2026-09-05 (owner: "derive w") — w IS derived; the open premise is the flat 1/2

**`w` is not a free parameter anywhere in the corpus.** The three interface
factors are `f_pp = z` (positive crossing, Markov axiom), `f_nn = z - h`
(negative crossing, Hecke skein) and `f_pn = z - h(1/2 - d/4)`
(`bring_color_weighted`, the default since 2026-06-01). Solving
`f_pn = w.f_pp + (1-w).f_nn` gives `(1-w)h = h(1/2 - d/4)` **identically**, so
`w = 1/2 + d/4`. Verified: `z - h(1/2 - d/4)` equals the corpus's degree-10
closed form for `b_pn` to **0.0 at 40 dps**.

So "derive w" reduces entirely to **deriving the flat 1/2** in
`sigma_avg = (sigma + sigma^-1)/2` (`prop:averaging-resonance-rule`).

## And the flat half is the whole miss

    w - w* = (q^2-1)/(2(q^2+1)) + d/4
             0.051981855026      0.000343927702      ratio 151.14

The ONE derived ingredient in `w` -- the flavour split -- is 151x too small to
matter. The entire miss is an undeformed average used in a deformed algebra.

## Which means could work: exactly those below the geometric

`M_p . M_-p = b_pp.b_nn = GM^2` for every `p`, so `delta(-p) = -delta(p)`.

| p | 3 | 2 | 1 | 0.5 | 0 | -0.5 | -1 | -2 | -3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| delta | -0.0615 | -0.0423 | **-0.0216** | -0.0109 | 0 | +0.0109 | **+0.0216** | +0.0423 | +0.0615 |

The convention sits at `p = +1`; the HARMONIC mean at `p = -1` is its exact
mirror. `M_p` increases in `p` and `M_0` is geometric, so the SEMF sign needs
`p < 0` -- **strictly below the geometric mean, where no average with `p >= 0`
can go.** That closes "just pick a better average" for the whole `p >= 0` half,
including the multiplicative/geometric one that the corpus's own connected-sum
factorisation might otherwise suggest (it gives `delta = 0` exactly -- neutral,
not SEMF).

All three classical means have clean `[2]` forms (`[2]_x = x + 1/x`):

    AM = [2]_{q^2}/(2[2]_q)     GM = 1/[2]_q     HM = 2/([2]_q [2]_{q^2})

and `AM.HM = GM^2` closes the triple.

## ⚠ A pattern I tested and it is NOT one

The three weights are `1/2`, `q^-1/[2]_q`, `q^-2/[2]_{q^2}` -- which look like a
ladder `q^-k/[2]_{q^k}`. **They are not.** At `p = 2` the formula predicts
0.551982 against the true 0.550893, and it fails at every non-classical `p`
tested (0.5, -2, -3). A coincidence of the three classical means. Pinned as a
probe assertion so nobody re-derives it as structure -- this is exactly the
near-pattern the anti-fit discipline exists for, and I would have shipped it had
I not tested off the classical points.

## Artifacts (added to the existing two)

`SymmetrySignAmGm.lean` grows to 14 decls, all axiom-clean: `weight_of_convention`,
`weight_miss`, `harmonic_mul_arithmetic`, `delta_harmonic_eq_neg_delta_arithmetic`,
`delta_harmonic_nonneg`, `arithmetic_pinned`, `harmonic_pinned`. Probe 9/9 -> 16/16.

**Still open, and now sharply stated:** derive the averaging rule, not `w`. A
rule with `p < 0` gives the SEMF sign; `p >= 0` cannot. `p < 0` is a TARGET to
check a derivation AGAINST, never a criterion to search ON, and nothing here
adopts the harmonic mean.


## 2026-09-05 (later) — the open half is ANSWERED: bar symmetry does not pin w

"Derive the averaging rule" resolves to: **it cannot be, from its own stated
justification.** Bar invariance of `f_pn = w.b_pp + (1-w).b_nn` reduces to
`wbar = 1 - w` — one equation — and the family `w_k = q^-k/[2]_{q^k}` satisfies
it for every `k`. The corpus's `1/2` is the `k = 0` member; what pins it is the
unstated assumption that `w` carries no `q`.

`delta(w_k)` vanishes at exactly `k = 1` (the geometric mean, `w_1 = 1/(q^2+1)`)
and is odd about it, so `k = 0`'s exact mirror is `k = 2`. The SEMF sign is the
region `k > 1`. Full detail and artifacts: `qou-79wa`.

**So this bean's "derive the averaging rule, not w" is discharged**, and the
residual is one scalar `k` with a derived admissible region rather than an
open-ended convention question.
