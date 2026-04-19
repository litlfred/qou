//! 6×6 Gram matrix on the NF basis of H_3(q).
//!
//! Thin layer on top of the [`crate::nf`] GB-NF kernel: computes
//! `G_{ij} = tr_M(b_i · b_j)` for the 6-element NF basis via
//! `mul_polys` + `reduce_nf`, then exposes inverse / determinant and
//! a JSON certificate matching `pyhecke.certificate`.
//!
//! Mirrors `pyhecke.gram` (see `tools/pyhecke/python/pyhecke/gram.py`).
//! Numerical output is byte-identical to the Python implementation
//! to within f64 rounding (< 1e-14 per entry).
//!
//! Public API:
//!
//! * [`gram_matrix`] — 6×6 Gram at an arbitrary `q > 1`.
//! * [`gram_inverse`] — 6×6 inverse at an arbitrary `q > 1`.
//! * [`det_6x6`] — determinant used by the certificate.
//! * [`GramCertificate`] — serde-serializable record.
//! * CLI entry via `cargo run --bin hecke-gram`.

use serde::{Deserialize, Serialize};

use crate::nf::{
    hecke_h, markov_z, mul_polys, poly_from, reduce_nf, trace_weights, NF_BASIS, NF_NAMES,
};

/// Compute the 6×6 Gram matrix on the NF basis at a given `q`.
///
/// `G[i, j] = tr_M(b_i · b_j)` where `b_k = NF_BASIS[k]` and
/// `tr_M` is the Markov trace extended linearly.
pub fn gram_matrix(q: f64) -> [[f64; 6]; 6] {
    let h = hecke_h(q);
    let tr_m = trace_weights(q);
    let mut g = [[0.0f64; 6]; 6];
    for i in 0..6 {
        for j in 0..6 {
            let prod = mul_polys(&poly_from(i), &poly_from(j));
            let nf = reduce_nf(prod, h);
            let mut acc = 0.0;
            for (k, basis_word) in NF_BASIS.iter().enumerate() {
                if let Some(c) = nf.get(*basis_word) {
                    acc += c * tr_m[k];
                }
            }
            g[i][j] = acc;
        }
    }
    g
}

/// Inverse of the Gram matrix (via Gauss-Jordan on f64).
pub fn gram_inverse(q: f64) -> [[f64; 6]; 6] {
    let g = gram_matrix(q);
    invert_6x6(&g).expect("Gram matrix is singular — check q value")
}

/// Partial pivoting + singularity detection shared by [`invert_6x6`]
/// and [`det_6x6`]. Returns the largest-magnitude row index `≥ i` in
/// column `i`, or `None` if the pivot is effectively zero.
fn _partial_pivot_row<const W: usize>(m: &[[f64; W]; 6], i: usize) -> Option<usize> {
    let mut best = i;
    for r in i + 1..6 {
        if m[r][i].abs() > m[best][i].abs() {
            best = r;
        }
    }
    if m[best][i].abs() < 1e-15 {
        None
    } else {
        Some(best)
    }
}

fn invert_6x6(a: &[[f64; 6]; 6]) -> Option<[[f64; 6]; 6]> {
    // Augmented matrix [A | I].
    let mut m = [[0.0f64; 12]; 6];
    for i in 0..6 {
        for j in 0..6 {
            m[i][j] = a[i][j];
        }
        m[i][6 + i] = 1.0;
    }
    for i in 0..6 {
        let best = _partial_pivot_row(&m, i)?;
        m.swap(i, best);
        let pivot = m[i][i];
        for j in 0..12 {
            m[i][j] /= pivot;
        }
        // Full Gauss-Jordan: zero ABOVE and BELOW pivot.
        for r in 0..6 {
            if r == i {
                continue;
            }
            let factor = m[r][i];
            if factor == 0.0 {
                continue;
            }
            for j in 0..12 {
                m[r][j] -= factor * m[i][j];
            }
        }
    }
    let mut inv = [[0.0f64; 6]; 6];
    for i in 0..6 {
        for j in 0..6 {
            inv[i][j] = m[i][6 + j];
        }
    }
    Some(inv)
}

pub fn det_6x6(a: &[[f64; 6]; 6]) -> f64 {
    let mut m = *a;
    let mut det = 1.0f64;
    for i in 0..6 {
        let best = match _partial_pivot_row(&m, i) {
            Some(r) => r,
            None => return 0.0,
        };
        if best != i {
            m.swap(i, best);
            det = -det;
        }
        det *= m[i][i];
        let pivot = m[i][i];
        for j in i..6 {
            m[i][j] /= pivot;
        }
        // Forward-only elimination: zero BELOW pivot (upper-triangular
        // target). Differs from `invert_6x6`'s full Gauss-Jordan, which
        // also zeroes above pivot — but they share `_partial_pivot_row`.
        for r in i + 1..6 {
            let factor = m[r][i];
            if factor == 0.0 {
                continue;
            }
            for j in i..6 {
                m[r][j] -= factor * m[i][j];
            }
        }
    }
    det
}

/// JSON-serializable record of a Gram-matrix computation.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GramCertificate {
    pub q: f64,
    pub z: f64,
    pub h: f64,
    pub n: u32,
    pub basis: Vec<String>,
    pub trace_weights: Vec<f64>,
    pub matrix: Vec<Vec<f64>>,
    pub inverse: Vec<Vec<f64>>,
    pub determinant: f64,
}

pub fn certificate_at(q: f64) -> GramCertificate {
    let g = gram_matrix(q);
    let inv = gram_inverse(q);
    GramCertificate {
        q,
        z: markov_z(q),
        h: hecke_h(q),
        n: 3,
        basis: NF_NAMES.iter().map(|s| s.to_string()).collect(),
        trace_weights: trace_weights(q).to_vec(),
        matrix: g.iter().map(|r| r.to_vec()).collect(),
        inverse: inv.iter().map(|r| r.to_vec()).collect(),
        determinant: det_6x6(&g),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::nf::Q_0;

    #[test]
    fn gram_diagonal_g00_is_one() {
        let g = gram_matrix(Q_0);
        assert!((g[0][0] - 1.0).abs() < 1e-14);
    }

    #[test]
    fn gram_inverse_is_right_inverse() {
        let q = Q_0;
        let g = gram_matrix(q);
        let inv = gram_inverse(q);
        for i in 0..6 {
            for j in 0..6 {
                let mut s = 0.0;
                for k in 0..6 {
                    s += g[i][k] * inv[k][j];
                }
                let target = if i == j { 1.0 } else { 0.0 };
                assert!((s - target).abs() < 1e-10, "i={},j={}: {} != {}", i, j, s, target);
            }
        }
    }

    #[test]
    fn det_at_q0_matches_python() {
        let g = gram_matrix(Q_0);
        let d = det_6x6(&g);
        assert!((d - (-0.3608011166161873)).abs() < 1e-10, "det = {}", d);
    }

    #[test]
    fn gram_first_row_matches_trace_weights() {
        let g = gram_matrix(Q_0);
        let tr = trace_weights(Q_0);
        for j in 0..6 {
            assert!(
                (g[0][j] - tr[j]).abs() < 1e-14,
                "G[0][{}] = {} vs TR_M[{}] = {}", j, g[0][j], j, tr[j]
            );
        }
    }
}
