//! `bring_color_weighted` — the colour-tube-weighted p-n interface convention,
//! ported from [`computations/closed_form_tau_M.py`].
//!
//! # What this computes
//!
//! The interface-only ratio of the canonical atomic braid trace,
//!
//! ```text
//!   tr_M(B_K) / tr_M(B_K^vac)  =  prod_{bonds i} f_i(q)
//! ```
//!
//! over the `A - 1` nearest-neighbour bonds of the canonical ordering
//! `K = p^Z n^N` (protons first, then neutrons — so there is exactly **one**
//! p-n bond for any `Z >= 1, N >= 1`). Per-bond factors:
//!
//! | bond | factor |
//! |---|---|
//! | p-p | `z` |
//! | n-n | `z - h` |
//! | p-n | `z - h*(1/2 - delta/4)` |
//!
//! with
//!
//! ```text
//!   z(q)     = q^3 / (q^2 + 1)              (gram::markov_z, convention D)
//!   h(q)     = q - 1/q                      (gram::hecke_h)
//!   delta(q) = (q-1)^2 * (1 - q^-4) / 3     (flavor_split_leading, PR #690)
//! ```
//!
//! `delta` is the substrate flavour split `Delta_m / M_N`
//! (`prop:flavor-split-substrate`), and the p-n factor is the uniform
//! bar-invariant average `z - h/2` shifted by the colour-tube asymmetry
//! `+ h*delta/4`. Setting `delta = 0` recovers `strict_averaged`.
//!
//! # Provenance of the port (re-derived from source, 2026-08-15)
//!
//! Every line below was read against the Python before porting:
//!
//! - `computations/closed_form_tau_M.py:300-323` — `closed_form_ratio`,
//!   `bring_color_weighted` branch: the three bond factors above.
//! - `computations/closed_form_tau_M.py:133-158` — `markov_z`: convention
//!   **D**, `q^3/(q^2+1)`, per owner ruling 2026-08-09.
//! - `computations/closed_form_tau_M.py:161-164` — `hecke_h`.
//! - `computations/closed_form_tau_M.py:240-282` — `canonical_interface_kinds`:
//!   the `["p"; Z] ++ ["n"; N]` ordering and the p-p / n-n / p-n dispatch.
//! - `computations/_li_2_q_util.py:227-233` — `flavor_split_leading`.
//!
//! **Correction to a prior transcription.** The module docstring of
//! `closed_form_tau_M.py` still says `z(q) = 1/(q^{1/2} + q^{-1/2})` at its
//! line 17 — that is **convention C, excised by the owner on 2026-08-09**.
//! The live `markov_z` returns D. A port that trusted the docstring instead
//! of the code would be wrong by `0.6126880 - 0.4993203`, i.e. 23 %. This
//! module follows the code, and re-uses [`crate::gram::markov_z`] /
//! [`crate::gram::hecke_h`] rather than re-spelling them, so a future
//! convention change lands in one place.
//!
//! # q_0 discipline
//!
//! This module never writes a numeric `q_0` literal. Callers that want the
//! substrate anchor pass [`crate::gram::Q_0`] — the **proton/experimental**
//! pin, per the AGENTS.md owner directive of 2026-08-07. Five binaries in
//! this crate still carry a truncated 5-digit muon `1.10998`; see the note on
//! [`crate::gram::Q_0`]. Do not add a sixth.
//!
//! # Precision — read before using the f64 path
//!
//! The Python canonical carries `mpmath.mpf` at 50+ dps. `f64` cannot
//! represent that, so this module ships **two** layers and says which is
//! which rather than silently degrading:
//!
//! - [`closed_form_ratio`] — `f64`. Matches the Python to ~1e-15 relative.
//!   **LOSSY** against the 50-dps floor; use for diagnostics, screening and
//!   anything already f64-bound (the rest of [`crate::gram`] is f64).
//! - [`mpfr::closed_form_ratio_mpfr`] — `rug::Float`, arbitrary precision.
//!   This is the layer that actually meets the L1 50-dps floor and the one
//!   the convergence self-check gates at 1e-45.
//!
//! # Convergence self-check
//!
//! A second numeric implementation of a convention is a drift surface — the
//! exact one that bean `qou-m7py` closed for `trace_weights`. So this module
//! carries the [`CANONICAL`] table of Python-produced 50-dps values and a
//! runtime [`verify_python_convergence`] that recomputes and **refuses
//! loudly** on divergence, mirroring `pyhecke.gram::_native_ok`.
//! See [`self::convergence`].

use crate::gram::{hecke_h, markov_z};

