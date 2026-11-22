---
# qou-oomz
title: 'Triage PR #8134: Braid closure: what it cannot see (commutator span), two-step split, cheat-sheet'
status: completed
type: task
priority: normal
created_at: 2026-11-20T08:00:00Z
updated_at: 2026-11-22T11:16:09Z
parent: qou-c20n
---

Open PR #8134 (`claude/braid-closure-unseen-subword-2026-11-16`, opened 2026-11-16) had no bean: none named in its title or branch, none citing it.
Found by the W6 session review (`docs/coordination/2026-11-20-session-review.md`).

- Origin session(s): session_01Qmmkt8Mmpyd1gtuFjWCYm3
- Owner: W5
- Task: give the PR a verdict (merge candidate / needs rework / port core / close as superseded) and record it here.
- Nothing has been decided about its content.

Created by W6, https://claude.ai/code/session_01VQDpPgX3UVCddvq75ab4EV

## 2026-11-21 — verdict PORT-CORE, ported (thread "Port unowned leftover QOU PRs")
W5's triage (docs/coordination/2026-11-20-legacy-claude-pr-triage.md) gave #8134 PORT-CORE (low). All five commits
are cherry-picked (-x) cleanly onto `claude/port-unowned-leftovers-2026-11-21` on main 845e2f8200, together with
#7865, #7845 and #7834. Lean check (lean-direct -B on ClosureUnseen's cone, #print axioms) in progress.
#8134 is closed only after the owner taps close. Session https://claude.ai/code/session_01Qmmkt91GpCvJB15AZz7wMr.


2026-11-22: ported and merged. #8797 (cores of #8134, #7865, #7845, #7834) merged at 89410dc1b6; #8798 (G3.4 from #7874) merged at 9ab92b09c8. Both rebase-merged. The originals were closed as superseded on the owner's card choice (close after the ports merge). Before merging I checked the Lean cone against main 9eea870d0d: 214 modules, and the only change was two comment lines in QBeta/TemperleyLiebTower.
