//! Exact 6-basis normal-form evaluator for `H_3(q)` at `>= 80` dps (`rug::Float`).
//!
//! Basis order (matching `gram.rs` and `pyhecke.atom`):
//! `[1, sigma_0, sigma_1, L_plus = sigma_0*sigma_1, L_minus = sigma_1*sigma_0, e_minus = sigma_0*sigma_1*sigma_0]`.
//!
//! Evaluates:
//! - Photonic & 4-photon states: `1`, `gamma_+`, `gamma_-`, `V`, `V^2`, `V^3 = gamma_+ * gamma_-`,
//!   `V^6 = (gamma_+ * gamma_-)^2`, `gamma_+^4`, `gamma_-^4`;
//! - Single hadrons (`A = 1`): bare `γγ` nucleon `V^3`, production `uud` (`p`) and `udd` (`n`)
//!   11-letter words (`PairSkeinMassConventionD`), symbolic charge-dressed split invariants
//!   (`NucleonChargeDressedWords`), and charged pion `pi^+- = sigma_0^2`.

use crate::scalars::{fmt_dps, Q0Params};
use rug::ops::{CompleteRound, Pow};
use rug::Float;
use serde::{Deserialize, Serialize};

pub const H3_BASIS_NAMES: [&str; 6] = [
    "1", "sigma_0", "sigma_1", "L_plus", "L_minus", "e_minus",
];

#[derive(Debug, Clone)]
pub struct H3Elem {
    pub prec: u32,
    pub c: [Float; 6],
}

impl H3Elem {
    pub fn zero(prec: u32) -> Self {
        Self {
            prec,
            c: std::array::from_fn(|_| Float::with_val(prec, 0)),
        }
    }

    pub fn one(prec: u32) -> Self {
        let mut z = Self::zero(prec);
        z.c[0] = Float::with_val(prec, 1);
        z
    }

    pub fn basis(prec: u32, idx: usize) -> Self {
        let mut z = Self::zero(prec);
        z.c[idx] = Float::with_val(prec, 1);
        z
    }

    pub fn scale(&self, s: &Float) -> Self {
        let p = self.prec;
        Self {
            prec: p,
            c: std::array::from_fn(|i| Float::with_val(p, &self.c[i] * s)),
        }
    }

    pub fn add(&self, rhs: &Self) -> Self {
        let p = self.prec;
        Self {
            prec: p,
            c: std::array::from_fn(|i| Float::with_val(p, &self.c[i] + &rhs.c[i])),
        }
    }

    pub fn sub(&self, rhs: &Self) -> Self {
        let p = self.prec;
        Self {
            prec: p,
            c: std::array::from_fn(|i| Float::with_val(p, &self.c[i] - &rhs.c[i])),
        }
    }

    /// Right-multiply by generator `sigma_0` (`sigma_0^2 = 1 + h * sigma_0`, `sigma_0*sigma_1*sigma_0 = e_minus`).
    pub fn mul_sigma0(&self, h: &Float) -> Self {
        let p = self.prec;
        let c = &self.c;
        // 1*s0 = s0
        // s0*s0 = 1 + h*s0
        // s1*s0 = L_-
        // L_+*s0 = e_-
        // L_-*s0 = s1 + h*L_-
        // e_-*s0 = L_+ + h*e_-
        let n0 = c[1].clone();
        let n1 = Float::with_val(p, &c[0] + Float::with_val(p, h * &c[1]));
        let n2 = c[4].clone();
        let n3 = c[5].clone();
        let n4 = Float::with_val(p, &c[2] + Float::with_val(p, h * &c[4]));
        let n5 = Float::with_val(p, &c[3] + Float::with_val(p, h * &c[5]));
        Self {
            prec: p,
            c: [n0, n1, n2, n3, n4, n5],
        }
    }

    /// Right-multiply by generator `sigma_1` (`sigma_1^2 = 1 + h * sigma_1`, `sigma_1*sigma_0*sigma_1 = e_minus`).
    pub fn mul_sigma1(&self, h: &Float) -> Self {
        let p = self.prec;
        let c = &self.c;
        // 1*s1 = s1
        // s0*s1 = L_+
        // s1*s1 = 1 + h*s1
        // L_+*s1 = s0 + h*L_+
        // L_-*s1 = e_-
        // e_-*s1 = L_- + h*e_-
        let n0 = c[2].clone();
        let n1 = c[3].clone();
        let n2 = Float::with_val(p, &c[0] + Float::with_val(p, h * &c[2]));
        let n3 = Float::with_val(p, &c[1] + Float::with_val(p, h * &c[3]));
        let n4 = c[5].clone();
        let n5 = Float::with_val(p, &c[4] + Float::with_val(p, h * &c[5]));
        Self {
            prec: p,
            c: [n0, n1, n2, n3, n4, n5],
        }
    }

