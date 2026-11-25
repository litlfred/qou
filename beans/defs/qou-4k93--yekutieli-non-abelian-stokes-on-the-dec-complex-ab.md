---
# qou-4k93
title: 'Yekutieli non-abelian Stokes on the DEC complex: abelian DEC vorticity as its specialisation'
status: todo
type: task
priority: normal
created_at: 2026-11-25T16:33:40Z
updated_at: 2026-11-25T16:37:38Z
parent: qou-i6e2
---

Owner 2026-11-25: 'is the discrete Stokes, discrete na-Stokes per yektieli? do we need to use that?' (1) discrete multiplicative-integral face holonomy on a 2-complex using MathlibExt/YekutieliIntegration; (2) prove the abelian DEC vorticity d1 v (PR #9434) is its abelian specialisation; (3) say what in q-NS needs the non-abelian form.

2026-11-25T16:55Z DONE (1)(2)(3) in DECYekutieliStokes.lean, PR #9434, sorry-free: faceHolonomy_abelian, faceHolonomy_eq_vort (general->paper). Velocity 1-form needs only abelian; non-abelian needed only for connection-valued vorticity (SU_q(2) gauge-covariant diffusion, braid/Hecke transports). REMAINING: global non-abelian Stokes on Bring (ordered conjugated kite product of 24 faces = product of 8 commutators) — needs spanning tree + face order of Bring map in Lean; content block.

2026-11-25T17:05Z owner Q 'non-commutative vorticity, gap?': TwistedHarmonicBound.lean (sorry-free): any flat rank-r twist on Bring keeps dim H1 >= 6r (chi=-6), scope (b). Curved connection could gap sections but breaks d1d0=0; not formalised.
