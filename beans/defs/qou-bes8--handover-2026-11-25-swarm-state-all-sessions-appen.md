---
# qou-bes8
title: 'Handover 2026-11-25: swarm state (all sessions append here)'
status: in-progress
type: task
created_at: 2026-11-25T16:25:07Z
updated_at: 2026-11-25T16:25:07Z
---

Owner, 2026-11-25, verbatim: "all handovefr notes should go into common .md (bean) all agents work on for their session (that should also be part of process)" and "your token use for the week is getting low, there are skills for handover, please make sure you and siblings start preparing".

ONE common handover ledger for the 2026-11-25 swarm. Every session appends ONE section with: session id + role; process/task; done (PRs/beans); in flight (branch, head sha, PR); next step; blockers; route to resume cold. Append with beans update <id> --body-append, then push with branch-store.ts push --id beans; on conflict re-read and retry.

## coordinator (session_01EucfRmMzrEARLFNgZfhwsQ)
- Site: #9396 (platform layer, Documents landing) merged ae92875; #9433 KG node regen merged 9686001; publish-main-local --deploy from 9686001 running in scratchpad qou-layer worktree (QA page pushed a9a583cd).
- Pins (owner consent): folio-assistant-sci 78f3321 (#222+#221), folio-assistant-core e2beef4 (#874+#875), cat-harness-tools 5593bb6. Re-pin to merge commits when #221/#222/#874/#875 merge.
- Open for owner: cat-harness#1405 merge (handoff envelope); Zenodo GitHub toggle (2a) then first release.
- Background agent: KG-node pre-merge gate PR (in flight).
- Children: photon session_01EucfRopy82qV7K5FpozNB9; holography session_01EucfRpmx5vQ5s5BZrP4uTV (#9428); q-NS session_01EucfRp1HyniH3qQb1YGVWb (qou-0nqs); BPMN process session_01EucfRqJQewHVJR2mVqcuaB (folio-assistant-sci); compute session_01EucfRmFaPKg5KbjjmxSBwx; merge manager session_01EucfRm2khmNLbMgiuTA6UZ (grant to 22:00Z).
