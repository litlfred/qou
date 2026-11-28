//! Fast two-row Gelfand–Tsetlin / Young orthogonal-seminormal evaluator on `H_n(q)` (`n <= 12`).
//!
//! Under Convention D (`z_D = q^3 / (q^2 + 1)`), every irreducible partition with `>= 3` rows
//! carries exact weight `y_lambda = 0` (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`).
//! For any `n`-strand word `W`, both the Convention-D Markov trace `tr_M(W)` and the multi-level
//! conditional-expectation two-row characters `chi_mu(E_{n -> m} W)` (`1 <= m <= n`, `mu = (m-r, r)`)
//! are determined completely by the diagonal entries `W_{T,T}` in the Gelfand–Tsetlin basis of
//! two-row standard Young tableaux:
//!
//! ```text
//!     chi_mu(E_{n -> m} W) = sum_{lambda = (n-k, k)} (y_lambda / y_mu) * sum_{T : T|_{1..m} = mu} W_{T,T}.
//! ```
//!
//! Each generator `sigma_g` (`0 <= g <= n - 2`, acting on `g + 1` and `g + 2`) decomposes into
//! `1x1` diagonal entries (`+q` on same row, `-q^-1` on same column) and `2x2` symmetric blocks
//! on `(T, s_g T)` with axial distance `d = ct_T(g+2) - ct_T(g+1)` (`|d| >= 2`):
//! `M_{T,T} = h / (1 - q^(-2d))`, `M_{T, s_g T} = sqrt(1 - 1 / [d]_q^2)`.
//!
//! Because each generator is `2`-sparse per row and maximum block dimension at `n = 12` is `297`
//! (`sum_{k=0}^6 dim(12-k, k)^2 = C_12 = 208_012`), propagating one basis vector `e_T` at a time
//! stays inside L1 cache and evaluates a 130-letter `H_12(q)` word at 320-bit MPFR in ~0.5 s.

use crate::scalars::Q0Params;
use rug::ops::Pow;
use rug::{Assign, Float};
use std::collections::HashMap;

/// Hecke word letter on generator `g` (`0 <= g <= n - 2`).
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum HeckeLetter {
    /// `sigma_g`
    Pos(usize),
    /// `sigma_g^-1 = sigma_g - h * 1`
    Inv(usize),
    /// `sigma_g - (h / 2) * 1` (`uud` / `udd` mixed flavour projector)
    Half(usize),
}

impl HeckeLetter {
    pub fn v_pair(s: usize) -> [Self; 2] {
        [Self::Pos(s), Self::Inv(s + 1)]
    }
}

/// Sparse action of a single generator `sigma_g` on a block of dimension `dim`:
/// - `diag_only`: `(idx, coeff)` where `sigma_g e_idx = coeff * e_idx`
/// - `pairs`: `(i, j, c_ii, c_jj, c_ij)` with `i < j` where
///   `sigma_g` acts by `[[c_ii, c_ij], [c_ij, c_jj]]` on `(e_i, e_j)`.
#[derive(Debug, Clone)]
struct SparseGen {
    diag_only: Vec<(usize, Float)>,
    pairs: Vec<(usize, usize, Float, Float, Float)>,
}

#[derive(Debug, Clone)]
struct TwoRowBlock {
    dim: usize,
    y_lambda: Float,
    /// For each SYT `t_idx` (`0..dim`) and each `m` (`1..=n`), the number of row-1 entries in `1..=m`.
    prefix_row1_counts: Vec<Vec<usize>>,
    gens: Vec<SparseGen>,
}

#[derive(Debug, Clone)]
pub struct TwoRowTowerRep {
    pub n: usize,
    pub prec: u32,
    pub h: Float,
    pub half_h: Float,
    blocks: Vec<TwoRowBlock>,
    /// `y_mu[m][r]` for `1 <= m <= n` and `0 <= 2*r <= m`.
    y_mu: Vec<Vec<Float>>,
}

#[derive(Debug, Clone)]
pub struct TowerEvalResult {
    pub tr_m: Float,
    /// All `(m, (m - r, r), chi_mu(E_{n -> m} W))` for `1 <= m <= n` and `0 <= 2*r <= m`.
    pub level_chars: Vec<(usize, (usize, usize), Float)>,
    pub min_char_m1_to_n: Float,
    pub min_char_m3_to_n: Float,
    pub failing_levels_m1_to_n: Vec<usize>,
    pub failing_levels_m3_to_n: Vec<usize>,
    pub reading3_m1_to_n: bool,
    pub reading3_m3_to_n: bool,
}

