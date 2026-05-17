//! Canonical χ^λ CLI for atomic braids.
//!
//! Computes `χ^λ(β_canonical(Z, N))` for every partition `λ ⊢ n`
//! at a single braid word, using
//! [`hecke_engine::wenzl_lr::chi_lambda_canonical_h_n_f64`] (f64
//! Hoefsmit seminormal evaluation with averaged-crossing
//! expansion).
//!
//! Unlike `hecke-tr-m-wenzl-lr` (which factors via LR and computes
//! a *tensor-product* `β_1 ⊗ β_2 ⊗ ...` — wrong for canonical
//! atomic braids per the 2026-05-17 audit), this binary takes the
//! FULL canonical word at H_n and evaluates χ^λ directly. The
//! averaged-crossing expansion is the only "non-trivial" step.
//!
//! Used by the canonical |tr_M| consumer (Σ_λ y_λ · χ^λ) to bypass
//! the broken tensor-product path. Reference:
//! `docs/audits/2026-05-17-knot-fusion-step1-audit.md`.
//!
//! Input (stdin or `--in PATH`): JSON
//!
//! ```json
//! {
//!   "n_strands": 12,
//!   "q": 1.1099785955541805,
//!   "label": "helium-4",
//!   "word": [[1, 1], [-1, 2], [0, 3], ...]
//! }
//! ```
//!
//! `word`: `[(sign, gen_1based), ...]`; sign ∈ {-1, 0, +1};
//! 0 = averaged half-sum `0.5·(σ + σ⁻¹)`.
//!
//! Output: per-partition χ^λ values (unnormalised — caller divides
//! by `averaging_denominator = 2^k` for `k` averaged crossings).
//!
//! Usage:
//! ```text
//! hecke-canonical-chi --in spec.json --out witness.json
//! cat spec.json | hecke-canonical-chi > witness.json
//! ```

use clap::Parser;
use hecke_engine::wenzl_lr::{
    averaging_denominator, chi_lambda_canonical_all_partitions_f64,
    Crossing, CrossingPair, WenzlFactor,
};
use serde::{Deserialize, Serialize};
use std::fs;
use std::io::{self, Read};
use std::path::PathBuf;
use std::time::Instant;

#[derive(Parser, Debug)]
#[command(name = "hecke-canonical-chi", version)]
struct Args {
    /// Path to the input JSON spec; if absent, reads stdin.
    #[arg(long)]
    r#in: Option<PathBuf>,
    /// Path to the output JSON; if absent, writes to stdout.
    #[arg(long)]
    out: Option<PathBuf>,
}

#[derive(Serialize, Deserialize, Debug)]
struct InputSpec {
    n_strands: usize,
    q: f64,
    label: String,
    /// `[(sign, gen_1based), ...]` with sign ∈ {-1, 0, +1}
    /// (0 = averaged half-sum).
    word: Vec<(i32, u32)>,
}

#[derive(Serialize)]
struct ChiTerm {
    lambda: Vec<usize>,
    chi_q_f64_unnormalised: f64,
    chi_q_f64_normalised: f64,
}

#[derive(Serialize)]
struct Output {
    computation: &'static str,
    description: &'static str,
    schema_version: u32,
    label: String,
    n_strands: usize,
    n_crossings: usize,
    n_averaged_crossings: usize,
    averaging_denominator: String,
    q: f64,
    n_partitions: usize,
    duration_ms: u128,
    chi_lambda_terms: Vec<ChiTerm>,
}

fn read_input(args: &Args) -> io::Result<InputSpec> {
    let raw = match &args.r#in {
        Some(p) => fs::read_to_string(p)?,
        None => {
            let mut buf = String::new();
            io::stdin().read_to_string(&mut buf)?;
            buf
        }
    };
    serde_json::from_str(&raw).map_err(|e| {
        io::Error::new(io::ErrorKind::InvalidData, format!("JSON parse: {}", e))
    })
}

fn run(args: Args) -> io::Result<()> {
    let spec = read_input(&args)?;
    let word: Vec<CrossingPair> = spec
        .word
        .iter()
        .map(|(s, g)| (Crossing::from_sign(*s), *g))
        .collect();
    // Wrap as a single-factor "WenzlFactor" to reuse the
    // averaging_denominator helper.
    let factor = WenzlFactor {
        label: spec.label.clone(),
        n_strands: spec.n_strands,
        word: word.clone(),
    };
    let avg_denom = averaging_denominator(&[factor]);
    let n_avg = word.iter().filter(|(c, _)| *c == Crossing::Averaged).count();
    let t0 = Instant::now();
    let chi_results =
        chi_lambda_canonical_all_partitions_f64(spec.n_strands, &word, spec.q);
    let dt = t0.elapsed().as_millis();
    let denom_f = avg_denom as f64;
    let chi_terms: Vec<ChiTerm> = chi_results
        .iter()
        .map(|(lam, chi)| ChiTerm {
            lambda: lam.clone(),
            chi_q_f64_unnormalised: *chi,
            chi_q_f64_normalised: chi / denom_f,
        })
        .collect();
    let out = Output {
        computation: "hecke-canonical-chi",
        description:
            "Canonical χ^λ at H_n for an atomic braid via direct \
             Hoefsmit seminormal evaluation (f64) with averaged- \
             crossing expansion.  Avoids the broken tensor-product \
             LR composition of `hecke-tr-m-wenzl-lr`; this is the \
             primitive used by the canonical |tr_M| consumer.  \
             Reference: docs/audits/2026-05-17-knot-fusion-step1-audit.md.",
        schema_version: 1,
        label: spec.label,
        n_strands: spec.n_strands,
        n_crossings: word.len(),
        n_averaged_crossings: n_avg,
        averaging_denominator: avg_denom.to_string(),
        q: spec.q,
        n_partitions: chi_terms.len(),
        duration_ms: dt,
        chi_lambda_terms: chi_terms,
    };
    let json = serde_json::to_string_pretty(&out)
        .map_err(|e| io::Error::new(io::ErrorKind::Other, format!("JSON ser: {}", e)))?;
    match args.out {
        Some(p) => fs::write(p, json)?,
        None => println!("{}", json),
    }
    Ok(())
}

fn main() {
    let args = Args::parse();
    if let Err(e) = run(args) {
        eprintln!("hecke-canonical-chi: {}", e);
        std::process::exit(1);
    }
}