    /// Full algebra product in `H_3(q)`.
    pub fn mul(&self, rhs: &Self, h: &Float) -> Self {
        let p = self.prec;
        let b0 = self.clone();
        let b1 = self.mul_sigma0(h);
        let b2 = self.mul_sigma1(h);
        let b3 = b1.mul_sigma1(h); // self * s0 * s1
        let b4 = b2.mul_sigma0(h); // self * s1 * s0
        let b5 = b3.mul_sigma0(h); // self * s0 * s1 * s0
        let bases = [b0, b1, b2, b3, b4, b5];

        let mut acc = Self::zero(p);
        for (k, bk) in bases.iter().enumerate() {
            let rk = &rhs.c[k];
            if !rk.is_zero() {
                for i in 0..6 {
                    acc.c[i] += Float::with_val(p, &bk.c[i] * rk);
                }
            }
        }
        acc
    }

    pub fn pow_u32(&self, exp: u32, h: &Float) -> Self {
        let mut res = Self::one(self.prec);
        let mut base = self.clone();
        let mut e = exp;
        while e > 0 {
            if e & 1 == 1 {
                res = res.mul(&base, h);
            }
            e >>= 1;
            if e > 0 {
                base = base.mul(&base, h);
            }
        }
        res
    }

    /// Ruled photon `gamma(a, b, c_01) = 1 + a*sigma_0 + b*sigma_1 + c_01*(sigma_0*sigma_1^-1)`.
    pub fn photon(params: &Q0Params, a: &Float, b: &Float, c01: &Float) -> Self {
        let p = params.prec_bits;
        let one = Self::one(p);
        let s0 = Self::basis(p, 1);
        let s1 = Self::basis(p, 2);
        let v = Self::vertex_v(params);
        one.add(&s0.scale(a))
            .add(&s1.scale(b))
            .add(&v.scale(c01))
    }

    /// Chiral `γγ` vertex `V = sigma_0 * sigma_1^-1 = sigma_0 * (sigma_1 - h*1) = L_+ - h*sigma_0`.
    pub fn vertex_v(params: &Q0Params) -> Self {
        let p = params.prec_bits;
        let s0 = Self::basis(p, 1);
        let s1_inv = Self::basis(p, 2).sub(&Self::one(p).scale(&params.h));
        s0.mul(&s1_inv, &params.h)
    }

    /// Coordinate sum `net(W) = sum_i c_i`.
    pub fn net(&self) -> Float {
        let mut s = Float::with_val(self.prec, 0);
        for x in &self.c {
            s += x;
        }
        s
    }
}

/// Convention-D Markov trace weights `[1, z_D, z_D, z_D^2, z_D^2, h*z_D^2 + z_D]`.
pub fn trace_weights_h3(params: &Q0Params) -> [Float; 6] {
    let p = params.prec_bits;
    let z = &params.z_d;
    let z2 = Float::with_val(p, z * z);
    let e_tr = Float::with_val(p, Float::with_val(p, &params.h * &z2) + z);
    [
        Float::with_val(p, 1),
        z.clone(),
        z.clone(),
        z2.clone(),
        z2,
        e_tr,
    ]
}

/// 6×6 Convention-D Frobenius Gram matrix `G[i][j] = tr_M(b_i * b_j)` (rank 5, 1D radical).
pub fn gram_matrix_h3(params: &Q0Params) -> [[Float; 6]; 6] {
    let p = params.prec_bits;
    let tw = trace_weights_h3(params);
    std::array::from_fn(|i| {
        let bi = H3Elem::basis(p, i);
        std::array::from_fn(|j| {
            let bj = H3Elem::basis(p, j);
            let prod = bi.mul(&bj, &params.h);
            let mut acc = Float::with_val(p, 0);
            for k in 0..6 {
                acc += Float::with_val(p, &prod.c[k] * &tw[k]);
            }
            acc
        })
    })
}

