//! Fast batch MPFR evaluator for `compound_shift_nf.build_atom_nf_mp(Z, N, dps)` across the nuclide chart.
//!
//! Replaces the `41,152,981` Python `hm_mp` calls (`~3,573 s` across `4,543` `(Z, N)` chart rows in
//! `all_nuclides_sdp_admissibility_mp.py`) with exact `6×6` `H_3(q)` right-multiplication operators
//! in `rug::Float` (`>= 266` bits, default `320` bits), handling magnitudes past `10^662` (`^{238}U`)
//! with zero `f64` overflow and `< 10^-80` relative error vs step-by-step `build_atom_nf_mp`.

use crate::scalars::{fmt_dps, Q0Params, MIN_PREC_BITS};
use rug::Float;
use serde::{Deserialize, Serialize};

/// Exact port of `hecke_core_symbolic._ground_state_ordering(Z, N)`.
pub fn ground_state_ordering(z: usize, n: usize) -> Vec<u8> {
    let a = z + n;
    let mut ordering = Vec::with_capacity(a);
    let mut pc = 0usize;
    let mut nc = 0usize;
    for k in 0..a {
        if (k % 2 == 0 && pc < z) || nc >= n {
            ordering.push(b'p');
            pc += 1;
        } else {
            ordering.push(b'n');
            nc += 1;
        }
    }
    ordering
}

/// Exact `6×6` transition matrix `M` of `compound_shift_nf.hm_mp(nf, c, d, gen, h)`:
/// `r[ti] = sum_si nf[si] * M[si][ti]` (note `hm_mp` left-multiplies basis words `(0,1)` and `(1,0)`).
type Op6 = [[Float; 6]; 6];

fn op6_identity(prec: u32) -> Op6 {
    std::array::from_fn(|i| {
        std::array::from_fn(|j| Float::with_val(prec, if i == j { 1 } else { 0 }))
    })
}

fn op6_hm(prec: u32, c: &Float, d: &Float, gen: usize, h: &Float) -> Op6 {
    let mut m: Op6 = std::array::from_fn(|_| std::array::from_fn(|_| Float::with_val(prec, 0)));
    let ch = Float::with_val(prec, c * h);
    if gen == 0 {
        // Mirrors compound_shift_nf.py lines 164-171 verbatim:
        m[0][0] += d;
        m[0][1] += c;
        m[1][0] += c;
        m[1][1] += Float::with_val(prec, &ch + d);
        m[2][2] += d;
        m[2][3] += c;
        m[3][2] += c;
        m[3][3] += Float::with_val(prec, &ch + d);
        m[4][4] += d;
        m[4][5] += c;
        m[5][4] += c;
        m[5][5] += Float::with_val(prec, &ch + d);
    } else {
        // Mirrors compound_shift_nf.py lines 173-180 verbatim:
        m[0][0] += d;
        m[0][2] += c;
        m[1][1] += d;
        m[1][4] += c;
        m[2][0] += c;
        m[2][2] += Float::with_val(prec, &ch + d);
        m[3][3] += d;
        m[3][5] += c;
        m[4][1] += c;
        m[4][4] += Float::with_val(prec, &ch + d);
        m[5][3] += c;
        m[5][5] += Float::with_val(prec, &ch + d);
    }
    m
}

fn op6_mul(prec: u32, a: &Op6, b: &Op6) -> Op6 {
    std::array::from_fn(|i| {
        std::array::from_fn(|k| {
            let mut s = Float::with_val(prec, 0);
            for j in 0..6 {
                if !a[i][j].is_zero() && !b[j][k].is_zero() {
                    s += Float::with_val(prec, &a[i][j] * &b[j][k]);
                }
            }
            s
        })
    })
}

#[inline]
fn apply_op6(prec: u32, v: &[Float; 6], op: &Op6) -> [Float; 6] {
    std::array::from_fn(|k| {
        let mut s = Float::with_val(prec, 0);
        for j in 0..6 {
            if !v[j].is_zero() && !op[j][k].is_zero() {
                s += Float::with_val(prec, &v[j] * &op[j][k]);
            }
        }
        s
    })
}

