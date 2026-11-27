---
# qou-gg4e
title: 'GAP: derive alpha_EM from the electron word sigma0 sigma1 sigma0 (Hopf closure); none in corpus'
status: todo
type: task
priority: normal
tags:
    - compute-accuracy
created_at: 2026-11-22T10:47:45Z
updated_at: 2026-11-27T14:18:32Z
parent: qou-wxhi
---

Owner 2026-11-22: "need to figure out how [alpha_EM] is directly connected to the electron word."

FINDING: no block or audit found (grep of content/ + docs/audits) derives alpha_EM from the electron word sigma0 sigma1 sigma0 in B3 with Hopf-link closure (owner ruling; trefoil sigma0^3 in B2 kept as backup). The live alpha_EM forms are q*[9]_q*[10]_q (force-carrier torus knots T(2,9), T(3,5)) with a CS correction (1 + delta_CS + kappa delta_CS^2), kappa admitted as a Lean sorry (rem:em-coupling-projection-discussion).

CANDIDATE TEST (preregister before any number): under reading 1 of the complex-readings bean (EM = arg tr_M), compute the phase of tr_M of the electron word's closure, with framing, at the fibre level (formal q / root of unity, since q0 is real), and state whether it is a function of q that could give alpha_EM without selection. Derive, do not fit; a miss is a result.

Also record: alpha_EM terms are the one class NOT covered by the m_p = m_n at q = 1 working assumption (bean qou-az9l scope; alpha*QPair*hol = -m_e/720 at q = 1, PR #8804 s40).

Routed to thread "Settle which alpha_em form is canonical". Not started.



2026-11-22, from thread 'Settle which alpha_em form is canonical' (PR #8987): under convention D the iota-odd part (iota: sigma -> -sigma^-1) of the Markov trace is exactly (y3/2)*tau with tau = chi_3 - chi_111 the alpha_em functional; tau(w) = q^e - (-q^-1)^e depends only on the writhe e. Sorry-free Lean: QOU/AlphaEM/TauExponentSum.lean. Electron sigma0 sigma1 sigma0: tau = q^3 + q^-3. At q = 1, tau = 1 - (-1)^e (not yet compared with -m_e/720). Consistent with the writhe-phase reading of rem:mass-modulus-em-phase-color-grading; does NOT show mass is the iota-even part.
