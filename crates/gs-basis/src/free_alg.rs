//! Free associative unital algebra $R\langle G \rangle$ over an ordered alphabet $G$
//! and commutative coefficient ring $R$.

use std::collections::BTreeMap;
use std::fmt;
use std::ops::{Add, Mul, Neg, Sub};

use serde::{Deserialize, Serialize};

use crate::order::MonomialOrder;
pub use crate::order::Word;
use crate::scalar::RingScalar;

/// Element of the free associative unital algebra $R\langle G \rangle$, stored as a canonical
/// zero-pruned map from words $w \in G^*$ to non-zero coefficients in $R$.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct FreeAlg<G: Ord, R> {
    terms: BTreeMap<Word<G>, R>,
}

impl<G: Ord + Clone, R: RingScalar> FreeAlg<G, R> {
    /// Additive identity $0$.
    pub fn zero() -> Self {
        Self {
            terms: BTreeMap::new(),
        }
    }

    /// Multiplicative identity $\mathbf{1}$ (empty word `[]` with coefficient `1`).
    pub fn one() -> Self {
        Self::scalar(R::one())
    }

    /// Scalar multiple $c \cdot \mathbf{1}$ of the empty word.
    pub fn scalar(c: R) -> Self {
        let mut terms = BTreeMap::new();
        if !c.is_zero() {
            terms.insert(Vec::new(), c);
        }
        Self { terms }
    }

    /// Single generator $1 \cdot g$.
    pub fn generator(g: G) -> Self {
        Self::word(vec![g])
    }

    /// Monic word $1 \cdot w$.
    pub fn word(w: Word<G>) -> Self {
        Self::term(w, R::one())
    }

    /// Single term $c \cdot w$.
    pub fn term(w: Word<G>, coeff: R) -> Self {
        let mut terms = BTreeMap::new();
        if !coeff.is_zero() {
            terms.insert(w, coeff);
        }
        Self { terms }
    }

    /// Build from `(word, coeff)` pairs, combining duplicates and pruning zero coefficients.
    pub fn from_terms<I: IntoIterator<Item = (Word<G>, R)>>(iter: I) -> Self {
        let mut terms: BTreeMap<Word<G>, R> = BTreeMap::new();
        for (w, c) in iter {
            if c.is_zero() {
                continue;
            }
            if let Some(existing) = terms.get_mut(&w) {
                let sum = existing.add_val(&c);
                if sum.is_zero() {
                    terms.remove(&w);
                } else {
                    *existing = sum;
                }
            } else {
                terms.insert(w, c);
            }
        }
        Self { terms }
    }

    /// Returns `true` iff `self == 0`.
    pub fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    /// Number of non-zero monomial terms in support.
    pub fn num_terms(&self) -> usize {
        self.terms.len()
    }

    /// Non-zero `(word, coeff)` map.
    pub fn terms(&self) -> &BTreeMap<Word<G>, R> {
        &self.terms
    }

    /// Coefficient of word `w` (`0` if absent).
    pub fn coeff(&self, w: &[G]) -> R {
        self.terms.get(w).cloned().unwrap_or_else(R::zero)
    }

    /// Maximum word length in support (`0` if zero or scalar).
    pub fn max_word_len(&self) -> usize {
        self.terms.keys().map(Vec::len).max().unwrap_or(0)
    }

    /// Maximum filtration degree in support with respect to `order`.
    pub fn max_filtration_degree<O: MonomialOrder<G>>(&self, order: &O) -> usize {
        self.terms
            .keys()
            .map(|w| order.filtration_degree(w))
            .max()
            .unwrap_or(0)
    }

