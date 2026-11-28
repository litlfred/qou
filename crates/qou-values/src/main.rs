//! CLI binary `qou-values` for millisecond `>= 80`-dps proton-pinned evaluation of
//! `ACCURACY.md` and paper `:val[...]` observables.

use std::path::PathBuf;
use std::process::ExitCode;
use std::time::Instant;

use clap::{Parser, Subcommand};

use qou_values::{
    evaluate_all, evaluate_by_key, list_observables, write_witness_file, PinMode, PrecisionConfig,
    SubstrateContext,
};

#[derive(Debug, Parser)]
#[command(
    name = "qou-values",
    version,
    about = "Fast >=80-dps MPFR proton-pinned witnessed-value evaluator & Frechet-Jacobian CLI for QOU"
)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Debug, Subcommand)]
enum Commands {
    /// List all registered observables, `:val[...]` keys, formulas, and epistemic tiers.
    List {
        /// Optional category substring filter (`aether_knot`, `mass_hadron`, `electroweak_atomic`, `nuclear_alpha`, `molecular_geometry`).
        #[arg(long)]
        category: Option<String>,
        /// Emit machine-readable JSON array.
        #[arg(long)]
        json: bool,
    },
    /// Evaluate a single observable or `:val[...]` key (including `t3_bond_count(A)`).
    Get {
        /// Observable ID, `:val[...]` directive, alias, or `t3_bond_count(A)`.
        key: String,
        /// Significant decimal digits (`15..=250`, default `80`).
        #[arg(long, default_value_t = 80)]
        dps: usize,
        /// Emit machine-readable JSON object.
        #[arg(long)]
        json: bool,
        /// Diagnostic opt-in: attach `delta_mu_pin_on_hold` against the on-hold muon pin.
        #[arg(long)]
        allow_on_hold_muon_comparison: bool,
    },
    /// Evaluate all registered scorecard & `:val[...]` observables at once.
    All {
        /// Significant decimal digits (`15..=250`, default `80`).
        #[arg(long, default_value_t = 80)]
        dps: usize,
        /// Emit machine-readable JSON dictionary (default when `--json` is passed, else compact table).
        #[arg(long)]
        json: bool,
        /// Diagnostic opt-in: attach `delta_mu_pin_on_hold` against the on-hold muon pin.
        #[arg(long)]
        allow_on_hold_muon_comparison: bool,
    },
    /// Emit a schema-valid QOU `.witness.json` file (`q0Anchor = "proton"`).
    EmitWitness {
        /// Witness computation name / stem.
        #[arg(long)]
        name: String,
        /// Output `.witness.json` path.
        #[arg(long)]
        out: PathBuf,
        /// Optional comma-separated subset of observable keys (evaluates all if omitted).
        #[arg(long, value_delimiter = ',')]
        keys: Option<Vec<String>>,
        /// Significant decimal digits (`15..=250`, default `80`).
        #[arg(long, default_value_t = 80)]
        dps: usize,
        /// Diagnostic opt-in: attach `delta_mu_pin_on_hold` against the on-hold muon pin.
        #[arg(long)]
        allow_on_hold_muon_comparison: bool,
    },
}

fn pin_mode(allow_muon: bool) -> PinMode {
    if allow_muon {
        PinMode::AllowOnHoldMuonComparison
    } else {
        PinMode::ProtonDefault
    }
}

fn fmt_elapsed_ms(started: Instant) -> String {
    let us = started.elapsed().as_micros();
    format!("{}.{:02}", us / 1000, (us % 1000) / 10)
}

fn trunc_str(s: &str, max_chars: usize) -> String {
    if s.len() <= max_chars {
        s.to_string()
    } else {
        format!("{}...", &s[..max_chars.saturating_sub(3)])
    }
}

