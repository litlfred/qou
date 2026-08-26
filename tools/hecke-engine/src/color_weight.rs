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

/// The **additive offset** of the p-n bond factor from the p-p factor `z`,
/// i.e. `pn_interface_factor(q, conv) - markov_z(q)`.
///
/// This is the `d` coefficient in [`crate::gram`]'s per-crossing
/// `(c, d)` parameterisation, where a bond contributes `c*z + d`:
///
/// | bond | `(c, d)` in `gram` | factor |
/// |---|---|---|
/// | p-p | `(1, 0)` | `z` |
/// | n-n | `(1, -h)` | `z - h` |
/// | p-n | `(1, pn_offset(q, conv))` | `z + pn_offset` |
///
/// It exists so that the `gram` p-n sites can *name* their convention
/// instead of open-coding `-0.5 * h`. See [`GRAM_PN_CONVENTION`].
#[inline]
pub fn pn_offset(q: f64, conv: PnConvention) -> f64 {
    let h = hecke_h(q);
    match conv {
        // Written as `-(0.5 * h)` rather than `-h / 2.0` so that it is
        // *syntactically* the expression the `gram` sites used before they
        // were wired here — the two are bit-identical (scaling by a power of
        // two is exact), and `pn_offset_is_bit_identical_to_the_open_coded_form`
        // asserts it.
        PnConvention::StrictAveraged => -(0.5 * h),
        PnConvention::BringColorWeighted => {
            -(h * (0.5 - flavor_split_leading(q) / 4.0))
        }
    }
}

/// [`pn_offset`] for a caller that holds only `h`, not `q`.
///
/// [`crate::gram::build_atom_nf`] is parameterised by `h = q - 1/q` alone, so
/// it cannot reach `delta(q)` directly. `h` *is* invertible for `q > 0` —
///
/// ```text
///   q = (h + sqrt(h^2 + 4)) / 2
/// ```
///
/// — so the canonical convention is reachable from that signature; it just
/// costs an archimedean square root that the `q`-carrying [`pn_offset`] does
/// not. The [`PnConvention::StrictAveraged`] arm needs no inversion at all
/// and is returned exactly.
///
/// Prefer [`pn_offset`] wherever `q` is in scope. This exists so that the
/// `h`-only signature is not mistaken for a *structural* obstruction to the
/// colour weighting — it is a soft one.
#[inline]
pub fn pn_offset_from_h(h: f64, conv: PnConvention) -> f64 {
    match conv {
        PnConvention::StrictAveraged => -(0.5 * h),
        PnConvention::BringColorWeighted => {
            let q = (h + (h * h + 4.0).sqrt()) / 2.0;
            pn_offset(q, conv)
        }
    }
}

/// The p-n convention the [`crate::gram`] atomic-braid path **currently**
/// evaluates at — deliberately a named constant rather than an inline
/// `-0.5 * h`, so the discrepancy below is visible at the call site.
///
/// # This is NOT the canonical convention
///
/// The owner ruling of 2026-08-15 (R3) makes
/// [`PnConvention::BringColorWeighted`] canonical for the p-n interface;
/// `gram` evaluates [`PnConvention::StrictAveraged`], which is the same
/// expression with `delta` forced to zero. The two differ by exactly
/// `h*delta/4` per p-n bond — about `7.19e-05` absolute at
/// [`crate::gram::Q_0`], which is ~1e11 times the f64 floor, so it is a
/// real shift and not rounding.
///
/// # Why it has not simply been flipped
///
/// Flipping this constant moves every number downstream of the atomic-braid
/// normal form. Measured 2026-08-25 on `main`: **51 Python files** and
/// **18 committed `*.witness.json`** consume those two `gram` sites. That is
/// an owner-scoped corpus migration, not an agent-side edit, so this constant
/// records the live state honestly instead of pre-empting it.
///
/// FLIPPED 2026-08-26 on owner authorisation ("do strict_averaged ->
/// bring_color_weighted"), which reaffirms the 2026-08-15 R3 ruling.
///
/// **The "51 Python files / 18 witnesses" figure above was a serious
/// undercount and is kept only as the record of what was believed.** It was
/// measured by grepping for files that NAME a convention. Measured instead by
/// import cone -- which is what actually determines whether a producer's
/// numbers move -- **1027 of the 1929 witness-writing producers** in
/// `computations/` reach a blind p-n site, 1027 of them through
/// `pyhecke/atom.py` and 449 through `hecke_characters.py`. That is an upper
/// bound: importing `atom.py` only matters for an atom that actually has a
/// mixed bond, so a proton-only or neutron-only producer is unaffected. But
/// it is the right order of magnitude, and it is two orders above the number
/// this doc comment used to carry.
pub const GRAM_PN_CONVENTION: PnConvention = PnConvention::BringColorWeighted;

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
    let mut ordering: Vec<u8> = vec![b'n'; a];
    ordering[..z_count].fill(b'p');
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