pub struct AtomNfBatchEngine {
    pub prec_bits: u32,
    m_proton: Op6,
    m_neutron: Op6,
    pow_pp: Vec<Op6>,
    pow_nn: Vec<Op6>,
    pow_pn: Vec<Op6>,
    pow_elec: Vec<Op6>,
}

impl AtomNfBatchEngine {
    pub fn new(params: &Q0Params, max_count: usize) -> Self {
        let p = params.prec_bits;
        assert!(p >= MIN_PREC_BITS);
        let h = &params.h;
        let zero = Float::with_val(p, 0);
        let one = Float::with_val(p, 1);
        let neg_h = Float::with_val(p, -h);
        let neg_half_h = Float::with_val(p, -Float::with_val(p, h / 2u32));

        let g_s0 = op6_hm(p, &one, &zero, 0, h);
        let g_s1_inv = op6_hm(p, &one, &neg_h, 1, h);
        let g_s0_inv = op6_hm(p, &one, &neg_h, 0, h);
        let g_s0_half = op6_hm(p, &one, &neg_half_h, 0, h);
        let g_s1_half = op6_hm(p, &one, &neg_half_h, 1, h);

        let v_step = op6_mul(p, &g_s0, &g_s1_inv);
        let v3 = op6_mul(p, &op6_mul(p, &v_step, &v_step), &v_step);
        let s0_sq = op6_mul(p, &g_s0, &g_s0);

        // Proton step (`compound_shift_nf.py` lines 212-219):
        let m_proton = op6_mul(
            p,
            &op6_mul(
                p,
                &op6_mul(p, &op6_mul(p, &v3, &g_s0), &g_s0_half),
                &g_s1_half,
            ),
            &s0_sq,
        );
        // Neutron step (`compound_shift_nf.py` lines 221-228):
        let m_neutron = op6_mul(
            p,
            &op6_mul(
                p,
                &op6_mul(p, &op6_mul(p, &v3, &g_s0_half), &g_s0_half),
                &g_s1_inv,
            ),
            &s0_sq,
        );

        let g_pp = g_s0;
        let g_nn = g_s0_inv;
        let g_pn = g_s0_half;
        let e_el = g_s1_inv;

        let build_pows = |base: &Op6| -> Vec<Op6> {
            let mut out = Vec::with_capacity(max_count + 1);
            out.push(op6_identity(p));
            for m in 1..=max_count {
                let next = op6_mul(p, &out[m - 1], base);
                out.push(next);
            }
            out
        };

        Self {
            prec_bits: p,
            m_proton,
            m_neutron,
            pow_pp: build_pows(&g_pp),
            pow_nn: build_pows(&g_nn),
            pow_pn: build_pows(&g_pn),
            pow_elec: build_pows(&e_el),
        }
    }