fn run() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();
    let started = Instant::now();

    match cli.command {
        Commands::List { category, json } => {
            let entries = list_observables(category.as_deref());
            if json {
                println!("{}", serde_json::to_string_pretty(&entries)?);
            } else {
                println!(
                    "{:<26} {:<28} {:<19} {:<15} {:<8} FORMULA",
                    "ID", ":val[...] KEY", "CATEGORY", "TIER", "UNIT"
                );
                println!("{}", "-".repeat(124));
                for e in &entries {
                    println!(
                        "{:<26} {:<28} {:<19} {:<15?} {:<8} {}",
                        e.id,
                        e.atlas_val_key.as_deref().unwrap_or("-"),
                        e.category.as_str(),
                        e.epistemic_tier,
                        e.unit.as_deref().unwrap_or("-"),
                        e.formula
                    );
                }
                println!(
                    "\nTotal: {} registered observables (plus parametric `t3_bond_count(A)` for any A >= 1).",
                    entries.len()
                );
            }
        }
        Commands::Get {
            key,
            dps,
            json,
            allow_on_hold_muon_comparison,
        } => {
            let cfg = PrecisionConfig::new(dps);
            let ctx = SubstrateContext::build(cfg, pin_mode(allow_on_hold_muon_comparison))?;
            let ev = evaluate_by_key(&key, &ctx)?;
            let elapsed_ms = fmt_elapsed_ms(started);
            if json {
                println!("{}", serde_json::to_string_pretty(&ev)?);
            } else {
                println!("Observable     : {}", ev.id);
                if let Some(vk) = &ev.atlas_val_key {
                    println!(":val[...] key  : :val[{vk}]");
                }
                println!(
                    "Category / Tier: {} / {:?}  (q0Anchor = {}, {} dps / {} MPFR bits, {} ms)",
                    ev.category.as_str(),
                    ev.epistemic_tier,
                    ev.q0_anchor,
                    ev.dps,
                    ev.mpfr_bits,
                    elapsed_ms
                );
                println!("Formula        : {}", ev.formula);
                println!(
                    "Predicted      : {}{}",
                    ev.value,
                    ev.unit.as_deref().map(|u| format!(" {u}")).unwrap_or_default()
                );
                println!("sigma_pred     : {}", ev.sigma_pred);
                if let (Some(exp), Some(sexp), Some(src)) =
                    (&ev.exp_value, &ev.exp_sigma, &ev.exp_source)
                {
                    println!("Experimental   : {} +- {} ({})", exp, sexp, src);
                    println!(
                        "Residual       : {}  ({} ppm | {} ppb | {} ppQ)",
                        ev.residual.as_deref().unwrap_or("0"),
                        trunc_str(ev.rel_ppm.as_deref().unwrap_or("0"), 14),
                        trunc_str(ev.rel_ppb.as_deref().unwrap_or("0"), 14),
                        trunc_str(ev.rel_ppq.as_deref().unwrap_or("0"), 14),
                    );
                    println!(
                        "Pulls          : {} sigma_exp  |  z_comb = {} sigma",
                        trunc_str(ev.pull_exp_sigma.as_deref().unwrap_or("0"), 12),
                        trunc_str(ev.z_comb_sigma.as_deref().unwrap_or("0"), 12),
                    );
                }
                if let Some(dmu) = &ev.delta_mu_pin_on_hold {
                    println!("Delta_mu_pin   : {}  [ON-HOLD DIAGNOSTIC ONLY]", dmu);
                }
            }
        }
        Commands::All {
            dps,
            json,
            allow_on_hold_muon_comparison,
        } => {
            let cfg = PrecisionConfig::new(dps);
            let ctx = SubstrateContext::build(cfg, pin_mode(allow_on_hold_muon_comparison))?;
            let rows = evaluate_all(&ctx);
            let elapsed_ms = fmt_elapsed_ms(started);
            if json {
                let mut by_id = serde_json::Map::new();
                let mut by_val = serde_json::Map::new();
                for r in &rows {
                    if let Some(vk) = &r.atlas_val_key {
                        by_val.insert(vk.clone(), serde_json::Value::String(r.value.clone()));
                    }
                    by_id.insert(r.id.clone(), serde_json::to_value(r)?);
                }
                let payload = serde_json::json!({
                    "q0_anchor": "proton",
                    "dps": cfg.output_dps,
                    "mpfr_bits": cfg.prec_bits,
                    "count": rows.len(),
                    "observables": by_id,
                    "atlas_val_keys": by_val,
                });
                println!("{}", serde_json::to_string_pretty(&payload)?);
            } else {
                println!(
                    "{:<26} {:<24} {:<24} {:<14} {:<12}",
                    "ID", "PREDICTED (trunc)", "SIGMA_PRED", "REL (ppb)", "PULL (exp)"
                );
                println!("{}", "-".repeat(106));
                for r in &rows {
                    println!(
                        "{:<26} {:<24} {:<24} {:<14} {:<12}",
                        r.id,
                        trunc_str(&r.value, 22),
                        trunc_str(&r.sigma_pred, 22),
                        r.rel_ppb
                            .as_deref()
                            .map(|s| trunc_str(s, 12))
                            .unwrap_or_else(|| "-".to_string()),
                        r.pull_exp_sigma
                            .as_deref()
                            .map(|s| trunc_str(s, 10))
                            .unwrap_or_else(|| "-".to_string()),
                    );
                }
                println!(
                    "\nEvaluated {} observables at {} dps ({} MPFR bits, q0Anchor = proton) in {} ms.",
                    rows.len(),
                    cfg.output_dps,
                    cfg.prec_bits,
                    elapsed_ms
                );
            }
        }
        Commands::EmitWitness {
            name,
            out,
            keys,
            dps,
            allow_on_hold_muon_comparison,
        } => {
            let cfg = PrecisionConfig::new(dps);
            let ctx = SubstrateContext::build(cfg, pin_mode(allow_on_hold_muon_comparison))?;
            let doc = write_witness_file(&name, &out, keys.as_deref(), &ctx, started)?;
            println!(
                "Wrote {} ({} assertions, allPassed={}, q0Anchor={}, {} ms)",
                out.display(),
                doc.assertions.len(),
                doc.all_passed,
                doc.q0_anchor,
                doc.duration_ms
            );
        }
    }
    Ok(())
}

fn main() -> ExitCode {
    if let Err(err) = run() {
        eprintln!("error: {err}");
        return ExitCode::FAILURE;
    }
    ExitCode::SUCCESS
}