// ---------------------------------------------------------------------------
// Convergence self-check against the Python canonical.
// ---------------------------------------------------------------------------

/// Runtime convergence self-check against the Python canonical.
///
/// # Why this exists
///
/// This module is a **second numeric implementation** of a convention whose
/// first implementation is `computations/closed_form_tau_M.py`. That is a
/// drift surface — the same one bean `qou-m7py` closed for `trace_weights`
/// (`z^3` in Rust vs `h*z^2 + z` in Python, undetected because nothing
/// compared them). A port without a comparator re-opens it.
///
/// # The pattern (mirrored from `pyhecke.gram::_native_ok`)
///
/// 1. Pin the *other* implementation's output as an in-tree reference
///    ([`CANONICAL`]), the way `gram.py` pins `TR_M` / `G`.
/// 2. Recompute here and compare at a stated tolerance.
/// 3. On mismatch **refuse loudly** ([`DIVERGENCE_MSG`]) — never silently
///    return the divergent number.
pub mod convergence {
    use super::PnConvention;

    /// One row of the pinned Python canonical.
    #[derive(Debug, Clone, Copy)]
    pub struct CanonicalRow {
        /// Isotope label, for error messages.
        pub isotope: &'static str,
        /// Proton count `Z`.
        pub z_count: usize,
        /// Neutron count `N`.
        pub n_count: usize,
        /// `closed_form_ratio(Z, N, q0, "bring_color_weighted")` as a decimal
        /// string carrying 50 significant digits.
        pub ratio_50dps: &'static str,
    }

    /// The substrate anchor as a 50-digit decimal string — `q_parameter.Q_50_DIGIT_STR`,
    /// the **proton/experimental** pin. Kept as a string so no f64 rounding
    /// enters the reference; [`super::super::gram::Q_0`] is its f64 shadow.
    pub const Q0_50DPS: &str = "1.1099785827513808075916690956107688798744991218736";

    /// `delta(q0)` — pinned for the self-check of the flavour split alone.
    pub const DELTA_Q0_50DPS: &str =
        "0.0013757108070270960085511092741065506222254760119378";

    /// `f_pn(q0)` under `bring_color_weighted` — pinned separately from the
    /// ratios because it is the only factor this port introduces.
    pub const F_PN_Q0_50DPS: &str =
        "0.50822978937673896257799579765589360389830839091657";

    /// Python-canonical `closed_form_ratio` at the proton `q0`, produced by
    /// running, from the repo root:
    ///
    /// ```text
    /// python3 - <<'PY'
    /// import sys
    /// sys.path.insert(0, "computations"); sys.path.insert(0, "computations/substrate")
    /// import mpmath as mp; mp.mp.dps = 60
    /// from q_parameter import Q_50_DIGIT_STR
    /// from closed_form_tau_M import closed_form_ratio
    /// q = mp.mpf(Q_50_DIGIT_STR)
    /// for name, Z, N in [("2H",1,1),("3H",1,2),("3He",2,1),("4He",2,2),("6Li",3,3),("7Li",3,4)]:
    ///     print(name, mp.nstr(closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted"), 50))
    /// PY
    /// ```
    ///
    /// Captured 2026-08-15 against `closed_form_tau_M.py` at commit `85e94fb8`.
    /// If a future convention ruling moves these, regenerate with the command
    /// above — **do not** hand-edit a digit to make a test go green.
    pub const CANONICAL: &[CanonicalRow] = &[
        CanonicalRow {
            isotope: "2H",
            z_count: 1,
            n_count: 1,
            ratio_50dps: "0.50822978937673896257799579765589360389830839091657",
        },
        CanonicalRow {
            isotope: "3H",
            z_count: 1,
            n_count: 2,
            ratio_50dps: "0.20513564044864976892685000166038351176091031419587",
        },
        CanonicalRow {
            isotope: "3He",
            z_count: 2,
            n_count: 1,
            ratio_50dps: "0.31138631207259565241288839663309982228956162859607",
        },
        CanonicalRow {
            isotope: "4He",
            z_count: 2,
            n_count: 2,
            ratio_50dps: "0.12568415289526626941387850586668409901893672284696",
        },
        CanonicalRow {
            isotope: "6Li",
            z_count: 3,
            n_count: 3,
            ratio_50dps: "0.031081425408716222670195151585816318684920749964179",
        },
        CanonicalRow {
            isotope: "7Li",
            z_count: 3,
            n_count: 4,
            ratio_50dps: "0.012545325442440024606630167466307946009113087306982",
        },
    ];

