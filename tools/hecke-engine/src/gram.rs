//! Gram matrix on the NF basis of H_3(q) — Rust implementation.
//!
//! Mirrors `pyhecke.gram` (see
//! `tools/pyhecke/python/pyhecke/gram.py`). Same NF basis, same
//! Markov-trace weights, same Hecke reduction rules — numerical
//! output is byte-identical to the Python implementation to within
//! f64 rounding (< 1e-14 per entry).
//!
//! Public API:
//!
//! * [`gram_matrix`] — 6×6 Gram at an arbitrary `q > 1`.
//! * [`gram_inverse`] — 6×6 inverse at an arbitrary `q > 1`.
//! * [`GramCertificate`] — serde-serializable record matching the
//!   JSON shape used by `pyhecke.certificate`.
//! * CLI entry via `cargo run --bin hecke-gram`.

use serde::{Deserialize, Serialize};

/// NF basis of H_3(q): 1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀.
pub const NF_BASIS: [&[u8]; 6] = [
    &[],
    &[0],
    &[1],
    &[0, 1],
    &[1, 0],
    &[0, 1, 0],
];

pub const NF_NAMES: [&str; 6] = ["gamma", "sigma_0", "sigma_1", "L_plus", "L_minus", "e_minus"];

/// Default substrate parameter q_0 (matches `q_parameter.py`).
pub const Q_0: f64 = 1.1099785955541805;

/// z = 1 / (q^{1/2} + q^{-1/2}) — Markov closure parameter.
#[inline]
pub fn markov_z(q: f64) -> f64 {
    1.0 / (q.sqrt() + (1.0 / q).sqrt())
}

/// h = q - q^{-1} — the Hecke relation coefficient.
#[inline]
pub fn hecke_h(q: f64) -> f64 {
    q - 1.0 / q
}

/// Markov-trace weights on the 6-element NF basis.
pub fn trace_weights(q: f64) -> [f64; 6] {
    let z = markov_z(q);
    [1.0, z, z, z * z, z * z, z * z * z]
}

// ─── Word representation + Hecke reduction ───────────────────────────

type Word = Vec<u8>;
type Poly = rustc_hash::FxHashMap<Word, f64>;

fn word_key(w: &[u8]) -> Word {
    w.to_vec()
}

fn poly_from(basis_idx: usize) -> Poly {
    let mut p: Poly = Default::default();
    p.insert(word_key(NF_BASIS[basis_idx]), 1.0);
    p
}

/// Multiply two polynomial representations (concatenate letters).
fn mul_polys(a: &Poly, b: &Poly) -> Poly {
    let mut r: Poly = Default::default();
    for (w1, c1) in a {
        for (w2, c2) in b {
            let mut w = w1.clone();
            w.extend_from_slice(w2);
            *r.entry(w).or_insert(0.0) += c1 * c2;
        }
    }
    r.retain(|_, v| v.abs() > 1e-15);
    r
}

/// Apply Hecke reductions until the polynomial is in NF.
///
/// Two rules:
///   σ_i σ_i  →  h σ_i + 1
///   σ_0 σ_1 σ_0  ↔  σ_1 σ_0 σ_1      (braid relation, canonical form)
///
/// The canonical form we keep matches the Python NF_BASIS, so any word
/// whose reduction lands on that basis stabilises after finitely many
/// rewrites.
fn reduce_nf(mut terms: Poly, h: f64) -> Poly {
    loop {
        let mut new_terms: Poly = Default::default();
        let mut changed = false;
        for (word, coeff) in &terms {
            if coeff.abs() < 1e-15 {
                continue;
            }
            let mut done = false;

            // Rule 1: σ_i σ_i = h σ_i + 1
            for p in 0..word.len().saturating_sub(1) {
                if word[p] == word[p + 1] {
                    let pre = &word[..p];
                    let suf = &word[p + 2..];
                    let mut w1: Word = pre.to_vec();
                    w1.push(word[p]);
                    w1.extend_from_slice(suf);
                    *new_terms.entry(w1).or_insert(0.0) += coeff * h;
                    let mut w2: Word = pre.to_vec();
                    w2.extend_from_slice(suf);
                    *new_terms.entry(w2).or_insert(0.0) += coeff;
                    changed = true;
                    done = true;
                    break;
                }
            }
            if done {
                continue;
            }

            // Rule 2: braid-commute to canonical form.
            // σ_a σ_b σ_a (a != b) → σ_b σ_a σ_b iff (b, a, b) < (a, b, a)
            for p in 0..word.len().saturating_sub(2) {
                let a = word[p];
                let b = word[p + 1];
                let c = word[p + 2];
                if a == c && a.abs_diff(b) == 1 {
                    let candidate = [b, a, b];
                    let original = [a, b, a];
                    if candidate < original {
                        let mut nw: Word = word[..p].to_vec();
                        nw.extend_from_slice(&candidate);
                        nw.extend_from_slice(&word[p + 3..]);
                        *new_terms.entry(nw).or_insert(0.0) += coeff;
                        changed = true;
                        done = true;
                        break;
                    }
                }
            }
            if !done {
                *new_terms.entry(word.clone()).or_insert(0.0) += coeff;
            }
        }
        new_terms.retain(|_, v| v.abs() > 1e-15);
        terms = new_terms;
        if !changed {
            break;
        }
    }
    terms
}

