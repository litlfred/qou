//! Joint mass-tower SDP — Rust binary.
//!
//! Runs the GB-NF reducer on a registry of confined particles and
//! emits the design-spec joint-tower-SDP certificate as JSON.
//!
//! Output schema matches the Python prototype:
//!   - folio-assistant/computations/joint-tower-sdp-h3.witness.json
//!   - folio-assistant/computations/joint-tower-sdp-h6-h9.witness.json
//!
//! Usage:
//!   cargo run --release --bin joint-tower-sdp [-- --output path.json]
//!
//! See [RUST_INTEGRATION.md](../../RUST_INTEGRATION.md) §"Phase R6".

use chrono::Utc;
use clap::Parser;
use hecke_engine::cross_level_embedding::{verify_edge, TowerEdgeSpec};
use hecke_engine::gb_nf_reducer::HeckeElement;
use hecke_engine::joint_tower_sdp_certificate as cert;
use hecke_engine::sdp_verifier::solve_alpha_psd;
use hecke_engine::wedderburn_psd::evaluate_all_blocks;
use std::fs;
use std::path::PathBuf;

#[derive(Parser)]
struct Args {
    /// Output JSON path.
    #[arg(short, long, default_value = "joint-tower-sdp-rust.witness.json")]
    output: PathBuf,

    /// Filter: only run atoms with native strand count <= this.
    #[arg(long)]
    max_n: Option<usize>,

    /// q_0 substrate parameter (numerical) for Wedderburn-block PSD evaluation.
    #[arg(long, default_value_t = 1.1097)]
    q0: f64,

    /// Skip Wedderburn-block PSD evaluation (faster).
    #[arg(long)]
    no_psd: bool,
}

#[derive(Clone, Debug)]
struct RegistryEntry {
    name: &'static str,
    atomic_n_0: usize,
    native_strand_count: usize,
    braid_word: Vec<i32>,
    rho_factor: u32,
    methodology: cert::Methodology,
    b_ame_mev: Option<f64>,
}

fn registry() -> Vec<RegistryEntry> {
    vec![
        // ─── ℓ = 0  fundamental ────────────────────────────────
        RegistryEntry {
            name: "quark",
            atomic_n_0: 1,
            native_strand_count: 1,
            braid_word: vec![],
            rho_factor: 0,
            methodology: cert::Methodology::PrincipledGbNf,
            b_ame_mev: None,
        },
        RegistryEntry {
            name: "electron",
            atomic_n_0: 2,
            native_strand_count: 2,
            braid_word: vec![1, 1, 1],
            rho_factor: 1,
            methodology: cert::Methodology::PrincipledDerivation,
            b_ame_mev: Some(0.51099895),
        },
        // ─── ℓ = 1  nucleon ────────────────────────────────────
        RegistryEntry {
            name: "proton",
            atomic_n_0: 3,
            native_strand_count: 3,
            braid_word: vec![1, -2, 1, -2, 1, -2],
            rho_factor: 1,
            methodology: cert::Methodology::PrincipledDerivation,
            b_ame_mev: Some(938.272),
        },
        RegistryEntry {
            name: "neutron",
            atomic_n_0: 3,
            native_strand_count: 3,
            braid_word: vec![1, -2, 1, -2, 1, -2],
            rho_factor: 1,
            methodology: cert::Methodology::PrincipledDerivation,
            b_ame_mev: Some(939.565),
        },
        // ─── ℓ = 2  light atoms (historical knot IDs) ──────────
        RegistryEntry {
            name: "deuteron-2H",
            atomic_n_0: 6,
            native_strand_count: 3, // 6_2 in B_3
            braid_word: vec![1, -2, 1, 1, 1, -2],
            rho_factor: 1,
            methodology: cert::Methodology::ManualHistoricalVolumeMatch,
            b_ame_mev: Some(2.2246),
        },
        RegistryEntry {
            name: "tritium-3H",
            atomic_n_0: 9,
            native_strand_count: 5, // 8_11 in B_5
            braid_word: vec![-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2],
            rho_factor: 2,
            methodology: cert::Methodology::ManualHistoricalVolumeMatch,
            b_ame_mev: Some(8.4818),
        },
        RegistryEntry {
            name: "helium3-3He",
            atomic_n_0: 9,
            native_strand_count: 3, // L6a4 in B_3
            braid_word: vec![-1, 2, -1, 2, -1, 2],
            rho_factor: 2,
            methodology: cert::Methodology::ManualHistoricalVolumeMatch,
            b_ame_mev: Some(7.7180),
        },
    ]
}

