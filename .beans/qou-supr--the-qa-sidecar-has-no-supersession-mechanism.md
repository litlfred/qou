---
# qou-supr
title: 'The QA sidecar has no supersession mechanism: 28 criterion-slots carry two contradictory verdicts on identical source'
status: todo
type: task
priority: normal
tags:
    - qa-sidecar
    - block-qa
created_at: 2026-08-22T07:30:00Z
updated_at: 2026-08-22T07:50:00Z
---

Found while validating a batch whose sidecars carried exactly two `agent:pq_12`
entries per criterion. That case turned out to be **correct behaviour** — the
skill says record after fixes, the agent recorded before *and* after, and the
two entries differ in `field_hash.md` (`25ff9ee9e6af` → `e1887582eda4`), so the
later one certifies the fixed `.md`. Measuring the class corpus-wide is what
turned up the real defect.

## Measurement

Across every `trap-*` criterion in every block sidecar, counting slots where one
agent batch left more than one entry:

| shape | slots | reading |
|---|---:|---|
| same `md` hash, same verdict | **157** | pure redundancy — noise, not a defect |
| same `md` hash, **differing verdict** | **28** | **the problem** |
| differing `md` hash, same verdict | 28 | the prescribed fix-then-re-record |
| differing `md` hash, differing verdict | 2 | fix changed the verdict — correct |

Worst batches by duplicated slots: `e00` (88), `g01` (29), `pq_12` (22),
`f00` (21), `d01` (13), `i00` (11). 96 batches total; 24 have at least one.

## The 28 that matter

Same agent, same criterion, **the same unchanged `.md`**, two different
verdicts. Nothing in the schema says which is authoritative. A consumer reading
the array gets `fail` from the first element and `pass` from the last.

Worked example — `quantum-peter-weyl-proof.qa.json`, `trap-meta-commentary`,
`agent:r01`, both entries at `field_hash.md = 7ca3799ef5c7`:

```
entry 1  result=fail  severity=major   21:39:14Z
entry 2  result=pass  severity=none    21:52:06Z
         evidence: "Superseding the earlier agent:r01 fail on this block: …"
```

**The agent did the right thing and said so.** The supersession is stated
plainly — in `evidence`, a free-text field no consumer parses. That is the whole
defect: the record is correct and machine-unreadable.

Note the hashes are *equal* here even though a fix was applied between the two
entries, unlike the `pq_12` case where they differ. So `field_hash` cannot be
used to order these, and the union script's staleness filter
(`qa-sidecar-agent-union.py`, which keys on `field_hash.md`) keeps **both** —
correctly, since neither is stale, and unhelpfully, since one is superseded.

## Why nothing catches it

The sidecar is append-only by design, which is right: entries append, script
candidates stay as provenance (`local/language-trap-agent-audit` §per-block
procedure). Append-only plus no supersession field means "the later entry wins"
is a convention nobody wrote down and nothing enforces. There is no schema
validation for it, `qa-staleness.ts` keys on hashes rather than on
contradictions, and the coverage scans this campaign has run all ask *"is there
an agent entry?"* — which is satisfied by either.

## Candidate fixes, cheapest first

1. **A checker.** Flag any criterion slot with two entries from the same
   `reviewer.id` at the same `field_hash.md` and differing `result`. 28 hits
   corpus-wide, so it is drainable in one pass. This is the honest minimum:
   make the ambiguity visible rather than resolving it silently.
2. **A `supersedes` field** in `block-qa/v1` carrying the superseded entry's
   timestamp or index, so the intent an agent currently writes in prose becomes
   structured. Schema change, lives in `litlfred/folio-assistant`
   (`schemas/block-qa.ts`) — coordinate before proposing.
3. **Say it in the skill.** `local/language-trap-agent-audit` should tell agents
   to record **once, after fixes** rather than before and after, which removes
   the 157 redundant slots at source and most of the 28.

Item 1 first. Item 3 is nearly free and prevents recurrence; item 2 is the only
one that makes the existing 28 resolvable by machine rather than by reading.

**Not attempted here.** Picking a winner for each of the 28 means deciding which
verdict is right, which is a re-adjudication of the block — an agent's judgement
call on someone else's judgement call, and not one to make in bulk.

## 2026-08-22 — item 3 is done

[`local/language-trap-agent-audit`](../.claude/skills/local/language-trap-agent-audit.md)
§per-block procedure now says **record once per criterion, after all fixes to
that block**, with the reason (the array is append-only, so a second entry does
not supersede the first) and the measured cost. That stops the 157 redundant
slots and most of the 28 contradictory ones at source.

**Items 1 and 2 remain open**, and item 1 is still the one worth doing: the 28
existing contradictions are not fixed by a skill change, and nothing today makes
them visible. The checker is ~20 lines — flag any criterion slot with two
entries from the same `reviewer.id` at the same `field_hash.md` and differing
`result` — and drains in one pass.

