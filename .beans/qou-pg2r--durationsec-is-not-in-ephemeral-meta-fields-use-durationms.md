---
# qou-pg2r
title: 'durationSec is NOT in _EPHEMERAL_META_FIELDS — serializing seconds makes wall-clock substantive witness content'
status: todo
type: task
priority: normal
created_at: 2026-08-15T21:11:00Z
updated_at: 2026-08-15T21:11:00Z
---

## The trap

`_EPHEMERAL_META_FIELDS`
(`tools/qou-substrate/python/qou_substrate/witness.py:1291`) contains
**`durationMs`** and **not** `durationSec`.

A producer that records its wall-clock as `durationSec` — especially
serialized as a *string* to dodge the raw-float64 ratchet — makes that field
**substantive witness content**. Every subsequent re-run then reports drift on
a meaningless timing number, so a genuinely-unchanged recomputation looks
stale.

The two spellings look interchangeable. Only one is masked.

## Evidence

Corpus agrees strongly with `durationMs`: **55 uses vs 2**.

Discovered when `main` and PR #5123 **independently** drained the same float64
duration leak in the #5107 probe — `main` as `durationMs`, the branch as
`durationSec`. Main's form is the correct one; the branch commit was dropped as
superseded on rebase. The branch's *own new* probe had copied the bad form and
was fixed in #5123.

Proof the fix works: consecutive no-op re-runs of the corrected probe now
differ **only** in `computedAt` / `commitSha` / `durationMs` — all masked.

## What to do

1. Grep `computations/` for `durationSec` and confirm the current count (do not
   trust the 2 above — it is a measurement from 2026-08-15, and per the
   repo's own "importer counts are measured, not maintained" note, a
   hand-carried number decays).
2. Convert each to `durationMs`, carried as an integer of milliseconds.
3. Re-run each producer and confirm consecutive no-op runs differ only in
   masked fields.
4. Consider whether `durationSec` should simply be **added** to
   `_EPHEMERAL_META_FIELDS` as a belt-and-braces measure — cheaper than
   policing every future producer, though converting to the canonical spelling
   is still preferable.

## Provenance

Surfaced by the `/prepare-merge-auto` pipeline for PR #5123 (bean
`qou-kc21im`), during a convergent-fix conflict resolution.
