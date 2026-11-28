//! Exact dyadic rationals $\mathbb{Z}\[\frac{1}{2}\]$ and dense-window dyadic Laurent
//! polynomials $\mathbb{Z}\[\frac{1}{2}\]\[q, q^{-1}\]$ with zero Euclidean GCD overhead.
//!
//! In computations where every non-integer scalar factor is a power of $2$ (such as $\pm\frac{1}{2}$),
//! general rational arithmetic (`BigRational`) wastes almost all of its runtime computing
//! $\gcd(\text{num}, \text{den})$ on every addition. Representing scalars as `mantissa * 2^exp2`
//! with odd `mantissa` reduces normalization to a single hardware `trailing_zeros` bit scan,
//! while [`DyadicLaurent`] factors a shared `2^exp2` shift out of a contiguous `Vec<BigInt>`
//! exponent window so multiplying by $h = q - q^{-1}$ and scaling by $2^k$ require zero
//! hash-map allocations and zero GCDs.

use std::cmp::Ordering;
use std::fmt;
use std::ops::{Add, Mul, Neg, Sub};

use num_bigint::BigInt;
use num_integer::Integer;
use num_rational::BigRational;
use num_traits::Signed;
use serde::{Deserialize, Deserializer, Serialize, Serializer};

use crate::scalar::RingScalar;

/// Exact element $\text{mantissa} \cdot 2^{\text{exp2}} \in \mathbb{Z}\[\frac{1}{2}\]$,
/// canonically normalized so `mantissa == 0 => exp2 == 0` and any non-zero `mantissa` is odd.
#[derive(Clone, PartialEq, Eq, Hash, Debug)]
pub struct DyadicScalar {
    mantissa: BigInt,
    exp2: i32,
}

impl Serialize for DyadicScalar {
    fn serialize<S: Serializer>(&self, serializer: S) -> Result<S::Ok, S::Error> {
        (self.mantissa.to_string(), self.exp2).serialize(serializer)
    }
}

impl<'de> Deserialize<'de> for DyadicScalar {
    fn deserialize<D: Deserializer<'de>>(deserializer: D) -> Result<Self, D::Error> {
        let (m_str, exp2): (String, i32) = Deserialize::deserialize(deserializer)?;
        let m: BigInt = m_str.parse().map_err(serde::de::Error::custom)?;
        Ok(Self::new(m, exp2))
    }
}

impl DyadicScalar {
    /// Construct and normalize `mantissa * 2^exp2`.
    pub fn new(mut mantissa: BigInt, mut exp2: i32) -> Self {
        if mantissa.is_zero() {
            return Self {
                mantissa,
                exp2: 0,
            };
        }
        if let Some(tz) = mantissa.trailing_zeros() {
            if tz > 0 {
                mantissa >>= tz;
                exp2 = exp2
                    .checked_add(i32::try_from(tz).expect("trailing_zeros exceeds i32::MAX"))
                    .expect("DyadicScalar exp2 overflow");
            }
        }
        Self { mantissa, exp2 }
    }

    /// Construct `m * 2^exp2` from an `i64` mantissa.
    pub fn from_i64_pow2(m: i64, exp2: i32) -> Self {
        Self::new(BigInt::from(m), exp2)
    }

    /// Exact dyadic scalar $\frac{1}{2} = 1 \cdot 2^{-1}$.
    pub fn half() -> Self {
        Self {
            mantissa: BigInt::from(1),
            exp2: -1,
        }
    }

    /// Canonical odd mantissa (`0` iff scalar is zero).
    pub fn mantissa(&self) -> &BigInt {
        &self.mantissa
    }

    /// Power-of-two exponent (`0` when scalar is zero).
    pub fn exp2(&self) -> i32 {
        self.exp2
    }

