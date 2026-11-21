---
# qou-oomz
title: 'Triage PR #8134: Braid closure: what it cannot see (commutator span), two-step split, cheat-sheet'
status: in-progress
type: task
priority: normal
created_at: 2026-11-20T08:00:00Z
updated_at: 2026-11-21T08:00:00Z
parent: qou-c20n
pr: 8134
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
