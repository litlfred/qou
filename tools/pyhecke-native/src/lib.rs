//! PyO3 native acceleration layer for `pyhecke`.
//!
//! Re-exposes the hottest hecke-engine kernels as a Python extension
//! module `pyhecke_native`. No NumPy dependency — returns nested
//! Python lists that `pyhecke.bridge` converts on demand. This keeps
//! the wheel small and the build simple.

use hecke_engine::{gram, seminormal, seminormal_mn, seminormal_mpfr};
use pyo3::prelude::*;

/// Markov parameter z = 1 / (q^{1/2} + q^{-1/2}).
#[pyfunction]
fn markov_z(q: f64) -> f64 {
    gram::markov_z(q)
}

/// Hecke relation coefficient h = q - q^{-1}.
#[pyfunction]
fn hecke_h(q: f64) -> f64 {
    gram::hecke_h(q)
}

/// Markov-trace weights on the NF basis as a length-6 list.
#[pyfunction]
fn trace_weights(q: f64) -> Vec<f64> {
    gram::trace_weights(q).to_vec()
}

/// Gram matrix G_ij = tr_M(b_i · b_j) as a 6x6 list of lists.
#[pyfunction]
fn gram_matrix(q: f64) -> Vec<Vec<f64>> {
    gram::gram_matrix(q).iter().map(|r| r.to_vec()).collect()
}

/// Gram determinant — delegates to shared `hecke_engine::gram::det_6x6`.
#[pyfunction]
fn gram_determinant(q: f64) -> f64 {
    gram::det_6x6(&gram::gram_matrix(q))
}

/// Gram inverse as a 6x6 list of lists.
#[pyfunction]
fn gram_inverse(q: f64) -> Vec<Vec<f64>> {
    gram::gram_inverse(q).iter().map(|r| r.to_vec()).collect()
}

/// NF multiplication: multiply NF vector by `(c · σ_gen + d · 1)`.
///
/// Takes the 6-element NF vector and optional `h` (defaults to
/// `hecke_h(q_0)` = q_0 - q_0^{-1}). Returns a new 6-element list.
#[pyfunction]
#[pyo3(signature = (nf, c, d, gen, h=None))]
fn hm(nf: Vec<f64>, c: f64, d: f64, gen: u8, h: Option<f64>) -> PyResult<Vec<f64>> {
    if nf.len() != 6 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            format!("nf must have exactly 6 elements, got {}", nf.len()),
        ));
    }
    let arr: [f64; 6] = [nf[0], nf[1], nf[2], nf[3], nf[4], nf[5]];
    let h_val = h.unwrap_or_else(|| gram::hecke_h(gram::Q_0));
    Ok(gram::hm(&arr, c, d, gen, h_val).to_vec())
}

/// Markov trace of a 6-element NF vector at a given `q`.
#[pyfunction]
#[pyo3(signature = (nf, q=None))]
fn nf_tr(nf: Vec<f64>, q: Option<f64>) -> PyResult<f64> {
    if nf.len() != 6 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            format!("nf must have exactly 6 elements, got {}", nf.len()),
        ));
    }
    let arr: [f64; 6] = [nf[0], nf[1], nf[2], nf[3], nf[4], nf[5]];
    Ok(gram::nf_tr(&arr, q.unwrap_or(gram::Q_0)))
}

/// Sum of NF coefficients.
#[pyfunction]
fn nf_net(nf: Vec<f64>) -> PyResult<f64> {
    Ok(nf.iter().sum())
}

/// Build the full atom NF for (Z, N) via Hecke multiplication.
///
/// Mirrors `hecke_core.build_atom_nf`: proton / neutron B_3 confinement
/// + quark crossings + gluon self-coupling + inter-nucleon crossings +
/// electron (σ₁⁻¹) insertion. Returns a length-6 list of f64.
///
/// `h` defaults to `hecke_h(Q_0) = Q_0 - Q_0^{-1}` (the physical
/// substrate value). Pass an explicit `h` for alternative q.
#[pyfunction]
#[pyo3(signature = (z, n, h=None))]
fn build_atom_nf(z: u32, n: u32, h: Option<f64>) -> Vec<f64> {
    let h_val = h.unwrap_or_else(|| gram::hecke_h(gram::Q_0));
    gram::build_atom_nf(z, n, h_val).to_vec()
}

