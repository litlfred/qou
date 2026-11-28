//! Declarative observable registry, `:val[...]` key resolution, and 80-dps MPFR
//! Fréchet–Jacobian uncertainty propagation wrt `(m_e, \mathfrak{D}_\beta \leftrightarrow m_p/m_e, m_{\pi^\pm})`.

use rug::ops::Pow;
use rug::Float;
use serde::{Deserialize, Serialize};

use crate::math::{
    catalan, f_i64, f_str, f_u128, fmt_sig, pi, q_int, qhankel_coulomb_shape_factor,
};
use crate::solvers::{
    alpha_em_inv_cs_at, alpha_em_inv_cs_seifert_at, alpha_em_inv_form_b_at, alpha_em_inv_form_c_at,
    codata_pdg, e0_base_mev_at, e0_electron_log_unit_mev_at, e0_tower_mev_at,
    eval_electroweak_bosons, f_bor_at, h3_gram_det_at, m_tau_over_m_e_koide_at, mk_over_mpi_at,
    n_v_ew_at, proton_ratio_phi_at, q_beta_base_mev_at, t3_bond_count, tau_n_two_term_s_at,
    tm_qbare_mev_at, vsepr_c2h4_deg_at, vsepr_h2o_deg_at, vsepr_nh3_deg_at,
    weak_vertex_two_term_at, QouValueError, SubstrateContext,
};

/// Scorecard / monograph observable category.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Category {
    AetherKnot,
    MassHadron,
    ElectroweakAtomic,
    NuclearAlpha,
    MolecularGeometry,
}

impl Category {
    pub fn as_str(self) -> &'static str {
        match self {
            Self::AetherKnot => "aether_knot",
            Self::MassHadron => "mass_hadron",
            Self::ElectroweakAtomic => "electroweak_atomic",
            Self::NuclearAlpha => "nuclear_alpha",
            Self::MolecularGeometry => "molecular_geometry",
        }
    }

    pub fn matches_filter(self, filter: &str) -> bool {
        let norm = filter.trim().to_ascii_lowercase().replace('-', "_");
        self.as_str().contains(&norm)
    }
}

/// Epistemic status tier matching `ACCURACY.md` and `scorecard-epistemic-status.witness.json`.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum EpistemicTier {
    CalibrationPin,
    ProvedExact,
    Derived,
    Selected,
    Conditional,
    Exploratory,
}

/// External empirical benchmark reference (`CODATA 2022`, `PDG 2024`, `AME2020`, `NIST`).
#[derive(Debug, Clone, Copy)]
pub enum ExpRefSpec {
    /// Fixed decimal strings `(value_str, sigma_str, source_label)`.
    Fixed(&'static str, &'static str, &'static str),
    /// Computed dynamically from exact CODATA/PDG ratios at full MPFR precision.
    Dynamic(fn(u32) -> (Float, Float), &'static str),
}

/// Point evaluation inputs `(m_e, q_0, m_{\pi^\pm})` passed to every observable closure.
pub struct EvalPoint<'a> {
    pub m_e_mev: &'a Float,
    pub q: &'a Float,
    pub m_pi_mev: &'a Float,
    pub ctx: &'a SubstrateContext,
    pub is_perturbed: bool,
}

/// Declarative specification of a registered QOU observable or `:val[...]` constant.
pub struct ObservableSpec {
    pub id: &'static str,
    pub atlas_val_key: Option<&'static str>,
    pub aliases: &'static [&'static str],
    pub category: Category,
    pub epistemic_tier: EpistemicTier,
    pub unit: Option<&'static str>,
    pub is_calibration_pin: bool,
    pub formula: &'static str,
    pub description: &'static str,
    pub exp_ref: Option<ExpRefSpec>,
    pub eval_fn: fn(&EvalPoint<'_>) -> Float,
}

/// Lightweight metadata row returned by `qou-values list`.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ObservableListEntry {
    pub id: String,
    pub atlas_val_key: Option<String>,
    pub aliases: Vec<String>,
    pub category: Category,
    pub epistemic_tier: EpistemicTier,
    pub unit: Option<String>,
    pub formula: String,
    pub description: String,
}

/// Fréchet–Jacobian partial derivatives wrt `(m_e, q_0, m_{\pi^\pm})`.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct JacobianRecord {
    pub do_dm_e: String,
    pub do_dq0: String,
    pub do_dm_pi: String,
}

/// Evaluated observable payload with full Fréchet–Jacobian uncertainty propagation and
/// experimental comparison metrics.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EvaluatedObservable {
    pub id: String,
    pub atlas_val_key: Option<String>,
    pub category: Category,
    pub epistemic_tier: EpistemicTier,
    pub unit: Option<String>,
    pub q0_anchor: String,
    pub dps: usize,
    pub mpfr_bits: u32,
    pub is_calibration_pin: bool,
    pub formula: String,
    pub value: String,
    pub sigma_pred: String,
    pub jacobian: JacobianRecord,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub exp_value: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub exp_sigma: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub exp_source: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub residual: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub roundtrip_residual: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub rel_ppm: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub rel_ppb: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub rel_ppq: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub pull_exp_sigma: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub z_comb_sigma: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub delta_mu_pin_on_hold: Option<String>,
}

// ── Dynamic experimental target helpers (exact MPFR ratios, zero float64) ────────

fn exp_m_mu_mev(prec: u32) -> (Float, Float) {
    let me = f_str(prec, codata_pdg::M_E_MEV);
    let r_mu = f_str(prec, codata_pdg::MASS_RATIO_MU_E);
    (me * r_mu, f_str(prec, codata_pdg::M_MU_SIGMA_MEV))
}

fn exp_mk_over_mpi(prec: u32) -> (Float, Float) {
    let mk = f_str(prec, codata_pdg::M_K_PM_EXP_MEV);
    let smk = f_str(prec, codata_pdg::M_K_PM_EXP_SIGMA_MEV);
    let mpi = f_str(prec, codata_pdg::M_PI_PM_MEV);
    let smpi = f_str(prec, codata_pdg::M_PI_PM_SIGMA_MEV);
    let ratio = Float::with_val(prec, &mk / &mpi);
    let rel_sq: Float =
        Float::with_val(prec, &smk / &mk).pow(2) + Float::with_val(prec, &smpi / &mpi).pow(2);
    let sig = Float::with_val(prec, &ratio * rel_sq.sqrt());
    (ratio, sig)
}

fn exp_q_beta_mev(prec: u32) -> (Float, Float) {
    let mn = f_str(prec, codata_pdg::M_N_EXP_MEV);
    let mp = f_str(prec, codata_pdg::M_P_EXP_MEV);
    let me = f_str(prec, codata_pdg::M_E_MEV);
    let sdm = f_str(prec, codata_pdg::DELTA_M_NP_EXP_SIGMA_MEV);
    let sme = f_str(prec, codata_pdg::M_E_SIGMA_MEV);
    let val = mn - mp - me;
    let var_sig: Float = sdm.pow(2) + sme.pow(2);
    let sig = var_sig.sqrt();
    (val, sig)
}

fn exp_v_ew_gev(prec: u32) -> (Float, Float) {
    let one = f_i64(prec, 1);
    let two = f_i64(prec, 2);
    let gf = f_str(prec, codata_pdg::FERMI_GF_NIST22_GEV_INV2);
    let sgf = f_str(prec, codata_pdg::FERMI_GF_NIST22_SIGMA_GEV_INV2);
    let v = &one / (two.clone().sqrt() * &gf).sqrt();
    let sv = Float::with_val(prec, &v * &sgf) / (two * gf);
    (v, sv)
}

