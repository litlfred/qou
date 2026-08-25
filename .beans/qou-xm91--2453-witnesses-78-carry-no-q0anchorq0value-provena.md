---
# qou-xm91
title: 2453 witnesses (78%) carry no q0Anchor/q0Value provenance pair
status: todo
type: task
created_at: 2026-08-15T10:35:54Z
updated_at: 2026-08-15T10:35:54Z
---


## Measured (PR #5082, `computations/q0_provenance_audit.py`)

**Do not quote a count from this bean.** Run it:

    python3 computations/q0_provenance_audit.py --json

The one number this bean is *about* — witnesses carrying NEITHER `q0Anchor`
nor `q0Value` — has been stable at **2453** across every revision of the
audit, because the canonical-pair test is an exact field-name check and has
not changed. Everything else moved repeatedly and the frozen table is deleted
rather than refreshed; refreshing would mint another generation.

## READ THIS BEFORE QUOTING EARLIER NUMBERS

Every count in this arc moved at least twice, and **never because the corpus
changed** — always because the audit was measuring the wrong thing. Three
separate instrument bugs, in order:

1. **Key names.** `stamp_staleness_metadata` writes **camelCase**
   `q0Anchor`/`q0Value`; the audit's key set held only snake_case, so matching
   on `k.lower()` never hit the canonical fields at all. Then a second pass
   missed `q_0_50dps`, `q0_proton`, `q_0_numeric` and ~16 more. Fixed by
   replacing the list with a pattern — and then the pattern over-matched
   `*_at_q0` keys (`tr_M_at_q0`, `jones_at_q0`), which name the *other*
   quantity, sweeping in ~90 non-anchors.
2. **False-precision by string prefix.** Flagged every ordinary 17-digit f64
   rendering, and could not clear them because an 18-character string cannot
   match a 20-character prefix. 79 files carrying the canonical value were
   reported "origin UNKNOWN".
3. **Round-vs-truncate.** The fix for (2) compared full overlaps, which a
   serializer that rounds its last digit (`...0878015` -> `...087802`) fails
   by construction. 145 files on the known stale constant moved INTO
   "unknown" — the bucket went *up*, which is how it was caught.

Now compared numerically in `Decimal`, at a tolerance set by the less precise
operand, with a regression test pinning all three failure modes to the real
corpus strings.

Lessons worth keeping: the audit was matching the field names I *expected*
producers to use, not the ones the writer actually emits — read the writer.
And a bucket moving in the *wrong direction* after a fix is the cheapest
signal available that the fix was wrong; watch for it.

## Why the gap exists, and why it is NOT simply "old files"

`WitnessBuilder.build()` DOES auto-stamp `q0Anchor` when absent
(witness.py ~L1150), and `stamp_staleness_metadata` resolves it from the
manifest + env. So the mechanism works — the 2453 are witnesses that either
predate it or are written by a path that bypasses the builder. Which of those,
per file, is unmeasured and is the first thing to establish.

## Why it matters more than the muon/proton split

The `qou-1c4y` migration is scoped as "move the ~840 muon witnesses". But for
78% of the corpus the anchor is not recorded at all, so "is this muon?" cannot
be answered from the file — only from its producer. A sweep scoped to the
labelled ones leaves the large majority in an unknown state, and the unknown
files are exactly the ones a later reader would most want the label on.

## Suggested approach — producer-side, not a witness rewrite

1. Split the 2453 by cause: predates the auto-stamp vs bypasses the builder.
   Only the second class is a live defect; the first heals on the next run.
2. For the bypass class, route those producers through the builder (or
   `stamp_staleness_metadata`) so the label is emitted going forward.
3. Do NOT bulk-write `q0Anchor` into existing witnesses. Stamping a file with
   an anchor nobody verified it used is manufacturing provenance — the same
   error as rewriting the 51 certificates, and the reason those were left
   alone. The label must come from a run.

## Related

* PR #5082 — the audit, and the derived-label fix that stopped a live
  flip-flop (the muon label was read from a stale witness whose producer now
  computes the PROTON value).
* `qou-1c4y` — the migration this re-scopes.
* AGENTS.md §"Migration posture" cited bean `tnjb` for that migration; `tnjb`
  is a completed dashboard bean. Corrected in #5082.

## CORRECTION — my framing above was wrong on the central point

A dispatched agent measured the split. The headline finding contradicts this
bean's premise, so read the correction before acting on anything above.

### The auto-stamp is NOT unconditional. The 78% is mostly BY DESIGN.

`build()` stamps `q0Anchor` only when the producer stem is declared in
`computations/q0_anchor_manifest.json` (or `QOU_Q0_ANCHOR` is set). The code
says so deliberately:

> *"Undeclared producers are still left unstamped: Q0_ANCHOR_MISSING is a
> tolerated state, and defaulting one in would assert a pin nobody
> established."*

That is the same principle I applied elsewhere in this arc (don't manufacture
provenance) — implemented, and I called it a gap. **It is a
manifest-coverage gap plus a deliberately-tolerated state, not a defect.**

### Measured split (2458 lacking q0Anchor)

    1467  (e) uses WitnessBuilder but producer NOT in the manifest  <- the engine
     674  (b) producer bypasses WitnessBuilder (hand-rolled json.dump)
     148  (d) orphan — no surviving producer
     120  (d) stale VENDORED copies under qou-mass/src/qou_mass/data/
      39  unknown (reverse-index matched >1 producer, disagreeing)
      10  (a) predates the stamp AND declared — heals on re-run
       0  (c) declared + builder + still missing

Verified by execution, not inference:

    canonical_isotope_witness    declared=True  -> q0Anchor=proton
    probe_inter_knot_decoupling  declared=False -> q0Anchor=None

Cross-tab: declared+builder 80.9% stamped; undeclared+builder **6.6%**.
Manifest membership, not builder usage, is the predictor.

### My "fix a producer, fix its witnesses" premise is FALSE

674 class-(b) witnesses come from **643 distinct producers** — 98% emit
exactly one witness. There is no leverage; this is a one-shot-probe corpus,
not a family bug. A per-producer sweep is ~643 edits for ~674 files.

### Other corrections

* **Cause (a) is 10 files, not the bulk.** The auto-stamp and the manifest
  landed in the SAME commit `a4d9906659` on **2026-08-10 — five days ago**.
  Nearly everything predates it, but predating alone does not heal: only a
  declared producer gets stamped on re-run.
* **120 files are stale vendored package data** under
  `qou-mass/src/qou_mass/data/`. Re-running the producer NEVER fixes them —
  it writes to `computations/`. Verified: one is frozen at 2026-05-19 while
  its `computations/` twin was regenerated 2026-07-11 and carries the anchor.
* **My count does not reproduce.** Agent measures 3142 tracked / 2458 missing
  (2476 under a strict-pair definition); I reported 3138 / 2453. ~5 files,
  no conclusion changes, but the exact definition needs pinning before either
  number is quoted as a baseline.

### Revised actionable item

The real work is **manifest coverage**: 1897 producers with witnesses use
WitnessBuilder, only **391 (21%)** are declared. Closing that is a data-file
change, far cheaper than 643 producer rewrites — BUT each entry requires
establishing that producer's actual pin, which is a judgement call per
producer, not a sweep. That is the honest shape of this task, and it is
bigger than "add a field".

Full per-file classification and producer lists are in the agent's scratchpad
output (`classB_producers.txt`, `classE_producers.txt`,
`q0anchor_missing_classified.json`).
