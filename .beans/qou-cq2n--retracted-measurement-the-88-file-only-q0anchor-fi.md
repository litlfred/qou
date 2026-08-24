---
# qou-cq2n
title: 'RETRACTED measurement: the 88% file-only q0Anchor figure is an over-count'
status: todo
type: task
created_at: 2026-08-24T14:21:00Z
updated_at: 2026-08-24T14:21:00Z
---


## The claim, and why it does not stand

While fixing `su4_1111_markov_trace_probe`'s `q0Anchor` I found that its
producer never emitted the field — main's committed witness carries it from the
573-witness backfill `b8eb7d9e66d`, which wrote into **files**, not producers.
So a re-run drops it, and since that producer could not run at all, the latent
regression had never fired.

**That specific finding stands** and is fixed: the producer now emits
`q0Anchor` at top level, and the witness classifies `Q0_OK`.

I then generalised it and got **715 of 817 (88 %)**. **Retract that number.**

### The detector was measuring itself

It asked "does the producer's *source text* contain the string `q0Anchor`?"
But the canonical `WitnessBuilder` handles the anchor —
`tools/qou-substrate/python/qou_substrate/witness.py` has **31** occurrences.
A producer that goes through the builder therefore emits `q0Anchor` **without
the literal ever appearing in its own source**, and my sweep counted every one
of those as file-only.

So 715 is an over-count by an unmeasured amount. It is not "roughly right" and
it is not a floor — the builder is the *normal* path, so the false positives
are plausibly the majority of the 715.

### What would actually measure it

Not a grep. Either:

1. **Run the producer** into a temp dir and check whether the emitted witness
   carries `q0Anchor` — decisive, but expensive and blocked for producers that
   cannot run (which is the population most at risk, since a producer that
   cannot run is exactly one whose file-only fields have never been tested).
2. **Resolve the call graph**: does the producer reach `WitnessBuilder.save`,
   or does it hand-build a dict and `write_text` (as `su4` and
   `pentagon_rt_torus_knot_higgs_probe` both do)? The hand-builders are the
   at-risk set. That is an AST question, not a string question.

Route 2 is the cheap one and is what a real audit should do.

### Why this is worth a bean rather than a silent delete

This is the fourth detector-blindness instance in two days of my own work, and
the shape is identical every time: **the detector keys on how something is
SPELLED rather than on what it DOES.** AGENTS.md's detector-blindness taxonomy
already catalogues thirteen such spellings for convention-C. Add this one:
*a field written by a shared helper is invisible to a grep of the caller.*

The su4 fix is unaffected — it was found by the audit, not by this sweep.
