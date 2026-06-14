---
# lk05
title: 'Lean drain: HeckeH3 — 11 errors, matrix simp<;>ring v4.24 drift (one-pattern fix candidate)'
status: todo
type: task
priority: normal
tags:
    - coordinate
created_at: 2026-06-14T17:29:07Z
updated_at: 2026-06-14T17:50:56Z
parent: w5q7
---

User pick (drain thread, opt 1). stdRep3_hecke0/1, stdRep3_braid +~3 more use fin_cases<;>simp<;>ring failing under Mathlib v4.24 matrix-indexing drift. Verify via lake-cache restore + lean-direct.

TRIAGE (build-unverified read, 2026-06-14): root cause is Laurent-poly ring->ring1 + "ext i j : 1" capping, NOT matrix-simp drift; 6 theorems (stdRep3_hecke0/1, stdRep3_braid, stdRep3_M_cubed_eq_one, halfBorromean[_Conj]_trivial_eval). ALREADY FIXED on sibling branch claude/stoic-brahmagupta-izu39s (commit 0951e8686f). Do NOT duplicate — coordinate + build-verify instead.

SATISFIED BY open PR #2125 (head claude/stoic-brahmagupta-izu39s): "HeckeH3 Laurent-T closers + QGeometricLanglands universe pinning", locally lake-build-verified (exit 0, no sorryAx); CI billing-blocked. Action: LAND #2125 (coordinate), do NOT redo. Caveat: #2125 also carries QGeometricLanglands and is behind current main (needs rebase).
