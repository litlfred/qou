//! General operator-selection LP — MPFR (arbitrary-precision) backend.
//!
//! Mirrors `pyhecke.lp_dual_solver.solve_operator_selection_lp`
//! (`prop:operator-selection-lp`) but solves with the Clarabel MPFR
//! backend at configurable bit-precision (167 bits ≈ 50 dps, the
//! QOU L1 floor) instead of SciPy HiGHS at `f64`.
//!
//! Primal:
//! ```text
//!     min  t · x
//!     s.t. 1ᵀ x = n_target          (net constraint)
//!          G x ≥ 0                   (Frobenius positivity)
//!          x_i ≥ -M                  (boundedness)
//! ```
//! Dual variables are the binding-energy shadow prices: `y0` (net) and
//! `y_i ≥ 0` (Frobenius), with the active set `{ i : y_i > tol }`.
//!
//! ## Clarabel cone layout (this module's convention)
//!
//! Clarabel solves `min ½xᵀPx + qᵀx  s.t.  A x + s = b,  s ∈ K`.
//! We set `P = 0`, `q = t`, and stack three cone blocks in this order:
//!
//! | block | rows | `A` rows | `b` | cone |
//! |-------|------|----------|-----|------|
//! | net (eq)        | 1   | `1ᵀ`  | `n_target` | `ZeroConeT(1)` |
//! | Frobenius `Gx≥0`| `d` | `-G`  | `0`        | `NonnegativeConeT(d)` |
//! | bounds `x≥-M`   | `d` | `-I`  | `M·1`      | `NonnegativeConeT(d)` |
//!
//! KKT stationarity `q + Aᵀ z = 0` then reads
//! `t = -z_eq·1 + Gᵀ z_G + z_bound`, so the Python conventions map to
//! Clarabel's `z` as **`y0 = -z_eq`** and **`y_i = z_G[i]`**.  These
//! sign choices are *proved* by the `kkt_*` / `complementary_slackness`
//! unit tests below, not assumed.
//!
//! Required feature: `clarabel-mpfr`.

use clarabel::algebra::{set_mpfr_default_precision, CscMatrix, MpfrFloat};
use clarabel::solver::*;
use num_traits::{FromPrimitive, Signed, Zero};

/// Working scalar: a run-time-precision MPFR float.
pub type T = MpfrFloat;

/// 167 bits ≈ 50 decimal places — the QOU L1 compute floor.
pub const DEFAULT_PREC_BITS: u32 = 167;

/// Both sides of the operator-selection LP plus the strong-duality check.
/// Field names match `pyhecke.lp_dual_solver.LpDualResult.to_dict()`.
#[derive(Debug, Clone)]
pub struct OpSelLpResult {
    pub x_star: Vec<T>,
    pub y0_star: T,
    pub y_star: Vec<T>,
    pub active_set: Vec<usize>,
    pub primal_obj: T,
    pub dual_obj: T,
    pub duality_gap: T,
    pub feasible: bool,
    pub status: String,
}

#[inline]
fn zero() -> T {
    T::zero()
}

