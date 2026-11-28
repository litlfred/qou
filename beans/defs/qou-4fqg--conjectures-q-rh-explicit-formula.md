---
# qou-4fqg
title: 'Conjectures: q-RH / explicit formula'
status: todo
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:03Z
updated_at: 2026-11-28T03:05:00Z
parent: b9cj
---

Sub-epic P2.QRH of UMBRELLA: open conjectures (formal mathematics only) (work-plan reorganisation 2026-10-04).

## 2026-11-22T21:58:00Z: applicability review — APPLIES

Owner instruction 2026-11-22 ("reviewed for applicability ... critical analysis"). Checked against docs/coordination/owner-rulings.md on origin/main, git log since the bean's last update, and the state of every PR it cites. Umbrella epic for q-RH; children open.

## 2026-11-28T03:05:00Z: q-RH cleanup (PR #9984)

Owner thread 2026-11-28. The intros of sec:q-gl-weil-bound-stability and sec:classical-limit-implications now state what QOU can say about RH. Finding: Bring's local zetas multiply to zeta(s)zeta(s-1)/L(E,s)^4 with E = 50a1 (exact counts at 7<=p<=41 and F_49 in computations/bring_local_zeta_point_counts.py), so local alignment feeds L(E,s), not zeta(s). conj:adelic-critical-line-persistence restates RH: its hypothesis shares no data with riemannZeta. Restating it for L(E,s) waits on the owner's card. rem:rh-surreal-bound relabelled as a heuristic. New Lean module QOU/BringsSurface/BringHasseLocalZeta.lean: IsWeilZeta for (X^2-aX+p)^4 when a^2<=4p, plus the Hasse table.
