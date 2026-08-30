---
# qou-7qjf
title: 'A fail with no evidence: the schema requires a quote, nothing checks, 303 have none'
status: completed
type: task
priority: normal
created_at: 2026-08-24T22:49:19Z
updated_at: 2026-08-24T22:54:28Z
---

Found while sorting the `unquotable` third of `qou-4sdp`. It is not one class
but two, and the larger one is worse than "evidence I cannot search":

| | count |
|---|---|
| agent `fail`/`warn` verdicts | 1,442 |
| evidence **empty string** | **303** |
| evidence present but no searchable quote | 150 |

## The contract exists. Nothing checks it.

`schemas/block-qa-schema/schema/block-qa.schema.json`, on `result`:

> `pass` = satisfied; **`fail` = violated (evidence must cite file:line +
> verbatim quote)**; `warn` = borderline …

That is prose in a `description`. The entry object's `required` list is
`["field_hash", "result", "reviewer", "reviewed_at"]` — `evidence` is not in
it, and there is no `if`/`then` conditional for it, **though the same schema
uses exactly that mechanism a few lines down** to tie `ruling: surviving` to
`result: fail`. The only consumer that reads the schema at all is
`qa-flag-preservation-audit.ts`.

And `content/pipeline/qa-agent-entry.ts`, the writer, validated `--result`
against its enum and checked the block exists — then did
`if (evidence) entry.evidence = evidence;` and wrote the verdict either way.

So: a documented requirement, an unused enforcement mechanism sitting in the
same file, and 303 violations. The session's recurring shape — **an absent
check indistinguishable from a passing one.**

## Six criteria never supply evidence at all

| criterion | empty / total |
|---|---|
| `expo-milnor-clarity` | **210 / 210 (100 %)** |
| `da-referee-verdict` | 16 / 16 (100 %) |
| `da-lean-narrative-divergence` | 9 / 9 (100 %) |
| `fit-section-chapter` | 7 / 7 (100 %) |
| `da-overclaim` | 12 / 13 (92 %) |
| `da-physical-implausibility` | 8 / 10 (80 %) |

`expo-milnor-clarity` alone is **69 % of every evidence-free verdict in the
corpus**. 210 of 210 is not adjudicator sloppiness, it is a path that never
asks for evidence — and it is a `major`-severity STRICT gate ("pass iff a
perfect 16/16"), so 210 blocks carry a major failure whose reason is nowhere
on record. Fixing that one adjudication path is the highest-leverage single
change available here, and it is not attempted in this bean.

## Fixed: the writer refuses to create more

`qa-agent-entry.ts` now exits 2 on `--result fail|warn` without non-empty
`--evidence`, with a message saying what to supply and why. Seven tests
(`qa-agent-entry.guard.test.ts`) pin all four paths: fail and warn rejected
with no evidence and with whitespace-only evidence, no sidecar written on
rejection, fail WITH evidence accepted and recorded, and `pass` / `n/a`
still accepted with none — because a verdict that found nothing has nothing
to evidence, and spreading the guard there would hollow out the sweep from
the other side.

Bar is **non-empty, not quote-shaped**, deliberately: some legitimate evidence
is a bare `file.lean:1` pointer, and demanding a quote would push authors
toward inventing one. Whether evidence is *quotable* stays advisory, measured
by `scripts/qa-stale-agent-evidence.py` (`qou-4sdp`).

This mirrors the rule the platform already pins for SCRIPT checkers —
`checker-missing-evidence.test.ts`: *"a checker that cannot read its evidence
has not verified anything, and must not say pass."* The agent side had no
equivalent.

## Not fixed, and why

* **The 303 standing violations.** They need re-adjudication, one criterion at
  a time; `expo-milnor-clarity` is 210 of them and should be taken as a single
  path fix rather than 210 judgements.
* **The schema conditional.** Adding `if result is fail then required:
  [evidence]` is the right end state and is idiomatic here, but it would
  invalidate all 303 existing entries the moment it lands. It needs the
  backfill first, or an explicit grandfather date. Left undone rather than
  landed as a breaking change nothing is ready for.