/// Per-generator Wedderburn volumes for the atom braid.
///
/// Returns a list of dicts `{sym, std, alt, full}` matching
/// `hecke_core.atom_per_generator_volumes`. `n_gens_total` =
/// `3A - 1` when `include_inter=True` (physical atom) else `2A`
/// (free baseline).
#[pyfunction]
#[pyo3(signature = (
    z, n,
    include_inter=true,
    crossings_per_pair=1,
    m_pp=None, m_pn=None, m_nn=None,
    q=None,
))]
#[allow(clippy::too_many_arguments)]
fn atom_per_generator_volumes(
    py: Python<'_>,
    z: u32,
    n: u32,
    include_inter: bool,
    crossings_per_pair: u32,
    m_pp: Option<u32>,
    m_pn: Option<u32>,
    m_nn: Option<u32>,
    q: Option<f64>,
) -> PyResult<PyObject> {
    let q_val = q.unwrap_or(gram::Q_0);
    let vols = gram::atom_per_generator_volumes(
        z, n, include_inter, crossings_per_pair,
        m_pp, m_pn, m_nn, q_val,
    );
    let list = pyo3::types::PyList::empty(py);
    for v in vols {
        let d = pyo3::types::PyDict::new(py);
        d.set_item("sym", v.sym)?;
        d.set_item("std", v.std)?;
        d.set_item("alt", v.alt)?;
        d.set_item("full", v.full)?;
        list.append(d)?;
    }
    Ok(list.into())
}

/// Hoefsmit seminormal character `χ_λ(β)` of a braid `β` for partition
/// `shape` at parameter `q`.
///
/// `shape`: partition λ ⊢ n as a list of descending part sizes.
/// `word`: braid as `[(sign, generator_index_1based), ...]`,
///   `sign ∈ {+1, -1}`, `generator_index ∈ {1, ..., n-1}`.
/// `q`: Hecke parameter (substrate value).
///
/// Returns `χ_λ(β) ∈ ℝ`.  Uses the sparse Hoefsmit kernel; gives a
/// ~50–100× speedup over the pure-Python implementation for `n ≥ 9`.
#[pyfunction]
fn chi_lambda_braid(shape: Vec<usize>, word: Vec<(i32, u32)>, q: f64) -> f64 {
    seminormal::chi_lambda_braid(&shape, &word, q)
}

/// Enumerate all partitions of `n` as a list of lists.
#[pyfunction]
fn partitions_of(n: usize) -> Vec<Vec<usize>> {
    seminormal::partitions_of(n)
}

/// **Classical Murnaghan-Nakayama character** `χ^λ(μ)`.
///
/// Computes the irreducible character of the symmetric group `S_n`
/// at the conjugacy class of cycle type `μ`, on the irrep indexed by
/// partition `λ`.  Returns an integer (classical MN values are in ℤ).
///
/// **Cost**: O(n² · #(border-strip-tableaux)) per character.  For
/// cross-validation with the Hoefsmit seminormal kernel at q = 1.
///
/// `lambda`: partition of n.
/// `mu`: cycle type (list of cycle lengths in any order).
#[pyfunction]
fn mn_chi(lambda: Vec<usize>, mu: Vec<usize>) -> i64 {
    seminormal_mn::mn_chi(&lambda, &mu)
}

/// **q-deformed character of an arbitrary braid word** via Hecke
/// expansion of inverse generators.
///
/// `chi_q_word(lambda, n_strands, word)` computes `χ_λ(β; q)` for
/// `β = product of (sign_i · σ_{gen_i})` returning a Laurent
/// polynomial as `[(half_exp, coeff_str), ...]`.  See
/// [`mn_chi_q`] for the polynomial encoding format.
///
/// Internally expands `σ⁻¹ = σ − h` for each negative generator
/// (cost `2^(#negatives)` per character — practical for short
/// atomic braids).
#[pyfunction]
fn chi_q_word(
    lambda: Vec<usize>,
    n_strands: usize,
    word: Vec<(i32, u32)>,
) -> Vec<(i32, String)> {
    let poly = seminormal_mn::chi_lambda_braid_qdef(&lambda, n_strands, &word);
    poly.terms
        .into_iter()
        .map(|(he, c)| (he, c.to_string()))
        .collect()
}

