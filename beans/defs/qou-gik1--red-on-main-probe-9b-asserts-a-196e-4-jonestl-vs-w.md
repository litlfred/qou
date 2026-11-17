---
# qou-gik1
title: 'RED on main: probe_9b asserts a 1.96e-4 Jones/TL-vs-Wenzl trace gap that convention D closed to EXACTLY zero'
status: in-progress
pr: 8189
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T06:21:19Z
updated_at: 2026-10-04T15:23:17Z
parent: qou-9nnz
---

## The measurement

`computations/probe-9b-perlambda-brane-tower.witness.json` carries `allPassed: false` **on `main` today** — this is pre-existing, not introduced by the raw-float64 drain that found it. One of its nine assertions fails:

```
trace_convention_gap_recorded
  computed  0.0
  expected  1.9554e-4
  tolerance 1e-6
  source    "|τ_pipeline − τ_Wenzl| ≈ 1.96e-4: the pipeline is the
             Jones/TL trace, NOT the corpus-canonical Wenzl z-trace"
```

The computed gap is **exactly 0.0**, not merely small. The assertion is not off by a rounding — the quantity it exists to record **no longer exists**.

## What that means

The probe's finding #1 (in its own docstring) is that the pipeline's closed-form τ is the SU(2)/Temperley–Lieb (Jones) Markov trace, while the corpus-canonical Wenzl z-trace gives a *different* scalar, `τ_W ≈ 0.998367` — a 1.96e-4 convention gap "recorded as data".

The two now coincide. The producer imports `closed_form_tau_M.markov_z`, which its own import comment labels "canonical convention-D z". Under the 2026-08-15 owner ruling convention D is canonical and C is excised, so the most likely reading — **inference, not measurement** — is that the migration collapsed the gap the assertion was written to record. I have not verified the mechanism; what is measured is that the gap is 0 and the assertion is red.

## Why this is not fixed here

Deciding what the assertion should now say is a judgement about the convention migration, not a precision fix, so it falls outside the two ASK-FIRST exemptions. Three shapes it could take, none adopted:

1. **Retire the assertion.** The convention gap was a C-vs-D artefact and D is canonical, so there is nothing left to assert. Cheapest; loses the record that the two traces once differed.
2. **Invert it** — assert the gap is now zero (`computed == 0`, tolerance `1e-40`), which turns a stale observation into a live check that the two conventions agree. Keeps a guard; commits to that agreement being a *property* rather than a coincidence of the current definitions.
3. **Leave it red** and banner the probe as superseded. Costs nothing, keeps `allPassed: false` on `main` indefinitely — which is what has been happening.

I would take **2**: the gap being exactly zero is a stronger and more useful statement than the 1.96e-4 it replaces, and a probe whose stated finding is "these two conventions differ" is worth keeping as "these two conventions agree" once they do. Marked as my judgement, not a finding.

Also worth noting for whoever takes it: the docstring's finding #1 states the 1.96e-4 gap in prose as well as in the assertion, so fixing only the assertion would leave the same stale claim in the file's own documentation — the pattern `qou-3x8x` records one probe over.

## Not in scope

Whether `τ_W ≈ 0.998367` is still the right Wenzl value, and whether the collapse to zero is correct rather than a symptom of both paths now calling the same function. Both need someone who knows what the two traces are supposed to be.


---

## The SAME stale premise sits in a SECOND probe — green, and vacuously so (2026-09-13)

Found while draining `probes/borromean_per_lambda_fr_probe.py` of raw float64.
It carries the identical 1.96e-4 claim, in two places:

- `add_data("wedderburn_lift_note", …)` — *"y-lambda-at-q0 × proved chi closed
  forms reproduce the Lean closed-form tau to 1.96e-4 relative only —
  **convention gap flagged**"*;
- the assertion name itself, `wedderburn_lift_consistent_to_2em4`.

**Measured: the mismatch is `9.983134063775882e-51`** — zero at the working
precision. And it is not circular: `tau` is the algebraic Lean closed form
`(4 + h² − 3h⁴ − h⁶)/(h² + 4)` from `params()`, while the lift is
`Σ_λ y_λ · χ^λ` read off `y-lambda-at-q0.witness.json` against the proved χ
forms. Two independent routes agreeing exactly.

**The committed witness has carried that value all along** — the prose
contradicted the number in the field beside it, so this is not something the
drain caused or revealed by re-running.

### Why this one is the sharper case

`probe_9b` is **RED** on this premise: its tolerance is sized around 1.96e-4,
so a value of zero fails it. This probe is **GREEN** — for the same reason,
inverted. Its tolerance is `5e-4`, which is **47 orders of magnitude** looser
than the 1e-51 it guards, so the assertion cannot fail for any regression short
of total breakage. Same stale premise; one probe reports it loudly and the
other passes silently and says nothing.

That makes the tolerance an instance of AGENTS.md's *"a bound sized to its own
miss is a fit"* pattern, surviving after the miss it was sized to went away.

### What was and was NOT changed here

- **Changed** (exemption 2, the corpus fixes the answer): the
  `wedderburn_lift_note` text, which stated a false number and flagged an open
  convention gap that convention D closed. It now states the measured 9.98e-51,
  says the two routes are independent, and records what it used to say.
- **NOT changed**: the assertion name `wedderburn_lift_consistent_to_2em4` and
  its `5e-4` tolerance. Renaming and tightening is the same decision this bean
  already puts to the owner for probe_9b, and settling it unilaterally on the
  second instance would pre-empt that. A comment at the site now says so.

**So the option set in this bean covers TWO probes, not one.** Whichever way it
is decided — rename to what is now true, keep the historical name with a note,
or revert to the C-frame — it should be applied to both, and the second one
needs its tolerance re-sized as well as its name, or it goes on passing
regardless of what it measures.

Blast radius checked: `wedderburn_lift_consistent_to_2em4` has **no consumer
outside its own producer** (grep over `.py`/`.md`/`.ts`/`.json`, excluding the
witness itself).


## Round 52 Progress
- [x] PR https://github.com/litlfred/qou/pull/8189 (`523155d5604cc384f307eb1cb22785f1fded85da`): updated `trace_convention_gap_recorded` in `probe_9b_perlambda_brane_tower.py` to `expected="0", tolerance="1e-40"` (`allPassed: true`, 0 raw float64) and tightened `wedderburn_lift_consistent_to_2em4` tolerance in `borromean_per_lambda_fr_probe.py` to `1e-40`.
