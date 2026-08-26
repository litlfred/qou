---
# qou-awwk
title: chi_convention_from_values_audit does not cover the -at-qinv- family
status: completed
type: task
priority: normal
created_at: 2026-08-26T15:18:59Z
updated_at: 2026-08-26T16:00:56Z
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


## ✅ CLOSED 2026-08-26 — the values audit now covers the family

`chi_convention_from_values_audit` takes `--point {q0,qinv}` (default both) and
measures BOTH qinv variants. The acceptance in `chi_convention_audit` is now
backed by an independent measurement rather than by the producer counting its
own crossings.

### What moved

Three things were pinned to q0: the evaluation point, the shift (taken as `-d`
straight off the q0-built word), and the witness path.

The braid word is still built at q0 — that is where its `d` values are pinned,
and it is what identifies WHICH crossing is the p-n interface. Only the SHIFT
moves to the target point, rebuilt there:

    blind      h(q)/2
    weighted   h(q) * (1/2 - delta(q)/4)     delta = flavor_split_leading(q)

exactly as the bean prescribed, and for the reason it prescribed: carrying `d`
across the bar is wrong rather than conservative, since `h(1/q0) = -h(q0)` and
delta is bar-MIXED.

Both qinv variants are measured. Checking only the blind one would have left
the colour-weighted label exactly as unbacked as before.

### The measurement — 9 rows, all AGREES

    chi-deuteron-h6-at-q0-50dps                    3.13e-03  0.00e+00  AGREES
    chi-deuteron-h6-at-qinv-50dps                  0.00e+00  3.86e-03  AGREES
    chi-deuteron-h6-at-qinv-50dps-colour-weighted  3.86e-03  2.00e-50  AGREES
    chi-tritium-h9-at-q0-50dps                     1.52e-02  1.02e-49  AGREES
    chi-tritium-h9-at-qinv-50dps                   0.00e+00  1.87e-02  AGREES
    chi-tritium-h9-at-qinv-50dps-colour-weighted   1.87e-02  1.00e-50  AGREES
    chi-helium-3-h9-at-q0-50dps                    1.94e-02  0.00e+00  AGREES
    chi-helium-3-h9-at-qinv-50dps                  0.00e+00  2.39e-02  AGREES
    chi-helium-3-h9-at-qinv-50dps-colour-weighted  2.39e-02  5.25e-49  AGREES

**The separation is the point, not the verdict.** The matching convention lands
at ~1e-49 against ~1e-2 for the other — six to seven orders. An audit that
returned AGREES because it could not tell the two apart at the bar point would
have been worse than no audit at all, since it would have looked like coverage.
That had to be demonstrated, not assumed.

### Regression

At q0 the rebuild reproduces the previous behaviour EXACTLY. Checked against an
`origin/main` worktree: deuteron `3.13e-03 / 1.60e-49` and tritium
`1.52e-02 / 1.33e-48` on both sides. self-test 8/8. `chi_convention_audit`
unchanged at ok 36 / mismatch 2 (both pre-existing).

### Not done, deliberately

helium-4 stays out of the DEFAULT atom set, as it always has — H_12 is ~11 min
per kernel run, and the audit runs one per convention per witness. `--atom
helium-4` covers it when a helium-4 label is actually in question. This is the
pre-existing design, preserved, not a new carve-out.
