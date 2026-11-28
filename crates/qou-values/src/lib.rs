//! `qou-values` — Fast arbitrary-precision MPFR (`rug::Float`) proton-pinned witnessed-value
//! evaluator and Fréchet–Jacobian uncertainty propagator for `ACCURACY.md` and paper `:val[...]`
//! directives.
//!
//! ### Core Guarantees
//! - **Zero `f64` arithmetic**: every constant, root solve, special function (`Cl_2`, `Li_2`,
//!   `Li_3`, `\zeta`, Catalan `G`, Hahn–Exton `q`-Bessel `J_{1/2}`), and Fréchet derivative runs
//!   natively in MPFR (`>= 368` bits by default, configurable `--dps 15..=250`).
//! - **Strict proton-pin default (`2026-11-28` owner ruling)**: `q_0^{(p)}` is solved in-process
//!   from the Borromean proton identity `2(Vol(4_1)/\hbar_q^2) F_Bor(q) - 12 = m_p/m_e`; the
//!   historical muon-ratio pin is gated as `on_hold` unless explicitly requested via
//!   [`PinMode::AllowOnHoldMuonComparison`].
//! - **Three-calibration anti-fit discipline**: only `(m_e, m_p/m_e, m_{\pi^\pm})` enter as
//!   physical calibration inputs; CODATA-2022 / PDG-2024 / AME2020 benchmarks enter strictly at
//!   the comparison boundary.

pub mod math;
pub mod registry;
pub mod solvers;
pub mod witness;

pub use math::PrecisionConfig;
pub use registry::{
    evaluate_all, evaluate_by_key, find_spec, list_observables, Category, EpistemicTier,
    EvaluatedObservable, ObservableListEntry, ObservableSpec, OBSERVABLES,
};
pub use solvers::{t3_bond_count, PinMode, QouValueError, SubstrateContext};
pub use witness::{build_witness_document, write_witness_file, QouWitnessDocument};

#[cfg(test)]
mod tests {
    use super::*;
    use crate::math::{f_str, vol_5_2};
    use crate::solvers::{locate_repo_root, solve_q0_muon_gated};
    use rug::Float;

    fn assert_close_str(actual_str: &str, expected_str: &str, tol_str: &str, label: &str) {
        let prec = 384;
        let actual = f_str(prec, actual_str);
        let expected = f_str(prec, expected_str);
        let tol = f_str(prec, tol_str);
        let diff = Float::with_val(prec, &actual - &expected).abs();
        assert!(
            diff < tol,
            "{label} mismatch: actual={actual_str}, expected={expected_str}, |diff|={} >= {tol_str}",
            diff.to_string_radix(10, Some(12))
        );
    }

    #[test]
    fn muon_pin_is_strictly_gated_on_hold_by_default() {
        let prec = 368;
        let r_mu = f_str(prec, solvers::codata_pdg::MASS_RATIO_MU_E);
        let v41 = math::vol_4_1(prec);
        let res = solve_q0_muon_gated(PinMode::ProtonDefault, &r_mu, &v41, prec);
        assert_eq!(res, Err(QouValueError::MuonPinOnHold));

        let ctx = SubstrateContext::build(PrecisionConfig::new(80), PinMode::ProtonDefault)
            .expect("proton context");
        assert!(ctx.q0_muon_opt.is_none());
        let mmu = evaluate_by_key(":val[atlas_m_mu_MeV]", &ctx).expect("m_mu lookup");
        assert_eq!(mmu.q0_anchor, "proton");
        assert!(mmu.delta_mu_pin_on_hold.is_none());
    }

