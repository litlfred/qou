//! Wedderburn-block PSD evaluator (R3 of RUST_INTEGRATION.md).
//!
//! For a braid β = σ_{i_1} σ_{i_2} ... ∈ B_n and substrate parameter
//! q_0 ∈ ℝ, evaluate ρ_λ(β) ∈ M_{d_λ}(ℝ) for every partition λ ⊢ n
//! using the existing Hoefsmit seminormal infrastructure
//! (`crate::seminormal::seminormal_matrices`).  Symmetrize and extract
//! eigenvalues; emit a `WedderburnBlockReport` per partition.
//!
//! This populates the empty `wedderburn_blocks` field of
//! `JointTowerSdpCertificate`.
//!
//! Implementation note: we use plain dense matrices via `Vec<Vec<f64>>`
//! since the per-partition dimension d_λ is small for n ≤ 21 (e.g.
//! at n = 10 the largest is d_{(5,5)} ≤ 42; at n = 18 the largest is
//! d_{(9,9)} = 4862).  Eigenvalues via QR iteration on the symmetric
//! part — sufficient for PSD diagnosis.

use crate::joint_tower_sdp_certificate::WedderburnBlockReport;
use crate::seminormal::{partitions_of, seminormal_matrices};

/// Inverse generator: T_i^{-1} = T_i - h, where h = q - q^{-1}.
fn invert_matrix(m: &[Vec<f64>], h: f64) -> Vec<Vec<f64>> {
    let n = m.len();
    let mut out = vec![vec![0.0f64; n]; n];
    for (i, row) in m.iter().enumerate() {
        for (j, &v) in row.iter().enumerate() {
            out[i][j] = if i == j { v - h } else { v };
        }
    }
    out
}

/// Sparse-times-dense matmul.  `sparse[i]` is `Vec<(j, val)>` for row i.
fn sparse_dense_mul(
    sparse: &[Vec<(usize, f64)>],
    dense: &[Vec<f64>],
    dim: usize,
) -> Vec<Vec<f64>> {
    let mut out = vec![vec![0.0f64; dim]; dim];
    for i in 0..dim {
        for &(k, vik) in &sparse[i] {
            for j in 0..dim {
                out[i][j] += vik * dense[k][j];
            }
        }
    }
    out
}

/// Convert sparse to dense for inversion / repeated mul.
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

/// Symmetrize: (M + M^T) / 2.
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

/// Symmetric eigenvalues via Jacobi rotation method.  Stable for
/// modest dimensions (d ≤ ~100).  Returns sorted ascending.
fn symmetric_eigenvalues(m_in: &[Vec<f64>]) -> Vec<f64> {
    let n = m_in.len();
    if n == 0 {
        return Vec::new();
    }
    if n == 1 {
        return vec![m_in[0][0]];
    }
    // Working copy
    let mut a: Vec<Vec<f64>> = m_in.iter().map(|r| r.clone()).collect();
    let max_iter = 100 * n * n;
    for _iter in 0..max_iter {
        // Find largest off-diagonal
        let mut p = 0usize;
        let mut q = 1usize;
        let mut max_off = 0.0f64;
        for i in 0..n {
            for j in (i + 1)..n {
                let val = a[i][j].abs();
                if val > max_off {
                    max_off = val;
                    p = i;
                    q = j;
                }
            }
        }
        if max_off < 1e-12 {
            break;
        }
        let app = a[p][p];
        let aqq = a[q][q];
        let apq = a[p][q];
        let theta = (aqq - app) / (2.0 * apq);
        let t = if theta >= 0.0 {
            1.0 / (theta + (1.0 + theta * theta).sqrt())
        } else {
            1.0 / (theta - (1.0 + theta * theta).sqrt())
        };
        let c = 1.0 / (1.0 + t * t).sqrt();
        let s = t * c;
        // Rotate
        a[p][p] = app - t * apq;
        a[q][q] = aqq + t * apq;
        a[p][q] = 0.0;
        a[q][p] = 0.0;
        for i in 0..n {
            if i != p && i != q {
                let aip = a[i][p];
                let aiq = a[i][q];
                a[i][p] = c * aip - s * aiq;
                a[p][i] = a[i][p];
                a[i][q] = s * aip + c * aiq;
                a[q][i] = a[i][q];
            }
        }
    }
    let mut eigs: Vec<f64> = (0..n).map(|i| a[i][i]).collect();
    eigs.sort_by(|x, y| x.partial_cmp(y).unwrap_or(std::cmp::Ordering::Equal));
    eigs
}

