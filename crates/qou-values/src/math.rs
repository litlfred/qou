//! Zero-`f64` arbitrary-precision MPFR (`rug::Float`) special functions and formatting.
//!
//! Every numerical constant and intermediate step in `qou-values` runs natively in MPFR
//! with configurable decimal digits (`--dps`, default `80`, internal working precision
//! `>= 368` bits `~ 110` decimal digits). No `f32` or `f64` operations exist anywhere
//! in this module or crate.

use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;

/// Precision configuration coupling output decimal digits (`output_dps`) to internal
/// MPFR guard precision (`prec_bits`).
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct PrecisionConfig {
    /// Requested significant decimal digits on output (`15..=250`, default `80`).
    pub output_dps: usize,
    /// Internal working decimal digits (`output_dps + 30`, minimum `105`).
    pub work_dps: usize,
    /// Internal MPFR significand width in bits (minimum `368`, > `332` bits ~ 100 dps).
    pub prec_bits: u32,
}

impl PrecisionConfig {
    /// Construct a precision configuration for `output_dps` decimal digits.
    pub fn new(output_dps: usize) -> Self {
        let clamped = output_dps.clamp(15, 250);
        let work_dps = (clamped + 30).max(105);
        // ceil(work_dps * log2(10)) + 16 guard bits; 3322 / 1000 > log2(10) = 3.321928...
        let bits = ((work_dps as u32) * 3322).div_ceil(1000) + 16;
        let prec_bits = bits.max(368);
        Self {
            output_dps: clamped,
            work_dps,
            prec_bits,
        }
    }
}

impl Default for PrecisionConfig {
    fn default() -> Self {
        Self::new(80)
    }
}

/// Parse an exact decimal string into a `prec`-bit MPFR `Float` with zero `f64` intermediate.
#[inline]
pub fn f_str(prec: u32, s: &str) -> Float {
    let parsed = Float::parse(s).unwrap_or_else(|e| panic!("invalid decimal literal `{s}`: {e}"));
    Float::with_val(prec, parsed)
}

/// Construct a `prec`-bit MPFR `Float` from an exact `i64`.
#[inline]
pub fn f_i64(prec: u32, n: i64) -> Float {
    Float::with_val(prec, n)
}

/// Construct a `prec`-bit MPFR `Float` from an exact `u128`.
#[inline]
pub fn f_u128(prec: u32, n: u128) -> Float {
    Float::with_val(prec, n)
}

/// Format an MPFR `Float` to `dps` significant decimal digits, expanding `e-1..e-4`
/// into clean fixed-point `0.xxxx` strings matching `mpmath.nstr` conventions.
pub fn fmt_sig(val: &Float, dps: usize) -> String {
    if val.is_zero() {
        return "0.0".to_string();
    }
    let raw = val.to_string_radix(10, Some(dps.max(1)));
    if let Some(e_pos) = raw.find('e') {
        if let Ok(exp) = raw[e_pos + 1..].parse::<i32>() {
            if (-4..=-1).contains(&exp) {
                let mant = &raw[..e_pos];
                let (sign, body) = match mant.strip_prefix('-') {
                    Some(rest) => ("-", rest),
                    None => ("", mant),
                };
                let digits: String = body.chars().filter(|&c| c != '.').collect();
                let zeros = "0".repeat((-exp - 1) as usize);
                return format!("{sign}0.{zeros}{digits}");
            }
        }
    }
    raw
}

/// `\pi` at `prec` MPFR bits.
#[inline]
pub fn pi(prec: u32) -> Float {
    Float::with_val(prec, Constant::Pi)
}

/// Catalan's constant `G = \beta(2)` at `prec` MPFR bits.
#[inline]
pub fn catalan(prec: u32) -> Float {
    Float::with_val(prec, Constant::Catalan)
}

/// Apéry's constant `\zeta(3)` at `prec` MPFR bits.
#[inline]
pub fn zeta_3(prec: u32) -> Float {
    Float::with_val(prec, Float::zeta_u(3))
}

/// Exact integer binomial coefficient `C(n, k)` in `u128`.
pub fn binom_u128(n: u32, k: u32) -> u128 {
    if k > n {
        return 0;
    }
    let k_eff = k.min(n - k);
    let mut acc: u128 = 1;
    for i in 1..=k_eff {
        acc = (acc * u128::from(n - k_eff + i)) / u128::from(i);
    }
    acc
}