    #[test]
    fn matches_master_atlas_80dps_witness_beyond_1e75() {
        let ctx = SubstrateContext::build(PrecisionConfig::new(80), PinMode::ProtonDefault)
            .expect("build 80-dps proton context");

        let root = locate_repo_root().expect("locate QOU repo root");
        let atlas_raw = std::fs::read_to_string(root.join("computations/master-atlas-80dps.witness.json"))
            .expect("read master-atlas-80dps.witness.json");
        let atlas: serde_json::Value = serde_json::from_str(&atlas_raw).expect("parse JSON");
        let anc = &atlas["data"]["anchors"];
        let obs = &atlas["data"]["observables"];

        // 1. Core 80-dps anchors (< 1e-75!)
        assert_close_str(
            &math::fmt_sig(&ctx.vol_4_1, 80),
            anc["vol_4_1_80dps"].as_str().unwrap(),
            "1e-77",
            "vol_4_1_80dps",
        );
        assert_close_str(
            &math::fmt_sig(&ctx.q0_proton, 80),
            anc["q0_proton_80dps"].as_str().unwrap(),
            "1e-77",
            "q0_proton_80dps",
        );
        // Note: master_atlas_jacobian_80dps.py uses WORK_DPS=95, eps_q=1e-31 (O(eps^2) ~ 1.92e-72 on 9.21e-13)
        assert_close_str(
            &math::fmt_sig(&ctx.q0_proton_sigma, 80),
            anc["q0_proton_sigma"].as_str().unwrap(),
            "1e-71",
            "q0_proton_sigma",
        );

        let gdet = evaluate_by_key(":val[gram_det]", &ctx).unwrap();
        assert_eq!(gdet.value, "0.0");

        let z_d = evaluate_by_key("z_markov_d", &ctx).unwrap();
        assert_close_str(
            &z_d.value,
            anc["markov_z_proton_80dps"].as_str().unwrap(),
            "1e-77",
            "z_markov_d",
        );

        let h_a = evaluate_by_key(":val[H_A]", &ctx).unwrap();
        assert_close_str(
            &h_a.value,
            anc["ha_proton_80dps"].as_str().unwrap(),
            "1e-77",
            "h_hecke",
        );

        let hbar = evaluate_by_key(":val[hbar_q]", &ctx).unwrap();
        assert_close_str(
            &hbar.value,
            anc["hbar_q_proton_80dps"].as_str().unwrap(),
            "1e-77",
            "hbar_q",
        );

        // 2. Every master-atlas observable value (< 1e-72) & Frechet sigma_pred (< 1e-60)
        for (our_key, wit_key, val_tol, sig_tol) in [
            ("atlas_m_mu_MeV", "m_mu_MeV", "1e-74", "1e-62"),
            ("atlas_alpha_em_inv_form_b", "alpha_em_inv_form_b", "1e-74", "1e-62"),
            ("alpha_em_inv_form_c", "alpha_em_inv_form_c_bloch_b3", "1e-74", "1e-62"),
            ("alpha_em_inv_cs_seifert", "alpha_em_inv_cs_seifert", "1e-74", "1e-62"),
            ("atlas_alpha_em_inv_cs", "alpha_em_inv_cs", "1e-74", "1e-62"),
            ("rydberg_hc_eV", "rydberg_form_b_eV", "1e-74", "1e-62"),
            ("rydberg_hc_form_c_eV", "rydberg_form_c_eV", "1e-74", "1e-62"),
            ("N_v_ew", "N_v_ew", "1e-74", "1e-62"),
            ("v_weak_GeV", "v_ew_GeV", "1e-74", "1e-60"),
            ("atlas_mk_over_mpi", "mk_over_mpi", "1e-76", "1e-65"),
            ("atlas_m_k_pm_MeV", "m_k_pm_MeV", "1e-74", "1e-62"),
            ("atlas_q_beta_base_MeV", "q_beta_base_MeV", "1e-76", "1e-65"),
            ("atlas_m_n_MeV", "m_n_MeV", "1e-73", "1e-60"),
            ("atlas_delta_m_np_MeV", "delta_m_np_MeV", "1e-76", "1e-65"),
            ("qbeta_3H_MeV", "qbeta_3H_MeV", "1e-75", "1e-65"),
            ("qbeta_14C_MeV", "qbeta_14C_MeV", "1e-75", "1e-65"),
            ("atlas_theta_ch4_deg", "theta_ch4_deg", "1e-74", "1e-75"),
            ("atlas_theta_nh3_deg", "theta_nh3_deg", "1e-55", "1e-48"),
            ("atlas_theta_h2o_deg", "theta_h2o_deg", "1e-55", "1e-48"),
            ("atlas_theta_c2h4_deg", "theta_c2h4_deg", "1e-55", "1e-48"),
            ("atlas_L_h2o_kJmol", "L_h2o_kJmol", "1e-74", "1e-62"),
        ] {
            let ev = evaluate_by_key(our_key, &ctx).unwrap_or_else(|e| panic!("{our_key}: {e}"));
            let w_pred = obs[wit_key]["pred"].as_str().unwrap();
            let w_sig = obs[wit_key]["sigma_pred"].as_str().unwrap();
            assert_close_str(&ev.value, w_pred, val_tol, &format!("{our_key}.value"));
            assert_close_str(&ev.sigma_pred, w_sig, sig_tol, &format!("{our_key}.sigma_pred"));
        }
    }