/// Exact 1D radical of `G`: `[1, -q^-1, -q^-1, q^-2, q^-2, -q^-3]`.
pub fn gram_radical_h3(params: &Q0Params) -> [Float; 6] {
    let p = params.prec_bits;
    let qi = &params.q_inv;
    let qi2 = Float::with_val(p, qi * qi);
    let qi3 = Float::with_val(p, &qi2 * qi);
    let neg_qi = Float::with_val(p, -qi);
    let neg_qi3 = Float::with_val(p, -qi3);
    [
        Float::with_val(p, 1),
        neg_qi.clone(),
        neg_qi,
        qi2.clone(),
        qi2,
        neg_qi3,
    ]
}

/// Linking-neutrality & topological closure summary (`PhotonU1NeutralCut`).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct U1NeutralityInfo {
    pub u1_neutral: bool,
    pub status: String,
    pub closure_components: Option<usize>,
    pub pairwise_linking: Option<Vec<i32>>,
    pub rationale: String,
}

/// Evaluate topological closure components and pairwise algebraic linking numbers of a 3-strand signed braid word
/// (`+1 = sigma_0`, `-1 = sigma_0^-1`, `+2 = sigma_1`, `-2 = sigma_1^-1`).
pub fn analyze_b3_closure(signed_word: &[i32]) -> (usize, Vec<i32>) {
    // Track bottom-to-top permutation and which strand occupies each position.
    // Initially strand s is at position s (s in 0..3).
    let mut pos_to_strand = [0usize, 1, 2];
    let mut cross_sum = [[0i32; 3]; 3];
    for &letter in signed_word {
        let g = (letter.unsigned_abs() as usize) - 1; // 0 or 1
        let sign = if letter > 0 { 1 } else { -1 };
        let s_left = pos_to_strand[g];
        let s_right = pos_to_strand[g + 1];
        cross_sum[s_left][s_right] += sign;
        cross_sum[s_right][s_left] += sign;
        pos_to_strand.swap(g, g + 1);
    }
    // Closure connects top position p to bottom strand p: strand `pos_to_strand[p]` -> `p`.
    let mut next_strand = [0usize; 3];
    for (p, &s) in pos_to_strand.iter().enumerate() {
        next_strand[s] = p;
    }
    let mut comp_of = [usize::MAX; 3];
    let mut n_comp = 0usize;
    for start in 0..3 {
        if comp_of[start] != usize::MAX {
            continue;
        }
        let mut cur = start;
        while comp_of[cur] == usize::MAX {
            comp_of[cur] = n_comp;
            cur = next_strand[cur];
        }
        n_comp += 1;
    }
    let mut lk_pairs = Vec::new();
    for c1 in 0..n_comp {
        for c2 in (c1 + 1)..n_comp {
            let mut sum_signs = 0i32;
            for s1 in 0..3 {
                if comp_of[s1] != c1 {
                    continue;
                }
                for s2 in 0..3 {
                    if comp_of[s2] != c2 {
                        continue;
                    }
                    sum_signs += cross_sum[s1][s2];
                }
            }
            assert_eq!(sum_signs % 2, 0, "sum of inter-component crossings must be even");
            lk_pairs.push(sum_signs / 2);
        }
    }
    lk_pairs.sort();
    (n_comp, lk_pairs)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct H3EvaluatedRow {
    pub id: String,
    pub category: String,
    pub label: String,
    pub word_expr: String,
    pub epistemic_tag: String,
    pub nf_coeffs: [String; 6],
    pub net: String,
    pub tr_m: String,
    pub abs_tr_m: String,
    pub u1_info: U1NeutralityInfo,
    pub chi_3: String,
    pub chi_21: String,
    pub chi_21_norm: String,
    pub chi_111: String,
    pub y_3: String,
    pub y_21: String,
    pub contrib_3: String,
    pub contrib_21: String,
    pub contrib_111: String,
    pub min_two_row_norm_margin_h3: String,
    pub min_all_specht_norm_margin_h3: String,
    pub min_multilevel_reading3_margin: String,
    pub reading3_every_level: bool,
    pub gram_slack: [String; 6],
    pub min_gram_slack: String,
}

/// Evaluate full `H_3(q)` invariants on an `H3Elem`.
pub fn evaluate_h3_elem(
    params: &Q0Params,
    gram: &[[Float; 6]; 6],
    tw: &[Float; 6],
    id: &str,
    category: &str,
    label: &str,
    word_expr: &str,
    epistemic_tag: &str,
    elem: &H3Elem,
    u1_info: U1NeutralityInfo,
    dps: usize,
) -> H3EvaluatedRow {
    let p = params.prec_bits;
    let c = &elem.c;
    let net = elem.net();
    let mut tr_m = Float::with_val(p, 0);
    for k in 0..6 {
        tr_m += Float::with_val(p, &c[k] * &tw[k]);
    }
    let abs_tr_m = Float::with_val(p, tr_m.clone().abs());

    // Specht characters on H_3(q)
    let q = &params.q;
    let q2 = Float::with_val(p, q * q);
    let q3 = Float::with_val(p, &q2 * q);
    let qi = &params.q_inv;
    let qi2 = Float::with_val(p, qi * qi);
    let qi3 = Float::with_val(p, &qi2 * qi);

    // chi^(3) = [1, q, q, q^2, q^2, q^3] (dim 1)
    let chi_3 = Float::with_val(
        p,
        &c[0]
            + Float::with_val(p, q * (&c[1] + &c[2]).complete(p))
            + Float::with_val(p, &q2 * (&c[3] + &c[4]).complete(p))
            + Float::with_val(p, &q3 * &c[5]),
    );
    // chi^(2,1) = [2, h, h, -1, -1, 0] (dim 2)
    let chi_21 = Float::with_val(
        p,
        Float::with_val(p, 2u32 * &c[0])
            + Float::with_val(p, &params.h * (&c[1] + &c[2]).complete(p))
            - Float::with_val(p, &c[3] + &c[4]),
    );
    let chi_21_norm = Float::with_val(p, &chi_21 / 2u32);
    // chi^(1,1,1) = [1, -q^-1, -q^-1, q^-2, q^-2, -q^-3] (dim 1)
    let chi_111 = Float::with_val(
        p,
        &c[0]
            - Float::with_val(p, qi * (&c[1] + &c[2]).complete(p))
            + Float::with_val(p, &qi2 * (&c[3] + &c[4]).complete(p))
            - Float::with_val(p, &qi3 * &c[5]),
    );

    // Convention-D weights y_(3) = (q^4 + 1)/(q^2 + 1)^2, y_(2,1) = q^2/(q^2 + 1)^2, y_(1,1,1) = 0
    let y_3 = params.y_two_row(3, 0);
    let y_21 = params.y_two_row(3, 1);
    let contrib_3 = Float::with_val(p, &y_3 * &chi_3);
    let contrib_21 = Float::with_val(p, &y_21 * &chi_21);

    // Multi-level reading-3 on H_3 -> H_2 -> H_1:
    // E_{3->2}(1)=1, E_{3->2}(s0)=s0, E_{3->2}(s1)=z_D*1, E_{3->2}(L_+)=z_D*s0, E_{3->2}(L_-)=z_D*s0,
    // E_{3->2}(e_-)=z_D*(1 + h*s0).
    let z = &params.z_d;
    let a0 = Float::with_val(
        p,
        &c[0] + Float::with_val(p, z * (&c[2] + &c[5]).complete(p)),
    );
    let a1 = Float::with_val(
        p,
        &c[1]
            + Float::with_val(p, z * (&c[3] + &c[4]).complete(p))
            + Float::with_val(p, z * Float::with_val(p, &params.h * &c[5])),
    );
    let chi_2 = Float::with_val(p, &a0 + Float::with_val(p, q * &a1));
    let chi_11 = Float::with_val(p, &a0 - Float::with_val(p, qi * &a1));
    let chi_1 = tr_m.clone();

    let min_two_row_norm_h3 = if chi_3 < chi_21_norm {
        chi_3.clone()
    } else {
        chi_21_norm.clone()
    };
    let min_all_specht_norm_h3 = if chi_111 < min_two_row_norm_h3 {
        chi_111.clone()
    } else {
        min_two_row_norm_h3.clone()
    };

    // Unnormalized character margin across all two-row levels m = 1, 2, 3 (matching level_chars)
    let mut min_ml = chi_3.clone();
    for cand in [&chi_21, &chi_2, &chi_11, &chi_1] {
        if cand < &min_ml {
            min_ml = cand.clone();
        }
    }
    let neg_tol: Float = -Float::with_val(p, Float::with_val(p, 10).pow(-75i32));
    let reading3_every_level = min_ml >= neg_tol;

    // 6x6 Frobenius Gram slack G * c
    let gram_slack_vals: [Float; 6] = std::array::from_fn(|i| {
        let mut acc = Float::with_val(p, 0);
        for j in 0..6 {
            acc += Float::with_val(p, &gram[i][j] * &c[j]);
        }
        acc
    });
    let mut min_gram = gram_slack_vals[0].clone();
    for v in &gram_slack_vals[1..] {
        if v < &min_gram {
            min_gram = v.clone();
        }
    }

    H3EvaluatedRow {
        id: id.to_string(),
        category: category.to_string(),
        label: label.to_string(),
        word_expr: word_expr.to_string(),
        epistemic_tag: epistemic_tag.to_string(),
        nf_coeffs: std::array::from_fn(|i| fmt_dps(&c[i], dps)),
        net: fmt_dps(&net, dps),
        tr_m: fmt_dps(&tr_m, dps),
        abs_tr_m: fmt_dps(&abs_tr_m, dps),
        u1_info,
        chi_3: fmt_dps(&chi_3, dps),
        chi_21: fmt_dps(&chi_21, dps),
        chi_21_norm: fmt_dps(&chi_21_norm, dps),
        chi_111: fmt_dps(&chi_111, dps),
        y_3: fmt_dps(&y_3, dps),
        y_21: fmt_dps(&y_21, dps),
        contrib_3: fmt_dps(&contrib_3, dps),
        contrib_21: fmt_dps(&contrib_21, dps),
        contrib_111: "0".to_string(),
        min_two_row_norm_margin_h3: fmt_dps(&min_two_row_norm_h3, dps),
        min_all_specht_norm_margin_h3: fmt_dps(&min_all_specht_norm_h3, dps),
        min_multilevel_reading3_margin: fmt_dps(&min_ml, dps),
        reading3_every_level,
        gram_slack: std::array::from_fn(|i| fmt_dps(&gram_slack_vals[i], dps)),
        min_gram_slack: fmt_dps(&min_gram, dps),
    }
}

/// Exact Pair-Skein Convention-D & Symbolic Charge-Dressed Split invariants (`A = 1` supplements).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HadronA1Supplements {
    /// `kappa_D = (q^4 + 1) / (q * (q^2 + 1))` (`PairSkeinMassConventionD`).
    pub pair_skein_kappa_d: String,
    /// `S_{uu}` (`mu_u = 0`), `S_{ud}`, `S_{dd}` (`mu_d = 1` unit, symbolic slope in `Delta_q`).
    pub pair_skein_s_uu_unit: String,
    pub pair_skein_s_ud_unit: String,
    pub pair_skein_s_du_unit: String,
    pub pair_skein_s_dd_unit: String,
    /// Production `tr_M(uud) - tr_M(udd)` at `q_0^(p)`.
    pub tr_m_proton_minus_neutron: String,
    /// Symbolic charge-dressed invariants (`NucleonChargeDressedWords.lean`):
    /// `G_1(q) = q^8 - 2q^6 + 2q^4 - q^2 + 1 > 0`, `G_2(q) = q^8 - 3q^6 + 4q^4 - 2q^2 + 1 > 0`,
    /// first-order slope `d/dc (tr(w_n) - tr(w_p))|_{c=0} = 3*(a - b)*(a*G_1(q) + b*G_2(q)) / q^6`
    /// evaluated at `a = 2/3, b = -1/3` (coupling `c` undetermined).
    pub charge_dressed_g1: String,
    pub charge_dressed_g2: String,
    pub charge_dressed_first_order_slope_n_minus_p: String,
    pub charge_dressed_coupling_c: Option<String>,
}

