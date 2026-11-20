---
# qou-s6pv
title: 'Hygiene: ~560 beans stay in-progress after the session that claimed them ended (measure, then ask owner)'
status: todo
type: task
priority: low
parent: qou-c20n
created_at: 2026-11-20T09:30:00Z
updated_at: 2026-11-20T09:30:00Z
---

Found by the 2026-11-20 session review (W6). On the beans mount (5793 beans): 1813 `in-progress`. Of the open beans whose
**latest** mention in a main commit belongs to one session, 560 are `in-progress` and 68 `todo` (628 total); every one of
those sessions has ended (latest commit ≤ 2026-11-19). An `in-progress` status there is a stale claim, not live work, which
hides real claims from the stalled-claim takeover rule and from sibling coordination.

Split by owner front: 222 under w2 trees (qou-10v9 / brng / cds1 / 99qc / exam), 19 under W8 (qou-6qbv), 8 under W10
(qou-c8p8), 7 w1, 3 w3, 352 under milestones with no live workstream (qou-5vkl 106, b9cj 92, qou-rtxm 58, qou-0uga 32,
qou-lpep 26, qou-qs0e 19, qou-vo9t 9). Per-bean list: `docs/coordination/2026-11-20-session-review.json` → `open_beans`.

Not done: flipping them to `todo` is a bulk status change, which the 2026-09-07 ask-first rule reserves to the owner.
Default if nobody acts: statuses stay as they are. The beans' content is not affected either way.
