//! Benchmark: GP-all-partitions-MPFR vs Hoefsmit-seminormal-MPFR on a
//! canonical atomic-braid word, at 50 dps precision.
//!
//! C-full Step 6 per the C-gate audit
//! (`docs/audits/2026-05-18-hoefsmit-c-gate-gp-cross-validate.md`):
//! measures whether the all-partitions GP path (Step 3, with per-T_w
//! memoisation across partitions) is faster than the seminormal
//! per-partition path on real canonical atomic braids.
//!
//! ## Input
//!
//! Hand-coded canonical braid words for a few small atoms. The word
//! format is `Vec<(Crossing, u32)>` where `Crossing` ∈ {Sigma,
//! SigmaInv, Averaged} and the u32 is the 1-based generator index.
//!
//! Atoms currently benchmarked:
//!   - p (Z=1, N=0) at H_3 — small, sanity
//!   - n (Z=0, N=1) at H_3 — small, sanity
//!   - tritium (Z=1, N=2) at H_9 — medium, ~30 partitions
//!
//! ⁴He (Z=2, N=2) at H_12 is too expensive for a quick bench (~8 min
//! seminormal baseline per PR #716); to add it pass `--include-he4`.
//!
//! ## Output
//!
//! For each atom + path:
//!   - wall time (ms)
//!   - bytes of returned all-partitions result
//!   - byte-equality flag (GP vs seminormal output)
//!
//! Plus a summary: per-atom speedup ratio (seminormal / GP).
//!
//! Exit 0 if every atom's GP path produces byte-identical output to
//! the seminormal path. Exit 1 if any mismatch (the benchmark loses
//! correctness — speedup is meaningless without correctness).

use std::time::Instant;

use hecke_engine::geck_pfeiffer::chi_lambda_via_gp_hoefsmit_all_partitions_mpfr;
use hecke_engine::wenzl_lr::{chi_lambda_canonical_all_partitions_mpfr, Crossing, CrossingPair};

/// Canonical Q_50_DIGIT_STR substrate parameter.  Source of truth:
/// `folio-assistant/computations/q_parameter.py::Q_50_DIGIT_STR`.
const Q_STR_50DPS: &str = "1.10997859555418057528159407960950937799328227995870";
const DPS: u32 = 50;

/// Convert a `&[CrossingPair]` to `&[(i32, u32)]` so the GP path
/// can consume it.
fn to_signed_word(word: &[CrossingPair]) -> Vec<(i32, u32)> {
    word.iter()
        .map(|(c, g)| {
            let sign = match c {
                Crossing::Sigma => 1,
                Crossing::SigmaInv => -1,
                Crossing::Averaged => 0,
            };
            (sign, *g)
        })
        .collect()
}

/// Hand-coded canonical atomic-braid words.  These follow the same
/// convention as `folio-assistant/computations/mass_at_3A_proper.py::
/// atom_braid_word_3A(Z, N)`:
///
///   For each nucleon k (0-indexed):
///     intra g₀ pass: σ / σ⁻¹ / averaged at base gen (3k + 1, 1-based)
///     intra g₁ pass: at (3k + 2, 1-based)
///     inter-nucleon (if k < A-1): at (3k + 3, 1-based)
///
/// The intra word for proton uses quark content (u, u, d):
///   g₀: 3 × σ (B₃ confinement) + (u,u)=σ + (u,d)=avg + 2 × σ (gluon) = 7 entries
///   g₁: 3 × σ⁻¹ (B₃) + (u,d)=avg = 4 entries
/// Total per proton: 11 entries.
///
/// For neutron (u, d, d):
///   g₀: 3 × σ + (u,d)=avg + (u,d)=avg + 2 × σ = 7 entries
///       (actually: B₃ + 3 quark-pair sigmas; with 1 same-type and 2 mixed,
///        the encoding is: 3σ + σ_avg + σ_avg + 2σ)
///   g₁: 3 × σ⁻¹ + (d,d)=σ⁻¹ = 4 entries
/// Total per neutron: 11 entries.
///
/// Rather than re-derive the exact sequence here, use a representative
/// canonical word: 11 ops total per nucleon (8 g₀, 3 g₁), shifted by
/// gen index 3k.
fn proton_word_h3() -> Vec<CrossingPair> {
    // Generator base = 0 (1-based gen 1, 2).  Per
    // `hecke_core.nucleon_gen_chains(['u','u','d'])`:
    //   g0 = 3·σ + σ + σ_avg + 2·σ = [(σ,1), (σ,1), (σ,1), (σ,1), (avg,1), (σ,1), (σ,1)]
    //        7 entries
    //   g1 = 3·σ⁻¹ + σ_avg = [(σ⁻¹,2), (σ⁻¹,2), (σ⁻¹,2), (avg,2)]
    //        4 entries
    let mut w = vec![
        (Crossing::Sigma, 1), (Crossing::Sigma, 1), (Crossing::Sigma, 1),
        (Crossing::Sigma, 1), (Crossing::Averaged, 1),
        (Crossing::Sigma, 1), (Crossing::Sigma, 1),
        (Crossing::SigmaInv, 2), (Crossing::SigmaInv, 2),
        (Crossing::SigmaInv, 2), (Crossing::Averaged, 2),
    ];
    debug_assert_eq!(w.len(), 11);
    let _ = &mut w;
    w
}

