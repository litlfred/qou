//! Cross-validate `chi_lambda_via_gp_hoefsmit` (Geck-Pfeiffer basis
//! expansion path) against `chi_lambda_braid` (Hoefsmit seminormal
//! direct path) at f64 precision.
//!
//! Purpose: gate the larger Geck-Pfeiffer implementation work
//! (candidates C-full and D per the Hoefsmit optimization audit) by
//! verifying that the existing GP scaffold produces correct χ^λ
//! values on test atomic braid words.
//!
//! **Averaged-crossing handling (C-full Step 1, 2026-05-18)**: GP's
//! `braid_to_hecke_with_avg` now handles averaged crossings (sign ==
//! 0) via the doubled half-sum
//! `(σ + σ⁻¹) · x = 2 σ x − h x` (computed as a single Hecke element,
//! no 2^k basis branching) plus a deferred `2^k` divisor applied at
//! the χ^λ output step.  This binary covers averaged-crossing test
//! cases (n=3, 4) and confirms GP matches the Hoefsmit seminormal
//! `chi_lambda_braid` (which uses direct `σ − h/2 · I` substitution).
//!
//! Test cases (covered by the `cases` vector in `main`):
//!   - n=3: σ_1; σ_1 σ_2; σ_1 σ_2 σ_1; mixed σ_1 σ_2⁻¹
//!   - n=3: averaged-only words (1 avg, 3 avgs)
//!   - n=4: 5-crossing positive word
//!   - n=4: mixed pos/neg/avg word (5 crossings, 2 avgs)
//!   - n=6: 10-crossing alternating σ / σ⁻¹ word
//!
//! Output: JSON to stdout with per-(partition, atom-word) rows:
//!   `{ "n": N, "lambda": [...], "word": [...],
//!     "chi_via_seminormal": f64, "chi_via_gp": f64,
//!     "abs_diff": f64, "rel_diff": f64 }`
//!
//! Exit 0 if all `rel_diff < 1e-12`; exit 1 if any partition exceeds
//! that tolerance.  Tolerance chosen at f64 precision floor; GP and
//! seminormal share the same `chi_lambda_braid` primitive for per-T_w
//! evaluation, so they should match to round-off.
//!
//! Reference: `docs/audits/2026-05-18-hoefsmit-matrix-product-optimization.md`
//! §C "Geck-Pfeiffer factorization (already scaffolded — biggest potential)".

use hecke_engine::geck_pfeiffer::{braid_to_hecke, chi_lambda_via_gp_hoefsmit};
use hecke_engine::seminormal::{chi_lambda_braid, partitions_of};

/// f64 approximation of the substrate parameter q_0 (calibrated per
/// `prop:three-calibration-inputs`).  Per Gemini + Copilot reviews on
/// PR #718, this binary uses the canonical literal rather than a
/// magic constant.  The full 50-dps decimal lives in
/// `folio-assistant/computations/q_parameter.py::Q_50_DIGIT_STR`; the
/// Rust kernel reads that via `q_str` for MPFR paths and uses this
/// f64 cast for the cross-validation tests (which run at f64
/// precision via `chi_lambda_braid` / `chi_lambda_via_gp_hoefsmit`).
///
/// **Drift discipline**: if Q_50_DIGIT_STR's leading f64-representable
/// digits drift, update this literal in lock-step. There is no
/// shared Rust constant module for substrate parameters yet (a
/// future C-full follow-up could add one and re-export
/// Q_50_DIGIT_STR's f64 prefix).
const Q0_F64: f64 = 1.10977859555418057297748154126596420587829;

#[derive(serde::Serialize)]
struct Row {
    n: usize,
    lambda: Vec<usize>,
    word_str: String,
    word_len: usize,
    chi_via_seminormal: f64,
    chi_via_gp: f64,
    abs_diff: f64,
    rel_diff: f64,
}

#[derive(serde::Serialize, Clone)]
struct SparsityRow {
    n: usize,
    word_str: String,
    word_len: usize,
    /// |basis expansion of T_β| — number of distinct S_n basis elements
    /// with non-zero coefficient in T_β = Σ c_w T_w.
    basis_size: usize,
    /// n! = upper bound on basis size.
    n_factorial: usize,
    /// Sparsity factor = n! / basis_size; higher = better GP win.
    sparsity_factor: f64,
}

fn word_str(word: &[(i32, u32)]) -> String {
    let parts: Vec<String> = word
        .iter()
        .map(|&(s, g)| {
            let suffix = match s {
                1 => "".to_string(),
                -1 => "⁻¹".to_string(),
                _ => format!("^{}", s),
            };
            format!("σ_{}{}", g, suffix)
        })
        .collect();
    parts.join(" ")
}

