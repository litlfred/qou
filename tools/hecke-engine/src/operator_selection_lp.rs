//! Operator-selection LP — generic over the Clarabel scalar.
//!
//! Mirrors `pyhecke.lp_dual_solver.solve_operator_selection_lp`
//! (`prop:operator-selection-lp`) but solves with Clarabel.  **Production
//! uses `MpfrFloat`** (167 bits ≈ 50 dps, the QOU L1 floor) — there is no
//! `f64` in production.  The function is generic over `F: FloatT` for ONE
//! reason: it lets a unit test solve the *same* LP with `f64` and with
//! `MpfrFloat` in-process and assert they agree, validating that the MPFR
//! backend introduces no discrepancy versus an independent float solve.
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

use clarabel::algebra::{set_mpfr_default_precision, CscMatrix, FloatT, MpfrFloat};
use clarabel::solver::*;
use num_traits::{FromPrimitive, Signed, Zero};
use std::fmt::Display;

/// Production scalar: a run-time-precision MPFR float (≈50 dps). The CLI and
/// every production caller use this. `f64` is used ONLY by the validation
/// tests, to confirm the MPFR solve agrees with an independent float solve.
pub type T = MpfrFloat;

/// 167 bits ≈ 50 decimal places — the QOU L1 compute floor.
pub const DEFAULT_PREC_BITS: u32 = 167;

/// Both sides of the operator-selection LP plus the strong-duality check.
/// Field names match `pyhecke.lp_dual_solver.LpDualResult.to_dict()`.
#[derive(Debug, Clone)]
pub struct OpSelLpResult<F> {
    pub x_star: Vec<F>,
    pub y0_star: F,
    pub y_star: Vec<F>,
    pub active_set: Vec<usize>,
    pub primal_obj: F,
    pub dual_obj: F,
    pub duality_gap: F,
    pub feasible: bool,
    pub status: String,
}

