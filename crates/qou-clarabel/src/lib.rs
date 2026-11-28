//! `qou-clarabel` — 80+ dps `MpfrFloat` operator-selection LP & dual shadow-price certifier (`3C`).
//!
//! Links directly against `Clarabel.rs` (`rev = "37f06c3"`, feature `mpfr`) at `>= 266` bits
//! (default `320` bits ≈ 96 dps, formatted to `80` dps) with zero `f64` round-trips.
//!
//! Per `H_3(q)` row `W`, solves and KKT-verifies three canonical operator-selection certificates:
//! 1. **6×6 NF-basis Frobenius Gram LP** (`min t·x s.t. 1^T x = net(W), G x >= 0, x >= -M`);
//! 2. **Full 3-partition Wedderburn LP** (`lambda in {(3), (2,1), (1,1,1)}`, `t_lambda = |c_lambda(W)|`,
//!    `G = diag(|c_lambda(W)|)`, `n_target = |tr_M(W)|`), applying the `2026-11-25` `qou-fu8c`
//!    identifiability rule: any block with `c_lambda(W) = 0` (always `(1,1,1)` under Convention D,
//!    plus any vanishing two-row block) emits `u_lambda_star = null` and `interval = ["0", "+inf"]`;
//! 3. **Two-row Quotient Wedderburn LP on `H_3(q)/rad`** (`lambda in {(3), (2,1)}`), yielding the
//!    row-dependent nonzero quotient shadow price `y0_quot_star` and dual pair `(u_(3), u_(2,1))`.

use clarabel::algebra::{set_mpfr_default_precision, CscMatrix, MpfrFloat};
use clarabel::solver::*;
use num_traits::{FromPrimitive, Signed, Zero};
use qou_gg_eval::h3::{gram_matrix_h3, trace_weights_h3, H3Elem, H3EvaluatedRow};
use qou_gg_eval::scalars::{fmt_dps, parse_dec, Q0Params, MIN_PREC_BITS};
use rug::Float;
use serde::{Deserialize, Serialize};
use serde_json::json;

pub type T = MpfrFloat;

/// Parse a full-precision decimal string into `Clarabel`'s `MpfrFloat` at the active thread-local precision.
pub fn parse_mpfr_str(s: &str) -> T {
    serde_json::from_value::<MpfrFloat>(json!([0, s]))
        .unwrap_or_else(|e| panic!("failed to parse MpfrFloat from {s:?}: {e}"))
}

/// Convert `MpfrFloat` back to a `rug::Float` at `prec_bits` via lossless decimal string formatting,
/// then round to `dps` decimal digits.
pub fn fmt_mpfr_dps(v: &T, prec_bits: u32, dps: usize) -> String {
    let raw = format!("{v}");
    let rf = parse_dec(prec_bits, &raw);
    fmt_dps(&rf, dps)
}

#[derive(Debug, Clone)]
pub struct RawClarabelLpSolve {
    pub x_star: Vec<T>,
    pub y0_star: T,
    pub y_star: Vec<T>,
    pub z_bound: Vec<T>,
    pub primal_obj: T,
    pub dual_obj_full: T,
    pub duality_gap: T,
    pub kkt_primal_res: T,
    pub kkt_dual_res: T,
    pub feasible: bool,
    pub status: String,
    pub tol_exponent_used: i32,
}

