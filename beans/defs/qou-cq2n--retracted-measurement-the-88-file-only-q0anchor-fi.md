---
# qou-cq2n
title: 'RETRACTED measurement: the 88% file-only q0Anchor figure is an over-count'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:21:00Z
updated_at: 2026-10-04T15:24:09Z
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

## Correction: "the 241 need a manifest entry — cheap" understates the work

I wrote that in three places — PR #5648's body and comments on #5623 and #5628 —
and the mechanism is right but the framing is not.

**The mechanism checks out.** Sampled that bucket: they do reach
`WitnessBuilder.save`, they are not manifest-listed, and a manifest entry would
therefore cause `save()` to stamp them. Nothing wrong there.

**What "cheap" gets wrong** is that a manifest entry does not merely *restore a
stamp* — it **asserts which pin the producer uses**. And the backfilled labels
disagree with each other:

| producer | its witness claims |
|---|---|
| `ame_2020_binding_energies` | muon |
| `casimir_beta_2_derivation` | proton |
| `i6_trace_convention_pin` | muon |
| `proton_brane_tower_correction_probe` | proton |

Copying each label into the manifest would assert a pin **on the authority of a
backfill** — precisely what `witness.py:1590-1605` refuses to do, in the same
breath that produces this whole at-risk bucket:

> Undeclared producers are still left unstamped: `Q0_ANCHOR_MISSING` is a
> tolerated state, and defaulting one in would assert a pin nobody established.

So the honest characterisation is **cheap mechanically, not cheap
epistemically**: each entry needs its pin *established* — read the producer,
determine which `q` it actually evaluates at — not copied from the field the
backfill left behind. That is a per-producer determination, and it is the
difference between a bulk edit and real work.

The irony is worth recording. The bucket exists *because* the builder refused to
assert an unestablished pin. "Just add manifest entries" would do the asserting
the builder declined to do, one layer up, and would look like progress: the
audit's at-risk count would fall while nothing had been established.

### Not a contradiction

A quick sample of this bucket found **6**, against the audit's **241**. Those
are not in tension — the sample used only the name-match fallback for locating
producers, while the audit resolves via `scriptFile` / `computation` first.
6 is a subset, not a competing count.

### Still open

The 241 remain at risk and the number is unchanged by the `qou-1c4y` manifest
migration (`ideal_muon` 120 → 37): re-measured after it landed, **398 of 1040,
still 38 %** — the migration reshuffled *which* producers are declared while
leaving the declared total at 651.

## Why "establish, don't copy" matters: the corroboration is circular

The obvious objection to the correction above is that the backfilled labels are
not arbitrary — `q0_anchor_consistency_audit` classifies these witnesses
**`Q0_OK`**, which by its own definition means *"anchor ∈ {muon,proton} and
`q0Value` matches that anchor's pin."* If the recorded value corroborates the
label, copying it into the manifest looks well-founded after all.

**It does not corroborate it.** Measured over every witness the backfill
`b8eb7d9e66d` touched:

```
witnesses touched by the backfill      : 574
  q0Anchor AND q0Value added together  : 573   <- circular
  q0Anchor added, q0Value pre-existing :   0
```

**Zero** had a pre-existing `q0Value`. The backfill wrote *both* fields, in the
same commit, in the same hunk. So the consistency audit is checking the
backfill against itself: `Q0_OK` here means the two fields agree because they
were written to agree, and carries **no independent information** about which
pin the producer actually uses.

