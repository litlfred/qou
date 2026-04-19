//! Hecke normal-form (Gröbner-basis NF) core for H_3(q).
//!
//! The Hecke algebra H_3(q) has the presentation
//! `⟨σ_0, σ_1 | σ_i² = h σ_i + 1, σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1⟩` with
//! `h = q − q⁻¹`. Its 6-dimensional NF basis is
//! `1, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0`.
//!
//! This module contains the word-rewriting kernel: [`reduce_nf`] and
//! [`mul_polys`] drive the two rewrite rules (quadratic relation and
//! braid canonicalization) to a normal form on the NF basis. These
//! are the hottest loops in the engine and are allocation-tuned —
//! words live inline in a `SmallVec<[u8; 8]>` (H_3 intermediates are
//! ≤6 bytes) and the new-terms hash buffer is swapped (rather than
//! freshly allocated) across loop iterations.

use smallvec::SmallVec;

/// NF basis of H_3(q): `1, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0`.
pub const NF_BASIS: [&[u8]; 6] = [
    &[],
    &[0],
    &[1],
    &[0, 1],
    &[1, 0],
    &[0, 1, 0],
];

/// Readable names for each NF basis element, used by the JSON
/// certificate.
pub const NF_NAMES: [&str; 6] = [
    "gamma", "sigma_0", "sigma_1", "L_plus", "L_minus", "e_minus",
];

/// Default substrate parameter `q₀` (matches `q_parameter.py`).
pub const Q_0: f64 = 1.1099785955541805;

/// Markov-closure parameter `z = 1 / (q^{1/2} + q^{-1/2})`.
#[inline]
pub fn markov_z(q: f64) -> f64 {
    1.0 / (q.sqrt() + (1.0 / q).sqrt())
}

/// Hecke relation coefficient `h = q − q⁻¹`.
#[inline]
pub fn hecke_h(q: f64) -> f64 {
    q - 1.0 / q
}

/// Markov-trace weights on the 6-element NF basis.
pub fn trace_weights(q: f64) -> [f64; 6] {
    let z = markov_z(q);
    [1.0, z, z, z * z, z * z, z * z * z]
}

/// A word in the generators `{σ_0, σ_1}`. Stored as a `SmallVec` with
/// 8 bytes of inline capacity, so H_3(q) words never touch the heap.
pub type Word = SmallVec<[u8; 8]>;

/// Polynomial in the free algebra: a sparse map from words to f64
/// coefficients, hashed with the fast `rustc_hash::FxHashMap`.
pub type Poly = rustc_hash::FxHashMap<Word, f64>;

/// Build a `Word` from a byte slice.
pub fn word_key(w: &[u8]) -> Word {
    SmallVec::from_slice(w)
}

/// Return the unit polynomial concentrated on `NF_BASIS[basis_idx]`.
pub fn poly_from(basis_idx: usize) -> Poly {
    let mut p: Poly = Default::default();
    p.insert(word_key(NF_BASIS[basis_idx]), 1.0);
    p
}

/// Multiply two polynomial representations (concatenate letters).
pub fn mul_polys(a: &Poly, b: &Poly) -> Poly {
    let mut r: Poly = Default::default();
    let mut w: Word = SmallVec::new();
    for (w1, c1) in a {
        for (w2, c2) in b {
            w.clear();
            w.extend_from_slice(w1);
            w.extend_from_slice(w2);
            let c = c1 * c2;
            r.entry(w.clone()).and_modify(|v| *v += c).or_insert(c);
        }
    }
    r.retain(|_, v| v.abs() > 1e-15);
    r
}

/// Apply Hecke reductions until the polynomial is in NF.
///
/// Two rules:
///   `σ_i σ_i → h σ_i + 1`
///   `σ_0 σ_1 σ_0 ↔ σ_1 σ_0 σ_1`      (braid relation; canonical form)
///
/// Buffer reuse: `new_terms` is swapped with `terms` each iteration
/// via `std::mem::swap`, keeping the hash-table allocation alive and
/// avoiding a fresh `Default::default()` per iteration.
pub fn reduce_nf(mut terms: Poly, h: f64) -> Poly {
    let mut new_terms: Poly = Default::default();
    let mut scratch: Word = SmallVec::new();
    loop {
        new_terms.clear();
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
                    // w1 = pre · σ_i · suf (keeps the letter)
                    scratch.clear();
                    scratch.extend_from_slice(pre);
                    scratch.push(word[p]);
                    scratch.extend_from_slice(suf);
                    let c1 = coeff * h;
                    new_terms.entry(scratch.clone())
                        .and_modify(|v| *v += c1).or_insert(c1);
                    // w2 = pre · suf (drops both copies)
                    scratch.clear();
                    scratch.extend_from_slice(pre);
                    scratch.extend_from_slice(suf);
                    let c2 = *coeff;
                    new_terms.entry(scratch.clone())
                        .and_modify(|v| *v += c2).or_insert(c2);
                    changed = true;
                    done = true;
                    break;
                }
            }
            if done {
                continue;
            }

            // Rule 2: braid-commute to canonical form.
            // σ_a σ_b σ_a (a ≠ b) → σ_b σ_a σ_b iff (b, a, b) < (a, b, a)
            for p in 0..word.len().saturating_sub(2) {
                let a = word[p];
                let b = word[p + 1];
                let c = word[p + 2];
                if a == c && a.abs_diff(b) == 1 {
                    let candidate = [b, a, b];
                    let original = [a, b, a];
                    if candidate < original {
                        scratch.clear();
                        scratch.extend_from_slice(&word[..p]);
                        scratch.extend_from_slice(&candidate);
                        scratch.extend_from_slice(&word[p + 3..]);
                        let c_val = *coeff;
                        new_terms.entry(scratch.clone())
                            .and_modify(|v| *v += c_val).or_insert(c_val);
                        changed = true;
                        done = true;
                        break;
                    }
                }
            }
            if !done {
                let c_val = *coeff;
                new_terms.entry(word.clone())
                    .and_modify(|v| *v += c_val).or_insert(c_val);
            }
        }
        new_terms.retain(|_, v| v.abs() > 1e-15);
        std::mem::swap(&mut terms, &mut new_terms);
        if !changed {
            break;
        }
    }
    terms
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn z_at_q0_matches_python() {
        let z = markov_z(Q_0);
        assert!((z - 0.4993203340335982).abs() < 1e-14, "z = {}", z);
    }

    #[test]
    fn h_at_q0() {
        let h = hecke_h(Q_0);
        let expected = Q_0 - 1.0 / Q_0;
        assert!((h - expected).abs() < 1e-15);
    }
}