// ─── Gram matrix ─────────────────────────────────────────────────────

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
        // Partial pivot
        let mut best = i;
        for r in i + 1..6 {
            if m[r][i].abs() > m[best][i].abs() {
                best = r;
            }
        }
        if m[best][i].abs() < 1e-15 {
            return None;
        }
        m.swap(i, best);
        let pivot = m[i][i];
        for j in 0..12 {
            m[i][j] /= pivot;
        }
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

// ─── NF multiplication kernel ────────────────────────────────────────

/// Multiply an NF element by `(c · σ_gen + d · 1)`.
///
/// Mirrors `pyhecke.gram.hm` (which closes over `h = q - q^{-1}`).
/// The `gen` argument must be 0 or 1.
///
/// `nf[0..6]` is the NF basis coefficient vector `[γ, σ₀, σ₁, L₊, L₋, e⁻]`.
pub fn hm(nf: &[f64; 6], c: f64, d: f64, gen: u8, h: f64) -> [f64; 6] {
    let mut r = [0.0f64; 6];
    let tables: [(usize, &[(usize, f64)]); 6] = if gen == 0 {
        [
            (0, &[(1, c), (0, d)]),
            (1, &[(1, c * h), (0, c), (1, d)]),
            (2, &[(3, c), (2, d)]),
            (3, &[(3, c * h), (2, c), (3, d)]),
            (4, &[(5, c), (4, d)]),
            (5, &[(5, c * h), (4, c), (5, d)]),
        ]
    } else {
        [
            (0, &[(2, c), (0, d)]),
            (1, &[(4, c), (1, d)]),
            (2, &[(2, c * h), (0, c), (2, d)]),
            (3, &[(5, c), (3, d)]),
            (4, &[(4, c * h), (1, c), (4, d)]),
            (5, &[(5, c * h), (3, c), (5, d)]),
        ]
    };
    for (si, tgts) in tables.iter() {
        if nf[*si].abs() < 1e-15 {
            continue;
        }
        for (ti, co) in tgts.iter() {
            r[*ti] += nf[*si] * co;
        }
    }
    r
}

/// Markov trace of an NF vector at a given `q`.
pub fn nf_tr(nf: &[f64; 6], q: f64) -> f64 {
    let tr = trace_weights(q);
    (0..6).map(|i| nf[i] * tr[i]).sum()
}

/// Sum of NF coefficients (the net, or augmentation, of the element).
pub fn nf_net(nf: &[f64; 6]) -> f64 {
    nf.iter().sum()
}

/// Build the atom NF for (Z, N) via Hecke multiplication.
///
/// Mirrors `hecke_core.build_atom_nf` byte-for-byte. Construction:
///
/// 1. Build each nucleon via B_3 confinement + quark crossings +
///    gluon self-coupling.
/// 2. Compose in ground-state interleaved order (p, n, p, n, …).
/// 3. Apply inter-nucleon crossings between each pair:
///    pp = σ₀, nn = σ₀⁻¹, pn = ½(σ₀ + σ₀⁻¹).
/// 4. Apply pe crossings for Z electrons (σ₁⁻¹).
///
/// `h` is `hecke_h(q)` for the target q; pass `hecke_h(Q_0)` to match
/// the Python default.
pub fn build_atom_nf(z_count: u32, n_count: u32, h: f64) -> [f64; 6] {
    let a = z_count + n_count;
    if a == 0 {
        return [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    }

    // Ground-state interleaved ordering.
    let mut ordering: Vec<u8> = Vec::with_capacity(a as usize);
    let (mut pc, mut nc) = (0u32, 0u32);
    for k in 0..a {
        if (k % 2 == 0 && pc < z_count) || nc >= n_count {
            ordering.push(b'p');
            pc += 1;
        } else {
            ordering.push(b'n');
            nc += 1;
        }
    }

    let mut nf = [1.0f64, 0.0, 0.0, 0.0, 0.0, 0.0];
    let half_h = 0.5 * h;

    for k in 0..a as usize {
        // B_3 confinement: 3x (σ₀ σ₁⁻¹)
        for _ in 0..3 {
            nf = hm(&nf, 1.0, 0.0, 0, h);
            nf = hm(&nf, 1.0, -h, 1, h);
        }

        if ordering[k] == b'p' {
            // Proton: uud
            nf = hm(&nf, 1.0, 0.0, 0, h);        // (0,1) uu → σ₀
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,2) ud → mixed
            nf = hm(&nf, 1.0, -half_h, 1, h);    // (1,2) ud → mixed (gen 1)
        } else {
            // Neutron: udd
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,1) ud → mixed
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,2) ud → mixed
            nf = hm(&nf, 1.0, -h, 1, h);         // (1,2) dd → σ₁⁻¹
        }

        // Gluon self-coupling: 2 × σ₀
        nf = hm(&nf, 1.0, 0.0, 0, h);
        nf = hm(&nf, 1.0, 0.0, 0, h);

        // Inter-nucleon crossings with all previous nucleons
        for prev in 0..k {
            let (ti, tj) = (ordering[prev], ordering[k]);
            if ti == b'p' && tj == b'p' {
                nf = hm(&nf, 1.0, 0.0, 0, h);         // pp: σ₀
            } else if ti == b'n' && tj == b'n' {
                nf = hm(&nf, 1.0, -h, 0, h);          // nn: σ₀⁻¹
            } else {
                nf = hm(&nf, 1.0, -half_h, 0, h);     // pn/np: mixed
            }
        }
    }

    // Electrons: pe crossing (EM channel, gen=1)
    for _ in 0..z_count {
        nf = hm(&nf, 1.0, -h, 1, h);
    }

    nf
}

