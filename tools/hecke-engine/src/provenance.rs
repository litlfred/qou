//! Reproducibility record for emitted certificates.
//!
//! # Why this exists
//!
//! On 2026-08-15 the substrate anchor `Q_0` was re-pinned muon → proton, and
//! the committed certificates were examined for regeneration.
//!
//! **Correction, recorded because the wrong version of this paragraph shipped
//! first.** It said the certificates "could not be" reproduced. That was
//! withdrawn: the f64 fields *are* derivable from the exact symbolic Laurent
//! terms the v9 certificates carry, via `tr_alt_f64 = eval(tr_alt) / 2^pn_count`
//! (`v9.rs:833-841`). Whoever reads this should not take "irreproducible" as
//! established — it is not, and the repair tooling depends on it being false.
//!
//! What is genuinely missing is narrower, and is what this type records: a
//! certificate does not say *how it was generated*, so a regeneration cannot be
//! set up without reading the emitter's source at the commit that produced it.
//! Three specifics:
//!
//! * **The generator was not recoverable per file.** The 51 committed
//!   certificates came from FOUR different binaries (`hecke-bigint (v9)` ×35,
//!   `hecke-modular` ×8, `hecke-crt` ×7+1), which emit different schemas —
//!   v9 carries exact symbolic Laurent terms, `hecke-crt` only an f64 summary.
//!   Re-running the wrong one silently downgrades exact rational data to
//!   float64. (`engine.binary` was recorded by v9 but not by the other two.)
//!
//! * **The parameters were not recorded at all.** Each generator takes a
//!   different cutoff — `threshold` in `hecke-crt`, `mid_strip_threshold` in
//!   `hecke-bigint` — and none of them wrote it down. Measured consequence:
//!   ¹⁰He records `elapsed_seconds = 0.0187`, while the same isotope at
//!   `hecke-crt`'s default threshold does not finish in 120 s in a release
//!   build. A >6000× discrepancy, with nothing in the file to say which
//!   parameter produced the committed number.
//!
//! * **The anchor was not recorded.** Nothing said whether a certificate was
//!   computed at the muon or the proton pin, so "is this stale?" could only be
//!   answered by reading the emitter's source at the commit that produced it.
//!
//! So: capture the actual `argv`, the anchor, and a ready-to-run command.
//!
//! # Design note — argv, not modelled parameters
//!
//! [`Generation`] stores the raw `argv` rather than typed fields per
//! generator. Modelling each binary's flags would need updating every time one
//! gains an option, and would silently drop anything not yet modelled — which
//! is exactly the failure being fixed. `argv` cannot go stale that way.
//! `reproduce` is derived from it as a literal command line, so the answer to
//! "how do I regenerate this file?" is a string in the file.

use serde::Serialize;

/// How a certificate was generated — enough to re-run it exactly.
#[derive(Serialize, Clone, Debug)]
pub struct Generation {
    /// Binary name as invoked, e.g. `"hecke-crt"`.
    pub binary: String,
    /// Full argument vector, argv[0] normalised to the binary's file name.
    pub argv: Vec<String>,
    /// Ready-to-run command that reproduces this certificate.
    pub reproduce: String,
    /// Substrate anchor used, as an f64.
    pub q0: f64,
    /// Which pin `q0` is. Must stay in sync with the `q0_pin` enum in
    /// `schemas/certificate.schema.json`; `classify_pin` is the only writer,
    /// and `classify_pin_is_a_schema_value` asserts the two agree.
    pub q0_pin: String,
    /// Crate version at generation time.
    pub engine_version: String,
    /// Git SHA if the build injected one.
    pub commit: String,
}

/// The proton pin (`m_p/m_e`) — the production default since 2026-08-07.
pub const Q0_PROTON: f64 = 1.1099785827513808;
/// The muon pin (`m_mu/m_e`) — the ideal-layer CAL-2 proxy, superseded for
/// production compute. Kept only so an older certificate can be *labelled*.
pub const Q0_MUON: f64 = 1.1099785955541805;

/// Classify an anchor by DISTANCE, in ppb from the proton pin.
///
/// Rewritten 2026-08-15 after a red-team pass. The first version compared
/// against the two f64 constants with a `1e-12` tolerance, justified as
/// "room for a value that round-tripped through a decimal string". Two things
/// were wrong with that:
///
/// 1. **The justification was empty.** Rust's `{}` f64 formatting is
///    shortest-round-trippable, so that round trip is exact and needed no
///    slack at all.
/// 2. **The tolerance it produced was too tight to be useful.** Every
///    muon-anchored artifact in this repo carries `1.1099785955733347`, not
///    the canonical `1.1099785955541805` — they differ by 3.154e-12, just
///    over the 1e-12 bound. So a module written to stop muon/proton collapse
///    classified the anchor 400+ real witnesses actually use as `"other"`.
///
/// Distance bucketing fixes both, and matches what
/// `computations/q0_provenance_audit.py` does on the Python side — the two
/// should not disagree about what "muon" means. The muon band is wide enough
/// to hold both the canonical value and the circular committed one, because
/// they ARE the same anchor: 11.5 ppb from proton, differing only in digits
/// past the ~8 that CODATA supports.
fn classify_pin(q0: f64) -> &'static str {
    let ppb = (q0 - Q0_PROTON).abs() / Q0_PROTON * 1e9;
    if ppb < 1.0 {
        "proton"
    } else if (5.0..=30.0).contains(&ppb) {
        "muon"
    } else if (1000.0..=1600.0).contains(&ppb) {
        // The 5-significant-digit `1.10998` literal, 1277 ppb off.
        "truncated-5-digit"
    } else {
        "other"
    }
}

