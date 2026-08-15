---
# qou-tp56
title: Repo-wide autoImplicit=false in qou Lake leanOptions (Mathlib-standard hygiene; prevents the zeta-notation auto-bound trap) — needs a FULL lake build to validate, CI or non-sandbox
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T03:14:24Z
updated_at: 2026-08-15T20:27:19Z
---

## Attempt 2 (2026-08-15, branch claude/tp56-autoimplicit-flip-2026-08-15)

State found at start: the flip itself is ALREADY ON MAIN — all three paper
lakefiles (`content/{quantum-observable-universe,unital-groebner-bases,fred2005-formal-groups}/lean/lakefile.toml`)
carry `[leanOptions] autoImplicit = false` since commit `3f5e9c0e1` (2026-08-01).
What remains is exactly the title's validation clause: a FULL
`lake build QOU UGB Fred2005` from the repo root against current main
(which includes the q-JM repairs `628b5c965`), plus fixes for any
auto-bound-implicit breakage the widened glob build surfaces.

This attempt: restore lake-cache/qou-v4-24-0 oleans, run the full named-target
build, triage reds (fix ≤ ~40 mechanically with explicit binders /
`universe u`; larger = commit inventory and stop honestly).
