// Compile-time guards on incompatible Clarabel-feature combinations.
//
// As of the litlfred Clarabel.rs fork rev 37f06c3 (PR #7), `MpfrFloat`
// implements native MPFR Cholesky / Jacobi-eigen / Jacobi-SVD PSD cones,
// so `clarabel-mpfr` and `clarabel-sdp` (`clarabel-mpfr-sdp`) compose
// cleanly for 50–80+ dps SDPs. `RationalReal` (`clarabel-bigrational`)
// remains LP/QP-only (exact rational eigendecomposition does not exist)
// and cannot share Clarabel's scalar parameter `T` with `clarabel-mpfr`.
#[cfg(all(feature = "clarabel-sdp", feature = "clarabel-bigrational"))]
compile_error!(
    "clarabel-sdp and clarabel-bigrational are mutually exclusive: \
     Clarabel-rs rational arithmetic supports LP/QP cones only (no rational \
     PSD eigendecomposition).  Pick one feature or the other."
);
#[cfg(all(feature = "clarabel-bigrational", feature = "clarabel-mpfr"))]
compile_error!(
    "clarabel-bigrational and clarabel-mpfr cannot both be enabled: \
     each provides its own concrete scalar type via the same upstream \
     `T` parameter — pick one backend."
);

// The mpfr feature (default on) controls the transitive rug-dependent
// surface. Two tiers:
//
//   Tier A — `use rug` at module top: dense_la_mpfr, seminormal_mpfr,
//            tr_m_atomic_mpfr, sdp_clarabel_mpfr_prep.
//   Tier B — `use rug` in inner functions: laurent_poly_q,
//            laurent_rational_q, precision_scalar, geck_pfeiffer.
//   Tier C — transitive via Tier A/B imports: laurent_hecke_element
//            (←laurent_rational_q), reduce_laurent (←laurent_rational_q),
//            seminormal_mn (←laurent_poly_q), tr_m_word_lq
//            (←laurent_poly_q), wenzl_lr (←laurent_poly_q +
//            seminormal_mpfr), atomic_reduce_cache (←laurent_hecke_element).
//
// Together this is the "mpfr cone". Disabling `mpfr` carves out the
// pure-Rust canonical surface for WASM: certificate, cross_level_embedding,
// gb_nf_reducer, gram, joint_tower_sdp_certificate, littlewood_richardson,
// rational_round, sdp_verifier, seminormal, sturm_psd, wedderburn_psd
// — ~3 500 LOC of WASM-targetable compute.

pub mod certificate;
pub mod color_weight;
pub mod cross_level_embedding;
#[cfg(feature = "mpfr")]
pub mod dense_la_mpfr;
#[cfg(feature = "mpfr")]
pub mod tl_cable;
pub mod gb_nf_reducer;
#[cfg(feature = "mpfr")]
pub mod geck_pfeiffer;
pub mod gram;
pub mod joint_tower_sdp_certificate;
pub mod kazhdan_lusztig;
#[cfg(feature = "mpfr")]
pub mod laurent_hecke_element;
#[cfg(feature = "mpfr")]
pub mod laurent_poly_q;
#[cfg(feature = "mpfr")]
pub mod laurent_rational_q;
pub mod littlewood_richardson;
#[cfg(feature = "mpfr")]
pub mod precision_scalar;
/// Reproducibility record for emitted certificates (argv + anchor + a
/// ready-to-run command). See the module docs for why it exists.
pub mod provenance;
pub mod rational_round;
#[cfg(feature = "mpfr")]
pub mod reduce_laurent;
// Clarabel-rs SDP backends are opt-in behind the `clarabel-sdp` feature.
// Default builds use only the bisection-based α* verifier (sdp_verifier),
// which works at any d without an external SDP solver.
//
// sdp_clarabel_mpfr_prep additionally requires `mpfr` because it uses
// `rug::Float` at module top — gating it on `clarabel-sdp` alone would
// fail to compile under `--features clarabel-sdp --no-default-features`.
// Per PR #1094 review (Copilot).
#[cfg(all(feature = "clarabel-sdp", feature = "mpfr"))]
pub mod sdp_clarabel_mpfr_prep;
#[cfg(feature = "clarabel-sdp")]
pub mod sdp_dual_certificate;
#[cfg(feature = "clarabel-sdp")]
pub mod sdp_per_block;
#[cfg(feature = "clarabel-sdp")]
pub mod sdp_recover_canonical;
#[cfg(feature = "clarabel-sdp")]
pub mod sdp_solve_canonical_t_w;
#[cfg(feature = "clarabel-sdp")]
pub mod sdp_solver_clarabel;
#[cfg(feature = "clarabel-mpfr")]
pub mod operator_selection_lp;
#[cfg(feature = "clarabel-sdp")]
pub mod operator_selection_sdp;
pub mod sdp_verifier;
pub mod seminormal;
pub mod seminormal_exact;
#[cfg(feature = "mpfr")]
pub mod seminormal_mn;
#[cfg(feature = "mpfr")]
pub mod seminormal_mpfr;
#[cfg(feature = "mpfr")]
pub mod matrix_m_mpfr;
#[cfg(feature = "mpfr")]
pub mod atomic_reduce_cache;
pub mod sturm_psd;
#[cfg(feature = "mpfr")]
pub mod tl_cable_mpfr;
#[cfg(feature = "mpfr")]
pub mod tr_m_atomic_mpfr;
#[cfg(feature = "mpfr")]
pub mod tr_m_word_lq;
pub mod wedderburn_psd;
#[cfg(feature = "mpfr")]
pub mod wenzl_lr;
