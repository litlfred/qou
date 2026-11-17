---
# qou-zv2l
title: 'GAP: canonical-ordering-dof witness is genuinely self-stale on scriptHash (producer re-run needed)'
status: in-progress
pr: 8333
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T12:56:59Z
updated_at: 2026-10-04T15:12:49Z
parent: qou-5vkl
---


Found incidentally while auditing `qou-wsha` (the `scriptCommitSha`
staleness re-key), not by a targeted sweep.

`computations/probes/canonical-ordering-dof.witness.json` is **genuinely
self-stale**: its recorded `scriptHash` does not match the current bytes of
its producer, so the producer was edited after the witness was generated.

    witness  computations/probes/canonical-ordering-dof.witness.json
    producer computations/probes/canonical_ordering_dof_probe.py
    scriptHash  recorded=87418d646ff1  current=894cafe018ee   -> STALE

This is the real thing, distinct from the `scriptCommitSha` false positives
in `qou-wsha` — `witness_dependency_drift.py --self-strict` would flag it,
and it is exactly the class of drift the idle-pass witness budget exists to
drain.

**Not fixed here.** Refreshing it means re-running the producer, which is a
compute action outside the scope of a docs-currency PR, and the witness
budget rule (≤ 3 per idle pass) wants it claimed deliberately rather than
ridden along. Next agent: re-run the producer per the compute-audit
long-compute logging discipline (`2>&1 | tee /tmp/<script>.log`) and commit
the refreshed witness with a `chore(witness)` message naming the producer.

Scope note: this is one witness, from the n=3 reliably-measurable sample of a
shallow clone — **not** a claim about the corpus-wide self-staleness backlog,
which was not measured.

## REFINEMENT (agent-4912 session, 2026-08-10, before merging #4931)

**The staleness is REAL but COMMENT-ONLY.**

```
git diff f471f7f46ff5 -- computations/probes/canonical_ordering_dof_probe.py
  -> 21 insertions, 0 deletions; EVERY added line is a '#' comment
```

The added block is the `STALE — CONVENTION C, pending pass 2 (bean qou-eea0)`
note explaining why `part6_crosscheck` is deliberately left red. The producer's
executable content is unchanged, so a re-run yields a **byte-identical payload**.

Consequences for whoever drains this:

1. **The refresh is a formality, not a recompute.** `durationMs=3` on the
   recorded witness — trivially cheap. Just re-run and commit.
2. **`allPassed: false` is BY DESIGN** — it is the red cross-check the comment
   block documents. Do NOT "fix" the red assertion while refreshing; silencing
   it is the exact failure that comment warns against.
3. **Generalised into the idle-backlog policy on #4931.** `scriptHash` is a
   whole-file hash, so comment/docstring-only edits drift it with no payload
   change. Both sites now say: diff the producer before re-running it. Cheap
   probes re-run; expensive producers with a comment-only diff get a bean
   rather than the idle pass.

Still open: #4931 stayed docs-only, so the witness itself is **not** refreshed.

## DRAINED 2026-08-10 — PR #4935

Producer re-run landed. **The comment-only prediction was confirmed
empirically**: every non-metadata key equal, `assertions` equal, `data` equal.
Only `scriptHash` (`87418d646ff1` → `894cafe018ee`) and `scriptCommitSha`
moved. `allPassed: false` (21/22) preserved deliberately — it is the red
cross-check the added comment block documents.

**Correction to the refinement above:** I read `durationMs: 3` as "3 ms probe".
That field is not wall time — the probe takes **46 s** (`durationMs` itself went
3 → 6). Cheap either way, so the "just re-run it" call was right, but the
number was wrong.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-10 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 56 Implementation (PR #8333)
- Implemented on branch `claude/round56-trd0-9nnz-fixes` (commit `e33bff7d43b72a19e618441a16ae41a21af05e0e`, https://github.com/litlfred/qou/pull/8333).
