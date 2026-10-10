# S17 — classification of the agent docs (bean qou-4gzy)

**Classify only. No file was moved, edited or deleted** (owner decision 10,
2026-10-04). Table: [`S17_agent_docs_classification.tsv`](S17_agent_docs_classification.tsv),
produced by [`scripts/classify-agent-docs.py`](../../../scripts/classify-agent-docs.py).
The script is deterministic: two runs on one tree give byte-identical output.

**Scope, 212 files:** `docs/coordination/` (198), `docs/handoffs/`,
`docs/handover/` and `docs/handovers/` (9), `docs/agent-briefs/` (4), and
`.claude/validation-errors-handoff.md`.

**Classes** follow the owner's docs/ split ruling of 2026-10-04:

| class | destination | files | referenced from outside | mixed (≥ 40 `$`) |
|---|---|---:|---:|---:|
| `coordination-ledger` | beans/notes | 97 | 85 | 8 |
| `outstanding-work` | beans | 47 | 43 | 1 |
| `handoff` | beans/notes | 27 | 24 | 4 |
| `math-note` | HOLD until the notes graph kind exists (folio-assistant-8npa) | 18 | 16 | 0 |
| `live-registry` | STAY | 13 | 12 | 1 |
| `status-survey` | beans/surveys | 7 | 7 | 0 |
| `unclear` | owner review | 3 | 2 | 0 |

## What a later move must respect

1. **189 of 212 files are named by some tracked file outside the scope.**
   - The count excludes `beans/` and this story's own analysis outputs.
   - It requires a left boundary, so `1ppb.md` inside `x-1ppb.md` does not count.
   - The heaviest are the theme ledgers that AGENTS.md cites: `1ppq-qbeta.md` (153), `s5-so3-keystone.md` (129), `ck-dk-canonical-registry.md` (121), `option-e.md` (87).
   - A move must rewrite those references in the same commit, or every one becomes a dead link.
2. **`live-registry` is not a document class.**
   - It covers the validated JSON registries, their `*_validate.py` validators, and the catalogs.
   - Code reads them, and AGENTS.md cites `ck-dk-canonical-registry.md` as "the ONE source of truth".
   - They stay where they are unless they move together with their validators and readers.
3. **`mixed = yes` (14 files):**
   - These sit in a non-math class but carry substantial mathematics.
   - They move verbatim.
   - They must never be summarised into a bean body, because that would rewrite the mathematics.
4. **`math-note` is never a todo.**
   - A finished derivation counted as open work would inflate the backlog.
   - These wait for the working-notes graph kind, or for an owner-approved verbatim move into `folio/` blocks.

## Confidence

- `h`: the rule fired on the file name.
- `m`: it fired on the title.
- `l`: no name rule fired, so the file fell back to math density.

The rules are filename and title heuristics, not a reading of each file. Spot-check any row before acting on it.
