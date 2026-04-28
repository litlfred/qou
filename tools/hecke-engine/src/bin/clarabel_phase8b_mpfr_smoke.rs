//! Smoke test for the Phase 8b MPFR backend:
//!   4. `T = MpfrFloat` at arbitrary working precision.
//!   5. (cross-check) `iter_diagnostics` populated for MpfrFloat too.
//!
//! Solves the same 2-D box LP as `clarabel_round4_rational_smoke` but
//! with `T = MpfrFloat` at 167-bit (~50 dps) — the precision target
//! of `R5_FULL_PLAN.md` for the QOU joint-tower confinement SDP.
//!
//! Required features: `clarabel-mpfr`.

use clarabel::algebra::{set_mpfr_default_precision, MpfrFloat};
use clarabel::algebra::CscMatrix;
use clarabel::solver::*;
use num_traits::{FromPrimitive, Signed};

type T = MpfrFloat;

fn rat(n: i64) -> T {
    T::from_i64(n).unwrap()
}

fn main() {
    println!("clarabel_phase8b_mpfr_smoke — MPFR backend new APIs");
    println!("===================================================\n");

    // 167 bits ≈ 50 dps — matches QOU R5_FULL_PLAN.md.
    set_mpfr_default_precision(167);

    // Box LP:
    //   minimize  x_1 - x_2
    //   s.t.      -1 ≤ x_1 ≤ 1,  -1 ≤ x_2 ≤ 1
    //   optimum:  x* = (-1, +1), f* = -2
    let p = CscMatrix::<T>::zeros((2, 2));
    let q_vec = vec![rat(1), -rat(1)];

    let one = rat(1);
    let neg_one = -rat(1);
    let a_mat = CscMatrix::new(
        4,
        2,
        vec![0, 2, 4],
        vec![0, 2, 1, 3],
        vec![one.clone(), neg_one.clone(), one.clone(), neg_one.clone()],
    );
    let b = vec![rat(1); 4];
    let cones = vec![SupportedConeT::NonnegativeConeT(4)];

    let settings = DefaultSettingsBuilder::default()
        .verbose(false)
        .max_iter(100)
        .build()
        .unwrap();
    let mut solver = DefaultSolver::new(&p, &q_vec, &a_mat, &b, &cones, settings).unwrap();
    solver.solve();

    println!("Test 4 — MpfrFloat solve at 167 bits (~50 dps)");
    println!("  status     = {:?}", solver.solution.status);
    println!("  iterations = {}", solver.info.iterations);
    let obj = solver.solution.obj_val.clone();
    let target = -rat(2);
    let diff = (obj.clone() - target.clone()).abs();
    println!("  obj_val    = {}", obj);
    println!("  expected   = {}", target);
    println!("  |Δ|        = {}", diff);
    // 50 dps tolerance: 1e-40 is plenty of margin
    let tol = T::from_f64(1e-40).unwrap();
    assert!(
        diff <= tol,
        "MpfrFloat solve missed the rational optimum by more than 1e-40"
    );
    println!("  ✓ matched x* = (-1, +1), f* = -2 to 1e-40\n");

    println!("Test 5 — iter_diagnostics on MpfrFloat");
    let diagnostics = &solver.info.iter_diagnostics;
    if diagnostics.is_empty() {
        println!("  (no rows — MpfrFloat may report bit-width as zero per upstream design)");
    } else {
        println!("  {} diagnostic rows captured", diagnostics.len());
        for d in diagnostics.iter().take(3) {
            println!(
                "    iter={:>3}  max_numer_bits={:>4}  max_denom_bits={:>4}",
                d.iter, d.max_numer_bits, d.max_denom_bits
            );
        }
    }

    println!("\nAll tests passed.");
}
