---
# qou-m4fp
title: 'V2: fix the framing convention — CWF decides whether T(t) is the writhe in disguise'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T18:23:24Z
updated_at: 2026-10-04T15:25:22Z
parent: qou-v2om
---

Calugareanu-White-Fuller: Lk = Tw + Wr (in-corpus at helicity-conservation.md;
Moffatt-Ricca uploaded at 2988eb82). Under a FIXED framing, Tw and Wr are NOT
independent. So the chapter's ribbon-framing-twist candidate T(t), advertised as
'independent of the writhe', may be the writhe in disguise. Decision table:
  Seifert framing   (Lk=0)   => Tw = -Wr   -> T(t) IS writhe-determined; candidate COLLAPSES
  blackboard        (Lk=Wr)  => Tw = 0     -> T(t) identically 0; NO charge
  free/independent  (Lk free)=> Tw free    -> works, but T(t) is then a free label (the
                                             fit risk already proved in TwistBatteryVacuity)
The framework must say which. This single question decides T(t)'s viability AND
whether L may use framing (qou-kl39). Kauffman (uploaded) is the other half: the
writhe is NOT an ambient-isotopy invariant (Reidemeister I shifts it +-1), so
'Y = f(writhe)' is ill-posed until the framing is pinned.

## Round 75 Progress (2026-11-17T11:49:05Z)
- Advanced in PR `litlfred/qou#8329` (branch `feat/round75-blocklen-equilateral-bondletter-descent-framing-43c1`, head `d2c6d3d8e433b1ecf3e00634b44d230b097bc7d3`).
