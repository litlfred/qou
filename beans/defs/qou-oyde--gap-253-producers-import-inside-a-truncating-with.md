---
# qou-oyde
title: 'GAP: 253 producers import inside a truncating with-open(w); one has already destroyed its witness on main'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:25:11Z
updated_at: 2026-10-04T15:19:36Z
parent: qou-5vkl
---

FOUND 2026-09-08 by triage, then verified independently. Priority: the CLASS is latent; ONE member has already fired and is RED on main.

## The instance that fired (FIXED in this PR)

computations/qbeta/qbeta-chain-closed-form.witness.json is **0 BYTES on main** and is the ONLY unparseable witness of 3702 (verified: json.load over the whole tree, exactly 1 JSONDecodeError). Byte history on that path: 5930 -> 6016 -> 6018 -> **0**, truncated by 36501d7b01 (2026-09-07, 'sweep(qou-4383): re-run all 74 candidate producers'), whose own --numstat records it as pure deletion (0+ 176-) while the message asserts no regression. The loss was not noticed.

## Mechanism

open(path, 'w') TRUNCATES AT OPEN. The producer did the import and the provenance stamp INSIDE the with-block:

    with open(out_p, 'w') as f:          # <- truncates here
        from qou_substrate.witness import WitnessBuilder as _WB   # <- can raise
        _WB.stamp_staleness_metadata(...)                          # <- can raise
        json.dump(witness, f, ...)                                 # first byte only here

Anything raising between the truncation and the dump destroys the committed witness and writes nothing back. qou_substrate is NOT on PyPI, so a bare container is the DEFAULT and that import is the likely raiser.

Reproduced deterministically: with a shim making qou_substrate unimportable, the witness went 6018 -> 0. After the fix, the same forced failure leaves it at 6018.

## Why this is a defect, not a by-design refusal

- A 0-byte JSON is never a refusal; the documented refusing producers explain themselves on stdout and LEAVE THE PRIOR ARTIFACT INTACT.
- The exception is ModuleNotFoundError on a third-party import, not a corpus-defined domain guard (contrast AmDifferenceInvalid).
- The producer PASSES: exit 0, ALL PASSED, 0.83 s, and regenerates the destroyed content with a provenance-ONLY diff (4 leaves: commitSha, computedAt, gitCommit, scriptCommitSha). NO number moved -- so this is restoration, not re-derivation.
- The canonical writer already does it correctly: WitnessBuilder.save runs its checks BEFORE the open and puts only json.dump inside. This producer deviated from house style.

## The corpus PREDICTED this and chose the wrong remedy

Bean qou-m549 (status: **completed**, 2026-09-04) records it verbatim as a TRAP: the producer 'crashed ... and TRUNCATED its own witness (175 lines -> nothing) on the way out ... Restore the witness from git before re-running, or the crash looks like a drain.' That is an instruction to the AGENT instead of a fix to the PRODUCER. Three days later a sweep hit it and committed the zero to main. This bean is the fix that was declined.

## Why it reached main unseen (also fixed in this PR)

computations/audits/q0_anchor_consistency_audit.py tallied Q0_PARSE_ERROR into the counter table and did NOTHING else: no print block naming the file (unlike Q0_FLIP and Q0_ANCHOR_UNRECOGNISED), and the --strict gate was 'if args.strict and (n_flip or n_unrec)' -- parse errors could not fail it. An unparseable witness was a bare integer on a console with no filename and a green gate.

## THE CLASS -- DO NOT SWEEP IT

MEASURED independently (AST: an Import/ImportFrom anywhere inside a with-block whose context is a truncating open(...,'w')): **252 files in computations/ still carry the identical template**, after my fix removed the 253rd. This is corpus-wide and is emphatically NOT a one-PR job -- a 252-file mechanical sweep needs its own scoped decision and one owner.

Only ONE member has actually fired. That one is fixed. The other 252 are latent: each destroys its witness only if something raises between its open() and its dump.

## Next honest step for whoever takes the class

Do not blanket-rewrite 252 files. Cheapest real reduction, in order:
1. Rank by BLAST RADIUS: a producer whose witness is expensive to regenerate (long compute) loses more than one that re-runs in 0.8 s. The 0.8 s case is the one that fired, which is luck, not design.
2. Prefer the one-line form out_p.write_text(json.dumps(...) + '\n') -- it builds the payload before the file is touched at all, so there is no window, and it reads as a simplification rather than a refactor.
3. Consider a shared helper in qou_substrate so the fix is one import rather than 252 edits, then migrate incrementally.

## Coordination

The truncating commit belongs to qou-4383 (in-progress, idle >24 h at the time of writing). Its SUBJECT is grouped-era |tr_M| by fingerprint, not witness I/O, and it did not notice the loss -- so scope does not overlap. But its sweep RE-RUNS PRODUCERS, so a re-run before this fix lands would re-truncate. Flagged on that PR.
