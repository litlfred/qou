//! In-process MPFR root solvers, proton-pin Borromean anchor, gated muon-pin diagnostic,
//! and domain physics evaluators (zero `f64`, zero fitting beyond `(m_e, m_p/m_e, m_{pi+-})`).

use std::fmt;
use std::path::{Path, PathBuf};

use rug::ops::Pow;
use rug::Float;

use crate::math::{
    catalan, f_i64, f_str, pi, polylog3_real, q_int, qhankel_coulomb_shape_factor,
    trace_poly_two_p, vol_4_1, vol_5_2, PrecisionConfig,
};

/// Errors returned by `qou-values`.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum QouValueError {
    /// Muon-ratio pin was requested without `--allow-on-hold-muon-comparison` (2026-11-28 owner ruling).
    MuonPinOnHold,
    /// Observable identifier or `:val[...]` key was not found in the registry.
    UnknownObservable(String),
    /// Invalid parametric argument (e.g. `t3_bond_count(...)` syntax).
    InvalidParameter(String),
    /// Upstream witness or I/O error.
    IoError(String),
}

impl fmt::Display for QouValueError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::MuonPinOnHold => write!(
                f,
                "muon pin is ON HOLD per the 2026-11-28 owner ruling (pending lepton-word rederivation); \
                 default evaluation is strictly proton-pinned. Pass `--allow-on-hold-muon-comparison` \
                 only for explicit cross-anchor diagnostics."
            ),
            Self::UnknownObservable(k) => write!(f, "unknown observable or `:val[...]` key: `{k}`"),
            Self::InvalidParameter(msg) => write!(f, "invalid parameter: {msg}"),
            Self::IoError(msg) => write!(f, "{msg}"),
        }
    }
}

impl std::error::Error for QouValueError {}

/// Anchor selection policy enforcing the 2026-11-28 proton-pin owner ruling.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum PinMode {
    /// Strict default: proton-ratio pin `q_0^{(p)}` only; muon-pin shift omitted/gated.
    #[default]
    ProtonDefault,
    /// Diagnostic opt-in (`--allow-on-hold-muon-comparison`): computes proton-pinned primary
    /// values and attaches `delta_mu_pin` diagnostic against the on-hold muon ratio.
    AllowOnHoldMuonComparison,
}

/// Authoritative CODATA-2022 and PDG-2024 calibration + validation constants (exact digit strings).
pub mod codata_pdg {
    // Three admissible calibration inputs (CAL-1 m_e, CAL-2 m_p/m_e <-> q_0, CAL-3 m_{pi+-})
    pub const M_E_MEV: &str = "0.51099895069";
    pub const M_E_SIGMA_MEV: &str = "0.00000000016";

    pub const MASS_RATIO_P_E: &str = "1836.152673426";
    pub const MASS_RATIO_P_E_SIGMA: &str = "0.000000032";

    pub const M_PI_PM_MEV: &str = "139.57039";
    pub const M_PI_PM_SIGMA_MEV: &str = "0.00018";

    // External comparison targets ONLY (never upstream model inputs)
    pub const MASS_RATIO_MU_E: &str = "206.7682827";
    pub const MASS_RATIO_MU_E_SIGMA: &str = "0.0000046";
    pub const M_MU_SIGMA_MEV: &str = "0.0000023";

    pub const M_P_EXP_MEV: &str = "938.27208943";
    pub const M_P_EXP_SIGMA_MEV: &str = "0.00000029";

    pub const M_N_EXP_MEV: &str = "939.56542194";
    pub const M_N_EXP_SIGMA_MEV: &str = "0.00000048";

    pub const DELTA_M_NP_EXP_MEV: &str = "1.29333251";
    pub const DELTA_M_NP_EXP_SIGMA_MEV: &str = "0.00000038";

    pub const M_TAU_OVER_M_E_CODATA22: &str = "3477.23";
    pub const M_TAU_OVER_M_E_CODATA22_SIGMA: &str = "0.23";
    pub const M_TAU_PDG24_MEV: &str = "1776.93";
    pub const M_TAU_PDG24_SIGMA_MEV: &str = "0.09";

    pub const M_K_PM_EXP_MEV: &str = "493.677";
    pub const M_K_PM_EXP_SIGMA_MEV: &str = "0.013";

    pub const ALPHA_EM_INV_CODATA22: &str = "137.035999177";
    pub const ALPHA_EM_INV_CODATA22_SIGMA: &str = "0.000000021";

    pub const RYDBERG_HC_EV_CODATA22: &str = "13.605693122990";
    pub const RYDBERG_HC_EV_CODATA22_SIGMA: &str = "0.000000000015";

    pub const RYDBERG_M_INV_CODATA22: &str = "10973731.568157";
    pub const RYDBERG_M_INV_CODATA22_SIGMA: &str = "0.000012";

    // Exact 2019 SI definitions for h/e and hc:
    // h = 6.62607015e-34 J*s = 662607015e-42 J*s, e = 1.602176634e-19 C = 1602176634e-28 C
    // => h / e = (662607015 / 1602176634) * 10^{-14} eV*s = 4.1356676969...e-15 eV*s
    pub const PLANCK_H_NUM: u128 = 662_607_015;
    pub const ELEM_E_DEN: u128 = 1_602_176_634;
    pub const SPEED_C_M_PER_S: u128 = 299_792_458;

    pub const FERMI_GF_GEV_INV2: &str = "0.000011663788";
    pub const FERMI_GF_SIGMA_GEV_INV2: &str = "0.000000000006";
    // Note: master_atlas_jacobian_80dps.py reads NIST CODATA-2022 `Fermi coupling constant` = 1.1663787e-5 +- 6e-12
    pub const FERMI_GF_NIST22_GEV_INV2: &str = "0.000011663787";
    pub const FERMI_GF_NIST22_SIGMA_GEV_INV2: &str = "0.000000000006";

    pub const PDG_MW_GEV: &str = "80.3692";
    pub const PDG_MW_SIGMA_GEV: &str = "0.0133";
    pub const PDG_MZ_GEV: &str = "91.1876";
    pub const PDG_MZ_SIGMA_GEV: &str = "0.0021";
    pub const PDG_MH_GEV: &str = "125.20";
    pub const PDG_MH_SIGMA_GEV: &str = "0.11";
    pub const PDG_GAMMA_Z_GEV: &str = "2.4955";
    pub const PDG_GAMMA_Z_SIGMA_GEV: &str = "0.0023";
    pub const PDG_SIN2_THETA_W_MZ: &str = "0.23122";
    pub const PDG_SIN2_THETA_W_MZ_SIGMA: &str = "0.00004";
    pub const PDG_TAU_N_S: &str = "878.4";
    pub const PDG_TAU_N_SIGMA_S: &str = "0.5";

    pub const B_HE4_AME20_MEV: &str = "28.2956624";
    pub const B_HE4_AME20_SIGMA_MEV: &str = "0.0000008";
}

/// Dimensionless Borromean factor `F_Bor(q) = |tr_M(\beta_Bor, q)| [3]_q! / q^3`.
pub fn f_bor_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let q_inv = Float::with_val(prec, &one / q);
    let h = Float::with_val(prec, q - &q_inv);
    let h2 = Float::with_val(prec, &h * &h);
    let h4 = Float::with_val(prec, &h2 * &h2);
    let h6 = Float::with_val(prec, &h4 * &h2);
    let num = f_i64(prec, 4) + &h2 - f_i64(prec, 3) * &h4 - &h6;
    let den = &h2 + f_i64(prec, 4);
    let tr_bor = (num / den).abs();
    let q2 = Float::with_val(prec, q * q);
    let q_inv2 = Float::with_val(prec, &q_inv * &q_inv);
    let qfact3 = (q2 + &one + q_inv2) * Float::with_val(prec, q + &q_inv);
    let q3 = q.clone().pow(3);
    (tr_bor * qfact3) / q3
}

