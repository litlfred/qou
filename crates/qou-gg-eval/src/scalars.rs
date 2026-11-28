//! Proton-pinned `q_0^(p)` and canonical energy scales in `rug::Float` (`>= 266` bits).
//!
//! Derives `Vol(4_1) = 2 * Cl_2(pi/3)` via exact rational Bernoulli numbers `B_{2k}`
//! and solves the proton anchor identity
//! `m_p / m_e = 2 * (Vol(4_1) / hbar_q^2) * F_Bor(q) - 12`
//! via damped Newton/secant iteration in `rug::Float` at `prec_bits >= 266`.

use rug::ops::{CompleteRound, Pow};
use rug::{Assign, Float, Integer, Rational};
use serde::{Deserialize, Serialize};

/// Default MPFR precision in bits (`320` bits ≈ `96.3` decimal digits, comfortably above 80 dps).
pub const DEFAULT_PREC_BITS: u32 = 320;

/// Minimum admissible MPFR precision (`266` bits ≈ `80.07` decimal digits).
pub const MIN_PREC_BITS: u32 = 266;

/// Default output decimal digits (`80` significant digits).
pub const DEFAULT_OUT_DPS: usize = 80;

/// CODATA 2022 proton-to-electron mass ratio (`qou_substrate/data/allascii.txt`).
pub const CODATA_2022_MP_OVER_ME: &str = "1836.152673426";

/// CODATA 2022 electron mass in MeV (`qou_substrate.constants.M_E_MEV`).
pub const CODATA_2022_ME_MEV: &str = "0.51099895069";

/// AME2020 nuclear total binding energies `B(Z, N)` in MeV (comparison boundary ONLY).
pub const AME2020_B_2H_MEV: &str = "2.224566";
pub const AME2020_B_3H_MEV: &str = "8.481796";
pub const AME2020_B_3HE_MEV: &str = "7.718041";
pub const AME2020_B_4HE_MEV: &str = "28.295673";

/// Parse an exact decimal literal into a `rug::Float` of precision `prec`.
pub fn parse_dec(prec: u32, s: &str) -> Float {
    Float::parse(s)
        .unwrap_or_else(|e| panic!("invalid decimal literal {s:?}: {e}"))
        .complete(prec)
}

/// Format a `rug::Float` to `dps` significant decimal digits without `f64` conversion.
pub fn fmt_dps(x: &Float, dps: usize) -> String {
    if x.is_zero() {
        return "0".to_string();
    }
    x.to_string_radix(10, Some(dps))
}

/// Compute `Vol(4_1) = 2 * Cl_2(pi / 3)` at `prec` bits using exact rational Bernoulli numbers:
/// `Cl_2(theta) = theta * (1 - ln(theta)) + sum_{k=1}^K |B_{2k}| * theta^(2k+1) / (2k * (2k+1)!)`.
/// At `theta = pi/3`, `(theta / (2*pi))^(2k) = (1/6)^(2k)`, so `K = 80` gives `< 10^-124` truncation error.
pub fn compute_vol_figure_eight(prec: u32) -> Float {
    let work = prec + 64;
    let max_m: usize = 160; // up to B_160 (K = 80)

    // Pascal triangle for binomial coefficients C(n, k) up to max_m + 1.
    let mut binom: Vec<Vec<Integer>> = vec![vec![Integer::from(0); max_m + 2]; max_m + 2];
    for n in 0..=max_m + 1 {
        binom[n][0].assign(1);
        binom[n][n].assign(1);
        for k in 1..n {
            let s = Integer::from(&binom[n - 1][k - 1] + &binom[n - 1][k]);
            binom[n][k] = s;
        }
    }

    // Exact Bernoulli numbers B_0 .. B_{max_m}: sum_{j=0}^m C(m+1, j) B_j = 0 for m >= 1.
    let mut bern: Vec<Rational> = vec![Rational::from(0); max_m + 1];
    bern[0] = Rational::from(1);
    bern[1] = Rational::from((-1, 2));
    for m in (2..=max_m).step_by(2) {
        let mut sum = Rational::from(0);
        // j = 0
        sum += &bern[0];
        // j = 1
        let c1 = Rational::from(&binom[m + 1][1]);
        sum += c1 * &bern[1];
        // even j = 2 .. m-2
        for j in (2..m).step_by(2) {
            let cj = Rational::from(&binom[m + 1][j]);
            sum += cj * &bern[j];
        }
        let denom = Rational::from(&binom[m + 1][m]);
        bern[m] = -sum / denom;
    }

    let pi = Float::with_val(work, rug::float::Constant::Pi);
    let theta = Float::with_val(work, &pi / 3u32);
    let ln_theta = Float::with_val(work, theta.clone().ln());
    let mut cl2 = Float::with_val(work, &theta * (Float::with_val(work, 1) - ln_theta));

    let theta_sq = Float::with_val(work, &theta * &theta);
    let mut theta_pow = theta.clone(); // theta^(2k+1), starts at theta^1 before loop step
    let mut fact = Integer::from(1); // (2k+1)!

    for k in 1..=(max_m / 2) {
        let two_k = 2 * k;
        theta_pow *= &theta_sq; // theta^(2k+1)
        fact *= two_k as u32;
        fact *= (two_k + 1) as u32;

        let b_abs = bern[two_k].clone().abs();
        let coeff_rat = b_abs / Rational::from(&fact * Integer::from(two_k as u32));
        let coeff = Float::with_val(work, coeff_rat);
        let term = Float::with_val(work, coeff * &theta_pow);
        cl2 += &term;
    }

    let vol_work = Float::with_val(work, cl2 * 2u32);
    Float::with_val(prec, vol_work)
}

