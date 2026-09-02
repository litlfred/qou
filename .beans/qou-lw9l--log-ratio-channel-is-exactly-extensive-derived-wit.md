---
# qou-lw9l
title: 'Log-ratio channel is EXACTLY extensive: derived, with g-cancellation as the mechanism'
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:27:41Z
updated_at: 2026-09-02T21:28:21Z
---

## Measured 2026-09-02 — `computations/probes/logratio_exactly_extensive_probe.py` (4/4)

Completes the dichotomy opened by `chain_binding_closed_form_probe` (#6394).

### The result

With `b = A-1` bonds the measured structure is `S_off = g^(b+1)`,
`S_on = g^(b+1)·f^b`, so

    L(A) = log(S_off/S_on) = -b·log f

**exactly linear in bond count, no constant term.** Worst relative deviation
2.4e-30 (pp), 9.2e-31 (nn) at A=2..5 — exact at compute precision. Slope:

    -E0·log f = 2.0507096923814336856 MeV/bond  (pp)
    -E0·log f = 3.79778293514235333  MeV/bond   (nn)

The pp slope reproduces `bpp_a_dependence_bound_probe`'s independently-computed
`-alpha·ln z` to **4.3e-13**. Two routes, one number.

### Why it matters: it DERIVES an assertion the corpus carries

`log_ratio_binding_prototype.py` states *"the EXTENSIVE invariant is the
log-ratio"* in one sentence, without derivation. It now follows from the same
identity that excludes the difference channel.

**The mechanism is that `g` cancels.** The free-trace growth `g^(b+1)` sits in
both numerator and denominator of the ratio and drops out entirely — verified
by recomputing L with g scaled 1.7x and getting a bit-identical value at every
A on both species. The DIFFERENCE channel cannot cancel it, which is exactly
what its two exclusion branches are about. So the two channels are not two
guesses at one quantity: they differ by whether the single-nucleon growth
survives, and that alone decides extensivity.

### Lean (both sorry-free, 0 axiom beyond the standard three)

    QOU.MassTheory.MarginalRatio.logRatio_linear_in_bonds
    QOU.MassTheory.MarginalRatio.logRatio_independent_of_growth

### Scope — shape, NOT magnitude

This settles only which channel is extensive. The magnitude is separately
measured to be wrong by the `t7qv` arc: `B(4He) = 10.387277` vs AME `28.295661`
(-63.29 %), three-body term negative at all eight A=3 orderings, four-body
negative in 80/80 random bond orders — every many-body correction pushing
further from the data.

**Extensive-and-short is a different problem from not-extensive.** What this
closes is the shape question; the arc's remaining difficulty is entirely in the
magnitude category now.
