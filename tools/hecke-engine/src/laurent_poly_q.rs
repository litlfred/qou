//! Laurent polynomial in `q^{1/2}` with `BigInt` coefficients.
//!
//! Used by F3.2 (q-deformed Murnaghan-Nakayama / Ram-Wenzl character
//! recursion).  Half-integer exponents are stored as `i32` keys equal
//! to `2 × (q-exponent)`, so monomial `q^{n/2}` has key `n`.
//!
//! Sparse representation (BTreeMap keyed by exponent) — most q-MN
//! intermediate polynomials have few non-zero terms (≤ n).

use num_bigint::BigInt;
use num_traits::{One, ToPrimitive, Zero};
use std::collections::BTreeMap;
use std::ops::{Add, AddAssign, Mul, MulAssign, Neg, Sub, SubAssign};

/// Laurent polynomial in `q^{1/2}` with `BigInt` coefficients.
///
/// Internally a `BTreeMap<i32, BigInt>` where the key `2k` represents
/// the monomial `q^{k}` and key `2k+1` represents `q^{(2k+1)/2}`.
///
/// ```ignore
/// use hecke_engine::laurent_poly_q::LaurentPolyQ;
/// // q + q^{-1}
/// let p = LaurentPolyQ::from_terms(vec![(2, 1), (-2, 1)]);
/// // q^{1/2}
/// let q_half = LaurentPolyQ::q_half_pow(1);
/// ```
#[derive(Clone, Debug, Default)]
pub struct LaurentPolyQ {
    pub terms: BTreeMap<i32, BigInt>,
}

impl LaurentPolyQ {
    pub fn zero() -> Self {
        Self { terms: BTreeMap::new() }
    }

    pub fn one() -> Self {
        let mut terms = BTreeMap::new();
        terms.insert(0, BigInt::one());
        Self { terms }
    }

    /// Constant polynomial (BigInt scalar).
    pub fn from_scalar<T: Into<BigInt>>(c: T) -> Self {
        let bi: BigInt = c.into();
        if bi.is_zero() {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        terms.insert(0, bi);
        Self { terms }
    }

    /// Build from a list of (half_exponent, coefficient) terms.
    /// `half_exponent = 2 × (q-exponent)`.
    pub fn from_terms<T: Into<BigInt>>(pairs: Vec<(i32, T)>) -> Self {
        let mut terms = BTreeMap::new();
        for (he, c) in pairs {
            let bi: BigInt = c.into();
            if !bi.is_zero() {
                *terms.entry(he).or_insert_with(BigInt::zero) += bi;
            }
        }
        // Strip zero entries.
        terms.retain(|_, v| !v.is_zero());
        Self { terms }
    }

    /// `q^{n/2}` for integer n (n=2 gives q, n=-2 gives q^{-1}, etc.).
    pub fn q_half_pow(half_exp: i32) -> Self {
        let mut terms = BTreeMap::new();
        terms.insert(half_exp, BigInt::one());
        Self { terms }
    }

    /// `q^n` for integer n.
    pub fn q_pow(n: i32) -> Self {
        Self::q_half_pow(2 * n)
    }

    /// `h := q − q^{-1}`, the Hecke parameter.
    pub fn hecke_h() -> Self {
        Self::from_terms(vec![(2, 1), (-2, -1)])
    }

    pub fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    /// Multiply in place by an integer.
    pub fn scalar_mul_assign<T: Into<BigInt>>(&mut self, c: T) {
        let bi: BigInt = c.into();
        if bi.is_zero() {
            self.terms.clear();
            return;
        }
        for v in self.terms.values_mut() {
            *v *= &bi;
        }
    }

    /// Substitute q = 1 (set every q^? = 1) and return the resulting
    /// integer.  Returns the sum of coefficients.
    pub fn evaluate_at_one(&self) -> BigInt {
        let mut total = BigInt::zero();
        for v in self.terms.values() {
            total += v;
        }
        total
    }

    /// Substitute q = exact value (as f64) and return the result.
    /// Internal arithmetic done via repeated f64 multiplication —
    /// for high precision use `evaluate_mpfr`.
    ///
    /// **Panics** if any coefficient is not representable in f64
    /// (overflows the f64 range or `BigInt::to_f64` returns `None`).
    /// This surfaces invariant violations early instead of silently
    /// producing wrong numeric results (Copilot review #r3143557490).
    /// Callers requiring overflow-tolerance should use the mpfr path.
    pub fn evaluate_f64(&self, q: f64) -> f64 {
        let mut total = 0.0f64;
        for (&he, c) in &self.terms {
            // q^{he/2}: use sqrt + powi pattern.
            let exponent_doubled = he as f64 / 2.0;
            let term = q.powf(exponent_doubled);
            // BigInt → f64 via num_traits::ToPrimitive.  Panic on
            // unrepresentable coefficients to avoid silent miscompute.
            let cf = c.to_f64().unwrap_or_else(|| {
                panic!(
                    "LaurentPolyQ::evaluate_f64: coefficient {} (at q^{{{}/2}}) \
                     is not representable in f64 — use mpfr path for full precision",
                    c, he
                )
            });
            total += cf * term;
        }
        total
    }

    /// Format as a string, useful for tests.
    pub fn pretty(&self) -> String {
        if self.is_zero() {
            return "0".to_string();
        }
        let mut parts = Vec::new();
        for (&he, c) in &self.terms {
            let coeff_str = c.to_string();
            let mono = if he == 0 {
                String::new()
            } else if he % 2 == 0 {
                let e = he / 2;
                if e == 1 { "q".to_string() } else { format!("q^{}", e) }
            } else {
                format!("q^({}/2)", he)
            };
            parts.push(if mono.is_empty() {
                coeff_str
            } else if coeff_str == "1" {
                mono
            } else if coeff_str == "-1" {
                format!("-{}", mono)
            } else {
                format!("{}*{}", coeff_str, mono)
            });
        }
        parts.join(" + ")
    }
}

// ── Arithmetic ────────────────────────────────────────────────────

impl AddAssign<&LaurentPolyQ> for LaurentPolyQ {
    fn add_assign(&mut self, other: &LaurentPolyQ) {
        for (&he, c) in &other.terms {
            let entry = self.terms.entry(he).or_insert_with(BigInt::zero);
            *entry += c;
            if entry.is_zero() {
                self.terms.remove(&he);
            }
        }
    }
}

impl SubAssign<&LaurentPolyQ> for LaurentPolyQ {
    fn sub_assign(&mut self, other: &LaurentPolyQ) {
        for (&he, c) in &other.terms {
            let entry = self.terms.entry(he).or_insert_with(BigInt::zero);
            *entry -= c;
            if entry.is_zero() {
                self.terms.remove(&he);
            }
        }
    }
}

impl Add for LaurentPolyQ {
    type Output = Self;
    fn add(mut self, other: Self) -> Self {
        self += &other;
        self
    }
}

impl Sub for LaurentPolyQ {
    type Output = Self;
    fn sub(mut self, other: Self) -> Self {
        self -= &other;
        self
    }
}

impl Neg for LaurentPolyQ {
    type Output = Self;
    fn neg(self) -> Self {
        let mut out = self;
        for v in out.terms.values_mut() {
            *v = -std::mem::replace(v, BigInt::zero());
        }
        out
    }
}

impl Mul for LaurentPolyQ {
    type Output = Self;
    fn mul(self, other: Self) -> Self {
        if self.is_zero() || other.is_zero() {
            return Self::zero();
        }
        let mut result = BTreeMap::<i32, BigInt>::new();
        for (&he1, c1) in &self.terms {
            for (&he2, c2) in &other.terms {
                let key = he1 + he2;
                let prod = c1 * c2;
                let entry = result.entry(key).or_insert_with(BigInt::zero);
                *entry += prod;
            }
        }
        result.retain(|_, v| !v.is_zero());
        Self { terms: result }
    }
}

impl MulAssign for LaurentPolyQ {
    fn mul_assign(&mut self, other: Self) {
        let result = std::mem::take(self) * other;
        *self = result;
    }
}

impl PartialEq for LaurentPolyQ {
    fn eq(&self, other: &Self) -> bool {
        self.terms == other.terms
    }
}
impl Eq for LaurentPolyQ {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn zero_one() {
        let z = LaurentPolyQ::zero();
        let o = LaurentPolyQ::one();
        assert!(z.is_zero());
        assert!(!o.is_zero());
        assert_eq!(z.evaluate_at_one(), BigInt::zero());
        assert_eq!(o.evaluate_at_one(), BigInt::one());
    }

