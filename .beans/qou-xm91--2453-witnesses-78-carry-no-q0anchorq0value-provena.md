---
# qou-xm91
title: 2453 witnesses (78%) carry no q0Anchor/q0Value provenance pair
status: todo
type: task
created_at: 2026-08-15T10:35:54Z
updated_at: 2026-08-15T10:35:54Z
---


## Measured (PR #5082, `computations/q0_provenance_audit.py`)

Over 3138 witnesses:

    CANONICAL provenance pair (q0Anchor / q0Value)
        666  both fields
         18  q0Anchor only
       2453  NEITHER  (78.2%)   <- this bean

    q0 VALUES recorded anywhere (a different question)
        470  proton
        799  muon
         13  truncated-5-digit (a 1.10998 literal, 1277 ppb off)
         51  other
       1831  none

    408  muon label that q_muon_at() does not reproduce
     18  multi-anchor candidates (some are q-sweeps — correct by design)

## READ THIS BEFORE QUOTING EARLIER NUMBERS

My own first pass under-reported every count. `stamp_staleness_metadata`
writes **camelCase** `q0Anchor` / `q0Value`, and the audit's key set held only
the snake_case spellings, so matching on `k.lower()` never hit the CANONICAL
fields at all. Superseded figures that appear in earlier commits/PR comments
in this arc: "1978 unrecorded (63%)" -> 2453 (78.2%); "709 muon" -> 799;
"243 non-reproducible" -> 408.

Lesson worth keeping: the audit was matching the field names I *expected*
producers to use, not the ones the writer actually emits. Read the writer.

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
