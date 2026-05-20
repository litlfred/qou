//! Hecke element with `LaurentRationalQ` coefficients.
//!
//! Port of `folio-assistant/computations/hecke_laurent_fast.py::
//! LaurentHeckeElement`. Sparse `BTreeMap<Word, LaurentRationalQ>`
//! where `Word = Vec<i32>` is a sequence of signed Hecke-generator
//! indices.
//!
//! **Sign convention** (matches Python source, hecke_laurent_fast.py
//! line 168-174):
//!   - non-negative gen index `i ≥ 0` → Hecke generator `σ_i`
//!   - negative gen index `i < 0`   → formal variable that commutes
//!     with every other letter (used for marker/placeholder slots
//!     in the markov_peel staging; treated as a scalar by R1).
//!
//! `BTreeMap` is used (not `HashMap`) so iteration order is stable
//! across runs and reproducible bit-for-bit serialisation.

use crate::laurent_rational_q::LaurentRationalQ;
use std::collections::BTreeMap;

/// A word in the Hecke generators: each `i32` is a signed gen index
/// per the convention above. Empty word is the identity.
pub type Word = Vec<i32>;

/// Sparse Hecke element: `Σ_w c_w · w` with `c_w : LaurentRationalQ`.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub struct LaurentHeckeElement {
    pub terms: BTreeMap<Word, LaurentRationalQ>,
}

impl LaurentHeckeElement {
    /// The zero element (empty term map).
    pub fn zero() -> Self {
        Self { terms: BTreeMap::new() }
    }

    /// The identity element (single empty-word term with coefficient 1).
    pub fn identity() -> Self {
        let mut terms = BTreeMap::new();
        terms.insert(Vec::new(), LaurentRationalQ::one());
        Self { terms }
    }

    /// Single-term constructor `c · word`. Drops zero coefficients.
    pub fn monomial(word: Word, c: LaurentRationalQ) -> Self {
        if c.is_zero() {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        terms.insert(word, c);
        Self { terms }
    }

    /// Number of distinct non-zero word terms.
    pub fn n_terms(&self) -> usize {
        self.terms.len()
    }

    /// True iff every term has zero coefficient.
    pub fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    /// In-place accumulate: `self += c · word`. Drops the entry if the
    /// resulting coefficient is zero (this is the hot inner accumulator
    /// used by both `mul` and the reduce loop).
    pub fn accumulate(&mut self, word: Word, c: LaurentRationalQ) {
        if c.is_zero() {
            return;
        }
        use std::collections::btree_map::Entry;
        match self.terms.entry(word) {
            Entry::Occupied(mut o) => {
                *o.get_mut() += &c;
                if o.get().is_zero() {
                    o.remove();
                }
            }
            Entry::Vacant(v) => {
                v.insert(c);
            }
        }
    }

    /// Add two elements (term-wise sum with cancellation).
    pub fn add(&self, other: &Self) -> Self {
        let mut out = self.clone();
        for (w, c) in &other.terms {
            out.accumulate(w.clone(), c.clone());
        }
        out
    }

    /// Multiply: `(Σ_v a_v · v) · (Σ_w b_w · w) = Σ_{v,w} a_v · b_w · (v ++ w)`.
    ///
    /// Matches `LaurentHeckeElement.__mul__` in the Python reference
    /// (hecke_laurent_fast.py:79-96). This is the "concatenate words,
    /// multiply coefficients" step; reduction (R1/R2/R3) is a separate
    /// pass in `reduce_laurent`.
    pub fn mul(&self, other: &Self) -> Self {
        let mut out = Self::zero();
        for (w1, c1) in &self.terms {
            for (w2, c2) in &other.terms {
                let mut w = Vec::with_capacity(w1.len() + w2.len());
                w.extend_from_slice(w1);
                w.extend_from_slice(w2);
                let cc = c1 * c2;
                out.accumulate(w, cc);
            }
        }
        out
    }

    /// FFI-friendly serialisation: list of `(word, [(exp, num_str, den_str)])`.
    /// Used by `pyhecke-native` to return the reduced element to Python.
    pub fn to_ffi(&self) -> Vec<(Vec<i32>, Vec<(i32, String, String)>)> {
        self.terms
            .iter()
            .map(|(w, c)| (w.clone(), c.to_ffi()))
            .collect()
    }

    /// FFI-friendly deserialisation: parse PyO3 input back into an
    /// element. Zero-coefficient terms are silently dropped.
    pub fn from_ffi(
        raw: &[(Vec<i32>, Vec<(i32, String, String)>)],
    ) -> Result<Self, String> {
        let mut out = Self::zero();
        for (w, triples) in raw {
            let c = LaurentRationalQ::from_ffi(triples)?;
            // Use accumulate so duplicate word entries are summed
            // (matches the Python ctor's per-key accumulation pattern).
            out.accumulate(w.clone(), c);
        }
        Ok(out)
    }
}

// ── Tests ─────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;
    use num_bigint::BigInt;
    use num_rational::BigRational;

