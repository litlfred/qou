//! Exact commutative coefficient rings for non-commutative Gröbner–Shirshov computations.

use std::collections::BTreeMap;
use std::fmt;
use std::ops::{Add, Mul, Neg, Sub};

use num_bigint::BigInt;
use num_integer::Integer;
use num_rational::BigRational;
use num_traits::{One, Signed, Zero};
use serde::{Deserialize, Serialize};

/// Exact commutative unital ring scalar supporting zero-pruning, unit inversion, and
/// exact division where defined.
pub trait RingScalar: Clone + PartialEq + Eq + fmt::Debug + fmt::Display {
    /// Additive identity $0$.
    fn zero() -> Self;

    /// Multiplicative identity $1$.
    fn one() -> Self;

    /// Canonical ring image of a signed 64-bit integer.
    fn from_i64(n: i64) -> Self;

    /// Returns `true` iff `self == 0`.
    fn is_zero(&self) -> bool;

    /// Returns `true` iff `self == 1`.
    fn is_one(&self) -> bool {
        *self == Self::one()
    }

    /// Additive inverse `-self`.
    fn neg_val(&self) -> Self;

    /// Sum `self + rhs`.
    fn add_val(&self, rhs: &Self) -> Self;

    /// Difference `self - rhs`.
    fn sub_val(&self, rhs: &Self) -> Self {
        self.add_val(&rhs.neg_val())
    }

    /// Product `self * rhs`.
    fn mul_val(&self, rhs: &Self) -> Self;

    /// Binary exponentiation `self^exp` (`0^0 = 1`).
    fn pow_u32(&self, mut exp: u32) -> Self {
        let mut base = self.clone();
        let mut acc = Self::one();
        while exp > 0 {
            if exp & 1 == 1 {
                acc = acc.mul_val(&base);
            }
            exp >>= 1;
            if exp > 0 {
                base = base.mul_val(&base);
            }
        }
        acc
    }

    /// Multiplicative inverse if `self` is a unit in the ring, or `None` otherwise.
    fn try_inv(&self) -> Option<Self>;

    /// Exact quotient `q` satisfying `q * rhs == self` when `rhs` is a non-zero divisor
    /// dividing `self` cleanly in the ring.
    fn try_div_exact(&self, rhs: &Self) -> Option<Self> {
        let inv = rhs.try_inv()?;
        Some(self.mul_val(&inv))
    }
}

impl RingScalar for i64 {
    fn zero() -> Self {
        0
    }
    fn one() -> Self {
        1
    }
    fn from_i64(n: i64) -> Self {
        n
    }
    fn is_zero(&self) -> bool {
        *self == 0
    }
    fn neg_val(&self) -> Self {
        self.checked_neg().expect("i64 negation overflow")
    }
    fn add_val(&self, rhs: &Self) -> Self {
        self.checked_add(*rhs).expect("i64 addition overflow")
    }
    fn sub_val(&self, rhs: &Self) -> Self {
        self.checked_sub(*rhs).expect("i64 subtraction overflow")
    }
    fn mul_val(&self, rhs: &Self) -> Self {
        self.checked_mul(*rhs).expect("i64 multiplication overflow")
    }
    fn try_inv(&self) -> Option<Self> {
        match *self {
            1 => Some(1),
            -1 => Some(-1),
            _ => None,
        }
    }
    fn try_div_exact(&self, rhs: &Self) -> Option<Self> {
        if *rhs == 0 {
            return None;
        }
        if self.checked_rem(*rhs)? == 0 {
            self.checked_div(*rhs)
        } else {
            None
        }
    }
}

impl RingScalar for BigInt {
    fn zero() -> Self {
        Zero::zero()
    }
    fn one() -> Self {
        One::one()
    }
    fn from_i64(n: i64) -> Self {
        BigInt::from(n)
    }
    fn is_zero(&self) -> bool {
        Zero::is_zero(self)
    }
    fn neg_val(&self) -> Self {
        -self
    }
    fn add_val(&self, rhs: &Self) -> Self {
        self + rhs
    }
    fn sub_val(&self, rhs: &Self) -> Self {
        self - rhs
    }
    fn mul_val(&self, rhs: &Self) -> Self {
        self * rhs
    }
    fn try_inv(&self) -> Option<Self> {
        let one: BigInt = One::one();
        if *self == one {
            Some(one)
        } else if *self == -(&one) {
            Some(-one)
        } else {
            None
        }
    }
    fn try_div_exact(&self, rhs: &Self) -> Option<Self> {
        if Zero::is_zero(rhs) {
            return None;
        }
        let (q, r) = self.div_rem(rhs);
        if Zero::is_zero(&r) {
            Some(q)
        } else {
            None
        }
    }
}

