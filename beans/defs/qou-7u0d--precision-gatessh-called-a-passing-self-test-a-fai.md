---
# qou-7u0d
title: precision-gates.sh called a PASSING self-test a failure — one flag-name mismatch, 19-of-20 measured
status: completed
type: task
priority: normal
created_at: 2026-09-07T05:41:08Z
updated_at: 2026-09-07T05:41:36Z
---

Found running the `precision-gates.sh` preflight on PR #6971.

## The defect

`scripts/precision-gates.sh:564` ran every gate's self-test as

    python3 "$script" --self-test >/dev/null 2>&1

and treated ANY non-zero exit as

    SELF-TEST FAILED — a detector that cannot be shown to fire is a no-op.

`scripts/word-provenance-gate.py` declared only `--selftest` (no hyphen). So
argparse rejected the flag, exited 2, and the runner reported the braid-word
gate as a no-op detector. **Its self-test in fact passes 9/9**:

    python3 scripts/word-provenance-gate.py --selftest
    word-provenance-gate: self-test passed (9/9)

The output was discarded to `/dev/null`, so the runner printed an accusation
and none of the evidence that contradicted it.

## Measured, because "probably a whole class" was the tempting reading

All 20 self-testing gate rows, both spellings, exit codes:

    --self-test=0, --selftest=0   :  8 gates (accept both)
    --self-test=0, --selftest=2   : 11 gates (runner's spelling only)
    --self-test=2, --selftest=0   :  1 gate  <- word-provenance-gate.py

**19 of 20 take `--self-test`; exactly one was the outlier.** So this is a
single-site fix, not a sweep — worth stating, because the shape invites a
runner-wide rewrite that would be larger than the defect.

## Exit code CANNOT discriminate, and that is the interesting part

The obvious runner fix is "argparse usage errors exit 2, real failures exit 1".
**Wrong here.** `word_provenance_gate.main()` returns **2** for a genuine
self-test failure as well:

    fails, n_cases = selftest()
    if fails:
        print(f"word-provenance-gate SELFTEST FAILED: {f}", file=sys.stderr)
        return 2

Same code, both causes. The reliable discriminator is argparse's own message.

## Fixed at both ends

1. **The gate** takes both spellings: `ap.add_argument("--selftest",
   "--self-test", ..., dest="selftest")`. `--selftest` stays live because
   `.github/workflows/word-provenance-gate.yml:65` calls it.
2. **The runner** captures the self-test output, retries the other spelling
   when stderr says `unrecognized arguments`, and PRINTS the first six lines
   of the failure when it does report one. A future gate with a third spelling
   is then reported as what it is.

Verified against two stubs rather than by reading: a gate accepting only
`--selftest` now passes; a gate whose self-test genuinely fails at exit 2 is
still reported failed with its message shown.

## Why it matters beyond the one gate

The message the runner prints is the strongest verdict it has — it says the
detector is a no-op. Attaching that to a sound gate is worse than silence: it
trains a reader to discount the message. Same family as `qou-1brv` (a self-test
whose verdict was a tautology and so could never fail), reached from the
opposite direction — that one could not report failure, this one reported a
failure that did not exist.
