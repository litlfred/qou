//! hecke-engine-node — napi-rs Node.js native bindings for hecke-engine.
//!
//! Re-exposes the same Gram + trace primitives as `pyhecke-native`'s
//! PyO3 layer, but for Node.js consumers via N-API. Tier-3 wrapper
//! per workplan v2 §3.6.
//!
//! Surface mirrors pyhecke-native intentionally: a Node consumer can
//! read pyhecke's docstrings to understand the API. Differences are
//! cosmetic (camelCase per JS convention).
//!
//! Phase A scope: the same handful of Gram + trace primitives that
//! pyhecke-native exposes today. Phase B adds the higher-level
//! `chi_lambda_braid` + `lr_coefficient` + `tr_m_atomic_mpfr` paths.
//!
//! Build:
//!   cd tools/hecke-engine-node
//!   npm install
//!   npm run build      # napi build → index.node + index.d.ts
//!   npm test           # runs the smoke tests in test/

use hecke_engine::gram;
use napi_derive::napi;

/// Markov parameter `z = 1 / (q^{1/2} + q^{-1/2})`.
#[napi]
pub fn markov_z(q: f64) -> f64 {
    gram::markov_z(q)
}

/// Hecke relation coefficient `h = q − q⁻¹`.
#[napi]
pub fn hecke_h(q: f64) -> f64 {
    gram::hecke_h(q)
}

/// Markov-trace weights on the NF basis as a length-6 array.
#[napi]
pub fn trace_weights(q: f64) -> Vec<f64> {
    gram::trace_weights(q).to_vec()
}

/// Gram matrix `G_ij = tr_M(b_i · b_j)` as a 6×6 array.
#[napi]
pub fn gram_matrix(q: f64) -> Vec<Vec<f64>> {
    gram::gram_matrix(q).iter().map(|r| r.to_vec()).collect()
}

/// Gram determinant — delegates to `hecke_engine::gram::det_6x6`.
#[napi]
pub fn gram_det(q: f64) -> f64 {
    gram::det_6x6(&gram::gram_matrix(q))
}

/// Package version string (matches Cargo.toml + package.json).
#[napi]
pub fn version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}
