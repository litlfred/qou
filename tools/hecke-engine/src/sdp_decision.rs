//! Unified SDP decision core — H_3(q) level.
//!
//! Parity partner of `folio-assistant/computations/sdp_decision.py`
//! for decisions whose candidate braid words live in H_3(q) (6-D NF).
//! Wider-algebra decisions (H_{3A}, H_{3A+2Z}) stay in Python until
//! the seminormal Plancherel sum is ported to Rust.
//!
//! Every non-SDP decision point in the atom-mass pipeline has the
//! same structural shape:
//!
//!   given a finite candidate set  C = {c_1, ..., c_K}
//!   each candidate c_k defines a Hecke braid word  W_k
//!   select the candidate that minimizes  tr_M(W_k · e_0)
//!   subject to Frobenius positivity  x_k^T G x_k >= 0
//!   with a dual-price certificate for every losing candidate.
//!
//! For real Hecke products the Frobenius constraint is auto-satisfied
//! (see `sdp_lift_audit`), so the SDP reduces to an LP over the
//! simplex. Argmin plus the gaps
//!
//!     g_k = tr_M(c_k) − tr_M(c*)
//!
//! are the dual-price certificates that replace heuristic
//! `min(valid, key=...)` selections with an optimality margin.
//!
//! H_3-level items targeted by this module:
//!   #4 gluon per-nucleon multiplicity (single-generator confinement)
//!   #7 Borromean exponent  n  in  (σ₀σ₁⁻¹)^n
//!   #11 Wedderburn weights as NF-basis scalar choices
//!   #12 quark crossing assignments

use serde::{Deserialize, Serialize};

use crate::atom::{hm, nf_tr};

/// One step of a braid word: `(c · σ_gen + d · 1)`.
pub type BraidStep = (f64, f64, u8);

/// A labelled candidate: a name plus its braid word.
pub type Candidate = (String, Vec<BraidStep>);

/// Result of an SDP decision over a discrete candidate set.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SdpDecisionReport {
    pub label: String,
    pub n_candidates: usize,
    /// `tr_M` per candidate, keyed by name.
    pub tr_m_by_candidate: Vec<(String, f64)>,
    pub optimal_name: String,
    pub optimal_tr_m: f64,
    /// SDP dual gaps `tr_M(c_k) − tr_M(c*)`, keyed by name.
    pub dual_gaps: Vec<(String, f64)>,
    /// For real Hecke products this is always true.
    pub frobenius_auto_valid: bool,
}

impl SdpDecisionReport {
    pub fn summary_lines(&self) -> Vec<String> {
        let mut out = vec![
            format!("  ── SDP decision ({}) ──", self.label),
            format!("  candidates: {}", self.n_candidates),
            format!("  optimal: {}  tr_M = {:+.6e}",
                self.optimal_name, self.optimal_tr_m),
        ];
        // Up to 5 runners-up by ascending gap.
        let mut sorted: Vec<&(String, f64)> = self.dual_gaps.iter().collect();
        sorted.sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(
            std::cmp::Ordering::Equal));
        let mut shown = 0;
        for (name, gap) in sorted {
            if *name == self.optimal_name {
                continue;
            }
            out.push(format!("    gap[{}] = {:+.6e}", name, gap));
            shown += 1;
            if shown >= 5 {
                break;
            }
        }
        out
    }
}

/// Apply a braid word to the identity NF vector `[1, 0, 0, 0, 0, 0]`
/// and return `tr_M` of the result at `q`.
fn apply_and_trace(word: &[BraidStep], q: f64, h: f64) -> f64 {
    let mut nf: [f64; 6] = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    for &(c, d, gen) in word {
        nf = hm(&nf, c, d, gen, h);
    }
    nf_tr(&nf, q)
}

/// SDP decision over discrete H_3(q) Hecke-word candidates.
///
/// For real Hecke products Frobenius positivity is auto-satisfied;
/// the SDP reduces to argmin over `tr_M` with dual-price certificates.
pub fn sdp_decide(
    candidates: &[Candidate],
    q: f64,
    h: f64,
    label: &str,
) -> SdpDecisionReport {
    let mut tr_m_by: Vec<(String, f64)> = Vec::with_capacity(candidates.len());
    for (name, word) in candidates {
        let t = apply_and_trace(word, q, h);
        tr_m_by.push((name.clone(), t));
    }
    let mut opt_idx = 0;
    let mut opt_val = f64::INFINITY;
    for (i, &(_, t)) in tr_m_by.iter().enumerate() {
        if t < opt_val {
            opt_val = t;
            opt_idx = i;
        }
    }
    let (opt_name, _) = tr_m_by[opt_idx].clone();
    let dual_gaps: Vec<(String, f64)> = tr_m_by.iter()
        .map(|(n, t)| (n.clone(), t - opt_val))
        .collect();
    SdpDecisionReport {
        label: label.to_string(),
        n_candidates: candidates.len(),
        tr_m_by_candidate: tr_m_by,
        optimal_name: opt_name,
        optimal_tr_m: opt_val,
        dual_gaps,
        frobenius_auto_valid: true,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::nf::{Q_0, hecke_h};

    #[test]
    fn smoke_decide_identity_vs_sigma() {
        let h = hecke_h(Q_0);
        let cands: Vec<Candidate> = vec![
            ("identity".into(), vec![]),
            ("sigma_0".into(), vec![(1.0, 0.0, 0)]),
            ("sigma_1".into(), vec![(1.0, 0.0, 1)]),
            ("L_plus".into(),  vec![(1.0, 0.0, 0), (1.0, 0.0, 1)]),
        ];
        let rep = sdp_decide(&cands, Q_0, h, "smoke");
        assert_eq!(rep.n_candidates, 4);
        assert!(rep.dual_gaps.iter().all(|&(_, g)| g >= -1e-12));
        // Optimal gap is zero.
        let opt_gap = rep.dual_gaps.iter()
            .find(|&(n, _)| *n == rep.optimal_name).unwrap().1;
        assert!(opt_gap.abs() < 1e-12);
    }
}
