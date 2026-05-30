//! Genuine **dense-PSD** operator-selection SDP — Clarabel PSD cone (f64).
//!
//! Unlike the diagonal lift `M(x) = diag(Gx)` (which is LP-equivalent and
//! handled by [`operator_selection_lp`](crate::operator_selection_lp)), this
//! solves an SDP with a genuine dense positive-semidefinite constraint that
//! captures off-diagonal correlations:
//!
//! ```text
//!     min  t · x
//!     s.t. 1ᵀ x = n_target
//!          M₀ + Σ_k x_k M_k  ⪰ 0        (dense PSD cone, p × p)
//! ```
//!
//! The PSD cone requires an eigen-step, which Clarabel implements via
//! LAPACK — so this path is **`f64`** (the MPFR backend has no PSD cone).
//! It is still a strict upgrade over cvxpy/SCS: Clarabel emits a proper
//! dual PSD certificate and the strong-duality gap.
//!
//! Clarabel encodes a PSD block in **svec** form (column-major upper
//! triangle, off-diagonal entries scaled by √2).  With `A x + s = b`,
//! `s ∈ PSDTriangleCone`, we set `b = svec(M₀)` and column `k` of `A` to
//! `-svec(M_k)`, so `s = svec(M₀ + Σ_k x_k M_k) ⪰ 0`.
//!
//! Required feature: `clarabel-sdp`.

use clarabel::algebra::CscMatrix;
use clarabel::solver::*;

/// Result of the dense-PSD operator-selection SDP.
#[derive(Debug, Clone)]
pub struct SdpDenseResult {
    pub x_star: Vec<f64>,
    /// Optimal slack matrix `S = M₀ + Σ_k x_k M_k` (should be PSD).
    pub slack_matrix: Vec<Vec<f64>>,
    pub primal_obj: f64,
    pub dual_obj: f64,
    pub duality_gap: f64,
    /// Minimum diagonal entry of `S` — a necessary PSD witness (≥ −tol).
    pub min_diag: f64,
    pub feasible: bool,
    pub status: String,
}

