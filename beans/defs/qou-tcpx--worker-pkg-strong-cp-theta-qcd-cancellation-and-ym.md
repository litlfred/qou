---
id: qou-tcpx
title: "SM/Eightfold Worker Pkg 5 (Q-Gap-11): Strong-CP theta_QCD=0 via 3x3 Singlet Writhe Cancellation & Multiscale Yang-Mills Freeze-Out"
status: todo
type: feature
priority: medium
parent: qou-sm8w
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T20:06:00Z
---

## Scope & Linked Legacy Beans (`tqcp`, `qou-1jqd`)

1. **Discharge `ColorSectorCPEven` (`theta_QCD = 0` without Axions, `tqcp`):** Formalize in Lean (`QOU/StandardModel/StrongCPBarCancellation.lean`) how closed `SU(3)_c`-singlet vacuum configurations (`det W_3 ~= 1` + bar-symmetric paired `T(2,9) oplus bar{T(2,9)}` colour-flux tubes in the `3x3` Bring `S_3 subset S_5` decomposition) cancel net chiral writhe identically (`theta_QCD = 0`, not `pi`, and zero `O(1)` radiative regeneration at 1-loop before 3-loop CKM Ellis-Gaillard `~10^{-16}`!).
2. **Wilson Area-Law String Tension & Multiscale RG Freeze-Out (`qou-1jqd`):** Formalize the discrete Wilson-loop string tension `sigma_str` from the Layer-1 crossing gap `Delta_q > 0` (`ConfinementLayerTower.lean`), proving discrete area-law decay `exp(-sigma_str * Area)` for non-singlet colour sources and documenting the exact Osterwalder-Schrader reflection-positivity condition from Nakayama-twisted Frobenius positivity (`#9197`, `#9205`).