// ─── Serialization ───────────────────────────────────────────────────

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

fn det_6x6(a: &[[f64; 6]; 6]) -> f64 {
    let mut m = *a;
    let mut det = 1.0f64;
    for i in 0..6 {
        let mut best = i;
        for r in i + 1..6 {
            if m[r][i].abs() > m[best][i].abs() {
                best = r;
            }
        }
        if m[best][i].abs() < 1e-15 {
            return 0.0;
        }
        if best != i {
            m.swap(i, best);
            det = -det;
        }
        det *= m[i][i];
        let pivot = m[i][i];
        for j in i..6 {
            m[i][j] /= pivot;
        }
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn z_at_q0_matches_python() {
        // pyhecke.gram.z at q_0 = 1.1099785955541805
        let z = markov_z(Q_0);
        assert!((z - 0.4993203340335982).abs() < 1e-14, "z = {}", z);
    }

    #[test]
    fn h_at_q0() {
        let h = hecke_h(Q_0);
        // q - 1/q at q_0
        let expected = Q_0 - 1.0 / Q_0;
        assert!((h - expected).abs() < 1e-15);
    }

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
        // g * inv = I
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
        // pyhecke Gram det at q_0 = -0.3608011166161873
        let g = gram_matrix(Q_0);
        let d = det_6x6(&g);
        assert!((d - (-0.3608011166161873)).abs() < 1e-10, "det = {}", d);
    }

    #[test]
    fn gram_first_row_matches_trace_weights() {
        // G[0, j] = tr_M(1 · b_j) = tr_M(b_j) = TR_M[j]
        let g = gram_matrix(Q_0);
        let tr = trace_weights(Q_0);
        for j in 0..6 {
            assert!(
                (g[0][j] - tr[j]).abs() < 1e-14,
                "G[0][{}] = {} vs TR_M[{}] = {}",
                j, g[0][j], j, tr[j]
            );
        }
    }

    #[test]
    fn hm_identity_on_gamma() {
        // hm(γ, 1, 0, 0) should give σ_0 (basis index 1)
        let nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        let out = hm(&nf, 1.0, 0.0, 0, hecke_h(Q_0));
        assert!((out[1] - 1.0).abs() < 1e-12);
        for i in [0, 2, 3, 4, 5] {
            assert!(out[i].abs() < 1e-12);
        }
    }

    #[test]
    fn nf_tr_of_gamma_is_one() {
        let nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        assert!((nf_tr(&nf, Q_0) - 1.0).abs() < 1e-14);
    }

    #[test]
    fn nf_net_sum() {
        let nf = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0];
        assert!((nf_net(&nf) - 21.0).abs() < 1e-14);
    }

    #[test]
    fn build_atom_nf_hydrogen() {
        // H (Z=1, N=0): one nucleon (proton) + one electron
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(1, 0, h);
        // Must be a finite length-6 result
        assert!(nf.iter().all(|x| x.is_finite()));
        // Non-trivial: at least one coordinate should be non-zero
        assert!(nf.iter().any(|x| x.abs() > 1e-10));
    }

    #[test]
    fn build_atom_nf_vacuum() {
        // (0, 0) → identity NF
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(0, 0, h);
        assert!((nf[0] - 1.0).abs() < 1e-14);
        for i in 1..6 {
            assert!(nf[i].abs() < 1e-14);
        }
    }
}
