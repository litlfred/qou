---
# qou-pwut
title: 287 root-level ad-hoc QA writers bypass qa-agent-entry.ts and emit no field_hash
status: todo
type: task
priority: normal
created_at: 2026-08-25T06:14:19Z
updated_at: 2026-08-29T01:35:00Z
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

---

## ANSWER to OPEN 1 — the `da-*` writer, measured 2026-08-29 (bean `qou-aemx` tranche)

OPEN 1 asked: *"Determine the writer behind the live `da-*` verdicts"*, and noted
it *"gates whether the guard is sufficient"*. Measured across all **3,617**
`content/**/*.qa.json` sidecars, **279,830** criterion entries:

| reviewer.kind | carries `field_hash` | count |
|---|---|---|
| `script` | yes | **179,959** — all of them |
| `agent` | yes | 46,450 |
| `agent` | **no** | **53,293** |

So the schema supports it and 46,450 agent verdicts do record it — **this is a
producer defect, not a schema or conceptual limit.** Three reviewer ids account
for 99.2 % of the gap:

| `reviewer.id` | with `field_hash` | without |
|---|---|---|
| `local/qa-agent-drain` | 2,242 | **39,655** |
| `local/qa-agent-drain-heuristic` | 10 | **10,245** |
| `local/branch-jargon-sweep` | 0 | **2,967** |
| `one-voice-audit` | 6,719 | **0** ✓ |
| `agent:pq_*` (per-block agents) | all | **0** ✓ |

**The answer to OPEN 1: the `da-*` path is `local/qa-agent-drain` and
`local/qa-agent-drain-heuristic`** — *not* the 287 root-level ad-hoc scripts this
bean tracks, and *not* `qa-agent-entry.ts`. All 13 `da-*` criteria sit at ~2,577
unhashed entries each, i.e. essentially every block's devils-advocate verdicts.

**Consequence, which is the thing OPEN 1 was gating: the PR #5745 evidence guard
is NOT sufficient.** It lands on `qa-agent-entry.ts`, and the `da-*` adjudication
does not go through it. Fixing the `da-*` path means fixing the two drain writers
(or routing them through the canonical entry point), which is a different change
from deciding the 287.

**Scope note — do not merge these two numbers.** This bean's `301 unhashed` is the
*empty-evidence* population from `qou-zsu6`. The 53,293 here is every agent entry
lacking `field_hash`, a superset measured on a different axis. They are not the
same count and neither supersedes the other.

### Worked instance of the consequence

Found by walking into it rather than by looking for it. On
`predicted-spectra/em-coupling-chern-simons`, the criterion
**`da-lean-narrative-divergence`** — defined in the registry as *"Lean proves
something weaker/different/vacuously-implied vs the .md claim
(proof-statement-integrity)"*, i.e. exactly the defect that block turned out to
have — carries two `pass` verdicts from `local/qa-agent-drain`, dated 2026-07-07
(*"Looks good. Heuristically verified."*) and 2026-07-13 (*"Reviewed
interactively. Content is sound."*). Neither carries a `field_hash`.

Those verdicts survived the block's `.md` correction in August **and** a `.lean`
edit made in this tranche: re-running `qa-sweep` updated the sidecar's top-level
`source_hashes.lean` and re-ran every `script` criterion, and left
`da-lean-narrative-divergence` **untouched** — verified, the criterion does not
appear in the sidecar diff at all.

So the gate for this defect class exists and is correctly scoped; what fails is
its **staleness model**. An agent verdict pinned to a commit sha rather than to
the content it reviewed stays green through arbitrary later edits to that
content.

### Adjacent defect found while measuring the above — and it is NOT the same one

Reading `qa-agent-entry.ts` to confirm the canonical path, its `field_hash` was
built from `.md` and `.ts` only — **no `.lean`** — and `qa-agent-drain-queue.ts:74`
gates on `e.field_hash?.md === curmd`, i.e. `.md` alone. The obvious reading is
that even correctly-written verdicts about the Lean can never go stale on a
`.lean` edit, which would make this a corpus-scale problem.

**Measured, it is not.** On Lean-reading criteria, agent verdicts carrying a
`field_hash` on blocks that have a `.lean`:

| | count |
|---|---|
| already record the `lean` key | **114** |
| do not | **4** (all `proof-statement-integrity`) |

A **latent** bug with 4 live instances. Fixed anyway (one conditional spread plus
a `leanPath` declaration, verified behaviourally in both branches), but it must
not be cited as an explanation for anything.

**Two false trails, recorded so they are not re-walked:**

1. *"40,646 agent entries carry a `field_hash` with no `lean` key."* True and
   misleading — **31,935** of those blocks have **no `.lean` sibling**, so the
   key is legitimately absent. Real population 9,056, and nearly all of that is
   `trap-*` criteria that read only `.md` prose and do not need it. Hence 4.
2. *"This explains the em-coupling incident."* It does not. Those
   `da-lean-narrative-divergence` verdicts carry **no `field_hash` at all** —
   they are `local/qa-agent-drain` output, i.e. **this bean's** defect. Two
   adjacent defects with one mechanism each; conflating them would have
   mis-attributed both and left the real one unfixed.

The `qa-agent-drain` / `-heuristic` writers remain unfixed and remain the live
issue for the `da-*` path.