/// Balanced symmetric quantum integer `[n]_q = (q^n - q^{-n}) / (q - q^{-1})`.
pub fn q_int(n: i32, q: &Float) -> Float {
    let prec = q.prec();
    if n == 0 {
        return f_i64(prec, 0);
    }
    if n == 1 {
        return f_i64(prec, 1);
    }
    let q_n = q.clone().pow(n);
    let q_neg_n = q.clone().pow(-n);
    let q_inv = f_i64(prec, 1) / q;
    let denom = Float::with_val(prec, q - &q_inv);
    (q_n - q_neg_n) / denom
}

/// Doubled 2-strand torus-link Plancherel trace polynomial
/// `2 P_m(h) = \sum_{j=0}^m C(m + j, 2j) h^{2j}`.
pub fn trace_poly_two_p(m: u32, h: &Float) -> Float {
    let prec = h.prec();
    let h2 = Float::with_val(prec, h * h);
    let mut h_pow = f_i64(prec, 1);
    let mut acc = f_i64(prec, 0);
    for j in 0..=m {
        let c = f_u128(prec, binom_u128(m + j, 2 * j));
        acc += &c * &h_pow;
        h_pow *= &h2;
    }
    acc
}

/// Hyperbolic volume of the figure-eight knot complement `Vol(4_1) = 2 Cl_2(\pi/3)`
/// computed to full `prec`-bit MPFR precision via the exponentially convergent
/// Clausen-zeta expansion at `\theta = \pi/3` (`(\theta / 2\pi)^{2k} = 36^{-k}`):
///
/// `Cl_2(\theta) = \theta (1 - \ln \theta) + \theta \sum_{k=1}^\infty \frac{2 \zeta(2k)}{2k(2k+1) 36^k}`.
pub fn vol_4_1(prec: u32) -> Float {
    let work = prec + 32;
    let pi_val = pi(work);
    let theta = pi_val / f_i64(work, 3);
    let one = f_i64(work, 1);
    let inv36 = f_i64(work, 1) / f_i64(work, 36);
    let mut p36 = inv36.clone();
    let mut series = f_i64(work, 0);
    let eps = f_i64(work, 1) >> (work.saturating_sub(6));

    let max_terms = ((work as usize) / 4) + 60;
    for k in 1..=max_terms {
        let two_k = (2 * k) as u32;
        let z2k = Float::with_val(work, Float::zeta_u(two_k));
        let denom = f_u128(work, u128::from(two_k) * u128::from(two_k + 1));
        let term = (f_i64(work, 2) * z2k * &p36) / denom;
        series += &term;
        if term.clone().abs() < eps {
            break;
        }
        p36 *= &inv36;
    }

    let cl2 = &theta * (&one - theta.clone().ln()) + &theta * series;
    Float::with_val(prec, f_i64(work, 2) * cl2)
}

/// Complex arithmetic helper `(re, im)` in pure `rug::Float`.
#[inline]
fn cmul(prec: u32, a: &(Float, Float), b: &(Float, Float)) -> (Float, Float) {
    let re = Float::with_val(prec, &a.0 * &b.0) - Float::with_val(prec, &a.1 * &b.1);
    let im = Float::with_val(prec, &a.0 * &b.1) + Float::with_val(prec, &a.1 * &b.0);
    (re, im)
}

#[inline]
fn cdiv(prec: u32, a: &(Float, Float), b: &(Float, Float)) -> (Float, Float) {
    let norm2 = Float::with_val(prec, &b.0 * &b.0) + Float::with_val(prec, &b.1 * &b.1);
    let re = (Float::with_val(prec, &a.0 * &b.0) + Float::with_val(prec, &a.1 * &b.1)) / &norm2;
    let im = (Float::with_val(prec, &a.1 * &b.0) - Float::with_val(prec, &a.0 * &b.1)) / norm2;
    (re, im)
}

