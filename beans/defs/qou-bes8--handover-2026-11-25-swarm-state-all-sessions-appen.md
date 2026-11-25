---
# qou-bes8
title: 'Handover 2026-11-25: swarm state (all sessions append here)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T16:25:07Z
updated_at: 2026-11-25T16:28:16Z
---

Owner, 2026-11-25, verbatim: "all handovefr notes should go into common .md (bean) all agents work on for their session (that should also be part of process)" and "your token use for the week is getting low, there are skills for handover, please make sure you and siblings start preparing".

ONE common handover ledger for the 2026-11-25 swarm. Every session appends ONE section with: session id + role; process/task; done (PRs/beans); in flight (branch, head sha, PR); next step; blockers; route to resume cold. Append with beans update <id> --body-append, then push with branch-store.ts push --id beans; on conflict re-read and retry.

## coordinator (session_01EucfRmMzrEARLFNgZfhwsQ)
- Site: #9396 (platform layer, Documents landing) merged ae92875; #9433 KG node regen merged 9686001; publish-main-local --deploy from 9686001 running in scratchpad qou-layer worktree (QA page pushed a9a583cd).
- Pins (owner consent): folio-assistant-sci 78f3321 (#222+#221), folio-assistant-core e2beef4 (#874+#875), cat-harness-tools 5593bb6. Re-pin to merge commits when #221/#222/#874/#875 merge.
- Open for owner: cat-harness#1405 merge (handoff envelope); Zenodo GitHub toggle (2a) then first release.
- Background agent: KG-node pre-merge gate PR (in flight).
- Children: photon session_01EucfRopy82qV7K5FpozNB9; holography session_01EucfRpmx5vQ5s5BZrP4uTV (#9428); q-NS session_01EucfRp1HyniH3qQb1YGVWb (qou-0nqs); BPMN process session_01EucfRqJQewHVJR2mVqcuaB (folio-assistant-sci); compute session_01EucfRmFaPKg5KbjjmxSBwx; merge manager session_01EucfRm2khmNLbMgiuTA6UZ (grant to 22:00Z).


### compute/derivation child — session_01EucfRmFaPKg5KbjjmxSBwx (stability epic qou-s028), 2026-11-25T16:3xZ
MERGED today: #9409 #9414 (LR fix + consumer), #9411 (interactive-sibling process), #9416/#9417/#9418 (probe-d attribution, withdrawal, ruling), #9421 (probe-d cone on the log law, scoped to the superseded letter), #9423 (Lean QOU.Nuclear.LogFormUniqueness: continuous extensive binding = -c log r).
OPEN: #9426 draft (gamma-gamma deuteron probes; Phase A 408/422 admissible bonds, B -0.16..7.67 MeV; card-1 selection V(2)^3 gives 0.0063 MeV = -99.7 %; head 963c58bc0b4 + Phase B child pushes). #9420 draft (a-K LP-dual face, analysis). #9424 (sibling; ruled tower E0, head f1c5d61dbbf5, merge main first).
BEANS: qou-xj4p (deuteron, open: binding unexplained), qou-fu8c (intervals delegated), qou-63be (new: Chmutov-Lando mutant check, not started), qou-of4i (sibling).
CHILDREN: session_01EucfRmaNiqxRg52fQZeNVB (Phase B + card 2), session_01EucfRq7fzfsm3Q1DZg9UTS (LP intervals, card 3), session_01EucfRqaU3YESdx7nHnDgpD (E0, done), session_01EucfRntKGFoPCof8huHo3z (deep binding-error budget).
OWNER CARDS 2026-11-25 recorded in owner-rulings.md on #9426: (1) bond scope decided after table, then 'go' = pure-junction cheapest; (2) p vs n: A+B+D; (3) LP duals as intervals; (4) ruled tower E0.
NEXT: qou-63be (cheap grep); collect child results; flip #9426 ready once Phase B is in.


### deuteron-overshoot child — session_01EucfRqaU3YESdx7nHnDgpD (bean qou-of4i, epic qou-s028), 2026-11-25T16:30Z
PR #9424 draft, branch claude/deuteron-overshoot-loci-2026-11-25, head f1c5d61dbbf5, pushed, tree clean, 68 behind main (merge main first; possible conflicts on the binding-log-free-energy and probe-d witnesses).
DONE: both loci measured. The +27.4 % is on the superseded letter; on the gg word the deuteron is unbound (qou-brng). Lean UniversalScaleMinimax (one-scale floor) and BondScaleUniversality (trace-only => one scale), lean-direct exit 0. Owner card 4 'ruled tower E0' applied: E0 4.227483, 2H +28.62 %. Precision gates NEW 0.
OPEN: owner decision on the 4 other order-zero log-law probes (framed on qou-of4i). qou-of4i stays open (Rule 13a).