    /// Relative tolerance for the **MPFR** comparison.
    ///
    /// The pinned references carry 50 significant digits, and `mpmath.nstr`
    /// rounds the 50th — so the reference itself is only meaningful to about
    /// `1e-49` relative. `1e-45` leaves four decades of headroom over that
    /// rounding while still being twenty decades stricter than the repo's
    /// 50-dps cross-check floor of `1e-25` (`compute-author.md` §1.1). A
    /// genuine algebraic divergence (a wrong bond factor, a dropped `delta/4`,
    /// convention C vs D) is `1e-3` or larger, so this gate has enormous
    /// discriminating margin and no false-positive risk from rounding.
    pub const TOL_MPFR: f64 = 1e-45;

    /// Relative tolerance for the **f64** comparison.
    ///
    /// The f64 path accumulates up to `A-1` multiplications of correctly
    /// rounded quotients; at the isotopes in [`CANONICAL`] that is at most six
    /// roundings, so `1e-15` is the honest bound. This is NOT a 50-dps check
    /// and is documented as lossy — it exists to catch an f64 *port* error,
    /// not to certify precision.
    pub const TOL_F64: f64 = 1e-15;

    /// Emitted verbatim on divergence. Mirrors `_NATIVE_STALE_MSG` in
    /// `pyhecke/gram.py`: name the likely cause, name the fix, and refuse.
    pub const DIVERGENCE_MSG: &str = concat!(
        "hecke_engine::color_weight DIVERGES from the Python canonical ",
        "(computations/closed_form_tau_M.py) at the proton q0. Likely causes, ",
        "in order: (1) a trace-convention ruling moved `markov_z` on one side ",
        "only (C `1/(q^1/2+q^-1/2)` vs D `q^3/(q^2+1)`); (2) the p-n factor ",
        "lost its `delta/4` colour weighting, collapsing to strict_averaged; ",
        "(3) `flavor_split_leading` was swapped for the POSITED subleading ",
        "form de-wired on 2026-06-29; (4) the q0 pin straddled the muon/proton ",
        "layer boundary. Regenerate the reference table with the command in ",
        "the `CANONICAL` docstring and reconcile the MATH. Refusing rather ",
        "than returning a divergent number. Do NOT widen TOL_MPFR."
    );

    /// A single divergent row.
    #[derive(Debug, Clone)]
    pub struct Divergence {
        /// Isotope that diverged.
        pub isotope: &'static str,
        /// Value this crate computed, as a decimal string.
        pub computed: String,
        /// Pinned Python-canonical value.
        pub expected: &'static str,
        /// Measured relative difference.
        pub rel_diff: f64,
        /// The tolerance that was applied.
        pub tol: f64,
    }