impl RingScalar for BigRational {
    fn zero() -> Self {
        Zero::zero()
    }
    fn one() -> Self {
        One::one()
    }
    fn from_i64(n: i64) -> Self {
        BigRational::from_integer(BigInt::from(n))
    }
    fn is_zero(&self) -> bool {
        Zero::is_zero(self)
    }
    fn neg_val(&self) -> Self {
        -self
    }
    fn add_val(&self, rhs: &Self) -> Self {
        self + rhs
    }
    fn sub_val(&self, rhs: &Self) -> Self {
        self - rhs
    }
    fn mul_val(&self, rhs: &Self) -> Self {
        self * rhs
    }
    fn try_inv(&self) -> Option<Self> {
        if Zero::is_zero(self) {
            None
        } else {
            Some(self.recip())
        }
    }
    fn try_div_exact(&self, rhs: &Self) -> Option<Self> {
        if Zero::is_zero(rhs) {
            None
        } else {
            Some(self / rhs)
        }
    }
}

/// Sparse Laurent polynomial in $R[q, q^{-1}]$, canonically pruned of zero coefficients.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct LaurentPoly<R> {
    terms: BTreeMap<i32, R>,
}

impl<R: RingScalar> LaurentPoly<R> {
    /// Zero Laurent polynomial.
    pub fn zero_poly() -> Self {
        Self {
            terms: BTreeMap::new(),
        }
    }

    /// Constant Laurent polynomial $c \cdot q^0$.
    pub fn constant(c: R) -> Self {
        let mut terms = BTreeMap::new();
        if !c.is_zero() {
            terms.insert(0, c);
        }
        Self { terms }
    }

    /// Single monomial $c \cdot q^k$.
    pub fn monomial(exp: i32, coeff: R) -> Self {
        let mut terms = BTreeMap::new();
        if !coeff.is_zero() {
            terms.insert(exp, coeff);
        }
        Self { terms }
    }

    /// Construct from `(exponent, coeff)` pairs, summing like exponents and pruning zeros.
    pub fn from_terms<I: IntoIterator<Item = (i32, R)>>(iter: I) -> Self {
        let mut terms: BTreeMap<i32, R> = BTreeMap::new();
        for (exp, coeff) in iter {
            if coeff.is_zero() {
                continue;
            }
            if let Some(existing) = terms.get_mut(&exp) {
                let sum = existing.add_val(&coeff);
                if sum.is_zero() {
                    terms.remove(&exp);
                } else {
                    *existing = sum;
                }
            } else {
                terms.insert(exp, coeff);
            }
        }
        Self { terms }
    }

    /// Indeterminate $q$.
    pub fn q() -> Self {
        Self::monomial(1, R::one())
    }

    /// Inverse indeterminate $q^{-1}$.
    pub fn q_inv() -> Self {
        Self::monomial(-1, R::one())
    }

    /// Balanced Hecke deformation parameter $h = q - q^{-1}$.
    pub fn h() -> Self {
        Self::from_terms([(1, R::one()), (-1, R::one().neg_val())])
    }

    /// Temperley–Lieb loop parameter $\delta = \[2\]_q = q + q^{-1}$.
    pub fn delta_two() -> Self {
        Self::from_terms([(1, R::one()), (-1, R::one())])
    }

    /// Symmetric quantum integer $\[n\]_q = \frac{q^n - q^{-n}}{q - q^{-1}}$ constructed
    /// division-free over any commutative ring $R$.
    pub fn q_int(n: i32) -> Self {
        if n == 0 {
            return Self::zero_poly();
        }
        let abs_n = n.unsigned_abs() as i32;
        let coeff = if n > 0 { R::one() } else { R::one().neg_val() };
        let mut terms = BTreeMap::new();
        for k in 0..abs_n {
            let exp = abs_n - 1 - 2 * k;
            terms.insert(exp, coeff.clone());
        }
        Self { terms }
    }

