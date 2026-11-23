---
# qou-nu01
title: 'SM/Eightfold Worker Pkg 4 (Q-Gap-10): Non-Zero Neutrino Mass Lift Above Unknot Vol(0_1)=0 & Dirac vs. Majorana Framing Test'
status: in-progress
type: feature
priority: medium
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T23:09:33Z
parent: qou-sm8w
---

## Scope (`sm-params-neutrino.md`)

1. **Radiative / Sweedler-Jet Mass Lift on `0_1`:** Formalize in Lean (`QOU/StandardModel/NeutrinoUnknotLift.lean`) why `Vol(0_1) = 0` vanishes at tree level in the volume-density chain while 2-loop weak `T(3,5)` Sweedler radical dressing generates `m_nu ~ (q_0^2 - 1)^{12} m_e` (`~0.024 eV` at `q_0 = 1.10998`, matching atmospheric `sqrt(Delta m_{31}^2) ~ 0.050 eV` order-of-magnitude with zero fitting!). Pre-register and evaluate exact candidate two-vertex weak-self-energy diagrams at 80 dps.
2. **Dirac vs. Majorana Character:** Prove whether bar-conjugation / mirror orientation on framed unknots `(0_1, +1)` vs `(0_1, -1)` preserves lepton number (`U(1)_{B-L}` Dirac) or admits a framing-change Majorana mass term (`Delta L = 2`, predicting `m_{beta beta}` for `0nu2beta`).
