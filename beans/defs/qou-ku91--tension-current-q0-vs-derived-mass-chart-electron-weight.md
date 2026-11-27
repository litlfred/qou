---
# qou-ku91
title: 'Tension: current q0 (hand-placed electron weight) vs derived mass-chart weight w_e'
status: todo
type: task
priority: high
created_at: 2026-11-27T22:16:00Z
updated_at: 2026-11-27T22:16:00Z
parent: qou-91w7
---

OWNER CARD 2026-11-27 22:15Z (thread "Derive the electron's categorical weight"): "Keep q0, open a tension bean". q0 is unchanged.

DERIVED (PR #9733, Lean QOU/Transcendental/MassTheory/ElectronMassChartWeight.lean): the mass formula's own rule is the energy reading q d/dq log Z (the carrier's hbar_q^-2 pole forces one derivative). On the electron it gives
  w_e = 3 + 4q^2(q^2-1)/((q^4+1)(q^2+1)), w_e(1) = 3 (writhe), 3.2035 at q0,
replacing the hand-placed weight 1 of the unit m_e/hbar_q^2. The n-p cell on this chart is -2/w_e m_e (neutron BELOW proton; sign from #9767).

TENSION (shadow run, PR #9772, audit docs/audits/2026-11-27-electron-categorical-weight.md s8): the proton pin re-solved with w_e gives q0'' = 1.063363. At q0'':
- alpha_EM^-1 = 107.19 (-21.8 %; -0.37 ppb now). Pure function of q, so no unit fixes it.
- m_mu (m_e/w_e unit) -11.4 % (+211 ppb now); m_tau/m_e -17.6 %; v_weak -16.2 %.
- Q-CLT binding median improves 68.9 % -> 57.1 %.
Switch: QOU_Q0_SHADOW=derived_we (shadow only).

So the current q0 and the derived electron weight cannot both hold without alpha_EM and m_mu moving.

OPEN: find the derived reason (if any) that the carrier coefficient is Vol and not Vol/w_e(1) = Vol/3, or a second derived factor in the mass chart that cancels w_e. No fitting: do not divide by the writhe or pick a factor to restore alpha_EM or m_mu.
Related: qou-6gf9, #9718 (log chart, merged), #9725 (wiring, merged), #9692 (Vol/3 finding).
