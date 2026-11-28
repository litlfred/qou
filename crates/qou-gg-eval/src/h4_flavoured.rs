//! 4-strand `H_4(q)` flavoured `γγ` nucleon census and 8-strand Reading-D junction ratios (`3B`).
//!
//! Enumerates all `2^1 + ... + 2^6 = 126` words in `{V(0), V(1)}` on 4 strands, filters by
//! multi-level reading-3 positivity (`m = 1..4`), and evaluates:
//! - **Reading A**: exact 24-element `H_4(q)` Coxeter normal form coordinate sum (`A1`),
//!   `E_{4->3}` at `z = 1` coordinate sum (`A2`), and `E_{4->3}` at `z = z_D` coordinate sum (`A3`),
//!   compared against `net(p) = 1 - h/2` and `net(n) = 1 - 3h/2 + h^2/2`;
//! - **Reading B**: exact word-reversal & bar-involution (`h -> -h`, `sigma_i -> sigma_i^-1`)
//!   conjugacy among the passing 4-strand words;
//! - **Reading D**: all ordered pairs `(w_1, w_2)` on 8 strands (`w_1` on gens `0..2`, `w_2` shifted
//!   by `+4` on gens `4..6`) bonded by `V(s)^k` (`s in {3, 2}`, `k in {1, 2, 3}`), checking reading 3
//!   at every level `m = 1..8` and reporting exact 80-dps trace ratios & unfitted `-E_0 ln r`
//!   (both order-zero `E_0^(0)` matching `gg_deuteron_flavoured_probe.py` and canonical `E_0^tower`).

use crate::h3::{trace_weights_h3, H3Elem};
use crate::scalars::{fmt_dps, parse_dec, Q0Params, AME2020_B_2H_MEV};
use crate::tower_gt::{HeckeLetter, TwoRowTowerRep};
use rug::Float;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Exact element of `H_4(q)` in the 24-element Coxeter basis `{T_w : w in S_4}`.
#[derive(Debug, Clone)]
pub struct H4Elem {
    pub prec: u32,
    pub perms: Vec<[u8; 4]>,
    pub c: [Float; 24],
}

fn all_s4_perms() -> Vec<[u8; 4]> {
    let mut out = Vec::with_capacity(24);
    for a in 0..4u8 {
        for b in 0..4u8 {
            if b == a {
                continue;
            }
            for c in 0..4u8 {
                if c == a || c == b {
                    continue;
                }
                let d = 6 - a - b - c;
                out.push([a, b, c, d]);
            }
        }
    }
    out
}

impl H4Elem {
    pub fn one(prec: u32, perms: &[[u8; 4]], idx_map: &HashMap<[u8; 4], usize>) -> Self {
        let mut c: [Float; 24] = std::array::from_fn(|_| Float::with_val(prec, 0));
        let id_idx = idx_map[&[0, 1, 2, 3]];
        c[id_idx] = Float::with_val(prec, 1);
        Self {
            prec,
            perms: perms.to_vec(),
            c,
        }
    }

    /// Right-multiply by `HeckeLetter` on `g in {0, 1, 2}`.
    pub fn mul_letter(&self, lt: HeckeLetter, h: &Float, idx_map: &HashMap<[u8; 4], usize>) -> Self {
        let p = self.prec;
        let (g, inv) = match lt {
            HeckeLetter::Pos(g) => (g, false),
            HeckeLetter::Inv(g) => (g, true),
            HeckeLetter::Half(_) => panic!("Half letter not used in pure γγ H_4 words"),
        };
        let mut out: [Float; 24] = std::array::from_fn(|_| Float::with_val(p, 0));
        for (idx, w) in self.perms.iter().enumerate() {
            let coeff = &self.c[idx];
            if coeff.is_zero() {
                continue;
            }
            if inv {
                out[idx] -= Float::with_val(p, coeff * h);
            }
            let up = w[g] < w[g + 1];
            let mut u = *w;
            u.swap(g, g + 1);
            let u_idx = idx_map[&u];
            out[u_idx] += coeff;
            if !up {
                out[idx] += Float::with_val(p, coeff * h);
            }
        }
        Self {
            prec: p,
            perms: self.perms.clone(),
            c: out,
        }
    }

    pub fn net_h4(&self) -> Float {
        let mut s = Float::with_val(self.prec, 0);
        for v in &self.c {
            s += v;
        }
        s
    }

