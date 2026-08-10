---
# qou-he82
title: Evaluate the Faddeev state integral at the substrate anchor
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:52:00Z
updated_at: 2026-08-10T23:29:32Z
parent: qou-i85j
---

ALREADY BUILT IN THE CORPUS — found by corpus-grep before writing anything (third such catch this session). computations/probes/qbeta_5two_chirality_state_integral_probe.py (bean qou-u5xq) implements Z_41 = int Phi_b(v)^2 e^{-pi i v^2} dv and Z_52 on the substrate ray tau = i*beta, beta = ln(q0)/2pi. Ran it: 5/5 assertions PASS (1424s). G1 (4_1 at b=1 vs the Garoufalidis-Kashaev closed form): rel err 1.097e-19. G2 (5_2 at the substrate, quadrature vs GGM/Peacock factorization - two INDEPENDENT evaluations): rel err 3.404e-14. G3 (even+i*odd split residual): 1.4e-31. Odd channel nonzero at both muon and proton anchors. H: |d ln(odd)/dq| ~ 355.94 vs the ~3.84e6 an S-swing needs, so SRigidityPrune binds - this is the derived odd ingredient, NOT the swing. ALSO: the corpus's phi_b_substrate_regime.py independently pins the substrate branch to arg b = +pi/4 => q = e^{2 pi i b^2} = 1/q0, i.e. the BAR-CONJUGATE - the same point I reached independently from the (q;q)_k convergence analysis in PR #4957. My earlier probe's b^2 = -0.0166i (arg b = -pi/4) is the branch the corpus documents as NOT supporting the product form; corrected.
