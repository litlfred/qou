---
# qou-azs1
title: Explore I_{1,2}(1) = (e^{i pi/6}/sqrt3)*2 sinh(Vol(4_1)/2pi) vs the CAL-2 anchor
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:52:00Z
updated_at: 2026-08-10T23:29:33Z
parent: qou-i85j
---

SETTLED. The identity is already the G1 GATE of qbeta_5two_chirality_state_integral_probe.py, verified by independent quadrature of the Faddeev state integral to rel err 1.097e-19: exact = quad = (0.328715166319487 + 0.189783789761268j). So it is not just 'V matches Vol(4_1)' - the whole state integral reproduces the closed form. STRUCTURAL PLACEMENT (the part that was genuinely open): b=1 => tau = b^2 = 1 => q = e^{2 pi i} = 1, so this identity sits at the CLASSICAL point q=1, NOT at the substrate. The substrate ray is tau = i*beta => q = 1/q0 = 0.9009. Two different points of the same q-family that happen to share V. HOW EACH USES V: literature 2 sinh(V/2pi) = 0.657430 (V/2pi = 0.323066); framework V/hbar_q^2 = 206.768 = m_mu/m_e. The denominators are unrelated - 2pi is universal, hbar_q^2 = 0.0098172 is substrate-dependent; ratio hbar_q^2/(2pi) = 0.00156 shows no structure. So: same constant, different evaluation points, different denominators. The sinh-vs-CAL-2 echo is an appearance, not a correspondence - consistent with anti-numerology expectations, since Vol(4_1) is what BOTH objects are built from (one is defined by the figure-eight knot).