/// Evaluate the proton anchor residual `R(q) = 2 * (Vol(4_1) / hbar_q^2) * F_Bor(q) - 12 - mp_me`.
fn proton_anchor_residual(q: &Float, vol: &Float, mp_me: &Float, work: u32) -> Float {
    let one = Float::with_val(work, 1);
    let q_inv = Float::with_val(work, &one / q);
    let hbar = Float::with_val(work, &one - &q_inv);
    let hbar2 = Float::with_val(work, &hbar * &hbar);

    let h = Float::with_val(work, q - &q_inv);
    let h2 = Float::with_val(work, &h * &h);
    let h4 = Float::with_val(work, &h2 * &h2);
    let h6 = Float::with_val(work, &h4 * &h2);

    // |tr_M(beta_Bor, q)| = (4 + h^2 - 3*h^4 - h^6) / (h^2 + 4)
    let num_bor = Float::with_val(
        work,
        Float::with_val(work, 4) + &h2 - Float::with_val(work, 3u32 * &h4) - &h6,
    );
    let den_bor = Float::with_val(work, &h2 + 4u32);
    let tr_bor = Float::with_val(work, num_bor / den_bor);

    // [3]_q! = [2]_q * [3]_q = (q + q^-1) * (q^2 + 1 + q^-2)
    let q2 = Float::with_val(work, q * q);
    let q_inv2 = Float::with_val(work, &q_inv * &q_inv);
    let q2_int = Float::with_val(work, q + &q_inv);
    let q3_int = q2.clone() + &one + &q_inv2;
    let q3_fact = Float::with_val(work, q2_int * q3_int);
    let q3_pow = Float::with_val(work, &q2 * q);

    let f_bor = Float::with_val(work, (tr_bor * q3_fact) / q3_pow);
    let lhs = Float::with_val(
        work,
        Float::with_val(work, 2u32 * vol) / hbar2 * f_bor - 12u32,
    );
    Float::with_val(work, lhs - mp_me)
}

/// Solve the proton substrate identity for `q_0^(p)` at `prec` bits via secant refinement.
pub fn solve_q0_proton(prec: u32, mp_me_override: Option<&str>) -> Float {
    let work = prec + 64;
    let vol = compute_vol_figure_eight(work);
    let mp_me = parse_dec(work, mp_me_override.unwrap_or(CODATA_2022_MP_OVER_ME));

    let mut q_prev = parse_dec(work, "1.10997858");
    let mut q_curr = parse_dec(work, "1.10997859");
    let mut f_prev = proton_anchor_residual(&q_prev, &vol, &mp_me, work);

    let tol = Float::with_val(work, 10).pow(-((prec as i32 * 3) / 10 + 10));
    for _ in 0..80 {
        let f_curr = proton_anchor_residual(&q_curr, &vol, &mp_me, work);
        if f_curr.clone().abs() < tol {
            break;
        }
        let dq = Float::with_val(work, &q_curr - &q_prev);
        let df = Float::with_val(work, &f_curr - &f_prev);
        if df.is_zero() {
            break;
        }
        let step = Float::with_val(work, (&f_curr * dq) / df);
        q_prev = q_curr.clone();
        f_prev = f_curr;
        q_curr -= step;
    }

    Float::with_val(prec, q_curr)
}