/// Enumerate two-row SYTs of shape `(n - r, r)` as bitmasks / row indicator vectors `row_of[0..n]` in `{0, 1}`.
fn enumerate_two_row_syts(n: usize, r: usize) -> Vec<Vec<u8>> {
    let mut out = Vec::new();
    let mut cur = Vec::with_capacity(n);
    fn rec(
        pos: usize,
        n: usize,
        target_r0: usize,
        target_r1: usize,
        c0: usize,
        c1: usize,
        cur: &mut Vec<u8>,
        out: &mut Vec<Vec<u8>>,
    ) {
        if pos == n {
            out.push(cur.clone());
            return;
        }
        if c0 < target_r0 {
            cur.push(0);
            rec(pos + 1, n, target_r0, target_r1, c0 + 1, c1, cur, out);
            cur.pop();
        }
        if c1 < target_r1 && c1 < c0 {
            cur.push(1);
            rec(pos + 1, n, target_r0, target_r1, c0, c1 + 1, cur, out);
            cur.pop();
        }
    }
    rec(0, n, n - r, r, 0, 0, &mut cur, &mut out);
    out
}

impl TwoRowTowerRep {
    pub fn new(params: &Q0Params, n: usize) -> Self {
        assert!(n >= 2, "TwoRowTowerRep requires n >= 2");
        let p = params.prec_bits;
        let one = Float::with_val(p, 1);
        let neg_q_inv = Float::with_val(p, -&params.q_inv);
        let half_h = Float::with_val(p, &params.h / 2u32);

        // Precompute axial-distance coefficients for d = -(n as i32) ..= (n as i32)
        // f(d) = h / (1 - q^(-2d)), off(d) = sqrt(1 - 1 / [d]_q^2) for |d| >= 2.
        let mut f_pos: Vec<Float> = vec![Float::with_val(p, 0); n + 1];
        let mut f_neg: Vec<Float> = vec![Float::with_val(p, 0); n + 1];
        let mut off_mag: Vec<Float> = vec![Float::with_val(p, 0); n + 1];
        for d in 2..=n {
            let two_d = (2 * d) as i32;
            let q_neg_2d = Float::with_val(p, params.q.clone().pow(-two_d));
            let q_pos_2d = Float::with_val(p, params.q.clone().pow(two_d));
            f_pos[d] = Float::with_val(p, &params.h / Float::with_val(p, &one - q_neg_2d));
            f_neg[d] = Float::with_val(p, &params.h / Float::with_val(p, &one - q_pos_2d));
            let qd = params.q_int(d as i32);
            let qd2 = Float::with_val(p, &qd * &qd);
            let inside = Float::with_val(p, &one - Float::with_val(p, &one / qd2));
            off_mag[d] = Float::with_val(p, inside.sqrt());
        }

        let mut y_mu = vec![Vec::new(); n + 1];
        for m in 1..=n {
            let mut ym = Vec::with_capacity(m / 2 + 1);
            for r in 0..=(m / 2) {
                ym.push(params.y_two_row(m, r));
            }
            y_mu[m] = ym;
        }

        let mut blocks = Vec::with_capacity(n / 2 + 1);
        for r in 0..=(n / 2) {
            let syts = enumerate_two_row_syts(n, r);
            let dim = syts.len();
            let mut syt_to_idx: HashMap<Vec<u8>, usize> = HashMap::with_capacity(dim);
            for (idx, syt) in syts.iter().enumerate() {
                syt_to_idx.insert(syt.clone(), idx);
            }

            // Compute contents ct_T(pos) = col - row for each entry pos in 0..n, plus prefix row1 counts.
            let mut contents: Vec<Vec<i32>> = Vec::with_capacity(dim);
            let mut prefix_row1_counts: Vec<Vec<usize>> = Vec::with_capacity(dim);
            for syt in &syts {
                let mut c0 = 0i32;
                let mut c1 = 0i32;
                let mut ct = Vec::with_capacity(n);
                let mut pref = Vec::with_capacity(n + 1);
                pref.push(0);
                let mut r1_acc = 0usize;
                for &row in syt {
                    if row == 0 {
                        ct.push(c0); // col = c0, row = 0 -> c0
                        c0 += 1;
                    } else {
                        ct.push(c1 - 1); // col = c1, row = 1 -> c1 - 1
                        c1 += 1;
                        r1_acc += 1;
                    }
                    pref.push(r1_acc);
                }
                contents.push(ct);
                prefix_row1_counts.push(pref);
            }

            let mut gens = Vec::with_capacity(n - 1);
            for g in 0..(n - 1) {
                let mut diag_only = Vec::new();
                let mut pairs = Vec::new();
                let mut visited = vec![false; dim];

                for i in 0..dim {
                    if visited[i] {
                        continue;
                    }
                    let d = contents[i][g + 1] - contents[i][g];
                    if d == 1 {
                        visited[i] = true;
                        diag_only.push((i, params.q.clone()));
                    } else if d == -1 {
                        visited[i] = true;
                        diag_only.push((i, neg_q_inv.clone()));
                    } else {
                        let mut swapped = syts[i].clone();
                        swapped.swap(g, g + 1);
                        let j = *syt_to_idx
                            .get(&swapped)
                            .expect("swapped SYT with |d| >= 2 must be valid SYT");
                        assert!(i < j, "visited order ensures i < j");
                        visited[i] = true;
                        visited[j] = true;
                        let ad = d.unsigned_abs() as usize;
                        let (c_ii, c_jj) = if d > 0 {
                            (f_pos[ad].clone(), f_neg[ad].clone())
                        } else {
                            (f_neg[ad].clone(), f_pos[ad].clone())
                        };
                        pairs.push((i, j, c_ii, c_jj, off_mag[ad].clone()));
                    }
                }
                gens.push(SparseGen { diag_only, pairs });
            }

            blocks.push(TwoRowBlock {
                dim,
                y_lambda: y_mu[n][r].clone(),
                prefix_row1_counts,
                gens,
            });
        }

        Self {
            n,
            prec: p,
            h: params.h.clone(),
            half_h,
            blocks,
            y_mu,
        }
    }