    /// Check the **f64** path against [`CANONICAL`] at [`TOL_F64`].
    ///
    /// Returns `Ok(max_rel_diff)` on agreement, or every divergent row.
    pub fn verify_f64_convergence() -> Result<f64, Vec<Divergence>> {
        let q = crate::gram::Q_0;
        let mut worst = 0.0f64;
        let mut bad = Vec::new();
        for row in CANONICAL {
            let got = super::closed_form_ratio(
                row.z_count,
                row.n_count,
                q,
                PnConvention::BringColorWeighted,
            );
            let want: f64 = row.ratio_50dps.parse().expect("pinned reference parses");
            let rel = ((got - want) / want).abs();
            if rel > worst {
                worst = rel;
            }
            // NaN must FAIL, not slip through: `rel > tol` alone would pass a
            // NaN silently, which is the one outcome this check exists to stop.
            if rel.is_nan() || rel > TOL_F64 {
                bad.push(Divergence {
                    isotope: row.isotope,
                    computed: format!("{got:.17e}"),
                    expected: row.ratio_50dps,
                    rel_diff: rel,
                    tol: TOL_F64,
                });
            }
        }
        if bad.is_empty() {
            Ok(worst)
        } else {
            Err(bad)
        }
    }

    /// Check the **MPFR** path against [`CANONICAL`] at [`TOL_MPFR`].
    ///
    /// This is the gate that matters: it is the only comparison in this crate
    /// carried out at the 50-dps L1 floor. `dps` is the working precision;
    /// pass at least 60 so the 50-digit reference is not the limiting factor.
    #[cfg(feature = "mpfr")]
    pub fn verify_mpfr_convergence(dps: u32) -> Result<f64, Vec<Divergence>> {
        use rug::Float;
        let bits = super::mpfr::bits_for_dps(dps);
        let q = Float::with_val(
            bits,
            Float::parse(Q0_50DPS).expect("pinned q0 parses"),
        );
        let mut worst = 0.0f64;
        let mut bad = Vec::new();
        for row in CANONICAL {
            let got = super::mpfr::closed_form_ratio_mpfr(
                row.z_count,
                row.n_count,
                &q,
                PnConvention::BringColorWeighted,
            );
            let want = Float::with_val(
                bits,
                Float::parse(row.ratio_50dps).expect("pinned reference parses"),
            );
            let diff = Float::with_val(bits, &got - &want);
            let rel = Float::with_val(bits, &diff / &want).abs().to_f64();
            if rel > worst {
                worst = rel;
            }
            // NaN must FAIL — see the note in `verify_f64_convergence`.
            if rel.is_nan() || rel > TOL_MPFR {
                bad.push(Divergence {
                    isotope: row.isotope,
                    computed: got.to_string_radix(10, Some(50)),
                    expected: row.ratio_50dps,
                    rel_diff: rel,
                    tol: TOL_MPFR,
                });
            }
        }
        if bad.is_empty() {
            Ok(worst)
        } else {
            Err(bad)
        }
    }

    /// Render divergences using [`DIVERGENCE_MSG`], for a caller that wants to
    /// panic / log rather than match on the rows.
    pub fn describe(bad: &[Divergence]) -> String {
        let mut s = String::from(DIVERGENCE_MSG);
        for d in bad {
            s.push_str(&format!(
                "\n  {}: computed {} vs canonical {} (rel {:.3e} > tol {:.0e})",
                d.isotope, d.computed, d.expected, d.rel_diff, d.tol
            ));
        }
        s
    }
}

#[cfg(test)]
mod tests {
    use super::convergence::{
        describe, verify_f64_convergence, CANONICAL, DELTA_Q0_50DPS, F_PN_Q0_50DPS,
        TOL_F64,
    };
    use super::*;
    use crate::gram::Q_0;

    /// Wiring the two `gram` p-n sites to [`pn_offset`] must not move a
    /// single bit — that is the whole premise on which the change was made
    /// without owner sign-off. `-(0.5 * h)` is exact (scaling by a power of
    /// two), so this is `assert_eq!` on `f64` deliberately, not a tolerance.
    #[test]
    fn pn_offset_is_bit_identical_to_the_open_coded_form() {
        for &q in &[Q_0, 1.0, 1.5, 2.0, 0.75] {
            let h = hecke_h(q);
            let open_coded = -(0.5 * h); // what gram.rs:726/888 used to inline
            assert_eq!(pn_offset(q, PnConvention::StrictAveraged), open_coded);
            assert_eq!(pn_offset_from_h(h, PnConvention::StrictAveraged), open_coded);
        }
    }

