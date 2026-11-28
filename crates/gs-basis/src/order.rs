//! Admissible monomial well-orders on free monoids $G^*$.
//!
//! A total order $<$ on words $G^*$ is **admissible** (a monomial order) if:
//! 1. $1 \le w$ for every word $w \in G^*$ (well-foundedness with empty word minimal), and
//! 2. $u < v \implies a u b < a v b$ for all context words $a, b \in G^*$ (two-sided
//!    multiplication invariance).

use std::cmp::Ordering;
use std::collections::BTreeMap;
use std::fmt;

use serde::{Deserialize, Serialize};

/// A word (monomial) in the free monoid $G^*$ over generator alphabet $G$.
pub type Word<G> = Vec<G>;

/// Admissible total order on words `[G]` in a free associative monoid.
pub trait MonomialOrder<G>: Clone + fmt::Debug {
    /// Total admissible comparison between `a` and `b`.
    fn cmp_words(&self, a: &[G], b: &[G]) -> Ordering;

    /// Filtration / weighted degree of a word (defaults to word length `w.len()`).
    fn filtration_degree(&self, w: &[G]) -> usize {
        w.len()
    }
}

/// Degree-lexicographic order (`DegLex`): shorter words first; ties broken left-to-right by `G::cmp`.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, Serialize, Deserialize)]
pub struct DegLex;

impl<G: Ord> MonomialOrder<G> for DegLex {
    fn cmp_words(&self, a: &[G], b: &[G]) -> Ordering {
        a.len().cmp(&b.len()).then_with(|| a.cmp(b))
    }
}

/// Degree-reverse-lexicographic order (`DegRevLex`): shorter words first; ties broken
/// right-to-left with inverted generator comparison (`b[k].cmp(&a[k])` at the rightmost
/// differing index `k`). Well-founded on every finite generator alphabet.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, Serialize, Deserialize)]
pub struct DegRevLex;

impl<G: Ord> MonomialOrder<G> for DegRevLex {
    fn cmp_words(&self, a: &[G], b: &[G]) -> Ordering {
        match a.len().cmp(&b.len()) {
            Ordering::Equal => {
                for (x, y) in a.iter().rev().zip(b.iter().rev()) {
                    if x != y {
                        return y.cmp(x);
                    }
                }
                Ordering::Equal
            }
            ord => ord,
        }
    }
}

/// Degree-right-lexicographic order (`DegRightLex`): shorter words first; ties broken
/// right-to-left by `G::cmp` (`a[k].cmp(&b[k])` at the rightmost differing index `k`).
/// Well-founded on any well-ordered alphabet `G` (even infinite).
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, Serialize, Deserialize)]
pub struct DegRightLex;

impl<G: Ord> MonomialOrder<G> for DegRightLex {
    fn cmp_words(&self, a: &[G], b: &[G]) -> Ordering {
        match a.len().cmp(&b.len()) {
            Ordering::Equal => {
                for (x, y) in a.iter().rev().zip(b.iter().rev()) {
                    if x != y {
                        return x.cmp(y);
                    }
                }
                Ordering::Equal
            }
            ord => ord,
        }
    }
}

/// Positive-weight degree-lexicographic order (`WeightedDegLex`): compares total strictly
/// positive generator weight $\sum_i w(g_i)$ (`w(g) >= 1`), breaking ties by `DegLex`.
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub struct WeightedDegLex<G: Ord> {
    weights: BTreeMap<G, usize>,
    default_weight: usize,
}

impl<G: Ord> WeightedDegLex<G> {
    /// Create a weighted degree-lexicographic order. All weights (and `default_weight`) must
    /// be strictly positive (`>= 1`) to guarantee well-foundedness (`1 < g` for all `g`).
    pub fn new(weights: BTreeMap<G, usize>, default_weight: usize) -> Self {
        assert!(
            default_weight >= 1,
            "default generator weight must be >= 1 for admissibility"
        );
        for w in weights.values() {
            assert!(
                *w >= 1,
                "every generator weight must be >= 1 for admissibility"
            );
        }
        Self {
            weights,
            default_weight,
        }
    }