    /// Multiply by $2^{\text{shift}}$ in $O(1)$ without touching `mantissa`.
    pub fn scale_pow2(&self, shift: i32) -> Self {
        if self.mantissa.is_zero() {
            Self::zero()
        } else {
            Self {
                mantissa: self.mantissa.clone(),
                exp2: self.exp2.checked_add(shift).expect("DyadicScalar exp2 overflow"),
            }
        }
    }

    /// Convert into an exact `BigRational`.
    pub fn to_big_rational(&self) -> BigRational {
        if self.mantissa.is_zero() {
            return <BigRational as RingScalar>::zero();
        }
        if self.exp2 >= 0 {
            BigRational::from_integer(&self.mantissa << (self.exp2 as usize))
        } else {
            let den = BigInt::from(1) << (self.exp2.unsigned_abs() as usize);
            BigRational::new_raw(self.mantissa.clone(), den)
        }
    }
}

impl Ord for DyadicScalar {
    fn cmp(&self, other: &Self) -> Ordering {
        if self == other {
            return Ordering::Equal;
        }
        let z = BigInt::from(0);
        if self.mantissa.is_zero() {
            return z.cmp(&other.mantissa);
        }
        if other.mantissa.is_zero() {
            return self.mantissa.cmp(&z);
        }
        if self.mantissa.is_positive() != other.mantissa.is_positive() {
            return if self.mantissa.is_positive() {
                Ordering::Greater
            } else {
                Ordering::Less
            };
        }
        let min_e = self.exp2.min(other.exp2);
        let lhs = &self.mantissa << ((self.exp2 - min_e) as usize);
        let rhs = &other.mantissa << ((other.exp2 - min_e) as usize);
        lhs.cmp(&rhs)
    }
}

impl PartialOrd for DyadicScalar {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl fmt::Display for DyadicScalar {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.mantissa.is_zero() {
            write!(f, "0")
        } else if self.exp2 >= 0 {
            let val = &self.mantissa << (self.exp2 as usize);
            write!(f, "{val}")
        } else {
            let den = BigInt::from(1) << (self.exp2.unsigned_abs() as usize);
            write!(f, "{}/{}", self.mantissa, den)
        }
    }
}

impl RingScalar for DyadicScalar {
    fn zero() -> Self {
        Self {
            mantissa: BigInt::from(0),
            exp2: 0,
        }
    }

    fn one() -> Self {
        Self {
            mantissa: BigInt::from(1),
            exp2: 0,
        }
    }

    fn from_i64(n: i64) -> Self {
        Self::new(BigInt::from(n), 0)
    }

    fn is_zero(&self) -> bool {
        self.mantissa.is_zero()
    }

    fn neg_val(&self) -> Self {
        Self {
            mantissa: -&self.mantissa,
            exp2: self.exp2,
        }
    }

    fn add_val(&self, rhs: &Self) -> Self {
        if self.is_zero() {
            return rhs.clone();
        }
        if rhs.is_zero() {
            return self.clone();
        }
        let min_e = self.exp2.min(rhs.exp2);
        let l_shift = (self.exp2 - min_e) as usize;
        let r_shift = (rhs.exp2 - min_e) as usize;
        let sum = (&self.mantissa << l_shift) + (&rhs.mantissa << r_shift);
        Self::new(sum, min_e)
    }

    fn mul_val(&self, rhs: &Self) -> Self {
        if self.is_zero() || rhs.is_zero() {
            return Self::zero();
        }
        // Product of two odd integers is already odd: zero trailing-zero scan needed!
        Self {
            mantissa: &self.mantissa * &rhs.mantissa,
            exp2: self
                .exp2
                .checked_add(rhs.exp2)
                .expect("DyadicScalar exp2 overflow"),
        }
    }

    fn try_inv(&self) -> Option<Self> {
        let one = BigInt::from(1);
        if self.mantissa == one {
            Some(Self {
                mantissa: one,
                exp2: -self.exp2,
            })
        } else if self.mantissa == -(&one) {
            Some(Self {
                mantissa: -one,
                exp2: -self.exp2,
            })
        } else {
            None
        }
    }