/// Dimensionless Borromean proton-to-electron substrate identity
/// `\Phi_p(q) = 2 (Vol(4_1) / \hbar_q^2) F_Bor(q) - 12`, `\hbar_q = 1 - q^{-1}`.
pub fn proton_ratio_phi_at(q: &Float, vol41: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let hbar = &one - Float::with_val(prec, &one / q);
    let hbar_sq = Float::with_val(prec, &hbar * &hbar);
    let f_bor = f_bor_at(q);
    f_i64(prec, 2) * (Float::with_val(prec, vol41 / &hbar_sq) * f_bor) - f_i64(prec, 12)
}

/// Solve `\Phi_p(q) = R_p` for the canonical proton-pinned substrate parameter `q_0^{(p)}`
/// at `prec` MPFR bits using damped central-step Newton iteration.
pub fn solve_q0_proton(r_p: &Float, vol41: &Float, prec: u32) -> Float {
    let work = prec + 24;
    let rp_w = Float::with_val(work, r_p);
    let v_w = Float::with_val(work, vol41);
    let mut q = f_i64(work, 111) / f_i64(work, 100);
    let dq_rel = f_i64(work, 1) >> (work / 2);
    let tol = f_i64(work, 1) >> work.saturating_sub(6);

    for _ in 0..35 {
        let f_val = proton_ratio_phi_at(&q, &v_w) - &rp_w;
        let h_step = Float::with_val(work, &q * &dq_rel);
        let q_plus = Float::with_val(work, &q + &h_step);
        let q_minus = Float::with_val(work, &q - &h_step);
        let fp = (proton_ratio_phi_at(&q_plus, &v_w) - proton_ratio_phi_at(&q_minus, &v_w))
            / (f_i64(work, 2) * &h_step);
        let step = f_val / fp;
        q -= &step;
        if step.abs() < tol {
            break;
        }
    }
    Float::with_val(prec, q)
}

/// On-hold muon-ratio comparison pin `q_0^{(\mu)} = [1 - \sqrt{Vol(4_1)/(m_\mu/m_e)}]^{-1}`.
/// Gated behind `PinMode::AllowOnHoldMuonComparison` per the 2026-11-28 owner ruling.
pub fn solve_q0_muon_gated(
    pin_mode: PinMode,
    r_mu: &Float,
    vol41: &Float,
    prec: u32,
) -> Result<Float, QouValueError> {
    if pin_mode != PinMode::AllowOnHoldMuonComparison {
        return Err(QouValueError::MuonPinOnHold);
    }
    let work = prec + 16;
    let one = f_i64(work, 1);
    let hbar = (Float::with_val(work, vol41) / Float::with_val(work, r_mu)).sqrt();
    let q = &one / (&one - hbar);
    Ok(Float::with_val(prec, q))
}

/// Form-B 4-topology Schwinger cubic `1/\alpha = T(q) + \alpha H(q)(1 - h^2 \alpha)`
/// (`QOU.Archimedean.EmFermionLoopFourTopology`).
pub fn alpha_em_inv_form_b_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let pi_v = pi(prec);
    let h = q - Float::with_val(prec, &one / q);
    let h2 = Float::with_val(prec, &h * &h);
    let t_term = Float::with_val(prec, q * q_int(9, q)) * q_int(10, q)
        + f_i64(prec, 8) / (f_i64(prec, 12) * &pi_v);
    let h_term = q_int(2, q) / (f_i64(prec, 8) * &pi_v);
    let mut a_val = Float::with_val(prec, &one / &t_term);
    let tol = f_i64(prec, 1) >> prec.saturating_sub(6);
    for _ in 0..30 {
        let a2 = Float::with_val(prec, &a_val * &a_val);
        let a3 = Float::with_val(prec, &a2 * &a_val);
        let f_val = Float::with_val(prec, &h_term * &h2) * &a3
            - Float::with_val(prec, &h_term * &a2)
            - Float::with_val(prec, &t_term * &a_val)
            + &one;
        let fp_val = f_i64(prec, 3) * Float::with_val(prec, &h_term * &h2) * &a2
            - f_i64(prec, 2) * Float::with_val(prec, &h_term * &a_val)
            - &t_term;
        let step = f_val / fp_val;
        a_val -= &step;
        if step.abs() < tol {
            break;
        }
    }
    one / a_val
}

/// Conditional Form-C two-loop Bloch-`B_3(\mathbb{C})` trilogarithm cubic
/// (`QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger`).
pub fn alpha_em_inv_form_c_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let pi_v = pi(prec);
    let h = q - Float::with_val(prec, &one / q);
    let h2 = Float::with_val(prec, &h * &h);
    let t_term = Float::with_val(prec, q * q_int(9, q)) * q_int(10, q)
        + f_i64(prec, 8) / (f_i64(prec, 12) * &pi_v);
    let h_term = q_int(2, q) / (f_i64(prec, 8) * &pi_v);
    let q_inv2 = q.clone().pow(-2);
    let delta_b3 = crate::math::zeta_3(prec) - polylog3_real(&q_inv2, prec);
    let c2_bloch = Float::with_val(prec, &h_term * &delta_b3) / (f_i64(prec, 8) * &pi_v);
    let c3 = c2_bloch - Float::with_val(prec, &h_term * &h2);

    let mut a_val = Float::with_val(prec, &one / &t_term);
    let tol = f_i64(prec, 1) >> prec.saturating_sub(6);
    for _ in 0..30 {
        let a2 = Float::with_val(prec, &a_val * &a_val);
        let a3 = Float::with_val(prec, &a2 * &a_val);
        let f_val = Float::with_val(prec, &c3 * &a3)
            + Float::with_val(prec, &h_term * &a2)
            + Float::with_val(prec, &t_term * &a_val)
            - &one;
        let fp_val = f_i64(prec, 3) * Float::with_val(prec, &c3 * &a2)
            + f_i64(prec, 2) * Float::with_val(prec, &h_term * &a_val)
            + &t_term;
        let step = f_val / fp_val;
        a_val -= &step;
        if step.abs() < tol {
            break;
        }
    }
    one / a_val
}

/// `8 x 8` homological Seifert pairing Chern–Simons resummation on `H_1(\Sigma_4; \mathbb{Z})`.
pub fn alpha_em_inv_cs_seifert_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let pi_v = pi(prec);
    let bare = Float::with_val(prec, q * q_int(9, q)) * q_int(10, q);
    let inv_q = Float::with_val(prec, &one / q);
    let hbar_q = Float::with_val(prec, &one - &inv_q);
    let cs_sum = Float::with_val(prec, &pi_v * &pi_v)
        * (f_i64(prec, 240) / f_i64(prec, 216) + f_i64(prec, 192) / f_i64(prec, 180));
    let d_cs = cs_sum
        * (q_int(2, q) / f_i64(prec, 2))
        * Float::with_val(prec, &hbar_q * &hbar_q)
        / &bare;
    let d29 = (Float::with_val(prec, q - &one) + &inv_q)
        * (q.clone().pow(3) - &one + inv_q.clone().pow(3));
    let d35 = q.clone().pow(4) - q.clone().pow(3) + q - &one + &inv_q
        - inv_q.clone().pow(3)
        + inv_q.clone().pow(4);
    let kappa_seifert = q.clone().pow(8) / (d29 * d35);
    &bare * (&one + &d_cs / (&one - &d_cs * kappa_seifert))
}

