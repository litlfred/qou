//! hecke-engine-r — extendr bindings for hecke-engine's gram primitives,
//! consumed from R.
//!
//! Tier-3 wrapper per workplan v2 §3.6. Sibling of:
//!   - pyhecke-native       (PyO3 → Python; production on PyPI)
//!   - hecke-engine-node    (napi-rs → Node.js; merged)
//!   - hecke-engine-wasm    (wasm-bindgen → browser; merged)
//!   - hecke-engine-jvm     (UniFFI → Kotlin/Swift/Java; merged)
//!   - hecke-engine-r       (extendr → R; this PR)
//!
//! Phase A surface mirrors the other 4 wrappers intentionally — an R
//! consumer can switch runtimes without API changes.
//!
//! Build (from R, via the `rextendr` package):
//!   library(rextendr)
//!   rextendr::document("tools/hecke-engine-r")
//!   # → generates R/extendr-wrappers.R + man/ pages + NAMESPACE
//!
//! Or via cargo:
//!   cd tools/hecke-engine-r
//!   cargo build --release

use extendr_api::prelude::*;
use hecke_engine::gram;

/// Engine version (matches Cargo.toml).
/// @export
#[extendr]
fn qou_version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

/// Markov parameter z = 1 / (q^{1/2} + q^{-1/2}).
/// @param q substrate parameter (numeric)
/// @return z (numeric)
/// @export
#[extendr]
fn qou_markov_z(q: f64) -> f64 {
    gram::markov_z(q)
}

/// Hecke relation coefficient h = q - q^{-1}.
/// @param q substrate parameter (numeric)
/// @return h (numeric)
/// @export
#[extendr]
fn qou_hecke_h(q: f64) -> f64 {
    gram::hecke_h(q)
}

/// Markov-trace weights on the NF basis (length-6 numeric vector).
/// @param q substrate parameter (numeric)
/// @return [1, z, z, z^2, z^2, z^3]
/// @export
#[extendr]
fn qou_trace_weights(q: f64) -> Vec<f64> {
    gram::trace_weights(q).to_vec()
}

/// Gram matrix G_ij = tr_M(b_i * b_j), returned as a 6x6 R matrix.
/// @param q substrate parameter (numeric)
/// @return 6x6 numeric matrix
/// @export
#[extendr]
fn qou_gram_matrix(q: f64) -> RMatrix<f64> {
    let m = gram::gram_matrix(q);
    let mut flat = Vec::with_capacity(36);
    // R is column-major; flatten accordingly so the matrix indexes correctly.
    for j in 0..6 {
        for i in 0..6 {
            flat.push(m[i][j]);
        }
    }
    RMatrix::new_matrix(6, 6, |r, c| flat[c * 6 + r])
}

/// Gram determinant.
/// @param q substrate parameter (numeric)
/// @return det(G(q)) (numeric)
/// @export
#[extendr]
fn qou_gram_det(q: f64) -> f64 {
    gram::det_6x6(&gram::gram_matrix(q))
}

// extendr macro that generates the R package boilerplate
// (wrapper.so registration + NAMESPACE entries).
extendr_module! {
    mod hecke_engine_r;
    fn qou_version;
    fn qou_markov_z;
    fn qou_hecke_h;
    fn qou_trace_weights;
    fn qou_gram_matrix;
    fn qou_gram_det;
}