That is the whole force of the correction. It is not merely that a manifest
entry asserts a pin — it is that the evidence which appears to support the
assertion is self-referential. An agent doing the reasonable thing (*"the audit
says OK, so the label is checked"*) gets a confirmation that was never a test.

### Not to be confused with the other circular anchor

`qou-yfsp` / `qou-i3yg` use "circular anchor" for something else — a producer
**inverting an observable to obtain q₀**, which is a fit-versus-derivation
question. This is a provenance question about two fields written by one pass.
Same adjective, unrelated defect; the audit file itself contains **zero**
mentions of co-writing or self-confirmation, so it is not documented there
either.

### Explicitly NOT claimed here

While measuring this I found **44** witnesses stamped `q0Anchor: muon` whose
producers are no longer in `ideal_muon`, so `q_parameter` (*"ideal_muon ⇒ muon;
anything else ⇒ proton"*) would give them **proton** on a re-run.

**That is `qou-1c4y`'s tracked work, not a finding of mine.** Its bean already
names the condition — *"witnesses stay muon-computed under a proton label"* —
and records that *"the 36 remaining are the correct end state"*, which matches
the 36 `ideal_muon` stems measured here. Reporting it as a defect would be
treating a sibling's in-flight migration as a discovery, which is the mistake
this session already made once with `qou-q7lf`.

Recorded only so the next reader knows the 44 were seen and deliberately left
to that arc.

## Remediation view: 93 producers, and a quarter of them cannot be fixed that way

`q0_anchor_reproducibility_audit.py --by-producer`.

**The "241" is 241 witnesses but only 93 producers**, and one of them —
`canonical_isotope_witness` — accounts for **120** of the witnesses. A
per-witness rate here is half one file. That is the distortion AGENTS.md
records costing a 39 %-vs-73 % swing on the staleness census; counting
producers is what avoids it.

| producers | witnesses | would a manifest entry reach it? |
|---:|---:|---|
| 48 | 196 | **EFFECTIVE** — reads `q_parameter` |
| 22 | 22 | UNKNOWN — no visible q0 source (indirect/helper) |
| 12 | 12 | **INERT** — hardcoded q0 literal |
| 11 | 11 | **INERT** — reads the anchor witness directly (`qou-aj91`) |

**23 of 93 producers (24 %) cannot be fixed by a manifest entry at all.** They
never consult the manifest: they read the anchor-defining witness directly, or
carry a literal. An entry for those declares a pin the producer does not obey —
which is worse than the missing stamp it replaces, because it *looks*
established.

So the shape of the work is now concrete: 48 producers where an entry is the
right instrument (and one of them drains 120 witnesses), 23 where it is the
wrong one, and 22 that need reading before either.

The 11 direct-anchor readers are `qou-aj91`'s class — that bean says the fix
belongs in `WitnessBuilder`, not in the producers, and this is a second reason
to agree.


## 2026-08-24 — RESOLVED for the reachable bucket: 48 producers declared, 396 -> 200 at-risk

**The instrument is a RUNTIME NO-OP, which is what makes it safe.** My own
objection on #5696 was that a manifest entry "declares a pin the producer does
not obey". Measured, that is backwards for this bucket: an undeclared producer
ALREADY resolves proton (`q_parameter.py:100-113`, `witness.py:324` — both
default not-in-`ideal_muon` to proton). Verified directly by adding one stem and
re-resolving:

    BEFORE  declared=False  resolve=proton
    AFTER   declared=True   resolve=proton

Only `q0_anchor_is_declared` flips. The entry does not re-pin anything; it
RECORDS the pin the producer was already using. That is precisely why this is
not the `qou-1c4y` bulk migration and does not need its sign-off — no witness is
regenerated, no producer changes anchor, `ideal_muon` is untouched (598 -> 646
in `physical_proton`, 48 insertions, additive only).

MEASURED EFFECT: at-risk 396 -> 200 (38% -> 19%); builder-but-undeclared
241 -> 45. The residual 45 are the INERT/UNKNOWN producers where an entry WOULD
be the lie I described — they never consult the manifest.

### The evidence does NOT rest on the on-disk stamps, and that matters

Provenance of the 196 labels in this bucket:

    174  ASSERTED: no reason recorded (backfill co-write)  <- circular, per this bean
     22  INDEPENDENT: transcribed from the producer's own recorded q0 value

So 89% of the labels are exactly the self-confirming kind this bean was opened
about. The determination does not use them: it uses the RUNTIME RESOLUTION RULE,
a code fact. The 22 independent readings are corroboration, and all 22 say
proton. Zero independent readings contradict it.

### Two producers read differently, and one is a real find

- **`qbeta_signchannel_cross_atom_probe` — a STALE WITNESS, not a mislabel.**
  Its `muon` label is one of the 22 INDEPENDENT ones: `q0AnchorReason` records it
  was transcribed from `parameters.q_50dps` in its own payload. Computed
  2026-06-22, before the proton directive. The producer calls plain `q_at()`, so
  a re-run today gives PROTON — the recorded numbers are muon-era and would
  move. The declaration is truthful about the producer; the witness still needs
  regenerating. THE STAMP CONFLICT IS A STALE-WITNESS DETECTOR, which is a use
  for this axis nobody has claimed yet.
- **`markov_peel_atomic_witness` — env-driven dual-layer**, writes
  `markov-peel-atomic-tr-m{,-muon}` by pin. Env wins over the manifest, so the
  entry fixes the proton stamp and leaves the muon run alone. Its muon stamp
  already reproduces via the env var, which the audit CANNOT SEE — so the audit
  over-reports on env-driven producers. Separately: its docstring asserts "it is
  tagged `physical_proton` in `q0_anchor_manifest.json`" and **it was not**
  (until this change). A source comment asserting a manifest fact that did not
  exist.

### One safety check worth keeping, and why it over-reported

`witness.py:1601` stamps by the BUILDER'S FILE (`self._script_path`) while
`q_parameter` selects by `sys.argv[0]`'s stem. For an imported helper those are
different files, so declaring a helper `physical_proton` could stamp proton on a
muon-resolved run. Checked all 48 against the importers of each: one flag,
`per_irrep_pole_atom` <- `block_swap_binding` (`ideal_muon`). READ, and it is
benign — `block_swap_binding` imports only `parts_of`, a pure helper, never
reaching that module's builder. Import-based detection over-reports because
importing a FUNCTION is not reaching the module's WitnessBuilder. Over-reporting
is the safe direction and it surfaced the one pair worth reading.

Also checked: 4 of the 48 mention the muon layer; 2 (`flavor_split_alpha_*`)
genuinely call `q_muon_at()`. AGENTS.md already adjudicates that shape — a
producer reading `q_at()`/`q_muon_at()` by name "belongs under
`physical_proton`" — so the entry is right for them too.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [B] title begins RETRACTED - the bean records its own retraction; nothing left to do (keep as record, status completed)