pub fn build_all_h3_rows(
    params: &Q0Params,
    dps: usize,
) -> (Vec<(H3Elem, H3EvaluatedRow)>, HadronA1Supplements) {
    let p = params.prec_bits;
    let zero = Float::with_val(p, 0);
    let half = Float::with_val(p, 1) / 2u32;
    let h = &params.h;
    let qh = Float::with_val(p, &params.q * h);
    let neg_h_over_q = -Float::with_val(p, h * &params.q_inv);

    let gram = gram_matrix_h3(params);
    let tw = trace_weights_h3(params);

    let one = H3Elem::one(p);
    let s0 = H3Elem::basis(p, 1);
    let s1 = H3Elem::basis(p, 2);
    let v = H3Elem::vertex_v(params);
    let v2 = v.pow_u32(2, h);
    let v3 = v.pow_u32(3, h);
    let v6 = v.pow_u32(6, h);

    let gamma_plus = H3Elem::photon(params, &zero, &zero, &qh);
    let gamma_minus = H3Elem::photon(params, &zero, &zero, &neg_h_over_q);
    let gamma_plus_4 = gamma_plus.pow_u32(4, h);
    let gamma_minus_4 = gamma_minus.pow_u32(4, h);

    // Charged pion pi^+- = sigma_0^2 = 1 + h*sigma_0
    let pion = s0.pow_u32(2, h);

    // Production 11-letter proton (uud) and neutron (udd) in H_3(q) (`pyhecke.atom` / `hecke_flint.py`):
    // proton:  V^3 * s0 * (s0 - h/2) * (s1 - h/2) * s0 * s0
    // neutron: V^3 * (s0 - h/2) * (s0 - h/2) * (s1 - h) * s0 * s0
    let half_h = Float::with_val(p, &params.h * &half);
    let a_s0 = s0.sub(&one.scale(&half_h));
    let a_s1 = s1.sub(&one.scale(&half_h));
    let i_s1 = s1.sub(&one.scale(h));
    let s0_sq = s0.mul(&s0, h);

    let proton_uud = v3
        .mul(&s0, h)
        .mul(&a_s0, h)
        .mul(&a_s1, h)
        .mul(&s0_sq, h);
    let neutron_udd = v3
        .mul(&a_s0, h)
        .mul(&a_s0, h)
        .mul(&i_s1, h)
        .mul(&s0_sq, h);

    let braid_u1 = |word: &[i32], note: &str| -> U1NeutralityInfo {
        let (nc, lk) = analyze_b3_closure(word);
        let neutral = nc == 1 || lk.iter().all(|&x| x == 0);
        U1NeutralityInfo {
            u1_neutral: neutral,
            status: if neutral {
                if nc == 1 {
                    "knot_1_component_neutral".to_string()
                } else {
                    "link_all_pairwise_lk_zero".to_string()
                }
            } else {
                "non_neutral_nonzero_linking".to_string()
            },
            closure_components: Some(nc),
            pairwise_linking: Some(lk),
            rationale: note.to_string(),
        }
    };

    let specs: Vec<(&str, &str, &str, &str, &str, H3Elem, U1NeutralityInfo)> = vec![
        (
            "photon_bare",
            "photonic_4photon",
            "\\gamma(0,0,0)",
            "1",
            "Theorem",
            one.clone(),
            braid_u1(&[], "3-component unlink; all pairwise linking numbers vanish"),
        ),
        (
            "photon_switched_plus",
            "photonic_4photon",
            "\\gamma_+ = \\gamma(0,0,qh)",
            "1 + q h V",
            "Theorem",
            gamma_plus,
            U1NeutralityInfo {
                u1_neutral: true,
                status: "termwise_linking_neutral".to_string(),
                closure_components: None,
                pairwise_linking: None,
                rationale: "Both braid summands 1 (3-unlink, lk=0) and V = sigma_0*sigma_1^-1 (1-component unknot) pass term-by-term linking neutrality".to_string(),
            },
        ),
        (
            "photon_switched_minus",
            "photonic_4photon",
            "\\gamma_- = \\gamma(0,0,-q^{-1}h)",
            "1 - q^{-1} h V",
            "Theorem",
            gamma_minus,
            U1NeutralityInfo {
                u1_neutral: true,
                status: "termwise_linking_neutral".to_string(),
                closure_components: None,
                pairwise_linking: None,
                rationale: "Both braid summands 1 (3-unlink, lk=0) and V = sigma_0*sigma_1^-1 (1-component unknot) pass term-by-term linking neutrality".to_string(),
            },
        ),
        (
            "vertex_v1",
            "photonic_4photon",
            "V",
            "\\sigma_0 \\sigma_1^{-1}",
            "Theorem",
            v.clone(),
            braid_u1(&[1, -2], "Single chiral vertex closes to 1-component unknot"),
        ),
        (
            "vertex_v2",
            "photonic_4photon",
            "V^2",
            "(\\sigma_0 \\sigma_1^{-1})^2",
            "Theorem",
            v2,
            braid_u1(&[1, -2, 1, -2], "Double chiral vertex closes to 1-component figure-eight knot 4_1"),
        ),
        (
            "nucleon_bare_v3",
            "hadron_a1",
            "\\beta_{\\mathrm{Bor}} = V^3 = \\gamma_+\\gamma_-",
            "(\\sigma_0 \\sigma_1^{-1})^3",
            "Theorem",
            v3.clone(),
            braid_u1(
                &[1, -2, 1, -2, 1, -2],
                "Borromean rings L6a4 (3 components, pairwise lk = [0, 0, 0]); unique linking-neutral two-photon factorisation gamma_+ * gamma_-",
            ),
        ),
        (
            "four_photon_switched_v6",
            "photonic_4photon",
            "(\\gamma_+\\gamma_-)^2 = V^6",
            "(\\sigma_0 \\sigma_1^{-1})^6",
            "Theorem",
            v6,
            braid_u1(
                &[1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2],
                "Switched 4-photon state V^6 (3 components, pairwise lk = [0, 0, 0])",
            ),
        ),
        (
            "four_photon_chiral_plus4",
            "photonic_4photon",
            "\\gamma_+^4",
            "(1 + q h V)^4",
            "Theorem",
            gamma_plus_4,
            U1NeutralityInfo {
                u1_neutral: true,
                status: "termwise_linking_neutral".to_string(),
                closure_components: None,
                pairwise_linking: None,
                rationale: "Every power V^k (k = 0..4) is linking-neutral (1, V^3 have lk = [0,0,0]; V, V^2, V^4 are 1-component knots)".to_string(),
            },
        ),
        (
            "four_photon_chiral_minus4",
            "photonic_4photon",
            "\\gamma_-^4",
            "(1 - q^{-1} h V)^4",
            "Theorem",
            gamma_minus_4,
            U1NeutralityInfo {
                u1_neutral: true,
                status: "termwise_linking_neutral".to_string(),
                closure_components: None,
                pairwise_linking: None,
                rationale: "Every power V^k (k = 0..4) is linking-neutral (1, V^3 have lk = [0,0,0]; V, V^2, V^4 are 1-component knots)".to_string(),
            },
        ),
        (
            "meson_pion_charged",
            "hadron_a1",
            "\\pi^\\pm",
            "\\sigma_0^2 = 1 + h \\sigma_0",
            "Conditional",
            pion,
            braid_u1(
                &[1, 1],
                "Hopf link plus spectator unknot in B_3 (3 components, pairwise lk = [0, 0, +1]); charged state fails U(1) linking neutrality",
            ),
        ),
        (
            "nucleon_proton_uud",
            "hadron_a1",
            "\\mathfrak{p}\\ (uud)",
            "V^3 \\sigma_0 (\\sigma_0 - \\tfrac{h}{2})(\\sigma_1 - \\tfrac{h}{2}) \\sigma_0^2",
            "Conditional",
            proton_uud,
            U1NeutralityInfo {
                u1_neutral: false,
                status: "flavoured_skein_superposition".to_string(),
                closure_components: None,
                pairwise_linking: None,
                rationale: "Typed 11-letter skein element with fractional -h/2 flavour projectors; outside pure γγ linking-neutral cut".to_string(),
            },
        ),
        (
            "nucleon_neutron_udd",
            "hadron_a1",
            "\\mathfrak{n}\\ (udd)",
            "V^3 (\\sigma_0 - \\tfrac{h}{2})^2 (\\sigma_1 - h) \\sigma_0^2",
            "Conditional",
            neutron_udd,
            U1NeutralityInfo {
                u1_neutral: false,
                status: "flavoured_skein_superposition".to_string(),
                closure_components: None,
                pairwise_linking: None,
                rationale: "Typed 11-letter skein element with fractional -h/2 flavour projectors; outside pure γγ linking-neutral cut".to_string(),
            },
        ),
    ];

    let mut out = Vec::with_capacity(specs.len());
    let mut tr_p = Float::with_val(p, 0);
    let mut tr_n = Float::with_val(p, 0);
    for (id, cat, lbl, expr, tag, elem, u1) in specs {
        let row = evaluate_h3_elem(params, &gram, &tw, id, cat, lbl, expr, tag, &elem, u1, dps);
        if id == "nucleon_proton_uud" {
            for k in 0..6 {
                tr_p += Float::with_val(p, &elem.c[k] * &tw[k]);
            }
        } else if id == "nucleon_neutron_udd" {
            for k in 0..6 {
                tr_n += Float::with_val(p, &elem.c[k] * &tw[k]);
            }
        }
        out.push((elem, row));
    }

    // Supplements: PairSkeinMassConventionD & NucleonChargeDressedWords
    let q = &params.q;
    let q2 = Float::with_val(p, q * q);
    let q3 = Float::with_val(p, &q2 * q);
    let q4 = Float::with_val(p, &q2 * &q2);
    let q6 = Float::with_val(p, &q4 * &q2);
    let q8 = Float::with_val(p, &q4 * &q4);
    let one_f = Float::with_val(p, 1);
    let q2_p1 = Float::with_val(p, &q2 + &one_f);

    let kappa_d = Float::with_val(
        p,
        Float::with_val(p, &q4 + &one_f) / Float::with_val(p, q * &q2_p1),
    );
    // Unit pair-skein coefficients S_{ab} = (q^3 * mu_a + q^-1 * mu_b) / (q^2 + 1) at (mu_u = 0, mu_d = 1)
    let s_uu = Float::with_val(p, 0);
    let s_ud = Float::with_val(p, &params.q_inv / &q2_p1);
    let s_du = Float::with_val(p, &q3 / &q2_p1);
    let s_dd = Float::with_val(p, Float::with_val(p, &q3 + &params.q_inv) / &q2_p1);

    // G_1(q) = q^8 - 2q^6 + 2q^4 - q^2 + 1
    let g1 = Float::with_val(
        p,
        &q8 - Float::with_val(p, 2u32 * &q6) + Float::with_val(p, 2u32 * &q4) - &q2 + &one_f,
    );
    // G_2(q) = q^8 - 3q^6 + 4q^4 - 2q^2 + 1
    let g2 = Float::with_val(
        p,
        &q8 - Float::with_val(p, 3u32 * &q6) + Float::with_val(p, 4u32 * &q4)
            - Float::with_val(p, 2u32 * &q2)
            + &one_f,
    );
    // At a = 2/3, b = -1/3: 3*(a - b)*(a*G_1 + b*G_2) / q^6 = 3 * 1 * ((2*G_1 - G_2)/3) / q^6 = (2*G_1 - G_2) / q^6
    let slope_np = Float::with_val(
        p,
        Float::with_val(p, Float::with_val(p, 2u32 * &g1) - &g2) / &q6,
    );
    let tr_diff_pn = Float::with_val(p, &tr_p - &tr_n);

    let supp = HadronA1Supplements {
        pair_skein_kappa_d: fmt_dps(&kappa_d, dps),
        pair_skein_s_uu_unit: fmt_dps(&s_uu, dps),
        pair_skein_s_ud_unit: fmt_dps(&s_ud, dps),
        pair_skein_s_du_unit: fmt_dps(&s_du, dps),
        pair_skein_s_dd_unit: fmt_dps(&s_dd, dps),
        tr_m_proton_minus_neutron: fmt_dps(&tr_diff_pn, dps),
        charge_dressed_g1: fmt_dps(&g1, dps),
        charge_dressed_g2: fmt_dps(&g2, dps),
        charge_dressed_first_order_slope_n_minus_p: fmt_dps(&slope_np, dps),
        charge_dressed_coupling_c: None,
    };

    (out, supp)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scalars::parse_dec;

    #[test]
    fn h3_associativity_and_borromean_two_photon_factorisation() {
        let params = Q0Params::proton_pinned(320, None);
        let p = params.prec_bits;
        let h = &params.h;
        let tol = parse_dec(p, "1e-88");

        // All 6^3 = 216 basis triples associative
        for i in 0..6 {
            let bi = H3Elem::basis(p, i);
            for j in 0..6 {
                let bj = H3Elem::basis(p, j);
                let ij = bi.mul(&bj, h);
                for k in 0..6 {
                    let bk = H3Elem::basis(p, k);
                    let lhs = ij.mul(&bk, h);
                    let rhs = bi.mul(&bj.mul(&bk, h), h);
                    for c in 0..6 {
                        let d = (lhs.c[c].clone() - &rhs.c[c]).abs();
                        assert!(d < tol, "non-associative at ({i},{j},{k}) coord {c}: {d}");
                    }
                }
            }
        }

        // Verify gamma(0,0,qh) * gamma(0,0,-h/q) == V^3
        let zero = Float::with_val(p, 0);
        let qh = Float::with_val(p, &params.q * h);
        let neg_hq: Float = -Float::with_val(p, h * &params.q_inv);
        let gp = H3Elem::photon(&params, &zero, &zero, &qh);
        let gm = H3Elem::photon(&params, &zero, &zero, &neg_hq);
        let prod = gp.mul(&gm, h);
        let v3 = H3Elem::vertex_v(&params).pow_u32(3, h);
        for c in 0..6 {
            let d = (prod.c[c].clone() - &v3.c[c]).abs();
            assert!(d < tol, "gamma_+ * gamma_- != V^3 at coord {c}: {d}");
        }

        // Verify Gram radical G * r_alt == 0
        let g = gram_matrix_h3(&params);
        let r = gram_radical_h3(&params);
        for i in 0..6 {
            let mut s = Float::with_val(p, 0);
            for j in 0..6 {
                s += Float::with_val(p, &g[i][j] * &r[j]);
            }
            assert!(s.clone().abs() < tol, "G * radical != 0 at row {i}: {s}");
        }
    }
}
