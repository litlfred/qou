---
# qou-pwut
title: 287 root-level ad-hoc QA writers bypass qa-agent-entry.ts and emit no field_hash
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T06:14:19Z
updated_at: 2026-10-04T15:11:45Z
parent: qou-trd0
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

---

## BOTH OPEN ITEMS ARE NOW CLOSED — and the writers were already fixed (2026-08-29)

Came back to fix the `qa-agent-drain` / `-heuristic` writers on owner
instruction. Measured before changing anything: **there is nothing left to fix.**

**OPEN 2 — "Decide the 287: delete as scratch debris, or consolidate."**
**Already decided: deleted.** Commit `9ddf0ad9c0`, *"remove 316 unreferenced
root-level ad-hoc QA scratch scripts"*. `find` over the whole tree for
`review_next_*.py`, `review_batch*.py`, `run_qa.py`, `info_seq*.py` returns **0**.

**OPEN 1's writers — already correct.** Only **three** files in the tree write an
agent verdict into a sidecar, and every one of them hashes all three siblings:

| writer | reviewer id | `field_hash` |
|---|---|---|
| `scripts/reaudit_verdict.py` | `local/qa-agent-drain` | `field_hash()` over md/ts/lean ✓ |
| `scripts/reaudit-proof-deterministic.py` | `local/qa-agent-drain` | `current_field_hash()` ✓ |
| `scripts/reaudit-da-compile-claims.py` | `local/reaudit-da-compile-claims` | `field_hash()` ✓ |
| `content/pipeline/qa-agent-entry.ts` | (caller-supplied) | fixed in #5946 ✓ |

**No file in the tree stamps `local/qa-agent-drain-heuristic` at all** — its
10,245 entries come from a writer that no longer exists.

So the **53,293 unhashed entries are historical residue** from writers already
fixed or deleted. This bean's premise — that the 287 are the live source — was
true when written and is no longer.

### What was actually missing, and is now fixed

**Nothing PREVENTED the class returning.** The sibling guard test
(`qa-agent-entry.guard.test.ts`, PR #5745) pins `evidence` only, and `field_hash`
is absent from the schema's `required` list — so the next writer added could
reintroduce the whole thing in silence, exactly as it arose the first time.

Added `content/pipeline/qa-agent-entry.fieldhash.test.ts`: five tests, each
pinned to a defect that actually occurred, including that the hash **tracks
content** rather than mere existence (a frozen digest would satisfy every other
assertion and pin nothing).

**Mutation-tested** — a guard never seen to fail is not a guard. Reverting the
writer to each historical defect:

| mutation | result |
|---|---|
| drop `field_hash` entirely (the `qa-agent-drain` defect) | 0 pass / 5 fail |
| drop the `.lean` spread (the pre-#5946 defect) | 3 pass / 2 fail |
| emit `lean` unconditionally (present-but-empty) | 3 pass / 2 fail |
| writer restored | **5 pass / 0 fail** |

### Still open, and it is not this bean's

**The 53,293 existing unhashed entries.** They cannot be repaired by hashing them
now — the hash would record *today's* content, asserting that a July verdict
reviewed an August block, which is worse than leaving them unresolvable.
Invalidating them instead would force re-review of essentially every `da-*`
verdict in the corpus. That is a scope decision for the author, not a cleanup.

**One piece of debris survived the purge:** `run_agy.sh` writes unhashed
`milnor-editor` verdicts (the 41 in the measurement) and clobbers whole
sidecars. It is hardcoded to `/Users/litlfred/space_cats/qou/...` and cannot run
anywhere in this repo, so it is inert. Deleting it is `qou-gljq`'s call.

---

## ARCHAEOLOGY, on full history — and they were never producers (2026-08-29)

Owner asked: we cannot have live content without producers; why were the
originals deleted, what must be restored, or do we not need the witnesses?

**First, a correction to this bean's own recorded limit.** It says *"Shallow
clone (51 commits) … `git fetch --deepen` times out against this remote."* Both
halves are stale. `--deepen=2000` took **20 s** (19 grafts → 2) and
`--unshallow` took **4 min** (shallow file gone, 31,381 commits). The archaeology
below was impossible when this bean was written and is routine now.

**Two false attributions I nearly published**, recorded because the tell is
reusable. Blaming the largest sidecar-touching commit gave `230cdd1136`
(*"decorating the Gram cannot break the confinement-LP degeneracy"*, 3,592
sidecars **A**dded) and then, after one deepen, `635c73ad4d` (*"4_1 gluing"*,
3,297 added). **Both are shallow graft points** — at a graft the parent is
unresolvable, so every file reads as an addition. The tell both times was an
implausible `A` count (the second was 25,599 files, i.e. the whole tree).
**At a graft boundary, `--name-status` is meaningless.**

**The real origin, on full history.** `-S` on the entry's own timestamp rather
than on the criterion name (the criterion dates to 2026-05-28 and is not the
same question):

    e62336dabc1  2026-07-07  chore(qa-sweep): heuristic agentic redo for
                             proof criteria (full replace)

Self-describing and honest: a **heuristic agentic redo**, **full replace**.

**Why the writers were deleted:** `9ddf0ad9c0`, 2026-08-25 — *"Option 3 of the
three the author picked, **approved explicitly**."* Recorded reasoning: 0 of 316
referenced anywhere; **286 distinct hashes across 316 files**; hardcoded
`/Users/litlfred/...` paths; none emits `field_hash`.

### They were serializers, not producers — so there is nothing to restore

286 distinct hashes over 316 files is not one tool run 316 times; it is 316
bespoke throwaways. Each took a verdict **an agent had already reached** and
wrote it to JSON. A witness producer *derives* a value and re-running it
regenerates that value; these *transcribed a judgement*. Restoring them would
restore the ability to **write** verdicts, not to **reproduce these ones**.

**And a QA agent verdict is not a witness.** There is no producer even in
principle — the "producer" was a model session in July. This document already
says so under `prepare-merge-auto`: *"An agent verdict has no producer —
`qa-sweep` regenerates script candidates and never a judgement."* So the answer
to *"do we not need the witnesses?"* is: **there are none to need.** The
reproducibility frame does not apply to this artifact class.

### The concern is right but displaced — and largely already handled

The real defect is not the missing producer. It is that these entries carry **no
`field_hash`**, so nothing records *which version of the block* was judged.

**But that already fails safe, verified in code, not taken from a commit
message.** [`qa-agent-drain-queue.ts:72-75`](../content/pipeline/qa-agent-drain-queue.ts)
computes `fresh` as `e.field_hash?.md === curmd`. A missing hash is `undefined`,
never equal, so the criterion lands in `need` and the block is queued.

**Every affected block is therefore ALREADY queued for re-review.** The
unhashed entries suppress nothing.

### Measured scale

| | |
|---|---|
| blocks affected | **3,389** of 3,617 sidecars (94 %) |
| distinct criteria | 31 |
| cosmetic (`trap-`/`voice-`/`milnor-`/`expo-`) | 8,655 |
| **substantive** (`da-`/`proof-`/`q-usage-`) | **44,638** |
| location | **100 % live content, 0 in `_deprecated/`** |

### So the only live question

Not restoration, and not re-queueing — both are already settled. It is whether
the stale text should be **removed** from the sidecars, since a human or agent
reading a `.qa.json` sees `"result": "pass"` with a confident note and no
indication it adjudicates nothing. The drain queue knows; a reader does not.
That is the author's call and nothing here presumes it.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
