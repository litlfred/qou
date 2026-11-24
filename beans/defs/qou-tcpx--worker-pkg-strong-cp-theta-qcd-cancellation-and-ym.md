---
# qou-tcpx
title: 'SM/Eightfold Worker Pkg 5 (Q-Gap-11): Strong-CP theta_QCD=0 via 3x3 Singlet Writhe Cancellation & Multiscale Yang-Mills Freeze-Out'
status: in-progress
type: feature
priority: medium
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-24T00:10:29Z
parent: qou-sm8w
---

## Scope & Linked Legacy Beans (`tqcp`, `qou-1jqd`)

1. **Discharge `ColorSectorCPEven` (`theta_QCD = 0` without Axions, `tqcp`):** Formalize in Lean (`QOU/StandardModel/StrongCPBarCancellation.lean`) how closed `SU(3)_c`-singlet vacuum configurations (`det W_3 ~= 1` + bar-symmetric paired `T(2,9) oplus bar{T(2,9)}` colour-flux tubes in the `3x3` Bring `S_3 subset S_5` decomposition) cancel net chiral writhe identically (`theta_QCD = 0`, not `pi`, and zero `O(1)` radiative regeneration at 1-loop before 3-loop CKM Ellis-Gaillard `~10^{-16}`!).
2. **Wilson Area-Law String Tension & Multiscale RG Freeze-Out (`qou-1jqd`):** Formalize the discrete Wilson-loop string tension `sigma_str` from the Layer-1 crossing gap `Delta_q > 0` (`ConfinementLayerTower.lean`), proving discrete area-law decay `exp(-sigma_str * Area)` for non-singlet colour sources and documenting the exact Osterwalder-Schrader reflection-positivity condition from Nakayama-twisted Frobenius positivity (`#9197`, `#9205`).


### Worker 26 Delivery (2026-11-23, branch `claude/sm8w-strong-cp-theta-qcd-string-tension-20261123`)

- **GitHub Issue:** https://github.com/litlfred/qou/issues/9233
- **Ready PR (held for owner OK):** https://github.com/litlfred/qou/pull/9234 (head `c48102d2974`)
- **Lean 4 Module (`0 sorry`, standard axioms only, zero empirical constants):** `folio/quantum-observable-universe/lean/QOU/StandardModel/StrongCPWritheCancellationAndStringTension.lean` (wired into `QOU.lean` next to `ThetaQcdFramingCp`):
  - **§1 (`\theta_{\mathrm{top}} = 0` & `ColorSectorCPEven`):** Signed Artin braid words, `writheWord_mirror_pair_eq_zero`, amphicheiral zero writhe on `4_1` & Borromean links, single-gluon chirality `w(T(2,9)) = +9 != 0` vs closed mirror-pair `w(T(2,9) ⊕ T̄(2,9)) = 0`, `wordPerm_sign_eq_neg_one_zpow_writhe`, rank-1 `[1^3]` Levi-Civita singlet projector `singletProj3` (`P^2 = P`, `Tr P = 1`), `sl_3(R)` Lie annihilation & `SL_3(R)` group invariance, balanced `[1^3]` Hecke phase cancellation, constructive `colorSectorCPEvenOfMirrorPair` (`framingPhase = 1`), and `cpEven_zpow_iff_zero_and_ne_neg_one` strictly excluding `\theta = \pi` (`\Theta = -1`) at ordered `q > 0, q != 1`.
  - **§2 (`\arg\det(M_u M_d) = 0` with `J_{\mathrm{CP}} != 0`):** Characteristic-free `3x3` Hermitian determinant reality `det_mul_hermitian3_im_eq_zero` & Sylvester positivity `det_mul_gramDiag3_real_and_pos` over `QuadI R = R[i]`, Jarlskog commutator-cube identity `jarlskog_commutator_cube_trace`, integer coexistence witness `strong_cp_zero_coexists_with_jarlskog_cp` (`det(M_u M_d) = 312 > 0`, `Im Tr([M_u^2, M_d^2]^3) = -351360 != 0`), factorized 1-loop chiral dressing no-regeneration `det_chiralDressed_im_eq_zero`, and zero-instance `HigherLoopStrongCPFiniteHypothesis` (`§3b-cond`).
  - **§3 (`\mathfrak{su}(3)_c` Casimir `9/4` & Markov-trace string tension):** Matrix-commutator proofs `su3_fundamental_casimir_matrix` (`4/3`), `su3_adjoint_casimir_matrix` (`3`), `su3_casimir_scaling_and_baryon_half_law` (`9/4` ratio & `1/2` baryon Y-junction law), `QOU.QInteger.qIntBal q 3` bridge, `markovZ3_confinement_bounds` (`0 < z_3(q) < 1` on `(0, 3/2]`), `creutz_ratio_cancels_perimeter`, `confinementLayer_worldsheet_area_lower_bound`, and paired `_real` area law `markovAreaDecay_real`.
- **Pre-registered 80-dps Probe & Stamped Witness (`q0Anchor = "proton"`, `stale: False`, `7/7` assertions):** `computations/probes/sm8w_strong_cp_string_tension/` (`PREREGISTRATION.md` committed first in `c16267ee045`, witness stamped in `c48102d2974`).
  - **Arm A:** Dense rotated `3x3` Hermitian Yukawa pair (`J_CP = 3.513e-5`) gives `|Im det(M_u M_d)| = 1.96e-86 < 1e-78` (`\bar{\theta}_{\mathrm{tree}} = 0`) and 1-loop chiral-dressed `|Im det| = 1.37e-86 < 1e-78`; finite 3-loop Ellis–Gaillard shift `2.52e-20` (envelope `3.20e-22`, induced `|d_n| = 6.04e-36 e*cm`) sits `10^10` below `PDG-2024`, while UV counterterm finiteness remains open.
  - **Arm B (honest hits & misses, `selectedCandidate = "none"`):** From `z_3(q_0) = q_0^3/[3]_{q_0} = 0.449305`, `0/7` zero-parameter candidates lie strictly inside `[420, 440] MeV`; half-proton-radius Y-junction arm `S5b_rp_half = 419.62 MeV` (`-2.41%` vs `430 MeV`, `-0.38 MeV` below `420 MeV`) and `N_c=3` bar-symmetric pion subcell `S3_pi_nc3_sym = 441.75 MeV` (`+2.73%` vs `430 MeV`, `+1.75 MeV` above `440 MeV`) bracket the lattice/Regge band, while `S2_pi_nc3 = 374.52 MeV` (`-12.90%`), `S6_rp_half_sym = 494.95 MeV` (`+15.10%`), `S1_pi_bare = 124.84 MeV` (`-70.97%`), `S5a_rp_full = 209.81 MeV` (`-51.21%`), and `S4_mp_compton = 839.24 MeV` (`+95.17%`) miss as reported.
