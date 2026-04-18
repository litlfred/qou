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

#[pymodule]
fn pyhecke_native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(markov_z, m)?)?;
    m.add_function(wrap_pyfunction!(hecke_h, m)?)?;
    m.add_function(wrap_pyfunction!(trace_weights, m)?)?;
    m.add_function(wrap_pyfunction!(gram_matrix, m)?)?;
    m.add_function(wrap_pyfunction!(gram_determinant, m)?)?;
    m.add_function(wrap_pyfunction!(gram_inverse, m)?)?;
    m.add("__version__", "0.1.0")?;
    Ok(())
}