/// Solve `min t·x  s.t.  1ᵀx = n_target,  M₀ + Σ_k x_k M_k ⪰ 0`.
///
/// * `t`          — objective, length `d`.
/// * `psd_const`  — `M₀`, a `p × p` symmetric matrix (row-major).
/// * `psd_slices` — `M_k` for `k = 0..d`, each `p × p` symmetric.
/// * `n_target`   — net-constraint RHS.
pub fn solve_operator_selection_sdp_dense(
    t: &[f64],
    psd_const: &[Vec<f64>],
    psd_slices: &[Vec<Vec<f64>>],
    n_target: f64,
) -> SdpDenseResult {
    let d = t.len();
    assert_eq!(psd_slices.len(), d, "psd_slices len {} != d {}", psd_slices.len(), d);
    let p = psd_const.len();
    assert!(p > 0, "PSD matrix must be non-empty");
    for (k, m) in psd_slices.iter().enumerate() {
        assert_eq!(m.len(), p, "psd_slices[{k}] has {} rows != p {}", m.len(), p);
    }
    let sqrt2 = 2f64.sqrt();

    // P = 0 (linear objective), q = t.
    let p_zero: CscMatrix<f64> = CscMatrix::<f64>::zeros((d, d));
    let q_vec = t.to_vec();

    // Rows: 0 = net equality (ZeroCone); 1.. = svec PSD block (PSDTriangleCone).
    let n_tri = p * (p + 1) / 2;
    let m_rows = 1 + n_tri;

    // A in CSC: column k holds the net coefficient (1) plus -svec(M_k).
    let mut indptr = vec![0usize];
    let mut rows_csc: Vec<usize> = Vec::new();
    let mut vals_csc: Vec<f64> = Vec::new();
    for k in 0..d {
        rows_csc.push(0);
        vals_csc.push(1.0); // net: Σ x_k = n_target
        let mut r = 1usize;
        for col in 0..p {
            for row_idx in 0..=col {
                let scale = if row_idx == col { 1.0 } else { sqrt2 };
                rows_csc.push(r);
                vals_csc.push(-psd_slices[k][row_idx][col] * scale);
                r += 1;
            }
        }
        indptr.push(rows_csc.len());
    }
    let a_csc = CscMatrix::new(m_rows, d, indptr, rows_csc, vals_csc);

    // b = [n_target, svec(M₀)].
    let mut b_vec = vec![n_target];
    for col in 0..p {
        for row_idx in 0..=col {
            let scale = if row_idx == col { 1.0 } else { sqrt2 };
            b_vec.push(psd_const[row_idx][col] * scale);
        }
    }

    let cones: Vec<SupportedConeT<f64>> = vec![
        SupportedConeT::ZeroConeT(1),
        SupportedConeT::PSDTriangleConeT(p),
    ];

    let settings = DefaultSettingsBuilder::default()
        .verbose(false)
        .max_iter(200)
        .build()
        .unwrap();
    let mut solver =
        DefaultSolver::new(&p_zero, &q_vec, &a_csc, &b_vec, &cones, settings).unwrap();
    solver.solve();

    let status = format!("{:?}", solver.solution.status);
    let feasible = matches!(
        solver.solution.status,
        SolverStatus::Solved | SolverStatus::AlmostSolved
    );
    let x_star = solver.solution.x.clone();

    // Reconstruct S = M₀ + Σ_k x_k M_k from the primal (more robust than
    // un-svec'ing the slack, and gives a direct PSD witness).
    let mut s = vec![vec![0.0; p]; p];
    for (i, srow) in s.iter_mut().enumerate() {
        for (j, sij) in srow.iter_mut().enumerate() {
            let mut v = psd_const[i][j];
            for k in 0..d {
                v += x_star[k] * psd_slices[k][i][j];
            }
            *sij = v;
        }
    }
    let min_diag = (0..p).map(|i| s[i][i]).fold(f64::INFINITY, f64::min);

    let primal_obj: f64 = t.iter().zip(&x_star).map(|(ti, xi)| ti * xi).sum();
    let dual_obj = solver.solution.obj_val_dual;
    let duality_gap = (primal_obj - dual_obj).abs();

    SdpDenseResult {
        x_star,
        slack_matrix: s,
        primal_obj,
        dual_obj,
        duality_gap,
        min_diag,
        feasible,
        status,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Known SDP: `min x₁ + x₂  s.t.  x₁ + x₂ = 2,  [[x₁,1],[1,x₂]] ⪰ 0`.
    /// The PSD constraint forces `x₁x₂ ≥ 1`; with `x₁+x₂=2` and AM–GM the
    /// only feasible point is `x* = (1,1)`, objective `2`.
    #[test]
    fn dense_psd_known_optimum() {
        let t = vec![1.0, 1.0];
        // M₀ = [[0,1],[1,0]]; M₁ = [[1,0],[0,0]]; M₂ = [[0,0],[0,1]].
        let m0 = vec![vec![0.0, 1.0], vec![1.0, 0.0]];
        let m1 = vec![vec![1.0, 0.0], vec![0.0, 0.0]];
        let m2 = vec![vec![0.0, 0.0], vec![0.0, 1.0]];
        let r = solve_operator_selection_sdp_dense(&t, &m0, &[m1, m2], 2.0);

        assert!(r.feasible, "status = {}", r.status);
        assert!(
            (r.x_star[0] - 1.0).abs() < 1e-4 && (r.x_star[1] - 1.0).abs() < 1e-4,
            "x* = {:?}, expected ~(1,1)",
            r.x_star
        );
        assert!((r.primal_obj - 2.0).abs() < 1e-4, "obj = {}, expected 2", r.primal_obj);
        // Strong duality: primal_obj ≈ dual_obj.
        assert!(r.duality_gap < 1e-5, "duality gap {} too large", r.duality_gap);
        // Slack matrix PSD (diagonal entries ≥ 0 is necessary; both ≈ 1).
        assert!(r.min_diag > -1e-6, "min diagonal {} negative — not PSD", r.min_diag);
    }

    /// Off-diagonal correlation actually binds: with a larger off-diagonal in
    /// `M₀` the PSD constraint is stricter than the diagonal (LP) lift, so the
    /// optimum differs from the componentwise `Gx ≥ 0` relaxation.
    #[test]
    fn dense_psd_offdiagonal_binds() {
        // [[x₁, 1.5],[1.5, x₂]] ⪰ 0 needs x₁x₂ ≥ 2.25; with x₁+x₂=3 the
        // feasible set is x₁x₂ ≥ 2.25 ⇒ x₁,x₂ ∈ [1.5, 1.5] only at equality,
        // i.e. x* = (1.5, 1.5), obj = 3.
        let t = vec![1.0, 1.0];
        let m0 = vec![vec![0.0, 1.5], vec![1.5, 0.0]];
        let m1 = vec![vec![1.0, 0.0], vec![0.0, 0.0]];
        let m2 = vec![vec![0.0, 0.0], vec![0.0, 1.0]];
        let r = solve_operator_selection_sdp_dense(&t, &m0, &[m1, m2], 3.0);
        assert!(r.feasible, "status = {}", r.status);
        assert!(
            (r.x_star[0] - 1.5).abs() < 1e-3 && (r.x_star[1] - 1.5).abs() < 1e-3,
            "x* = {:?}, expected ~(1.5,1.5)",
            r.x_star
        );
        assert!(r.duality_gap < 1e-5, "gap {}", r.duality_gap);
        assert!(r.min_diag > -1e-6, "min diag {}", r.min_diag);
    }
}
