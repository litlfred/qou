---
# qou-lw9l
title: 'Log-ratio channel is EXACTLY extensive: derived, with g-cancellation as the mechanism'
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:27:41Z
updated_at: 2026-09-02T22:01:04Z
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


## EXTENDED 2026-09-02 — the channel has NO many-body term at all

`computations/probes/logratio_exactly_pairwise_additive_probe.py`, 4/4.

Extended the exact-linearity test from the pure chains to **every mixed
composition** of A=3 and A=4:

    S_on/S_off = f_pp^(Z-1) * f_pn * f_nn^(N-1)     worst rel dev 1.78e-50

across all 9 compositions. Taking logs, `L = sum over chain bonds of
(-log f_bond)` — **exactly pairwise-additive, with identically ZERO many-body
terms.** No three-body at A=3, no four-body at A=4. Not small; zero to fifty
digits.

### The consequence for the shortfall

The channel is ~2.7x short (`B(4He) = 10.387` vs AME `28.296`). The natural
place to look for missing binding is a many-body term. **In this channel there
is none to find.** Whatever closes the gap must change the per-bond VALUES or
the BOND COUNT — it cannot be an irreducible 3- or 4-body piece of L. That
removes a candidate class; it does not supply the binding.

### Tension with t7qv, and the candidate reconciliation

`t7qv` measures three-body negative at all 8 A=3 orderings (`c1491ec174`) and
four-body negative in 80/80 random bond orders (`2bbb6115c5`), by **Mobius
inversion over nucleon SUBSETS**. Not in conflict with additivity over the
CHAIN bond set: for chain 1-2-3, the subset {1,3} has a sub-braid where 1 and 3
are adjacent and bonded, while the full chain has no such bond. Mobius
inversion attributes that manufactured bond to a "three-body term".

**FLAGGED AS A READING, NOT VERIFIED.** Their own commit names *"a labelling
artifact of embedding the bond graph in a line"*, so the mechanism was
identified there. What this adds is the measurement that over the chain bond
set the term is exactly zero. Confirming it against their probe is separate
work and was not done.

### An f_pn mismatch, chased rather than rounded away

    measured (blind arm) 0.50815788774864559388
    canonical            0.50822978937673896258     rel 1.41e-4

Not a defect: `atomic_tr_m_helium4_canonical.py:243` defines
`f_pn = z_d - h_q*(1/2 - delta/4)`, the colour-WEIGHTED value; this probe uses
the blind arm. Every mixed composition carries exactly one `averaged_weighted`
crossing (#6379) and that is the only place the arms differ — #6379 measured
the gap at ~1e-4. `f_pp` and `f_nn` are arm-independent: a pure chain carries
no `averaged_weighted` crossing at all.