    #[test]
    fn q_pow() {
        let q = LaurentPolyQ::q_pow(1);
        let q_inv = LaurentPolyQ::q_pow(-1);
        let h = LaurentPolyQ::hecke_h();
        // q − q^{-1}.
        assert_eq!(h, q.clone() - q_inv.clone());
        // h evaluated at q=1 is 0.
        assert_eq!(h.evaluate_at_one(), BigInt::zero());
        // q · q^{-1} = 1.
        let one = q * q_inv;
        assert_eq!(one, LaurentPolyQ::one());
    }

    #[test]
    fn add_sub() {
        let a = LaurentPolyQ::from_terms(vec![(2, 3), (-2, 5)]);
        let b = LaurentPolyQ::from_terms(vec![(2, 4)]);
        let c = a.clone() + b.clone();
        // Should be 7q + 5q^{-1}.
        assert_eq!(c, LaurentPolyQ::from_terms(vec![(2, 7), (-2, 5)]));
        let d = a - b;
        // Should be -q + 5q^{-1}.
        assert_eq!(d, LaurentPolyQ::from_terms(vec![(2, -1), (-2, 5)]));
    }

    #[test]
    fn mul() {
        let q = LaurentPolyQ::q_pow(1);
        let q_inv = LaurentPolyQ::q_pow(-1);
        let h = LaurentPolyQ::hecke_h();
        // h · h = q² − 2 + q^{-2}.
        let h_sq = h.clone() * h;
        assert_eq!(
            h_sq,
            LaurentPolyQ::from_terms(vec![(4, 1), (0, -2), (-4, 1)])
        );
        // (q + q^{-1}) · (q − q^{-1}) = q² − q^{-2}.
        let plus = q.clone() + q_inv.clone();
        let minus = q.clone() - q_inv.clone();
        let prod = plus * minus;
        assert_eq!(prod, LaurentPolyQ::from_terms(vec![(4, 1), (-4, -1)]));
    }

    #[test]
    fn evaluate_f64() {
        // (q + q^{-1}) at q=2 should be 2.5.
        let p = LaurentPolyQ::q_pow(1) + LaurentPolyQ::q_pow(-1);
        assert!((p.evaluate_f64(2.0) - 2.5).abs() < 1e-12);
    }

    #[test]
    fn half_integer_exponents() {
        // q^{1/2} · q^{1/2} = q.
        let qh = LaurentPolyQ::q_half_pow(1);
        let q_full = qh.clone() * qh;
        assert_eq!(q_full, LaurentPolyQ::q_pow(1));
    }
}