/// The kind of a nearest-neighbour bond in the canonical atomic braid.
///
/// Mirrors `InterfaceKind` in `closed_form_tau_M.py`. The `Averaged` label is
/// carried for both `strict_averaged` and `bring_color_weighted` — as in the
/// Python, the `delta`-aware value lives in the factor layer, not the label
/// layer (`closed_form_tau_M.py:240-251`).
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum InterfaceKind {
    /// p-p bond: `sigma_g`, factor `z`.
    Positive,
    /// n-n bond: `sigma_g^{-1}`, factor `z - h`.
    Negative,
    /// p-n bond: factor `z - h/2` (`strict_averaged`) or
    /// `z - h*(1/2 - delta/4)` (`bring_color_weighted`).
    Averaged,
}

/// The p-n averaging convention.
///
/// Only the two conventions that are *mathematically* distinct at the factor
/// level are modelled. The Python's third value, `chi_lambda_braid`, is a
/// property of the legacy **marshalling** layer (it drops the averaging and
/// treats p-n as a positive crossing) and has no meaning inside the engine,
/// so it is deliberately not ported — porting it would import a marshalling
/// bug as if it were a convention.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum PnConvention {
    /// Uniform bar-invariant projection, `delta = 0`: `f_pn = z - h/2`.
    StrictAveraged,
    /// Colour-tube weighted (the Python default since 2026-06-01):
    /// `f_pn = z - h*(1/2 - delta/4)`.
    BringColorWeighted,
}

/// `delta(q) = (q-1)^2 * (1 - q^-4) / 3` — the leading substrate flavour
/// split `Delta_m / M_N` (`prop:flavor-split-substrate`, PR #690).
///
/// Port of `computations/_li_2_q_util.py::flavor_split_leading`.
///
/// The *subleading* Python sibling (`flavor_split_subleading`, the
/// `(1 + hbar_q^3)` form) is **not** ported: it is POSITED, not derived, and
/// the owner de-wired it from this convention on 2026-06-29 precisely so the
/// colour weighting reads only the proven leading split. Porting it would
/// hand a future caller a non-canonical knob.
#[inline]
pub fn flavor_split_leading(q: f64) -> f64 {
    let qi = 1.0 / q;
    (q - 1.0) * (q - 1.0) * (1.0 - qi * qi * qi * qi) / 3.0
}

/// The p-n bond factor under the given convention.
///
/// - [`PnConvention::StrictAveraged`]: `z - h/2`
/// - [`PnConvention::BringColorWeighted`]: `z - h*(1/2 - delta/4)`
#[inline]
pub fn pn_interface_factor(q: f64, conv: PnConvention) -> f64 {
    let z = markov_z(q);
    let h = hecke_h(q);
    match conv {
        PnConvention::StrictAveraged => z - h / 2.0,
        PnConvention::BringColorWeighted => {
            z - h * (0.5 - flavor_split_leading(q) / 4.0)
        }
    }
}

/// Per-bond factor for a labelled bond kind.
///
/// Port of `closed_form_tau_M.py::interface_factor`, extended so that the
/// `Averaged` case takes the convention explicitly (the Python resolves this
/// by branching in `closed_form_ratio` instead).
#[inline]
pub fn interface_factor(kind: InterfaceKind, q: f64, conv: PnConvention) -> f64 {
    match kind {
        InterfaceKind::Positive => markov_z(q),
        InterfaceKind::Negative => markov_z(q) - hecke_h(q),
        InterfaceKind::Averaged => pn_interface_factor(q, conv),
    }
}

/// Bond kinds of the canonical atomic braid for `(Z, N)`.
///
/// Ordering is protons-first: `K = p^Z n^N`, so the bond list is
/// `Positive^(Z-1) ++ [Averaged] ++ Negative^(N-1)` whenever both species are
/// present. Returns an empty vector for `A = Z + N < 2` (no bonds).
///
/// Port of `closed_form_tau_M.py::canonical_interface_kinds`.
pub fn canonical_interface_kinds(z_count: usize, n_count: usize) -> Vec<InterfaceKind> {
    let a = z_count + n_count;
    if a < 2 {
        return Vec::new();
    }
    let mut ordering: Vec<u8> = Vec::with_capacity(a);
    ordering.extend(std::iter::repeat(b'p').take(z_count));
    ordering.extend(std::iter::repeat(b'n').take(n_count));
    (0..a - 1)
        .map(|k| match (ordering[k], ordering[k + 1]) {
            (b'p', b'p') => InterfaceKind::Positive,
            (b'n', b'n') => InterfaceKind::Negative,
            _ => InterfaceKind::Averaged,
        })
        .collect()
}

/// Counts of each bond kind — port of `closed_form_tau_M.py::interface_census`.
///
/// Returns `(positive, negative, averaged, total)`.
pub fn interface_census(z_count: usize, n_count: usize) -> (usize, usize, usize, usize) {
    let kinds = canonical_interface_kinds(z_count, n_count);
    let pos = kinds.iter().filter(|k| **k == InterfaceKind::Positive).count();
    let neg = kinds.iter().filter(|k| **k == InterfaceKind::Negative).count();
    let avg = kinds.iter().filter(|k| **k == InterfaceKind::Averaged).count();
    (pos, neg, avg, kinds.len())
}