/// Solve the operator-selection LP at `prec_bits` MPFR precision.
///
/// * `t`        — objective / Markov traces, length `d`.
/// * `g`        — Frobenius Gram, `d × d`, row-major (`g[i][j]`).
/// * `n_target` — net-constraint right-hand side.
/// * `m_bound`  — lower bound `-M` on each `x_i` (pass a large positive `M`).
/// * `dual_tol` — threshold above which a dual `y_i` counts as active.
/// * `prec_bits`— MPFR working precision in bits (167 ≈ 50 dps).
///
/// Returns primal `x*`, dual `(y0, y)`, the active set, both objectives,
/// the duality gap, and a feasibility flag + raw solver status string.
pub fn solve_operator_selection_lp(
    t: &[T],
    g: &[Vec<T>],
    n_target: &T,
    m_bound: &T,
    dual_tol: &T,
    prec_bits: u32,
) -> OpSelLpResult {
    set_mpfr_default_precision(prec_bits);
    let d = t.len();
    assert_eq!(g.len(), d, "Gram row count {} != d {}", g.len(), d);
    for (i, row) in g.iter().enumerate() {
        assert_eq!(row.len(), d, "Gram row {i} has length {} != d {}", row.len(), d);
    }

    // P = 0 (linear program).
    let p_zero: CscMatrix<T> = CscMatrix::<T>::zeros((d, d));
    // q = t.
    let q_vec: Vec<T> = t.to_vec();

    // Row index ranges.
    //   row 0                : net equality
    //   rows 1 ..= d         : Frobenius  Gx ≥ 0   (A = -G)
    //   rows 1+d ..= 2d      : bounds     x ≥ -M   (A = -I)
    let m_rows = 1 + 2 * d;

    // Build A column-by-column (CSC). For column c the nonzeros are, in
    // ascending row order:
    //   (0,           +1)            — net
    //   (1+i,         -g[i][c])      — Frobenius, all i
    //   (1+d+c,       -1)            — bound (diagonal)
    let mut indptr: Vec<usize> = vec![0];
    let mut rows_csc: Vec<usize> = Vec::new();
    let mut vals_csc: Vec<T> = Vec::new();
    for c in 0..d {
        // net
        rows_csc.push(0);
        vals_csc.push(T::from_i64(1).unwrap());
        // Frobenius -g[i][c]
        for i in 0..d {
            rows_csc.push(1 + i);
            vals_csc.push(-g[i][c].clone());
        }
        // bound -1 (diagonal)
        rows_csc.push(1 + d + c);
        vals_csc.push(T::from_i64(-1).unwrap());
        indptr.push(rows_csc.len());
    }
    let a_csc = CscMatrix::new(m_rows, d, indptr, rows_csc, vals_csc);

    // b = [n_target, 0×d, M×d].
    let mut b_vec: Vec<T> = Vec::with_capacity(m_rows);
    b_vec.push(n_target.clone());
    for _ in 0..d {
        b_vec.push(zero());
    }
    for _ in 0..d {
        b_vec.push(m_bound.clone());
    }

    let cones: Vec<SupportedConeT<T>> = vec![
        SupportedConeT::ZeroConeT(1),
        SupportedConeT::NonnegativeConeT(d), // Gx ≥ 0
        SupportedConeT::NonnegativeConeT(d), // x ≥ -M
    ];

    // Tolerances: exploit MPFR headroom past the f64 floor (~1e-8).
    let eps = T::from_f64(1e-15).unwrap();
    let eps_red = T::from_f64(1e-10).unwrap();
    let settings = DefaultSettingsBuilder::default()
        .verbose(false)
        .max_iter(200)
        .tol_gap_abs(eps.clone())
        .tol_gap_rel(eps.clone())
        .tol_feas(eps.clone())
        .reduced_tol_gap_abs(eps_red.clone())
        .reduced_tol_gap_rel(eps_red.clone())
        .reduced_tol_feas(eps_red)
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

    let x_star: Vec<T> = solver.solution.x.clone();
    let z = &solver.solution.z;

    // Dual extraction per the cone layout above.
    let y0_star = -z[0].clone(); // y0 = -z_eq
    let y_star: Vec<T> = (0..d).map(|i| z[1 + i].clone()).collect(); // y_i = z_G[i]
    let active_set: Vec<usize> = (0..d)
        .filter(|&i| y_star[i] > *dual_tol)
        .collect();

    // primal_obj = t·x  (== solver.solution.obj_val).
    let mut primal_obj = zero();
    for c in 0..d {
        primal_obj = primal_obj + t[c].clone() * x_star[c].clone();
    }
    // dual_obj = n_target · y0  (matches the Python LpDualResult).
    let dual_obj = n_target.clone() * y0_star.clone();
    let duality_gap = (primal_obj.clone() - dual_obj.clone()).abs();

    OpSelLpResult {
        x_star,
        y0_star,
        y_star,
        active_set,
        primal_obj,
        dual_obj,
        duality_gap,
        feasible,
        status,
    }
}