fn solve_per_atom(
    entry: &RegistryEntry,
    q0: f64,
    do_psd: bool,
) -> cert::JointTowerSdpCertificate {
    let n = entry.native_strand_count.max(1);
    let e = HeckeElement::reduce_braid(n, &entry.braid_word);
    let filt = e.filtration_certificate();
    let n_steps = e.jet_log.len() as u64;
    let n_hecke = e
        .jet_log
        .iter()
        .filter(|ev| ev.relation == "hecke-quadratic")
        .count() as u64;

    let wedderburn = if do_psd && n >= 2 {
        evaluate_all_blocks(n, &entry.braid_word, q0)
    } else {
        Vec::new()
    };

    cert::JointTowerSdpCertificate {
        name: entry.name.to_string(),
        atomic_n_0: entry.atomic_n_0,
        native_strand_count: entry.native_strand_count,
        braid_word: entry.braid_word.clone(),
        filtration_certificate: filt,
        jet_log: e.jet_log,
        n_steps,
        n_hecke_relations_fired: n_hecke,
        wedderburn_blocks: wedderburn,
        cross_level_edges: Vec::new(),
        psd_cone_alpha_star: None,
        psd_cone_gap: None,
        rho_factor: entry.rho_factor,
        b_pred_mev: None,
        b_ame_mev: entry.b_ame_mev,
        err_ppb: None,
        methodology: entry.methodology.clone(),
    }
}

/// Tower edges enumerated from the design spec
/// (prop:joint-tower-sdp-confinement §"Output").
fn tower_edges() -> Vec<TowerEdgeSpec<'static>> {
    vec![
        // ── ℓ ≤ 1 ────────────────────────────────────────────────
        TowerEdgeSpec {
            parent_name: "proton",
            parent_n: 3,
            constituents: vec![("quark", 1), ("quark", 1), ("quark", 1)],
        },
        TowerEdgeSpec {
            parent_name: "neutron",
            parent_n: 3,
            constituents: vec![("quark", 1), ("quark", 1), ("quark", 1)],
        },
        // ── ℓ = 2 ────────────────────────────────────────────────
        // Atomic n_0 = 3·A; the parent_n in this verifier matches the
        // *native* H_n of the historical knot braid (B_3 for 6_2,
        // L6a4; B_5 for 8_11).  The full atomic embedding 3⊗nucleon
        // → atomic-n_0 lives at the larger H_{3A} and is wired in
        // when the joint-tower SDP solver lands (R5).
    ]
}

