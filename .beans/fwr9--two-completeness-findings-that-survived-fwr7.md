---
# fwr9
title: 'two completeness findings that survived fwr7'
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T03:05:00Z
updated_at: 2026-08-10T03:05:00Z
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