/// Legacy Witten `2 x 2` Chern–Simons Gram resummation (`meson_em_sinh_closed_form.py`).
pub fn alpha_em_inv_cs_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let pi_v = pi(prec);
    let pi2 = Float::with_val(prec, &pi_v * &pi_v);
    let qi = Float::with_val(prec, &one / q);
    let n2 = q_int(2, q);
    let n3 = q_int(3, q);
    let n5 = q_int(5, q);
    let n9 = q_int(9, q);
    let n10 = q_int(10, q);
    let bare = Float::with_val(prec, q * &n9) * &n10;

    let cs_29 = Float::with_val(prec, &pi2 * f_i64(prec, 10)) / f_i64(prec, 9);
    let cs_35 = Float::with_val(prec, &pi2 * f_i64(prec, 16)) / f_i64(prec, 15);
    let hbar = Float::with_val(prec, &one - &qi);
    let c1 = Float::with_val(prec, &cs_29 + &cs_35)
        * Float::with_val(prec, &n2 / f_i64(prec, 2))
        * Float::with_val(prec, &hbar * &hbar)
        / &bare;

    let g_cl_11 = &cs_29 + Float::with_val(prec, &pi2 * f_i64(prec, 64)) / f_i64(prec, 324);
    let g_cl_22 = &cs_35 + Float::with_val(prec, &pi2 * f_i64(prec, 64)) / f_i64(prec, 225);
    let g_cl_12 = Float::with_val(prec, &pi2 * f_i64(prec, 289)) / f_i64(prec, 270);
    let det_cl = g_cl_11 * g_cl_22 - Float::with_val(prec, &g_cl_12 * &g_cl_12);

    let lk_q = (Float::with_val(prec, &n2 * &n5) - Float::with_val(prec, &n3 * &n9)).abs();
    let cs_q_29 = Float::with_val(prec, &pi2 * (Float::with_val(prec, &n2 * &n2) - &one))
        * (Float::with_val(prec, &n9 * &n9) - &one)
        / (f_i64(prec, 12) * Float::with_val(prec, &n2 * &n9));
    let cs_q_35 = Float::with_val(prec, &pi2 * (Float::with_val(prec, &n3 * &n3) - &one))
        * (Float::with_val(prec, &n5 * &n5) - &one)
        / (f_i64(prec, 12) * Float::with_val(prec, &n3 * &n5));
    let sl_q_29 = Float::with_val(prec, &n2 - &one) * Float::with_val(prec, &n9 - &one);
    let sl_q_35 = Float::with_val(prec, &n3 - &one) * Float::with_val(prec, &n5 - &one);
    let n2_n9 = Float::with_val(prec, &n2 * &n9);
    let n3_n5 = Float::with_val(prec, &n3 * &n5);
    let g_q_11 = cs_q_29
        + Float::with_val(prec, &pi2 * Float::with_val(prec, &sl_q_29 * &sl_q_29))
            / Float::with_val(prec, &n2_n9 * &n2_n9);
    let g_q_22 = cs_q_35
        + Float::with_val(prec, &pi2 * Float::with_val(prec, &sl_q_35 * &sl_q_35))
            / Float::with_val(prec, &n3_n5 * &n3_n5);
    let g_q_12 = Float::with_val(prec, &pi2 * Float::with_val(prec, &lk_q * &lk_q))
        / Float::with_val(prec, &n2_n9 * &n3_n5);
    let det_q = g_q_11 * g_q_22 - Float::with_val(prec, &g_q_12 * &g_q_12);

    let kappa_gram = det_cl / det_q;
    &bare * (&one + &c1 / (&one - &c1 * kappa_gram))
}

/// Conditional Bring–Schwinger electroweak crossing fixed point `N_v = v / m_p`
/// (`QOU.StandardModel.ElectroweakBringSchwingerBridge`).
pub fn n_v_ew_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let pi_v = pi(prec);
    let hbar_q = &one - Float::with_val(prec, &one / q);
    let q2 = q_int(2, q);
    let t_ew = Float::with_val(prec, q * q_int(4, q))
        * q_int(6, q)
        * q_int(8, q)
        * Float::with_val(prec, &q2 / f_i64(prec, 2))
        + Float::with_val(prec, &one / &pi_v);
    let h_hab = Float::with_val(prec, &q2 / (f_i64(prec, 8) * &pi_v));
    let c3 = Float::with_val(prec, &hbar_q * &hbar_q) * &h_hab;

    let mut a_val = Float::with_val(prec, &one / &t_ew);
    let tol = f_i64(prec, 1) >> prec.saturating_sub(6);
    for _ in 0..30 {
        let a2 = Float::with_val(prec, &a_val * &a_val);
        let a3 = Float::with_val(prec, &a2 * &a_val);
        let f_val = Float::with_val(prec, &c3 * &a3)
            - Float::with_val(prec, &h_hab * &a2)
            + Float::with_val(prec, &t_ew * &a_val)
            - &one;
        let fp_val = f_i64(prec, 3) * Float::with_val(prec, &c3 * &a2)
            - f_i64(prec, 2) * Float::with_val(prec, &h_hab * &a_val)
            + &t_ew;
        let step = f_val / fp_val;
        a_val -= &step;
        if step.abs() < tol {
            break;
        }
    }
    one / a_val
}

/// Meson mass ratio `m_{K^\pm} / m_{\pi^\pm} = \sqrt{[3]_q [4]_q + (\alpha_{\mathrm{EM,B}}(q)/\pi)(1 + \ln(1 + \hbar_q))}`.
pub fn mk_over_mpi_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let hbar_q = &one - Float::with_val(prec, &one / q);
    let strong_core = q_int(3, q) * q_int(4, q);
    let em_inv = alpha_em_inv_form_b_at(q);
    let one_plus_hb = Float::with_val(prec, &one + &hbar_q);
    let em_corr = (&one / em_inv) / pi(prec) * (&one + one_plus_hb.ln());
    (strong_core + em_corr).sqrt()
}

/// Koide quadratic resolvent `(+)` root for `m_\tau / m_e` welded to `(1, m_\mu^{\mathrm{QOU}}/m_e = Vol(4_1)/\hbar_q^2)`
/// (`S3CirculantKoideTraceIdentity`, `gap2b_mtau_s3_circulant_koide_probe.py`):
/// `\sqrt{m_\tau / m_e} = 2(1 + \sqrt{r_\mu}) + \sqrt{3(1 + 4\sqrt{r_\mu} + r_\mu)}`, where `r_\mu = Vol(4_1)/\hbar_q^2`.
pub fn m_tau_over_m_e_koide_at(q: &Float, vol41: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let hbar = &one - Float::with_val(prec, &one / q);
    let r_mu = Float::with_val(prec, vol41 / Float::with_val(prec, &hbar * &hbar));
    let s_mu = r_mu.clone().sqrt();
    let disc = f_i64(prec, 3) * (&one + f_i64(prec, 4) * &s_mu + &r_mu);
    let sqrt_rtau = f_i64(prec, 2) * (&one + s_mu) + disc.sqrt();
    Float::with_val(prec, &sqrt_rtau * &sqrt_rtau)
}

/// Order-zero hadronic scale `E_0^{(N=0)} = m_e / (q(q - 1))`.
pub fn e0_base_mev_at(m_e: &Float, q: &Float) -> Float {
    let prec = q.prec();
    let q_minus_1 = Float::with_val(prec, q - f_i64(prec, 1));
    Float::with_val(prec, m_e / Float::with_val(prec, q * &q_minus_1))
}

/// Canonical tower-summed hadronic scale `E_0^{\mathrm{full}} = m_e / (q(q - 1)(1 - \hbar_q^2))`
/// (`qbeta_e0.py::canonical`).
pub fn e0_tower_mev_at(m_e: &Float, q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let hbar = &one - Float::with_val(prec, &one / q);
    let denom_tower = &one - Float::with_val(prec, &hbar * &hbar);
    e0_base_mev_at(m_e, q) / denom_tower
}

/// Derived per-nat electron log-energy unit `m_e / (-\ln \tau_e)` (`\tau_e = q^3(q^4+1)/(q^2+1)^2`).
pub fn e0_electron_log_unit_mev_at(m_e: &Float, q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let q2 = Float::with_val(prec, q * q);
    let q4 = Float::with_val(prec, &q2 * &q2);
    let q2p1 = Float::with_val(prec, &q2 + &one);
    let tau_e: Float = (q.clone().pow(3) * Float::with_val(prec, &q4 + &one))
        / Float::with_val(prec, &q2p1 * &q2p1);
    Float::with_val(prec, m_e / (-tau_e.ln()))
}

