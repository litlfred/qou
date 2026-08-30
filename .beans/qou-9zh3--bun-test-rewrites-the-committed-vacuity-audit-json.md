---
# qou-9zh3
title: bun test rewrites the committed vacuity audit json, and its content depends on Lean build state
status: todo
type: bug
priority: normal
created_at: 2026-08-30T14:26:33Z
updated_at: 2026-08-30T14:26:33Z
---

Found while roasting the Roth arc (PR #6096, `qou-br3w`).

Running `bun test` from the folio rewrote `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json`:
204 lines changed, `total_defects` 133 -> 67, `total_promoted_from_exempt` 66 -> 0. Reverted by hand.

TWO PROBLEMS, and the second is the one that bites.

1. A test run mutates a COMMITTED artifact as a side effect. Anyone who runs `bun test` and then
   stages broadly ships the rewrite without noticing.

2. The rewritten content DEPENDS ON HOW MUCH OF THE LEAN BUILD IS PRESENT. The run above happened
   with 2259 of 2420 oleans built and produced a materially different report than a run against a
   complete build would. So the committed artifact is not a function of the source tree alone --
   which means a diff against it cannot be read as a change in the corpus, and the numbers in it
   cannot be quoted without saying which build state produced them.

RELATED, AND WORTH A LOOK: `qou-c7jp` is the same file being overwritten from the `--diff` path, and
it is marked COMPLETED. Either that fix did not cover the whole-corpus path, or it regressed. I did
not investigate which, and I did not touch that bean -- it is not mine to reopen.

Not fixed here: it is not the Roth branch's defect and the Roth branch is not where it belongs.