impl Generation {
    /// Capture the current process invocation.
    ///
    /// `q0` is passed rather than read from a constant so a binary that takes
    /// an explicit `--q` records what it actually used, not what it would have
    /// defaulted to.
    pub fn capture(q0: f64) -> Self {
        let argv: Vec<String> = std::env::args().collect();
        // argv[0] is a path like `target/release/hecke-crt`; keep only the
        // file name, so the record does not depend on where it was built.
        let binary = argv
            .first()
            .map(|p| {
                std::path::Path::new(p)
                    .file_name()
                    .map(|s| s.to_string_lossy().into_owned())
                    .unwrap_or_else(|| p.clone())
            })
            .unwrap_or_else(|| "unknown".to_string());

        let mut normalised = argv.clone();
        if let Some(first) = normalised.first_mut() {
            *first = binary.clone();
        }

        let args_tail = normalised[1..].join(" ");
        let reproduce = if args_tail.is_empty() {
            format!("cargo run --release --bin {binary}")
        } else {
            format!("cargo run --release --bin {binary} -- {args_tail}")
        };

        Self {
            binary,
            argv: normalised,
            reproduce,
            q0,
            q0_pin: classify_pin(q0).to_string(),
            engine_version: env!("CARGO_PKG_VERSION").to_string(),
            commit: option_env!("GIT_SHA").unwrap_or("unknown").to_string(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn classifies_both_pins_and_neither() {
        assert_eq!(classify_pin(Q0_PROTON), "proton");
        assert_eq!(classify_pin(Q0_MUON), "muon");
        assert_eq!(classify_pin(1.5), "other");
    }

    /// The two pins are 11.54 ppb apart, so the classifier must not collapse
    /// them — that collapse is the whole defect this module addresses.
    /// The value the corpus ACTUALLY uses must classify as muon.
    ///
    /// This is the case the first implementation got wrong: it is 3.154e-12
    /// from the canonical muon constant, which the old 1e-12 tolerance
    /// rejected. Comparing the two constants to each other — which the test
    /// below does — structurally could not catch that.
    #[test]
    fn the_corpus_muon_value_classifies_as_muon() {
        assert_eq!(classify_pin(1.1099785955733347), "muon");
        assert_eq!(classify_pin(Q0_MUON), "muon");
        // And the 5-digit literal is called out, not lumped into "other".
        assert_eq!(classify_pin(1.10998), "truncated-5-digit");
    }

    /// Every value `classify_pin` can emit must be in the schema's enum.
    ///
    /// It was not: `"truncated-5-digit"` was added to the classifier and not
    /// to `schemas/certificate.schema.json`, so any certificate generated at
    /// the 1.10998 literal would have been schema-INVALID — and that is
    /// precisely the certificate class the bucket exists to find. Read the
    /// enum out of the schema file rather than restating it, so the test
    /// fails on a real divergence instead of on a stale copy.
    #[test]
    fn classify_pin_is_a_schema_value() {
        let schema = std::fs::read_to_string(concat!(
            env!("CARGO_MANIFEST_DIR"),
            "/schemas/certificate.schema.json"
        ))
        .expect("certificate schema must be readable from the crate root");
        let doc: serde_json::Value =
            serde_json::from_str(&schema).expect("certificate schema must parse");
        let allowed = doc["properties"]["generation"]["properties"]["q0_pin"]["enum"]
            .as_array()
            .expect("q0_pin must declare an enum")
            .iter()
            .map(|v| v.as_str().unwrap().to_string())
            .collect::<Vec<_>>();

        // Sample across every branch, including the bucket boundaries.
        for q in [
            Q0_PROTON,
            Q0_MUON,
            1.1099785955733347,
            1.10998,
            1.5,
            0.0,
            f64::NAN,
        ] {
            let got = classify_pin(q);
            assert!(
                allowed.iter().any(|a| a == got),
                "classify_pin({q}) = {got:?}, not in schema enum {allowed:?}"
            );
        }
    }

    #[test]
    fn the_two_pins_are_distinguishable() {
        assert_ne!(classify_pin(Q0_PROTON), classify_pin(Q0_MUON));
        let rel = (Q0_PROTON - Q0_MUON).abs() / Q0_PROTON;
        assert!(rel > 1e-9 && rel < 1e-7, "pin gap moved: {rel:e}");
    }

    /// A value that round-tripped through a decimal string must still classify.
    #[test]
    fn classification_survives_a_string_round_trip() {
        let s = format!("{Q0_PROTON}");
        assert_eq!(classify_pin(s.parse::<f64>().unwrap()), "proton");
    }

    #[test]
    fn capture_records_a_runnable_command_and_the_pin() {
        let g = Generation::capture(Q0_PROTON);
        assert_eq!(g.q0_pin, "proton");
        assert!(!g.binary.is_empty());
        // argv[0] must be a bare file name, not a build path, or the record
        // would differ between machines for the same run.
        assert!(!g.binary.contains('/'), "binary not normalised: {}", g.binary);
        assert_eq!(g.argv.first().unwrap(), &g.binary);
        assert!(g.reproduce.starts_with("cargo run --release --bin "));
        assert!(g.reproduce.contains(&g.binary));
    }

    /// `capture` must report the anchor it was GIVEN, not a constant — a
    /// binary with an explicit `--q` has to record what it actually used.
    #[test]
    fn capture_reports_the_anchor_it_was_given() {
        assert_eq!(Generation::capture(Q0_MUON).q0_pin, "muon");
        assert_eq!(Generation::capture(2.0).q0_pin, "other");
        assert_eq!(Generation::capture(2.0).q0, 2.0);
    }
}
