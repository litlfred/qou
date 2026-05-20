//! Laurent polynomial in `q` with `BigRational` coefficients.
//!
//! Port of `folio-assistant/computations/laurent_q.py::LaurentQ`. Used
//! as the coefficient algebra for the LaurentQ-direct Markov-trace
//! reduce loop on atomic-braid words (the Tier 1.A hot path per the
//! 2026-05-20 compute-optimisation roadmap).
//!
//! Internal repr: `BTreeMap<i32, BigRational>` keyed by integer
//! q-exponent. Zero coefficients are pruned on every operation so
//! `is_zero()` short-circuits on map-emptiness.
//!
//! **Ring-not-field**: deliberately stays in `Q[q, q^{-1}]` (no
//! division by polynomials). All Hecke / Markov compositions are
//! closed under add/sub/mul.
//!
//! Contrast with `laurent_poly_q::LaurentPolyQ` (this crate): that
//! type uses `BigInt` coefficients and `q^{1/2}` half-integer
//! exponents, suitable for the q-MN character recursion. `LaurentRationalQ`
//! uses `BigRational` and integer exponents, matching the Python
//! `LaurentQ` exactly so the Hecke σ² → (q − q⁻¹)σ + 1 rule can
//! produce rationals like `1/2` and so the Markov trace can be taken
//! without precision loss.

use num_bigint::BigInt;
use num_rational::BigRational;
use num_traits::{One, Zero};
use std::collections::BTreeMap;
use std::ops::{Add, AddAssign, Mul, Neg, Sub};

/// Sparse Laurent polynomial in `q` with `BigRational` coefficients.
///
/// ```ignore
/// use hecke_engine::laurent_rational_q::LaurentRationalQ;
/// // q − q^{-1}
/// let h = LaurentRationalQ::hecke_a();
/// // (q − q^{-1})^2 = q^2 − 2 + q^{-2}
/// let h2 = &h * &h;
/// ```
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub struct LaurentRationalQ {
    pub coefs: BTreeMap<i32, BigRational>,
}

impl LaurentRationalQ {
    /// The zero polynomial.
    pub fn zero() -> Self {
        Self { coefs: BTreeMap::new() }
    }

    /// The constant `1`.
    pub fn one() -> Self {
        let mut coefs = BTreeMap::new();
        coefs.insert(0, BigRational::one());
        Self { coefs }
    }

    /// Constant polynomial `c · 1` from a rational.
    pub fn from_rational(c: BigRational) -> Self {
        if c.is_zero() {
            return Self::zero();
        }
        let mut coefs = BTreeMap::new();
        coefs.insert(0, c);
        Self { coefs }
    }

    /// Constant polynomial `c · 1` from an integer.
    pub fn from_int<T: Into<BigInt>>(c: T) -> Self {
        let bi: BigInt = c.into();
        if bi.is_zero() {
            return Self::zero();
        }
        Self::from_rational(BigRational::from(bi))
    }

    /// Build from `(exp, num, den)` triples. Zero coefficients are
    /// dropped automatically. Same-exponent entries are summed.
    ///
    /// Panics if `den == 0`.
    pub fn from_terms<I, T>(triples: I) -> Self
    where
        I: IntoIterator<Item = (i32, T, T)>,
        T: Into<BigInt>,
    {
        let mut coefs: BTreeMap<i32, BigRational> = BTreeMap::new();
        for (exp, num, den) in triples {
            let r = BigRational::new(num.into(), den.into());
            if r.is_zero() {
                continue;
            }
            let entry = coefs.entry(exp).or_insert_with(BigRational::zero);
            *entry += r;
            if entry.is_zero() {
                coefs.remove(&exp);
            }
        }
        Self { coefs }
    }

    /// Single monomial `c · q^{exp}`.
    pub fn monomial(exp: i32, c: BigRational) -> Self {
        if c.is_zero() {
            return Self::zero();
        }
        let mut coefs = BTreeMap::new();
        coefs.insert(exp, c);
        Self { coefs }
    }

    /// `q^{exp}` (coefficient 1).
    pub fn q_pow(exp: i32) -> Self {
        Self::monomial(exp, BigRational::one())
    }

    /// The Hecke parameter `h := q − q^{-1}` as a LaurentRationalQ.
    ///
    /// This is the canonical R1 multiplier: `σ_i² → h · σ_i + 1`.
    pub fn hecke_a() -> Self {
        let mut coefs = BTreeMap::new();
        coefs.insert(1, BigRational::one());
        coefs.insert(-1, -BigRational::one());
        Self { coefs }
    }