    /// Apply a single letter to vector `v` in-place (using scratch buffer `out`).
    #[inline]
    fn apply_letter(&self, blk: &TwoRowBlock, letter: HeckeLetter, v: &mut [Float], out: &mut [Float]) {
        let p = self.prec;
        let (g, shift_opt): (usize, Option<&Float>) = match letter {
            HeckeLetter::Pos(g) => (g, None),
            HeckeLetter::Inv(g) => (g, Some(&self.h)),
            HeckeLetter::Half(g) => (g, Some(&self.half_h)),
        };
        let sg = &blk.gens[g];

        for &(idx, ref c) in &sg.diag_only {
            out[idx].assign(&v[idx] * c);
            if let Some(sh) = shift_opt {
                out[idx] -= Float::with_val(p, &v[idx] * sh);
            }
        }
        for &(i, j, ref c_ii, ref c_jj, ref c_ij) in &sg.pairs {
            let vi = &v[i];
            let vj = &v[j];
            let mut ni = Float::with_val(p, vi * c_ii);
            ni += Float::with_val(p, vj * c_ij);
            let mut nj = Float::with_val(p, vi * c_ij);
            nj += Float::with_val(p, vj * c_jj);
            if let Some(sh) = shift_opt {
                ni -= Float::with_val(p, vi * sh);
                nj -= Float::with_val(p, vj * sh);
            }
            out[i] = ni;
            out[j] = nj;
        }
        v.clone_from_slice(out);
    }

