---
# qou-zkia
title: 887 sidecar entries claim a Lean sibling fails to compile; measured ~86% false
status: todo
type: task
priority: normal
created_at: 2026-08-23T10:39:37Z
updated_at: 2026-08-23T10:40:20Z
---

## Measured

`887` criteria entries across `258` blocks assert that a block's Lean sibling
fails to compile. Found while deleting three shadowing stubs (`qou-lo1t`,
PR #5533) whose sidecars made this claim — I checked out all three and built
them, and **all three compiled clean, exit 0**.

By criterion:

| criterion | entries |
|---|---|
| `da-reproducibility` | 254 |
| `da-lean-narrative-divergence` | 236 |
| `da-referee-verdict` | 188 |
| `da-overclaim` | 146 |
| `da-vacuous` | 52 |
| `wall-side-statement` | 11 |

**Random sample of 14 of those blocks, compiled with `lean`-direct against a
built import cone: 12 compile, 2 fail.** With my three that is 15 of 17, so
the claim is false roughly 86% of the time.

## Not stale — presenting as current

This is the part that matters. The sidecar staleness mechanism keys on
`source_hashes.lean`, and for **241 of the 258** the recorded hash still
matches the file on disk. Only 14 have drifted, and 3 have no sibling. So
these are not stale entries awaiting a routine re-sweep — they are
fresh-looking entries that a reader, a watcher, or an agent has no signal to
distrust. 188 of them have already hardened into `da-referee-verdict`
"open-objection".

## Cause: two environment artifacts, neither about the Lean

Of the 413 entries carrying error text:

- **83** record `object file '/Users/litlfred/space_cats/qou/.lake/packages/…'
  does not exist` — a **missing-olean** error, from the author's own laptop
  path. The checker ran without a built import cone, so every sibling that
  imports anything failed.
- **83** record `unexpected token 'section'; expected 'lemma'` — a **parse**
  error, not a compile error. It is what a statement-extractor produces when
  it expects a `lemma` and meets `noncomputable section`. The sidecars carry a
  `source_hashes.lean_statement` field, so such an extraction step exists.

The remaining 474 carry no error text at all.

## What would close it

Fix the checker to build the import cone (or skip rather than fail when it
cannot), and to distinguish extractor-parse failure from sibling-compile
failure. Then invalidate and re-sweep the affected criteria across the 258
blocks — `/integration-audit` is the mechanism. The checker lives on the
folio-assistant side, so this is not a qou-only change.

## Do not confuse with

Two of the fourteen genuinely fail (`qou-exists-axiom-2.lean`,
`neutrino-knot.lean`). The claim is wrong at scale, not always wrong; each
block still needs checking rather than a blanket clear.
