---
# qou-v2aa
title: 'Phase 1: Split PI into Ch9 (defs) + Ch11 (compute) manifests'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-arch
created_at: 2026-08-04T01:29:45Z
updated_at: 2026-10-10T07:16:26Z
parent: qou-8lxd
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## COMPLETED — inferred from the chapter layout, 2026-10-10 (method stated)

There is **no `particles-interactions` directory** under
`folio/quantum-observable-universe/`. What exists is
`knots-particles-confinement/` — manifest comment: *"particle definitions,
hadron algebra, knot-particle dictionary, confinement/shell hierarchy
(**definitional core** — upstream of eightfold-way + mass-theory)"* — alongside
`nuclear-interactions/`.

**Be clear what that is evidence of.** The definitional/compute split this bean
asks for is present in the layout and the old combined chapter is gone. I did
**not** trace the commit that did it, so this is inferred from structure, not
provenance. `git log` on those two directories is the check if anyone needs it;
I am recording the method rather than implying I ran it.
