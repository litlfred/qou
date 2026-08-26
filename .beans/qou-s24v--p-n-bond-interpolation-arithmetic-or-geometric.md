---
# qou-s24v
title: 'p-n bond interpolation: arithmetic or geometric?'
status: todo
type: task
priority: normal
created_at: 2026-08-26T17:01:26Z
updated_at: 2026-08-26T17:02:06Z
---

Opened 2026-08-26 out of `qou-cblw` §3 (PR #5841), which closed "which bar-even
`E`?" as a negative and left this as the question that actually has a
structural route.

## The situation

The three inter-nucleon bond factors are

    f_pp = z                (positive crossing sigma)
    f_nn = z - h            (negative crossing sigma^-1)
    f_pn = z - (1/2 - eps)h  (a weighted combination)

and `f_pp`, `f_nn` are a single orbit of the q-bar: `bar(z) = z - h` exactly
under convention D (`QOU.Hecke.ClosedForm.markovZ_bar_eq_shift`, PR #5841).

So `f_pn` should be a bar-even "mean" of its two neighbours — and **there are
two derived candidates, both bar-even, both genuine convex bonds**:

    arithmetic   (f_pp + f_nn)/2 = z - h/2     eps = 0        (= strict_averaged)
    geometric    sqrt(f_pp*f_nn) = z/q^2       eps = -(q^2-1)/(2(q^2+1))

Measured at the proton pin they differ by 151x in magnitude and in sign
(`+3.44e-04` canonical vs `-5.20e-02` geometric), so this is not a
higher-order correction — it is a fork.

## The argument on each side

**Arithmetic.** The Markov trace is LINEAR in the bond element. A bond that is
a convex combination `(1/2+eps)sigma + (1/2-eps)sigma^-1` in the Hecke algebra
traces to the corresponding convex combination of `z` and `z-h`. If the p-n
bond is literally "half a positive crossing and half a negative crossing",
arithmetic is forced and `eps = 0`.

**Geometric.** The closed form is a PRODUCT over bonds
(`ClosedForm.closedFormProduct`). In a product, the natural interpolation
between two factors is the multiplicative midpoint: `f_pn^2 = f_pp * f_nn` says
that replacing a p-p and an n-n bond by two p-n bonds leaves the product
unchanged. That is a real structural property and the arithmetic mean does not
have it.

Note the geometric mean is `z/q^2`, i.e. exactly the bar-norm's square root —
`sqrt(z * bar z)` — which is the canonical bar-even representative of the
orbit. That is suggestive but is not an argument.

## Why this is not the colour-tube question

The canonical `bring_color_weighted` offset `delta/4` is `O((q-1)^3)`; both
means here differ at `O(1)` and `O(q-1)`. So this fork sits UNDER the
colour-tube correction, not beside it: whichever mean is right, `delta/4` is
then a correction on top of it. Settling this does not settle `qou-1oxx` and
`qou-1oxx` does not settle this.

## What would close it

A derivation of the p-n bond element itself — not its trace — from the
colour-tube geometry, so that the weights are read off rather than chosen.
Route: `conj:s5-so3-fiber-action` / the A=4 interface operator (Option E
PROBE 2). Deriving it from an isotope anchor is a FIT and does not close this.

## Do not

Do not "test both against AME and keep the better one". That is the seventh
fit-based ansatz in a different costume, and the 151x gap makes it especially
tempting because one of them will fit visibly better.

Prior: `computations/probes/pn_offset_bar_odd_class_probe.py` (16 assertions),
Lean `QOU.MassTheory.PnOffset` (12 declarations, sorry-free).
