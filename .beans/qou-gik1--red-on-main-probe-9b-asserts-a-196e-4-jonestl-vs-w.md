---
# qou-gik1
title: 'RED on main: probe_9b asserts a 1.96e-4 Jones/TL-vs-Wenzl trace gap that convention D closed to EXACTLY zero'
status: todo
type: task
priority: normal
created_at: 2026-09-13T06:21:19Z
updated_at: 2026-09-13T06:21:19Z
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
