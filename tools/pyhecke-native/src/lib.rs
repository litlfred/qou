//! PyO3 native acceleration layer for `pyhecke`.
//!
//! Re-exposes the hottest hecke-engine kernels as a Python extension
//! module `pyhecke_native`. No NumPy dependency — returns nested
//! Python lists that `pyhecke.bridge` converts on demand. This keeps
//! the wheel small and the build simple.

use hecke_engine::gram;
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

/// Gram determinant.
#[pyfunction]
fn gram_determinant(q: f64) -> f64 {
    let m = gram::gram_matrix(q);
    // Inline LU-style determinant (mirrors det_6x6 in hecke_engine::gram).
    let mut a = m;
    let mut det = 1.0f64;
    for i in 0..6 {
        let mut best = i;
        for r in i + 1..6 {
            if a[r][i].abs() > a[best][i].abs() {
                best = r;
            }
        }
        if a[best][i].abs() < 1e-15 {
            return 0.0;
        }
        if best != i {
            a.swap(i, best);
            det = -det;
        }
        det *= a[i][i];
        let pivot = a[i][i];
        for j in i..6 {
            a[i][j] /= pivot;
        }
        for r in i + 1..6 {
            let factor = a[r][i];
            if factor == 0.0 {
                continue;
            }
            for j in i..6 {
                a[r][j] -= factor * a[i][j];
            }
        }
    }
    det
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
    m.add("__version__", "0.2.0")?;
    Ok(())
}
