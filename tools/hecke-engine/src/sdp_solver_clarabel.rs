//! Phase R5.3: Clarabel.rs SDP solver — porting the bisection
//! verifier to a true semidefinite program.
//!
//! For a candidate Hecke element T_w with known coefficients
//! (e.g. proton's Borromean braid):
//!     find  α* := max{α ∈ [0, 1] :
//!         α · ρ_λ(T_w) + (1 − α) · I_{d_λ}  ⪰ 0  ∀ λ ⊢ n}
//!
//! Posed as a single SDP:
//!     maximize α
//!     subject to:
//!         α · (ρ_λ − I) + I  ⪰ 0    for every λ ⊢ n
//!         0 ≤ α ≤ 1
//!
//! Variables: just α (1 variable).
//! Constraints: 2 nonneg-cone (for 0 ≤ α ≤ 1) + n_blocks PSD-triangle cones.
//!
//! Same answer as `sdp_verifier::solve_alpha_psd` (bisection); this
//! version is the production path that will scale to multiple
//! variables in R5.4 (proton T_w recovery test) and R5.5 (⁶Li).
//!
//! See [R5_FULL_PLAN.md](../../R5_FULL_PLAN.md) §"R5.3".

use crate::seminormal::{partitions_of, seminormal_matrices};
use clarabel::algebra::CscMatrix;
use clarabel::solver::*;

#[derive(Debug, Clone)]
pub struct ClarabelSdpReport {
    pub n: usize,
    pub q0: f64,
    pub alpha_star: f64,
    pub solver_status: String,
    pub n_blocks: usize,
    pub block_dims: Vec<usize>,
    pub iterations: u32,
}

fn invert_matrix_h(m: &[Vec<f64>], h: f64) -> Vec<Vec<f64>> {
    let n = m.len();
    let mut out = vec![vec![0.0f64; n]; n];
    for (i, row) in m.iter().enumerate() {
        for (j, &v) in row.iter().enumerate() {
            out[i][j] = if i == j { v - h } else { v };
        }
    }
    out
}

fn sparse_to_dense(sparse: &[Vec<(usize, f64)>], dim: usize) -> Vec<Vec<f64>> {
    let mut out = vec![vec![0.0f64; dim]; dim];
    for (i, row) in sparse.iter().enumerate() {
        for &(j, v) in row {
            out[i][j] = v;
        }
    }
    out
}

fn dense_dense_mul(a: &[Vec<f64>], b: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let n = a.len();
    let m = b[0].len();
    let k = b.len();
    let mut out = vec![vec![0.0f64; m]; n];
    for i in 0..n {
        for kk in 0..k {
            let aik = a[i][kk];
            if aik == 0.0 {
                continue;
            }
            for j in 0..m {
                out[i][j] += aik * b[kk][j];
            }
        }
    }
    out
}

fn symmetrize(m: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let n = m.len();
    let mut out = vec![vec![0.0f64; n]; n];
    for i in 0..n {
        for j in 0..n {
            out[i][j] = 0.5 * (m[i][j] + m[j][i]);
        }
    }
    out
}

fn build_rho_lambda(shape: &[usize], braid_word: &[i32], q: f64) -> Vec<Vec<f64>> {
    let h = q - 1.0 / q;
    let sparse_gens = seminormal_matrices(shape, q);
    let dim = if sparse_gens.is_empty() {
        1
    } else {
        sparse_gens[0].len()
    };
    let mut prod = vec![vec![0.0f64; dim]; dim];
    for i in 0..dim {
        prod[i][i] = 1.0;
    }
    let dense_gens: Vec<Vec<Vec<f64>>> = sparse_gens
        .iter()
        .map(|sg| sparse_to_dense(sg, dim))
        .collect();
    let dense_inv: Vec<Vec<Vec<f64>>> = dense_gens
        .iter()
        .map(|dg| invert_matrix_h(dg, h))
        .collect();
    for &gen in braid_word {
        let idx = gen.unsigned_abs() as usize - 1;
        if idx >= dense_gens.len() {
            continue;
        }
        let g = if gen > 0 {
            &dense_gens[idx]
        } else {
            &dense_inv[idx]
        };
        prod = dense_dense_mul(&prod, g);
    }
    symmetrize(&prod)
}