/// **q-deformed Murnaghan-Nakayama character** `χ^λ(T_w; q)`.
///
/// Computes the Hecke character of the canonical permutation braid
/// `T_w ∈ H_n(q)` of cycle type `μ`, returning the result as a list
/// of `(half_exponent, coefficient)` pairs encoding a Laurent
/// polynomial in `q^{1/2}`.  The half-exponent `2k` represents
/// `q^{k}`; `2k+1` represents `q^{(2k+1)/2}`.
///
/// At `q = 1` (sum of coefficients) this collapses to classical
/// MN — verified by Rust unit tests.  Currently handles
/// permutation-form braids only; mixed-sign generators (inverses)
/// require Hecke-relation expansion (next milestone).
///
/// Returns `[(half_exp, coeff_str), ...]` where `coeff_str` is the
/// BigInt rendered as decimal (callers parse via `int(s)`).
#[pyfunction]
fn mn_chi_q(lambda: Vec<usize>, mu: Vec<usize>) -> Vec<(i32, String)> {
    let poly = seminormal_mn::chi_lambda_mn_qdef(&lambda, &mu);
    poly.terms
        .into_iter()
        .map(|(he, c)| (he, c.to_string()))
        .collect()
}

/// **Batch character evaluation across many partitions** (rayon-parallel).
///
/// Evaluates `χ_λ(β)` for every partition in `shapes` in parallel using
/// Rust rayon.  Returns a `List[float]` in the same order.
///
/// Faster than calling `chi_lambda_braid` from a Python
/// `multiprocessing.Pool`: no per-partition pickling overhead, rayon
/// work-stealing balances dim variation across partitions.
#[pyfunction]
fn chi_lambdas_braid(
    shapes: Vec<Vec<usize>>,
    word: Vec<(i32, u32)>,
    q: f64,
) -> Vec<f64> {
    seminormal::chi_lambdas_braid(&shapes, &word, q)
}

/// **Batch MPFR character evaluation across many partitions** (rayon-parallel).
///
/// Like `chi_lambda_braid_mpfr` but in batch.  Returns a `List[str]`,
/// each entry being a decimal string at requested `dps` precision.
#[pyfunction]
#[pyo3(signature = (shapes, word, q_str, dps=50))]
fn chi_lambdas_braid_mpfr(
    shapes: Vec<Vec<usize>>,
    word: Vec<(i32, u32)>,
    q_str: String,
    dps: u32,
) -> Vec<String> {
    seminormal_mpfr::chi_lambdas_braid_mpfr(&shapes, &word, &q_str, dps)
}

/// **High-precision (MPFR) character `χ_λ(β)`.**
///
/// Computes the Hoefsmit seminormal character at `dps` decimal-precision
/// using MPFR-backed arbitrary-precision arithmetic. Returns the result
/// as a decimal string (callers should parse via `mpmath.mpf` or
/// equivalent). Substantially slower than the `f64` path (~10–30×) but
/// exact at the requested precision — no f64 rounding error.
///
/// `q_str`: substrate parameter as a decimal string (avoids f64 lossy
///   conversion at the boundary).
/// `dps`: requested decimal precision (default 50 if caller passes a
///   smaller value, MPFR uses internal guard bits).
#[pyfunction]
#[pyo3(signature = (shape, word, q_str, dps=50))]
fn chi_lambda_braid_mpfr(
    shape: Vec<usize>,
    word: Vec<(i32, u32)>,
    q_str: String,
    dps: u32,
) -> String {
    seminormal_mpfr::chi_lambda_braid_mpfr(&shape, &word, &q_str, dps)
}

#[pymodule]
fn pyhecke_native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(markov_z, m)?)?;
    m.add_function(wrap_pyfunction!(hecke_h, m)?)?;
    m.add_function(wrap_pyfunction!(trace_weights, m)?)?;
    m.add_function(wrap_pyfunction!(gram_matrix, m)?)?;
    m.add_function(wrap_pyfunction!(gram_determinant, m)?)?;
    m.add_function(wrap_pyfunction!(gram_inverse, m)?)?;
    m.add_function(wrap_pyfunction!(hm, m)?)?;
    m.add_function(wrap_pyfunction!(nf_tr, m)?)?;
    m.add_function(wrap_pyfunction!(nf_net, m)?)?;
    m.add_function(wrap_pyfunction!(build_atom_nf, m)?)?;
    m.add_function(wrap_pyfunction!(atom_per_generator_volumes, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambda_braid, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambdas_braid, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambda_braid_mpfr, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambdas_braid_mpfr, m)?)?;
    m.add_function(wrap_pyfunction!(partitions_of, m)?)?;
    m.add_function(wrap_pyfunction!(mn_chi, m)?)?;
    m.add_function(wrap_pyfunction!(mn_chi_q, m)?)?;
    m.add_function(wrap_pyfunction!(chi_q_word, m)?)?;
    // Pull __version__ directly from Cargo.toml so the Python module,
    // the Rust crate, and pyproject.toml never drift. (Gemini review
    // r3103025537: hardcoded version is fragile.)
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}
