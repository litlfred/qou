//! `qou-gg-cli` — deterministic 80-dps JSON emitter for Annex A (`rem:gg-hadron-datum-table`),
//! plus bounded-RSS 320-bit `MpfrFloat` LP/PSD batch modes (`--lp-batch`, `--lp-batch-jsonl`,
//! `--lp-single`) and nuclide `H_3(q)` normal-form batch evaluation (`--atom-nf-batch`).

use clap::Parser;
use qou_clarabel::batch::{
    solve_item_isolated_tls, solve_lp_batch, stream_lp_batch_jsonl, LpBatchItem, LpBatchRequest,
};
use qou_clarabel::{certify_all_h3_rows, HadronRowLpCertificate};
use qou_gg_eval::atom_nf_batch::{evaluate_atom_nf_batch, AtomNfBatchRequest};
use qou_gg_eval::h3::{build_all_h3_rows, H3EvaluatedRow, HadronA1Supplements, H3_BASIS_NAMES};
use qou_gg_eval::h4_flavoured::{evaluate_h4_flavoured_census, H4FlavouredCensusReport};
use qou_gg_eval::lepton_pair_6s::{evaluate_lepton_pair_6s, LeptonPair6sReport};
use qou_gg_eval::light_nuclei_t3::{evaluate_light_nuclei_t3, LightNucleusT3Row};
use qou_gg_eval::scalars::{
    Q0Params, Q0SummaryJson, DEFAULT_OUT_DPS, DEFAULT_PREC_BITS, MIN_PREC_BITS,
};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::io::{self, Read};

#[derive(Debug, Parser)]
#[command(name = "qou-gg-cli")]
#[command(about = "80-dps proton-pinned MPFR + Clarabel evaluator & bounded-memory batch LP/NF CLI")]
struct CliArgs {
    /// MPFR working precision in bits (`>= 266` for 80-dps modes; default `320` ≈ 96 dps).
    #[arg(long, default_value_t = DEFAULT_PREC_BITS)]
    prec_bits: u32,

    /// Output significant decimal digits (`>= 80` for datum modes; default `80`).
    #[arg(long, default_value_t = DEFAULT_OUT_DPS)]
    dps: usize,

    /// Optional explicit decimal override for `q_0^(p)`.
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

    /// Read an `LpBatchRequest` JSON object from stdin and emit an `LpBatchResponse` JSON object to stdout.
    #[arg(long)]
    lp_batch: bool,

    /// Read one `LpBatchItem` JSON object per line (JSONL) from stdin and stream one result JSON line per input line.
    #[arg(long)]
    lp_batch_jsonl: bool,

    /// Read a single LP JSON object from stdin (`clarabel-operator-selection-lp` compatible) and emit its result.
    #[arg(long)]
    lp_single: bool,

    /// Read an `AtomNfBatchRequest` JSON object from stdin and emit an `AtomNfBatchResponse` JSON object to stdout.
    #[arg(long)]
    atom_nf_batch: bool,

    /// Pretty-print JSON output (non-JSONL modes).
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

fn read_stdin_string() -> String {
    let mut s = String::new();
    io::stdin()
        .read_to_string(&mut s)
        .expect("failed reading stdin");
    s
}

fn main() {
    let args = CliArgs::parse();

    if args.lp_batch_jsonl {
        let prec = args.prec_bits.max(113);
        let stdin = io::stdin();
        let stdout = io::stdout();
        stream_lp_batch_jsonl(stdin.lock(), stdout.lock(), prec, args.dps)
            .expect("JSONL batch LP stream failed");
        return;
    }

    if args.lp_batch {
        let input = read_stdin_string();
        let mut req: LpBatchRequest =
            serde_json::from_str(&input).expect("invalid LpBatchRequest JSON on stdin");
        if req.prec_bits.is_none() {
            req.prec_bits = Some(args.prec_bits.max(113));
        } else if let Some(pb) = req.prec_bits {
            req.prec_bits = Some(pb.max(113));
        }
        if req.out_dps.is_none() {
            req.out_dps = Some(args.dps);
        }
        let resp = solve_lp_batch(&req);
        let out = if args.pretty {
            serde_json::to_string_pretty(&resp).unwrap()
        } else {
            serde_json::to_string(&resp).unwrap()
        };
        println!("{out}");
        return;
    }

    if args.lp_single {
        let input = read_stdin_string();
        let item: LpBatchItem =
            serde_json::from_str(&input).expect("invalid single LP JSON on stdin");
        let t_ref = item.t.as_deref().expect("single LP JSON requires `t`");
        let g_ref = item.g.as_deref().expect("single LP JSON requires `G`");
        let m_str = item.m_bound.as_deref().unwrap_or("1000000");
        let prec = item.prec_bits.unwrap_or(args.prec_bits).max(113);
        let dps = item
            .out_dps
            .unwrap_or_else(|| ((prec as usize * 30103) / 100_000).max(50));
        let res = solve_item_isolated_tls(
            item.id,
            t_ref,
            g_ref,
            &item.n_target,
            m_str,
            prec,
            dps,
            item.psd_diagonal_lift,
        );
        let out = if args.pretty {
            serde_json::to_string_pretty(&res).unwrap()
        } else {
            serde_json::to_string(&res).unwrap()
        };
        println!("{out}");
        return;
    }

    if args.atom_nf_batch {
        let input = read_stdin_string();
        let req: AtomNfBatchRequest =
            serde_json::from_str(&input).expect("invalid AtomNfBatchRequest JSON on stdin");
        let resp = evaluate_atom_nf_batch(&req);
        let out = if args.pretty {
            serde_json::to_string_pretty(&resp).unwrap()
        } else {
            serde_json::to_string(&resp).unwrap()
        };
        println!("{out}");
        return;
    }

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
