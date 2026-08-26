---
# qou-awwk
title: chi_convention_from_values_audit does not cover the -at-qinv- family
status: todo
type: task
priority: normal
created_at: 2026-08-26T15:18:59Z
updated_at: 2026-08-26T15:19:34Z
---

Found 2026-08-26 while landing qou-1oxx (PR #5830), by auditing my OWN change
rather than the corpus.

## The gap

`chi_convention_audit.PRODUCER_CONVENTION` accepts BOTH conventions for a
producer that emits both, on the stated grounds that "the discrimination is
left to `chi_convention_from_values_audit`, which measures rather than
asserts". That is true for the Hoefsmit q0 producer. It is NOT true for
`chi_at_q_inv_via_native_mpfr.py`, which I widened the same way in #5830.

`chi_convention_from_values_audit.main()` hardcodes

    p = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"

so it never opens an `-at-qinv-` witness, weighted or blind. The deferral is
vacuous for that whole family.

I wrote the comment asserting the deferral. It was a coverage claim with
nothing behind it, and it is now corrected in-file to say exactly that.

## What stands in meanwhile

The qinv label is DERIVED from the word — counting crossings whose `d` matches
`-h_0*(1/2 - delta/4)` — not asserted, and not inferred from the filename as
the previous `convention_inferred_by` regex did. The producer records
`n_colour_weighted_crossings` so a reader can check it against the atom
(measured: exactly 1 for every A>=2 atom, 0 for A=1 and free words).

That is strictly better than what it replaced, but it is the producer
vouching for itself. It is not an independent measurement.

## The fix, and why it was not done inline

The values audit already has the right shape: it rebuilds the braid word and
runs the kernel TWICE, once blind and once colour-weighted, then compares the
stored chi against each. It also already handles `n_pn == 0` structurally
(INDISTINGUISHABLE) rather than by comparing near-equal floats.

Extending it to qinv is therefore a parameterisation, not a rewrite: take the
evaluation point as an argument and rebuild the shifts there. The one thing
that MUST NOT be done is to carry `d` across the bar — `h(1/q0) = -h(q0)`, so
the q0 coefficients are wrong at the bar point. `chi_at_q_inv_via_native_mpfr.
_avg_shifts_at` already does this correctly and can be reused.

Cost is the reason it is filed: two more H_12 kernel runs per atom, ~22 min
for helium-4 alone, on top of what the audit already pays for the q0 family.
Doing it inside #5830 would have meant a ~45 min compute I could not validate
without a further ~20 min, on a machine already running the helium-4 pair.

## Do not "fix" this by narrowing the acceptance instead

Reverting `PRODUCER_CONVENTION` to a single constant would flag every
colour-weighted qinv witness CRITICAL against a correctly-derived label. The
producer genuinely emits both frames; the table has to accept both. The gap is
the missing measurement, not the acceptance.