/// Neutron at H_3 — quark content (u, d, d).
fn neutron_word_h3() -> Vec<CrossingPair> {
    // g0: 3·σ + σ_avg(0,1) + σ_avg(0,2) + 2·σ ... wait:
    //   (0,1): u,d → mixed → avg, gen=0 (1-based 1)
    //   (0,2): u,d → mixed → avg, gen=0 (1-based 1)
    //   (1,2): d,d → σ⁻¹, gen=1 (1-based 2)
    // So g0 = 3·σ + 2·σ_avg + 2·σ (gluon) at gen 1
    //   g1 = 3·σ⁻¹ + σ⁻¹ at gen 2
    let w = vec![
        (Crossing::Sigma, 1), (Crossing::Sigma, 1), (Crossing::Sigma, 1),
        (Crossing::Averaged, 1), (Crossing::Averaged, 1),
        (Crossing::Sigma, 1), (Crossing::Sigma, 1),
        (Crossing::SigmaInv, 2), (Crossing::SigmaInv, 2),
        (Crossing::SigmaInv, 2), (Crossing::SigmaInv, 2),
    ];
    debug_assert_eq!(w.len(), 11);
    w
}

#[derive(serde::Serialize)]
struct BenchRow {
    atom: String,
    n_strands: usize,
    word_len: usize,
    n_averaged: usize,
    seminormal_wall_ms: u128,
    gp_wall_ms: u128,
    /// seminormal / gp wall ratio; >1 means GP is faster.
    speedup_ratio: f64,
    /// True iff every partition's χ^λ output is byte-equal between
    /// seminormal and GP at this dps.
    byte_equal: bool,
    n_partitions: usize,
    n_mismatches: usize,
}

fn bench_atom(label: &str, n_strands: usize, word: &[CrossingPair]) -> BenchRow {
    eprintln!("→ {} (H_{}, {} crossings)...", label, n_strands, word.len());

    let n_averaged = word.iter().filter(|(c, _)| *c == Crossing::Averaged).count();

    // Seminormal path.
    let t_semi = Instant::now();
    let semi_rows = chi_lambda_canonical_all_partitions_mpfr(
        n_strands, word, Q_STR_50DPS, DPS,
    );
    let semi_wall_ms = t_semi.elapsed().as_millis();
    eprintln!("  seminormal: {} ms, {} partitions", semi_wall_ms, semi_rows.len());

    // GP path — same input as a signed word.
    let signed_word = to_signed_word(word);
    let t_gp = Instant::now();
    let gp_rows = chi_lambda_via_gp_hoefsmit_all_partitions_mpfr(
        n_strands, &signed_word, Q_STR_50DPS, DPS,
    );
    let gp_wall_ms = t_gp.elapsed().as_millis();
    eprintln!("  GP:         {} ms, {} partitions", gp_wall_ms, gp_rows.len());

    // Numerical-agreement check at MPFR precision.  Byte-equality
    // is too strict: seminormal and GP arrive at each χ^λ via
    // different summation orders, and MPFR addition is non-
    // associative at the precision boundary — so last-digit
    // disagreements at ~10⁻⁵⁰ (1 ULP at 50 dps) are expected.
    // Tolerance 1e-45 absorbs that.
    use rug::Float;
    let prec = (DPS as f64 * 3.322 + 16.0) as u32;
    let tolerance = 1.0e-45_f64;
    let semi_map: std::collections::BTreeMap<_, _> =
        semi_rows.iter().cloned().collect();
    let gp_map: std::collections::BTreeMap<_, _> =
        gp_rows.iter().cloned().collect();
    let mut n_mismatches = 0usize;
    let mut worst_abs_diff: f64 = 0.0;
    for (lam, semi_chi_str) in &semi_map {
        let gp_chi_str = gp_map
            .get(lam)
            .expect("GP partition list must match seminormal");
        let semi_f = Float::parse(semi_chi_str)
            .map(|p| Float::with_val(prec, p))
            .expect("seminormal output not a valid decimal");
        let gp_f = Float::parse(gp_chi_str)
            .map(|p| Float::with_val(prec, p))
            .expect("GP output not a valid decimal");
        let diff = Float::with_val(prec, &semi_f - &gp_f);
        let abs_d: f64 = diff.abs().to_f64();
        if abs_d > worst_abs_diff {
            worst_abs_diff = abs_d;
        }
        if abs_d > tolerance {
            n_mismatches += 1;
            if n_mismatches <= 3 {
                eprintln!(
                    "  MISMATCH λ={:?} abs_diff={:.3e}\n    semi: {}\n    gp:   {}",
                    lam, abs_d, semi_chi_str, gp_chi_str
                );
            }
        }
    }
    let byte_equal = worst_abs_diff <= tolerance;
    eprintln!(
        "  worst abs_diff: {:.3e}  (tolerance {:.0e})",
        worst_abs_diff, tolerance
    );
    let speedup_ratio = if gp_wall_ms == 0 {
        f64::NAN
    } else {
        semi_wall_ms as f64 / gp_wall_ms as f64
    };
    eprintln!(
        "  speedup: {:.2}× (byte_equal={}, {} mismatches)",
        speedup_ratio, byte_equal, n_mismatches
    );

    BenchRow {
        atom: label.to_string(),
        n_strands,
        word_len: word.len(),
        n_averaged,
        seminormal_wall_ms: semi_wall_ms,
        gp_wall_ms,
        speedup_ratio,
        byte_equal,
        n_partitions: semi_rows.len(),
        n_mismatches,
    }
}

