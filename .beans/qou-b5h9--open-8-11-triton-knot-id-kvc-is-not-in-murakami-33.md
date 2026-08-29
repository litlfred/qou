---
# qou-b5h9
title: 'OPEN: 8_11 (triton knot-ID) KVC is not in Murakami 3.3 - Ohtsuki machinery stops at 6 crossings, this is a paper'
status: todo
type: task
priority: normal
created_at: 2026-08-25T19:18:13Z
updated_at: 2026-08-25T19:59:13Z
parent: qou-9ot5
---

## ANSWERED 2026-08-25 — partly. See docs/audits/2026-08-25-is-8-11-kvc-attackable.md

NUMERICALLY YES, today. Colored Jones DOES exist in the repo - kashaev_link_statesum.py
(planar state sum + tensor network) is general over any PD code at roots of unity, and it
reproduces fig-8's closed form exactly and runs on 8_11. Cost is N^6 and 8_11 is only
~1.8x Whitehead at equal N (treewidth-bounded 2-bridge); N=61 ~ 10 min. Precision is NOT
the bottleneck - complex128 has ~14 digits of headroom.

THE BLOCKER IS THE CONVENTION, NOT COMPUTE. deficit_face_of returns None (non-unique) for
8_11; 1200 (strand-pair, outer-face) choices give 1184 distinct values at N=7, spanning
[5.205, 15.623]. And 19 of 1200 land within 5% of Vol=8.2863 BY CHANCE, 1 within 2%. So
scanning conventions against the volume is numerology. Needs an independent reference:
generalize norm_weightblock from 3 strands to arbitrary m (the one concrete build item).

PROVABLY NO. Ohtsuki-Yokota's homotopy step is 'quite non-trivial' and they state it FAILS
at 7_2 - an obstruction one crossing lower. Takata's 8-crossing paper is 'in preparation'
and whether 8_11 is in it is UNVERIFIED. And the repo's own squeeze method needs a
positive sum: 4_1 has one (proved), Whitehead does not (3556 Lean lines, two programmes,
both open on exactly that gap), 8_11 has none.

QOU BARELY NEEDS IT. The 3H->8_11 assignment is the same conj:canonical-knot-id-sdp shown
to be AME-driven census fitting, so a volume justification is CIRCULAR. Eleven consumers
use Vol(8_11) as a number, independently certified by SnapPy.

Bug caught: kashaev_link_statesum._solve_mod inverts via Fermat pow(a,N-2,N), valid ONLY
for prime N. Composite N are silently wrong.