    /// The `h`-only entry point must agree with the `q`-carrying one under
    /// *both* conventions — i.e. the `q = (h + sqrt(h^2+4))/2` inversion is
    /// the genuine inverse of `h = q - 1/q` on `q > 0`, not an approximation
    /// that happens to be close at the anchor.
    #[test]
    fn pn_offset_from_h_round_trips_the_q_carrying_form() {
        for &q in &[Q_0, 1.0, 1.5, 2.0, 0.75] {
            let h = hecke_h(q);
            for conv in [PnConvention::StrictAveraged, PnConvention::BringColorWeighted] {
                let via_q = pn_offset(q, conv);
                let via_h = pn_offset_from_h(h, conv);
                assert!(
                    (via_q - via_h).abs() <= 1e-15 * via_q.abs().max(1.0),
                    "q={q}: via_q={via_q:.17e} via_h={via_h:.17e} ({conv:?})"
                );
            }
        }
    }

    /// The offset is the `gram` `d` coefficient: `factor = z + d`.
    #[test]
    fn pn_offset_is_the_factor_minus_z() {
        for conv in [PnConvention::StrictAveraged, PnConvention::BringColorWeighted] {
            let lhs = pn_interface_factor(Q_0, conv);
            let rhs = markov_z(Q_0) + pn_offset(Q_0, conv);
            assert!((lhs - rhs).abs() < 1e-16, "{conv:?}: {lhs} vs {rhs}");
        }
    }

    /// The p-n convention `gram` evaluates at is pinned by an assertion, so
    /// that it cannot drift silently in either direction.
    ///
    /// It previously asserted [`PnConvention::StrictAveraged`] and was
    /// written to fail the moment the constant moved -- deliberately, so the
    /// flip and the corpus migration it implies had to land together. That
    /// flip is now authorised (owner, 2026-08-26, reaffirming the 2026-08-15
    /// R3 ruling), so the assertion moves with it and keeps doing the same
    /// job facing the other way: anything that quietly reverted `gram` to the
    /// colour-blind constant would now break this test.
    #[test]
    fn gram_pn_convention_is_the_colour_weighted_one() {
        assert_eq!(
            GRAM_PN_CONVENTION,
            PnConvention::BringColorWeighted,
            "GRAM_PN_CONVENTION changed. `bring_color_weighted` is canonical \
             (owner ruling 2026-08-15 R3, reaffirmed 2026-08-26). Reverting it \
             to StrictAveraged makes `gram` colour-blind again and silently \
             renumbers every atom carrying a mixed bond (bean qou-cblw)."
        );

        // The two are far enough apart that no recorded number is ambiguous
        // about which convention produced it: h*delta/4 at the proton pin is
        // ~1e11 times the f64 floor.
        let blind = pn_offset(Q_0, PnConvention::StrictAveraged);
        let canon = pn_offset(Q_0, PnConvention::BringColorWeighted);
        assert!(
            (canon - blind).abs() > 1e-8,
            "the two conventions must stay distinguishable: {canon} vs {blind}"
        );
    }

    #[test]
    fn census_matches_python_at_the_light_isotopes() {
        // (Z, N) -> (positive, negative, averaged, total), from
        // closed_form_tau_M.interface_census — see /tmp ground-truth run.
        assert_eq!(interface_census(1, 1), (0, 0, 1, 1)); // 2H
        assert_eq!(interface_census(1, 2), (0, 1, 1, 2)); // 3H
        assert_eq!(interface_census(2, 1), (1, 0, 1, 2)); // 3He
        assert_eq!(interface_census(2, 2), (1, 1, 1, 3)); // 4He
        assert_eq!(interface_census(3, 3), (2, 2, 1, 5)); // 6Li
        assert_eq!(interface_census(3, 4), (2, 3, 1, 6)); // 7Li
    }

    #[test]
    fn single_nucleon_has_no_bonds() {
        assert!(canonical_interface_kinds(1, 0).is_empty());
        assert!(canonical_interface_kinds(0, 1).is_empty());
        assert!(canonical_interface_kinds(0, 0).is_empty());
        // An empty product is 1 — matches the Python's `mp.mpf(1)` early return.
        let r = closed_form_ratio(1, 0, Q_0, PnConvention::BringColorWeighted);
        assert!((r - 1.0).abs() < 1e-15);
    }