    fn lq_one() -> LaurentRationalQ {
        LaurentRationalQ::one()
    }

    fn lq_int(n: i64) -> LaurentRationalQ {
        LaurentRationalQ::from_int(BigInt::from(n))
    }

    #[test]
    fn identity_times_anything_is_anything() {
        let id = LaurentHeckeElement::identity();
        let e = LaurentHeckeElement::monomial(vec![0, 1, 0], lq_int(3));
        assert_eq!(id.mul(&e), e);
        assert_eq!(e.mul(&id), e);
    }

    #[test]
    fn zero_times_anything_is_zero() {
        let z = LaurentHeckeElement::zero();
        let e = LaurentHeckeElement::monomial(vec![0, 1], lq_int(7));
        assert!(z.mul(&e).is_zero());
        assert!(e.mul(&z).is_zero());
    }

    #[test]
    fn mul_concatenates_words() {
        let a = LaurentHeckeElement::monomial(vec![0], lq_int(2));
        let b = LaurentHeckeElement::monomial(vec![1], lq_int(3));
        let p = a.mul(&b);
        assert_eq!(p.n_terms(), 1);
        assert_eq!(p.terms[&vec![0, 1]], lq_int(6));
    }

    #[test]
    fn mul_distributes_over_add() {
        // (σ0 + σ1) · σ0 = σ0 σ0 + σ1 σ0
        let mut left = LaurentHeckeElement::zero();
        left.accumulate(vec![0], lq_one());
        left.accumulate(vec![1], lq_one());
        let right = LaurentHeckeElement::monomial(vec![0], lq_one());
        let p = left.mul(&right);
        assert_eq!(p.n_terms(), 2);
        assert_eq!(p.terms[&vec![0, 0]], lq_one());
        assert_eq!(p.terms[&vec![1, 0]], lq_one());
    }

    #[test]
    fn accumulate_drops_zero_after_cancellation() {
        let mut e = LaurentHeckeElement::zero();
        e.accumulate(vec![0, 1], lq_int(5));
        e.accumulate(vec![0, 1], lq_int(-5));
        assert!(e.is_zero());
    }

    #[test]
    fn add_collapses_like_terms() {
        let a = LaurentHeckeElement::monomial(vec![0, 1], lq_int(2));
        let b = LaurentHeckeElement::monomial(vec![0, 1], lq_int(3));
        let s = a.add(&b);
        assert_eq!(s.n_terms(), 1);
        assert_eq!(s.terms[&vec![0, 1]], lq_int(5));
    }

    #[test]
    fn add_keeps_distinct_words() {
        let a = LaurentHeckeElement::monomial(vec![0], lq_int(2));
        let b = LaurentHeckeElement::monomial(vec![1], lq_int(3));
        let s = a.add(&b);
        assert_eq!(s.n_terms(), 2);
    }

    #[test]
    fn rational_coefs_in_mul() {
        // (1/2) σ0 · (2/3) σ1 = (1/3) σ0 σ1
        let a = LaurentHeckeElement::monomial(
            vec![0],
            LaurentRationalQ::from_rational(BigRational::new(1.into(), 2.into())),
        );
        let b = LaurentHeckeElement::monomial(
            vec![1],
            LaurentRationalQ::from_rational(BigRational::new(2.into(), 3.into())),
        );
        let p = a.mul(&b);
        assert_eq!(
            p.terms[&vec![0, 1]].coefs[&0],
            BigRational::new(1.into(), 3.into())
        );
    }

    #[test]
    fn ffi_round_trip_preserves_element() {
        let mut e = LaurentHeckeElement::zero();
        e.accumulate(vec![0, 1], LaurentRationalQ::hecke_a());
        e.accumulate(vec![1, 0], lq_int(2));
        let f = e.to_ffi();
        let r = LaurentHeckeElement::from_ffi(&f).unwrap();
        assert_eq!(e, r);
    }

    #[test]
    fn ffi_dedups_duplicate_words_via_sum() {
        // Two FFI entries with the same word — must be summed.
        let raw = vec![
            (vec![0i32], vec![(0i32, "3".to_string(), "1".to_string())]),
            (vec![0i32], vec![(0i32, "4".to_string(), "1".to_string())]),
        ];
        let r = LaurentHeckeElement::from_ffi(&raw).unwrap();
        assert_eq!(r.n_terms(), 1);
        assert_eq!(r.terms[&vec![0]], lq_int(7));
    }
}