fn exp_nv_ew(prec: u32) -> (Float, Float) {
    let (v, sv) = exp_v_ew_gev(prec);
    let mp_gev = f_str(prec, codata_pdg::M_P_EXP_MEV) / f_i64(prec, 1000);
    let smp_gev = f_str(prec, codata_pdg::M_P_EXP_SIGMA_MEV) / f_i64(prec, 1000);
    let nv = Float::with_val(prec, &v / &mp_gev);
    let rel_sq: Float =
        Float::with_val(prec, &sv / &v).pow(2) + Float::with_val(prec, &smp_gev / &mp_gev).pow(2);
    let snv = &nv * rel_sq.sqrt();
    (nv, snv)
}

fn exp_onshell_sin2(prec: u32) -> (Float, Float) {
    let one = f_i64(prec, 1);
    let mw = f_str(prec, codata_pdg::PDG_MW_GEV);
    let smw = f_str(prec, codata_pdg::PDG_MW_SIGMA_GEV);
    let mz = f_str(prec, codata_pdg::PDG_MZ_GEV);
    let smz = f_str(prec, codata_pdg::PDG_MZ_SIGMA_GEV);
    let r = Float::with_val(prec, &mw / &mz);
    let s2 = &one - Float::with_val(prec, &r * &r);
    let rel_sq: Float =
        Float::with_val(prec, &smw / &mw).pow(2) + Float::with_val(prec, &smz / &mz).pow(2);
    let ds2 = f_i64(prec, 2) * Float::with_val(prec, &r * &r) * rel_sq.sqrt();
    (s2, ds2)
}

fn hc_ev_m(prec: u32) -> Float {
    // Exact 2019 SI: h = 662607015e-42 J*s, e = 1602176634e-28 C, c = 299792458 m/s
    // => (h / e) * c = (662607015 * 299792458) / (1602176634 * 10^14) eV * m
    let num = f_u128(prec, codata_pdg::PLANCK_H_NUM * codata_pdg::SPEED_C_M_PER_S);
    let den = f_u128(prec, codata_pdg::ELEM_E_DEN) * f_i64(prec, 10).pow(14);
    num / den
}

// ── Static declarative observable registry ──────────────────────────────────────

