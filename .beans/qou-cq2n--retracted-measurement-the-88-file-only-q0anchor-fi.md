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

## Replaced with a measured figure: 38 %, not 88 %

`computations/audits/q0_anchor_reproducibility_audit.py`.

```
manifest-declared producer stems : 651
witnesses carrying q0Anchor      : 1032

  488  reproduces: manifest + builder
  241  AT RISK: builder, but not manifest-declared
  155  AT RISK: hand-built witness, never stamped
  106  reproduces: producer writes it
   42  producer-not-found

  => 396 would NOT survive a re-run (38 %)
```

The grep said 88 %. It more than doubled the real number.

### The rule the audit encodes

From `witness.py:1590-1605`, which is authoritative and which I should have
read before sweeping: `WitnessBuilder.save` stamps `q0Anchor` **only when the
pin is positively declared** for that producer — an env var, or an entry in
`q0_anchor_manifest.json`. Undeclared producers are deliberately left unstamped,
because *"defaulting one in would assert a pin nobody established."*

So a stamp reproduces when **either** the producer writes the field itself,
**or** it is manifest-declared *and* reaches the builder. Everything else on
disk is a backfill artifact one re-run from vanishing.

### Two buckets, two different remediations

- **241 builder, not manifest-declared** — the code is fine; the *manifest* is
  short. Fix is a manifest entry, not an edit. Cheap.
- **155 hand-built** — never on the stamping path at all. These need the field
  written explicitly, as `su4` and `pentagon` now do.

### Stated limits, so the next reader does not over-trust this either

- `uses_builder` is textual **on the builder**, not on the field. A builder
  reached only through a helper module is missed, which makes a safe stamp
  read as at-risk. **396 is an upper bound**, not a point estimate.
- 42 witnesses have no locatable producer and are unclassified — not counted
  either way.
- The total moved 831 → 1032 between the two sweeps because the branch rebased
  onto main (+83 commits) in between. Same corpus question, larger corpus.

### The selftest is the part that matters

`--selftest` asserts that `su4_1111_markov_trace_probe` and
`pentagon_rt_torus_knot_higgs_probe` classify as reproducing — two answers
established by hand on this branch. Both pass. Without it this audit could be
narrowed into reporting a clean tree, which is precisely how the grep failed.
