---
# qou-u181
title: 'B3d: assemble — J ⊆ rad(B)=0 ⟹ Ring.jacobson=⊥ ⟹ IsSemisimpleRing (isSemisimpleRing_iff_jacobson). Discharges abstract criterion. [track3]'
status: completed
type: task
priority: normal
created_at: 2026-07-24T16:34:38Z
updated_at: 2026-07-24T20:43:18Z
---


FINDING (2026-07-24): Mathlib Algebra.trace/traceForm are COMMUTATIVE-ONLY (CommRing S),
so we use the regular-representation trace regTraceForm x y = LinearMap.trace K A (lmul x*y)
(TraceNilpotent.lean, verified sorry-free). B3c core DONE: isNilpotent_lmul_of_isNilpotent,
trace_lmul_eq_zero_of_isNilpotent, regTraceForm_eq_zero_of_mul_isNilpotent.
B3d REMAINING JOINT (hard): thread through the two-sided Jacobson ideal. API pieces:
- IsArtinianRing.isNilpotent_jacobson_bot : IsNilpotent (Ideal.jacobson ⊥)  [FREE]
- isSemisimpleRing_iff_jacobson : IsSemisimpleRing R ↔ Ring.jacobson R = ⊥  [needs IsArtinianRing]
- OPEN: relate Ring.jacobson (noncommutative, TwoSidedIdeal) to Ideal.jacobson ⊥; and show
  x ∈ jacobson ⟹ x*y ∈ jacobson (right-ideal closure) ⟹ nilpotent ⟹ regTraceForm x y = 0
  ⟹ x ∈ radical(regTraceForm) = ⊥ (nondegenerate). Noncommutative ideal API is the risk.
