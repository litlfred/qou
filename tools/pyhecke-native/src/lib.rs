//! PyO3 native acceleration layer for `pyhecke`.
//!
//! Re-exposes the hottest hecke-engine kernels as a Python extension
//! module `pyhecke_native`. No NumPy dependency — returns nested
//! Python lists that `pyhecke.bridge` converts on demand. This keeps
//! the wheel small and the build simple.

use hecke_engine::{atom, gram, nf};
use pyo3::prelude::*;
use pyo3::types::PyList;

/// Markov parameter z = 1 / (q^{1/2} + q^{-1/2}).
#[pyfunction]
fn markov_z(q: f64) -> f64 {
    nf::markov_z(q)
}

/// Hecke relation coefficient h = q - q^{-1}.
#[pyfunction]
fn hecke_h(q: f64) -> f64 {
    nf::hecke_h(q)
}

/// Markov-trace weights on the NF basis as a length-6 list.
#[pyfunction]
fn trace_weights(q: f64) -> Vec<f64> {
    nf::trace_weights(q).to_vec()
}

/// Gram matrix G_ij = tr_M(b_i · b_j) as a 6x6 list of lists.
#[pyfunction]
fn gram_matrix<'py>(py: Python<'py>, q: f64) -> PyResult<Bound<'py, PyList>> {
    let g = gram::gram_matrix(q);
    let outer = PyList::empty(py);
    for row in g.iter() {
        outer.append(PyList::new(py, row)?)?;
    }
    Ok(outer)
}

/// Gram determinant — delegates to shared `hecke_engine::gram::det_6x6`.
#[pyfunction]
fn gram_determinant(q: f64) -> f64 {
    gram::det_6x6(&gram::gram_matrix(q))
}

/// Gram inverse as a 6x6 list of lists.
#[pyfunction]
fn gram_inverse<'py>(py: Python<'py>, q: f64) -> PyResult<Bound<'py, PyList>> {
    let inv = gram::gram_inverse(q);
    let outer = PyList::empty(py);
    for row in inv.iter() {
        outer.append(PyList::new(py, row)?)?;
    }
    Ok(outer)
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
    let h_val = h.unwrap_or_else(|| nf::hecke_h(nf::Q_0));
    Ok(atom::hm(&arr, c, d, gen, h_val).to_vec())
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
    Ok(atom::nf_tr(&arr, q.unwrap_or(nf::Q_0)))
}

/// Sum of NF coefficients.
#[pyfunction]
fn nf_net(nf: Vec<f64>) -> PyResult<f64> {
    Ok(nf.iter().sum())
}

/// Batched NF multiplication — apply a sequence of `(c, d, gen)` ops
/// in one Rust call.
///
/// Equivalent to repeated `hm` in a Python loop, but without the
/// per-iteration Python↔Rust marshal. For callers that need to run
/// many NF multiplications that aren't covered by `build_atom_nf`,
/// this variant is 10-50× faster than looping `hm` from Python
/// (depending on chain length). `h` defaults to `hecke_h(Q_0)`.
#[pyfunction]
#[pyo3(signature = (nf, ops, h=None))]
fn hm_seq(nf: Vec<f64>, ops: Vec<(f64, f64, u8)>, h: Option<f64>) -> PyResult<Vec<f64>> {
    if nf.len() != 6 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            format!("nf must have exactly 6 elements, got {}", nf.len()),
        ));
    }
    let mut arr: [f64; 6] = [nf[0], nf[1], nf[2], nf[3], nf[4], nf[5]];
    let h_val = h.unwrap_or_else(|| nf::hecke_h(nf::Q_0));
    for (c, d, gen) in ops {
        arr = atom::hm(&arr, c, d, gen, h_val);
    }
    Ok(arr.to_vec())
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
    let h_val = h.unwrap_or_else(|| nf::hecke_h(nf::Q_0));
    atom::build_atom_nf(z, n, h_val).to_vec()
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
    let q_val = q.unwrap_or(nf::Q_0);
    let vols = atom::atom_per_generator_volumes(
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

#[pymodule]
fn pyhecke_native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(markov_z, m)?)?;
    m.add_function(wrap_pyfunction!(hecke_h, m)?)?;
    m.add_function(wrap_pyfunction!(trace_weights, m)?)?;
    m.add_function(wrap_pyfunction!(gram_matrix, m)?)?;
    m.add_function(wrap_pyfunction!(gram_determinant, m)?)?;
    m.add_function(wrap_pyfunction!(gram_inverse, m)?)?;
    m.add_function(wrap_pyfunction!(hm, m)?)?;
    m.add_function(wrap_pyfunction!(hm_seq, m)?)?;
    m.add_function(wrap_pyfunction!(nf_tr, m)?)?;
    m.add_function(wrap_pyfunction!(nf_net, m)?)?;
    m.add_function(wrap_pyfunction!(build_atom_nf, m)?)?;
    m.add_function(wrap_pyfunction!(atom_per_generator_volumes, m)?)?;
    // Pull __version__ directly from Cargo.toml so the Python module,
    // the Rust crate, and pyproject.toml never drift. (Gemini review
    // r3103025537: hardcoded version is fragile.)
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}