/// Solve `min t·x s.t. 1^T x = n_target, G x >= 0, x >= -M` in `MpfrFloat` at `prec_bits`.
/// Uses the KKT sign convention of `tools/hecke-engine/src/operator_selection_lp.rs`:
/// - Row `0`: `1^T x + s_eq = n_target`, `s_eq in ZeroConeT(1)` -> `y0 = -z_eq`
/// - Rows `1..=d`: `-G x + s_G = 0`, `s_G in NonnegativeConeT(d)` -> `y_i = z_G[i]`
/// - Rows `1+d..=2d`: `-I x + s_B = M*1`, `s_B in NonnegativeConeT(d)` -> `w_i = z_B[i]`.
pub fn solve_lp_mpfr(
    t: &[T],
    g: &[Vec<T>],
    n_target: &T,
    m_bound: &T,
    prec_bits: u32,
) -> RawClarabelLpSolve {
    assert!(
        prec_bits >= MIN_PREC_BITS,
        "prec_bits ({prec_bits}) < {MIN_PREC_BITS}"
    );
    set_mpfr_default_precision(prec_bits);
    let d = t.len();
    assert_eq!(g.len(), d);

    let p_zero: CscMatrix<T> = CscMatrix::<T>::zeros((d, d));
    let q_vec: Vec<T> = t.to_vec();
    let m_rows = 1 + 2 * d;

    let mut indptr: Vec<usize> = vec![0];
    let mut rows_csc: Vec<usize> = Vec::new();
    let mut vals_csc: Vec<T> = Vec::new();
    for c in 0..d {
        rows_csc.push(0);
        vals_csc.push(T::from_i64(1).unwrap());
        for (i, g_row) in g.iter().enumerate() {
            rows_csc.push(1 + i);
            vals_csc.push(-g_row[c].clone());
        }
        rows_csc.push(1 + d + c);
        vals_csc.push(T::from_i64(-1).unwrap());
        indptr.push(rows_csc.len());
    }
    let a_csc = CscMatrix::new(m_rows, d, indptr, rows_csc, vals_csc);

    let mut b_vec: Vec<T> = Vec::with_capacity(m_rows);
    b_vec.push(n_target.clone());
    for _ in 0..d {
        b_vec.push(T::zero());
    }
    for _ in 0..d {
        b_vec.push(m_bound.clone());
    }

    let cones: Vec<SupportedConeT<T>> = vec![
        SupportedConeT::ZeroConeT(1),
        SupportedConeT::NonnegativeConeT(d),
        SupportedConeT::NonnegativeConeT(d),
    ];

    // Probe actual working decimal precision of MpfrFloat
    let one = T::from_i64(1).unwrap();
    let mut usable_dps = 0f64;
    for k in 1..=300i32 {
        let probe = one.clone() + T::from_f64(10f64.powi(-k)).unwrap();
        if probe == one {
            break;
        }
        usable_dps = f64::from(k);
    }
    let dps = (f64::from(prec_bits) * std::f64::consts::LOG10_2).min(usable_dps);
    let e_tight = ((0.8 * dps).floor() as i32).clamp(12, 300);
    let max_iter = 200u32 + 12 * ((dps - 16.0).max(0.0) as u32);

    let mut e_used = e_tight;
    let mut solver;
    let mut ladder: Vec<String> = Vec::new();
    loop {
        let eps_i = T::from_f64(10f64.powi(-e_used)).unwrap();
        let eps_red_i = T::from_f64(10f64.powi(-((e_used as f64 * 0.625).floor() as i32))).unwrap();
        let settings = DefaultSettingsBuilder::default()
            .verbose(false)
            .max_iter(max_iter)
            .tol_gap_abs(eps_i.clone())
            .tol_gap_rel(eps_i.clone())
            .tol_feas(eps_i)
            .reduced_tol_gap_abs(eps_red_i.clone())
            .reduced_tol_gap_rel(eps_red_i.clone())
            .reduced_tol_feas(eps_red_i)
            .build()
            .unwrap();
        solver = DefaultSolver::new(&p_zero, &q_vec, &a_csc, &b_vec, &cones, settings).unwrap();
        solver.solve();

        let converged = matches!(
            solver.solution.status,
            SolverStatus::Solved | SolverStatus::AlmostSolved
        );
        let decided = matches!(
            solver.solution.status,
            SolverStatus::PrimalInfeasible
                | SolverStatus::DualInfeasible
                | SolverStatus::AlmostPrimalInfeasible
                | SolverStatus::AlmostDualInfeasible
        );
        if converged || decided || e_used <= 12 {
            break;
        }
        ladder.push(format!("{:?}@1e-{}", solver.solution.status, e_used));
        e_used = (e_used - 8).max(12);
    }

    let feasible = matches!(
        solver.solution.status,
        SolverStatus::Solved | SolverStatus::AlmostSolved
    );
    let mut status = format!("{:?}", solver.solution.status);
    if !ladder.is_empty() {
        status = format!("{status}@1e-{e_used} after [{}]", ladder.join(", "));
    }

    let x_star: Vec<T> = solver.solution.x.clone();
    let z = &solver.solution.z;
    let y0_star = -z[0].clone();
    let y_star: Vec<T> = (0..d).map(|i| z[1 + i].clone()).collect();
    let z_bound: Vec<T> = (0..d).map(|i| z[1 + d + i].clone()).collect();

    let mut primal_obj = T::zero();
    let mut sum_x = T::zero();
    let mut sum_zb = T::zero();
    for c in 0..d {
        primal_obj = primal_obj + t[c].clone() * x_star[c].clone();
        sum_x = sum_x + x_star[c].clone();
        sum_zb = sum_zb + z_bound[c].clone();
    }
    let dual_obj_full = n_target.clone() * y0_star.clone() - m_bound.clone() * sum_zb;
    let duality_gap = (primal_obj.clone() - dual_obj_full.clone()).abs();

    // Independent KKT primal residual: max(|1^T x - n_target|, max_i max(0, -(Gx)_i), max_i max(0, -x_i - M))
    let mut kkt_primal_res = (sum_x - n_target.clone()).abs();
    for i in 0..d {
        let mut gx_i = T::zero();
        for j in 0..d {
            gx_i = gx_i + g[i][j].clone() * x_star[j].clone();
        }
        let viol_g = -gx_i;
        if viol_g > kkt_primal_res {
            kkt_primal_res = viol_g;
        }
        let viol_b = -x_star[i].clone() - m_bound.clone();
        if viol_b > kkt_primal_res {
            kkt_primal_res = viol_b;
        }
    }

    // Independent KKT dual stationarity residual: max_j |t_j - y0 - (G^T y)_j - z_bound_j|
    let mut kkt_dual_res = T::zero();
    for j in 0..d {
        let mut gty_j = T::zero();
        for i in 0..d {
            gty_j = gty_j + g[i][j].clone() * y_star[i].clone();
        }
        let res_j = (t[j].clone() - y0_star.clone() - gty_j - z_bound[j].clone()).abs();
        if res_j > kkt_dual_res {
            kkt_dual_res = res_j;
        }
    }

    RawClarabelLpSolve {
        x_star,
        y0_star,
        y_star,
        z_bound,
        primal_obj,
        dual_obj_full,
        duality_gap,
        kkt_primal_res,
        kkt_dual_res,
        feasible,
        status,
        tol_exponent_used: e_used,
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct NfGramLpCertificate {
    pub status: String,
    pub feasible: bool,
    pub tol_exponent_used: i32,
    pub n_target_net: String,
    pub y0_star: String,
    pub y_star: [String; 6],
    pub active_basis_names: Vec<String>,
    pub primal_obj: String,
    pub dual_obj: String,
    pub duality_gap: String,
    pub kkt_primal_residual: String,
    pub kkt_dual_residual: String,
    pub min_row_gram_slack: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WedderburnPartitionDual {
    pub partition: String,
    pub abs_contrib: String,
    pub u_identified: bool,
    pub u_lambda_star: Option<String>,
    pub u_lambda_star_interval: Option<[String; 2]>,
    pub is_active: Option<bool>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WedderburnLpCertificate {
    pub scope: String,
    pub status: String,
    pub feasible: bool,
    pub tol_exponent_used: i32,
    pub n_target_abs_tr_m: String,
    pub y0_star: String,
    pub primal_obj: String,
    pub dual_obj: String,
    pub duality_gap: String,
    pub kkt_primal_residual: String,
    pub kkt_dual_residual: String,
    pub partitions: Vec<WedderburnPartitionDual>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HadronRowLpCertificate {
    pub row_id: String,
    pub prec_bits: u32,
    pub backend: String,
    pub nf_gram_lp: NfGramLpCertificate,
    pub wedderburn_full_lp: WedderburnLpCertificate,
    pub wedderburn_quotient_lp: WedderburnLpCertificate,
}

fn build_wedderburn_cert(
    scope: &str,
    part_names: &[&str],
    abs_contribs_rug: &[Float],
    abs_tr_m_rug: &Float,
    prec_bits: u32,
    dps: usize,
) -> WedderburnLpCertificate {
    set_mpfr_default_precision(prec_bits);
    let d = part_names.len();
    let zero_guard = parse_dec(prec_bits, "1e-75");
    let active_guard = parse_dec(prec_bits, "1e-20");

    // Clean exact-zero entries (`|c_lambda| < 1e-75`) before handing to Clarabel
    let mut is_zero = vec![false; d];
    let mut t_mpfr = Vec::with_capacity(d);
    for (i, c) in abs_contribs_rug.iter().enumerate() {
        if c.clone().abs() < zero_guard {
            is_zero[i] = true;
            t_mpfr.push(T::zero());
        } else {
            t_mpfr.push(parse_mpfr_str(&fmt_dps(c, dps + 10)));
        }
    }
    let mut g_mpfr = vec![vec![T::zero(); d]; d];
    for i in 0..d {
        g_mpfr[i][i] = t_mpfr[i].clone();
    }
    let n_target_str = fmt_dps(abs_tr_m_rug, dps + 10);
    let n_target_mpfr = parse_mpfr_str(&n_target_str);
    let m_bound_mpfr = parse_mpfr_str("1000000");

    let raw = solve_lp_mpfr(&t_mpfr, &g_mpfr, &n_target_mpfr, &m_bound_mpfr, prec_bits);

    // Apply `qou-fu8c` (2026-11-25) identifiability rule:
    // If `c_lambda = 0`, `u_lambda` does not appear in the dual stationarity equation (`0 * u_lambda`)
    // and ranges freely over `[0, +inf)` on the optimal dual face -> publish `null` + `["0", "+inf"]`.
    // Also if `n_target == 0` AND `c_lambda > 0`, check dual stationarity: `y_0 <= min_j |c_j|` with
    // dual objective `0 * y_0 = 0`, so `y_0` itself would range on `(-inf, min |c|]` ONLY when `n_target == 0`!
    let n_is_zero = abs_tr_m_rug.clone().abs() < zero_guard;
    let mut partitions = Vec::with_capacity(d);
    for i in 0..d {
        let u_id = !is_zero[i] && !n_is_zero;
        if u_id {
            let u_rug = parse_dec(prec_bits, &format!("{}", raw.y_star[i]));
            let act = u_rug > active_guard;
            partitions.push(WedderburnPartitionDual {
                partition: part_names[i].to_string(),
                abs_contrib: if is_zero[i] {
                    "0".to_string()
                } else {
                    fmt_dps(&abs_contribs_rug[i], dps)
                },
                u_identified: true,
                u_lambda_star: Some(fmt_dps(&u_rug, dps)),
                u_lambda_star_interval: None,
                is_active: Some(act),
            });
        } else {
            partitions.push(WedderburnPartitionDual {
                partition: part_names[i].to_string(),
                abs_contrib: if is_zero[i] {
                    "0".to_string()
                } else {
                    fmt_dps(&abs_contribs_rug[i], dps)
                },
                u_identified: false,
                u_lambda_star: None,
                u_lambda_star_interval: Some(["0".to_string(), "+inf".to_string()]),
                is_active: None,
            });
        }
    }

    WedderburnLpCertificate {
        scope: scope.to_string(),
        status: raw.status,
        feasible: raw.feasible,
        tol_exponent_used: raw.tol_exponent_used,
        n_target_abs_tr_m: fmt_dps(abs_tr_m_rug, dps),
        y0_star: fmt_mpfr_dps(&raw.y0_star, prec_bits, dps),
        primal_obj: fmt_mpfr_dps(&raw.primal_obj, prec_bits, dps),
        dual_obj: fmt_mpfr_dps(&raw.dual_obj_full, prec_bits, dps),
        duality_gap: fmt_mpfr_dps(&raw.duality_gap, prec_bits, dps),
        kkt_primal_residual: fmt_mpfr_dps(&raw.kkt_primal_res, prec_bits, dps),
        kkt_dual_residual: fmt_mpfr_dps(&raw.kkt_dual_res, prec_bits, dps),
        partitions,
    }
}

/// Certify all `H_3(q)` rows via Clarabel `MpfrFloat` at `prec_bits`.
pub fn certify_all_h3_rows(
    params: &Q0Params,
    rows: &[(H3Elem, H3EvaluatedRow)],
    dps: usize,
) -> Vec<HadronRowLpCertificate> {
    let p = params.prec_bits;
    set_mpfr_default_precision(p);

    let tw_rug = trace_weights_h3(params);
    let g_rug = gram_matrix_h3(params);

    let t_nf: Vec<T> = tw_rug
        .iter()
        .map(|x| parse_mpfr_str(&fmt_dps(x, dps + 10)))
        .collect();
    let g_nf: Vec<Vec<T>> = g_rug
        .iter()
        .map(|r| {
            r.iter()
                .map(|x| parse_mpfr_str(&fmt_dps(x, dps + 10)))
                .collect()
        })
        .collect();
    let m_bound = parse_mpfr_str("1000000");
    let active_guard = parse_dec(p, "1e-20");

    let mut certs = Vec::with_capacity(rows.len());
    for (elem, eval_row) in rows {
        let net_rug = elem.net();
        let n_target_nf = parse_mpfr_str(&fmt_dps(&net_rug, dps + 10));
        let raw_nf = solve_lp_mpfr(&t_nf, &g_nf, &n_target_nf, &m_bound, p);

        let y_star_strs: [String; 6] =
            std::array::from_fn(|i| fmt_mpfr_dps(&raw_nf.y_star[i], p, dps));
        let mut active_names = Vec::new();
        for (i, name) in qou_gg_eval::h3::H3_BASIS_NAMES.iter().enumerate() {
            let yi = parse_dec(p, &format!("{}", raw_nf.y_star[i]));
            if yi > active_guard {
                active_names.push((*name).to_string());
            }
        }

        let nf_gram_lp = NfGramLpCertificate {
            status: raw_nf.status,
            feasible: raw_nf.feasible,
            tol_exponent_used: raw_nf.tol_exponent_used,
            n_target_net: eval_row.net.clone(),
            y0_star: fmt_mpfr_dps(&raw_nf.y0_star, p, dps),
            y_star: y_star_strs,
            active_basis_names: active_names,
            primal_obj: fmt_mpfr_dps(&raw_nf.primal_obj, p, dps),
            dual_obj: fmt_mpfr_dps(&raw_nf.dual_obj_full, p, dps),
            duality_gap: fmt_mpfr_dps(&raw_nf.duality_gap, p, dps),
            kkt_primal_residual: fmt_mpfr_dps(&raw_nf.kkt_primal_res, p, dps),
            kkt_dual_residual: fmt_mpfr_dps(&raw_nf.kkt_dual_res, p, dps),
            min_row_gram_slack: eval_row.min_gram_slack.clone(),
        };

        let abs_c3 = parse_dec(p, &eval_row.contrib_3).abs();
        let abs_c21 = parse_dec(p, &eval_row.contrib_21).abs();
        let abs_c111 = Float::with_val(p, 0);
        let abs_tr = parse_dec(p, &eval_row.abs_tr_m);

        let wedderburn_full_lp = build_wedderburn_cert(
            "full_H3_partitions_[(3),(2,1),(1,1,1)]",
            &["(3)", "(2,1)", "(1,1,1)"],
            &[abs_c3.clone(), abs_c21.clone(), abs_c111],
            &abs_tr,
            p,
            dps,
        );
        let wedderburn_quotient_lp = build_wedderburn_cert(
            "two_row_quotient_H3_mod_rad_[(3),(2,1)]",
            &["(3)", "(2,1)"],
            &[abs_c3, abs_c21],
            &abs_tr,
            p,
            dps,
        );

        certs.push(HadronRowLpCertificate {
            row_id: eval_row.id.clone(),
            prec_bits: p,
            backend: "clarabel-mpfr@37f06c3".to_string(),
            nf_gram_lp,
            wedderburn_full_lp,
            wedderburn_quotient_lp,
        });
    }

    certs
}

#[cfg(test)]
mod tests {
    use super::*;
    use qou_gg_eval::h3::build_all_h3_rows;

    #[test]
    fn clarabel_mpfr_certifies_all_h3_rows_to_high_precision() {
        let params = Q0Params::proton_pinned(320, None);
        let (rows, _) = build_all_h3_rows(&params, 80);
        let certs = certify_all_h3_rows(&params, &rows, 80);
        assert_eq!(certs.len(), rows.len());

        let loose_bound = parse_dec(320, "1e-50");
        for cert in &certs {
            assert!(
                cert.nf_gram_lp.feasible,
                "NF Gram LP failed on {}",
                cert.row_id
            );
            let gap_nf = parse_dec(320, &cert.nf_gram_lp.duality_gap);
            let kkt_d_nf = parse_dec(320, &cert.nf_gram_lp.kkt_dual_residual);
            assert!(
                gap_nf < loose_bound,
                "NF duality gap too large on {}: {gap_nf}",
                cert.row_id
            );
            assert!(
                kkt_d_nf < loose_bound,
                "NF KKT dual residual too large on {}: {kkt_d_nf}",
                cert.row_id
            );

            // Check qou-fu8c rule on full Wedderburn LP: (1,1,1) MUST be unidentified (`None`, `["0", "+inf"]`)
            let p111 = &cert.wedderburn_full_lp.partitions[2];
            assert_eq!(p111.partition, "(1,1,1)");
            assert!(!p111.u_identified);
            assert!(p111.u_lambda_star.is_none());
            assert_eq!(
                p111.u_lambda_star_interval,
                Some(["0".to_string(), "+inf".to_string()])
            );

            // Check two-row quotient LP feasibility & KKT residual
            assert!(
                cert.wedderburn_quotient_lp.feasible,
                "Quotient LP failed on {}",
                cert.row_id
            );
            let gap_q = parse_dec(320, &cert.wedderburn_quotient_lp.duality_gap);
            assert!(
                gap_q < loose_bound,
                "Quotient duality gap too large on {}: {gap_q}",
                cert.row_id
            );
        }
    }
}
