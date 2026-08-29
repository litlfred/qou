---
# qou-mdlv
title: '`.md` vs `.lean` formula divergence is a CLASS, not a singleton — two confirmed, and the grep that finds them is a lower bound'
status: in-progress
type: task
priority: high
created_at: 2026-08-29T00:45:00Z
updated_at: 2026-08-29T00:45:00Z
---

Follow-on to `qou-aemx`. PR #5931 found that `em-coupling-chern-simons`'s
`.lean` states a formula its own `.md` names as superseded. The obvious next
question — singleton or class? — is answered: **class**, and this is how to
find more.

## The detector

Blocks whose `.md` *announces* its own supersession are greppable:

```sh
grep -rlniE "previously displayed|previously stated|superseded (form|version)|\
earlier form of this|this (proposition|theorem|lemma|definition) previously" \
  content/ --include=*.md
```

Six hits on `main` at 2026-08-29. Triaged:

| block | Lean | verdict |
|---|---|---|
| `em-coupling-chern-simons` | sibling | **divergent** — PR #5931 |
| `centered-hecke-variance-positive` | library decl | **divergent** — PR #5936 |
| `y-lambda-recipe-from-partition` | sibling | migrated to D, migration documented in the file — the good exemplar |
| `birthday-axioms-do-not-pin-the-birthday` | library decl | different class (an assertion became a check, no formula moved) |
| `mba-step09a-mass-identity` | none | no Lean to diverge from |
| `st-is-median-resummation` | none | no Lean to diverge from |

**2 of 4 blocks that have Lean are divergent.**

## This is a LOWER BOUND, and that is the important part

The grep only finds blocks whose prose *says* it was superseded. A block
silently corrected — no "previously read" sentence — will not match, and
nothing in the pipeline compares an `.md`'s mathematical content against its
`.lean`'s. So the true count is unknown and is at least 2.

Note also that "no sibling `.lean`" does **not** mean "no Lean": per AGENTS.md
§0a the `lean.ref` resolves to a library file when no sibling exists. Both
`centered-hecke-variance-positive` and `birthday-axioms…` are that shape. A
sweep keyed on sibling files alone would have missed the second confirmed case.

## Why it survives

`centered-hecke-variance-positive` shows the mechanism cleanly:

1. The module is an **orphan** (`qou-orph`) — `lake build QOU` never compiled
   it, so nobody had reason to open it.
2. But a compile would **not** have caught it either. The stale file type-checked
   fine; it was *internally* consistent and only *externally* wrong.
3. There is no automated `.md` ↔ `.lean` content comparison. The
   `proof-statement-integrity` criterion is the right home for one and does not
   currently do this.

So the drift is invisible to every existing gate. It ran 19 days here and
across at least two merges in the `em-coupling` case.

## What would actually close it

Not another grep. A criterion that extracts the displayed formula from an
`.md` and the stated proposition from its resolved `.lean` and compares them —
or, much cheaper and probably sufficient: flag any block whose `.md` was
modified more recently than its resolved `.lean` **and** whose `.md` diff
touched a `$$…$$` display block. That is mechanical and needs no semantics.

Not attempted here. Recorded as the honest next step rather than done badly.

## Open

- [ ] Run the cheap heuristic above corpus-wide and see how many candidates it
      yields. If it is a handful, triage them; if it is hundreds, it needs
      narrowing before it is useful.
- [ ] Decide whether `proof-statement-integrity` should carry it as a
      mechanical criterion. Author call — it would flag existing blocks.