    fn try_div_exact(&self, rhs: &Self) -> Option<Self> {
        if rhs.is_zero() {
            return None;
        }
        if self.is_zero() {
            return Some(Self::zero());
        }
        let (q, r) = self.mantissa.div_rem(&rhs.mantissa);
        if r.is_zero() {
            Some(Self::new(q, self.exp2 - rhs.exp2))
        } else {
            None
        }
    }
}

/// Dense-window dyadic Laurent polynomial in $\mathbb{Z}\[\frac{1}{2}\]\[q, q^{-1}\]$,
/// stored as $2^{\text{exp2}} \sum_{k=0}^{\text{coeffs.len()}-1} \text{coeffs}\[k\]\, q^{\text{min\_exp} + k}$.
#[derive(Clone, PartialEq, Eq, Debug)]
pub struct DyadicLaurent {
    min_exp: i32,
    exp2: i32,
    coeffs: Vec<BigInt>,
}

impl Serialize for DyadicLaurent {
    fn serialize<S: Serializer>(&self, serializer: S) -> Result<S::Ok, S::Error> {
        let raw: Vec<(i32, String, i32)> = self
            .nonzero_terms()
            .into_iter()
            .map(|(e, m, e2)| (e, m.to_string(), e2))
            .collect();
        raw.serialize(serializer)
    }
}

impl<'de> Deserialize<'de> for DyadicLaurent {
    fn deserialize<D: Deserializer<'de>>(deserializer: D) -> Result<Self, D::Error> {
        let raw: Vec<(i32, String, i32)> = Deserialize::deserialize(deserializer)?;
        let mut acc = Self::zero_poly();
        for (e, m_str, e2) in raw {
            let m: BigInt = m_str.parse().map_err(serde::de::Error::custom)?;
            acc = acc.add_val(&Self::monomial(e, DyadicScalar::new(m, e2)));
        }
        Ok(acc)
    }
}

impl DyadicLaurent {
    fn from_raw(mut min_exp: i32, mut exp2: i32, mut coeffs: Vec<BigInt>) -> Self {
        // 1. Trim trailing zeros:
        while coeffs.last().map_or(false, RingScalar::is_zero) {
            coeffs.pop();
        }
        // 2. Trim leading zeros:
        let first_nz = coeffs.iter().position(|c| !c.is_zero());
        match first_nz {
            None => Self {
                min_exp: 0,
                exp2: 0,
                coeffs: Vec::new(),
            },
            Some(lead) => {
                if lead > 0 {
                    coeffs.drain(0..lead);
                    min_exp += lead as i32;
                }
                // 3. Factor out shared power of 2 across all non-zero coefficients:
                let min_tz = coeffs
                    .iter()
                    .filter(|c| !c.is_zero())
                    .filter_map(BigInt::trailing_zeros)
                    .min()
                    .unwrap_or(0);
                if min_tz > 0 {
                    let shift = min_tz as usize;
                    for c in &mut coeffs {
                        if !c.is_zero() {
                            *c >>= shift;
                        }
                    }
                    exp2 = exp2
                        .checked_add(min_tz as i32)
                        .expect("DyadicLaurent exp2 overflow");
                }
                Self {
                    min_exp,
                    exp2,
                    coeffs,
                }
            }
        }
    }

    /// Zero Laurent polynomial.
    pub fn zero_poly() -> Self {
        Self {
            min_exp: 0,
            exp2: 0,
            coeffs: Vec::new(),
        }
    }

    /// Constant polynomial from a [`DyadicScalar`].
    pub fn constant(c: DyadicScalar) -> Self {
        if c.is_zero() {
            Self::zero_poly()
        } else {
            Self {
                min_exp: 0,
                exp2: c.exp2,
                coeffs: vec![c.mantissa],
            }
        }
    }

