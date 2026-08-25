---
# qou-pwut
title: 287 root-level ad-hoc QA writers bypass qa-agent-entry.ts and emit no field_hash
status: todo
type: task
priority: normal
created_at: 2026-08-25T06:14:19Z
updated_at: 2026-08-25T06:29:55Z
---

## What

`content/pipeline/qa-agent-entry.ts` is the documented, canonical writer for
agent QA verdicts. It has **one caller in the whole repo** — a line in
`.claude/skills/local/language-trap-agent-audit.md`.

Meanwhile **287 tracked, root-level ad-hoc Python scripts** (`review_next_*.py`,
`review_batch*.py`, `run_qa.py`, `info_seq*.py`) write QA entries directly:

- **none of the 287 emits `field_hash`** — they write `reviewed_sha` only;
- **none of the 287 handles `evidence` at all** (`grep -l '"evidence"'` → 0).

They are the source of the 301 `unhashed` empty-evidence entries measured in
`qou-zsu6`.

## Why unhashed is worse than stale

An entry with no `field_hash` is neither live nor stale — it can never be
resolved to a block version, so no consumer can decide whether it still
applies. And `qa-agent-drain-queue.ts:74` gates on
`e.field_hash?.md === curmd`, so such an entry **never suppresses the drain
queue**: its block is re-reviewed indefinitely, appending yet another entry
each pass. That is a plausible mechanism for the duplicate-verdict problem
tracked separately in `qou-supr`.

## Consequence for the guard in PR #5745

The evidence guard lands on `qa-agent-entry.ts` and is correct, but it only
covers the minority path. If the `da-*` adjudication (94% of the live backlog)
runs through the ad-hoc scripts rather than the canonical writer, the guard
will not stop new empty verdicts. **Establishing which writer the `da-*` path
actually uses is the next step, and it gates whether the guard is sufficient.**

## OPEN

1. Determine the writer behind the live `da-*` verdicts.
2. Decide the 287: delete as scratch debris, or consolidate onto the canonical
   writer. They are tracked in git, so this needs a call, not a cleanup.

## Limit

Shallow clone (51 commits) — `git log` shows all 287 first appearing in the
graft commit `454abeb9`, which is an artifact of the boundary, NOT evidence
they landed together. `git fetch --deepen` times out against this remote. No
claim is made about when or how they landed.


---

**Correction (same session):** the `unhashed` 301 tracked here are, like the
rest, **misfiled rather than silent** — they record their reason under
`notes`. See the retraction on `qou-zsu6`. The two defects this bean names
are unaffected and stand on their own: the 287 scripts emit **no `field_hash`**
(so their entries are permanently unadjudicable and never suppress the drain
queue), and they bypass the canonical writer entirely.

Also corrected: this bean previously said the live `da-*` verdicts might come
from these scripts, making the PR #5745 guard insufficient. **They do not.**
Live entries require a `field_hash`, which these scripts never emit. The live
verdicts come from a *third* writer (`local/qa-agent-drain`) that emits
`field_hash`, `verdict`, `referee_argument` and `agent_model` — none of which
`qa-agent-entry.ts` writes either. So there are **three** writer families, not
two, and identifying the third one's source is the open task.