/// Conditional pivotal `T^3` weight-trace base `Q_\beta^{\mathrm{base}}` on Borromean `V^3`.
pub fn q_beta_base_mev_at(m_e: &Float, q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let q2 = Float::with_val(prec, q * q);
    let q4 = Float::with_val(prec, &q2 * &q2);
    let q6 = Float::with_val(prec, &q4 * &q2);
    let q8 = Float::with_val(prec, &q4 * &q4);
    let q10 = Float::with_val(prec, &q8 * &q2);
    let q12 = Float::with_val(prec, &q6 * &q6);
    let poly = q12 - f_i64(prec, 3) * q10 + f_i64(prec, 3) * q8 - f_i64(prec, 5) * q6
        + f_i64(prec, 3) * &q4
        - f_i64(prec, 3) * &q2
        + &one;
    let q2p1 = Float::with_val(prec, &q2 + &one);
    let denom = Float::with_val(prec, &q4 * q2p1.pow(3));
    let eps_flavour = (Float::with_val(prec, &q2 - &one) * poly / denom).abs();
    eps_flavour * e0_tower_mev_at(m_e, q)
}

/// Exact `H_3(q)` 6x6 Frobenius Gram determinant `\det G_D(q)` at canonical Convention-D Markov
/// trace `z = q^3 / (q^2 + 1)` (`QOU.Nuclear.GramSignature` / `confinement-operator-selection` /
/// `gram-matrix-dual`). Under the `N = 2` Temperley–Lieb `TL_3` quotient, the antisymmetric `(1^3)`
/// sign representation spans a 1D radical, so `\det G_D(q) == 0` identically (`3.998e-17` in
/// legacy float64 witnesses was IEEE rounding noise).
pub fn h3_gram_det_at(q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let q2 = Float::with_val(prec, q * q);
    let z: Float = q.clone().pow(3) / Float::with_val(prec, &q2 + &one);
    let h = q - Float::with_val(prec, &one / q);

    // Normal form basis indices: 0: 1, 1: s0, 2: s1, 3: s0 s1, 4: s1 s0, 5: s0 s1 s0
    // Right-multiplication action of s0 and s1 on the 6 NF basis vectors:
    // b * s0:
    //   0 (1)       -> 1 (s0)
    //   1 (s0)      -> h*1(s0) + 0(1)
    //   2 (s1)      -> 4 (s1 s0)
    //   3 (s0 s1)   -> 5 (s0 s1 s0)
    //   4 (s1 s0)   -> h*4(s1 s0) + 2(s1)
    //   5 (s0 s1 s0)-> s0 s1 s0 s0 = h*(s0 s1 s0) + s0 s1 = h*5 + 3
    // b * s1:
    //   0 (1)       -> 2 (s1)
    //   1 (s0)      -> 3 (s0 s1)
    //   2 (s1)      -> h*2(s1) + 0(1)
    //   3 (s0 s1)   -> h*3(s0 s1) + 1(s0)
    //   4 (s1 s0)   -> s1 s0 s1 = s0 s1 s0 = 5
    //   5 (s0 s1 s0)-> s0 s1 s0 s1 = s0 (s0 s1 s0) = (h s0 + 1) s1 s0 = h*5 + 4
    let mul_gen = |vec: &[Float; 6], gen: usize| -> [Float; 6] {
        let z0 = || f_i64(prec, 0);
        let mut out = [z0(), z0(), z0(), z0(), z0(), z0()];
        if gen == 0 {
            out[1] += &vec[0];
            out[0] += &vec[1];
            out[1] += Float::with_val(prec, &h * &vec[1]);
            out[4] += &vec[2];
            out[5] += &vec[3];
            out[2] += &vec[4];
            out[4] += Float::with_val(prec, &h * &vec[4]);
            out[3] += &vec[5];
            out[5] += Float::with_val(prec, &h * &vec[5]);
        } else {
            out[2] += &vec[0];
            out[3] += &vec[1];
            out[0] += &vec[2];
            out[2] += Float::with_val(prec, &h * &vec[2]);
            out[1] += &vec[3];
            out[3] += Float::with_val(prec, &h * &vec[3]);
            out[5] += &vec[4];
            out[4] += &vec[5];
            out[5] += Float::with_val(prec, &h * &vec[5]);
        }
        out
    };

    let words: [&[usize]; 6] = [&[], &[0], &[1], &[0, 1], &[1, 0], &[0, 1, 0]];
    // Markov traces on the 6 basis elements:
    // tr(1) = 1, tr(s0) = z, tr(s1) = z, tr(s0 s1) = z^2, tr(s1 s0) = z^2, tr(s0 s1 s0) = h z^2 + z
    let z2 = Float::with_val(prec, &z * &z);
    let tr_basis = [
        one.clone(),
        z.clone(),
        z.clone(),
        z2.clone(),
        z2.clone(),
        Float::with_val(prec, &h * &z2) + &z,
    ];

    let mut mat: Vec<Vec<Float>> = vec![vec![f_i64(prec, 0); 6]; 6];
    for i in 0..6 {
        let mut ei = [
            f_i64(prec, 0),
            f_i64(prec, 0),
            f_i64(prec, 0),
            f_i64(prec, 0),
            f_i64(prec, 0),
            f_i64(prec, 0),
        ];
        ei[i] = one.clone();
        for j in 0..6 {
            let mut prod = ei.clone();
            for &g in words[j] {
                prod = mul_gen(&prod, g);
            }
            let mut tr = f_i64(prec, 0);
            for k in 0..6 {
                tr += Float::with_val(prec, &prod[k] * &tr_basis[k]);
            }
            mat[i][j] = tr;
        }
    }

    // Exact partial-pivoted Gaussian elimination in MPFR with algebraic rank-deficiency guard
    let rank_tol = f_i64(prec, 1) >> prec.saturating_sub(24);
    let mut det = one;
    let mut sign = 1i64;
    for col in 0..6 {
        let mut piv = col;
        let mut max_abs = mat[col][col].clone().abs();
        for r in (col + 1)..6 {
            let cand = mat[r][col].clone().abs();
            if cand > max_abs {
                max_abs = cand;
                piv = r;
            }
        }
        if max_abs <= rank_tol {
            return f_i64(prec, 0);
        }
        if piv != col {
            mat.swap(col, piv);
            sign = -sign;
        }
        let diag = mat[col][col].clone();
        det *= &diag;
        for r in (col + 1)..6 {
            let factor = Float::with_val(prec, &mat[r][col] / &diag);
            for c in col..6 {
                let sub = Float::with_val(prec, &factor * &mat[col][c]);
                mat[r][c] -= sub;
            }
        }
    }
    if sign < 0 { -det } else { det }
}

/// Self-consistent Sirlin 1-loop electroweak gauge boson outputs `(M_W, M_Z, \sin^2\theta_W(M_Z), \Gamma_Z)`
/// from `(m_e, q, m_\pi)` (`ElectroweakBosonThresholdsAndWeinberg.lean`, `L2a` baryon threshold).
pub struct ElectroweakBosonBundle {
    pub sin2_theta_w_onshell_planch: Float,
    pub sin2_theta_w_msbar_mz_k17: Float,
    pub m_w_l2a_gev: Float,
    pub m_z_l2a_gev: Float,
    pub m_h_borromean_gev: Float,
    pub gamma_z_gev: Float,
}