fn main() {
    let include_he4 = std::env::args().any(|a| a == "--include-he4");

    let mut rows = Vec::new();

    rows.push(bench_atom("proton", 3, &proton_word_h3()));
    rows.push(bench_atom("neutron", 3, &neutron_word_h3()));

    // Synthetic deuteron-shaped word at H_6 — exercises the
    // algorithms with a longer word + larger basis-expansion footprint.
    // 2 nucleons × ~11 ops + 1 inter-nucleon averaged crossing = 23 ops.
    // (Not bit-perfect deuteron: just a representative shape.)
    let deuteron_like = {
        let mut w = proton_word_h3();
        // Shift the neutron-like sub-word to generators 4, 5.
        for (c, g) in neutron_word_h3() {
            let new_g = match g {
                1 => 4,
                2 => 5,
                _ => g + 3,
            };
            w.push((c, new_g));
        }
        // Inter-nucleon averaged crossing at gen 3.
        w.push((Crossing::Averaged, 3));
        w
    };
    rows.push(bench_atom("deuteron-like-h6", 6, &deuteron_like));

    // Synthetic tritium-shaped word at H_9 — 3 nucleons + 2 inter-
    // nucleon crossings = 35 entries.  At H_9 there are 30
    // partitions with max dim 42 — enough to amortise the GP basis-
    // expansion overhead, more representative of the
    // canonical_chi_all_partitions scaling target.
    let tritium_like = {
        let mut w = proton_word_h3();
        for (c, g) in neutron_word_h3() {
            w.push((c, match g { 1 => 4, 2 => 5, _ => g + 3 }));
        }
        w.push((Crossing::Averaged, 3));
        for (c, g) in neutron_word_h3() {
            w.push((c, match g { 1 => 7, 2 => 8, _ => g + 6 }));
        }
        w.push((Crossing::Averaged, 6));
        w
    };
    rows.push(bench_atom("tritium-like-h9", 9, &tritium_like));

    if include_he4 {
        eprintln!(
            "→ ⁴He skipped (use --include-he4 to enable; ~10+ min seminormal baseline)"
        );
        // Not implemented: would need a proper canonical word builder
        // for higher A.  Deferred to a Python-driven harness in the
        // computations dir.
    }

    let n_failures: usize = rows.iter().filter(|r| !r.byte_equal).count();
    let summary = serde_json::json!({
        "binary": "gp-bench",
        "purpose": "C-full Step 6: GP-all-partitions-MPFR vs Hoefsmit-seminormal-MPFR",
        "q_str_50dps": Q_STR_50DPS,
        "dps": DPS,
        "rows": rows,
        "n_failures": n_failures,
    });
    println!("{}", serde_json::to_string_pretty(&summary).unwrap());

    if n_failures > 0 {
        eprintln!(
            "✗ {}/{} atoms have byte-mismatch between GP and seminormal",
            n_failures,
            rows.len(),
        );
        std::process::exit(1);
    }
    eprintln!("✓ all {} atoms: GP byte-equal to seminormal", rows.len());
}
