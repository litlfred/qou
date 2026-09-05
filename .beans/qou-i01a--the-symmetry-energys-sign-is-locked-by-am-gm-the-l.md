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