pub fn eval_electroweak_bosons(m_e_mev: &Float, q: &Float, _m_pi_mev: &Float, vol41: &Float) -> ElectroweakBosonBundle {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let two = f_i64(prec, 2);
    let pi_v = pi(prec);
    let hv = q - Float::with_val(prec, &one / q);
    let hb = &one - Float::with_val(prec, &one / q);
    let q2 = q_int(2, q);

    let me_gev = Float::with_val(prec, m_e_mev / f_i64(prec, 1000));
    let mp_gev = &me_gev * proton_ratio_phi_at(q, vol41);
    let mmu_gev = &me_gev * (vol41 / Float::with_val(prec, &hb * &hb));

    let alpha0 = &one / alpha_em_inv_form_c_at(q);
    let nv = n_v_ew_at(q);
    let v_ew = Float::with_val(prec, &nv * &mp_gev);

    let tp2 = trace_poly_two_p(2, &hv);
    let tp3 = trace_poly_two_p(3, &hv);
    let tp4 = trace_poly_two_p(4, &hv);
    let r_zw = (Float::with_val(prec, &tp3 * Float::with_val(prec, &q2 * &q2)))
        / (Float::with_val(prec, &tp2 * f_i64(prec, 4)));
    let c2_w = &one / Float::with_val(prec, &r_zw * &r_zw);
    let s2_w = Float::with_val(prec, &one - &c2_w);

    let a0_gev = (Float::with_val(prec, &pi_v * &alpha0)).sqrt() * &v_ew;
    let drho_yt1 = f_i64(prec, 3) / (f_i64(prec, 32) * Float::with_val(prec, &pi_v * &pi_v));
    let dr_weak_1l = (&alpha0 / (f_i64(prec, 4) * Float::with_val(prec, &pi_v * &s2_w)))
        * (((f_i64(prec, 7) - f_i64(prec, 4) * &s2_w) / &two) * c2_w.clone().ln()
            + f_i64(prec, 6));

    let dr_of_z = |z: &Float| -> Float {
        let re = Float::with_val(prec, z / &me_gev);
        let rmu = Float::with_val(prec, z / &mmu_gev);
        let rp = Float::with_val(prec, z / &mp_gev);
        let five_thirds = f_i64(prec, 5) / f_i64(prec, 3);
        let vp_e = Float::with_val(prec, &re * &re).ln() - &five_thirds;
        let vp_mu = Float::with_val(prec, &rmu * &rmu).ln() - &five_thirds;
        let vp_p = Float::with_val(prec, &rp * &rp).ln() - &five_thirds;
        (&alpha0 / (f_i64(prec, 3) * &pi_v))
            * (vp_e + vp_mu + (f_i64(prec, 14) / f_i64(prec, 3)) * vp_p)
            - Float::with_val(prec, &c2_w / &s2_w) * &drho_yt1
            + &dr_weak_1l
    };

    // Fixed-point iteration / Newton solve for z = M_Z
    let mut mz = f_i64(prec, 91);
    let dz = f_i64(prec, 1) >> (prec / 2);
    let tol = f_i64(prec, 1) >> prec.saturating_sub(6);
    let s2_sqrt = s2_w.clone().sqrt();
    let eval_f = |z: &Float| -> Float {
        let dr = dr_of_z(z);
        let denom = &s2_sqrt * Float::with_val(prec, &one - dr).sqrt();
        (Float::with_val(prec, &a0_gev / denom) * &r_zw) - z
    };
    for _ in 0..25 {
        let fv = eval_f(&mz);
        let zp = Float::with_val(prec, &mz + &dz);
        let zm = Float::with_val(prec, &mz - &dz);
        let fp = (eval_f(&zp) - eval_f(&zm)) / (f_i64(prec, 2) * &dz);
        let step = fv / fp;
        mz -= &step;
        if step.abs() < tol {
            break;
        }
    }
    let mw = Float::with_val(prec, &mz / &r_zw);

    // 1-loop GQW Sweedler k=17 MS-bar sin^2(theta_W)(M_Z)
    let d_inva_pert = (&two / (f_i64(prec, 3) * &pi_v))
        * (Float::with_val(prec, &mz / &me_gev).ln()
            + Float::with_val(prec, &mz / &mmu_gev).ln()
            + (f_i64(prec, 14) / f_i64(prec, 3)) * Float::with_val(prec, &mz / &mp_gev).ln());
    let inv_aem_mz = Float::with_val(prec, &one / &alpha0) - d_inva_pert;
    let u0 = Float::with_val(prec, q * q) - &one;
    let neg_ln_u0 = -(u0.ln());
    let s2_msbar_k17 = f_i64(prec, 3) / f_i64(prec, 8)
        - (f_i64(prec, 109) / f_i64(prec, 24))
            * (f_i64(prec, 17) * neg_ln_u0 / (f_i64(prec, 2) * &pi_v))
            / inv_aem_mz;

    let h_fac_base = Float::with_val(prec, &tp4 / &tp2)
        * (f_i64(prec, 6) / f_i64(prec, 5))
        * Float::with_val(prec, &q2 / &two);
    let c_borromean = &one - f_i64(prec, 2) * catalan(prec) * hv.pow(4);
    let mh_borr = Float::with_val(prec, &mw * &h_fac_base) * c_borromean;

    // Standard Model Z total decay width evaluated on QOU-derived (G_F(q), M_Z(q), sin^2 theta_W(M_Z)):
    // \Gamma_Z = \frac{G_F M_Z^3}{6 \sqrt{2} \pi} \sum_{f != t} N_c^f (v_f^2 + a_f^2),
    // where v_f = I_3^f - 2 Q_f s_W^2, a_f = I_3^f, summed over:
    //   3 neutrinos: I3 = +1/2, Q = 0, Nc = 1
    //   3 charged leptons: I3 = -1/2, Q = -1, Nc = 1
    //   2 up-type quarks (u, c): I3 = +1/2, Q = +2/3, Nc = 3 * (1 + alpha_s/pi -> pure EW tree = 3)
    //   3 down-type quarks (d, s, b): I3 = -1/2, Q = -1/3, Nc = 3
    let gf_qou = &one / (two.clone().sqrt() * Float::with_val(prec, &v_ew * &v_ew));
    let half = f_i64(prec, 1) / f_i64(prec, 2);
    let s2_eff = &s2_msbar_k17;
    // Neutrinos (3x): v = 1/2, a = 1/2 => v^2 + a^2 = 1/2
    let sum_nu = f_i64(prec, 3) * &half;
    // Charged leptons (3x): v = -1/2 + 2 s2, a = -1/2
    let v_l = f_i64(prec, 2) * s2_eff - &half;
    let sum_l = f_i64(prec, 3) * (Float::with_val(prec, &v_l * &v_l) + f_i64(prec, 1) / f_i64(prec, 4));
    // Up quarks u, c (2 families x 3 colours): v = 1/2 - (4/3) s2, a = 1/2
    let v_u = &half - (f_i64(prec, 4) / f_i64(prec, 3)) * s2_eff;
    let sum_u = f_i64(prec, 6) * (Float::with_val(prec, &v_u * &v_u) + f_i64(prec, 1) / f_i64(prec, 4));
    // Down quarks d, s, b (3 families x 3 colours): v = -1/2 + (2/3) s2, a = -1/2
    let v_d = (f_i64(prec, 2) / f_i64(prec, 3)) * s2_eff - &half;
    let sum_d = f_i64(prec, 9) * (Float::with_val(prec, &v_d * &v_d) + f_i64(prec, 1) / f_i64(prec, 4));
    // Include custodial 1 + \Delta\rho_{y_t=1} factor = 1 + 3/(32 \pi^2) from QOU's unit-Yukawa top loop
    let rho_cust = Float::with_val(prec, &one + &drho_yt1);
    let gamma_z = (gf_qou * mz.clone().pow(3))
        / (f_i64(prec, 6) * two.sqrt() * &pi_v)
        * rho_cust
        * (sum_nu + sum_l + sum_u + sum_d);

    ElectroweakBosonBundle {
        sin2_theta_w_onshell_planch: s2_w,
        sin2_theta_w_msbar_mz_k17: s2_msbar_k17,
        m_w_l2a_gev: mw,
        m_z_l2a_gev: mz,
        m_h_borromean_gev: mh_borr,
        gamma_z_gev: gamma_z,
    }
}

