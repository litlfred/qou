// Compile-time guards on incompatible Clarabel-feature combinations.
//
// The upstream Clarabel-rs SDP path defines `MaybeBlasFloatT: Copy`
// under `cfg(feature = "sdp")` (src/algebra/floats.rs:111).  Neither
// `RationalReal` (bigrational backend) nor `MpfrFloat` (mpfr backend)
// is `Copy` — they wrap heap-allocated arbitrary-precision values.
// Enabling `sdp + bigrational` or `sdp + mpfr` together would
// fail to compile inside Clarabel itself with a generic-bound error.
// Surface the conflict here with a clear message instead of letting
// downstream consumers hit the inscrutable Copy-bound failure.
#[cfg(all(feature = "clarabel-sdp", feature = "clarabel-bigrational"))]
compile_error!(
    "clarabel-sdp and clarabel-bigrational are mutually exclusive: \
     upstream Clarabel-rs requires MaybeBlasFloatT: Copy under cfg(sdp), \
     and BigRational is not Copy.  Pick one feature or the other."
);
#[cfg(all(feature = "clarabel-sdp", feature = "clarabel-mpfr"))]
compile_error!(
    "clarabel-sdp and clarabel-mpfr are mutually exclusive: \
     upstream Clarabel-rs requires MaybeBlasFloatT: Copy under cfg(sdp), \
     and MpfrFloat is not Copy.  Use clarabel-sdp + the f64 path \
     plus per-block MPFR-precision constraint preparation \
     (CLARABEL_PRECISION_PLAN.md §S4-MPFR), or clarabel-mpfr alone \
     for LP/QP/SOCP-only problems."
);
#[cfg(all(feature = "clarabel-bigrational", feature = "clarabel-mpfr"))]
compile_error!(
    "clarabel-bigrational and clarabel-mpfr cannot both be enabled: \
     each provides its own concrete scalar type via the same upstream \
     `T` parameter — pick one backend."
);

pub mod certificate;
pub mod cross_level_embedding;
pub mod dense_la_mpfr;
pub mod gb_nf_reducer;
pub mod geck_pfeiffer;
pub mod gram;
pub mod joint_tower_sdp_certificate;
pub mod laurent_poly_q;
pub mod laurent_rational_q;
pub mod littlewood_richardson;
pub mod precision_scalar;
pub mod rational_round;
// Clarabel-rs SDP backends are opt-in behind the `clarabel-sdp` feature.
// Default builds use only the bisection-based α* verifier (sdp_verifier),
// which works at any d without an external SDP solver.
#[cfg(feature = "clarabel-sdp")]
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
pub mod sdp_verifier;
pub mod seminormal;
pub mod seminormal_mn;
pub mod seminormal_mpfr;
pub mod sturm_psd;
pub mod tr_m_word_lq;
pub mod wedderburn_psd;
pub mod wenzl_lr;