    /// Weight assigned to generator `g`.
    pub fn weight_of(&self, g: &G) -> usize {
        self.weights.get(g).copied().unwrap_or(self.default_weight)
    }

    /// Total weight of a word.
    pub fn word_weight(&self, w: &[G]) -> usize {
        w.iter().map(|g| self.weight_of(g)).sum()
    }
}

impl<G: Ord + Clone + fmt::Debug> MonomialOrder<G> for WeightedDegLex<G> {
    fn cmp_words(&self, a: &[G], b: &[G]) -> Ordering {
        self.word_weight(a)
            .cmp(&self.word_weight(b))
            .then_with(|| a.len().cmp(&b.len()))
            .then_with(|| a.cmp(b))
    }

    fn filtration_degree(&self, w: &[G]) -> usize {
        self.word_weight(w)
    }
}

/// Runtime-selectable admissible monomial order over alphabet `G`.
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum OrderKind<G: Ord> {
    /// Standard degree-lexicographic order.
    DegLex,
    /// Standard degree-reverse-lexicographic order (for finite alphabets).
    DegRevLex,
    /// Degree-right-lexicographic order.
    DegRightLex,
    /// Positive-weight degree-lexicographic order.
    WeightedDegLex(WeightedDegLex<G>),
}

impl<G: Ord + Clone + fmt::Debug> MonomialOrder<G> for OrderKind<G> {
    fn cmp_words(&self, a: &[G], b: &[G]) -> Ordering {
        match self {
            OrderKind::DegLex => DegLex.cmp_words(a, b),
            OrderKind::DegRevLex => DegRevLex.cmp_words(a, b),
            OrderKind::DegRightLex => DegRightLex.cmp_words(a, b),
            OrderKind::WeightedDegLex(w) => w.cmp_words(a, b),
        }
    }

    fn filtration_degree(&self, w: &[G]) -> usize {
        match self {
            OrderKind::WeightedDegLex(ord) => ord.filtration_degree(w),
            _ => w.len(),
        }
    }
}

/// Verify admissibility axioms (`[] <= w` and `u < v => a u b < a v b`) across a sample of words.
pub fn verify_admissibility_sample<G: Clone + Eq, O: MonomialOrder<G>>(
    order: &O,
    words: &[Vec<G>],
) -> bool {
    for w in words {
        let empty_cmp = order.cmp_words(&[], w);
        if w.is_empty() {
            if empty_cmp != Ordering::Equal {
                return false;
            }
        } else if empty_cmp != Ordering::Less {
            return false;
        }
    }
    for u in words {
        for v in words {
            if order.cmp_words(u, v) == Ordering::Less {
                for a in words {
                    for b in words {
                        let mut aub = Vec::with_capacity(a.len() + u.len() + b.len());
                        aub.extend_from_slice(a);
                        aub.extend_from_slice(u);
                        aub.extend_from_slice(b);

                        let mut avb = Vec::with_capacity(a.len() + v.len() + b.len());
                        avb.extend_from_slice(a);
                        avb.extend_from_slice(v);
                        avb.extend_from_slice(b);

                        if order.cmp_words(&aub, &avb) != Ordering::Less {
                            return false;
                        }
                    }
                }
            }
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn all_orders_satisfy_two_sided_admissibility() {
        let mut sample: Vec<Vec<usize>> = vec![vec![]];
        for i in 0..3 {
            sample.push(vec![i]);
            for j in 0..3 {
                sample.push(vec![i, j]);
            }
        }
        assert!(verify_admissibility_sample(&DegLex, &sample));
        assert!(verify_admissibility_sample(&DegRevLex, &sample));
        assert!(verify_admissibility_sample(&DegRightLex, &sample));

        let mut weights = BTreeMap::new();
        weights.insert(0usize, 1usize);
        weights.insert(1usize, 3usize);
        weights.insert(2usize, 5usize);
        let w_ord = WeightedDegLex::new(weights, 2);
        assert!(verify_admissibility_sample(&w_ord, &sample));
    }
}
