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

## Summary of Changes

FIXED. And MY OWN DIAGNOSIS IN THE ROAST WAS WRONG -- corrected below and in the roast doc.

THE CAUSE. `content/pipeline/lean-vacuity-ledger-foreign-entries.test.ts` ran

    bun run content/pipeline/lean-vacuity-axiom-audit.ts --quiet --review-ledger <2-entry fixture>

That is a WHOLE-CORPUS scan, so qou-c7jp's guard -- which refuses to write the committed record from
a PARTIAL scan -- does not fire; and with no `--json` the audit writes its default path, which IS the
committed record. Promotions are computed against the ledger it was given, so the fixture's two
entries produced `total_promoted_from_exempt: 0`.

Fix: pass `--json` to a temp path. c7jp's guard already documents this as the escape hatch ("To
write a partial report anyway, name an output"), and it is the right one here -- the test does not
care about the report at all, only about what happens to the ledger.

WHAT I GOT WRONG. The roast (R5) said the rewritten content "depends on how much of the Lean build
is present". IT DOES NOT. Nothing in this audit reads .lake. Measured three ways on the same tree:

    committed record   defects 133  exempt  59  promoted 66   (STALE -- main's qou-z9ws drain
                                                               commits moved the ledger past it)
    fresh corpus run   defects 114  exempt  57  promoted 53   (correct for the current tree)
    under `bun test`   defects  67  exempt 125  promoted  0   (FABRICATED from the test fixture)

So the file was not a stale snapshot, which is what I claimed. It was a fabricated one, written from
a test fixture, every time anyone ran `bun test`. That is worse than what I reported, and I reported
it wrongly because I diffed the numbers and reasoned about the build without checking what actually
invoked the script.

qou-c7jp DID NOT REGRESS -- the roast left that open and it is now closed. Its guard covers partial
scans only, and this was a full scan. Nothing to reopen there.

SEPARATELY VISIBLE, NOT FIXED HERE: the committed record is stale against the current ledger (133/59
/66 recorded, 114/57/53 measured). That is a content question for whoever owns the vacuity gate, not
a defect in this test.

The fix carries a byte-comparison assertion on the committed record, and I checked it is
load-bearing: reverting the `--json` flag makes the new assertion fail.