    /// Underlying non-zero exponent-to-coefficient map.
    pub fn terms(&self) -> &BTreeMap<i32, R> {
        &self.terms
    }

    /// Coefficient of $q^{\text{exp}}$ ($0$ if absent).
    pub fn coeff(&self, exp: i32) -> R {
        self.terms.get(&exp).cloned().unwrap_or_else(R::zero)
    }

    /// Minimum exponent with non-zero coefficient, or `None` if zero.
    pub fn min_degree(&self) -> Option<i32> {
        self.terms.keys().next().copied()
    }

    /// Maximum exponent with non-zero coefficient, or `None` if zero.
    pub fn max_degree(&self) -> Option<i32> {
        self.terms.keys().next_back().copied()
    }

    /// Multiply by $q^{\text{shift}}$.
    pub fn shift(&self, shift: i32) -> Self {
        let terms = self
            .terms
            .iter()
            .map(|(&e, c)| (e + shift, c.clone()))
            .collect();
        Self { terms }
    }

    /// Scale all coefficients by `s`.
    pub fn scale(&self, s: &R) -> Self {
        if s.is_zero() {
            return Self::zero_poly();
        }
        let mut terms = BTreeMap::new();
        for (&e, c) in &self.terms {
            let prod = c.mul_val(s);
            if !prod.is_zero() {
                terms.insert(e, prod);
            }
        }
        Self { terms }
    }

    /// Bar involution $q \mapsto q^{-1}$ fixing coefficients in $R$.
    pub fn bar(&self) -> Self {
        let terms = self.terms.iter().map(|(&e, c)| (-e, c.clone())).collect();
        Self { terms }
    }

    /// Evaluate at an explicit pair `(q_val, q_inv_val)` in a target ring `S`.
    pub fn eval_with<S: RingScalar, F: Fn(&R) -> S>(
        &self,
        q_val: &S,
        q_inv_val: &S,
        map_coeff: F,
    ) -> S {
        let mut acc = S::zero();
        for (&exp, coeff) in &self.terms {
            let c_mapped = map_coeff(coeff);
            let power = if exp >= 0 {
                q_val.pow_u32(exp as u32)
            } else {
                q_inv_val.pow_u32(exp.unsigned_abs())
            };
            acc = acc.add_val(&c_mapped.mul_val(&power));
        }
        acc
    }

    /// Evaluate at a unit `q_val` in `R`.
    pub fn eval_at_unit(&self, q_val: &R) -> Option<R> {
        let q_inv = q_val.try_inv()?;
        Some(self.eval_with(q_val, &q_inv, Clone::clone))
    }
}

impl<R: RingScalar> fmt::Display for LaurentPoly<R> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.terms.is_empty() {
            return write!(f, "0");
        }
        let mut first = true;
        for (&exp, coeff) in self.terms.iter().rev() {
            if !first {
                write!(f, " + ")?;
            }
            first = false;
            match exp {
                0 => write!(f, "{coeff}")?,
                1 if coeff.is_one() => write!(f, "q")?,
                1 => write!(f, "({coeff})*q")?,
                e if coeff.is_one() => write!(f, "q^{e}")?,
                e => write!(f, "({coeff})*q^{e}")?,
            }
        }
        Ok(())
    }
}

