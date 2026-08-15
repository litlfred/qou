---
# qou-tp56
title: Repo-wide autoImplicit=false in qou Lake leanOptions (Mathlib-standard hygiene; prevents the zeta-notation auto-bound trap) — needs a FULL lake build to validate, CI or non-sandbox
status: todo
type: task
created_at: 2026-08-15T03:14:24Z
updated_at: 2026-08-15T03:14:24Z
---


## 2026-08-15 first attempt (dispatched agent, terminated at session limit)

Baseline `lake build QOU UGB Fred2005` in a worktree ran ~75 min to
[4687/4840] before the agent hit the session limit; the flip itself was
NEVER applied or committed (agent was classifying reds first), branch
never pushed. Findings that survive: only 2 red modules in the whole
baseline (QJucysMurphy ring_nf regressions + CompositionLemma), both
PRE-EXISTING — and main has since fixed q-JM (628b5c965). One tail
module cost 3120s of typeclass inference under CPU contention (two
concurrent builds). Relaunched fresh on current main 20:2x UTC.
