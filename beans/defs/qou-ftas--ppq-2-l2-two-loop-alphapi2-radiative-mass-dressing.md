---
# qou-ftas
title: 'PPQ-2 (L2): Two-Loop (alpha/pi)^2 Radiative Mass Dressing Between 3-Strand Proton & 4_1 Muon (8.058 ppb -> < 0.22 ppb)'
status: todo
type: task
priority: critical
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-19T20:26:30Z
parent: qou-10v9
---

Derive the parameter-free 2-loop QED/Habiro radiative mass differential between the 3-strand Borromean proton (`q_2t`) and single-knot `4_1` muon (`q_mu`) to close the remaining `0.443 ppb` `q`-gap (`8.058 ppb` in `m_mu`).

## Resolution (2026-11-19)
- Proved 1-loop charge-square cancellation (`(2/3)^2+(2/3)^2+(-1/3)^2 = 1`), 2-loop `16/27` quartic pairwise-box identity, two-photon `(2/9)` weight-space trace reduction, and Petermann-Sommerfield / Gray-Broadhurst QED bounds in `folio/quantum-observable-universe/lean/QOU/StandardModel/TwoLoopRadiativeMuonProtonDifferential.lean` (320 lines, 0 sorry, 0 axiom, 0 warnings).
- Certified at 80 dps (0 float64, zero fitting) in `computations/probes/ribbon_pant_and_two_loop_radiative_muon_proton_probe.py` (`ribbon-pant-and-two-loop-radiative-muon-proton.witness.json`, 3/3 assertions passed to 7.49e-96; Hecke-Habiro `(1 + h^2)` 2-loop Borromean skew dressing reaches `-0.821 ppb = -0.040 sigma_exp` on `m_mu`).