/// Pack a symmetric matrix into Clarabel's lower-triangular column-
/// stacked SDP-cone vectorization with `sqrt(2)` scaling on
/// off-diagonal entries.  Standard svec layout:
///     vec(M) = [M_00,  sqrt(2) M_10, ..., sqrt(2) M_{d-1,0},
///               M_11,  sqrt(2) M_21, ..., M_{d-1,d-1}].
fn svec_pack(m: &[Vec<f64>]) -> Vec<f64> {
    let d = m.len();
    let mut out = Vec::with_capacity(d * (d + 1) / 2);
    let sqrt2 = 2f64.sqrt();
    for col in 0..d {
        for row in col..d {
            let v = m[row][col];
            let scale = if row == col { 1.0 } else { sqrt2 };
            out.push(v * scale);
        }
    }
    out
}

/// Pose and solve via Clarabel.rs — single-variable α formulation.
pub fn solve_alpha_psd_clarabel(n: usize, braid_word: &[i32], q: f64) -> ClarabelSdpReport {
    let parts = partitions_of(n);
    let block_dims: Vec<usize> = parts
        .iter()
        .map(|sh| {
            let sg = seminormal_matrices(sh, q);
            if sg.is_empty() {
                1
            } else {
                sg[0].len()
            }
        })
        .collect();

    // Build per-block ρ matrices once.
    let rhos: Vec<Vec<Vec<f64>>> = parts
        .iter()
        .map(|sh| build_rho_lambda(sh, braid_word, q))
        .collect();

    // Variables: α only.  Single column.
    let p_dim = 1usize;
    // P = 0 (no quadratic), q_vec = -1 (minimize -α).
    let p = CscMatrix::zeros((p_dim, p_dim));
    let q_vec = vec![-1.0f64];

    // Constraints, in Clarabel "A x + s = b, s ∈ K" form.
    //
    // 1. α + s = 1, s ∈ ℝ_+    →   1 - α ≥ 0
    // 2. -α + s = 0, s ∈ ℝ_+   →   α ≥ 0
    // 3. per block λ:
    //    constraint M_λ(α) := α · (ρ_λ − I) + I  ⪰ 0
    //    Clarabel form:
    //      A_block α + s_block = b_block, s_block ∈ PSDᶜ
    //    where
    //      svec(M_λ(α)) = α · svec(ρ_λ − I) + svec(I)
    //    so:
    //      svec(I) − A_block · α  ∈ PSDᶜ
    //   ⇒  A_block = -(ρ_λ − I)_svec,  b_block = I_svec.

    let mut a_rows: Vec<usize> = Vec::new();
    let mut a_vals: Vec<f64> = Vec::new();
    let mut b: Vec<f64> = Vec::new();
    let mut cones: Vec<SupportedConeT<f64>> = Vec::new();
    let mut row = 0usize;

    // (1) α ≤ 1
    a_rows.push(row);
    a_vals.push(1.0);
    b.push(1.0);
    cones.push(SupportedConeT::NonnegativeConeT(1));
    row += 1;

    // (2) α ≥ 0
    a_rows.push(row);
    a_vals.push(-1.0);
    b.push(0.0);
    cones.push(SupportedConeT::NonnegativeConeT(1));
    row += 1;

    // (3) PSD blocks
    for (b_idx, _shape) in parts.iter().enumerate() {
        let d = block_dims[b_idx];
        let cone_dim = d * (d + 1) / 2;
        let rho = &rhos[b_idx];
        // Build (ρ − I) and I matrices, then svec each.
        let mut rho_minus_i = vec![vec![0.0f64; d]; d];
        let mut identity = vec![vec![0.0f64; d]; d];
        for i in 0..d {
            for j in 0..d {
                rho_minus_i[i][j] = rho[i][j];
                if i == j {
                    rho_minus_i[i][j] -= 1.0;
                    identity[i][j] = 1.0;
                }
            }
        }
        let svec_a = svec_pack(&rho_minus_i);
        let svec_b = svec_pack(&identity);
        for k in 0..cone_dim {
            // A_block · α  with sign such that svec(I) − A_block · α  ∈ PSDᶜ
            // ⇔ Clarabel: A x + s = b, s ∈ PSDᶜ
            //   pick A x = -(ρ − I)_svec · α, b = I_svec
            //   then s = I_svec - A x = I_svec + (ρ−I)_svec · α
            //   = svec(I + α(ρ−I)) which is what we want ⪰ 0.
            // So A entry is -(ρ−I)_svec[k].
            a_rows.push(row + k);
            a_vals.push(-svec_a[k]);
            b.push(svec_b[k]);
        }
        cones.push(SupportedConeT::PSDTriangleConeT(d));
        row += cone_dim;
    }

    // Build CSC: single column, `a_rows.len()` non-zeros.
    let m_rows = row;
    let nnz = a_rows.len();
    let a_indptr: Vec<usize> = vec![0, nnz];
    let a_csc = CscMatrix::new(m_rows, p_dim, a_indptr, a_rows, a_vals);

    let settings = DefaultSettingsBuilder::default()
        .verbose(false)
        .max_iter(200)
        .build()
        .unwrap();

    let mut solver = DefaultSolver::new(&p, &q_vec, &a_csc, &b, &cones, settings).unwrap();
    solver.solve();

    let alpha_star = -solver.solution.obj_val;
    let status = format!("{:?}", solver.solution.status);
    let iters = solver.solution.iterations;

    ClarabelSdpReport {
        n,
        q0: q,
        alpha_star,
        solver_status: status,
        n_blocks: parts.len(),
        block_dims,
        iterations: iters,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn proton_borromean_clarabel_alpha_one() {
        // Borromean braid in H_3: all blocks PSD ⇒ α* ≈ 1.
        let q = 1.1097;
        let report = solve_alpha_psd_clarabel(3, &[1, -2, 1, -2, 1, -2], q);
        assert!(
            report.alpha_star > 0.999,
            "α* = {} expected ≈ 1.0; status: {}",
            report.alpha_star,
            report.solver_status
        );
        assert_eq!(report.n_blocks, 3);
    }

    #[test]
    fn deuteron_clarabel_alpha_quantifies_gap() {
        // 6_2 in B_3: standard block NOT PSD ⇒ α* < 1.
        let q = 1.1097;
        let report = solve_alpha_psd_clarabel(3, &[1, -2, 1, 1, 1, -2], q);
        assert!(
            report.alpha_star >= 0.0 && report.alpha_star <= 1.0 + 1e-6,
            "α* = {} should be in [0,1]; status: {}",
            report.alpha_star,
            report.solver_status
        );
        assert!(
            report.alpha_star < 0.9999,
            "α* = {} expected < 1; status: {}",
            report.alpha_star,
            report.solver_status
        );
    }

    #[test]
    fn clarabel_matches_bisection() {
        // For Borromean and deuteron, Clarabel SDP and bisection
        // verifier should agree on α* to within tolerance.
        use crate::sdp_verifier::solve_alpha_psd as bisection;
        let q = 1.1097;
        for braid in [
            vec![1, -2, 1, -2, 1, -2],     // proton Borromean
            vec![1, -2, 1, 1, 1, -2],      // deuteron 6_2
            vec![-1, 2, -1, 2, -1, 2],     // ³He L6a4
        ] {
            let bis = bisection(3, &braid, q);
            let clar = solve_alpha_psd_clarabel(3, &braid, q);
            let diff = (bis.alpha_star - clar.alpha_star).abs();
            assert!(
                diff < 1e-3,
                "Bisection α*={:.6} vs Clarabel α*={:.6} for braid {:?} (diff {:.2e}); status {}",
                bis.alpha_star,
                clar.alpha_star,
                braid,
                diff,
                clar.solver_status
            );
        }
    }
}