/// Convert an `MpfrFloat` to `f64` via its decimal `Display` (lossy —
/// for JSON summary fields only; the full-precision value stays in `T`).
pub fn to_f64(v: &T) -> f64 {
    format!("{}", v).parse::<f64>().unwrap_or(f64::NAN)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn f(x: f64) -> T {
        T::from_f64(x).unwrap()
    }

    /// The 3-channel dummy LP from `lp_dual_solver.py`'s smoke test.
    fn dummy() -> (Vec<T>, Vec<Vec<T>>, T) {
        let t = vec![f(1.0), f(0.5), f(0.3)];
        let g = vec![
            vec![f(1.0), f(0.2), f(0.1)],
            vec![f(0.2), f(1.0), f(0.3)],
            vec![f(0.1), f(0.3), f(1.0)],
        ];
        (t, g, f(1.0))
    }

    #[test]
    fn solves_and_is_feasible() {
        set_mpfr_default_precision(DEFAULT_PREC_BITS);
        let (t, g, n) = dummy();
        let r = solve_operator_selection_lp(
            &t, &g, &n, &f(1e6), &f(1e-9), DEFAULT_PREC_BITS,
        );
        assert!(r.feasible, "status = {}", r.status);
        assert_eq!(r.x_star.len(), 3);
        assert_eq!(r.y_star.len(), 3);
    }

    #[test]
    fn strong_duality_gap_is_zero() {
        set_mpfr_default_precision(DEFAULT_PREC_BITS);
        let (t, g, n) = dummy();
        let r = solve_operator_selection_lp(
            &t, &g, &n, &f(1e6), &f(1e-9), DEFAULT_PREC_BITS,
        );
        // primal_obj == dual_obj == n_target · y0  ⇒ the y0 sign is right.
        assert!(
            r.duality_gap < f(1e-6),
            "duality gap {} too large (primal {}, dual {})",
            to_f64(&r.duality_gap),
            to_f64(&r.primal_obj),
            to_f64(&r.dual_obj),
        );
    }

    #[test]
    fn kkt_stationarity_holds() {
        // t = y0·1 + Gᵀy + z_bound, with y0 = -z_eq, y_i = z_G[i].
        // For inactive bounds (interior x) z_bound ≈ 0, so check
        //   | t[c] - ( y0 + Σ_i g[i][c]·y_i ) |  small  (G symmetric).
        set_mpfr_default_precision(DEFAULT_PREC_BITS);
        let (t, g, n) = dummy();
        let d = t.len();
        let r = solve_operator_selection_lp(
            &t, &g, &n, &f(1e6), &f(1e-9), DEFAULT_PREC_BITS,
        );
        for c in 0..d {
            let mut recon = r.y0_star.clone();
            for i in 0..d {
                recon = recon + g[i][c].clone() * r.y_star[i].clone();
            }
            let resid = (t[c].clone() - recon).abs();
            // bound multiplier may absorb a little; loose tol on f64-seeded data
            assert!(
                resid < f(1e-5),
                "KKT residual at c={c} is {} (too large)",
                to_f64(&resid),
            );
        }
    }

    #[test]
    fn complementary_slackness_holds() {
        // y_i · (Gx)_i ≈ 0 for every channel.
        set_mpfr_default_precision(DEFAULT_PREC_BITS);
        let (t, g, n) = dummy();
        let d = t.len();
        let r = solve_operator_selection_lp(
            &t, &g, &n, &f(1e6), &f(1e-9), DEFAULT_PREC_BITS,
        );
        for i in 0..d {
            let mut gx_i = zero();
            for c in 0..d {
                gx_i = gx_i + g[i][c].clone() * r.x_star[c].clone();
            }
            let cs = (r.y_star[i].clone() * gx_i).abs();
            assert!(
                cs < f(1e-5),
                "complementary slackness violated at i={i}: y·(Gx) = {}",
                to_f64(&cs),
            );
        }
    }

    #[test]
    fn dual_multipliers_are_nonnegative() {
        set_mpfr_default_precision(DEFAULT_PREC_BITS);
        let (t, g, n) = dummy();
        let r = solve_operator_selection_lp(
            &t, &g, &n, &f(1e6), &f(1e-9), DEFAULT_PREC_BITS,
        );
        // Frobenius cone duals must be ≥ 0 (within IPM tol).
        for (i, y) in r.y_star.iter().enumerate() {
            assert!(
                *y > f(-1e-6),
                "y_star[{i}] = {} is significantly negative",
                to_f64(y),
            );
        }
    }
}
