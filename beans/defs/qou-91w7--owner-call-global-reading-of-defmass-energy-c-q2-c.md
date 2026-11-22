---
# qou-91w7
title: 'OWNER CALL: global reading of def:mass-energy (c_q^2 converts mass to energy, or pure number); E0 pole'
status: todo
type: task
priority: normal
created_at: 2026-11-22T10:47:45Z
updated_at: 2026-11-22T11:09:02Z
parent: qou-wxhi
---

FINDING 2026-11-22 (thread "Make the n-p gap vanish at q = 1", issue #9002, audit docs/audits/2026-11-22-np-gap-at-q-one-unit-map.md s5, commit 3e8ff68c7; relayed to the n-p cell thread):
E0 = m_e c_q^2 hbar_q has a pole at q = 1. Whether that pole is a defect depends on ONE global reading of def:mass-energy (E = m c_q^2):
- (A) c_q^2 converts mass to energy. Then every E0-scaled MeV row is an energy compared with a CODATA mass and must be divided by c_q^2 ~ 82.68 at q0: the n-p cell becomes 2 m_e hbar_q ln q = 0.01057 MeV (vanishes at q = 1, -99.18 % vs 1.29333), the beta-vertex budgets become 0.00508 MeV (placement B) and 0.00946 MeV (placement C), and Q_beta, the z_D cell and binding all land near -99 %.
- (B) c_q^2 is a pure number (experiment uses c = 1). Nothing is mixed; current rows and budgets stand; the q = 1 pole stays.
Reading (A) clashes with the q0 pin: CAL-2 (m_mu/m_e = Vol(4_1)/hbar_q^2) and the proton pin both put 1/hbar_q^2 = q^2 c_q^2 inside dimensionless mass ratios.
DEFAULT: (B) until the owner decides. OWNER DECISION needed. No code or content changes yet.



2026-11-22 PIPELINE TRACE (n-p cell thread, owner asked to talk it through the canonical chain):
- Steps 1-8 (R-matrix action, Stokes -> Hecke quadratic, Markov trace, Wedderburn, Frobenius pairing, weight-space/GB-NF): every object is in Q(q). No unit and no c_q appears. categorical-lagrangian.md has no c_q or hbar_q.
- def:information-speed-of-light: c_q := q^-1/hbar_q = 1/(q-1). It is a RATIO OF TWO COUPLING WEIGHTS, so an element of Q(q), dimensionless as defined. The prose calls it 'not set to 1', a Lieb-Robinson velocity.
- def:mass-energy: E(beta) = m(beta) c_q^2 with m(beta) = framing-corrected |tr_M| in R (def:mass-identity). Both sides are elements of R before tau.
- MeV enters ONLY at step 9 through CAL-1 m_e. Energies are attached to it two different ways in the corpus: (i) E0 = m_e c_q^2 hbar_q = m_e/(q(q-1)) (energy-scale-planck.md: 'energy of one Hecke reduction step'; used for Q_beta, the log binding functional, the n-p cell); (ii) cheat-sheet step 9 B = m_e*rho*[...] (energy = m_e x number, no c_q^2). So the corpus is internally mixed REGARDLESS of reading: two energies, one with c_q^2 and one without.
- The CAL-2 pin m_mu/m_e = Vol(4_1)/hbar_q^2 is dimensionless only if hbar_q is a pure number, and then c_q = q^-1/hbar_q is too. So reading A (c_q is the image of physical c, mapped to 1) contradicts the pin; reading B (c_q^2 an element of Q(q) evaluated at q0) is what the definitions literally say. Supports the other thread's point (2).
- Under B, def:mass-energy defines a categorical energy, not physical rest energy E = m c^2 (c = 1 would force c_q = 1). The q = 1 pole is then real: the MeV n-p cell tends to 2 m_e = 1.022 MeV as q -> 1. That is a model statement, not a defect.
- Agent's recommendation (judgement): keep reading B as the default, scope the 'speed of light' wording, and separately audit which energies use E0 and which use bare m_e (bean to follow if the owner agrees).
