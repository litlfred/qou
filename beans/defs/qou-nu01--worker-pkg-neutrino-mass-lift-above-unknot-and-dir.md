---
# qou-nu01
title: 'SM/Eightfold Worker Pkg 4 (Q-Gap-10): Non-Zero Neutrino Mass Lift Above Unknot Vol(0_1)=0 & Dirac vs. Majorana Framing Test'
status: in-progress
type: feature
priority: medium
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T23:51:20Z
parent: qou-sm8w
---

## Scope (`sm-params-neutrino.md`)

1. **Radiative / Sweedler-Jet Mass Lift on `0_1`:** Formalize in Lean (`QOU/StandardModel/NeutrinoUnknotLift.lean`) why `Vol(0_1) = 0` vanishes at tree level in the volume-density chain while 2-loop weak `T(3,5)` Sweedler radical dressing generates `m_nu ~ (q_0^2 - 1)^{12} m_e` (`~0.024 eV` at `q_0 = 1.10998`, matching atmospheric `sqrt(Delta m_{31}^2) ~ 0.050 eV` order-of-magnitude with zero fitting!). Pre-register and evaluate exact candidate two-vertex weak-self-energy diagrams at 80 dps.
2. **Dirac vs. Majorana Character:** Prove whether bar-conjugation / mirror orientation on framed unknots `(0_1, +1)` vs `(0_1, -1)` preserves lepton number (`U(1)_{B-L}` Dirac) or admits a framing-change Majorana mass term (`Delta L = 2`, predicting `m_{beta beta}` for `0nu2beta`).



## Worker 25 Delivery Note (2026-11-23 — Issue #9229, PR #9230 Ready, Holding Merge for Owner OK)

- **Branch:** `claude/sm8w-neutrino-unknot-sweedler-lift-20261123` (HEAD `062a7e40e52`, rebased cleanly onto `origin/main` `a9cd4483fe5`)
- **GitHub Issue:** https://github.com/litlfred/qou/issues/9229
- **Ready PR:** https://github.com/litlfred/qou/pull/9230 (push comment: https://github.com/litlfred/qou/pull/9230#issuecomment-7117427523)
- **Lean 4 Module:** `folio/quantum-observable-universe/lean/QOU/StandardModel/NeutrinoUnknotSweedlerMassLift.lean` (wired in `QOU.lean`, `0` errors, `0` warnings, `0` sorries, standard axioms `[propext, Classical.choice, Quot.sound]` only, `§7c` generic + `_real` specializations):
  1. `unknot_tree_invariants_and_volumeMass_zero` & `lepton_selfEnergy_projects_neutral_slot` (`E * diag(0, me) * F = me • Pu` onto neutral `ν_L` while `F*D*F = E*D*E = 0`).
  2. `sweedlerMassLift_pos`, `t35TwoLoopSweedlerLift_pos`, `weinbergSeesawScale_pos`, `sweedlerMassLift_at_one_eq_zero`, `sweedlerMassLift_strictAnti`.
  3. `dirac_framing_conserves_and_forbids_majorana`, `majorana_zmod2_quotient_kills_lepton_number_and_permits_pair`, `sweedler_antipode_sq_eq_conj_G_and_pow_four` (`S^2(a) = G a G`, `S^4 = id`), `sweedler_antipode_sq_ne_id_and_nakayama_ne` (`S^2(X) = -X != X`, `nakayama(G) = -G != S^2(G)`), `bare_majorana_bilinear_forbidden`, and `weinberg_quadratic_singlet_sweedler_invariant_and_vev` (`O_W = eps_ew(L_1,H_1)*eps_ew(L_2,H_2)` invariant under 4-fold Sweedler `Delta^(3)(G)` & `Delta^(3)(X)` and reducing at `H = (0, v_EW)` to `v_EW^2 nu_{L,1} nu_{L,2}`).
  4. `s3_commutant_iff`, `s3NeutralMass_spectrum_trace_det`, `nh_splittings_pos_and_ratios`, `ih_splittings_sign_and_ratio`, and `nh_mass_sum_lt_ih_of_matched_splittings`.
- **Pre-Registered `80`-dps Probe & Witness (`computations/probes/sm8w_neutrino_unknot_sweedler_lift/`):**
  - `PREREGISTRATION.md` committed first (`17eb2cb7635`); `sm8w-neutrino-unknot-sweedler-lift.witness.json` (`7/7` assertions passed, `q0Anchor = "proton"`, `stale: False`, `0` float64).
  - Key `80`-dps findings: `k = 12` Sweedler (`12.46 meV`) and `T(3,5)^2`-dressed (`17.57 meV`) land inside the PDG `[8.68, 49.53] meV` window (`sum m_nu(NH) = 0.0157-0.0221 eV < 0.12 eV`); `C_Nv_r6` (`M_UV = m_p N_v^6 = 3.064e14 GeV`) gives `197.9 meV`; `D_M4_k4_control` gives `9.123 meV` (`+5.14%` vs `sqrt(dm21^2)`), while compounding `(alpha_W/pi)^2` with `k >= 8` double-counts weak loop suppression (`<= 0.0265 meV`); `S_3 -> S_2` spurion `2*eps/b = q_0^2 - 1` (`0.05691`) and `hbar_q` (`0.00991`) bracket PDG `dm21^2/|dm32^2| = 0.03070`.