pub static OBSERVABLES: &[ObservableSpec] = &[
    // ============================================================================
    // 1. Aether & Knot Constants
    // ============================================================================
    ObservableSpec {
        id: "q0_proton",
        atlas_val_key: Some("q_0_proton"),
        aliases: &["q_0", "q0"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::CalibrationPin,
        unit: None,
        is_calibration_pin: false,
        formula: "root of 2*(Vol(4_1)/hbar_q^2)*F_Bor(q) - 12 = m_p/m_e",
        description: "Proton-pinned substrate deformation parameter q_0^(p) (active default).",
        exp_ref: None,
        eval_fn: |p| p.q.clone(),
    },
    ObservableSpec {
        id: "h_hecke",
        atlas_val_key: Some("H_A"),
        aliases: &["gram_h", "ha_proton"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "q_0 - q_0^{-1}",
        description: "Hecke algebra quadratic parameter h = q_0 - q_0^{-1}.",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            p.q - Float::with_val(prec, f_i64(prec, 1) / p.q)
        },
    },
    ObservableSpec {
        id: "hbar_q",
        atlas_val_key: Some("hbar_q"),
        aliases: &["hbar_q_reduced"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "1 - q_0^{-1}",
        description: "Categorical reduced Planck step hbar_q = 1 - q_0^{-1}.",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            let one = f_i64(prec, 1);
            &one - Float::with_val(prec, &one / p.q)
        },
    },
    ObservableSpec {
        id: "hbar_q0",
        atlas_val_key: None,
        aliases: &["ln_q0", "log_q0"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "ln(q_0)",
        description: "Logarithmic aether deformation step ln(q_0).",
        exp_ref: None,
        eval_fn: |p| p.q.clone().ln(),
    },
    ObservableSpec {
        id: "hbar_q_sq",
        atlas_val_key: Some("hbar_q_sq"),
        aliases: &["hbond_h_squared_hbar"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "(1 - q_0^{-1})^2",
        description: "Squared categorical Planck step hbar_q^2.",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            let one = f_i64(prec, 1);
            let hb = &one - Float::with_val(prec, &one / p.q);
            Float::with_val(prec, &hb * &hb)
        },
    },
    ObservableSpec {
        id: "two_q",
        atlas_val_key: Some("two_q"),
        aliases: &["qint_2"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "q_0 + q_0^{-1}",
        description: "Balanced quantum integer [2]_{q_0}.",
        exp_ref: None,
        eval_fn: |p| q_int(2, p.q),
    },
    ObservableSpec {
        id: "qint_3",
        atlas_val_key: Some("qint_3"),
        aliases: &[],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "q_0^2 + 1 + q_0^{-2}",
        description: "Balanced quantum integer [3]_{q_0}.",
        exp_ref: None,
        eval_fn: |p| q_int(3, p.q),
    },
    ObservableSpec {
        id: "qint_4",
        atlas_val_key: Some("qint_4"),
        aliases: &[],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "(q_0^4 - q_0^{-4}) / (q_0 - q_0^{-1})",
        description: "Balanced quantum integer [4]_{q_0}.",
        exp_ref: None,
        eval_fn: |p| q_int(4, p.q),
    },
    ObservableSpec {
        id: "z_markov_d",
        atlas_val_key: None,
        aliases: &["markov_z_proton"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "q_0^3 / (q_0^2 + 1)",
        description: "Canonical N=2 quantum-trace Markov parameter z = q_0^3 / (q_0^2 + 1).",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            let q2 = Float::with_val(prec, p.q * p.q);
            p.q.clone().pow(3) / Float::with_val(prec, q2 + f_i64(prec, 1))
        },
    },
    ObservableSpec {
        id: "vol_4_1",
        atlas_val_key: Some("Vol_4_1"),
        aliases: &["vol_4_1_decimal_50"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::ProvedExact,
        unit: None,
        is_calibration_pin: false,
        formula: "2 * Cl_2(pi / 3)",
        description: "Hyperbolic volume of the figure-eight knot complement 4_1.",
        exp_ref: None,
        eval_fn: |p| p.ctx.vol_4_1.clone(),
    },
    ObservableSpec {
        id: "vol_5_2",
        atlas_val_key: Some("vol_5_2"),
        aliases: &[],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::ProvedExact,
        unit: None,
        is_calibration_pin: false,
        formula: "3 * D(z_0), z_0^3 - z_0^2 + 1 = 0",
        description: "Hyperbolic volume of the 5_2 knot complement.",
        exp_ref: None,
        eval_fn: |p| p.ctx.vol_5_2.clone(),
    },
    ObservableSpec {
        id: "f_bor",
        atlas_val_key: None,
        aliases: &["F_Bor"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "|tr_M(beta_Bor)| * [3]_{q_0}! / q_0^3",
        description: "Dimensionless Borromean baryon factor F_Bor(q_0).",
        exp_ref: None,
        eval_fn: |p| f_bor_at(p.q),
    },
    ObservableSpec {
        id: "gram_G",
        atlas_val_key: None,
        aliases: &["catalan_G"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::ProvedExact,
        unit: None,
        is_calibration_pin: false,
        formula: "sum_{k>=0} (-1)^k / (2k + 1)^2",
        description: "Catalan's constant G (ideal octahedron / Whitehead hyperbolic volume unit).",
        exp_ref: None,
        eval_fn: |p| catalan(p.q.prec()),
    },
    ObservableSpec {
        id: "gram_det",
        atlas_val_key: Some("gram_det"),
        aliases: &["h3_gram_det"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "det_{6x6} tr_M(b_i b_j) in H_3(q_0)",
        description: "Determinant of the 6x6 H_3(q_0) Frobenius normal-form Gram matrix.",
        exp_ref: None,
        eval_fn: |p| h3_gram_det_at(p.q),
    },
    ObservableSpec {
        id: "e0_base",
        atlas_val_key: Some("E_0_N0_MeV"),
        aliases: &["e0_order_zero_MeV"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_e / (q_0 * (q_0 - 1))",
        description: "Order-zero hadronic energy scale E_0^(N=0).",
        exp_ref: None,
        eval_fn: |p| e0_base_mev_at(p.m_e_mev, p.q),
    },
    ObservableSpec {
        id: "e0_tower",
        atlas_val_key: Some("E_0_full_MeV"),
        aliases: &["e0_canonical_MeV"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_e / (q_0 * (q_0 - 1) * (1 - hbar_q^2))",
        description: "Canonical tower-summed hadronic energy scale E_0^full.",
        exp_ref: None,
        eval_fn: |p| e0_tower_mev_at(p.m_e_mev, p.q),
    },
    ObservableSpec {
        id: "e0_log_unit",
        atlas_val_key: None,
        aliases: &["electron_log_unit_MeV"],
        category: Category::AetherKnot,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_e / (-ln(tau_e(q_0)))",
        description: "Derived per-nat log-of-trace energy unit from ElectronCategoricalEnergy.",
        exp_ref: None,
        eval_fn: |p| e0_electron_log_unit_mev_at(p.m_e_mev, p.q),
    },

    // ============================================================================
    // 2. Mass & Hadron Scorecard / :val[atlas_*] Keys
    // ============================================================================
    ObservableSpec {
        id: "m_e_MeV",
        atlas_val_key: Some("atlas_m_e_MeV"),
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::CalibrationPin,
        unit: Some("MeV"),
        is_calibration_pin: true,
        formula: "m_e (calibration input 1)",
        description: "Electron rest-mass energy (overall MeV unit pin).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_E_MEV,
            codata_pdg::M_E_SIGMA_MEV,
            "CODATA 2022",
        )),
        eval_fn: |p| p.m_e_mev.clone(),
    },
    ObservableSpec {
        id: "m_p_MeV",
        atlas_val_key: Some("atlas_m_p_MeV"),
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::CalibrationPin,
        unit: Some("MeV"),
        is_calibration_pin: true,
        formula: "m_e * [2*(Vol(4_1)/hbar_q^2)*F_Bor(q_0) - 12]",
        description: "Proton rest-mass energy round-trip check at proton pin q_0^(p).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_P_EXP_MEV,
            codata_pdg::M_P_EXP_SIGMA_MEV,
            "CODATA 2022",
        )),
        eval_fn: |p| Float::with_val(p.q.prec(), p.m_e_mev * proton_ratio_phi_at(p.q, &p.ctx.vol_4_1)),
    },
    ObservableSpec {
        id: "m_mu_MeV",
        atlas_val_key: Some("atlas_m_mu_MeV"),
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_e * Vol(4_1) / hbar_q^2",
        description: "Proton-anchored muon mass prediction (+211.21 ppb mu-p tension).",
        exp_ref: Some(ExpRefSpec::Dynamic(exp_m_mu_mev, "CODATA 2022")),
        eval_fn: |p| {
            let prec = p.q.prec();
            let one = f_i64(prec, 1);
            let hb = &one - Float::with_val(prec, &one / p.q);
            Float::with_val(prec, p.m_e_mev * &p.ctx.vol_4_1) / Float::with_val(prec, &hb * &hb)
        },
    },
    ObservableSpec {
        id: "m_tau_over_m_e",
        atlas_val_key: None,
        aliases: &["mtau_over_me"],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "[2(1 + sqrt(r_mu)) + sqrt(3(1 + 4 sqrt(r_mu) + r_mu))]^2, r_mu = Vol(4_1)/hbar_q^2",
        description: "Conditional Koide (+) quadratic resolvent tau-to-electron mass ratio.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_TAU_OVER_M_E_CODATA22,
            codata_pdg::M_TAU_OVER_M_E_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| m_tau_over_m_e_koide_at(p.q, &p.ctx.vol_4_1),
    },
    ObservableSpec {
        id: "m_tau_MeV",
        atlas_val_key: None,
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_e * (m_tau / m_e)_Koide",
        description: "Conditional Koide (+) quadratic resolvent tau lepton mass.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_TAU_PDG24_MEV,
            codata_pdg::M_TAU_PDG24_SIGMA_MEV,
            "PDG 2024",
        )),
        eval_fn: |p| Float::with_val(p.q.prec(), p.m_e_mev * m_tau_over_m_e_koide_at(p.q, &p.ctx.vol_4_1)),
    },
    ObservableSpec {
        id: "m_pi_pm_MeV",
        atlas_val_key: Some("atlas_m_pi_pm_MeV"),
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::CalibrationPin,
        unit: Some("MeV"),
        is_calibration_pin: true,
        formula: "m_{pi^+-} (calibration input 3)",
        description: "Charged pion rest-mass energy (meson-sector scale pin).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_PI_PM_MEV,
            codata_pdg::M_PI_PM_SIGMA_MEV,
            "PDG 2024",
        )),
        eval_fn: |p| p.m_pi_mev.clone(),
    },
    ObservableSpec {
        id: "m_k_over_m_pi",
        atlas_val_key: Some("atlas_mk_over_mpi"),
        aliases: &["mk_over_mpi"],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Selected,
        unit: None,
        is_calibration_pin: false,
        formula: "sqrt([3]_q*[4]_q + (alpha_EM,B(q)/pi)*(1 + ln(1 + hbar_q)))",
        description: "Charged kaon-to-pion mass ratio (+51.43 ppb, < 0.002 sigma_exp).",
        exp_ref: Some(ExpRefSpec::Dynamic(exp_mk_over_mpi, "PDG 2024")),
        eval_fn: |p| mk_over_mpi_at(p.q),
    },
    ObservableSpec {
        id: "m_k_pm_MeV",
        atlas_val_key: Some("atlas_m_k_pm_MeV"),
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Selected,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_{pi^+-} * (m_K / m_pi)",
        description: "Charged kaon mass rendered against m_{pi^+-} at proton q_0.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_K_PM_EXP_MEV,
            codata_pdg::M_K_PM_EXP_SIGMA_MEV,
            "PDG 2024",
        )),
        eval_fn: |p| Float::with_val(p.q.prec(), p.m_pi_mev * mk_over_mpi_at(p.q)),
    },
    ObservableSpec {
        id: "q_beta_base_MeV",
        atlas_val_key: Some("atlas_q_beta_base_MeV"),
        aliases: &["Q_beta"],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "|eps_n - eps_p| * E_0^full on V^3",
        description: "Conditional T^3 weight-trace free-neutron Q_beta^- base (conjectures C1-C3).",
        exp_ref: Some(ExpRefSpec::Dynamic(exp_q_beta_mev, "CODATA 2022")),
        eval_fn: |p| q_beta_base_mev_at(p.m_e_mev, p.q),
    },
    ObservableSpec {
        id: "delta_m_np_MeV",
        atlas_val_key: Some("atlas_delta_m_np_MeV"),
        aliases: &["Delta_pn"],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_e + Q_beta^base",
        description: "Conditional neutron-proton mass difference m_n - m_p.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::DELTA_M_NP_EXP_MEV,
            codata_pdg::DELTA_M_NP_EXP_SIGMA_MEV,
            "CODATA 2022",
        )),
        eval_fn: |p| Float::with_val(p.q.prec(), p.m_e_mev + q_beta_base_mev_at(p.m_e_mev, p.q)),
    },
    ObservableSpec {
        id: "m_n_MeV",
        atlas_val_key: Some("atlas_m_n_MeV"),
        aliases: &[],
        category: Category::MassHadron,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "m_p(q_0) + m_e + Q_beta^base",
        description: "Conditional free-neutron mass prediction.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::M_N_EXP_MEV,
            codata_pdg::M_N_EXP_SIGMA_MEV,
            "CODATA 2022",
        )),
        eval_fn: |p| {
            let prec = p.q.prec();
            let mp = Float::with_val(prec, p.m_e_mev * proton_ratio_phi_at(p.q, &p.ctx.vol_4_1));
            mp + p.m_e_mev + q_beta_base_mev_at(p.m_e_mev, p.q)
        },
    },

    // ============================================================================
    // 3. Electroweak & Atomic Constants (ACCURACY.md Vectors 2 & 4 / :val[atlas_*])
    // ============================================================================
    ObservableSpec {
        id: "alpha_em_inv_form_b",
        atlas_val_key: Some("atlas_alpha_em_inv_form_b"),
        aliases: &["alpha_em_inv", "inv_alpha_form_b"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "1/alpha = q_0[9][10] + 2/(3*pi) + alpha*H*(1 - h^2*alpha)",
        description: "4-topology Schwinger Form-B cubic inverse fine-structure constant (-0.365 ppb).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::ALPHA_EM_INV_CODATA22,
            codata_pdg::ALPHA_EM_INV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| alpha_em_inv_form_b_at(p.q),
    },
    ObservableSpec {
        id: "alpha_em_inv_form_c",
        atlas_val_key: None,
        aliases: &["alpha_em_inv_form_c_bloch_b3"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "Form B + c2_bloch*alpha^2, c2_bloch = H*(zeta(3) - Li_3(q_0^{-2}))/(8*pi)",
        description: "Conditional 2-loop Bloch-B_3(C) inverse fine-structure constant (-0.024 ppb, -0.16 sigma).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::ALPHA_EM_INV_CODATA22,
            codata_pdg::ALPHA_EM_INV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| alpha_em_inv_form_c_at(p.q),
    },
    ObservableSpec {
        id: "alpha_em_inv_cs_seifert",
        atlas_val_key: None,
        aliases: &[],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "q_0[9][10] * (1 + d_CS / (1 - d_CS * kappa_Seifert))",
        description: "8x8 homological Seifert pairing CS inverse fine-structure constant (-24.53 ppb).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::ALPHA_EM_INV_CODATA22,
            codata_pdg::ALPHA_EM_INV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| alpha_em_inv_cs_seifert_at(p.q),
    },
    ObservableSpec {
        id: "alpha_em_inv_cs",
        atlas_val_key: Some("atlas_alpha_em_inv_cs"),
        aliases: &[],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Exploratory,
        unit: None,
        is_calibration_pin: false,
        formula: "q_0[9][10] * (1 + c_1 / (1 - c_1 * kappa_Gram))",
        description: "Legacy 2x2 Witten Chern-Simons Gram-resummed alpha_EM^{-1} (-467.64 ppb).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::ALPHA_EM_INV_CODATA22,
            codata_pdg::ALPHA_EM_INV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| alpha_em_inv_cs_at(p.q),
    },
    ObservableSpec {
        id: "rydberg_hc_eV",
        atlas_val_key: None,
        aliases: &["rydberg_form_b_eV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("eV"),
        is_calibration_pin: false,
        formula: "0.5 * m_e * alpha_EM,B(q_0)^2",
        description: "Hydrogenic Rydberg energy R_inf * h * c with Form-B alpha_EM (+0.725 ppb).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::RYDBERG_HC_EV_CODATA22,
            codata_pdg::RYDBERG_HC_EV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| {
            let prec = p.q.prec();
            let a_inv = alpha_em_inv_form_b_at(p.q);
            (Float::with_val(prec, p.m_e_mev * f_i64(prec, 1_000_000)) / f_i64(prec, 2))
                / Float::with_val(prec, &a_inv * &a_inv)
        },
    },
    ObservableSpec {
        id: "rydberg_hc_form_c_eV",
        atlas_val_key: None,
        aliases: &["rydberg_form_c_eV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("eV"),
        is_calibration_pin: false,
        formula: "0.5 * m_e * alpha_EM,C(q_0)^2",
        description: "Hydrogenic Rydberg energy R_inf * h * c with 2-loop Form-C alpha_EM (+0.043 ppb).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::RYDBERG_HC_EV_CODATA22,
            codata_pdg::RYDBERG_HC_EV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| {
            let prec = p.q.prec();
            let a_inv = alpha_em_inv_form_c_at(p.q);
            (Float::with_val(prec, p.m_e_mev * f_i64(prec, 1_000_000)) / f_i64(prec, 2))
                / Float::with_val(prec, &a_inv * &a_inv)
        },
    },
    ObservableSpec {
        id: "rydberg_m_inv",
        atlas_val_key: None,
        aliases: &["R_inf_m_inv"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("m^-1"),
        is_calibration_pin: false,
        formula: "(0.5 * m_e * alpha_EM,B(q_0)^2) / (h * c)",
        description: "Rydberg wavenumber R_inf in m^-1 using Form-B alpha_EM and exact SI h*c.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::RYDBERG_M_INV_CODATA22,
            codata_pdg::RYDBERG_M_INV_CODATA22_SIGMA,
            "CODATA 2022",
        )),
        eval_fn: |p| {
            let prec = p.q.prec();
            let a_inv = alpha_em_inv_form_b_at(p.q);
            let ry_ev = (Float::with_val(prec, p.m_e_mev * f_i64(prec, 1_000_000))
                / f_i64(prec, 2))
                / Float::with_val(prec, &a_inv * &a_inv);
            ry_ev / hc_ev_m(prec)
        },
    },
    ObservableSpec {
        id: "N_v_ew",
        atlas_val_key: None,
        aliases: &["n_v_ew"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "1/alpha_v = q_0([2]/2)[4][6][8] + 1/pi - alpha_v*H*(1 - hbar_q^2*alpha_v)",
        description: "Bring-Schwinger electroweak crossing fixed point N_v = v / m_p (-29.37 ppb).",
        exp_ref: Some(ExpRefSpec::Dynamic(exp_nv_ew, "CODATA 2022")),
        eval_fn: |p| n_v_ew_at(p.q),
    },
    ObservableSpec {
        id: "v_weak_GeV",
        atlas_val_key: None,
        aliases: &["v_ew_GeV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("GeV"),
        is_calibration_pin: false,
        formula: "(m_p(q_0) / 1000) * N_v(q_0)",
        description: "Electroweak Higgs VEV v_weak from Bring-Schwinger fixed point (-29.37 ppb, -0.11 sigma).",
        exp_ref: Some(ExpRefSpec::Dynamic(exp_v_ew_gev, "CODATA 2022 / PDG 2024")),
        eval_fn: |p| {
            let prec = p.q.prec();
            let mp_gev = (Float::with_val(prec, p.m_e_mev * proton_ratio_phi_at(p.q, &p.ctx.vol_4_1)))
                / f_i64(prec, 1000);
            mp_gev * n_v_ew_at(p.q)
        },
    },
    ObservableSpec {
        id: "sin2_theta_w_mz",
        atlas_val_key: None,
        aliases: &["sin2_thetaW_msbar_mz"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "3/8 - (109/24)*(17 * (-ln(q_0^2 - 1)) / (2*pi)) * alpha_EM(M_Z)",
        description: "1-loop Georgi-Quinn-Weinberg MS-bar sin^2(theta_W)(M_Z) at Sweedler k = 17.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::PDG_SIN2_THETA_W_MZ,
            codata_pdg::PDG_SIN2_THETA_W_MZ_SIGMA,
            "PDG 2024",
        )),
        eval_fn: |p| {
            eval_electroweak_bosons(p.m_e_mev, p.q, p.m_pi_mev, &p.ctx.vol_4_1)
                .sin2_theta_w_msbar_mz_k17
        },
    },
    ObservableSpec {
        id: "sin2_theta_w_onshell",
        atlas_val_key: None,
        aliases: &["sin2_thetaW_planch"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: None,
        is_calibration_pin: false,
        formula: "1 - [P_2(h) / (P_3(h) * ([2]_q / 2)^2)]^2",
        description: "On-shell torus-link Plancherel dressed sin^2(theta_W) = 1 - M_W^2 / M_Z^2.",
        exp_ref: Some(ExpRefSpec::Dynamic(exp_onshell_sin2, "PDG 2024")),
        eval_fn: |p| {
            eval_electroweak_bosons(p.m_e_mev, p.q, p.m_pi_mev, &p.ctx.vol_4_1)
                .sin2_theta_w_onshell_planch
        },
    },
    ObservableSpec {
        id: "m_w_GeV",
        atlas_val_key: None,
        aliases: &["MW_L2a_GeV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("GeV"),
        is_calibration_pin: false,
        formula: "M_Z(q_0) / [(P_3(h)/P_2(h))*([2]_q/2)^2] (Sirlin 1-loop L2a)",
        description: "Self-consistent 1-loop Sirlin W-boson mass (baryon threshold m_p(q_0), y_t = 1).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::PDG_MW_GEV,
            codata_pdg::PDG_MW_SIGMA_GEV,
            "PDG 2024",
        )),
        eval_fn: |p| {
            eval_electroweak_bosons(p.m_e_mev, p.q, p.m_pi_mev, &p.ctx.vol_4_1).m_w_l2a_gev
        },
    },
    ObservableSpec {
        id: "m_z_GeV",
        atlas_val_key: None,
        aliases: &["MZ_L2a_GeV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("GeV"),
        is_calibration_pin: false,
        formula: "fixed point z = sqrt(pi*alpha_EM)*v_weak*r_ZW / (sin(theta_W)*sqrt(1 - Delta r(z)))",
        description: "Self-consistent 1-loop Sirlin Z-boson mass (baryon threshold m_p(q_0), y_t = 1).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::PDG_MZ_GEV,
            codata_pdg::PDG_MZ_SIGMA_GEV,
            "PDG 2024",
        )),
        eval_fn: |p| {
            eval_electroweak_bosons(p.m_e_mev, p.q, p.m_pi_mev, &p.ctx.vol_4_1).m_z_l2a_gev
        },
    },
    ObservableSpec {
        id: "m_h_GeV",
        atlas_val_key: None,
        aliases: &["mH_L2a_borromean_GeV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("GeV"),
        is_calibration_pin: false,
        formula: "M_W * (P_4/P_2) * (6/5) * ([2]_q/2) * (1 - 2*G*h^4)",
        description: "W/Z-reconciled T(2,8) Higgs boson mass (Borromean 2*G*h^4 loop factor).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::PDG_MH_GEV,
            codata_pdg::PDG_MH_SIGMA_GEV,
            "PDG 2024",
        )),
        eval_fn: |p| {
            eval_electroweak_bosons(p.m_e_mev, p.q, p.m_pi_mev, &p.ctx.vol_4_1).m_h_borromean_gev
        },
    },
    ObservableSpec {
        id: "gamma_z_GeV",
        atlas_val_key: None,
        aliases: &["Gamma_Z_GeV"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("GeV"),
        is_calibration_pin: false,
        formula: "(G_F(q_0)*M_Z(q_0)^3 / (6*sqrt(2)*pi)) * (1 + Delta rho) * sum_{f!=t} N_c^f (v_f^2 + a_f^2)",
        description: "Total Z decay width evaluated from QOU-derived (G_F(q_0), M_Z(q_0), sin^2 theta_W(M_Z)).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::PDG_GAMMA_Z_GEV,
            codata_pdg::PDG_GAMMA_Z_SIGMA_GEV,
            "PDG 2024",
        )),
        eval_fn: |p| {
            eval_electroweak_bosons(p.m_e_mev, p.q, p.m_pi_mev, &p.ctx.vol_4_1).gamma_z_gev
        },
    },
    ObservableSpec {
        id: "tau_n_s",
        atlas_val_key: None,
        aliases: &["neutron_lifetime_s"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("s"),
        is_calibration_pin: false,
        formula: "hbar / [ (G_F(q_0)^2 m_e^5 / (2*pi^3)) * (91/16) * (1 + 2*t_2/t_1) * f_0(w_0) ]",
        description: "Two-term weak-vertex free-neutron lifetime (QOU G_F(q_0) + WeakVertexTwoTerm 2*t_2/t_1).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::PDG_TAU_N_S,
            codata_pdg::PDG_TAU_N_SIGMA_S,
            "PDG 2024",
        )),
        eval_fn: |p| tau_n_two_term_s_at(p.m_e_mev, p.q, &p.ctx.vol_4_1),
    },
    ObservableSpec {
        id: "weak_vertex_2t2_over_t1",
        atlas_val_key: None,
        aliases: &["two_t2_over_t1_lepton_first"],
        category: Category::ElectroweakAtomic,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "-4*(q_0^2 - 1)*(2*q_0^{10} + 1) / (9*(q_0^2 + 1)*(q_0^{12} + q_0^8 - 1))",
        description: "Covariant two-term weak-vertex fractional trace shift 2*t_2/t_1 on T(3,5) (lepton-first).",
        exp_ref: None,
        eval_fn: |p| weak_vertex_two_term_at(p.q).2,
    },

    // ============================================================================
    // 4. Nuclear & alpha-Decay Constants + Transfer-Matrix Beta Benchmarks
    // ============================================================================
    ObservableSpec {
        id: "f_coulomb_ball",
        atlas_val_key: None,
        aliases: &["coulomb_shape_uniform_ball"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::ProvedExact,
        unit: None,
        is_calibration_pin: false,
        formula: "(3/5) * sqrt(3/5)",
        description: "Classical uniform-ball Coulomb shape factor f = (3/5)*sqrt(3/5) in E_C = f*Q^2/r_rms.",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            let tf = f_i64(prec, 3) / f_i64(prec, 5);
            &tf * tf.clone().sqrt()
        },
    },
    ObservableSpec {
        id: "f_coulomb_qhankel",
        atlas_val_key: None,
        aliases: &["coulomb_shape_qhankel"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "E_shell * r_rms on p^Z for Hahn-Exton J_{1/2}(p^k; p^2), p = 1/q_0",
        description: "Derived s-shell (A <= 4) E_q(2) q-Hankel Coulomb shape factor (~0.520011).",
        exp_ref: None,
        eval_fn: |p| {
            if p.is_perturbed {
                qhankel_coulomb_shape_factor(p.q, p.q.prec())
            } else {
                p.ctx.f_qhankel_at_q0().clone()
            }
        },
    },
    ObservableSpec {
        id: "b_he4_m3a_MeV",
        atlas_val_key: None,
        aliases: &["B_4He_M3a_MeV"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Selected,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "E_osc(m_e, q_0) * |lambda_0(K_4, M3a)|, E_osc = m_e / (q_0 - 1)^2",
        description: "3D K_4 tetrahedral colour-flux plaquette ground-state 4He binding energy (+3.65%).",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::B_HE4_AME20_MEV,
            codata_pdg::B_HE4_AME20_SIGMA_MEV,
            "AME2020",
        )),
        eval_fn: |p| {
            let prec = p.q.prec();
            let qm1 = Float::with_val(prec, p.q - f_i64(prec, 1));
            let e_osc = Float::with_val(prec, p.m_e_mev / Float::with_val(prec, &qm1 * &qm1));
            match p.ctx.he4_m3a_dimless() {
                Some(eig) => e_osc * eig,
                None => f_i64(prec, 0),
            }
        },
    },
    ObservableSpec {
        id: "b_he4_64g_MeV",
        atlas_val_key: None,
        aliases: &["B_alpha_64G_MeV"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Exploratory,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "64 * G * m_e",
        description: "Octahedral-Catalan 64*G*m_e alpha-cluster binding proxy.",
        exp_ref: Some(ExpRefSpec::Fixed(
            codata_pdg::B_HE4_AME20_MEV,
            codata_pdg::B_HE4_AME20_SIGMA_MEV,
            "AME2020",
        )),
        eval_fn: |p| {
            let prec = p.q.prec();
            f_i64(prec, 64) * catalan(prec) * p.m_e_mev
        },
    },
    ObservableSpec {
        id: "w_po210_212_214",
        atlas_val_key: None,
        aliases: &["w_po214_over_po212"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "W(2, 5) / W(1, 5) = (2*4) / (1*5) = 8/5",
        description: "Scale-free Racah seniority-0 coherent-pair 214Po/212Po preformation ratio (8/5 = 1.6).",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            f_i64(prec, 8) / f_i64(prec, 5)
        },
    },
    ObservableSpec {
        id: "w_po212_over_po210",
        atlas_val_key: None,
        aliases: &[],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "[W(1,5)*W(1,5)] / [W(1,5)*W(1,1)] = 25 / 5 = 5",
        description: "Racah seniority-0 coherent-pair N=126 shell-closure jump W(212Po)/W(210Po) = 5.",
        exp_ref: None,
        eval_fn: |p| f_i64(p.q.prec(), 5),
    },
    ObservableSpec {
        id: "s_alpha_mj_po210",
        atlas_val_key: None,
        aliases: &["S_alpha_210Po_MJ"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "(1 / (2*5)) * (1 / (2*1)) = 1 / 20",
        description: "Mayer-Jensen N=126 closed-shell 210Po alpha preformation factor (1/20 = 0.05).",
        exp_ref: None,
        eval_fn: |p| {
            let prec = p.q.prec();
            f_i64(prec, 1) / f_i64(prec, 20)
        },
    },
    ObservableSpec {
        id: "t3_bond_count_he4",
        atlas_val_key: None,
        aliases: &["t3_bond_count(4)"],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Derived,
        unit: None,
        is_calibration_pin: false,
        formula: "min(A*(A-1)/2, 3*floor(A/2)) at A = 4",
        description: "Ruled T_3 colour-valence pair-cap bond count at A = 4 (6 bonds = full K_4).",
        exp_ref: None,
        eval_fn: |p| f_u128(p.q.prec(), u128::from(t3_bond_count(4))),
    },
    ObservableSpec {
        id: "qbeta_3H_MeV",
        atlas_val_key: None,
        aliases: &[],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Exploratory,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "|log_q(P(2,1)/P(1,2))| * hbar_q * m_e / 3",
        description: "Bare monotone transfer-matrix 3H -> 3He beta^- Q-value.",
        exp_ref: Some(ExpRefSpec::Fixed("0.01861", "0.00001", "NNDC / AME2020")),
        eval_fn: |p| tm_qbare_mev_at(1, 2, p.m_e_mev, p.q),
    },
    ObservableSpec {
        id: "qbeta_14C_MeV",
        atlas_val_key: None,
        aliases: &[],
        category: Category::NuclearAlpha,
        epistemic_tier: EpistemicTier::Exploratory,
        unit: Some("MeV"),
        is_calibration_pin: false,
        formula: "|log_q(P(7,7)/P(6,8))| * hbar_q * m_e / 3",
        description: "Bare monotone transfer-matrix 14C -> 14N beta^- Q-value (-8.11%).",
        exp_ref: Some(ExpRefSpec::Fixed("0.15648", "0.00004", "NNDC / AME2020")),
        eval_fn: |p| tm_qbare_mev_at(6, 8, p.m_e_mev, p.q),
    },

    // ============================================================================
    // 5. Molecular VSEPR & Condensed-Matter (:val[atlas_theta_*], :val[atlas_L_h2o_kJmol])
    // ============================================================================
    ObservableSpec {
        id: "theta_ch4_deg",
        atlas_val_key: Some("atlas_theta_ch4_deg"),
        aliases: &["predicted_ch4_deg"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("deg"),
        is_calibration_pin: false,
        formula: "arccos(-1/3) * 180 / pi",
        description: "Exact T_d tetrahedral CH_4 H-C-H bond angle.",
        exp_ref: Some(ExpRefSpec::Fixed("109.47122", "0.01", "NIST CCCBDB")),
        eval_fn: |p| {
            let prec = p.q.prec();
            (-f_i64(prec, 1) / f_i64(prec, 3)).acos() * f_i64(prec, 180) / pi(prec)
        },
    },
    ObservableSpec {
        id: "theta_nh3_deg",
        atlas_val_key: Some("atlas_theta_nh3_deg"),
        aliases: &["predicted_nh3_deg"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("deg"),
        is_calibration_pin: false,
        formula: "argmin_{C_{3v}} VSEPR(3 x q_0, 1 x q_0^3)",
        description: "q-weighted VSEPR NH_3 H-N-H bond angle (+0.20%).",
        exp_ref: Some(ExpRefSpec::Fixed("106.67", "0.05", "NIST CCCBDB")),
        eval_fn: |p| vsepr_nh3_deg_at(p.q),
    },
    ObservableSpec {
        id: "theta_h2o_deg",
        atlas_val_key: Some("atlas_theta_h2o_deg"),
        aliases: &["predicted_h2o_deg"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("deg"),
        is_calibration_pin: false,
        formula: "argmin_{C_{2v}} VSEPR(2 x q_0, 2 x q_0^3)",
        description: "q-weighted VSEPR H_2O H-O-H bond angle (+0.23%).",
        exp_ref: Some(ExpRefSpec::Fixed("104.4776", "0.01", "NIST CCCBDB")),
        eval_fn: |p| vsepr_h2o_deg_at(p.q),
    },
    ObservableSpec {
        id: "theta_c2h4_deg",
        atlas_val_key: Some("atlas_theta_c2h4_deg"),
        aliases: &["predicted_c2h4_deg"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("deg"),
        is_calibration_pin: false,
        formula: "argmin_{C_{2v} planar} VSEPR(1 x q_0^2, 2 x q_0)",
        description: "q-weighted VSEPR planar C_2H_4 H-C-H bond angle (+0.54%).",
        exp_ref: Some(ExpRefSpec::Fixed("116.60", "0.10", "NIST CCCBDB")),
        eval_fn: |p| vsepr_c2h4_deg_at(p.q),
    },
    ObservableSpec {
        id: "theta_co2_deg",
        atlas_val_key: Some("atlas_theta_co2_deg"),
        aliases: &["predicted_co2_deg"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Derived,
        unit: Some("deg"),
        is_calibration_pin: false,
        formula: "180",
        description: "Exact D_{inf h} linear CO_2 O-C-O bond angle.",
        exp_ref: Some(ExpRefSpec::Fixed("180.00", "0.01", "NIST CCCBDB")),
        eval_fn: |p| f_i64(p.q.prec(), 180),
    },
    ObservableSpec {
        id: "theta_h2s_deg",
        atlas_val_key: Some("atlas_theta_h2s_deg"),
        aliases: &["predicted_h2s_deg"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("deg"),
        is_calibration_pin: false,
        formula: "90 (orthogonal pure-p baseline)",
        description: "Orthogonal p-orbital baseline H_2S H-S-H angle.",
        exp_ref: Some(ExpRefSpec::Fixed("92.11", "0.05", "NIST CCCBDB")),
        eval_fn: |p| f_i64(p.q.prec(), 90),
    },
    ObservableSpec {
        id: "L_h2o_kJmol",
        atlas_val_key: Some("atlas_L_h2o_kJmol"),
        aliases: &["hbond_h2o_L_pred"],
        category: Category::MolecularGeometry,
        epistemic_tier: EpistemicTier::Conditional,
        unit: Some("kJ/mol"),
        is_calibration_pin: false,
        formula: "2 * (q_0 - q_0^{-1})^2 * E_OH (E_OH = 458.9 kJ/mol)",
        description: "Hydrogen-bond q-plaquette H_2O latent heat of vaporization (-1.34%).",
        exp_ref: Some(ExpRefSpec::Fixed("40.657", "0.020", "CRC Handbook")),
        eval_fn: |p| {
            let prec = p.q.prec();
            let h = p.q - Float::with_val(prec, f_i64(prec, 1) / p.q);
            f_i64(prec, 2) * Float::with_val(prec, &h * &h) * f_str(prec, "458.9")
        },
    },
];

/// Strip `:val[...]` or `{...}` directive wrappers so callers can pass `:val[atlas_m_mu_MeV]`
/// or `atlas_m_mu_MeV` or `m_mu_MeV` interchangeably.
pub fn normalize_lookup_key(raw: &str) -> &str {
    let mut s = raw.trim();
    if let Some(rest) = s.strip_prefix(":val[") {
        if let Some(end) = rest.find(']') {
            s = &rest[..end];
        }
    }
    s.trim()
}

/// Parse a parametric `t3_bond_count(A)` query (e.g. `t3_bond_count(56)` or `t3_bond_count:56`).
fn parse_parametric_t3_bond_count(norm_key: &str) -> Result<Option<u64>, QouValueError> {
    if let Some(inner) = norm_key
        .strip_prefix("t3_bond_count(")
        .and_then(|r| r.strip_suffix(')'))
    {
        let a = inner.trim().parse::<u64>().map_err(|_| {
            QouValueError::InvalidParameter(format!(
                "expected non-negative integer A in `t3_bond_count(A)`, got `{inner}`"
            ))
        })?;
        return Ok(Some(a));
    }
    if let Some(inner) = norm_key.strip_prefix("t3_bond_count:") {
        let a = inner.trim().parse::<u64>().map_err(|_| {
            QouValueError::InvalidParameter(format!(
                "expected non-negative integer A in `t3_bond_count:A`, got `{inner}`"
            ))
        })?;
        return Ok(Some(a));
    }
    Ok(None)
}

/// Look up a static `ObservableSpec` by `id`, `atlas_val_key`, or `aliases`.
pub fn find_spec(query: &str) -> Option<&'static ObservableSpec> {
    let key = normalize_lookup_key(query);
    OBSERVABLES.iter().find(|spec| {
        spec.id.eq_ignore_ascii_case(key)
            || spec
                .atlas_val_key
                .is_some_and(|vk| vk.eq_ignore_ascii_case(key))
            || spec.aliases.iter().any(|al| al.eq_ignore_ascii_case(key))
    })
}

/// List all registered observables (optionally filtered by category substring).
pub fn list_observables(category_filter: Option<&str>) -> Vec<ObservableListEntry> {
    OBSERVABLES
        .iter()
        .filter(|s| category_filter.is_none_or(|f| s.category.matches_filter(f)))
        .map(|s| ObservableListEntry {
            id: s.id.to_string(),
            atlas_val_key: s.atlas_val_key.map(ToString::to_string),
            aliases: s.aliases.iter().map(|a| (*a).to_string()).collect(),
            category: s.category,
            epistemic_tier: s.epistemic_tier,
            unit: s.unit.map(ToString::to_string),
            formula: s.formula.to_string(),
            description: s.description.to_string(),
        })
        .collect()
}

/// Evaluate one `ObservableSpec` with full central-difference MPFR Fréchet–Jacobian
/// covariance propagation wrt `(m_e, R_p = m_p/m_e, m_{\pi^\pm})`.
pub fn evaluate_spec(spec: &ObservableSpec, ctx: &SubstrateContext) -> EvaluatedObservable {
    let prec = ctx.cfg.prec_bits;
    let dps = ctx.cfg.output_dps;

    let o_pred = (spec.eval_fn)(&EvalPoint {
        m_e_mev: &ctx.m_e_mev,
        q: &ctx.q0_proton,
        m_pi_mev: &ctx.m_pi_pm_mev,
        ctx,
        is_perturbed: false,
    });

    let eps = f_str(prec, "1e-30");
    let dme_h = Float::with_val(prec, &ctx.m_e_mev * &eps);
    let dq_h = Float::with_val(prec, &ctx.q0_proton * &eps);
    let dmpi_h = Float::with_val(prec, &ctx.m_pi_pm_mev * &eps);

    let me_p = Float::with_val(prec, &ctx.m_e_mev + &dme_h);
    let me_m = Float::with_val(prec, &ctx.m_e_mev - &dme_h);
    let do_dme = ((spec.eval_fn)(&EvalPoint {
        m_e_mev: &me_p,
        q: &ctx.q0_proton,
        m_pi_mev: &ctx.m_pi_pm_mev,
        ctx,
        is_perturbed: true,
    }) - (spec.eval_fn)(&EvalPoint {
        m_e_mev: &me_m,
        q: &ctx.q0_proton,
        m_pi_mev: &ctx.m_pi_pm_mev,
        ctx,
        is_perturbed: true,
    })) / (f_i64(prec, 2) * &dme_h);

    let q_p = Float::with_val(prec, &ctx.q0_proton + &dq_h);
    let q_m = Float::with_val(prec, &ctx.q0_proton - &dq_h);
    let do_dq = ((spec.eval_fn)(&EvalPoint {
        m_e_mev: &ctx.m_e_mev,
        q: &q_p,
        m_pi_mev: &ctx.m_pi_pm_mev,
        ctx,
        is_perturbed: true,
    }) - (spec.eval_fn)(&EvalPoint {
        m_e_mev: &ctx.m_e_mev,
        q: &q_m,
        m_pi_mev: &ctx.m_pi_pm_mev,
        ctx,
        is_perturbed: true,
    })) / (f_i64(prec, 2) * &dq_h);

    let mpi_p = Float::with_val(prec, &ctx.m_pi_pm_mev + &dmpi_h);
    let mpi_m = Float::with_val(prec, &ctx.m_pi_pm_mev - &dmpi_h);
    let do_dmpi = ((spec.eval_fn)(&EvalPoint {
        m_e_mev: &ctx.m_e_mev,
        q: &ctx.q0_proton,
        m_pi_mev: &mpi_p,
        ctx,
        is_perturbed: true,
    }) - (spec.eval_fn)(&EvalPoint {
        m_e_mev: &ctx.m_e_mev,
        q: &ctx.q0_proton,
        m_pi_mev: &mpi_m,
        ctx,
        is_perturbed: true,
    })) / (f_i64(prec, 2) * &dmpi_h);

    // Truncation floor 10^{-dps}
    let trunc_floor = f_i64(prec, 1) / f_i64(prec, 10).pow(dps as u32);
    let var_pred: Float = Float::with_val(prec, &do_dme * &ctx.m_e_sigma_mev).pow(2)
        + Float::with_val(prec, &do_dq * &ctx.q0_proton_sigma).pow(2)
        + Float::with_val(prec, &do_dmpi * &ctx.m_pi_pm_sigma_mev).pow(2)
        + trunc_floor.pow(2);
    let sigma_pred = var_pred.sqrt();

    let delta_mu_pin_on_hold = ctx.q0_muon_opt.as_ref().map(|q_mu| {
        let o_mu = (spec.eval_fn)(&EvalPoint {
            m_e_mev: &ctx.m_e_mev,
            q: q_mu,
            m_pi_mev: &ctx.m_pi_pm_mev,
            ctx,
            is_perturbed: true,
        });
        fmt_sig(&Float::with_val(prec, o_mu - &o_pred), dps)
    });

    let (
        exp_value,
        exp_sigma,
        exp_source,
        residual,
        roundtrip_residual,
        rel_ppm,
        rel_ppb,
        rel_ppq,
        pull_exp_sigma,
        z_comb_sigma,
    ) = match spec.exp_ref {
        None => (None, None, None, None, None, None, None, None, None, None),
        Some(exp_spec) => {
            let (o_exp, s_exp, src) = match exp_spec {
                ExpRefSpec::Fixed(vs, ss, src) => (f_str(prec, vs), f_str(prec, ss), src),
                ExpRefSpec::Dynamic(f, src) => {
                    let (v, s) = f(prec);
                    (v, s, src)
                }
            };
            let rt_delta = Float::with_val(prec, &o_pred - &o_exp);
            let delta = if spec.is_calibration_pin {
                f_i64(prec, 0)
            } else {
                rt_delta.clone()
            };
            let abs_exp = o_exp.clone().abs();
            let frac = if abs_exp.is_zero() {
                f_i64(prec, 0)
            } else {
                Float::with_val(prec, &delta / &abs_exp)
            };
            let ppm = Float::with_val(prec, &frac * f_i64(prec, 1_000_000));
            let ppb = Float::with_val(prec, &frac * f_i64(prec, 1_000_000_000));
            let ppq = Float::with_val(prec, frac.abs() * f_i64(prec, 10).pow(15));
            let pull_e = if s_exp > 0 {
                Float::with_val(prec, &delta / &s_exp)
            } else {
                f_i64(prec, 0)
            };
            let s_comb = (Float::with_val(prec, &sigma_pred * &sigma_pred)
                + Float::with_val(prec, &s_exp * &s_exp))
            .sqrt();
            let z_c = if s_comb > 0 {
                Float::with_val(prec, &delta / &s_comb)
            } else {
                f_i64(prec, 0)
            };
            (
                Some(fmt_sig(&o_exp, dps)),
                Some(fmt_sig(&s_exp, dps)),
                Some(src.to_string()),
                Some(fmt_sig(&delta, dps)),
                Some(fmt_sig(&rt_delta, dps)),
                Some(fmt_sig(&ppm, dps)),
                Some(fmt_sig(&ppb, dps)),
                Some(fmt_sig(&ppq, dps)),
                Some(fmt_sig(&pull_e, dps)),
                Some(fmt_sig(&z_c, dps)),
            )
        }
    };

    EvaluatedObservable {
        id: spec.id.to_string(),
        atlas_val_key: spec.atlas_val_key.map(ToString::to_string),
        category: spec.category,
        epistemic_tier: spec.epistemic_tier,
        unit: spec.unit.map(ToString::to_string),
        q0_anchor: "proton".to_string(),
        dps,
        mpfr_bits: prec,
        is_calibration_pin: spec.is_calibration_pin,
        formula: spec.formula.to_string(),
        value: fmt_sig(&o_pred, dps),
        sigma_pred: fmt_sig(&sigma_pred, dps),
        jacobian: JacobianRecord {
            do_dm_e: fmt_sig(&do_dme, dps),
            do_dq0: fmt_sig(&do_dq, dps),
            do_dm_pi: fmt_sig(&do_dmpi, dps),
        },
        exp_value,
        exp_sigma,
        exp_source,
        residual,
        roundtrip_residual,
        rel_ppm,
        rel_ppb,
        rel_ppq,
        pull_exp_sigma,
        z_comb_sigma,
        delta_mu_pin_on_hold,
    }
}

/// Evaluate any observable by `id`, `:val[...]` key, alias, or parametric `t3_bond_count(A)`.
pub fn evaluate_by_key(
    query: &str,
    ctx: &SubstrateContext,
) -> Result<EvaluatedObservable, QouValueError> {
    if let Some(spec) = find_spec(query) {
        return Ok(evaluate_spec(spec, ctx));
    }
    let norm = normalize_lookup_key(query);
    if let Some(a) = parse_parametric_t3_bond_count(norm)? {
        let bonds = t3_bond_count(a);
        return Ok(EvaluatedObservable {
            id: format!("t3_bond_count({a})"),
            atlas_val_key: None,
            category: Category::NuclearAlpha,
            epistemic_tier: EpistemicTier::Derived,
            unit: None,
            q0_anchor: "proton".to_string(),
            dps: ctx.cfg.output_dps,
            mpfr_bits: ctx.cfg.prec_bits,
            is_calibration_pin: false,
            formula: format!("min(A*(A-1)/2, 3*floor(A/2)) at A = {a}"),
            value: bonds.to_string(),
            sigma_pred: "0.0".to_string(),
            jacobian: JacobianRecord {
                do_dm_e: "0.0".to_string(),
                do_dq0: "0.0".to_string(),
                do_dm_pi: "0.0".to_string(),
            },
            exp_value: None,
            exp_sigma: None,
            exp_source: None,
            residual: None,
            roundtrip_residual: None,
            rel_ppm: None,
            rel_ppb: None,
            rel_ppq: None,
            pull_exp_sigma: None,
            z_comb_sigma: None,
            delta_mu_pin_on_hold: ctx.q0_muon_opt.as_ref().map(|_| "0.0".to_string()),
        });
    }
    Err(QouValueError::UnknownObservable(query.to_string()))
}

/// Evaluate every registered observable in `OBSERVABLES` in deterministic registry order.
pub fn evaluate_all(ctx: &SubstrateContext) -> Vec<EvaluatedObservable> {
    OBSERVABLES.iter().map(|s| evaluate_spec(s, ctx)).collect()
}
