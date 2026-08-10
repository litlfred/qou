---
# fwr10
title: 'completeness pass over blocks that declare no prerequisites'
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T03:35:00Z
updated_at: 2026-08-10T03:35:00Z
parent: fwr6
---
Branch `claude/fwr10-completeness-pass-2026-08-10`. `fwr6` item 6.

The forward-reference arc was about edges that exist and point the wrong way.
This is the opposite defect: dependencies a reader needs that `uses[]` never
declares. It is the `uses-editorial-completeness` axis.

**Scoped by evidence, and it is much smaller than feared.** 510 blocks declare
no prerequisites, but only **110** name another block in their own prose, and
**41** name three or more. The other 400 name nobody — which is what a genuine
standalone looks like, and most of them will be exactly that.

| prose refs, none declared | blocks |
|---|---|
| 3 or more | 41 |
| 1-2 | 69 |
| none | 400 |

Among the 110, the kinds skew as you would expect if this is real: 37 prose, 27
remark, 22 proposition, 7 definition, 5 proof. A `-proof` block with an empty
`uses[]` is already an anomaly — proofs conventionally declare their parent.

**The prose-reference count prioritises a reading. It is never a source to
populate from.** Inferring `uses[]` from prose mentions is the failure the axis
exists to prevent, and a mention is a weaker claim than "the reader must go read
that first". `fwr5` rejected two of its eight candidates on exactly that
distinction — relatedness is not dependency.

Standard of evidence, from `fwr5` and `fwr7`: adding an edge asserts a reader
must go elsewhere first, so it carries a real burden, and one reading is not the
bar. `fwr7`'s two independent readers overturned eight of eight proposals that a
single earlier reader had reported.
