---
# qou-s24v
title: 'p-n bond interpolation: arithmetic or geometric?'
status: completed
type: task
priority: normal
created_at: 2026-08-26T17:01:26Z
updated_at: 2026-08-26T17:24:18Z
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


## RESOLVED 2026-08-26, same day — and it retracts this bean's own argument

**The case for the geometric mean, as written above, is unsound.** I wrote it;
it does not survive contact with the bond elements.

The argument was: *"the closed form is a PRODUCT over bonds, so the natural
interpolation between two factors is the multiplicative midpoint."* That takes
a geometric mean at the level of **factors** while borrowing its motivation
from a multiplicative structure that exists only at the level of **elements** —
and the two levels are not connected here.

The two like-flavour bonds are `sigma` (p-p, `d = 0`) and `sigma - h*1 =
sigma^-1` (n-n, `d = -h`). They are **mutually inverse**. So:

    tau(sigma * sigma^-1) = tau(1) = 1          <- TRACE of the product
    f_pp * f_nn           = (q/(q^2+1))^2       <- product of TRACES

and `1/4 - f_pp*f_nn = ((q^2-1)/(2(q^2+1)))^2` is a **square**, so the product
of the factors is `<= 1/4` at EVERY `q` (equality only at `q = 1`), never `1`.
Measured at the proton pin: `0.2473` against `1`, a gap of `0.7527`.

So the Markov trace is not multiplicative on these bonds — it could not be, a
bond and its inverse would need reciprocal traces — and the closed form's
product over bonds is a product of *traces*, not the trace of a *product*.
There is no multiplicative structure at the factor level to take a midpoint in.
At the element level the multiplicative midpoint of `sigma` and `sigma^-1` IS
the identity, whose trace is 1, which is neither the geometric mean `z/q^2`
(0.497) nor any other member of the family.

**The arithmetic mean has no such gap**, because the trace is LINEAR:
`(f_pp + f_nn)/2 = tau((sigma + sigma^-1)/2)`, the skein symmetriser that
`QOU.BraidKnot.interface_knot_markov_z_bar_symmetric` is already stated about.
Its bond constant is the midpoint of the other two (`arithMean_bondConst_eq_midpoint`).

**Verdict: arithmetic, as the structurally-backed choice.** The arithmetic mean
of the factors is the trace of a canonical element; the geometric mean is the
trace of nothing canonical.

Lean §4 of `QOU.MassTheory.PnOffset` (4 further declarations, sorry-free):
`fPP_mul_fNN_eq`, `one_sub_fPP_mul_fNN`, `quarter_sub_fPP_mul_fNN`,
`arithMean_bondConst_eq_midpoint`. Probe now 20 assertions. PR #5841.

## SCOPE — what this does NOT establish

Scope (a), not (b). It removes the structural argument FOR the geometric mean;
it does **not** prove `eps = 0` is physically correct. The colour-tube
correction `delta/4` sits on top of the arithmetic mean either way, and
`qou-cblw` §3 stands: nothing in the corpus picks the bar-odd `E`.

What it DOES do is close the fork this bean was opened for, so the remaining
question is the offset ON the arithmetic mean rather than a choice between two
means. It also means the "do not test both against AME" warning above is now
mostly moot — there is one mean, not two.

**Corpus note.** This did NOT need the colour-tube geometry re-derivation the
bean says it needs. That estimate was wrong: the deciding fact is that the two
like-flavour bonds are mutually inverse, which is already in the corpus
(`bondD`, `interfaceFactor_eq_bond_expectation`). Formalize-first would have
found it before the bean was opened.