impl<R: RingScalar> RingScalar for LaurentPoly<R> {
    fn zero() -> Self {
        Self::zero_poly()
    }
    fn one() -> Self {
        Self::constant(R::one())
    }
    fn from_i64(n: i64) -> Self {
        Self::constant(R::from_i64(n))
    }
    fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }
    fn neg_val(&self) -> Self {
        let terms = self
            .terms
            .iter()
            .map(|(&e, c)| (e, c.neg_val()))
            .collect();
        Self { terms }
    }
    fn add_val(&self, rhs: &Self) -> Self {
        let mut terms = self.terms.clone();
        for (&exp, r_coeff) in &rhs.terms {
            if let Some(l_coeff) = terms.get_mut(&exp) {
                let sum = l_coeff.add_val(r_coeff);
                if sum.is_zero() {
                    terms.remove(&exp);
                } else {
                    *l_coeff = sum;
                }
            } else {
                terms.insert(exp, r_coeff.clone());
            }
        }
        Self { terms }
    }
    fn mul_val(&self, rhs: &Self) -> Self {
        if self.is_zero() || rhs.is_zero() {
            return Self::zero_poly();
        }
        let mut acc: BTreeMap<i32, R> = BTreeMap::new();
        for (&e1, c1) in &self.terms {
            for (&e2, c2) in &rhs.terms {
                let prod = c1.mul_val(c2);
                if prod.is_zero() {
                    continue;
                }
                let exp = e1 + e2;
                if let Some(existing) = acc.get_mut(&exp) {
                    let sum = existing.add_val(&prod);
                    if sum.is_zero() {
                        acc.remove(&exp);
                    } else {
                        *existing = sum;
                    }
                } else {
                    acc.insert(exp, prod);
                }
            }
        }
        Self { terms: acc }
    }
    fn try_inv(&self) -> Option<Self> {
        if self.terms.len() != 1 {
            return None;
        }
        let (&exp, coeff) = self.terms.iter().next()?;
        let c_inv = coeff.try_inv()?;
        Some(Self::monomial(-exp, c_inv))
    }
    fn try_div_exact(&self, rhs: &Self) -> Option<Self> {
        if rhs.is_zero() {
            return None;
        }
        if self.is_zero() {
            return Some(Self::zero_poly());
        }
        if let Some(inv) = rhs.try_inv() {
            return Some(self.mul_val(&inv));
        }
        // Laurent polynomial long division in R[q, q^{-1}]:
        let rhs_min = rhs.min_degree()?;
        let rhs_max = rhs.max_degree()?;
        let rhs_lead = rhs.terms.get(&rhs_max)?;
        let mut rem = self.clone();
        let mut quot_terms: BTreeMap<i32, R> = BTreeMap::new();
        let max_steps = (self.max_degree()? - self.min_degree()? + 2).max(1) as usize;
        for _ in 0..=max_steps {
            if rem.is_zero() {
                return Some(Self::from_terms(quot_terms));
            }
            let rem_min = rem.min_degree()?;
            let rem_max = rem.max_degree()?;
            if rem_max - rem_min < rhs_max - rhs_min {
                return None;
            }
            let rem_lead = rem.terms.get(&rem_max)?;
            let q_coeff = rem_lead.try_div_exact(rhs_lead)?;
            let q_exp = rem_max - rhs_max;
            let step = Self::monomial(q_exp, q_coeff.clone());
            rem = rem.sub_val(&step.mul_val(rhs));
            quot_terms.insert(q_exp, q_coeff);
        }
        if rem.is_zero() {
            Some(Self::from_terms(quot_terms))
        } else {
            None
        }
    }
}

impl<R: RingScalar> Add for LaurentPoly<R> {
    type Output = Self;
    fn add(self, rhs: Self) -> Self::Output {
        self.add_val(&rhs)
    }
}

impl<R: RingScalar> Add<&LaurentPoly<R>> for &LaurentPoly<R> {
    type Output = LaurentPoly<R>;
    fn add(self, rhs: &LaurentPoly<R>) -> Self::Output {
        self.add_val(rhs)
    }
}

impl<R: RingScalar> Sub for LaurentPoly<R> {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self::Output {
        self.sub_val(&rhs)
    }
}

impl<R: RingScalar> Sub<&LaurentPoly<R>> for &LaurentPoly<R> {
    type Output = LaurentPoly<R>;
    fn sub(self, rhs: &LaurentPoly<R>) -> Self::Output {
        self.sub_val(rhs)
    }
}

impl<R: RingScalar> Mul for LaurentPoly<R> {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self::Output {
        self.mul_val(&rhs)
    }
}

impl<R: RingScalar> Mul<&LaurentPoly<R>> for &LaurentPoly<R> {
    type Output = LaurentPoly<R>;
    fn mul(self, rhs: &LaurentPoly<R>) -> Self::Output {
        self.mul_val(rhs)
    }
}

impl<R: RingScalar> Neg for LaurentPoly<R> {
    type Output = Self;
    fn neg(self) -> Self::Output {
        self.neg_val()
    }
}

impl<R: RingScalar> Neg for &LaurentPoly<R> {
    type Output = LaurentPoly<R>;
    fn neg(self) -> Self::Output {
        self.neg_val()
    }
}

