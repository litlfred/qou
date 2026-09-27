---
# qou-8dzi
title: AGENTS.md's detector-blindness row count was stale for the SEVENTH time (46 -> 47)
status: completed
type: task
priority: normal
created_at: 2026-09-27T10:17:52Z
updated_at: 2026-09-27T10:18:28Z
---

## Measured 2026-09-27, fixed in `5a6afef6f3` (PR #7477)

**The claim.** AGENTS.md §"Precision goals" (the convention-C / detector-blindness
paragraph) said the taxonomy
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`
*"catalogues **forty-six** rows"*. It is **47**.

**The evidence.**

- `grep -cE '^\| *[0-9]+ *\|'` on the taxonomy → **47**; the id sequence is
  **1..47 with no gaps and no duplicates** (checked by extracting and sorting).
- The taxonomy **self-reports its own count** at line 994: *"The table is at 47
  rows as of 2026-09-26."*
- Row 47 landed on `main` as **`f75b27e70f`** (2026-09-26, a sibling's commit:
  *"docs(taxonomy): row 47 — `find <symlink>` traverses nothing, and this is the
  SECOND time it cost a wrong conclusion"*), and AGENTS.md's count was not moved
  with it.

**Why this was actionable without asking.** Exemption 2 of the 2026-09-07 override
— the corpus artifact fixes the answer and a reviewer checks the change by counting
the table, not by following my reasoning. The line being corrected *also* instructs
the reader to do exactly this: *"**Re-count the table; do not trust this sentence,
including this parenthesis.**"*

**Seventh staleness, and the parenthesis keeps its own tally.** Prior values
recorded there: thirteen (at 15 rows), sixteen (at 17), eighteen (at 21),
twenty-two (at 26), thirty-five (at 39), forty-five (at 46), now forty-six (at 47).
So the failure is structural rather than anyone's lapse: a row lands in the
taxonomy and the summary line in the file every agent actually reads does not move.

## What was changed, and what was deliberately NOT

Changed (3 edits, `AGENTS.md` only):

1. `forty-six` → `forty-seven`, with the re-count method and the landing sha.
2. `**Rows 35-46 are NOT in this list**` → `35-47`, so the
   not-in-the-group-split range covers the table again.
3. Row **47** promoted to the "newest" slot with its content; row 46 folded in
   below it.

**NOT changed: the group-split claim** (*"the groups below split the FIRST
THIRTY-FOUR seven ways"*). It was checked and left alone. This matters because the
same parenthesis records that an agent previously *"invented a group count while
correcting a row count"* — so the tempting second edit here is the known trap.
Only the total and the not-in-list range moved.

## Row 47 itself — worth reading before your next `find`

`find <path>` where `<path>` is a **symlink** traverses **nothing** without `-L`.
`folio-assistant/` in this repo is one (`-> ../folio-assistant`, created by
`scripts/setup-folio-assistant.sh`), so

    find folio-assistant -name X        -> 0 hits, silently, exit 0
    find -L folio-assistant -name X     -> the hit
    cd folio-assistant && find . -name X -> the hit

i.e. **a correct query over a present file reports absence.** The sibling
asymmetry is what makes it dangerous: `os.path.exists` and `grep -r` **do**
resolve the symlink, so a Python audit and a shell `find` over the same path give
opposite answers, and the `find` is the one that reads as corroboration.

Second instance. The first cost the **retracted** bean `qou-7br7`; the repeat read
the same silence as evidence that `gen-block-jsonld` / `gen-library-jsonld` — the
generators AGENTS.md's corpus-grep **path 0** names — had been dropped in the
platform restructure. Both were present the whole time.

**The reusable half is about WHERE a trap is recorded**, not about `find`: the
first record lived in one Python script's docstring under `scripts/`, invisible
unless you were editing that script, and never reached the table AGENTS.md points
every agent at. A trap recorded only beside the code that hit it will be hit again.

## Scope of the fix, and a standing recommendation (my judgement, not a finding)

This drains **one** instance; it does not fix the mechanism, and the tally above
predicts an eighth. The cheap structural fix would be for the taxonomy to be the
only place the count lives — AGENTS.md citing the artifact without restating a
number — but that is a wording change to a heavily-read passage and is the owner's
call, not an exemption. Left unproposed beyond this line.

Completed as mechanical (a count corrected against the artifact that decides it);
no conjecture is involved, so rule 13a does not apply.

Opened **after** the work landed, and recorded as such: this was unclaimed durable
work, which is exactly the omission AGENTS.md §3 asks agents to surface rather than
quietly absorb.
