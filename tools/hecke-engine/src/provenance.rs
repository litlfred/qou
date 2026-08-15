//! Reproducibility record for emitted certificates.
//!
//! # Why this exists
//!
//! On 2026-08-15 the substrate anchor `Q_0` was re-pinned muon → proton, and
//! the committed certificates needed regenerating to match. **They could not
//! be**, and the reason was not the compute cost — it was that a certificate
//! did not record enough about its own generation to be reproduced:
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
    /// Which pin `q0` is — `"proton"`, `"muon"`, or `"other"`.
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

/// Classify an anchor without asserting more precision than is meaningful.
///
/// The two pins are 11.54 ppb apart, so a tolerance anywhere between float64
/// noise and ~1e-9 separates them unambiguously; 1e-12 is used to leave room
/// for a value that round-tripped through a decimal string.
fn classify_pin(q0: f64) -> &'static str {
    if (q0 - Q0_PROTON).abs() < 1e-12 {
        "proton"
    } else if (q0 - Q0_MUON).abs() < 1e-12 {
        "muon"
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