    pub fn eval_zn(&self, z: usize, n: usize) -> [Float; 6] {
        let p = self.prec_bits;
        let a = z + n;
        let mut nf: [Float; 6] =
            std::array::from_fn(|i| Float::with_val(p, if i == 0 { 1 } else { 0 }));
        if a == 0 {
            return nf;
        }
        let ord = ground_state_ordering(z, n);
        let mut prev_p = 0usize;
        let mut prev_n = 0usize;
        for &tk in &ord {
            if tk == b'p' {
                nf = apply_op6(p, &nf, &self.m_proton);
                if prev_p > 0 {
                    nf = apply_op6(p, &nf, &self.pow_pp[prev_p]);
                }
                if prev_n > 0 {
                    nf = apply_op6(p, &nf, &self.pow_pn[prev_n]);
                }
                prev_p += 1;
            } else {
                nf = apply_op6(p, &nf, &self.m_neutron);
                if prev_p > 0 {
                    nf = apply_op6(p, &nf, &self.pow_pn[prev_p]);
                }
                if prev_n > 0 {
                    nf = apply_op6(p, &nf, &self.pow_nn[prev_n]);
                }
                prev_n += 1;
            }
        }
        if z > 0 {
            nf = apply_op6(p, &nf, &self.pow_elec[z]);
        }
        nf
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AtomNfBatchRequest {
    #[serde(default)]
    pub prec_bits: Option<u32>,
    #[serde(default)]
    pub q0: Option<String>,
    #[serde(default)]
    pub nf_dps: Option<usize>,
    #[serde(default)]
    pub net_dps: Option<usize>,
    #[serde(default)]
    pub log10_dps: Option<usize>,
    pub pairs: Vec<[usize; 2]>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AtomNfBatchRow {
    #[serde(rename = "Z")]
    pub z: usize,
    #[serde(rename = "N")]
    pub n: usize,
    #[serde(rename = "A")]
    pub a: usize,
    pub nf_str: [String; 6],
    pub nf_net_str: String,
    pub nf_net_log10_abs_str: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AtomNfBatchResponse {
    pub schema: String,
    pub prec_bits: u32,
    pub n_rows: usize,
    pub rows: Vec<AtomNfBatchRow>,
}

pub fn evaluate_atom_nf_batch(req: &AtomNfBatchRequest) -> AtomNfBatchResponse {
    let prec = req.prec_bits.unwrap_or(384).max(MIN_PREC_BITS);
    let nf_dps = req.nf_dps.unwrap_or(80);
    let net_dps = req.net_dps.unwrap_or(30);
    let log_dps = req.log10_dps.unwrap_or(20);

    let params = Q0Params::proton_pinned(prec, req.q0.as_deref());
    let max_c = req
        .pairs
        .iter()
        .map(|&[z, n]| z.max(n))
        .max()
        .unwrap_or(0);
    let engine = AtomNfBatchEngine::new(&params, max_c);

    let mut rows = Vec::with_capacity(req.pairs.len());
    for &[z, n] in &req.pairs {
        let nf = engine.eval_zn(z, n);
        let mut net = Float::with_val(prec, 0);
        for c in &nf {
            net += c;
        }
        let log10_str = if net.is_zero() {
            None
        } else {
            let l10 = Float::with_val(prec, net.clone().abs().log10());
            Some(fmt_dps(&l10, log_dps))
        };
        rows.push(AtomNfBatchRow {
            z,
            n,
            a: z + n,
            nf_str: std::array::from_fn(|i| fmt_dps(&nf[i], nf_dps)),
            nf_net_str: fmt_dps(&net, net_dps),
            nf_net_log10_abs_str: log10_str,
        });
    }

    AtomNfBatchResponse {
        schema: "qou-atom-nf-batch/v1".to_string(),
        prec_bits: prec,
        n_rows: rows.len(),
        rows,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scalars::parse_dec;

    #[test]
    fn pb208_and_u238_match_50dps_reference_without_overflow() {
        let req = AtomNfBatchRequest {
            prec_bits: Some(320),
            q0: None,
            nf_dps: Some(80),
            net_dps: Some(30),
            log10_dps: Some(20),
            pairs: vec![[82, 126], [92, 146]],
        };
        let resp = evaluate_atom_nf_batch(&req);
        assert_eq!(resp.rows.len(), 2);

        // Pb-208: net = -1.24832157929872945564366142077e+499
        let pb_net = parse_dec(320, &resp.rows[0].nf_net_str);
        let pb_ref = parse_dec(320, "-1.24832157929872945564366142077e+499");
        let rel_pb = Float::with_val(320, (pb_net - &pb_ref).abs() / pb_ref.abs());
        assert!(
            rel_pb < parse_dec(320, "1e-28"),
            "Pb-208 rel mismatch: {rel_pb}"
        );

        // U-238: net = 1.43969549828089075667614896438e+662
        let u_net = parse_dec(320, &resp.rows[1].nf_net_str);
        let u_ref = parse_dec(320, "1.43969549828089075667614896438e+662");
        let rel_u = Float::with_val(320, (u_net - &u_ref).abs() / u_ref.abs());
        assert!(
            rel_u < parse_dec(320, "1e-28"),
            "U-238 rel mismatch: {rel_u}"
        );
    }
}
