---
# qou-sn3k
title: 'SW-4 residual: general seminormal rep — SUPERSEDED by qou-im9l (closed 2026-08-19)'
status: completed
type: task
priority: normal
created_at: 2026-08-11T10:15:21Z
updated_at: 2026-08-19T19:56:26Z
parent: qou-59vq
---

## SUPERSEDED / CLOSED 2026-08-19

This bean was created 2026-08-11 with an **empty body and no parent**, and left at
`in-progress` ever since. It therefore never appeared on the `qou-59vq` SchurWeyl arc
board while holding an open claim on the arc's headline item.

Its scope — the general-λ seminormal representation — is exactly **`qou-im9l`
(SW-4-gen)**, which is `completed`. Verified on main (`4c8cc533b5`):

- `hoefsmit_seminormal_rep` is declared and proved at
  `QOU/SchurWeyl/HoefsmitRepGeneral.lean:98` (it lives there rather than in
  `HoefsmitRep.lean` because its proof needs `SeminormalRep`, which imports that file).
- `QOU/SchurWeyl/HoefsmitRep.lean` is at **0 real sorries**.
- `qou-im9l` merged as `45817bf516`, its closeout as `a263bed527`.

Closed as superseded rather than scrapped: the work is done, not abandoned. Nothing here
needs re-deriving — see `qou-im9l` for the record, including the consolidation with
sibling PR #5282.

**Why this is worth a commit rather than a silent edit.** A stale `in-progress` bean is
not inert. Under the stalled-claim / sibling-coordination rules an agent reads
`in-progress` as "someone owns this", so this one could either steer a sibling away from
work that is actually finished, or invite a takeover of a claim with no branch behind it.
It also had no parent, so the arc board — the thing an agent reads to pick work — could
not show it.
