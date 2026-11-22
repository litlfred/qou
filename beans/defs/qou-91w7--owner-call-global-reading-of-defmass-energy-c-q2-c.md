---
# qou-91w7
title: 'OWNER CALL: global reading of def:mass-energy (c_q^2 converts mass to energy, or pure number); E0 pole'
status: todo
type: task
priority: normal
created_at: 2026-11-22T10:47:45Z
updated_at: 2026-11-22T10:47:45Z
parent: qou-wxhi
---

FINDING 2026-11-22 (thread "Make the n-p gap vanish at q = 1", issue #9002, audit docs/audits/2026-11-22-np-gap-at-q-one-unit-map.md s5, commit 3e8ff68c7; relayed to the n-p cell thread):
E0 = m_e c_q^2 hbar_q has a pole at q = 1. Whether that pole is a defect depends on ONE global reading of def:mass-energy (E = m c_q^2):
- (A) c_q^2 converts mass to energy. Then every E0-scaled MeV row is an energy compared with a CODATA mass and must be divided by c_q^2 ~ 82.68 at q0: the n-p cell becomes 2 m_e hbar_q ln q = 0.01057 MeV (vanishes at q = 1, -99.18 % vs 1.29333), the beta-vertex budgets become 0.00508 MeV (placement B) and 0.00946 MeV (placement C), and Q_beta, the z_D cell and binding all land near -99 %.
- (B) c_q^2 is a pure number (experiment uses c = 1). Nothing is mixed; current rows and budgets stand; the q = 1 pole stays.
Reading (A) clashes with the q0 pin: CAL-2 (m_mu/m_e = Vol(4_1)/hbar_q^2) and the proton pin both put 1/hbar_q^2 = q^2 c_q^2 inside dimensionless mass ratios.
DEFAULT: (B) until the owner decides. OWNER DECISION needed. No code or content changes yet.