    /// True iff every coefficient is zero (i.e. the empty polynomial).
    pub fn is_zero(&self) -> bool {
        self.coefs.is_empty()
    }

    /// Number of non-zero monomials.
    pub fn n_terms(&self) -> usize {
        self.coefs.len()
    }

    /// Smallest non-zero exponent, or `None` if zero.
    pub fn min_exp(&self) -> Option<i32> {
        self.coefs.keys().next().copied()
    }

    /// Largest non-zero exponent, or `None` if zero.
    pub fn max_exp(&self) -> Option<i32> {
        self.coefs.keys().next_back().copied()
    }

    /// Pretty representation, useful for tests and debug.
    pub fn pretty(&self) -> String {
        if self.coefs.is_empty() {
            return "0".to_string();
        }
        let mut parts = Vec::new();
        // Print in descending exponent order to match the Python
        // `LaurentQ.__repr__` (which iterates `sorted(..., reverse=True)`).
        for (&e, c) in self.coefs.iter().rev() {
            let cs = c.to_string();
            let term = if e == 0 {
                cs
            } else if e == 1 {
                if cs == "1" {
                    "q".to_string()
                } else if cs == "-1" {
                    "-q".to_string()
                } else {
                    format!("{}*q", cs)
                }
            } else if cs == "1" {
                format!("q^{}", e)
            } else if cs == "-1" {
                format!("-q^{}", e)
            } else {
                format!("{}*q^{}", cs, e)
            };
            parts.push(term);
        }
        parts.join(" + ")
    }

    /// FFI-friendly serialisation: list of `(exp, num_decimal, den_decimal)`
    /// for PyO3 round-tripping. Uses decimal strings to avoid the BigInt
    /// FFI cap (matches the pattern in `tr_m_word_lq.rs::to_ffi`).
    pub fn to_ffi(&self) -> Vec<(i32, String, String)> {
        self.coefs
            .iter()
            .map(|(&e, c)| (e, c.numer().to_str_radix(10), c.denom().to_str_radix(10)))
            .collect()
    }

    /// FFI-friendly deserialisation: parse `(exp, num_decimal, den_decimal)`
    /// triples back into a `LaurentRationalQ`. Used by `pyhecke-native`
    /// to receive Hecke-element coefficients from the Python boundary.
    pub fn from_ffi(triples: &[(i32, String, String)]) -> Result<Self, String> {
        let mut coefs: BTreeMap<i32, BigRational> = BTreeMap::new();
        for (e, ns, ds) in triples {
            let num = BigInt::parse_bytes(ns.as_bytes(), 10)
                .ok_or_else(|| format!("LaurentRationalQ::from_ffi: bad numerator {:?}", ns))?;
            let den = BigInt::parse_bytes(ds.as_bytes(), 10)
                .ok_or_else(|| format!("LaurentRationalQ::from_ffi: bad denominator {:?}", ds))?;
            if den.is_zero() {
                return Err(format!(
                    "LaurentRationalQ::from_ffi: zero denominator at exp {}",
                    e
                ));
            }
            let r = BigRational::new(num, den);
            if r.is_zero() {
                continue;
            }
            let entry = coefs.entry(*e).or_insert_with(BigRational::zero);
            *entry += r;
            if entry.is_zero() {
                coefs.remove(e);
            }
        }
        Ok(Self { coefs })
    }
}

// ── Arithmetic ────────────────────────────────────────────────────

impl AddAssign<&LaurentRationalQ> for LaurentRationalQ {
    fn add_assign(&mut self, other: &LaurentRationalQ) {
        for (&e, c) in &other.coefs {
            let entry = self.coefs.entry(e).or_insert_with(BigRational::zero);
            *entry += c;
            if entry.is_zero() {
                self.coefs.remove(&e);
            }
        }
    }
}

impl Add<&LaurentRationalQ> for &LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn add(self, other: &LaurentRationalQ) -> LaurentRationalQ {
        let mut out = self.clone();
        out += other;
        out
    }
}

impl Add for LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn add(mut self, other: LaurentRationalQ) -> LaurentRationalQ {
        self += &other;
        self
    }
}

impl Neg for LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn neg(self) -> LaurentRationalQ {
        let coefs = self.coefs.into_iter().map(|(e, c)| (e, -c)).collect();
        LaurentRationalQ { coefs }
    }
}

impl Neg for &LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn neg(self) -> LaurentRationalQ {
        let coefs = self.coefs.iter().map(|(&e, c)| (e, -c)).collect();
        LaurentRationalQ { coefs }
    }
}

