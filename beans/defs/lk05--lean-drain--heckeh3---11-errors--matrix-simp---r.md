---
# lk05
title: 'Lean drain: HeckeH3 — 11 errors, matrix simp<;>ring v4.24 drift (one-pattern fix candidate)'
status: completed
type: task
priority: normal
tags:
    - coordinate
    - blocked
created_at: 2026-06-14T17:29:07Z
updated_at: 2026-06-14T18:15:00Z
parent: w5q7
---

User pick (drain thread, opt 1). stdRep3_hecke0/1, stdRep3_braid +~3 more use fin_cases<;>simp<;>ring failing under Mathlib v4.24 matrix-indexing drift. Verify via lake-cache restore + lean-direct.

TRIAGE (build-unverified read, 2026-06-14): root cause is Laurent-poly ring->ring1 + "ext i j : 1" capping, NOT matrix-simp drift; 6 theorems (stdRep3_hecke0/1, stdRep3_braid, stdRep3_M_cubed_eq_one, halfBorromean[_Conj]_trivial_eval). ALREADY FIXED on sibling branch claude/stoic-brahmagupta-izu39s (commit 0951e8686f). Do NOT duplicate — coordinate + build-verify instead.

SATISFIED BY open PR #2125 (head claude/stoic-brahmagupta-izu39s): "HeckeH3 Laurent-T closers + QGeometricLanglands universe pinning", locally lake-build-verified (exit 0, no sorryAx); CI billing-blocked. Action: LAND #2125 (coordinate), do NOT redo. Caveat: #2125 also carries QGeometricLanglands and is behind current main (needs rebase).

BLOCKER (2026-06-14): #2125 cannot be cleanly rebased onto current main — 3-day-stale branch; rebase hits add/add conflicts on tools/qou-substrate/* (pkg restructured on main) + ~dozens of .claude/skills/*.md conflicts (~50 files, 374KB output). Aborted cleanly. Main also touched HeckeH3.lean (commit 32b7684d). Options: (a) cherry-pick HeckeH3.lean fix to fresh branch off main [honors intent, drops QGL]; (b) leave whole #2125 for sibling/owner rebase; (c) full ~50-file conflict resolution. Awaiting owner decision.

DONE: HeckeH3 landed on main via cherry-pick PR #2309 (MERGED, sha 13f645cb); lean-direct verified LEAN_EXIT=0 on current main; Gemini doc-nit fixed+resolved. QGL remains on #2125 for the sibling.