    /// Scale all coefficients by `s`.
    pub fn scale(&self, s: &R) -> Self {
        if s.is_zero() {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        for (w, c) in &self.terms {
            let prod = c.mul_val(s);
            if !prod.is_zero() {
                terms.insert(w.clone(), prod);
            }
        }
        Self { terms }
    }

    /// Two-sided context multiplication `scale * left * self * right`.
    pub fn bimul_words(&self, left: &[G], right: &[G], scale: &R) -> Self {
        if scale.is_zero() || self.is_zero() {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        for (w, c) in &self.terms {
            let prod = c.mul_val(scale);
            if prod.is_zero() {
                continue;
            }
            let mut full = Vec::with_capacity(left.len() + w.len() + right.len());
            full.extend_from_slice(left);
            full.extend_from_slice(w);
            full.extend_from_slice(right);
            terms.insert(full, prod);
        }
        Self { terms }
    }

    /// Map coefficients along a ring homomorphism `R -> S`.
    pub fn map_scalars<S: RingScalar, F: Fn(&R) -> S>(&self, f: F) -> FreeAlg<G, S> {
        let mut terms = BTreeMap::new();
        for (w, c) in &self.terms {
            let sc = f(c);
            if !sc.is_zero() {
                terms.insert(w.clone(), sc);
            }
        }
        FreeAlg { terms }
    }

    /// Leading `(word, coeff)` pair with respect to `order`, or `None` if `self == 0`.
    pub fn leading_term<O: MonomialOrder<G>>(&self, order: &O) -> Option<(&[G], &R)> {
        self.terms
            .iter()
            .max_by(|(w1, _), (w2, _)| order.cmp_words(w1, w2))
            .map(|(w, c)| (w.as_slice(), c))
    }

    /// Leading monomial $\operatorname{lm}(f)$ with respect to `order`.
    pub fn leading_monomial<O: MonomialOrder<G>>(&self, order: &O) -> Option<&[G]> {
        self.leading_term(order).map(|(w, _)| w)
    }

    /// Leading coefficient $\operatorname{lc}(f)$ with respect to `order`.
    pub fn leading_coeff<O: MonomialOrder<G>>(&self, order: &O) -> Option<&R> {
        self.leading_term(order).map(|(_, c)| c)
    }

    /// Add `scale * rhs` into `self` in-place.
    pub fn add_scaled_assign(&mut self, rhs: &Self, scale: &R) {
        if scale.is_zero() || rhs.is_zero() {
            return;
        }
        for (w, c) in &rhs.terms {
            let delta = c.mul_val(scale);
            if delta.is_zero() {
                continue;
            }
            if let Some(existing) = self.terms.get_mut(w) {
                let sum = existing.add_val(&delta);
                if sum.is_zero() {
                    self.terms.remove(w);
                } else {
                    *existing = sum;
                }
            } else {
                self.terms.insert(w.clone(), delta);
            }
        }
    }

    /// Binary exponentiation `self^exp` in $R\langle G \rangle$.
    pub fn pow_u32(&self, mut exp: u32) -> Self {
        let mut base = self.clone();
        let mut acc = Self::one();
        while exp > 0 {
            if exp & 1 == 1 {
                acc = &acc * &base;
            }
            exp >>= 1;
            if exp > 0 {
                base = &base * &base;
            }
        }
        acc
    }
}

impl<G: Ord + fmt::Display, R: RingScalar> fmt::Display for FreeAlg<G, R> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.terms.is_empty() {
            return write!(f, "0");
        }
        let mut first = true;
        for (w, c) in &self.terms {
            if !first {
                write!(f, " + ")?;
            }
            first = false;
            if w.is_empty() {
                write!(f, "{c}")?;
            } else {
                if !c.is_one() {
                    write!(f, "({c})*")?;
                }
                for (idx, g) in w.iter().enumerate() {
                    if idx > 0 {
                        write!(f, "·")?;
                    }
                    write!(f, "g{g}")?;
                }
            }
        }
        Ok(())
    }
}

impl<G: Ord + Clone, R: RingScalar> Add for FreeAlg<G, R> {
    type Output = Self;
    fn add(mut self, rhs: Self) -> Self::Output {
        self.add_scaled_assign(&rhs, &R::one());
        self
    }
}

impl<G: Ord + Clone, R: RingScalar> Add<&FreeAlg<G, R>> for &FreeAlg<G, R> {
    type Output = FreeAlg<G, R>;
    fn add(self, rhs: &FreeAlg<G, R>) -> Self::Output {
        let mut out = self.clone();
        out.add_scaled_assign(rhs, &R::one());
        out
    }
}

impl<G: Ord + Clone, R: RingScalar> Sub for FreeAlg<G, R> {
    type Output = Self;
    fn sub(mut self, rhs: Self) -> Self::Output {
        self.add_scaled_assign(&rhs, &R::one().neg_val());
        self
    }
}

impl<G: Ord + Clone, R: RingScalar> Sub<&FreeAlg<G, R>> for &FreeAlg<G, R> {
    type Output = FreeAlg<G, R>;
    fn sub(self, rhs: &FreeAlg<G, R>) -> Self::Output {
        let mut out = self.clone();
        out.add_scaled_assign(rhs, &R::one().neg_val());
        out
    }
}

impl<G: Ord + Clone, R: RingScalar> Neg for FreeAlg<G, R> {
    type Output = Self;
    fn neg(self) -> Self::Output {
        self.scale(&R::one().neg_val())
    }
}

impl<G: Ord + Clone, R: RingScalar> Neg for &FreeAlg<G, R> {
    type Output = FreeAlg<G, R>;
    fn neg(self) -> Self::Output {
        self.scale(&R::one().neg_val())
    }
}

impl<G: Ord + Clone, R: RingScalar> Mul for FreeAlg<G, R> {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self::Output {
        &self * &rhs
    }
}

impl<G: Ord + Clone, R: RingScalar> Mul<&FreeAlg<G, R>> for &FreeAlg<G, R> {
    type Output = FreeAlg<G, R>;
    fn mul(self, rhs: &FreeAlg<G, R>) -> Self::Output {
        if self.is_zero() || rhs.is_zero() {
            return FreeAlg::zero();
        }
        let mut terms: BTreeMap<Word<G>, R> = BTreeMap::new();
        for (w1, c1) in &self.terms {
            for (w2, c2) in &rhs.terms {
                let prod = c1.mul_val(c2);
                if prod.is_zero() {
                    continue;
                }
                let mut w = Vec::with_capacity(w1.len() + w2.len());
                w.extend_from_slice(w1);
                w.extend_from_slice(w2);
                if let Some(existing) = terms.get_mut(&w) {
                    let sum = existing.add_val(&prod);
                    if sum.is_zero() {
                        terms.remove(&w);
                    } else {
                        *existing = sum;
                    }
                } else {
                    terms.insert(w, prod);
                }
            }
        }
        FreeAlg { terms }
    }
}