/// Two-term weak-vertex traces `(t_1(q), t_{2,\mathrm{lep}}(q), 2 t_2 / t_1)` on `T(3,5) = (\sigma_0\sigma_1)^5`
/// (`QOU.Nuclear.WeakVertexTwoTerm` / `weak_vertex_two_term_probe.py`).
pub fn weak_vertex_two_term_at(q: &Float) -> (Float, Float, Float) {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let q2 = Float::with_val(prec, q * q);
    let q2p1 = Float::with_val(prec, &q2 + &one);
    let t1 = (&q2 * (q.clone().pow(12) + q.clone().pow(8) - &one))
        / Float::with_val(prec, &q2p1 * &q2p1);
    let t2_lep = (-f_i64(prec, 2)
        * &q2
        * Float::with_val(prec, &q2 - &one)
        * (f_i64(prec, 2) * q.clone().pow(10) + &one))
        / (f_i64(prec, 9) * q2p1.pow(3));
    let two_t2_over_t1 = (f_i64(prec, 2) * &t2_lep) / &t1;
    (t1, t2_lep, two_t2_over_t1)
}

/// Free-neutron weak lifetime `\tau_n` (in seconds) evaluated with QOU-derived Fermi constant
/// `G_F(m_e, q_0)` and the `WeakVertexTwoTerm` lepton-first two-term trace factor `(1 + 2 t_2 / t_1)`
/// at the exact relativistic Sargent phase-space integral `f_0(w_0)`:
///
/// `f_0(w_0) = \frac{\sqrt{w_0^2 - 1}}{60}(2 w_0^4 - 9 w_0^2 - 8) + \frac{1}{4} w_0 \ln(w_0 + \sqrt{w_0^2 - 1})`,
/// `\Gamma_n = \frac{G_F(q_0)^2 m_e^5}{2 \pi^3} (1 + 3 g_A^{(0)2}) (1 + 2 t_2(q_0)/t_1(q_0)) f_0(w_0)`,
/// `\tau_n = \hbar / \Gamma_n`, using exact SI `\hbar = h / (2\pi)` and tree-level SU(4) spin-flavour
/// `g_A^{(0)} = 5/4 = 1.25` (zero empirical `V_{ud}` or `g_A` fitting; `w_0 = \Delta m_{np}^{\mathrm{exp}} / m_e`
/// kinematic phase-space window, since QOU's conditional `Q_\beta^{\mathrm{base}}` sits `-58.4%` low).
pub fn tau_n_two_term_s_at(m_e_mev: &Float, q: &Float, vol41: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let two = f_i64(prec, 2);
    let pi_v = pi(prec);

    let me_gev = Float::with_val(prec, m_e_mev / f_i64(prec, 1000));
    let mp_gev = &me_gev * proton_ratio_phi_at(q, vol41);
    let v_ew_gev = n_v_ew_at(q) * mp_gev;
    let gf_gev_inv2 = &one / (two.clone().sqrt() * Float::with_val(prec, &v_ew_gev * &v_ew_gev));
    // Convert G_F from GeV^{-2} to MeV^{-2}: 1 GeV^{-2} = 10^{-6} MeV^{-2}
    let gf_mev_inv2 = gf_gev_inv2 / f_i64(prec, 1_000_000);

    let dm_exp = f_str(prec, codata_pdg::DELTA_M_NP_EXP_MEV);
    let w0 = Float::with_val(prec, &dm_exp / m_e_mev);
    let w0_sq = Float::with_val(prec, &w0 * &w0);
    let p0 = Float::with_val(prec, &w0_sq - &one).sqrt();
    let f0 = (&p0 / f_i64(prec, 60))
        * (f_i64(prec, 2) * Float::with_val(prec, &w0_sq * &w0_sq)
            - f_i64(prec, 9) * &w0_sq
            - f_i64(prec, 8))
        + (&w0 / f_i64(prec, 4)) * Float::with_val(prec, &w0 + &p0).ln();

    // Non-relativistic quark-model / SU(4) Wigner-constituent axial ratio |g_A| = 5/4 (1 + 3*(25/16) = 91/16)
    // modulated by the QOU WeakVertexTwoTerm lepton-first factor (1 + 2*t2/t1)
    let (_, _, two_t2_over_t1) = weak_vertex_two_term_at(q);
    let matrix_elem_sq =
        (f_i64(prec, 91) / f_i64(prec, 16)) * Float::with_val(prec, &one + two_t2_over_t1);

    let gamma_mev = (Float::with_val(prec, &gf_mev_inv2 * &gf_mev_inv2) * m_e_mev.clone().pow(5))
        / (f_i64(prec, 2) * pi_v.clone().pow(3))
        * matrix_elem_sq
        * f0;

    // Exact 2019 SI \hbar in MeV * s:
    // h = 662607015e-42 J*s, e = 1602176634e-28 C => h / e = (662607015 / 1602176634) * 10^{-14} eV*s
    // = (662607015 / 1602176634) * 10^{-20} MeV*s; \hbar = (h / e) / (2 * \pi)
    let h_over_e_mev_s = (crate::math::f_u128(prec, codata_pdg::PLANCK_H_NUM)
        / crate::math::f_u128(prec, codata_pdg::ELEM_E_DEN))
        / f_i64(prec, 10).pow(20);
    let hbar_mev_s = h_over_e_mev_s / (f_i64(prec, 2) * pi_v);
    hbar_mev_s / gamma_mev
}

/// Monotone transfer-matrix `\ln |P_N(q)|` at canonical Markov weight `z = q^3/(q^2+1)`
/// (`master_atlas_jacobian_80dps.py::_tm_log_abs_skein`).
fn tm_log_abs_skein(z_p: usize, n_n: usize, q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let ha = q - Float::with_val(prec, &one / q);
    let ha_half = Float::with_val(prec, &ha / f_i64(prec, 2));
    let q2 = Float::with_val(prec, q * q);
    let z_m = q.clone().pow(3) / Float::with_val(prec, &q2 + &one);
    let a_tot = z_p + n_n;
    let mut acc = f_i64(prec, 0);

    for i in 0..a_tot.saturating_sub(1) {
        let mut m00 = one.clone();
        let mut m01 = f_i64(prec, 0);
        let mut m10 = f_i64(prec, 0);
        let mut m11 = one.clone();
        let i_is_p = i < z_p;
        for j in (i + 1)..a_tot {
            let j_is_p = j < z_p;
            let d_ij = if i_is_p && j_is_p {
                f_i64(prec, 0)
            } else if !i_is_p && !j_is_p {
                -ha.clone()
            } else {
                -ha_half.clone()
            };
            let t00 = Float::with_val(prec, &ha + &d_ij);
            let nm00 = Float::with_val(prec, &m00 * &t00) + &m01;
            let nm01 = &m00 + Float::with_val(prec, &m01 * &d_ij);
            let nm10 = Float::with_val(prec, &m10 * &t00) + &m11;
            let nm11 = &m10 + Float::with_val(prec, &m11 * &d_ij);
            m00 = nm00;
            m01 = nm01;
            m10 = nm10;
            m11 = nm11;
        }
        let v_i = Float::with_val(prec, &z_m * &m00) + &m10;
        if !v_i.is_zero() {
            acc += v_i.abs().ln();
        }
    }
    acc
}

/// Bare monotone transfer-matrix `\beta^-` Q-value `|\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})| \hbar_q m_e / 3`.
pub fn tm_qbare_mev_at(z_p: usize, n_n: usize, m_e: &Float, q: &Float) -> Float {
    let prec = q.prec();
    let one = f_i64(prec, 1);
    let par = tm_log_abs_skein(z_p, n_n, q);
    let dau = tm_log_abs_skein(z_p + 1, n_n - 1, q);
    let hbar_q = &one - Float::with_val(prec, &one / q);
    ((dau - par).abs() / q.clone().ln()) * hbar_q * m_e / f_i64(prec, 3)
}