    /// Single monomial `coeff * q^q_exp`.
    pub fn monomial(q_exp: i32, coeff: DyadicScalar) -> Self {
        if coeff.is_zero() {
            Self::zero_poly()
        } else {
            Self {
                min_exp: q_exp,
                exp2: coeff.exp2,
                coeffs: vec![coeff.mantissa],
            }
        }
    }

    /// Indeterminate $q$.
    pub fn q() -> Self {
        Self::monomial(1, DyadicScalar::one())
    }

    /// Inverse indeterminate $q^{-1}$.
    pub fn q_inv() -> Self {
        Self::monomial(-1, DyadicScalar::one())
    }

    /// Balanced Hecke parameter $h = q - q^{-1}$.
    pub fn h() -> Self {
        Self {
            min_exp: -1,
            exp2: 0,
            coeffs: vec![BigInt::from(-1), BigInt::from(0), BigInt::from(1)],
        }
    }

    /// Temperley–Lieb loop parameter $\delta = q + q^{-1}$.
    pub fn delta_two() -> Self {
        Self {
            min_exp: -1,
            exp2: 0,
            coeffs: vec![BigInt::from(1), BigInt::from(0), BigInt::from(1)],
        }
    }

    /// Minimum $q$-exponent with non-zero coefficient (`None` if zero).
    pub fn min_degree(&self) -> Option<i32> {
        if self.coeffs.is_empty() {
            None
        } else {
            Some(self.min_exp)
        }
    }

    /// Maximum $q$-exponent with non-zero coefficient (`None` if zero).
    pub fn max_degree(&self) -> Option<i32> {
        if self.coeffs.is_empty() {
            None
        } else {
            Some(self.min_exp + (self.coeffs.len() as i32) - 1)
        }
    }

    /// Count of non-zero monomials in support.
    pub fn num_nonzero_terms(&self) -> usize {
        self.coeffs.iter().filter(|c| !c.is_zero()).count()
    }

    /// Coefficient of $q^{\text{q\_exp}}$ as a normalized [`DyadicScalar`].
    pub fn coeff(&self, q_exp: i32) -> DyadicScalar {
        if self.coeffs.is_empty() || q_exp < self.min_exp {
            return DyadicScalar::zero();
        }
        let idx = (q_exp - self.min_exp) as usize;
        match self.coeffs.get(idx) {
            None => DyadicScalar::zero(),
            Some(c) if c.is_zero() => DyadicScalar::zero(),
            Some(c) => DyadicScalar::new(c.clone(), self.exp2),
        }
    }

    /// Return all non-zero terms as `(q_exp, odd_mantissa, term_exp2)` triples sorted by `q_exp`.
    pub fn nonzero_terms(&self) -> Vec<(i32, BigInt, i32)> {
        let mut out = Vec::with_capacity(self.num_nonzero_terms());
        for (idx, c) in self.coeffs.iter().enumerate() {
            if !c.is_zero() {
                let d = DyadicScalar::new(c.clone(), self.exp2);
                out.push((self.min_exp + idx as i32, d.mantissa, d.exp2));
            }
        }
        out
    }

    /// Scale by $2^{\text{shift}}$ in $O(1)$ without cloning or touching `BigInt` limbs.
    pub fn scale_pow2(&self, shift: i32) -> Self {
        if self.coeffs.is_empty() {
            Self::zero_poly()
        } else {
            Self {
                min_exp: self.min_exp,
                exp2: self.exp2.checked_add(shift).expect("DyadicLaurent exp2 overflow"),
                coeffs: self.coeffs.clone(),
            }
        }
    }