    /// Evaluate `tr_M(W)` and all multi-level reading-3 characters `chi_mu(E_{n -> m} W)` (`m = 1..=n`).
    pub fn evaluate_word(&self, word: &[HeckeLetter]) -> TowerEvalResult {
        use rug::Assign;
        let p = self.prec;
        let n = self.n;

        // Accumulate weighted prefix sums: weighted_sum[m][r_mu] = sum_lambda y_lambda * sum_{T: T|_{1..m}=mu} W_{TT}
        let mut weighted_sum: Vec<Vec<Float>> = (0..=n)
            .map(|m| {
                if m == 0 {
                    Vec::new()
                } else {
                    (0..=(m / 2)).map(|_| Float::with_val(p, 0)).collect()
                }
            })
            .collect();

        for blk in &self.blocks {
            let dim = blk.dim;
            let mut v = vec![Float::with_val(p, 0); dim];
            let mut scratch = vec![Float::with_val(p, 0); dim];

            for start_t in 0..dim {
                for x in &mut v {
                    x.assign(0);
                }
                v[start_t].assign(1);
                for &lt in word {
                    self.apply_letter(blk, lt, &mut v, &mut scratch);
                }
                let w_tt = &v[start_t];
                let weighted_w_tt = Float::with_val(p, &blk.y_lambda * w_tt);
                let pref = &blk.prefix_row1_counts[start_t];
                for m in 1..=n {
                    let r_mu = pref[m];
                    weighted_sum[m][r_mu] += &weighted_w_tt;
                }
            }
        }

        // Notice weighted_sum[1][0] / y_mu[1][0]: at m=1, y_mu[1][0] = [2]_q / [2]_q = 1,
        // and sum_lambda y_lambda * tr_lambda(W) = tr_M(W)!
        let tr_m = weighted_sum[1][0].clone();

        let neg_tol: Float = -Float::with_val(p, Float::with_val(p, 10).pow(-70i32));
        let mut level_chars = Vec::new();
        let mut min_m1 = Float::with_val(p, f64::INFINITY);
        let mut min_m3 = Float::with_val(p, f64::INFINITY);
        let mut fail_m1 = Vec::new();
        let mut fail_m3 = Vec::new();

        for m in 1..=n {
            let mut failed_this_m = false;
            for r_mu in 0..=(m / 2) {
                let chi_mu = Float::with_val(p, &weighted_sum[m][r_mu] / &self.y_mu[m][r_mu]);
                if chi_mu < min_m1 {
                    min_m1 = chi_mu.clone();
                }
                if m >= 3 && chi_mu < min_m3 {
                    min_m3 = chi_mu.clone();
                }
                if chi_mu < neg_tol {
                    failed_this_m = true;
                }
                level_chars.push((m, (m - r_mu, r_mu), chi_mu));
            }
            if failed_this_m {
                fail_m1.push(m);
                if m >= 3 {
                    fail_m3.push(m);
                }
            }
        }
        if n < 3 {
            min_m3 = min_m1.clone();
        }

        TowerEvalResult {
            tr_m,
            level_chars,
            min_char_m1_to_n: min_m1,
            min_char_m3_to_n: min_m3,
            reading3_m1_to_n: fail_m1.is_empty(),
            reading3_m3_to_n: fail_m3.is_empty(),
            failing_levels_m1_to_n: fail_m1,
            failing_levels_m3_to_n: fail_m3,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::h3::{build_all_h3_rows, trace_weights_h3, H3Elem};
    use crate::scalars::parse_dec;

    #[test]
    fn tower_h3_agrees_with_exact_nf_evaluator() {
        let params = Q0Params::proton_pinned(320, None);
        let p = params.prec_bits;
        let tol = parse_dec(p, "1e-84");
        let rep3 = TwoRowTowerRep::new(&params, 3);
        let tw = trace_weights_h3(&params);

        // Check V^3 and proton_uud and neutron_udd
        let v3_word: Vec<HeckeLetter> = (0..3).flat_map(|_| HeckeLetter::v_pair(0)).collect();
        let res_v3 = rep3.evaluate_word(&v3_word);
        let v3_nf = H3Elem::vertex_v(&params).pow_u32(3, &params.h);
        let mut tr_nf = Float::with_val(p, 0);
        for k in 0..6 {
            tr_nf += Float::with_val(p, &v3_nf.c[k] * &tw[k]);
        }
        assert!(
            (res_v3.tr_m.clone() - &tr_nf).abs() < tol,
            "V^3 trace mismatch: {} vs {}",
            res_v3.tr_m,
            tr_nf
        );
        assert!(res_v3.reading3_m1_to_n);

        // Check proton_uud word
        let mut p_word = v3_word.clone();
        p_word.extend_from_slice(&[
            HeckeLetter::Pos(0),
            HeckeLetter::Half(0),
            HeckeLetter::Half(1),
            HeckeLetter::Pos(0),
            HeckeLetter::Pos(0),
        ]);
        let res_p = rep3.evaluate_word(&p_word);
        let (rows, _) = build_all_h3_rows(&params, 80);
        let p_row = &rows
            .iter()
            .find(|(_, r)| r.id == "nucleon_proton_uud")
            .unwrap()
            .0;
        let mut tr_p_nf = Float::with_val(p, 0);
        for k in 0..6 {
            tr_p_nf += Float::with_val(p, &p_row.c[k] * &tw[k]);
        }
        assert!(
            (res_p.tr_m.clone() - &tr_p_nf).abs() < tol,
            "proton trace mismatch: {} vs {}",
            res_p.tr_m,
            tr_p_nf
        );
    }
}
