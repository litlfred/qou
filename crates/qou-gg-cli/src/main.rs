//! `qou-gg-cli` — deterministic 80-dps JSON emitter for Annex A (`rem:gg-hadron-datum-table`)
//! and `computations/gg_hadron_datum_table.py`.

use clap::Parser;
use qou_clarabel::{certify_all_h3_rows, HadronRowLpCertificate};
use qou_gg_eval::h3::{build_all_h3_rows, H3EvaluatedRow, HadronA1Supplements, H3_BASIS_NAMES};
use qou_gg_eval::h4_flavoured::{evaluate_h4_flavoured_census, H4FlavouredCensusReport};
use qou_gg_eval::lepton_pair_6s::{evaluate_lepton_pair_6s, LeptonPair6sReport};
use qou_gg_eval::light_nuclei_t3::{evaluate_light_nuclei_t3, LightNucleusT3Row};
use qou_gg_eval::scalars::{
    Q0Params, Q0SummaryJson, DEFAULT_OUT_DPS, DEFAULT_PREC_BITS, MIN_PREC_BITS,
};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Parser)]
#[command(name = "qou-gg-cli")]
#[command(about = "80-dps proton-pinned MPFR + Clarabel evaluator for proper gamma-gamma hadrons and A=1..4 light nuclei")]
struct CliArgs {
    /// MPFR working precision in bits (`>= 266`, default `320` ≈ 96 dps).
    #[arg(long, default_value_t = DEFAULT_PREC_BITS)]
    prec_bits: u32,

    /// Output significant decimal digits (`>= 80`, default `80`).
    #[arg(long, default_value_t = DEFAULT_OUT_DPS)]
    dps: usize,

    /// Optional explicit decimal override for `q_0^(p)` (defaults to internal MPFR proton-anchor Newton/secant solve).
    #[arg(long)]
    q0: Option<String>,

    /// Maximum vertices `L` in the 4-strand flavoured `H_4` census (default `6`).
    #[arg(long, default_value_t = 6)]
    flavoured_max_vertices: usize,

    /// Maximum vertices `L` in the 6-strand neutral lepton-pair census (default `5`).
    #[arg(long, default_value_t = 5)]
    lepton_max_vertices: usize,

    /// Section selector (`all`, `h3`, `flavoured`, `lepton6`, `light-nuclei`).
    #[arg(long, default_value = "all")]
    section: String,

    /// Pretty-print JSON output.
    #[arg(long)]
    pretty: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CombinedH3Row {
    #[serde(flatten)]
    pub eval: H3EvaluatedRow,
    pub lp_certificate: HadronRowLpCertificate,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FullDatumPayload {
    pub schema: String,
    pub engine: String,
    pub h3_basis_names: [String; 6],
    pub q0_summary: Q0SummaryJson,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub h3_rows: Option<Vec<CombinedH3Row>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub hadron_a1_supplements: Option<HadronA1Supplements>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub light_nuclei_t3_rows: Option<Vec<LightNucleusT3Row>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub h4_flavoured_census: Option<H4FlavouredCensusReport>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub lepton_pair_6s: Option<LeptonPair6sReport>,
}

fn main() {
    let args = CliArgs::parse();
    assert!(
        args.prec_bits >= MIN_PREC_BITS,
        "--prec-bits ({}) must be >= {} (80 dps floor)",
        args.prec_bits,
        MIN_PREC_BITS
    );
    assert!(
        args.dps >= 80,
        "--dps ({}) must be >= 80 for production witnesses",
        args.dps
    );

    let params = Q0Params::proton_pinned(args.prec_bits, args.q0.as_deref());
    let sec = args.section.as_str();

    let (h3_rows, hadron_a1_supplements) = if sec == "all" || sec == "h3" {
        let (raw_rows, supp) = build_all_h3_rows(&params, args.dps);
        let certs = certify_all_h3_rows(&params, &raw_rows, args.dps);
        let mut cert_map: HashMap<String, HadronRowLpCertificate> = certs
            .into_iter()
            .map(|c| (c.row_id.clone(), c))
            .collect();
        let combined: Vec<CombinedH3Row> = raw_rows
            .into_iter()
            .map(|(_, ev)| {
                let cert = cert_map.remove(&ev.id).unwrap();
                CombinedH3Row {
                    eval: ev,
                    lp_certificate: cert,
                }
            })
            .collect();
        (Some(combined), Some(supp))
    } else {
        (None, None)
    };

    let light_nuclei_t3_rows = if sec == "all" || sec == "light-nuclei" {
        Some(evaluate_light_nuclei_t3(&params, args.dps))
    } else {
        None
    };

    let h4_flavoured_census = if sec == "all" || sec == "flavoured" {
        Some(evaluate_h4_flavoured_census(
            &params,
            args.flavoured_max_vertices,
            args.dps,
        ))
    } else {
        None
    };

    let lepton_pair_6s = if sec == "all" || sec == "lepton6" {
        Some(evaluate_lepton_pair_6s(
            &params,
            args.lepton_max_vertices,
            args.dps,
        ))
    } else {
        None
    };

    let payload = FullDatumPayload {
        schema: "qou-gg-datum-table/v1".to_string(),
        engine: "qou-gg-eval+qou-clarabel (rug/MPFR + Clarabel.rs@37f06c3)".to_string(),
        h3_basis_names: H3_BASIS_NAMES.map(|s| s.to_string()),
        q0_summary: params.to_summary_json(args.dps),
        h3_rows,
        hadron_a1_supplements,
        light_nuclei_t3_rows,
        h4_flavoured_census,
        lepton_pair_6s,
    };

    let json_out = if args.pretty {
        serde_json::to_string_pretty(&payload).expect("JSON serialization failed")
    } else {
        serde_json::to_string(&payload).expect("JSON serialization failed")
    };
    println!("{json_out}");
}