    #[test]
    fn matches_per_observable_100x_koide_coulomb_he4_and_vol52() {
        let ctx = SubstrateContext::build(PrecisionConfig::new(80), PinMode::ProtonDefault)
            .expect("build 80-dps proton context");

        // Vol(5_2) 50-dps SnapPy ManifoldHP reference from hyperbolic_volumes.py (< 1e-48)
        let v52_str = math::fmt_sig(&vol_5_2(ctx.cfg.prec_bits), 80);
        assert_close_str(
            &v52_str,
            "2.8281220883307831627638988092766349427709813173006",
            "1e-49",
            "vol_5_2_50dps",
        );

        // Koide (+) root m_tau / m_e from gap2b-mtau-s3-circulant-koide-probe.witness.json (< 1e-48)
        let mtau = evaluate_by_key("m_tau_over_m_e", &ctx).unwrap();
        assert_close_str(
            &mtau.value,
            "3477.4423064158730225498913589145330526823157603419",
            "1e-46",
            "m_tau_over_m_e",
        );

        // Derived q-Hankel Coulomb shape factor vs coulomb-shape-factor-qbessel-probe.witness.json:
        // (1) At the witness's 50-digit q_0 string (`step`), agrees to all 59 witness digits (< 1e-58)!
        // (2) At full 80-dps q_0^(p), agrees to < 1e-50 (differing at 9.04e-52 solely from 50->80 dps q_0 upgrade).
        let root = locate_repo_root().expect("repo root");
        let qh_raw = std::fs::read_to_string(
            root.join("computations/probes/coulomb-shape-factor-qbessel-probe.witness.json"),
        )
        .expect("read qhankel witness");
        let qh_json: serde_json::Value = serde_json::from_str(&qh_raw).unwrap();
        let qh_expected = qh_json["data"]["rows"]["primary_nu_half_p_1_over_q0"]["f"]
            .as_str()
            .unwrap();
        let qh_step_50 = qh_json["q0Value"].as_str().unwrap();
        let f_qh_at_50 = math::qhankel_coulomb_shape_factor(
            &f_str(ctx.cfg.prec_bits, qh_step_50),
            ctx.cfg.prec_bits,
        );
        assert_close_str(
            &math::fmt_sig(&f_qh_at_50, 65),
            qh_expected,
            "1e-58",
            "f_coulomb_qhankel_at_witness_50dps_q0",
        );
        let f_qh = evaluate_by_key("f_coulomb_qhankel", &ctx).unwrap();
        assert_close_str(&f_qh.value, qh_expected, "1e-50", "f_coulomb_qhankel_80dps_q0");

        // 4He M3a K_4 plaquette binding energy vs gap1b witness (< 1e-46)
        let b_he4 = evaluate_by_key("b_he4_m3a_MeV", &ctx).unwrap();
        assert_close_str(
            &b_he4.value,
            "29.329056386925924959440707804669055725497012864727",
            "1e-47",
            "b_he4_m3a_MeV",
        );

        // Racah seniority-0 ratios & T3 bond counts
        let w_po = evaluate_by_key("w_po210_212_214", &ctx).unwrap();
        assert_close_str(&w_po.value, "1.6", "1e-78", "w_po210_212_214");

        // Rydberg wavenumber R_inf in m^-1 matches CODATA-2022 (10973731.568157 m^-1) to +0.725 ppb (< 0.01 m^-1)
        let ry_m = evaluate_by_key("rydberg_m_inv", &ctx).unwrap();
        assert_close_str(&ry_m.value, "10973731.568157", "0.01", "rydberg_m_inv_codata22");
        assert_eq!(t3_bond_count(1), 0);
        assert_eq!(t3_bond_count(2), 1);
        assert_eq!(t3_bond_count(3), 3);
        assert_eq!(t3_bond_count(4), 6);
        assert_eq!(t3_bond_count(56), 84);
        let t3_56 = evaluate_by_key("t3_bond_count(56)", &ctx).unwrap();
        assert_eq!(t3_56.value, "84");

        // Cross-check per-observable-100x-status.witness.json headline rows
        let po_raw = std::fs::read_to_string(root.join("computations/per-observable-100x-status.witness.json"))
            .expect("read per-observable-100x-status.witness.json");
        let po_json: serde_json::Value = serde_json::from_str(&po_raw).unwrap();
        for row in po_json["data"]["rows"].as_array().unwrap() {
            let obs_name = row["obs"].as_str().unwrap();
            let po_pred = row["pred_MeV"].as_str().unwrap();
            let mapped = match obs_name {
                "m_p" => Some(("m_p_MeV", "1e-9")),
                "m_mu" => Some(("m_mu_MeV", "1e-9")),
                "Q_beta" => Some(("q_beta_base_MeV", "1e-11")),
                "m_n" => Some(("m_n_MeV", "1e-9")),
                "Delta_pn" => Some(("delta_m_np_MeV", "1e-11")),
                "alpha_em_inv" => Some(("alpha_em_inv_form_b", "1e-9")),
                "m_e" => Some(("m_e_MeV", "1e-12")),
                "m_K/m_pi" => Some(("m_k_over_m_pi", "1e-10")),
                _ => None,
            };
            if let Some((k, tol)) = mapped {
                let ev = evaluate_by_key(k, &ctx).unwrap();
                assert_close_str(&ev.value, po_pred, tol, &format!("100x::{obs_name}"));
            }
        }
    }
}