/// Solve the operator-selection LP, generic over the Clarabel scalar `F`
/// (`MpfrFloat` in production; `f64` only for cross-validation).
///
/// * `t`        — objective / Markov traces, length `d`.
/// * `g`        — Frobenius Gram, `d × d`, row-major (`g[i][j]`).
/// * `n_target` — net-constraint right-hand side.
/// * `m_bound`  — lower bound `-M` on each `x_i` (pass a large positive `M`).
/// * `dual_tol` — threshold above which a dual `y_i` counts as active.
/// * `prec_bits`— MPFR working precision in bits (167 ≈ 50 dps). Sets the
///   thread-local MPFR default; ignored (harmless) for non-MPFR `F`.
///
/// Returns primal `x*`, dual `(y0, y)`, the active set, both objectives,
/// the duality gap, and a feasibility flag + raw solver status string.
pub fn solve_operator_selection_lp<F: FloatT>(
    t: &[F],
    g: &[Vec<F>],
    n_target: &F,
    m_bound: &F,
    dual_tol: &F,
    prec_bits: u32,
) -> OpSelLpResult<F> {
    set_mpfr_default_precision(prec_bits);
    let d = t.len();
    assert_eq!(g.len(), d, "Gram row count {} != d {}", g.len(), d);
    for (i, row) in g.iter().enumerate() {
        assert_eq!(row.len(), d, "Gram row {i} has length {} != d {}", row.len(), d);
    }

    // P = 0 (linear program).
    let p_zero: CscMatrix<F> = CscMatrix::<F>::zeros((d, d));
    // q = t.
    let q_vec: Vec<F> = t.to_vec();

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
    let mut vals_csc: Vec<F> = Vec::new();
    for c in 0..d {
        // net
        rows_csc.push(0);
        vals_csc.push(F::from_i64(1).unwrap());
        // Frobenius -g[i][c]
        for i in 0..d {
            rows_csc.push(1 + i);
            vals_csc.push(-g[i][c].clone());
        }
        // bound -1 (diagonal)
        rows_csc.push(1 + d + c);
        vals_csc.push(F::from_i64(-1).unwrap());
        indptr.push(rows_csc.len());
    }
    let a_csc = CscMatrix::new(m_rows, d, indptr, rows_csc, vals_csc);

    // b = [n_target, 0×d, M×d].
    let mut b_vec: Vec<F> = Vec::with_capacity(m_rows);
    b_vec.push(n_target.clone());
    for _ in 0..d {
        b_vec.push(F::zero());
    }
    for _ in 0..d {
        b_vec.push(m_bound.clone());
    }

    let cones: Vec<SupportedConeT<F>> = vec![
        SupportedConeT::ZeroConeT(1),
        SupportedConeT::NonnegativeConeT(d), // Gx ≥ 0
        SupportedConeT::NonnegativeConeT(d), // x ≥ -M
    ];

    // Tolerances, DERIVED FROM `prec_bits` rather than fixed.
    //
    // These used to be `1e-12` / `1e-8` hardcoded, with the note that
    // "1e-12 is achievable by BOTH the f64 and the MPFR IPM ... MPFR can be
    // pushed tighter via a custom settings build". The consequence was that
    // `prec_bits` widened the *arithmetic* and never tightened *termination*,
    // so the MPFR path stopped at an f64-scale residual no matter what it was
    // asked for. Measured 2026-08-23 at H_3 (bean `qou/ftuv`): `primal_obj`
    // came back 3.81482e-16 identically at (167 bits, 1e-9), (167, 1e-30) and
    // (333, 1e-40) — six figures apart from nothing. The duals carried ~19
    // genuine digits while the binary's own CLI documents "167 ≈ 50 dps".
    //
    // Scaling instead of a "custom settings build": the caller already passes
    // the precision, so the tolerance can follow it. `0.8 · dps` for the main
    // tolerance leaves ~20% headroom for IPM round-off; `0.5 · dps` for the
    // reduced (fallback) tolerance keeps the same ratio the fixed pair had.
    //
    // **`prec_bits` is NOT the number to scale by.** The doc comment above
    // says it is "ignored (harmless) for non-MPFR `F`", so for `F = f64` it
    // reports whatever the caller asked for while the arithmetic stays at 53
    // bits. Keying the tolerance on it asked the f64 IPM for 1e-40 and got
    // `InsufficientProgress` — caught by `mpfr_agrees_with_f64`, which is
    // exactly the shared cross-validation test the old fixed constants were
    // chosen to keep converging.
    //
    // So probe `F`'s ACTUAL working precision: the largest `k` with
    // `1 + 10^-k ≠ 1`. That is ~15 for f64 and ~50 at 167 bits, costs at most
    // 300 additions, and cannot disagree with the type in play. The requested
    // precision still caps it, so asking for less than `F` can do is honoured.
    //
    // At f64 the clamps then reproduce the old constants exactly —
    // `floor(0.8 · 15) = 12` and `max(8, floor(0.5 · 15)) = 8`. At 167 bits
    // they become 1e-40 / 1e-25.
    //
    // The 300/250 ceilings keep `10^-e` inside f64's normal range (min normal
    // ≈ 2.2e-308), since `F::from_f64` is how the value is built.
    let one = F::from_f64(1.0).unwrap();
    let mut usable_dps = 0f64;
    for k in 1..=300i32 {
        let probe = one.clone() + F::from_f64(10f64.powi(-k)).unwrap();
        if probe == one {
            break;
        }
        usable_dps = f64::from(k);
    }
    let dps = (f64::from(prec_bits) * std::f64::consts::LOG10_2).min(usable_dps);
    let e_tight = ((0.8 * dps).floor() as i32).clamp(12, 300);
    let e_red = ((0.5 * dps).floor() as i32).clamp(8, 250);
    let eps = F::from_f64(10f64.powi(-e_tight)).unwrap();
    let eps_red = F::from_f64(10f64.powi(-e_red)).unwrap();
    // A tighter tolerance needs more interior-point steps. 200 was tuned for
    // the f64 tolerance; hold that at f64 and allow more as precision rises.
    let max_iter = 200u32 + 10 * ((dps - 16.0).max(0.0) as u32);
    // TOLERANCE LADDER — "the solver gave up" is not "the LP has no solution".
    //
    // `e_tight` above is derived from the arithmetic width alone, and
    // `tol_gap_abs` / `tol_feas` are ABSOLUTE. On a problem whose natural
    // scale is small that asks for the impossible: measured 2026-08-23 on
    // `wedderburn_lp_ew_wiring` (d = 28, |t| ~ 1e-5, n_target ~ 3e-4,
    // optimum 1.67e-9, Gram well-conditioned at cond 53), the solver returned
    //
    //     prec_bits=113  ->  AlmostSolved            feasible
    //     prec_bits=167  ->  InsufficientProgress    "infeasible"
    //
    // and the caller wrote 72 NaNs into a committed witness as though the LP
    // had no solution. It has one; scipy finds it. The demand for an absolute
    // 1e-40 residual on a 1e-9 optimum is what could not be met.
    //
    // `InsufficientProgress` and `MaxIterations` are statements about the
    // SOLVER; only `PrimalInfeasible` / `DualInfeasible` are statements about
    // the PROBLEM. Collapsing all of them into one bool made the two
    // indistinguishable. So: try the tight tolerance, and on a
    // non-convergence status loosen and retry rather than reporting a
    // mathematical verdict the solver never reached. The achieved exponent is
    // returned so a witness records the tolerance its numbers actually meet
    // instead of the one that was requested.
    let mut e_used = e_tight;
    let mut solver;
    let mut ladder = Vec::new();
    loop {
        let eps_i = F::from_f64(10f64.powi(-e_used)).unwrap();
        let eps_red_i =
            F::from_f64(10f64.powi(-((e_used as f64 * 0.625).floor() as i32))).unwrap();
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
        solver =
            DefaultSolver::new(&p_zero, &q_vec, &a_csc, &b_vec, &cones, settings).unwrap();
        solver.solve();

        let converged = matches!(
            solver.solution.status,
            SolverStatus::Solved | SolverStatus::AlmostSolved
        );
        // A genuine infeasibility certificate is an ANSWER — stop, do not
        // loosen. Loosening on these would turn a correct "no solution"
        // into a fabricated one.
        let decided = matches!(
            solver.solution.status,
            SolverStatus::PrimalInfeasible
                | SolverStatus::DualInfeasible
                | SolverStatus::AlmostPrimalInfeasible
                | SolverStatus::AlmostDualInfeasible
        );
        if converged || decided {
            break;
        }
        ladder.push(format!("{:?}@1e-{}", solver.solution.status, e_used));
        // Back off 8 decades a step, down to the tolerance this code used
        // BEFORE the precision-derived pair replaced it (`eps_red = 1e-8`).
        // The floor is deliberately NOT `e_red`: that scales with precision,
        // so at 333 bits it is 1e-50 and the ladder would bottom out tighter
        // than the f64 path ever demanded — asking for more precision would
        // make a solve fail that 167 bits completes. Flooring at the old
        // constant guarantees the ladder is never worse than the behaviour
        // it replaced.
        const E_FLOOR: i32 = 8;
        if e_used <= E_FLOOR {
            break;
        }
        e_used = (e_used - 8).max(E_FLOOR);
    }
    let _ = &eps;
    let _ = &eps_red;

    let mut status = format!("{:?}", solver.solution.status);
    if !ladder.is_empty() {
        // Say what was tried. A retry that leaves no trace is the same
        // absent-check shape this ladder exists to fix.
        status = format!("{status}@1e-{e_used} after [{}]", ladder.join(", "));
    }
    let feasible = matches!(
        solver.solution.status,
        SolverStatus::Solved | SolverStatus::AlmostSolved
    );

    let x_star: Vec<F> = solver.solution.x.clone();
    let z = &solver.solution.z;

    // Dual extraction per the cone layout above.
    let y0_star = -z[0].clone(); // y0 = -z_eq
    let y_star: Vec<F> = (0..d).map(|i| z[1 + i].clone()).collect(); // y_i = z_G[i]
    let active_set: Vec<usize> = (0..d).filter(|&i| y_star[i] > *dual_tol).collect();

    // primal_obj = t·x  (== solver.solution.obj_val).
    let mut primal_obj = F::zero();
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

/// Convert a Clarabel scalar to `f64` via its decimal `Display` (lossy —
/// for summary / JSON fields only; the full-precision value stays in `F`).
pub fn to_f64<F: Display>(v: &F) -> f64 {
    format!("{}", v).parse::<f64>().unwrap_or(f64::NAN)
}

/// JSON/FFI-ready result: `f64` summary fields PLUS full-precision decimal
/// strings.  This is what the JSON CLI and the PyO3 binding return, so
/// neither has to handle Clarabel scalar types directly.
#[derive(Debug, Clone)]
pub struct OpSelLpStringResult {
    pub x_star: Vec<f64>,
    pub y0_star: f64,
    pub y_star: Vec<f64>,
    pub active_set: Vec<usize>,
    pub primal_obj: f64,
    pub dual_obj: f64,
    pub duality_gap: f64,
    pub feasible: bool,
    pub status: String,
    pub x_star_str: Vec<String>,
    pub y0_star_str: String,
    pub y_star_str: Vec<String>,
    pub primal_obj_str: String,
    pub dual_obj_str: String,
    pub duality_gap_str: String,
    pub precision_bits: u32,
}

/// Parse a decimal string into an `MpfrFloat` at the current MPFR default
/// precision via the crate's `Deserialize` impl (wire format `(prec, s)`;
/// `prec = 0` means "use the thread-local default", set by the caller).
/// `rug::Float::parse` accepts plain decimals and `1e6` / `1e-9` forms.
fn parse_mpfr(s: &str) -> Result<MpfrFloat, String> {
    serde_json::from_value::<MpfrFloat>(serde_json::json!([0, s]))
        .map_err(|e| format!("cannot parse MPFR scalar {s:?}: {e}"))
}

/// String-in / string-out operator-selection LP — the production MPFR path
/// with decimal-string IO, so callers (the JSON CLI, the PyO3 wheel binding)
/// need no Clarabel types.  Inputs are decimal strings (carry full 50-dps
/// precision, not f64); `prec_bits` sets the MPFR working precision.
pub fn solve_operator_selection_lp_from_strings(
    t: &[String],
    g: &[Vec<String>],
    n_target: &str,
    m_bound: &str,
    dual_tol: &str,
    prec_bits: u32,
) -> Result<OpSelLpStringResult, String> {
    set_mpfr_default_precision(prec_bits);
    let t_m: Vec<MpfrFloat> = t.iter().map(|s| parse_mpfr(s)).collect::<Result<_, _>>()?;
    let g_m: Vec<Vec<MpfrFloat>> = g
        .iter()
        .map(|row| row.iter().map(|s| parse_mpfr(s)).collect::<Result<_, _>>())
        .collect::<Result<_, _>>()?;
    let n_m = parse_mpfr(n_target)?;
    let mb = parse_mpfr(m_bound)?;
    let dt = parse_mpfr(dual_tol)?;

    let r = solve_operator_selection_lp(&t_m, &g_m, &n_m, &mb, &dt, prec_bits);

    Ok(OpSelLpStringResult {
        x_star: r.x_star.iter().map(to_f64).collect(),
        y0_star: to_f64(&r.y0_star),
        y_star: r.y_star.iter().map(to_f64).collect(),
        active_set: r.active_set.clone(),
        primal_obj: to_f64(&r.primal_obj),
        dual_obj: to_f64(&r.dual_obj),
        duality_gap: to_f64(&r.duality_gap),
        feasible: r.feasible,
        status: r.status.clone(),
        x_star_str: r.x_star.iter().map(|x| format!("{x}")).collect(),
        y0_star_str: format!("{}", r.y0_star),
        y_star_str: r.y_star.iter().map(|y| format!("{y}")).collect(),
        primal_obj_str: format!("{}", r.primal_obj),
        dual_obj_str: format!("{}", r.dual_obj),
        duality_gap_str: format!("{}", r.duality_gap),
        precision_bits: prec_bits,
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    /// The 3-channel dummy LP from `lp_dual_solver.py`'s smoke test, over `F`.
    fn dummy<F: FloatT>() -> (Vec<F>, Vec<Vec<F>>, F) {
        let f = |x: f64| F::from_f64(x).unwrap();
        let t = vec![f(1.0), f(0.5), f(0.3)];
        let g = vec![
            vec![f(1.0), f(0.2), f(0.1)],
            vec![f(0.2), f(1.0), f(0.3)],
            vec![f(0.1), f(0.3), f(1.0)],
        ];
        (t, g, f(1.0))
    }

    fn solve_dummy<F: FloatT>() -> OpSelLpResult<F> {
        set_mpfr_default_precision(DEFAULT_PREC_BITS);
        let (t, g, n) = dummy::<F>();
        let big = F::from_f64(1e6).unwrap();
        let tol = F::from_f64(1e-9).unwrap();
        solve_operator_selection_lp(&t, &g, &n, &big, &tol, DEFAULT_PREC_BITS)
    }

    #[test]
    fn solves_and_is_feasible() {
        let r = solve_dummy::<MpfrFloat>();
        assert!(r.feasible, "status = {}", r.status);
        assert_eq!(r.x_star.len(), 3);
        assert_eq!(r.y_star.len(), 3);
    }

    #[test]
    fn strong_duality_gap_is_zero() {
        let r = solve_dummy::<MpfrFloat>();
        let tol = MpfrFloat::from_f64(1e-6).unwrap();
        // primal_obj == dual_obj == n_target · y0  ⇒ the y0 sign is right.
        assert!(
            r.duality_gap < tol,
            "duality gap {} too large (primal {}, dual {})",
            to_f64(&r.duality_gap),
            to_f64(&r.primal_obj),
            to_f64(&r.dual_obj),
        );
    }

    #[test]
    fn kkt_stationarity_holds() {
        // t = y0·1 + Gᵀy + z_bound, with y0 = -z_eq, y_i = z_G[i].
        let (t, g, _) = dummy::<MpfrFloat>();
        let r = solve_dummy::<MpfrFloat>();
        let tol = MpfrFloat::from_f64(1e-5).unwrap();
        for c in 0..t.len() {
            let mut recon = r.y0_star.clone();
            for i in 0..t.len() {
                recon = recon + g[i][c].clone() * r.y_star[i].clone();
            }
            let resid = (t[c].clone() - recon).abs();
            assert!(resid < tol, "KKT residual at c={c} is {}", to_f64(&resid));
        }
    }

    #[test]
    fn complementary_slackness_holds() {
        // y_i · (Gx)_i ≈ 0 for every channel.
        let (_, g, _) = dummy::<MpfrFloat>();
        let r = solve_dummy::<MpfrFloat>();
        let d = g.len();
        let tol = MpfrFloat::from_f64(1e-5).unwrap();
        for i in 0..d {
            let mut gx_i = MpfrFloat::zero();
            for c in 0..d {
                gx_i = gx_i + g[i][c].clone() * r.x_star[c].clone();
            }
            let cs = (r.y_star[i].clone() * gx_i).abs();
            assert!(cs < tol, "complementary slackness at i={i}: {}", to_f64(&cs));
        }
    }

    #[test]
    fn dual_multipliers_are_nonnegative() {
        let r = solve_dummy::<MpfrFloat>();
        let neg = MpfrFloat::from_f64(-1e-6).unwrap();
        for (i, y) in r.y_star.iter().enumerate() {
            assert!(*y > neg, "y_star[{i}] = {} is significantly negative", to_f64(y));
        }
    }

    /// **The owner's validation:** the MPFR solve agrees with an independent
    /// `f64` (float) solve of the *same* LP.  Both use the identical Clarabel
    /// kernel; only the scalar precision differs.  Agreement to the f64 IPM
    /// floor confirms the MPFR backend introduces no discrepancy vs float —
    /// f64 is used here ONLY for this check (production is MPFR-only).
    #[test]
    fn mpfr_agrees_with_f64() {
        let rf = solve_dummy::<f64>();
        let rm = solve_dummy::<MpfrFloat>();
        assert!(
            rf.feasible && rm.feasible,
            "feasibility differs: f64={} mpfr={}",
            rf.status, rm.status
        );

        // Objective agrees to the f64 floor.
        let pf = rf.primal_obj;
        let pm = to_f64(&rm.primal_obj);
        let rel = (pf - pm).abs() / pf.abs().max(1e-30);
        assert!(rel < 1e-6, "primal_obj: f64={pf} mpfr={pm} rel={rel:e}");

        // Same active set (which Frobenius channels are tight).
        assert_eq!(
            rf.active_set, rm.active_set,
            "active sets differ: f64={:?} mpfr={:?}",
            rf.active_set, rm.active_set
        );

        // Each dual shadow price agrees.
        for i in 0..rf.y_star.len() {
            let yf = rf.y_star[i];
            let ym = to_f64(&rm.y_star[i]);
            let drel = (yf - ym).abs() / yf.abs().max(1e-9);
            assert!(drel < 1e-5, "y_star[{i}]: f64={yf} mpfr={ym} rel={drel:e}");
        }
    }

    /// The string-in/string-out entry point (used by the CLI and the PyO3
    /// wheel binding) solves the dummy LP via decimal-string IO.
    #[test]
    fn from_strings_solves_dummy() {
        let t = vec!["1.0".to_string(), "0.5".to_string(), "0.3".to_string()];
        let g = vec![
            vec!["1.0".into(), "0.2".into(), "0.1".into()],
            vec!["0.2".into(), "1.0".into(), "0.3".into()],
            vec!["0.1".into(), "0.3".into(), "1.0".into()],
        ];
        let r = solve_operator_selection_lp_from_strings(
            &t, &g, "1.0", "1e6", "1e-9", DEFAULT_PREC_BITS,
        )
        .expect("solve");
        assert!(r.feasible, "status {}", r.status);
        assert_eq!(r.x_star.len(), 3);
        assert!((r.primal_obj - 0.16875).abs() < 1e-4, "primal {}", r.primal_obj);
        assert_eq!(r.active_set, vec![0, 1]);
        assert!(r.primal_obj_str.len() >= 20, "str too short: {}", r.primal_obj_str);
    }
}