fn main() {
    let args = Args::parse();
    let reg = registry();

    let mut certs: Vec<cert::JointTowerSdpCertificate> = Vec::new();
    let mut max_n_observed = 0usize;
    let mut total_jet = 0u64;
    let mut total_hecke = 0u64;
    let mut max_grade_observed = 0u32;

    println!(
        "══════════════════════════════════════════════════════════════════════"
    );
    println!("  Joint mass-tower SDP — Rust binary (R1+R2+R3+R4+R6)");
    println!(
        "══════════════════════════════════════════════════════════════════════"
    );

    for entry in &reg {
        if let Some(max_n) = args.max_n {
            if entry.native_strand_count > max_n {
                continue;
            }
        }
        println!(
            "\n──── {} (atomic n_0 = {}, native B_{}) ────",
            entry.name, entry.atomic_n_0, entry.native_strand_count
        );
        println!("  braid: {:?}", entry.braid_word);
        let cert = solve_per_atom(entry, args.q0, !args.no_psd);
        println!("  filtration shape: {:?}", cert.filtration_certificate.shape);
        println!(
            "  max grade: {}, jet steps: {}, Hecke fires: {}",
            cert.filtration_certificate.max_grade, cert.n_steps, cert.n_hecke_relations_fired
        );
        if !cert.wedderburn_blocks.is_empty() {
            let n_blocks = cert.wedderburn_blocks.len();
            let n_psd = cert
                .wedderburn_blocks
                .iter()
                .filter(|b| b.psd_symmetric_part)
                .count();
            let min_eig = cert
                .wedderburn_blocks
                .iter()
                .map(|b| b.min_eigenvalue)
                .fold(f64::INFINITY, f64::min);
            println!(
                "  Wedderburn blocks: {}/{} PSD, global min eigenvalue {:+.4e}",
                n_psd, n_blocks, min_eig
            );
            for b in &cert.wedderburn_blocks {
                let flag = if b.psd_symmetric_part { "PSD" } else { "NOT PSD" };
                println!(
                    "    λ={:?} (d_λ={}): eigs ∈ [{:+.4e}, {:+.4e}]  {}",
                    b.partition, b.d_lambda, b.min_eigenvalue, b.max_eigenvalue, flag
                );
            }
        }
        max_n_observed = max_n_observed.max(entry.native_strand_count);
        total_jet += cert.n_steps;
        total_hecke += cert.n_hecke_relations_fired;
        max_grade_observed = max_grade_observed.max(cert.filtration_certificate.max_grade);
        certs.push(cert);
    }

    // ─── R5-minimal: PSD-cone α* verifier ─────────────────────────
    if !args.no_psd {
        println!(
            "\n══════════════════════════════════════════════════════════════════════"
        );
        println!("  R5-minimal — PSD-cone α* (bisection on α; equiv. SDP value)");
        println!(
            "══════════════════════════════════════════════════════════════════════"
        );
        for (i, entry) in reg.iter().enumerate() {
            if let Some(max_n) = args.max_n {
                if entry.native_strand_count > max_n {
                    continue;
                }
            }
            let n = entry.native_strand_count.max(1);
            if n < 2 {
                continue;
            }
            let report = solve_alpha_psd(n, &entry.braid_word, args.q0);
            println!(
                "  {}: α* = {:.10}, gap = {:.4e}, min_eig at α* = {:+.4e}, iters = {}",
                entry.name,
                report.alpha_star,
                1.0 - report.alpha_star,
                report.min_eigenvalue_at_alpha_star,
                report.iterations
            );
            // attach to cert
            if let Some(c) = certs.get_mut(i) {
                c.psd_cone_alpha_star = Some(report.alpha_star);
                c.psd_cone_gap = Some(1.0 - report.alpha_star);
            }
        }
    }

    // ─── R4: Cross-level edge verification ────────────────────────
    println!(
        "\n══════════════════════════════════════════════════════════════════════"
    );
    println!("  R4 — Cross-level embedding (multi-LR consistency)");
    println!(
        "══════════════════════════════════════════════════════════════════════"
    );
    let edges_by_parent = tower_edges();
    for spec in &edges_by_parent {
        let constituent_names: Vec<&str> = spec.constituents.iter().map(|(s, _)| *s).collect();
        println!(
            "\n──── {} (n_0 = {}) ← {:?} ────",
            spec.parent_name, spec.parent_n, constituent_names
        );
        let edges = verify_edge(spec);
        let n_consistent = edges.iter().filter(|e| e.embedding_consistent).count();
        println!(
            "  {}/{} per-partition LR-decompositions consistent",
            n_consistent,
            edges.len()
        );
        for e in &edges {
            println!("    {}", e.diagnostic);
        }
        // Attach edges to the parent's certificate
        for c in certs.iter_mut() {
            if c.name == spec.parent_name {
                c.cross_level_edges = edges;
                break;
            }
        }
    }

    let witness = cert::JointTowerSdpWitness {
        computation: "joint-tower-sdp-rust".to_string(),
        computed_at: Utc::now().to_rfc3339(),
        description:
            "Rust port of joint-tower SDP certificate emitter. Runs GB-NF reduction \
             on the confined-particle registry, emits design-spec certificate \
             (filtration + jet-order log per atom). Phases R1+R2+R6 of \
             RUST_INTEGRATION.md; R3 (Wedderburn PSD) and R5 (SDP solver) deferred."
                .to_string(),
        design_spec: "prop:joint-tower-sdp-confinement".to_string(),
        consumed_by: "prop:atom-knot-mass-derivation".to_string(),
        phase: "rust-r1-r2-r3-r4-r5min-r6".to_string(),
        engine: cert::EngineMetadata {
            name: "hecke-engine".to_string(),
            version: env!("CARGO_PKG_VERSION").to_string(),
            language: "rust".to_string(),
        },
        q_0_numeric: 1.1097,
        per_atom_certificates: certs,
        summary: cert::WitnessSummary {
            n_atoms: reg.len(),
            max_grade_observed,
            total_jet_steps: total_jet,
            total_hecke_relations_fired: total_hecke,
            max_native_strand_count: max_n_observed,
        },
    };

    let json = serde_json::to_string_pretty(&witness).expect("serialize");
    fs::write(&args.output, json).expect("write output");
    println!("\n→ wrote {}", args.output.display());
    println!(
        "  atoms: {}, max grade: {}, total jet steps: {}, total Hecke fires: {}",
        witness.summary.n_atoms,
        witness.summary.max_grade_observed,
        witness.summary.total_jet_steps,
        witness.summary.total_hecke_relations_fired,
    );
}