/// Hyperbolic volume of the `5_2` knot complement `Vol(5_2) = 3 D(z_0)` where `z_0` is the
/// upper-half-plane root of `z^3 - z^2 + 1 = 0`.
///
/// Uses `w_0 = 1 / z_0` and the algebraic identity `1 - w_0 = -w_0^3` together with the
/// Bloch-Wigner symmetries `D(z_0) = -D(w_0) = D(1 - w_0) = D(-w_0^3)`, where
/// `|-w_0^3| \approx 0.655866`, giving rapid geometric convergence at any MPFR precision.
pub fn vol_5_2(prec: u32) -> Float {
    let work = prec + 40;
    let one = f_i64(work, 1);
    let zero = f_i64(work, 0);
    // Initial rational seed near 0.8774 + 0.7449 i
    let mut z = (
        f_i64(work, 88) / f_i64(work, 100),
        f_i64(work, 74) / f_i64(work, 100),
    );
    let tol_sq = f_i64(work, 1) >> (2 * work.saturating_sub(12));

    for _ in 0..40 {
        let z2 = cmul(work, &z, &z);
        let z3 = cmul(work, &z2, &z);
        let f_val = (
            Float::with_val(work, &z3.0 - &z2.0) + &one,
            Float::with_val(work, &z3.1 - &z2.1),
        );
        // f'(z) = 3 z^2 - 2 z
        let fp = (
            f_i64(work, 3) * &z2.0 - f_i64(work, 2) * &z.0,
            f_i64(work, 3) * &z2.1 - f_i64(work, 2) * &z.1,
        );
        let step = cdiv(work, &f_val, &fp);
        z.0 -= &step.0;
        z.1 -= &step.1;
        let step_n2 = Float::with_val(work, &step.0 * &step.0)
            + Float::with_val(work, &step.1 * &step.1);
        if step_n2 < tol_sq {
            break;
        }
    }

    // w0 = 1 / z0; u = -w0^3 = 1 - w0, |u| ~ 0.655866
    let w0 = cdiv(work, &(one.clone(), zero.clone()), &z);
    let w2 = cmul(work, &w0, &w0);
    let w3 = cmul(work, &w2, &w0);
    let u = (-w3.0, -w3.1);

    let eps_sq = f_i64(work, 1) >> (2 * work.saturating_sub(8));
    let mut up = u.clone();
    let mut im_li2 = f_i64(work, 0);
    let max_terms = (work as usize) * 3 + 200;
    for n in 1..=max_terms {
        let n_sq = f_u128(work, (n as u128) * (n as u128));
        let im_term = Float::with_val(work, &up.1 / &n_sq);
        im_li2 += &im_term;
        if n > 20 {
            let mag2 = (Float::with_val(work, &up.0 * &up.0)
                + Float::with_val(work, &up.1 * &up.1))
                / Float::with_val(work, &n_sq * &n_sq);
            if mag2 < eps_sq {
                break;
            }
        }
        up = cmul(work, &up, &u);
    }

    let one_minus_u_re = Float::with_val(work, &one - &u.0);
    let one_minus_u_im = Float::with_val(work, -&u.1);
    let arg_one_minus_u = one_minus_u_im.atan2(&one_minus_u_re);
    let abs_u = (Float::with_val(work, &u.0 * &u.0) + Float::with_val(work, &u.1 * &u.1)).sqrt();
    let bw = im_li2 + arg_one_minus_u * abs_u.ln();
    Float::with_val(prec, f_i64(work, 3) * bw)
}

/// Real trilogarithm `\mathrm{Li}_3(x) = \sum_{n=1}^\infty x^n / n^3` for `|x| < 1`
/// (at `x = q_0^{-2} \approx 0.8116`, ~1,250 terms reach `110` dps in `< 0.3 ms`).
pub fn polylog3_real(x: &Float, prec: u32) -> Float {
    let work = prec + 24;
    let xw = Float::with_val(work, x);
    let mut xp = xw.clone();
    let mut acc = f_i64(work, 0);
    let eps = f_i64(work, 1) >> work.saturating_sub(6);
    let max_terms = (work as usize) * 5 + 400;
    for n in 1..=max_terms {
        let n_u = n as u128;
        let denom = f_u128(work, n_u * n_u * n_u);
        let term = Float::with_val(work, &xp / denom);
        acc += &term;
        if n > 16 && term.clone().abs() < eps {
            break;
        }
        xp *= &xw;
    }
    Float::with_val(prec, acc)
}

