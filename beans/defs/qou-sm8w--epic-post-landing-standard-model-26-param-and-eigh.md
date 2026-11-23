---
id: qou-sm8w
title: "EPIC: Post-Landing Standard Model (26-Param & Lagrangian) + Eightfold Way Structural Gap Closure"
status: in-progress
type: epic
priority: critical
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T20:06:00Z
---

## Overview

Umbrella epic coordinating worker-ready Lean 4 + 80-dps derivation packages for every remaining structural block in `appendix-standard-model` (26 SM parameters + Lagrangian terms) and `eightfold-way` after the Nov-23 Frobenius / L2 / 5-Layer `ConfinementLayer` PR wave lands.

## Child Worker Packages (Queued as `Q-Gap-1..2` + `Q-Gap-7..11`)

1. **`qou-gen3` (`Q-Gap-7`, aggregates `qou-x4qm`, `qou-xtcl`, `qou-htk4`, `qou-y0mq`):** Three-generation replication (`N_gen = 3` Riemann-Roch / Prym zero-mode count on Bring `Z_3 x Z_5` curve, excluding `T(2,9)`), `S_3 subset S_5` overlap CKM/PMNS Yukawa texture generator, and satellite `T(2,n)-4_1` tau mass carrier (`18/26` SM params).
2. **`qou-8fw2` (`Q-Gap-8`, aggregates `qou-20sx`, `qou-3oi0`, `qou-wyy9`, `qou-yw3v`, `qou-ywsk`, `qou-c9uj`):** Eightfold Way `W_3^*`-decorated HOMFLY-PT (`a = q^3`) framed hypercharge `Y`, ordered content-to-braid map (`bar{D}^0 != K^0`), diquark Casimir `Lambda-Sigma^0` 77 MeV split, 2nd-order GMO 6% deviation, `eta-eta'` Witten-Veneziano `U(1)_A` susceptibility, full `N=3` `dim Sym^3 = 10` decuplet, and `eightfold-open-problems.md` sync with `F = V_2 oplus W_3^*`.
3. **`qou-ewsb` (`Q-Gap-9`, aggregates `qou-ukqh`, `qou-z3x8`, `qou-zd6l`, `qou-5iaz`, `qou-0whz`):** Categorical Higgs / EWSB mechanism (`CategoricalHiggsMechanism`), `v_EW` & `m_H` (`lambda_H`) combining `#9204` Sweedler `(q_0^2-1)^8` scaling with toroidal `T(2,4), T(2,6), T(2,8)` Schur/Habiro invariants, and UV-to-`M_Z`/`Lambda_QCD` RG threshold matching for `sin^2 theta_W(M_Z)` and `alpha_s(M_Z)`.
4. **`Q-Gap-1` & `Q-Gap-2` + `qou-37y0` (`qou-15sj`, `qou-91w7`, `qou-37y0`):** Archimedean 2-loop `Delta_2` & `[10]_q` for `alpha_EM`, joint Hopf+`4_1` `mu-p` anchor closure, and intra-nucleon Borromean Jackson `q^{-2}` EM self-energy for scheme-comparable `m_d - m_u`.
5. **`qou-nu01` (`Q-Gap-10`):** Non-zero neutrino mass lift above `Vol(0_1) = 0` (higher-order Sweedler/Taft `(q_0^2-1)^{12..16}` / Reidemeister torsion through `T(3,5)` weak loop) and topological Dirac vs. Majorana framing test (`0nu2beta`).
6. **`qou-tcpx` (`Q-Gap-11`, aggregates `tqcp`, `qou-1jqd`):** Strong-CP `theta_QCD = 0` via `3x3` `SU(3)_c`-singlet bar-involution writhe cancellation (`ColorSectorCPEven` + `det W_3 ~= 1`) and multiscale `ConfinementLayer` (`qou-5lct`) Wilson-loop / 4D Yang-Mills freeze-out bridge.
