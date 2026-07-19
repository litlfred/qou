//! Certified categorical q\*-test runner (N = 5 validation, N = 6 rung).
//!
//! Reproduces the four gates of the Python N=5 reference (PR #4034) with the
//! Rust `tl_cable` engine, and extends the same construction to N = 6
//! (`cN = 5` cable, TL₁₅ = 9 694 845 diagrams). Real MPFR arithmetic.
//!
//! Usage:
//!   tl-cable-qstar 5        # validate against the #4034 witness (TL₁₂)
//!   tl-cable-qstar 6        # the N=6 rung (TL₁₅ — large offline compute)
//!
//! auditOnly; no c_k wired; no fit.

use hecke_engine::tl_cable::{jp, TlEngine, PREC};
use rug::ops::Pow;
use rug::Float;
use rustc_hash::FxHashMap;
use std::io::Write;
use std::time::Instant;

fn fl(v: f64) -> Float {
    Float::with_val(PREC, v)
}
fn fi(v: i32) -> Float {
    Float::with_val(PREC, v)
}

/// Real power `base^exp` (exp real, base > 0).
fn fpow(base: &Float, exp: &Float) -> Float {
    Float::with_val(PREC, base.pow(exp))
}
/// Integer power `base^k` (exact sign for negative base).
fn fpowi(base: &Float, k: i32) -> Float {
    Float::with_val(PREC, base.pow(k))
}
/// Relative difference `(a − b) / b` (subtraction materialized first).
fn rel_diff(a: &Float, b: &Float) -> Float {
    let d = Float::with_val(PREC, a - b);
    Float::with_val(PREC, d / b)
}

const BRAID_5_2: [i32; 6] = [1, 1, 1, 2, -1, 2]; // B₃, writhe 4
const BRAID_4_1: [i32; 4] = [1, -2, 1, -2]; // B₃, writhe 0
const Q_STAR_STR: &str = "1.10997859303152";

// --------- Masbaum trusted tower J'_{K_p}(N) at real q (Rmk 5.2), p = ±1 ------

/// c'_{n,p} for p = 1, −1 (Masbaum eq. before (35)); a = √q.
fn c_prime(n: i32, p: i32, a: &Float) -> Float {
    let e = (n * (n + 3)) / 2; // always integer
    match p {
        1 => {
            let s = if n % 2 == 0 { 1 } else { -1 };
            Float::with_val(PREC, fi(s) * fpowi(a, e))
        }
        -1 => fpowi(a, -e),
        _ => panic!("c_prime: p must be ±1 here"),
    }
}

/// f̃_{K_p,n} = (−1)^n · a^{−n(n+1)} · a^{n(n+3)/2} · c'_{n,p}.
fn f_tilde(n: i32, p: i32, a: &Float) -> Float {
    let sign = if n % 2 == 0 { 1 } else { -1 };
    let t = Float::with_val(PREC, fpowi(a, -(n * (n + 1))) * &fpowi(a, (n * (n + 3)) / 2));
    Float::with_val(PREC, fi(sign) * t) * c_prime(n, p, a)
}

/// J'_{K_p}(N) = Σ_{n<N} f̃_n (q^{1−N})_n (q^{1+N})_n  at real q.
fn j_twist(n_order: i32, p: i32, q: &Float) -> Float {
    let a = Float::with_val(PREC, q.clone().sqrt());
    let mut total = fi(0);
    let mut poch_m = fi(1);
    let mut poch_p = fi(1);
    for n in 0..n_order {
        if n > 0 {
            // poch_m *= 1 − q^{1−N} q^{n−1};  poch_p *= 1 − q^{1+N} q^{n−1}
            let em = 1 - n_order + (n - 1);
            let ep = 1 + n_order + (n - 1);
            poch_m *= &(fi(1) - fpowi(q, em));
            poch_p *= &(fi(1) - fpowi(q, ep));
        }
        let term = Float::with_val(PREC, f_tilde(n, p, &a) * &poch_m) * &poch_p;
        total += &term;
    }
    total
}