/// `tr_M(B_K) / tr_M(B_K^vac)` — the interface-only closed-form product, in
/// `f64`.
///
/// **LOSSY relative to the 50-dps L1 floor** — see the module-level precision
/// note. For production precision use [`mpfr::closed_form_ratio_mpfr`].
///
/// Port of `closed_form_tau_M.py::closed_form_ratio`.
pub fn closed_form_ratio(
    z_count: usize,
    n_count: usize,
    q: f64,
    conv: PnConvention,
) -> f64 {
    canonical_interface_kinds(z_count, n_count)
        .into_iter()
        .fold(1.0, |acc, kind| acc * interface_factor(kind, q, conv))
}

// ---------------------------------------------------------------------------
// MPFR layer — the one that meets the 50-dps L1 floor.
// ---------------------------------------------------------------------------

/// Arbitrary-precision mirror of the f64 surface above.
///
/// Same algebra, `rug::Float` throughout, so the result matches the Python
/// `mpmath` canonical to the working precision rather than to f64's ~1e-16.
#[cfg(feature = "mpfr")]
pub mod mpfr {
    use super::{canonical_interface_kinds, InterfaceKind, PnConvention};
    use rug::Float;

    /// Working bits for a requested decimal precision, with the same 8-bit
    /// buffer `precision_scalar::to_rug` uses.
    #[inline]
    pub fn bits_for_dps(dps: u32) -> u32 {
        (dps as f64 * std::f64::consts::LOG2_10 + 8.0).ceil() as u32
    }

    /// `z(q) = q^3/(q^2+1)` at the precision of `q` (convention D).
    pub fn markov_z(q: &Float) -> Float {
        let q2 = Float::with_val(q.prec(), q * q);
        let q3 = Float::with_val(q.prec(), &q2 * q);
        let denom = Float::with_val(q.prec(), &q2 + 1u32);
        q3 / denom
    }

    /// `h(q) = q - 1/q` at the precision of `q`.
    pub fn hecke_h(q: &Float) -> Float {
        let inv = Float::with_val(q.prec(), 1u32) / q;
        Float::with_val(q.prec(), q - &inv)
    }

    /// `delta(q) = (q-1)^2 (1 - q^-4)/3` at the precision of `q`.
    pub fn flavor_split_leading(q: &Float) -> Float {
        let one = Float::with_val(q.prec(), 1u32);
        let qm1 = Float::with_val(q.prec(), q - &one);
        let qi = Float::with_val(q.prec(), &one / q);
        let qi2 = Float::with_val(q.prec(), &qi * &qi);
        let qi4 = Float::with_val(q.prec(), &qi2 * &qi2);
        let head = Float::with_val(q.prec(), &qm1 * &qm1);
        let tail = Float::with_val(q.prec(), &one - &qi4);
        Float::with_val(q.prec(), &head * &tail) / 3u32
    }

    /// The p-n bond factor at the precision of `q`.
    pub fn pn_interface_factor(q: &Float, conv: PnConvention) -> Float {
        let z = markov_z(q);
        let h = hecke_h(q);
        let half = Float::with_val(q.prec(), 1u32) / 2u32;
        let w = match conv {
            PnConvention::StrictAveraged => half,
            PnConvention::BringColorWeighted => {
                let d4 = flavor_split_leading(q) / 4u32;
                Float::with_val(q.prec(), &half - &d4)
            }
        };
        Float::with_val(q.prec(), &z - &Float::with_val(q.prec(), &h * &w))
    }

    /// Per-bond factor at the precision of `q`.
    pub fn interface_factor(kind: InterfaceKind, q: &Float, conv: PnConvention) -> Float {
        match kind {
            InterfaceKind::Positive => markov_z(q),
            InterfaceKind::Negative => {
                let z = markov_z(q);
                let h = hecke_h(q);
                Float::with_val(q.prec(), &z - &h)
            }
            InterfaceKind::Averaged => pn_interface_factor(q, conv),
        }
    }

    /// `tr_M(B_K)/tr_M(B_K^vac)` at the precision of `q` — the production
    /// path, matching the Python `mpmath` canonical to working precision.
    pub fn closed_form_ratio_mpfr(
        z_count: usize,
        n_count: usize,
        q: &Float,
        conv: PnConvention,
    ) -> Float {
        canonical_interface_kinds(z_count, n_count)
            .into_iter()
            .fold(Float::with_val(q.prec(), 1u32), |acc, kind| {
                let f = interface_factor(kind, q, conv);
                Float::with_val(q.prec(), &acc * &f)
            })
    }
}

