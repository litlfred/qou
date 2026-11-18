---
# qou-99fk
title: qa-sweep writes block-qa attestations into the TRACKED test/attestations store -- undeclared and unignored
status: in-progress
type: task
priority: high
created_at: 2026-10-10T07:37:59Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-5vkl
---

## The finding

`qa-sweep` at platform pin `717aa19a` writes **two** artifacts per block:

| path | state |
|---|---|
| `test/results/block-qa/<block>.qa.json` | **gitignored** (`.gitignore:284 test/results/*`) — the destination the owner ruling intends |
| `test/attestations/block-qa/<block>.attestations.json` | **NOT ignored**, and its parent `test/attestations/` is a **committed store** (426 tracked files) |

So running `qa-sweep` on any block leaves an **untracked file** in a tracked
store. Caught by the session stop-hook's untracked-files check after a routine
two-block sweep; it will fire for every agent who runs qa-sweep, every time.

## Why it is not obvious which way to fix it

**Three readings, and the corpus supports more than one:**

1. **It should be gitignored**, like its `test/results/` twin. `qou.json:67`
   states the QA store is "published to the qa-reports branch keyed by commit and
   **never committed** (owner ruling 2026-10-04, decision 11)". Taken literally
   that covers this file too.
2. **It should be declared and committed.** `test/attestations/` is otherwise a
   *committed* store — `bib-human-review` (reference attestations) and
   `bib-verification` are both tracked. On that reading `block-qa` is a third
   attestation kind that simply has no `qou.json` entry yet.
3. **The platform should not write there at all** — the duplicate write is the
   defect, and `test/results/block-qa/` alone is correct.

**Measured, to narrow it:** `git ls-files test/attestations/` yields exactly two
subtrees, `bib-human-review` and `bib-verification`. **Zero** `block-qa`
attestations are committed anywhere in history, and `qou.json` carries **no**
`attestations/block-qa` declaration. So reading 2 has no precedent behind it
today — but that is an absence, not a decision, and the absence is equally
consistent with "nobody has declared it yet".

## What was done, and what was deliberately NOT done

**Done:** the two generated files were **deleted, not committed** — derived
output, regenerable by re-running qa-sweep, and the ruling says QA results are
never committed. That is the conservative action under all three readings.

**Not done:** no `.gitignore` line was added. Adding one picks reading 1 over
readings 2 and 3 and silences the signal, and the destination of a derived store
is an owner/platform call rather than agent cleanup. A `.gitignore` entry would
also make the duplicate write permanently invisible, which is the wrong outcome
if reading 3 is right.

## Blast radius

Low in content terms, recurring in agent terms. Nothing in `folio/`,
`computations/` or the Lean tree is affected. The cost is one false
"untracked files" stop-hook hit per agent per qa-sweep run, and the standing
risk that someone resolves it by committing the files — which would start an
undeclared derived store inside a committed one.

## Recommendation (agent judgement, not a finding)

Reading **1**: gitignore `test/attestations/block-qa/`, matching the
`test/results/*` precedent and the "never committed" wording, and keep a
`.gitkeep` so an absent directory is never mistaken for a clean run — the same
pattern `test/results/` already uses. Reading 3 is cleaner if the platform
agrees the second write is redundant, but that is a `folio-assistant` change,
not a qou one.

## Default if nothing is done

Nothing breaks. Every agent running qa-sweep keeps getting a spurious untracked
-files prompt and has to re-derive this analysis to know the files are safe to
delete. Which is the cost this bean exists to remove.


## RECURRED, exactly as predicted (2026-10-10, same session)

Two more qa-sweep runs, two more untracked files:
`test/attestations/block-qa/.../brings-surface/{defect-legendrian-knot,topological-charge-quantization}.attestations.json`.
Deleted again. This is now observed twice in one session, which is the argument
for fixing it rather than re-deriving the analysis each time.

## SECOND SYMPTOM, same root: the in-tree `.qa.json` sidecars appear ORPHANED

Found while demoting two blocks for `qou-8b0q` (relabel `prop:`/`thm:` ->
`conj:`). After both qa-sweep runs:

- **`qa-sweep` did not modify either `.qa.json`.** `git status` after the runs
  lists the `.ts`, `.lean`, the regenerated index and the author-note edit —
  **no sidecar**. The only writes were to `test/results/block-qa/` and
  `test/attestations/block-qa/`.
- The sidecars still record the **old** labels (`prop:defect-legendrian-knot`,
  `thm:topological-charge-quantization`) and carry `source_hashes` for
  `md`/`ts`/`lean`/`lean_statement`. I changed the `.ts` and `.lean`, so those
  hashes are now stale **and nothing refreshed them**.
- AGENTS.md's documented remedy for a stale sidecar is to delete the stale
  `criteria.<crit>` entry and re-run qa-sweep. At this pin that no longer
  writes the sidecar, so the remedy does not apply.

**Scope of the claim, stated so it is not over-read.** What is measured is
(a) two qa-sweep invocations wrote no sidecar, and (b) `git log --since='14 days'
-- 'folio/**/*.qa.json'` returns only the `content/` -> `folio/` tree-move
commits (path fixes, `qou-yqko`), not QA runs. That is strong evidence the
in-tree sidecars are no longer a live output at platform `717aa19a`; it is **not**
proof that no code path writes them. The discriminator would be grepping the
platform for the sidecar write path, which I did not do.

**Deliberately NOT done:** I did not hand-edit the two sidecars' `label` fields
to match. They are derived artifacts; patching one field would leave
`source_hashes` stale anyway and would fake currency on a file nothing maintains.
The honest state is a visibly stale derived file plus this note.

**What this adds to the decision.** The original three readings were about where
`block-qa` attestations belong. This adds a fourth question with the same root:
if derived QA moved to `test/`, are the ~900 in-tree `.qa.json` sidecars now
legacy, and should they be retired rather than left to go stale on every edit?
That is a larger call than this bean, and an owner one.


## 2026-10-10 — the state this bean describes has CHANGED. Re-measured, no action taken.

Observed while running `qa-sweep` on twelve blocks for the owner's content
decisions. Recording because this bean's framing — *"undeclared and
unignored"* — is now only half right, and an agent arriving on the old wording
would file a defect that no longer exists.

**What is true now, measured on `main` + this branch:**

- `test/attestations/` is **tracked and populated**: `git ls-files` counts
  **434** files. So it is no longer *undeclared* in the sense of nobody having
  decided; main carries it deliberately.
- It is still **not gitignored**: `git check-ignore -v` on a block-qa path
  returns `rc=1`. So the "unignored" half of the title stands.
- **Twelve sweeps on nine blocks whose `.md` I had just edited left the tree
  byte-clean.** Not one attestation changed, which is the interesting part.

**Why it did not change, and it is not a bug in the sweep.** The entries are
**agent** verdicts, not mechanical ones, and they label their own staleness
blindness in the data: every note I inspected opens
`[EXPIRED-NO-FIELD-HASH]`. There is no `source_hashes` key anywhere in the
file. So the store is an archive of agent judgements that already announces it
cannot tell whether the source moved under it — which is the same thing
`qa-sweep` warns about on stdout for the `dak-*` criteria (*"a verdict that
cannot go stale is worse than a missing one"*).

**The mechanical verdicts I relied on did NOT come from this store.** The
`0 critical / 0 major / 0 minor` results in this session are computed live by
the sweep each run; the store holds only the `needs-agent` side. So nothing in
the content decisions rests on it, and that is worth stating plainly before
anyone re-reads those numbers.

**No action taken, deliberately.** Whether a tracked 434-file agent-verdict
archive that self-labels `EXPIRED-NO-FIELD-HASH` should be gitignored, moved to
the cat-harness `qa-reports` branch (which `.folio-assistant-pin` says is where
the derived QA corpus now lives, owner ruling 2026-10-04), or given a field
hash, is an owner call about someone else's arc. This bean stays `todo` at
`high` with its title's second half intact.

## 2026-10-10 — owner decision

Owner decision 6a (ofri, 2026-10-10): leave `test/attestations/` and the in-tree `.qa.json` sidecars as they are. The measurement suggested alongside 6a has not been run. It would grep the pinned platform for the sidecar write path, and it needs the folio-assistant clone, which is absent in this container. It remains the next step if the question is reopened.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-5vkl`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

In-progress in Round 98 PR litlfred/qou#8442.