/// Complete proton-pinned scalar context at `prec_bits`.
#[derive(Debug, Clone)]
pub struct Q0Params {
    pub prec_bits: u32,
    pub q: Float,
    pub q_inv: Float,
    pub h: Float,
    pub hbar_q: Float,
    pub q2_int: Float,
    pub q3_int: Float,
    pub z_d: Float,
    pub vol_4_1: Float,
    pub m_e_mev: Float,
    pub e0_order_zero_mev: Float,
    pub e0_tower_mev: Float,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Q0SummaryJson {
    pub q0_anchor: String,
    pub prec_bits: u32,
    pub out_dps: usize,
    pub q0: String,
    pub h: String,
    pub hbar_q: String,
    pub z_d: String,
    pub vol_figure_eight: String,
    pub m_e_mev: String,
    pub e0_order_zero_mev: String,
    pub e0_tower_mev: String,
}

impl Q0Params {
    pub fn proton_pinned(prec_bits: u32, q0_override: Option<&str>) -> Self {
        assert!(
            prec_bits >= MIN_PREC_BITS,
            "prec_bits ({prec_bits}) must be >= {MIN_PREC_BITS} (80 dps floor)"
        );
        let vol_4_1 = compute_vol_figure_eight(prec_bits);
        let q = match q0_override {
            Some(s) => parse_dec(prec_bits, s),
            None => solve_q0_proton(prec_bits, None),
        };
        let one = Float::with_val(prec_bits, 1);
        let q_inv = Float::with_val(prec_bits, &one / &q);
        let h = Float::with_val(prec_bits, &q - &q_inv);
        let hbar_q = Float::with_val(prec_bits, &one - &q_inv);
        let q2_int = Float::with_val(prec_bits, &q + &q_inv);
        let q2 = Float::with_val(prec_bits, &q * &q);
        let q_inv2 = Float::with_val(prec_bits, &q_inv * &q_inv);
        let q3_int = q2.clone() + &one + &q_inv2;

        let q3 = Float::with_val(prec_bits, &q2 * &q);
        let q2_plus_1 = Float::with_val(prec_bits, &q2 + &one);
        let z_d = Float::with_val(prec_bits, q3 / q2_plus_1);

        let m_e_mev = parse_dec(prec_bits, CODATA_2022_ME_MEV);
        let q_minus_1 = Float::with_val(prec_bits, &q - &one);
        let denom_0 = Float::with_val(prec_bits, &q * q_minus_1);
        let e0_order_zero_mev = Float::with_val(prec_bits, &m_e_mev / denom_0);
        let one_minus_hbar2 =
            Float::with_val(prec_bits, &one - Float::with_val(prec_bits, &hbar_q * &hbar_q));
        let e0_tower_mev = Float::with_val(prec_bits, &e0_order_zero_mev / one_minus_hbar2);

        Self {
            prec_bits,
            q,
            q_inv,
            h,
            hbar_q,
            q2_int,
            q3_int,
            z_d,
            vol_4_1,
            m_e_mev,
            e0_order_zero_mev,
            e0_tower_mev,
        }
    }

    /// Quantum integer `[m]_q = (q^m - q^-m) / (q - q^-1)`.
    pub fn q_int(&self, m: i32) -> Float {
        let p = self.prec_bits;
        if m == 0 {
            return Float::with_val(p, 0);
        }
        let qm = Float::with_val(p, self.q.clone().pow(m));
        let q_invm = Float::with_val(p, self.q_inv.clone().pow(m));
        Float::with_val(p, (qm - q_invm) / &self.h)
    }

    /// Two-row Convention-D Ocneanu/Schur–Weyl weight `y_{(m-r, r)} = [m - 2r + 1]_q / [2]_q^m`.
    pub fn y_two_row(&self, m: usize, r: usize) -> Float {
        assert!(2 * r <= m, "invalid two-row partition ({}, {})", m - r, r);
        let p = self.prec_bits;
        let num = self.q_int((m - 2 * r + 1) as i32);
        let den = Float::with_val(p, self.q2_int.clone().pow(m as u32));
        Float::with_val(p, num / den)
    }

    pub fn to_summary_json(&self, dps: usize) -> Q0SummaryJson {
        Q0SummaryJson {
            q0_anchor: "proton".to_string(),
            prec_bits: self.prec_bits,
            out_dps: dps,
            q0: fmt_dps(&self.q, dps),
            h: fmt_dps(&self.h, dps),
            hbar_q: fmt_dps(&self.hbar_q, dps),
            z_d: fmt_dps(&self.z_d, dps),
            vol_figure_eight: fmt_dps(&self.vol_4_1, dps),
            m_e_mev: fmt_dps(&self.m_e_mev, dps),
            e0_order_zero_mev: fmt_dps(&self.e0_order_zero_mev, dps),
            e0_tower_mev: fmt_dps(&self.e0_tower_mev, dps),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn vol_4_1_matches_50_digit_reference() {
        let vol = compute_vol_figure_eight(320);
        let ref50 = parse_dec(320, "2.0298832128193072500424051085490405718833786150606");
        let diff = (vol - &ref50).abs();
        let bound = parse_dec(320, "1e-49");
        assert!(diff < bound, "Vol(4_1) mismatch: diff = {diff}");
    }

    #[test]
    fn q0_proton_matches_prefix_and_residual() {
        let p = Q0Params::proton_pinned(320, None);
        let s = fmt_dps(&p.q, 50);
        assert!(
            s.starts_with("1.10997858275138"),
            "unexpected q0^(p) prefix: {s}"
        );
        let mp_me = parse_dec(320, CODATA_2022_MP_OVER_ME);
        let res = proton_anchor_residual(&p.q, &p.vol_4_1, &mp_me, 320).abs();
        assert!(
            res < parse_dec(320, "1e-85"),
            "proton residual too large: {res}"
        );
    }
}