/// Truncated $h$-jet ring $R\[h\]/(h^{K+1})$ keeping powers $h^0, h^1, \dots, h^K$.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct TruncatedJet<R, const K: usize = 8> {
    coeffs: Vec<R>,
}

impl<R: RingScalar, const K: usize> TruncatedJet<R, K> {
    fn normalize(mut coeffs: Vec<R>) -> Self {
        if coeffs.len() > K + 1 {
            coeffs.truncate(K + 1);
        }
        while let Some(last) = coeffs.last() {
            if last.is_zero() {
                coeffs.pop();
            } else {
                break;
            }
        }
        Self { coeffs }
    }

    /// Zero jet in $R\[h\]/(h^{K+1})$.
    pub fn zero_jet() -> Self {
        Self { coeffs: Vec::new() }
    }

    /// Constant jet $c + O(h^{K+1})$.
    pub fn constant(c: R) -> Self {
        Self::normalize(vec![c])
    }

    /// Indeterminate $h \pmod{h^{K+1}}$.
    pub fn h() -> Self {
        if K == 0 {
            Self::zero_jet()
        } else {
            Self::normalize(vec![R::zero(), R::one()])
        }
    }

    /// Construct from dense coefficient slice `[c_0, c_1, ...]`, truncating above `h^K`.
    pub fn from_coeffs(coeffs: Vec<R>) -> Self {
        Self::normalize(coeffs)
    }

    /// Maximum retained exponent $K$ of $R\[h\]/(h^{K+1})$.
    pub const fn truncation_order() -> usize {
        K
    }

    /// Coefficient of $h^{\text{deg}}$ (`0` if `deg > K` or trailing zero).
    pub fn coeff(&self, deg: usize) -> R {
        self.coeffs.get(deg).cloned().unwrap_or_else(R::zero)
    }

    /// Lowest index $v$ with `coeff(v) != 0`, or `None` if zero.
    pub fn valuation(&self) -> Option<usize> {
        self.coeffs.iter().position(|c| !c.is_zero())
    }

    /// Non-zero prefix slice of coefficients up to the highest non-zero power $\le K$.
    pub fn coeffs(&self) -> &[R] {
        &self.coeffs
    }
}

impl<const K: usize> TruncatedJet<BigRational, K> {
    /// Positive-branch expansion of $q(h) = \frac{h}{2} + \sqrt{1 + \frac{h^2}{4}} \in \mathbb{Q}\[h\]/(h^{K+1})$
    /// satisfying $q(h) - q(h)^{-1} \equiv h \pmod{h^{K+1}}$ and $q(0) = 1$.
    pub fn q_from_h() -> Self {
        let mut q = Self::one();
        let h = Self::h();
        let two = Self::from_i64(2);
        let mut prec = 1usize;
        while prec <= K + 1 {
            // Newton step on f(q) = q^2 - h*q - 1 = 0: q_{next} = (q^2 + 1) / (2*q - h)
            let numer = q.mul_val(&q).add_val(&Self::one());
            let denom = two.mul_val(&q).sub_val(&h);
            let denom_inv = denom.try_inv().expect("2*q - h has constant term 2 != 0");
            q = numer.mul_val(&denom_inv);
            prec = prec.saturating_mul(2);
        }
        q
    }

    /// Expand a rational Laurent polynomial $P(q, q^{-1}) \in \mathbb{Q}\[q, q^{-1}\]$ into
    /// $\mathbb{Q}\[h\]/(h^{K+1})$ around $q = 1$ ($h = q - q^{-1}$).
    pub fn from_laurent_poly(poly: &LaurentPoly<BigRational>) -> Self {
        let q = Self::q_from_h();
        let q_inv = q.sub_val(&Self::h());
        poly.eval_with(&q, &q_inv, |c| Self::constant(c.clone()))
    }
}

impl<R: RingScalar, const K: usize> fmt::Display for TruncatedJet<R, K> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.coeffs.is_empty() {
            return write!(f, "0 + O(h^{})", K + 1);
        }
        let mut first = true;
        for (deg, c) in self.coeffs.iter().enumerate() {
            if c.is_zero() {
                continue;
            }
            if !first {
                write!(f, " + ")?;
            }
            first = false;
            match deg {
                0 => write!(f, "{c}")?,
                1 if c.is_one() => write!(f, "h")?,
                1 => write!(f, "({c})*h")?,
                d if c.is_one() => write!(f, "h^{d}")?,
                d => write!(f, "({c})*h^{d}")?,
            }
        }
        write!(f, " + O(h^{})", K + 1)
    }
}

