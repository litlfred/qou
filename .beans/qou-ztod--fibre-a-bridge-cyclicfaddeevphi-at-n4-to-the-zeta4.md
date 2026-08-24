---
# qou-ztod
title: 'FIBRE-A: bridge CyclicFaddeevPhi at N=4 to the zeta4 analytic model -- the two sorry-free zeta4 artifacts do not touch'
status: todo
type: task
priority: normal
created_at: 2026-08-19T14:21:19Z
updated_at: 2026-08-19T14:21:54Z
---

FINDING: grep -rl CyclicFaddeevPhi over the whole QOU tree returns its OWN FILE AND NOTHING ELSE. Two sorry-free zeta4 objects exist and do not touch: (1) QOU/Mass/ComplexVolumeZeta4Partner.lean -- analytic model vModel z = cosh z + i sinh z over C, with the zeta4 orbit, vanishing trivial/sign isotypes, and IsZeta4Faithful as a PROVED falsifier; (2) QOU/QBeta/FaddeevPhiFibreBranch.lean -- algebraic CyclicFaddeevPhi zeta N D over a generic field, discharged unconditionally at every primitive N-th root of unity by the finite q-Pochhammer. zeta4 = i is primitive 4th, so CyclicFaddeevPhi zeta 4 sits exactly where the model rotation acts. frakV_descent_zeta4_partner_probe.py records single_fibre_V OPEN, "Missing: both fibre kernels AND their assembly"; one kernel may already be built and merely unconnected. HONEST CAVEAT from the fibre-branch file itself: there is NO sorry-free bridge making the cyclic dilog an instance of the exact C-FaddeevPhi class -- the correspondence is a genuine DEGENERATION of the functional equation. So bridge to the zeta4 ACTION on vModel, not to FaddeevPhi. Falsifiable at once: nonzero zeta4 orbit sum or nonzero sign isotype refutes the assembly. Doc: option A.