    /// Apply conditional expectation `E_{4->3}(z): H_4(q) -> H_3(q)` (`E(a * sigma_2 * b) = z * a * b`).
    pub fn project_to_h3(&self, z: &Float, h: &Float) -> H3Elem {
        let p = self.prec;
        let mut acc = H3Elem::zero(p);

        // Map S_3 perm [a, b, c] to H3Elem basis index:
        // [0,1,2]->0 (1), [1,0,2]->1 (s0), [0,2,1]->2 (s1),
        // [1,2,0]->3? Let's check: 1 * s0 * s1: [0,1,2] -> s0 swaps pos 0,1 -> [1,0,2] -> s1 swaps pos 1,2 -> [1,2,0] = L_+ (idx 3)!
        // [2,0,1]: 1 * s1 * s0: [0,1,2] -> [0,2,1] -> [2,0,1] = L_- (idx 4)!
        // [2,1,0]: e_- (idx 5)!
        let s3_basis_idx = |w3: [u8; 3]| -> usize {
            match w3 {
                [0, 1, 2] => 0,
                [1, 0, 2] => 1,
                [0, 2, 1] => 2,
                [1, 2, 0] => 3,
                [2, 0, 1] => 4,
                [2, 1, 0] => 5,
                _ => unreachable!("invalid S_3 perm {w3:?}"),
            }
        };

        for (idx, w) in self.perms.iter().enumerate() {
            let coeff = &self.c[idx];
            if coeff.is_zero() {
                continue;
            }
            if w[3] == 3 {
                let b_idx = s3_basis_idx([w[0], w[1], w[2]]);
                acc.c[b_idx] += coeff;
            } else {
                let pos3 = w.iter().position(|&x| x == 3).unwrap(); // 0, 1, or 2
                let mut rem = Vec::with_capacity(3);
                for (k, &val) in w.iter().enumerate() {
                    if k != pos3 {
                        rem.push(val);
                    }
                }
                let b_idx = s3_basis_idx([rem[0], rem[1], rem[2]]);
                let mut elem = H3Elem::basis(p, b_idx);
                // T_w = T_{w_0} * sigma_2 * sigma_1 * ... * sigma_{pos3}
                // E_{4->3}(z)(T_w) = z * T_{w_0} * sigma_1 * ... * sigma_{pos3}
                for g in (pos3..=1).rev() {
                    elem = if g == 0 {
                        elem.mul_sigma0(h)
                    } else {
                        elem.mul_sigma1(h)
                    };
                }
                let scaled = elem.scale(&Float::with_val(p, coeff * z));
                acc = acc.add(&scaled);
            }
        }
        acc
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct H4NucleonWordRow {
    pub word: String,
    pub n_vertices: usize,
    pub tr_m: String,
    pub min_level_char: String,
    pub net_a1_h4: String,
    pub net_a2_e4to3_z1: String,
    pub net_a3_e4to3_zd: String,
    pub abs_diff_a3_vs_proton_net: String,
    pub abs_diff_a3_vs_neutron_net: String,
    pub site_swap_partner: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct H8FlavouredAtomRow {
    pub w1: String,
    pub w2: String,
    pub bond: String,
    pub ratio: String,
    pub b_order_zero_mev: Option<String>,
    pub b_tower_mev: Option<String>,
    pub b_err_vs_ame_order_zero_pct: Option<String>,
    pub b_err_vs_ame_tower_pct: Option<String>,
    pub min_level_char: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct H4FlavouredCensusReport {
    pub max_vertices: usize,
    pub n_candidates_h4: usize,
    pub n_passing_nucleon_words: usize,
    pub proton_production_net_target: String,
    pub neutron_production_net_target: String,
    pub nucleon_words: Vec<H4NucleonWordRow>,
    pub n_ordered_pairs_h8: usize,
    pub n_total_h8_evaluations: usize,
    pub n_passing_h8_atoms: usize,
    pub n_passing_v3_cubed_atoms: usize,
    pub n_bound: usize,
    pub n_unbound: usize,
    pub b_order_zero_min_mev: Option<String>,
    pub b_order_zero_max_mev: Option<String>,
    pub b_tower_min_mev: Option<String>,
    pub b_tower_max_mev: Option<String>,
    pub passing_atoms: Vec<H8FlavouredAtomRow>,
}

fn format_v_word(seq: &[u8]) -> String {
    seq.iter().map(|&s| format!("V{s}")).collect()
}

fn expand_v_seq(seq: &[u8], shift: usize) -> Vec<HeckeLetter> {
    let mut out = Vec::with_capacity(seq.len() * 2);
    for &s in seq {
        out.extend_from_slice(&HeckeLetter::v_pair((s as usize) + shift));
    }
    out
}

pub fn evaluate_h4_flavoured_census(
    params: &Q0Params,
    max_vertices: usize,
    dps: usize,
) -> H4FlavouredCensusReport {
    let p = params.prec_bits;
    let rep4 = TwoRowTowerRep::new(params, 4);
    let rep8 = TwoRowTowerRep::new(params, 8);

    let perms = all_s4_perms();
    let mut idx_map = HashMap::with_capacity(24);
    for (i, w) in perms.iter().enumerate() {
        idx_map.insert(*w, i);
    }

    // net(p) = 1 - h/2, net(n) = 1 - 3h/2 + h^2/2 (`PairSkeinMassConventionD` / `atom.py`)
    let one = Float::with_val(p, 1);
    let half = Float::with_val(p, 1) / 2u32;
    let h = &params.h;
    let net_p = Float::with_val(p, &one - Float::with_val(p, h * &half));
    let net_n = Float::with_val(
        p,
        &one - Float::with_val(p, 3u32 * Float::with_val(p, h * &half))
            + Float::with_val(p, Float::with_val(p, h * h) * &half),
    );

    let mut cands: Vec<Vec<u8>> = Vec::new();
    for len in 1..=max_vertices {
        for mask in 0..(1usize << len) {
            let mut seq = Vec::with_capacity(len);
            for bit in (0..len).rev() {
                seq.push(((mask >> bit) & 1) as u8);
            }
            cands.push(seq);
        }
    }

    let tw3 = trace_weights_h3(params);
    let mut passing_seqs: Vec<Vec<u8>> = Vec::new();
    let mut nucleon_rows: Vec<H4NucleonWordRow> = Vec::new();

    for seq in &cands {
        let letters = expand_v_seq(seq, 0);
        let ev = rep4.evaluate_word(&letters);
        if !ev.reading3_m1_to_n {
            continue;
        }
        passing_seqs.push(seq.clone());

        let mut h4 = H4Elem::one(p, &perms, &idx_map);
        for &lt in &letters {
            h4 = h4.mul_letter(lt, h, &idx_map);
        }
        let a1 = h4.net_h4();
        let e_z1 = h4.project_to_h3(&one, h);
        let e_zd = h4.project_to_h3(&params.z_d, h);
        let a2 = e_z1.net();
        let a3 = e_zd.net();

        // Internal consistency check: tr_M^(3)(E_{4->3}(z_D)(W)) == tr_M^(4)(W)
        let mut tr_proj = Float::with_val(p, 0);
        for k in 0..6 {
            tr_proj += Float::with_val(p, &e_zd.c[k] * &tw3[k]);
        }
        let tr_err = (tr_proj - &ev.tr_m).abs();
        assert!(
            tr_err < parse_dec(p, "1e-82"),
            "E_{{4->3}}(z_D) trace mismatch on {}: {tr_err}",
            format_v_word(seq)
        );

        let diff_p = (a3.clone() - &net_p).abs();
        let diff_n = (a3.clone() - &net_n).abs();
        let swapped: Vec<u8> = seq.iter().map(|&x| 1 - x).collect();

        nucleon_rows.push(H4NucleonWordRow {
            word: format_v_word(seq),
            n_vertices: seq.len(),
            tr_m: fmt_dps(&ev.tr_m, dps),
            min_level_char: fmt_dps(&ev.min_char_m1_to_n, dps),
            net_a1_h4: fmt_dps(&a1, dps),
            net_a2_e4to3_z1: fmt_dps(&a2, dps),
            net_a3_e4to3_zd: fmt_dps(&a3, dps),
            abs_diff_a3_vs_proton_net: fmt_dps(&diff_p, dps),
            abs_diff_a3_vs_neutron_net: fmt_dps(&diff_n, dps),
            site_swap_partner: format_v_word(&swapped),
        });
    }

    // Reading D: all ordered pairs (w1, w2) on 8 strands with bonds V(s)^k, s in {3, 2}, k in {1, 2, 3}
    let bonds = [(3usize, 1usize), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3)];
    let b_ame = parse_dec(p, AME2020_B_2H_MEV);
    let hundred = Float::with_val(p, 100);

    let mut passing_atoms = Vec::new();
    let mut b0_vals: Vec<Float> = Vec::new();
    let mut bt_vals: Vec<Float> = Vec::new();
    let mut n_evals = 0usize;
    let mut n_v3_cubed = 0usize;

    for w1 in &passing_seqs {
        let l1 = expand_v_seq(w1, 0);
        let w1_name = format_v_word(w1);
        for w2 in &passing_seqs {
            let mut x = l1.clone();
            x.extend(expand_v_seq(w2, 4));
            let ev_x = rep8.evaluate_word(&x);
            n_evals += 1;
            let w2_name = format_v_word(w2);

            for &(s, k) in &bonds {
                let mut xk = x.clone();
                for _ in 0..k {
                    xk.extend_from_slice(&HeckeLetter::v_pair(s));
                }
                let ev_xk = rep8.evaluate_word(&xk);
                n_evals += 1;

                if !ev_x.reading3_m1_to_n || !ev_xk.reading3_m1_to_n {
                    continue;
                }
                if s == 3 && k == 3 {
                    n_v3_cubed += 1;
                }
                let ratio = Float::with_val(p, &ev_xk.tr_m / &ev_x.tr_m);
                let (b0_opt, bt_opt, err0_opt, errt_opt) = if ratio > 0 {
                    let ln_r = Float::with_val(p, ratio.clone().ln());
                    let b0: Float = -Float::with_val(p, &params.e0_order_zero_mev * &ln_r);
                    let bt: Float = -Float::with_val(p, &params.e0_tower_mev * &ln_r);
                    let err0 = Float::with_val(
                        p,
                        Float::with_val(p, Float::with_val(p, &b0 / &b_ame) - &one) * &hundred,
                    );
                    let errt = Float::with_val(
                        p,
                        Float::with_val(p, Float::with_val(p, &bt / &b_ame) - &one) * &hundred,
                    );
                    b0_vals.push(b0.clone());
                    bt_vals.push(bt.clone());
                    (
                        Some(fmt_dps(&b0, dps)),
                        Some(fmt_dps(&bt, dps)),
                        Some(fmt_dps(&err0, dps)),
                        Some(fmt_dps(&errt, dps)),
                    )
                } else {
                    (None, None, None, None)
                };

                passing_atoms.push(H8FlavouredAtomRow {
                    w1: w1_name.clone(),
                    w2: w2_name.clone(),
                    bond: format!("V({s})^{k}"),
                    ratio: fmt_dps(&ratio, dps),
                    b_order_zero_mev: b0_opt,
                    b_tower_mev: bt_opt,
                    b_err_vs_ame_order_zero_pct: err0_opt,
                    b_err_vs_ame_tower_pct: errt_opt,
                    min_level_char: fmt_dps(&ev_xk.min_char_m1_to_n, dps),
                });
            }
        }
    }

    let n_bound = bt_vals.iter().filter(|b| **b > 0).count();
    let n_unbound = bt_vals.len() - n_bound;
    let min_opt = |vals: &[Float]| -> Option<String> {
        let mut it = vals.iter();
        let first = it.next()?;
        let mut m = first.clone();
        for v in it {
            if v < &m {
                m = v.clone();
            }
        }
        Some(fmt_dps(&m, dps))
    };
    let max_opt = |vals: &[Float]| -> Option<String> {
        let mut it = vals.iter();
        let first = it.next()?;
        let mut m = first.clone();
        for v in it {
            if v > &m {
                m = v.clone();
            }
        }
        Some(fmt_dps(&m, dps))
    };

    H4FlavouredCensusReport {
        max_vertices,
        n_candidates_h4: cands.len(),
        n_passing_nucleon_words: passing_seqs.len(),
        proton_production_net_target: fmt_dps(&net_p, dps),
        neutron_production_net_target: fmt_dps(&net_n, dps),
        nucleon_words: nucleon_rows,
        n_ordered_pairs_h8: passing_seqs.len() * passing_seqs.len(),
        n_total_h8_evaluations: n_evals,
        n_passing_h8_atoms: passing_atoms.len(),
        n_passing_v3_cubed_atoms: n_v3_cubed,
        n_bound,
        n_unbound,
        b_order_zero_min_mev: min_opt(&b0_vals),
        b_order_zero_max_mev: max_opt(&b0_vals),
        b_tower_min_mev: min_opt(&bt_vals),
        b_tower_max_mev: max_opt(&bt_vals),
        passing_atoms,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn h4_l3_reproduces_flavoured_witness_counts() {
        let params = Q0Params::proton_pinned(320, None);
        let rep = evaluate_h4_flavoured_census(&params, 3, 40);
        // At L=3, gg-deuteron-flavoured.witness.json has 2 nucleon words (V0V0V0, V1V1V1) and 8 passing atoms
        assert_eq!(rep.n_passing_nucleon_words, 2);
        assert_eq!(rep.n_passing_h8_atoms, 8);
    }
}
