---
# qou-9b5a
title: 'Move BondLengthSumTail.lean under QOU/Transcendental (new outside boundary from #9659)'
status: completed
type: task
priority: normal
created_at: 2026-11-27T21:22:02Z
updated_at: 2026-11-27T21:25:59Z
parent: qou-s028
---

#9659 (566e2ea564) added QOU/MassTheory/BondLengthSumTail.lean, which imports Mathlib.Analysis.SpecificLimits.Normed. transcendental-boundary-audit --check now fails on main: 462 outside, baseline 461, new 1. Post-merge follow-up per the fast-merge ruling: move the analytic half into QOU/Transcendental, or split it, keeping declaration names. Owner thread: C2 (qou-brng).

Fixed by #9720 (moved under QOU/Transcendental/MassTheory).