/// Evaluate ρ_λ(β) for every partition λ ⊢ n, then emit per-block
/// PSD reports.
pub fn evaluate_all_blocks(n: usize, braid_word: &[i32], q: f64) -> Vec<WedderburnBlockReport> {
    if n < 2 {
        return Vec::new();
    }
    let h = q - 1.0 / q;
    let parts = partitions_of(n);
    let mut out: Vec<WedderburnBlockReport> = Vec::with_capacity(parts.len());
    for shape in parts {
        // Build seminormal sparse generator matrices once per partition
        let sparse_gens = seminormal_matrices(&shape, q);
        let dim = if sparse_gens.is_empty() {
            1
        } else {
            sparse_gens[0].len()
        };
        // Identity dense
        let mut prod = vec![vec![0.0f64; dim]; dim];
        for i in 0..dim {
            prod[i][i] = 1.0;
        }
        // Multiply by each generator according to braid word
        let mut dense_gens: Vec<Vec<Vec<f64>>> = Vec::with_capacity(sparse_gens.len());
        let mut dense_inv_gens: Vec<Vec<Vec<f64>>> = Vec::with_capacity(sparse_gens.len());
        for sg in &sparse_gens {
            let dg = sparse_to_dense(sg, dim);
            let dg_inv = invert_matrix(&dg, h);
            dense_gens.push(dg);
            dense_inv_gens.push(dg_inv);
        }
        for &gen in braid_word {
            let idx = gen.unsigned_abs() as usize - 1;
            if idx >= dense_gens.len() {
                // Generator out of range for this n — leave as identity
                continue;
            }
            let g = if gen > 0 {
                &dense_gens[idx]
            } else {
                &dense_inv_gens[idx]
            };
            prod = dense_dense_mul(&prod, g);
        }
        let sym = symmetrize(&prod);
        let eigs = symmetric_eigenvalues(&sym);
        let min_eig = eigs.first().copied().unwrap_or(0.0);
        let max_eig = eigs.last().copied().unwrap_or(0.0);
        out.push(WedderburnBlockReport {
            partition: shape.clone(),
            d_lambda: dim,
            matrix_at_q_0_sym_eigvals: eigs.clone(),
            min_eigenvalue: min_eig,
            max_eigenvalue: max_eig,
            psd_symmetric_part: min_eig >= -1e-9,
        });
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn h2_electron_blocks() {
        // n=2, braid σ_1^3, q_0 ≈ 1.1097
        // Two 1D Wedderburn blocks: trivial (eigenvalue = q^3) and sign
        // (eigenvalue = -q^{-3}).  Both single-eigenvalue.
        let q = 1.1097;
        let blocks = evaluate_all_blocks(2, &[1, 1, 1], q);
        assert_eq!(blocks.len(), 2);
        // partition (2): trivial, ρ(σ_1) = q
        // partition (1,1): sign, ρ(σ_1) = -q^{-1}
        // ρ(σ_1^3): trivial = q^3, sign = -q^{-3}
        for b in &blocks {
            assert_eq!(b.d_lambda, 1);
            assert_eq!(b.matrix_at_q_0_sym_eigvals.len(), 1);
            if b.partition == vec![2] {
                let expected = q.powi(3);
                assert!((b.matrix_at_q_0_sym_eigvals[0] - expected).abs() < 1e-9,
                    "trivial block: expected {} got {}", expected, b.matrix_at_q_0_sym_eigvals[0]);
            }
        }
    }

    #[test]
    fn h3_proton_borromean() {
        // n=3, braid (σ_1 σ_2^{-1})^3, q_0 ≈ 1.1097
        // Three Wedderburn blocks: (3), (2,1), (1,1,1).
        let q = 1.1097;
        let blocks = evaluate_all_blocks(3, &[1, -2, 1, -2, 1, -2], q);
        assert_eq!(blocks.len(), 3);
        let dims: Vec<usize> = blocks.iter().map(|b| b.d_lambda).collect();
        // dimensions of irreps of S_3: 1, 2, 1
        assert!(dims.contains(&1));
        assert!(dims.contains(&2));
    }
}