// -------------------------------- gate runner ---------------------------------

struct Assertion {
    name: String,
    computed: f64,
    expected: f64,
    tolerance: f64,
    passed: bool,
    source: String,
}

fn log(t0: Instant, msg: &str) {
    println!("  [{:7.0}s] {}", t0.elapsed().as_secs_f64(), msg);
    std::io::stdout().flush().ok();
}

fn main() {
    let n_target: i32 = std::env::args()
        .nth(1)
        .and_then(|s| s.parse().ok())
        .unwrap_or(5);
    let c_n = (n_target - 1) as usize; // cable width: N=5 → 4, N=6 → 5
    let k = 3usize; // 3-strand knot braids (B₃)

    // framing magnitude exponent fe = cN(cN+2)/2 (θ_{V_N} ribbon; may be half-int);
    // sign alternates (−1)^cN. writhe(5₂)=4 ⇒ framing power = 4·fe (integer).
    let fe = (c_n as f64) * (c_n as f64 + 2.0) / 2.0;
    let fr_sign = if c_n % 2 == 0 { 1.0 } else { -1.0 };
    let framing_pow_5two = 4.0 * fe; // 48 (N=5), 70 (N=6)

    let t0 = Instant::now();
    println!("{}", "=".repeat(78));
    println!(
        " N={} categorical q*-test (JW {}-cable, TL{}={} diagrams) — Rust engine",
        n_target,
        c_n,
        c_n * k,
        {
            // Catalan(cN·k)
            let m = c_n * k;
            let mut cat: u128 = 1;
            for i in 0..m as u128 {
                cat = cat * (2 * (m as u128) - i) / (i + 1);
            }
            cat / (m as u128 + 1)
        }
    );
    println!("{}", "=".repeat(78));

    // engines: framing needs cN·2 (unknot 2-strand), gates need cN·3, plus the
    // cN denominator engine.
    let mut strand_counts = vec![c_n, c_n * 2, c_n * k];
    strand_counts.sort_unstable();
    strand_counts.dedup();
    log(t0, &format!("building TL engines {:?} ...", strand_counts));
    let mut engines: FxHashMap<usize, TlEngine> = FxHashMap::default();
    for &nn in &strand_counts {
        let e = TlEngine::build(nn);
        log(t0, &format!("  TL{} built ({} diagrams)", nn, e.ndiag));
        engines.insert(nn, e);
    }

    let q_star = Float::with_val(PREC, Float::parse(Q_STAR_STR).unwrap());
    let mut assertions: Vec<Assertion> = Vec::new();

    // ---- G1: unknot ribbon framing at N (cheap, TL_{cN·2}) ----
    log(t0, "[G1] unknot framing ...");
    let mut g1_ok = true;
    let mut fr_measured = String::new();
    for qs in [fl(1.11), fl(0.95)] {
        let jr = jp(&[1], 2, c_n, &qs, &engines);
        let fr = Float::with_val(PREC, fi(1) / &jr);
        let expect = Float::with_val(PREC, fl(fr_sign) * fpow(&qs, &fl(fe)));
        let dev = rel_diff(&fr, &expect).abs().to_f64();
        g1_ok &= dev < 1e-18;
        if fr_measured.is_empty() {
            fr_measured = fr.to_f64().to_string();
        }
        log(
            t0,
            &format!("    q={}: fr={:.6}  |fr - sign·q^fe| rel={:.2e}", qs, fr.to_f64(), dev),
        );
    }
    assertions.push(Assertion {
        name: format!("gate_unknot_ribbon_framing_N{}", n_target),
        computed: if g1_ok { 1.0 } else { 0.0 },
        expected: 1.0,
        tolerance: 0.5,
        passed: g1_ok,
        source: format!(
            "fr = {}q^{{{}}} (θ_V ribbon magnitude; sign (−1)^cN) from writhe-1 unknot",
            if fr_sign > 0.0 { "+" } else { "−" },
            fe
        ),
    });
    println!("    G1 ribbon framing: {}", if g1_ok { "PASS" } else { "FAIL" });

    // ---- G2: 4₁ (w=0, framing-free) vs trusted p=−1 tower at one q ----
    log(t0, "[G2] 4₁ vs trusted p=−1 tower ...");
    let q2 = fl(1.06);
    let jc = jp(&BRAID_4_1, k, c_n, &q2, &engines);
    let jt = j_twist(n_target, -1, &Float::with_val(PREC, q2.clone().pow(2u32)));
    let jt2 = j_twist(
        n_target,
        -1,
        &Float::with_val(PREC, fi(1) / &q2.clone().pow(2u32)),
    );
    let e_a = rel_diff(&jc, &jt).abs().to_f64();
    let e_b = {
        let d = Float::with_val(PREC, &jc - &jt2);
        Float::with_val(PREC, d / &jt).abs().to_f64()
    };
    let err2 = e_a.min(e_b);
    let g2_ok = err2 < 1e-15;
    log(
        t0,
        &format!(
            "    q={}: cable={:.10} tower={:.10} rel={:.2e}  {}",
            q2,
            jc.to_f64(),
            jt.to_f64(),
            err2,
            if g2_ok { "PASS" } else { "FAIL" }
        ),
    );
    assertions.push(Assertion {
        name: format!("gate_41_N{}_matches_trusted_tower", n_target),
        computed: err2,
        expected: 0.0,
        tolerance: 1e-15,
        passed: g2_ok,
        source: format!("4₁ {}-cable J' (framing-free) = trusted p=−1 tower", c_n),
    });

    // ---- G3: 4₁ amphichiral null at q* ----
    log(t0, "[G3] 4₁ null at q* ...");
    let a41 = jp(&BRAID_4_1, k, c_n, &q_star, &engines);
    let q_star_inv = Float::with_val(PREC, fi(1) / &q_star);
    let b41 = jp(&BRAID_4_1, k, c_n, &q_star_inv, &engines);
    let null_rel = rel_diff(&a41, &b41).abs().to_f64();
    let g3_ok = null_rel < 1e-18;
    log(
        t0,
        &format!("    |B(4₁;q*)|/|J| = {:.2e}  {}", null_rel, if g3_ok { "PASS" } else { "FAIL" }),
    );
    assertions.push(Assertion {
        name: format!("gate_41_N{}_null_at_qstar", n_target),
        computed: null_rel,
        expected: 0.0,
        tolerance: 1e-18,
        passed: g3_ok,
        source: "B(4₁;q*) = 0 — mirror/bar control".to_string(),
    });

    // ---- T: the 3-point + slope-bound certificate at q* ----
    let h = fl(2e-8);
    let pts = [
        Float::with_val(PREC, &q_star - &h),
        q_star.clone(),
        Float::with_val(PREC, &q_star + &h),
    ];
    let j5f = |q: &Float, engines: &FxHashMap<usize, TlEngine>| -> Float {
        let jj = jp(&BRAID_5_2, k, c_n, q, engines);
        let jm = jp(&BRAID_5_2, k, c_n, &Float::with_val(PREC, fi(1) / q), engines);
        // B = (q^fp·J(q) − (1/q)^fp·J(1/q))/2   (fp = framing_pow_5two)
        let fp = framing_pow_5two;
        let fac_p = fpow(q, &fl(fp));
        let fac_m = fpow(&Float::with_val(PREC, fi(1) / q), &fl(fp));
        let bp = Float::with_val(PREC, &fac_p * &jj);
        let bm = Float::with_val(PREC, &fac_m * &jm);
        let d = Float::with_val(PREC, &bp - &bm);
        Float::with_val(PREC, d / fi(2))
    };

    log(t0, "[T] B(5₂) at 3 sample points ...");
    let mut bv: Vec<f64> = Vec::new();
    for (i, qq) in pts.iter().enumerate() {
        let b = j5f(qq, &engines);
        bv.push(b.to_f64());
        log(t0, &format!("    point {}/3: B = {:.8}", i + 1, b.to_f64()));
    }
    let b_star = bv[1];
    let sign_changes = bv
        .windows(2)
        .filter(|w| w[0].signum() != w[1].signum())
        .count();
    let slope_rel = ((bv[2] - bv[0]).abs() / b_star.abs()) / (2.0 * 2e-8);
    let cert = slope_rel * (2.0 * 2e-8);
    let no_zero = sign_changes == 0 && b_star.abs() > 0.0 && cert < 0.01;
    println!(
        "\n    B(q*) = {:.6}   signs = {:?}   |d ln B/dq| ≈ {:.3e}",
        b_star,
        bv.iter().map(|v| v.signum() as i32).collect::<Vec<_>>(),
        slope_rel
    );
    println!(
        "    certificate: s·2h = {:.3e} ≪ 1 — no zero can hide: {}",
        cert,
        if no_zero { "PASS" } else { "FAIL" }
    );
    assertions.push(Assertion {
        name: format!("N{}_no_qstar_zero_certificate", n_target),
        computed: if no_zero { 1.0 } else { 0.0 },
        expected: 1.0,
        tolerance: 0.5,
        passed: no_zero,
        source: "3-point + slope-bound certificate: same sign at q*±2e-8 and q*, slope·window ≪ 1"
            .to_string(),
    });

    let all_passed = assertions.iter().all(|a| a.passed);
    println!("\n{}", "=".repeat(78));
    for a in &assertions {
        println!(
            "  [{}] {}  computed={:.3e} tol={:.0e}",
            if a.passed { "PASS" } else { "FAIL" },
            a.name,
            a.computed,
            a.tolerance
        );
    }
    println!("  allPassed = {}   ({:.0}s total)", all_passed, t0.elapsed().as_secs_f64());

    // ---- emit raw results JSON (witness wrapping is a downstream step) ----
    let out_path = format!(
        "computations/probes/qbeta-5two-n{}-cable-qstar-rust.results.json",
        n_target
    );
    let mut j = String::new();
    j.push_str("{\n");
    j.push_str(&format!("  \"engine\": \"hecke-engine (rust, tl_cable, {}-bit MPFR)\",\n", PREC));
    j.push_str(&format!("  \"n_target\": {},\n", n_target));
    j.push_str(&format!("  \"cable_width\": {},\n", c_n));
    j.push_str(&format!("  \"tl_strands\": {},\n", c_n * k));
    j.push_str(&format!("  \"durationSec\": {:.1},\n", t0.elapsed().as_secs_f64()));
    j.push_str("  \"assertions\": [\n");
    for (i, a) in assertions.iter().enumerate() {
        j.push_str(&format!(
            "    {{\"name\": \"{}\", \"computed\": {:e}, \"expected\": {}, \"tolerance\": {:e}, \"passed\": {}, \"source\": {:?}}}{}\n",
            a.name, a.computed, a.expected, a.tolerance, a.passed, a.source,
            if i + 1 < assertions.len() { "," } else { "" }
        ));
    }
    j.push_str("  ],\n");
    j.push_str(&format!("  \"allPassed\": {},\n", all_passed));
    j.push_str(&format!("  \"B_qstar\": {:e},\n", b_star));
    j.push_str(&format!(
        "  \"B_samples\": [{:e}, {:e}, {:e}],\n",
        bv[0], bv[1], bv[2]
    ));
    j.push_str(&format!("  \"rel_slope\": {:e},\n", slope_rel));
    j.push_str(&format!("  \"certificate_s2h\": {:e},\n", cert));
    j.push_str(&format!("  \"framing_measured_fr\": {:?}\n", fr_measured));
    j.push_str("}\n");
    std::fs::write(&out_path, j).expect("write results");
    println!("  results -> {}", out_path);

    std::process::exit(if all_passed { 0 } else { 1 });
}