impl<R: RingScalar, const K: usize> RingScalar for TruncatedJet<R, K> {
    fn zero() -> Self {
        Self::zero_jet()
    }
    fn one() -> Self {
        Self::constant(R::one())
    }
    fn from_i64(n: i64) -> Self {
        Self::constant(R::from_i64(n))
    }
    fn is_zero(&self) -> bool {
        self.coeffs.is_empty()
    }
    fn neg_val(&self) -> Self {
        Self::normalize(self.coeffs.iter().map(RingScalar::neg_val).collect())
    }
    fn add_val(&self, rhs: &Self) -> Self {
        let len = self.coeffs.len().max(rhs.coeffs.len()).min(K + 1);
        let mut out = Vec::with_capacity(len);
        for i in 0..len {
            out.push(self.coeff(i).add_val(&rhs.coeff(i)));
        }
        Self::normalize(out)
    }
    fn mul_val(&self, rhs: &Self) -> Self {
        if self.is_zero() || rhs.is_zero() {
            return Self::zero_jet();
        }
        let max_deg = (self.coeffs.len() + rhs.coeffs.len() - 2).min(K);
        let mut out = vec![R::zero(); max_deg + 1];
        for (i, c1) in self.coeffs.iter().enumerate() {
            if c1.is_zero() {
                continue;
            }
            for (j, c2) in rhs.coeffs.iter().enumerate() {
                if i + j > K {
                    break;
                }
                if !c2.is_zero() {
                    out[i + j] = out[i + j].add_val(&c1.mul_val(c2));
                }
            }
        }
        Self::normalize(out)
    }
    fn try_inv(&self) -> Option<Self> {
        let c0_inv = self.coeff(0).try_inv()?;
        // Solve self * inv = 1 mod h^{K+1} recursively:
        // inv[0] = c0^{-1}; inv[m] = -c0^{-1} * sum_{j=1..=m} self[j] * inv[m - j].
        let mut inv = vec![R::zero(); K + 1];
        inv[0] = c0_inv.clone();
        for m in 1..=K {
            let mut acc = R::zero();
            for j in 1..=m {
                let sj = self.coeff(j);
                if !sj.is_zero() && !inv[m - j].is_zero() {
                    acc = acc.add_val(&sj.mul_val(&inv[m - j]));
                }
            }
            inv[m] = c0_inv.mul_val(&acc).neg_val();
        }
        Some(Self::normalize(inv))
    }
}

/// Convenience helper for rational numbers `num / den`.
pub fn rat(num: i64, den: i64) -> BigRational {
    assert!(den != 0, "rational denominator must be non-zero");
    let r = BigRational::new(BigInt::from(num), BigInt::from(den));
    if r.denom().is_negative() {
        BigRational::new(-r.numer(), -r.denom())
    } else {
        r
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn laurent_poly_ring_identities_and_exact_division() {
        type L = LaurentPoly<i64>;
        let q = L::q();
        let qi = L::q_inv();
        let h = L::h();
        assert_eq!(&q * &qi, L::one());
        assert_eq!(L::q_int(3), L::from_terms([(-2, 1), (0, 1), (2, 1)]));

        let prod = &(&h * &h) + &L::from_i64(4);
        let delta = L::delta_two();
        assert_eq!(prod, &delta * &delta);
        assert_eq!(prod.try_div_exact(&delta), Some(delta));
    }

    #[test]
    fn truncated_jet_inversion_and_laurent_expansion() {
        type J = TruncatedJet<BigRational, 8>;
        let q = J::q_from_h();
        let q_inv = q.try_inv().unwrap();
        assert_eq!(q.mul_val(&q_inv), J::one());
        assert_eq!(q.sub_val(&q_inv), J::h());

        let q3 = LaurentPoly::<BigRational>::q_int(3);
        let jet_q3 = J::from_laurent_poly(&q3);
        // [3]_q = q^2 + 1 + q^{-2} = (q - q^{-1})^2 + 3 = 3 + h^2 exactly!
        let expected = J::from_coeffs(vec![rat(3, 1), rat(0, 1), rat(1, 1)]);
        assert_eq!(jet_q3, expected);
    }
}