/// Unnormalized Hahn–Exton q-Bessel lattice amplitude `\tilde{J}_{1/2}(p^k; p^2)` with `p = 1 / step`
/// (omitting the `k`-independent `(p^3; p^2)_\infty / (p^2; p^2)_\infty` prefactor, which cancels
/// identically in normalized shell weights `w_k / \sum_j w_j`), evaluated at raised precision
/// when `k < 0` to absorb alternating-series peak cancellation (`coulomb_shape_factor_qbessel_probe.py`).
fn hahn_exton_half_unnorm_on_lattice(k: i32, step: &Float, base_work: u32) -> Float {
    let extra_bits: u32 = if k < 0 {
        let k2 = (k as i64 * k as i64) as u32;
        // Peak ~ step^{k^2} while sum ~ step^{-k^2/2}: ~0.23 * k^2 bits cancelled at q0 ~ 1.11;
        // 3/8 = 0.375 bits per k^2 + 112 guard bits preserves full base_work precision.
        (k2 * 3) / 8 + 112
    } else {
        64
    };
    let work = base_work + extra_bits;
    let one = f_i64(work, 1);
    let step_w = Float::with_val(work, step);
    let p = Float::with_val(work, &one / &step_w);
    let q_big = Float::with_val(work, &p * &p);
    let x = p.clone().pow(k);
    let x2 = Float::with_val(work, &x * &x);
    // nu = 1/2 => a = Q^{3/2} = p^3
    let a = p.clone().pow(3);

    let mut s = f_i64(work, 0);
    let mut t = one.clone();
    let mut q_k = one.clone();
    let tiny = f_i64(work, 1) >> base_work.saturating_sub(8);

    for _ in 0..2000 {
        s += &t;
        let q_prev = q_k.clone();
        q_k *= &q_big;
        let denom = Float::with_val(work, &one - Float::with_val(work, &a * &q_prev))
            * Float::with_val(work, &one - &q_k);
        let t_next = -(Float::with_val(work, &q_k * &x2) / denom) * &t;
        let abs_next = t_next.clone().abs();
        let abs_t_half = Float::with_val(work, t.clone().abs() / f_i64(work, 2));
        let scale_ref = s.clone().abs().max(&tiny);
        if abs_next <= abs_t_half && abs_next < Float::with_val(work, &tiny * scale_ref) {
            s += &t_next;
            break;
        }
        t = t_next;
    }

    let x_half = x.sqrt();
    let val = x_half * s;
    Float::with_val(base_work, val)
}

/// Derived s-shell (`A <= 4`) Coulomb shape factor `f_qhankel(q_0)` on the full Jackson
/// lattice `p^\mathbb{Z}` (`p = 1/q_0`, `\nu = 1/2`; `QOU.Nuclear.CoulombShellShapeFactor`,
/// `coulomb_shape_factor_qbessel_probe.py`), computed directly in MPFR (`~0.52001056299485...`).
pub fn qhankel_coulomb_shape_factor(q0: &Float, prec: u32) -> Float {
    let work = prec + 32;
    let one = f_i64(work, 1);
    let q_w = Float::with_val(work, q0);
    let p = Float::with_val(work, &one / &q_w);
    let tail_sq = f_i64(work, 1) >> (2 * work);

    let mut kmin: i32 = -1;
    let mut small_run = 0;
    while small_run < 4 && kmin > -60 {
        kmin -= 1;
        let r = p.clone().pow(kmin);
        let jv = hahn_exton_half_unnorm_on_lattice(kmin, &q_w, work);
        let w = Float::with_val(work, &r * &r) * Float::with_val(work, &jv * &jv);
        if w < tail_sq {
            small_run += 1;
        } else {
            small_run = 0;
        }
    }

    // Inner edge weight decays as p^{3 k}; choose kmax so p^{3 kmax} < tail_sq
    let ln_p_abs = p.clone().ln().abs();
    let target_ln = f_i64(work, (2 * work) as i64) * f_i64(work, 2).ln();
    let kmax_f = target_ln / (f_i64(work, 3) * ln_p_abs);
    let kmax = (kmax_f.to_i32_saturating_round(rug::float::Round::Up).unwrap_or(180) + 8).min(550);

    // Radii p^k decrease as k increases; iterate from largest k (smallest r) to smallest k (largest r)
    let mut pairs: Vec<(Float, Float)> = Vec::with_capacity((kmax - kmin + 1) as usize);
    for k in (kmin..=kmax).rev() {
        let r = p.clone().pow(k);
        let jv = hahn_exton_half_unnorm_on_lattice(k, &q_w, work);
        let w = Float::with_val(work, &r * &r) * Float::with_val(work, &jv * &jv);
        pairs.push((r, w));
    }

    let mut tot = f_i64(work, 0);
    for (_, w) in &pairs {
        tot += w;
    }

    let two = f_i64(work, 2);
    let mut energy = f_i64(work, 0);
    let mut inner = f_i64(work, 0);
    let mut rms_sq = f_i64(work, 0);
    for (r, w_raw) in &pairs {
        let w = Float::with_val(work, w_raw / &tot);
        let half_w = Float::with_val(work, &w / &two);
        energy += Float::with_val(work, &w / r) * Float::with_val(work, &half_w + &inner);
        inner += &w;
        rms_sq += &w * Float::with_val(work, r * r);
    }

    let f_val = energy * rms_sq.sqrt();
    Float::with_val(prec, f_val)
}