    /// Multiply by $h = q - q^{-1}$ via a single shift-and-subtract pass over the contiguous
    /// `Vec<BigInt>` buffer (zero convolution, zero hash-map allocations).
    pub fn mul_h(&self) -> Self {
        if self.coeffs.is_empty() {
            return Self::zero_poly();
        }
        let len = self.coeffs.len();
        let mut out = vec![BigInt::from(0); len + 2];
        for (k, c) in self.coeffs.iter().enumerate() {
            if !c.is_zero() {
                out[k + 2] += c;
                out[k] -= c;
            }
        }
        Self::from_raw(self.min_exp - 1, self.exp2, out)
    }

    /// Fast fused operation `(mantissa * 2^exp2_shift * h^h_pow) * self` avoiding `BigInt`
    /// multiplications whenever `mantissa` is `0`, `+1`, or `-1`.
    pub fn scale_dyadic_h_pow(&self, mantissa: i64, exp2_shift: i32, h_pow: u32) -> Self {
        if mantissa == 0 || self.coeffs.is_empty() {
            return Self::zero_poly();
        }
        let mut cur = self.clone();
        for _ in 0..h_pow {
            cur = cur.mul_h();
        }
        match mantissa {
            1 => cur.scale_pow2(exp2_shift),
            -1 => {
                for c in &mut cur.coeffs {
                    if !c.is_zero() {
                        *c = -&*c;
                    }
                }
                cur.exp2 += exp2_shift;
                cur
            }
            m => {
                let tz = m.trailing_zeros() as i32;
                let odd_m = m >> tz;
                if odd_m == 1 {
                    cur.scale_pow2(exp2_shift + tz)
                } else if odd_m == -1 {
                    for c in &mut cur.coeffs {
                        if !c.is_zero() {
                            *c = -&*c;
                        }
                    }
                    cur.exp2 += exp2_shift + tz;
                    cur
                } else {
                    let bm = BigInt::from(odd_m);
                    for c in &mut cur.coeffs {
                        if !c.is_zero() {
                            *c *= &bm;
                        }
                    }
                    cur.exp2 += exp2_shift + tz;
                    cur
                }
            }
        }
    }
}

impl fmt::Display for DyadicLaurent {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let terms = self.nonzero_terms();
        if terms.is_empty() {
            return write!(f, "0");
        }
        for (i, (q_exp, mant, e2)) in terms.iter().rev().enumerate() {
            if i > 0 {
                write!(f, " + ")?;
            }
            let sc = DyadicScalar {
                mantissa: mant.clone(),
                exp2: *e2,
            };
            match *q_exp {
                0 => write!(f, "{sc}")?,
                1 if sc.is_one() => write!(f, "q")?,
                1 => write!(f, "({sc})*q")?,
                e if sc.is_one() => write!(f, "q^{e}")?,
                e => write!(f, "({sc})*q^{e}")?,
            }
        }
        Ok(())
    }
}

impl RingScalar for DyadicLaurent {
    fn zero() -> Self {
        Self::zero_poly()
    }

    fn one() -> Self {
        Self::constant(DyadicScalar::one())
    }

    fn from_i64(n: i64) -> Self {
        Self::constant(DyadicScalar::from_i64(n))
    }

    fn is_zero(&self) -> bool {
        self.coeffs.is_empty()
    }

    fn neg_val(&self) -> Self {
        if self.coeffs.is_empty() {
            Self::zero_poly()
        } else {
            Self {
                min_exp: self.min_exp,
                exp2: self.exp2,
                coeffs: self.coeffs.iter().map(|c| -c).collect(),
            }
        }
    }

