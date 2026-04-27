pub mod certificate;
pub mod cross_level_embedding;
pub mod gb_nf_reducer;
pub mod geck_pfeiffer;
pub mod gram;
pub mod joint_tower_sdp_certificate;
pub mod laurent_poly_q;
pub mod littlewood_richardson;
// Clarabel-rs SDP backends are opt-in behind the `clarabel-sdp` feature.
// Default builds use only the bisection-based α* verifier (sdp_verifier),
// which works at any d without an external SDP solver.
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
pub mod wedderburn_psd;