/// Exact `C_{3v}`-symmetric `AX_3E_1` bond angle `\theta(NH_3)` in degrees (`master_atlas_jacobian_80dps.py`).
pub fn vsepr_nh3_deg_at(q: &Float) -> Float {
    let out_prec = q.prec();
    let prec = out_prec + 96;
    let qw = Float::with_val(prec, q);
    let one = f_i64(prec, 1);
    let two = f_i64(prec, 2);
    let three = f_i64(prec, 3);
    let sqrt3 = three.clone().sqrt();
    let q2 = Float::with_val(prec, &qw * &qw);
    let q4 = Float::with_val(prec, &q2 * &q2);

    let energy = |alpha: &Float| -> Float {
        let sin_a = alpha.clone().sin();
        let cos_a = alpha.clone().cos();
        Float::with_val(prec, &three * &q2) / Float::with_val(prec, &sqrt3 * sin_a)
            + Float::with_val(prec, &three * &q4)
                / Float::with_val(prec, &two * Float::with_val(prec, &one + cos_a)).sqrt()
    };

    let eps = f_i64(prec, 1) >> (prec / 3);
    let grad = |alpha: &Float| -> Float {
        let ap = Float::with_val(prec, alpha + &eps);
        let am = Float::with_val(prec, alpha - &eps);
        (energy(&ap) - energy(&am)) / (f_i64(prec, 2) * &eps)
    };

    let mut a = f_i64(prec, 12) / f_i64(prec, 10);
    let tol = f_i64(prec, 1) >> (prec * 2 / 3);
    for _ in 0..30 {
        let g = grad(&a);
        let ap = Float::with_val(prec, &a + &eps);
        let am = Float::with_val(prec, &a - &eps);
        let gp = (grad(&ap) - grad(&am)) / (f_i64(prec, 2) * &eps);
        let step = g / gp;
        a -= &step;
        if step.abs() < tol {
            break;
        }
    }
    let sin_a = a.sin();
    let cos_theta = &one - (&three * Float::with_val(prec, &sin_a * &sin_a)) / &two;
    Float::with_val(out_prec, cos_theta.acos() * f_i64(prec, 180) / pi(prec))
}

/// Exact `C_{2v}`-symmetric `AX_2E_2` bond angle `\theta(H_2O)` in degrees (`master_atlas_jacobian_80dps.py`).
pub fn vsepr_h2o_deg_at(q: &Float) -> Float {
    let out_prec = q.prec();
    let prec = out_prec + 96;
    let qw = Float::with_val(prec, q);
    let one = f_i64(prec, 1);
    let two = f_i64(prec, 2);
    let four = f_i64(prec, 4);
    let q2 = Float::with_val(prec, &qw * &qw);
    let q4 = Float::with_val(prec, &q2 * &q2);
    let q6 = Float::with_val(prec, &q4 * &q2);

    let energy = |beta: &Float, gamma: &Float| -> Float {
        let sb = beta.clone().sin();
        let sg = gamma.clone().sin();
        let cb = beta.clone().cos();
        let cg = gamma.clone().cos();
        Float::with_val(prec, &q2 / Float::with_val(prec, &two * sb))
            + Float::with_val(prec, &q6 / Float::with_val(prec, &two * sg))
            + Float::with_val(prec, &four * &q4)
                / Float::with_val(
                    prec,
                    &two * Float::with_val(prec, &one + Float::with_val(prec, cb * cg)),
                )
                .sqrt()
    };

    let eps = f_i64(prec, 1) >> (prec / 3);
    let grad = |b: &Float, g: &Float| -> (Float, Float) {
        let bp = Float::with_val(prec, b + &eps);
        let bm = Float::with_val(prec, b - &eps);
        let gp = Float::with_val(prec, g + &eps);
        let gm = Float::with_val(prec, g - &eps);
        let db = (energy(&bp, g) - energy(&bm, g)) / (f_i64(prec, 2) * &eps);
        let dg = (energy(b, &gp) - energy(b, &gm)) / (f_i64(prec, 2) * &eps);
        (db, dg)
    };

    let mut b = f_i64(prec, 91) / f_i64(prec, 100);
    let mut g = f_i64(prec, 102) / f_i64(prec, 100);
    let tol_sq = f_i64(prec, 1) >> (prec * 4 / 3);
    for _ in 0..35 {
        let (fb, fg) = grad(&b, &g);
        let bp = Float::with_val(prec, &b + &eps);
        let bm = Float::with_val(prec, &b - &eps);
        let gp = Float::with_val(prec, &g + &eps);
        let gm = Float::with_val(prec, &g - &eps);
        let (fb_bp, fg_bp) = grad(&bp, &g);
        let (fb_bm, fg_bm) = grad(&bm, &g);
        let (fb_gp, fg_gp) = grad(&b, &gp);
        let (fb_gm, fg_gm) = grad(&b, &gm);
        let j00 = (fb_bp - fb_bm) / (f_i64(prec, 2) * &eps);
        let j10 = (fg_bp - fg_bm) / (f_i64(prec, 2) * &eps);
        let j01 = (fb_gp - fb_gm) / (f_i64(prec, 2) * &eps);
        let j11 = (fg_gp - fg_gm) / (f_i64(prec, 2) * &eps);
        let det = Float::with_val(prec, &j00 * &j11) - Float::with_val(prec, &j01 * &j10);
        let sb = (Float::with_val(prec, &j11 * &fb) - Float::with_val(prec, &j01 * &fg)) / &det;
        let sg = (-Float::with_val(prec, &j10 * &fb) + Float::with_val(prec, &j00 * &fg)) / det;
        b -= &sb;
        g -= &sg;
        let n2 = Float::with_val(prec, &sb * &sb) + Float::with_val(prec, &sg * &sg);
        if n2 < tol_sq {
            break;
        }
    }
    Float::with_val(out_prec, f_i64(prec, 2) * b * f_i64(prec, 180) / pi(prec))
}

/// Exact `C_{2v}` planar `AX_3` bond angle `\theta(C_2H_4)` in degrees (`master_atlas_jacobian_80dps.py`).
pub fn vsepr_c2h4_deg_at(q: &Float) -> Float {
    let out_prec = q.prec();
    let prec = out_prec + 96;
    let qw = Float::with_val(prec, q);
    let two = f_i64(prec, 2);
    let q2 = Float::with_val(prec, &qw * &qw);
    let q3 = qw.pow(3);

    let energy = |phi: &Float| -> Float {
        let sp = phi.clone().sin();
        let cp2 = Float::with_val(prec, phi / &two).cos();
        Float::with_val(prec, &q2 / Float::with_val(prec, &two * sp))
            + Float::with_val(prec, &q3 / cp2)
    };

    let eps = f_i64(prec, 1) >> (prec / 3);
    let grad = |phi: &Float| -> Float {
        let pp = Float::with_val(prec, phi + &eps);
        let pm = Float::with_val(prec, phi - &eps);
        (energy(&pp) - energy(&pm)) / (f_i64(prec, 2) * &eps)
    };

    let mut phi = f_i64(prec, 102) / f_i64(prec, 100);
    let tol = f_i64(prec, 1) >> (prec * 2 / 3);
    for _ in 0..30 {
        let gv = grad(&phi);
        let pp = Float::with_val(prec, &phi + &eps);
        let pm = Float::with_val(prec, &phi - &eps);
        let gpv = (grad(&pp) - grad(&pm)) / (f_i64(prec, 2) * &eps);
        let step = gv / gpv;
        phi -= &step;
        if step.abs() < tol {
            break;
        }
    }
    Float::with_val(out_prec, f_i64(prec, 2) * phi * f_i64(prec, 180) / pi(prec))
}

/// Ruled `T_3` colour-valence pair-cap bond count `t3_bond_count(A) = min(A(A-1)/2, 3 * floor(A/2))`
/// (`QOU.MassTheory.NucleusBondValence`, PR `#9710` / `#9998`).
/// Equals `0` for `A <= 1`, `1` for `A = 2`, and `3 * (A / 2)` for `A >= 3`.
pub const fn t3_bond_count(a: u64) -> u64 {
    if a <= 1 {
        return 0;
    }
    let pairs = (a * (a - 1)) / 2;
    let t3_cap = 3 * (a / 2);
    if pairs < t3_cap { pairs } else { t3_cap }
}

