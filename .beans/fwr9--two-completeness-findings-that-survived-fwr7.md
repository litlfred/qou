---
# fwr9
title: 'two completeness findings that survived fwr7'
status: completed
type: task
priority: normal
created_at: 2026-08-10T03:05:00Z
updated_at: 2026-08-10T03:15:00Z
parent: fwr5
---
Branch `claude/fwr9-completeness-followup-2026-08-10`.

`fwr7` proposed eight edge edits and two independent readers refuted all eight.
But the readings turned up two real defects of a different kind — both on the
`uses-editorial-completeness` axis, which is `fwr5`'s, not `detangler`'s.

**1. A missing entry.** `prop:frobenius-s-classification` names
`thm:wedderburn-mass-formula` in its first sentence and leans on it, and does not
declare it. Both readers found this independently while refuting the *retarget*
proposal — the retarget's second half was true even though its first half was
false. Adding an edge is a stronger claim than removing one, so it gets the
`uses-editorial-review` treatment: read the `.md` cold, list what the narrative
leans on, then compare.

**2. A transitive-redundancy warn.** `def:two-row-projection` reaches
`prop:wedderburn-weight-canonical` both directly and through
`def:two-row-stratum`. `uses-editorial-hygiene` calls this tidiness, explicitly
not a correctness problem: the graph is right, just not minimal. The question is
whether the direct edge earns its place — a reader who has read the stratum
block has already met the weight, so the direct edge may be restating rather than
declaring.

Neither is an ordering defect, so neither moves a block. Note that the missing
entry, if added, points **backward** (`thm:wedderburn-mass-formula` precedes the
source), so it costs no forward reference.

---

**Outcome: one edge added, one deliberately left alone.**

**1. Added.** `prop:frobenius-s-classification` now declares
`thm:wedderburn-mass-formula`. Confirmed by reading rather than taken from the
report: the block's opening sentence is *"the three log-functionals in the
Wedderburn mass formula ([Wedderburn mass formula](#thm:wedderburn-mass-formula))
carry..."* — the whole proposition is an S-classification of objects that theorem
introduces, so a reader who has not met it does not know what the three
log-functionals are. It declared only `prop:confined-knot-binding`.

The edge points **backward** — target at manifest position 38, source at 40 — so
it costs no forward reference. Adding it is free in the ordering metric and
strictly better for the reader.

**2. Left alone.** `def:two-row-projection` reaches
`prop:wedderburn-weight-canonical` twice over: directly, and through
`def:two-row-stratum`. Two reasons not to touch it, and they agree:

- The skill is explicit that `uses-editorial-hygiene`'s transitive-redundancy
  warn is *"tidiness only. The graph is correct, just not minimal. Do not let it
  distract from the completeness question."*
- The direct edge is not a duplicate of the transitive path — it has its own
  inline citation at `two-row-projection.md:14`, *"where $y_\lambda$ is the
  Wenzl weight from [`prop:wedderburn-weight-canonical`]"*. A block that names a
  target in its own prose earns a direct declaration whether or not a path
  already exists. Removing it would make the manifest disagree with the text.

Removing an edge is destructive and nothing here asked for it. A minimal graph
is not the goal; an accurate one is.