    fn add_val(&self, rhs: &Self) -> Self {
        if self.coeffs.is_empty() {
            return rhs.clone();
        }
        if rhs.coeffs.is_empty() {
            return self.clone();
        }
        let min_q = self.min_exp.min(rhs.min_exp);
        let max_q = self.max_degree().unwrap().max(rhs.max_degree().unwrap());
        let len = (max_q - min_q + 1) as usize;
        let min_e2 = self.exp2.min(rhs.exp2);
        let l_shift = (self.exp2 - min_e2) as usize;
        let r_shift = (rhs.exp2 - min_e2) as usize;

        let mut out = vec![BigInt::from(0); len];
        let l_off = (self.min_exp - min_q) as usize;
        for (i, c) in self.coeffs.iter().enumerate() {
            if !c.is_zero() {
                if l_shift == 0 {
                    out[l_off + i] += c;
                } else {
                    out[l_off + i] += c << l_shift;
                }
            }
        }
        let r_off = (rhs.min_exp - min_q) as usize;
        for (i, c) in rhs.coeffs.iter().enumerate() {
            if !c.is_zero() {
                if r_shift == 0 {
                    out[r_off + i] += c;
                } else {
                    out[r_off + i] += c << r_shift;
                }
            }
        }
        Self::from_raw(min_q, min_e2, out)
    }

    fn mul_val(&self, rhs: &Self) -> Self {
        if self.coeffs.is_empty() || rhs.coeffs.is_empty() {
            return Self::zero_poly();
        }
        let mut out = vec![BigInt::from(0); self.coeffs.len() + rhs.coeffs.len() - 1];
        for (i, c1) in self.coeffs.iter().enumerate() {
            if c1.is_zero() {
                continue;
            }
            for (j, c2) in rhs.coeffs.iter().enumerate() {
                if !c2.is_zero() {
                    out[i + j] += c1 * c2;
                }
            }
        }
        Self::from_raw(
            self.min_exp + rhs.min_exp,
            self.exp2 + rhs.exp2,
            out,
        )
    }

    fn try_inv(&self) -> Option<Self> {
        if self.coeffs.len() != 1 {
            return None;
        }
        let sc = DyadicScalar::new(self.coeffs[0].clone(), self.exp2);
        let inv_sc = sc.try_inv()?;
        Some(Self::monomial(-self.min_exp, inv_sc))
    }
}

impl Add for DyadicLaurent {
    type Output = Self;
    fn add(self, rhs: Self) -> Self::Output {
        self.add_val(&rhs)
    }
}

impl Add<&DyadicLaurent> for &DyadicLaurent {
    type Output = DyadicLaurent;
    fn add(self, rhs: &DyadicLaurent) -> Self::Output {
        self.add_val(rhs)
    }
}

impl Sub for DyadicLaurent {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self::Output {
        self.sub_val(&rhs)
    }
}

impl Sub<&DyadicLaurent> for &DyadicLaurent {
    type Output = DyadicLaurent;
    fn sub(self, rhs: &DyadicLaurent) -> Self::Output {
        self.sub_val(rhs)
    }
}

impl Mul for DyadicLaurent {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self::Output {
        self.mul_val(&rhs)
    }
}

impl Mul<&DyadicLaurent> for &DyadicLaurent {
    type Output = DyadicLaurent;
    fn mul(self, rhs: &DyadicLaurent) -> Self::Output {
        self.mul_val(rhs)
    }
}

impl Neg for DyadicLaurent {
    type Output = Self;
    fn neg(self) -> Self::Output {
        self.neg_val()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scalar::{rat, LaurentPoly};

    #[test]
    fn dyadic_laurent_matches_rational_laurent_without_gcd() {
        let h_d = DyadicLaurent::h();
        let half_minus_h = h_d.scale_dyadic_h_pow(-1, -1, 0); // -1/2 * h
        let p_d = &(&DyadicLaurent::one() + &half_minus_h) * &h_d.mul_h();

        type LR = LaurentPoly<BigRational>;
        let h_r = LR::h();
        let half_minus_h_r = h_r.scale(&rat(-1, 2));
        let p_r = &(&LR::one() + &half_minus_h_r) * &(&h_r * &h_r);

        assert_eq!(p_d.min_degree(), p_r.min_degree());
        assert_eq!(p_d.max_degree(), p_r.max_degree());
        for exp in -6..=6 {
            assert_eq!(p_d.coeff(exp).to_big_rational(), p_r.coeff(exp));
        }
    }
}