/// Locate the QOU repository root (walking up from `QOU_REPO_ROOT`, `current_dir()`, or `CARGO_MANIFEST_DIR`).
pub fn locate_repo_root() -> Option<PathBuf> {
    if let Ok(env_root) = std::env::var("QOU_REPO_ROOT") {
        let p = PathBuf::from(env_root);
        if p.join("ACCURACY.md").is_file() {
            return Some(p);
        }
    }
    for start in [
        std::env::current_dir().ok(),
        Some(PathBuf::from(env!("CARGO_MANIFEST_DIR"))),
    ]
    .into_iter()
    .flatten()
    {
        let mut cur: &Path = &start;
        loop {
            if cur.join("ACCURACY.md").is_file() && cur.join("computations").is_dir() {
                return Some(cur.to_path_buf());
            }
            match cur.parent() {
                Some(parent) => cur = parent,
                None => break,
            }
        }
    }
    None
}

/// Load the dimensionless 462x462 Hoefsmit Lanczos ground-state eigenvalue `|E_ground_exact_dimless|`
/// for `^4He` (`M3a_kA_plaquette_pos`, `A=4`) from `gap1b-4he-tetrahedral-k4-flux-ring.witness.json`
/// without copying any witness float literal into Rust source.
pub fn load_he4_m3a_dimless_eigenvalue(prec: u32) -> Result<Float, QouValueError> {
    let root = locate_repo_root().ok_or_else(|| {
        QouValueError::IoError("could not locate QOU repo root for gap1b witness".to_string())
    })?;
    let path = root.join(
        "computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b-4he-tetrahedral-k4-flux-ring.witness.json",
    );
    let raw = std::fs::read_to_string(&path)
        .map_err(|e| QouValueError::IoError(format!("failed reading {}: {e}", path.display())))?;
    let val: serde_json::Value = serde_json::from_str(&raw)
        .map_err(|e| QouValueError::IoError(format!("invalid JSON in {}: {e}", path.display())))?;
    let eig_str = val
        .pointer("/data/part2a_fixed_radius_plaquette_summary/models/M3a_kA_plaquette_pos/per_A/A=4/E_ground_exact_dimless")
        .and_then(|v| v.as_str())
        .ok_or_else(|| {
            QouValueError::IoError("missing M3a A=4 E_ground_exact_dimless in gap1b witness".to_string())
        })?;
    Ok(f_str(prec, eig_str).abs())
}

/// Cached precomputed MPFR context so single-observable queries finish in `< 5 ms`
/// and full-registry evaluations (`all`, ~50 observables + Jacobians) finish in `< 20 ms`.
pub struct SubstrateContext {
    pub cfg: PrecisionConfig,
    pub pin_mode: PinMode,
    pub vol_4_1: Float,
    pub vol_5_2: Float,
    pub m_e_mev: Float,
    pub m_e_sigma_mev: Float,
    pub r_p: Float,
    pub r_p_sigma: Float,
    pub m_pi_pm_mev: Float,
    pub m_pi_pm_sigma_mev: Float,
    pub q0_proton: Float,
    pub dq0_drp: Float,
    pub q0_proton_sigma: Float,
    pub deriv_step_rel_agreement: Float,
    pub q0_muon_opt: Option<Float>,
    f_qhankel_cache: std::sync::OnceLock<Float>,
    he4_m3a_cache: std::sync::OnceLock<Option<Float>>,
}

impl SubstrateContext {
    /// Lazily evaluate and cache `f_qhankel(q_0^{(p)})` at `cfg.prec_bits`.
    pub fn f_qhankel_at_q0(&self) -> &Float {
        self.f_qhankel_cache
            .get_or_init(|| qhankel_coulomb_shape_factor(&self.q0_proton, self.cfg.prec_bits))
    }

    /// Lazily load and cache the dimensionless `^4He` `M3a` Lanczos eigenvalue from the `gap1b` witness.
    pub fn he4_m3a_dimless(&self) -> Option<&Float> {
        self.he4_m3a_cache
            .get_or_init(|| load_he4_m3a_dimless_eigenvalue(self.cfg.prec_bits).ok())
            .as_ref()
    }

    /// Build the proton-pinned MPFR substrate context at `cfg` precision.
    pub fn build(cfg: PrecisionConfig, pin_mode: PinMode) -> Result<Self, QouValueError> {
        let prec = cfg.prec_bits;
        let dprec = prec + 256;
        let v41_hi = vol_4_1(dprec);
        let v41 = Float::with_val(prec, &v41_hi);
        let v52 = vol_5_2(prec);
        let m_e = f_str(prec, codata_pdg::M_E_MEV);
        let sigma_me = f_str(prec, codata_pdg::M_E_SIGMA_MEV);
        let r_p_hi = f_str(dprec, codata_pdg::MASS_RATIO_P_E);
        let r_p = Float::with_val(prec, &r_p_hi);
        let sigma_rp = f_str(prec, codata_pdg::MASS_RATIO_P_E_SIGMA);
        let m_pi = f_str(prec, codata_pdg::M_PI_PM_MEV);
        let sigma_mpi = f_str(prec, codata_pdg::M_PI_PM_SIGMA_MEV);

        let q_p_hi = solve_q0_proton(&r_p_hi, &v41_hi, dprec);
        let q_p = Float::with_val(prec, &q_p_hi);

        // Implicit derivative dq_0^(p) / d(m_p/m_e) = 1 / Phi_p'(q_0^(p)) evaluated at dprec = prec + 256 bits
        // with eps1 = 1e-50 so O(eps1^2) = 1e-100 AND >135 digits survive subtraction (>100 true sig figs).
        let eps1 = f_str(dprec, "1e-50");
        let h1 = Float::with_val(dprec, &q_p_hi * &eps1);
        let dphi_1 = (proton_ratio_phi_at(&Float::with_val(dprec, &q_p_hi + &h1), &v41_hi)
            - proton_ratio_phi_at(&Float::with_val(dprec, &q_p_hi - &h1), &v41_hi))
            / (f_i64(dprec, 2) * &h1);

        let eps2 = f_str(dprec, "1e-44");
        let h2 = Float::with_val(dprec, &q_p_hi * &eps2);
        let dphi_2 = (proton_ratio_phi_at(&Float::with_val(dprec, &q_p_hi + &h2), &v41_hi)
            - proton_ratio_phi_at(&Float::with_val(dprec, &q_p_hi - &h2), &v41_hi))
            / (f_i64(dprec, 2) * &h2);

        let deriv_agree_hi =
            Float::with_val(dprec, &dphi_1 - &dphi_2).abs() / dphi_1.clone().abs();
        let deriv_agree = Float::with_val(prec, deriv_agree_hi);
        let dq0_drp = Float::with_val(prec, f_i64(dprec, 1) / dphi_1);
        let sigma_qp = Float::with_val(prec, dq0_drp.clone().abs() * &sigma_rp);

        let q0_muon_opt = if pin_mode == PinMode::AllowOnHoldMuonComparison {
            let r_mu = f_str(prec, codata_pdg::MASS_RATIO_MU_E);
            Some(solve_q0_muon_gated(pin_mode, &r_mu, &v41, prec)?)
        } else {
            None
        };

        Ok(Self {
            cfg,
            pin_mode,
            vol_4_1: v41,
            vol_5_2: v52,
            m_e_mev: m_e,
            m_e_sigma_mev: sigma_me,
            r_p,
            r_p_sigma: sigma_rp,
            m_pi_pm_mev: m_pi,
            m_pi_pm_sigma_mev: sigma_mpi,
            q0_proton: q_p,
            dq0_drp,
            q0_proton_sigma: sigma_qp,
            deriv_step_rel_agreement: deriv_agree,
            q0_muon_opt,
            f_qhankel_cache: std::sync::OnceLock::new(),
            he4_m3a_cache: std::sync::OnceLock::new(),
        })
    }
}