fn validate(n: usize, word: &[(i32, u32)], q: f64) -> Vec<Row> {
    let mut rows = Vec::new();
    for lambda in partitions_of(n) {
        let chi_semi = chi_lambda_braid(&lambda, word, q);
        let chi_gp = chi_lambda_via_gp_hoefsmit(&lambda, n, word, q);
        let abs_diff = (chi_semi - chi_gp).abs();
        let denom = chi_semi.abs().max(1.0);
        let rel_diff = abs_diff / denom;
        rows.push(Row {
            n,
            lambda,
            word_str: word_str(word),
            word_len: word.len(),
            chi_via_seminormal: chi_semi,
            chi_via_gp: chi_gp,
            abs_diff,
            rel_diff,
        });
    }
    rows
}

fn main() {
    // Substrate q_0 — see Q0_F64 module-level const above for
    // provenance and drift discipline.
    let q0: f64 = Q0_F64;

    // Test cases — covers positive, mixed σ-σ⁻¹, and (after C-full
    // Step 1) averaged crossings via `hecke_mul_ts_averaged_right`.
    let cases: Vec<(usize, Vec<(i32, u32)>, &str)> = vec![
        (3, vec![(1, 1)], "σ_1 at n=3"),
        (3, vec![(1, 1), (1, 2)], "σ_1 σ_2 at n=3"),
        (3, vec![(1, 1), (1, 2), (1, 1)], "σ_1 σ_2 σ_1 at n=3"),
        (3, vec![(1, 1), (-1, 2)], "σ_1 σ_2⁻¹ at n=3 (mixed)"),
        (4, vec![(1, 1), (1, 2), (1, 3), (1, 1), (1, 2)], "5-crossing at n=4"),
        (
            6,
            vec![
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5),
            ],
            "alt σ/σ⁻¹ at n=6 (10 crossings)",
        ),
        // ── C-full Step 1 averaged-crossing tests ──
        // Single averaged crossing — basic sanity for the
        // half-sum extension.
        (3, vec![(0, 1)], "(σ_1+σ_1⁻¹)/2 at n=3 (1 avg)"),
        // Averaged + positive interleave.
        (3, vec![(1, 1), (0, 2)], "σ_1 · avg(σ_2) at n=3"),
        // Multiple averages — tests the 2^k normalisation.
        (
            3,
            vec![(0, 1), (0, 2), (0, 1)],
            "avg(σ_1) avg(σ_2) avg(σ_1) at n=3 (3 avgs)",
        ),
        // Mixed positive / negative / averaged at n=4.
        (
            4,
            vec![(1, 1), (0, 2), (-1, 3), (0, 1), (1, 2)],
            "mixed-w-avg at n=4 (2 avgs in 5 crossings)",
        ),
    ];

    let mut all_rows = Vec::new();
    let mut sparsity_rows = Vec::new();
    let tolerance = 1.0e-12_f64;
    let mut worst: f64 = 0.0;
    let mut failures = 0_usize;

    fn n_factorial(n: usize) -> usize {
        (1..=n).product()
    }

    for (n, word, label) in &cases {
        eprintln!("→ validating: {}", label);
        let rows = validate(*n, word, q0);
        for r in &rows {
            if r.rel_diff > worst {
                worst = r.rel_diff;
            }
            if r.rel_diff > tolerance {
                failures += 1;
                eprintln!(
                    "  FAIL λ={:?}: chi_semi={:.6e}  chi_gp={:.6e}  rel_diff={:.3e}",
                    r.lambda, r.chi_via_seminormal, r.chi_via_gp, r.rel_diff
                );
            }
        }
        // Sparsity probe: how many basis elements in the T_β expansion?
        // This is the key cost driver for GP (vs n! upper bound).
        let basis = braid_to_hecke(*n, word);
        let basis_size = basis.len();
        let nf = n_factorial(*n);
        let sparsity = nf as f64 / basis_size.max(1) as f64;
        sparsity_rows.push(SparsityRow {
            n: *n,
            word_str: word_str(word),
            word_len: word.len(),
            basis_size,
            n_factorial: nf,
            sparsity_factor: sparsity,
        });
        eprintln!(
            "  sparsity: |T_β basis| = {}  vs  n! = {}  →  factor {:.2}×",
            basis_size, nf, sparsity
        );
        all_rows.extend(rows);
    }

    let summary = serde_json::json!({
        "binary": "gp-cross-validate",
        "purpose": "C-gate: cross-validate Geck-Pfeiffer χ^λ against Hoefsmit seminormal",
        "tolerance_rel_diff": tolerance,
        "worst_rel_diff": worst,
        "n_cases": cases.len(),
        "n_partition_rows": all_rows.len(),
        "n_failures": failures,
        "q": q0,
        "rows": all_rows,
        "sparsity_rows": sparsity_rows,
    });

    println!("{}", serde_json::to_string_pretty(&summary).unwrap());

    if failures > 0 {
        eprintln!(
            "✗ {} failures across {} rows (worst rel_diff = {:.3e})",
            failures,
            all_rows.len(),
            worst
        );
        std::process::exit(1);
    } else {
        eprintln!(
            "✓ all {} rows agree at rel_diff ≤ {:.0e} (worst {:.3e})",
            all_rows.len(),
            tolerance,
            worst
        );
    }
}