    #[test]
    fn pure_species_have_no_averaged_bond() {
        // p^4: three p-p bonds, no p-n — so the convention cannot matter.
        let bring = closed_form_ratio(4, 0, Q_0, PnConvention::BringColorWeighted);
        let strict = closed_form_ratio(4, 0, Q_0, PnConvention::StrictAveraged);
        assert_eq!(bring, strict);
        assert!((bring - markov_z(Q_0).powi(3)).abs() < 1e-15);
    }

    #[test]
    fn flavor_split_matches_python_f64() {
        let want: f64 = DELTA_Q0_50DPS.parse().unwrap();
        let got = flavor_split_leading(Q_0);
        assert!(
            ((got - want) / want).abs() < TOL_F64,
            "delta(q0): got {got:.17e}, want {want:.17e}"
        );
    }

    #[test]
    fn pn_factor_matches_python_f64() {
        let want: f64 = F_PN_Q0_50DPS.parse().unwrap();
        let got = pn_interface_factor(Q_0, PnConvention::BringColorWeighted);
        assert!(
            ((got - want) / want).abs() < TOL_F64,
            "f_pn(q0): got {got:.17e}, want {want:.17e}"
        );
    }

    #[test]
    fn deuteron_ratio_is_exactly_the_pn_factor() {
        // A = 2 with one of each species: the product has a single bond.
        let ratio = closed_form_ratio(1, 1, Q_0, PnConvention::BringColorWeighted);
        let f_pn = pn_interface_factor(Q_0, PnConvention::BringColorWeighted);
        assert_eq!(ratio, f_pn);
    }

    #[test]
    fn colour_weighting_is_a_real_shift_not_a_no_op() {
        // Guards against a port that silently collapses to strict_averaged:
        // the two conventions must differ, by h*delta/4 on the single p-n bond.
        let bring = closed_form_ratio(1, 1, Q_0, PnConvention::BringColorWeighted);
        let strict = closed_form_ratio(1, 1, Q_0, PnConvention::StrictAveraged);
        let shift = hecke_h(Q_0) * flavor_split_leading(Q_0) / 4.0;
        assert!((bring - strict - shift).abs() < 1e-16);
        // ~7e-5 absolute at q0 — small, but a hundred times the f64 floor.
        assert!(shift > 5e-5 && shift < 1e-4, "shift = {shift:e}");
    }

    #[test]
    fn f64_path_converges_to_the_python_canonical() {
        match verify_f64_convergence() {
            Ok(worst) => assert!(worst <= TOL_F64, "worst rel {worst:.3e}"),
            Err(bad) => panic!("{}", describe(&bad)),
        }
    }

    #[test]
    fn canonical_table_is_self_consistent() {
        // Every pinned row parses and is a plausible ratio in (0, 1).
        for row in CANONICAL {
            let v: f64 = row.ratio_50dps.parse().unwrap();
            assert!(v > 0.0 && v < 1.0, "{}: {}", row.isotope, row.ratio_50dps);
            assert!(
                row.ratio_50dps.chars().filter(|c| c.is_ascii_digit()).count() >= 50,
                "{} reference lost digits",
                row.isotope
            );
        }
    }

    #[cfg(feature = "mpfr")]
    #[test]
    fn mpfr_path_converges_to_the_python_canonical_at_50dps() {
        use super::convergence::{verify_mpfr_convergence, TOL_MPFR};
        match verify_mpfr_convergence(60) {
            Ok(worst) => assert!(worst <= TOL_MPFR, "worst rel {worst:.3e}"),
            Err(bad) => panic!("{}", describe(&bad)),
        }
    }

    #[cfg(feature = "mpfr")]
    #[test]
    fn mpfr_beats_f64_on_the_same_input() {
        // The point of shipping two layers: show the MPFR one is actually
        // more accurate, rather than asserting it on faith.
        use super::convergence::{verify_f64_convergence, verify_mpfr_convergence};
        let f64_worst = verify_f64_convergence().expect("f64 path converges");
        let mpfr_worst = verify_mpfr_convergence(60).expect("mpfr path converges");
        assert!(
            mpfr_worst < f64_worst,
            "mpfr {mpfr_worst:.3e} should beat f64 {f64_worst:.3e}"
        );
    }
}
