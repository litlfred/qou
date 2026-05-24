//! hecke-engine-c — C-ABI bindings for hecke-engine.
//!
//! Tier-3 wrapper per workplan v2 §3.6. Sibling of pyhecke-native,
//! hecke-engine-{node,wasm,jvm,r}. The C ABI is the universal
//! lowest-common-denominator — consumed by:
//!   - Octave (via MEX shim)
//!   - Native iOS / Android (via Bridging-Header / JNI)
//!   - Embedded Lua / Tcl / Guile / etc.
//!   - R via `.Call()` (independent of extendr; alternative path)
//!
//! All exported functions use `#[no_mangle] extern "C"` so cbindgen
//! emits them into `include/hecke_engine.h` with C-compatible
//! signatures. The header is committed for downstream-consumer
//! convenience but regenerates cleanly on every `cargo build`.
//!
//! Memory ownership: arrays returned to C consumers (gram-matrix
//! flatten + trace-weights vector) are caller-allocated. The
//! consumer passes in a `double*` of the right size, we fill it.
//! No malloc/free across the FFI boundary — keeps the ABI safe
//! for any C-callable runtime.

use hecke_engine::gram;

/// Engine version as a null-terminated C string.
///
/// The returned pointer points into a static buffer; the caller
/// must NOT free it. Valid for the lifetime of the process.
#[no_mangle]
pub extern "C" fn qou_hecke_version() -> *const std::os::raw::c_char {
    // env!() expands to a 'static &str; the null-terminated form is
    // built once and leaked (it's tiny + lives for the process).
    static VERSION: std::sync::OnceLock<std::ffi::CString> = std::sync::OnceLock::new();
    let s = VERSION.get_or_init(|| {
        std::ffi::CString::new(env!("CARGO_PKG_VERSION")).unwrap()
    });
    s.as_ptr()
}

/// Markov parameter z = 1 / (q^{1/2} + q^{-1/2}).
#[no_mangle]
pub extern "C" fn qou_hecke_markov_z(q: f64) -> f64 {
    gram::markov_z(q)
}

/// Hecke relation coefficient h = q - q^{-1}.
#[no_mangle]
pub extern "C" fn qou_hecke_h(q: f64) -> f64 {
    gram::hecke_h(q)
}

/// Markov-trace weights on the NF basis.
///
/// `out` must point to at least 6 contiguous `double`s. Fills:
///   out[0..6] = [1, z, z, z^2, z^2, z^3]
/// where z = qou_hecke_markov_z(q).
#[no_mangle]
pub extern "C" fn qou_hecke_trace_weights(q: f64, out: *mut f64) {
    if out.is_null() { return; }
    let w = gram::trace_weights(q);
    unsafe {
        std::ptr::copy_nonoverlapping(w.as_ptr(), out, 6);
    }
}

/// Gram matrix G_ij = tr_M(b_i * b_j), row-major.
///
/// `out` must point to at least 36 contiguous `double`s. Fills:
///   out[i*6 + j] = G[i][j]   for i, j in 0..6
#[no_mangle]
pub extern "C" fn qou_hecke_gram_matrix_flat(q: f64, out: *mut f64) {
    if out.is_null() { return; }
    let m = gram::gram_matrix(q);
    let mut k = 0usize;
    for row in m.iter() {
        for &v in row.iter() {
            unsafe { *out.add(k) = v; }
            k += 1;
        }
    }
}

/// Gram determinant.
#[no_mangle]
pub extern "C" fn qou_hecke_gram_det(q: f64) -> f64 {
    gram::det_6x6(&gram::gram_matrix(q))
}
