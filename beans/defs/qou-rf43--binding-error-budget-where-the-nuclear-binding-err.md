---
# qou-rf43
title: 'Binding error budget: where the nuclear binding errors come from (2H-4He, 6Li/7Li vs AME2020)'
status: in-progress
type: task
priority: normal
tags:
    - compute-accuracy
created_at: 2026-11-25T16:29:06Z
updated_at: 2026-11-27T14:18:44Z
parent: qou-s028
---

2026-11-25 RESUME STATE: audit docs/audits/2026-11-25-binding-error-budget.md written from corpus + seconds re-measures (owner token-budget handover: no new probes). PR #9436 (draft), branch claude/binding-error-budget-2026-11-25, head 281e13fb9. Ranked: bond word (~350x on 2H), missing positive b3 (+1.426 MeV needed; open qou-brng), nucleon block sign flip, topology; scale/pin/convention/numerics ~1%. Open entries §5: Phase B flavour (sibling session_01EucfRmaNiqxRg52fQZeNVB), all-pairs Lean, E_osc provenance (#9221), full-tower trace, gg 6Li/7Li, non-trace energy map. Owner decision §6 pending (ACCURACY.md K_A plaquette rows use E_osc chart). Keep open until §6 answered.

2026-11-25 16:45Z: owner answered §6 with '2 then 1' (relayed by the coordinator). The provenance check is done: E_osc was pre-registered, not tuned, but the +1.81% headline is the cell nearest AME out of a 6×4 grid. Added the scope note under Table 3.2a (template), regenerated ACCURACY.md (--check PASS), added the ruling row. PR #9436 head 3d4d9b6b1. The scorecard decision is closed. The bean stays open for the §5 open entries (Phase B flavour, a Lean proof for all pairs, the full-tower trace, γγ 6Li/7Li, a non-trace energy map).