impl Sub<&LaurentRationalQ> for &LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn sub(self, other: &LaurentRationalQ) -> LaurentRationalQ {
        self + &(-other)
    }
}

impl Mul<&LaurentRationalQ> for &LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn mul(self, other: &LaurentRationalQ) -> LaurentRationalQ {
        if self.coefs.is_empty() || other.coefs.is_empty() {
            return LaurentRationalQ::zero();
        }
        let mut coefs: BTreeMap<i32, BigRational> = BTreeMap::new();
        for (&e1, c1) in &self.coefs {
            for (&e2, c2) in &other.coefs {
                let e = e1 + e2;
                let prod = c1 * c2;
                let entry = coefs.entry(e).or_insert_with(BigRational::zero);
                *entry += prod;
                if entry.is_zero() {
                    coefs.remove(&e);
                }
            }
        }
        LaurentRationalQ { coefs }
    }
}

impl Mul for LaurentRationalQ {
    type Output = LaurentRationalQ;
    fn mul(self, other: LaurentRationalQ) -> LaurentRationalQ {
        (&self).mul(&other)
    }
}

// ── Tests ─────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    fn r(n: i64, d: i64) -> BigRational {
        BigRational::new(n.into(), d.into())
    }

    #[test]
    fn zero_and_one() {
        let z = LaurentRationalQ::zero();
        let o = LaurentRationalQ::one();
        assert!(z.is_zero());
        assert!(!o.is_zero());
        assert_eq!(o.n_terms(), 1);
        assert_eq!(o.coefs[&0], BigRational::one());
        // 0 * anything = 0
        let prod = &z * &o;
        assert!(prod.is_zero());
    }

    #[test]
    fn hecke_a_value() {
        // h = q − q^{-1}
        let h = LaurentRationalQ::hecke_a();
        assert_eq!(h.coefs[&1], BigRational::one());
        assert_eq!(h.coefs[&-1], -BigRational::one());
        assert_eq!(h.n_terms(), 2);
    }

    #[test]
    fn hecke_a_squared() {
        // (q − q^{-1})^2 = q^2 − 2 + q^{-2}
        let h = LaurentRationalQ::hecke_a();
        let h2 = &h * &h;
        assert_eq!(h2.coefs[&2], BigRational::one());
        assert_eq!(h2.coefs[&0], BigRational::from(BigInt::from(-2)));
        assert_eq!(h2.coefs[&-2], BigRational::one());
        assert_eq!(h2.n_terms(), 3);
    }

    #[test]
    fn add_cancellation_drops_zeros() {
        let h = LaurentRationalQ::hecke_a();
        let nh = -&h;
        let s = &h + &nh;
        assert!(s.is_zero());
    }

    #[test]
    fn rational_coefficients_preserved() {
        // (1/2) · q + (1/3) · q^{-1}
        let p = LaurentRationalQ::from_terms(vec![(1i32, 1i64, 2i64), (-1, 1, 3)]);
        assert_eq!(p.coefs[&1], r(1, 2));
        assert_eq!(p.coefs[&-1], r(1, 3));
        // p * p = 1/4 q^2 + (1/2·1/3 + 1/3·1/2) + 1/9 q^{-2}
        //       = 1/4 q^2 + 1/3 + 1/9 q^{-2}
        let p2 = &p * &p;
        assert_eq!(p2.coefs[&2], r(1, 4));
        assert_eq!(p2.coefs[&0], r(1, 3));
        assert_eq!(p2.coefs[&-2], r(1, 9));
    }

    #[test]
    fn ffi_round_trip() {
        let h = LaurentRationalQ::hecke_a();
        let h2 = &h * &h;
        let ffi = h2.to_ffi();
        let recon = LaurentRationalQ::from_ffi(&ffi).unwrap();
        assert_eq!(h2, recon);
    }

    #[test]
    fn ffi_zero_denominator_rejected() {
        let bad = vec![(0i32, "1".to_string(), "0".to_string())];
        assert!(LaurentRationalQ::from_ffi(&bad).is_err());
    }

    #[test]
    fn ffi_pre_simplified_rational() {
        // 2/4 should reduce to 1/2 via BigRational::new (which calls gcd).
        let triples = vec![(0i32, "2".to_string(), "4".to_string())];
        let l = LaurentRationalQ::from_ffi(&triples).unwrap();
        assert_eq!(l.coefs[&0], BigRational::new(1.into(), 2.into()));
    }

    #[test]
    fn pretty_smoke() {
        let h = LaurentRationalQ::hecke_a();
        let s = h.pretty();
        // Just ensure it doesn't panic and contains both terms.
        assert!(s.contains("q"));
    }
}
