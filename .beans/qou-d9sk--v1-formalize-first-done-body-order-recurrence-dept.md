---
# qou-d9sk
title: 'V1 formalize-first DONE: body-order recurrence depth >= 3 forced; 3-term target is unfalsifiable (first prediction at body order 2d >= 6)'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:45:57Z
updated_at: 2026-08-29T18:46:55Z
parent: qou-mhj9
---

PR #6059. Lean: QOU/MassTheory/BodyOrderRecurrenceDepth.lean, sorry-free,
lean-direct exit 0 (3.1s), #print axioms clean on all 10 decls.

FINDING. Writing B_n = m_e * a^(n) (obligation (B) of
thm:binding-closure-conditional): a^0 = a^1 = 0 (no binding from zero or one
nucleon), a^2 != 0 (the deuteron binds).

1. d >= 3 is FORCED (three_le_depth). A depth-d recurrence whose first d terms
   vanish is identically zero for ANY kernel (eq_zero_of_initial_eq_zero), so
   the vanishing one-body term bounds the depth from BELOW. The corpus had only
   the upper bound d <= rank V <= 2g = 8.

2. THE 3-TERM TARGET IS UNFALSIFIABLE. At d = 3 the map (c1,c2) -> (a3,a4) is
   surjective (depth_three_kernel_reaches): c2 = t3/a2, c1 = (t4 - t3^2/a2)/a2
   realise ANY pair. So matching a2:a3:a4 = 1 : -0.519787 : +4.45038 solves for
   the kernel — an anchor inversion, i.e. the forbidden fit. Same shape as
   A4InterfaceMagnitude.magnitude_form_surjective.

3. FIRST PREDICTION AT BODY ORDER 2d. c0 survives unconstrained after a3,a4, so
   a5 is free too (a_five_free); a6 is the first determined value (a_six). With
   d >= 3 that is body order >= 6, i.e. A >= 6 (6Li) — the measurement covers
   A <= 4. Extending the Ursell inversion to 6Li/7Li is the PREREQUISITE.

4. S5 DICHOTOMY (scope-(b) on the conjunction). s5_bring_hodge_depth.lean
   proves H1(Bring) = W_(4,1)^+2. By Schur an equivariant endomorphism of W^+2
   satisfies a degree-<=2 char poly, i.e. d <= 2 — inconsistent with (1). So at
   least one fails: M is S5-equivariant; the operator-power index is the body
   order; or the one-body term vanishes. NOT a refutation of
   conj:qdifference-kernel-prolongation-symbol, which survives with
   non-equivariant M.

CONSEQUENCE: do NOT run the Bring Picard-Fuchs computation against the 3-term
ratio. It cannot decide anything. See qou-i5yp re-scope.
