//! Dynamic Buchberger–Shirshov engine and unified [`NormalFormBasis`] trait.
//!
//! Implements non-commutative Gröbner–Shirshov completion (Shirshov 1962, Bergman 1978,
//! Bokut–Chen 2014) over any `RingScalar` and admissible `MonomialOrder`.

use std::cmp::Ordering;
use std::collections::BTreeMap;
use std::fmt;
use std::hash::Hash;

use rustc_hash::FxHashMap;
use serde::{Deserialize, Serialize};

use crate::free_alg::{FreeAlg, Word};
use crate::order::MonomialOrder;
use crate::scalar::RingScalar;

/// Unified normal-form basis interface shared by dynamic Buchberger–Shirshov bases and
/// specialized combinatorial backends (`BokutShiaoHecke`, `TemperleyLiebBasis`).
pub trait NormalFormBasis<R: RingScalar, G: Ord + Clone = usize> {
    /// Reduce a single word $w \in G^*$ to its normal form in $R\langle G \rangle / I$.
    fn reduce_word(&self, word: &[G]) -> FreeAlg<G, R>;

    /// Reduce an arbitrary free-algebra element by $R$-linearity.
    fn reduce(&self, elem: &FreeAlg<G, R>) -> FreeAlg<G, R> {
        let mut acc = FreeAlg::zero();
        for (w, c) in elem.terms() {
            let red = self.reduce_word(w);
            acc.add_scaled_assign(&red, c);
        }
        acc
    }

    /// Multiply two elements and reduce their product to normal form.
    fn multiply_reduced(&self, a: &FreeAlg<G, R>, b: &FreeAlg<G, R>) -> FreeAlg<G, R> {
        self.reduce(&(a * b))
    }
}

/// A monic rewrite rule `lhs -> rhs` representing the relation `lhs - rhs = 0`,
/// where every monomial in `rhs` is strictly smaller than `lhs` under the ambient order.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct RewriteRule<G: Ord, R> {
    /// Non-empty monic leading word.
    pub lhs: Word<G>,
    /// Lower-order tail `rhs` satisfying `m < lhs` for every `m` in `rhs.terms()`.
    pub rhs: FreeAlg<G, R>,
}

impl<G: Ord + Clone, R: RingScalar> RewriteRule<G, R> {
    /// Construct an explicit rule after checking `lhs` is non-empty and `m < lhs` for all `m` in `rhs`.
    pub fn try_new<O: MonomialOrder<G>>(
        lhs: Word<G>,
        rhs: FreeAlg<G, R>,
        order: &O,
    ) -> Result<Self, ShirshovError> {
        if lhs.is_empty() {
            return Err(ShirshovError::ScalarUnitRelation);
        }
        for m in rhs.terms().keys() {
            if order.cmp_words(m, &lhs) != Ordering::Less {
                return Err(ShirshovError::InvalidRuleOrientation);
            }
        }
        Ok(Self { lhs, rhs })
    }

    /// Orient a non-zero relation $f \in R\langle G \rangle$ into a monic `RewriteRule` by
    /// dividing all lower terms cleanly by $\operatorname{lc}(f)$.
    pub fn from_relation<O: MonomialOrder<G>>(
        rel: &FreeAlg<G, R>,
        order: &O,
    ) -> Result<Self, ShirshovError> {
        let (lm_slice, lc) = rel
            .leading_term(order)
            .ok_or(ShirshovError::ZeroRelation)?;
        if lm_slice.is_empty() {
            return Err(ShirshovError::ScalarUnitRelation);
        }
        let lhs = lm_slice.to_vec();
        let mut rhs_terms = BTreeMap::new();
        for (w, c) in rel.terms() {
            if w.as_slice() == lm_slice {
                continue;
            }
            // lhs + sum (c / lc) * w = 0  ==>  lhs -> sum (-c / lc) * w
            let q = c
                .try_div_exact(lc)
                .ok_or(ShirshovError::NonDivisibleLeadingCoeff)?;
            let neg_q = q.neg_val();
            if !neg_q.is_zero() {
                rhs_terms.insert(w.clone(), neg_q);
            }
        }
        Ok(Self {
            lhs,
            rhs: FreeAlg::from_terms(rhs_terms),
        })
    }

    /// Underlying two-sided ideal relation `lhs - rhs`.
    pub fn as_relation(&self) -> FreeAlg<G, R> {
        &FreeAlg::word(self.lhs.clone()) - &self.rhs
    }
}

/// Errors encountered during rule orientation or Buchberger–Shirshov completion.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum ShirshovError {
    /// Attempted to orient `0` into a rewrite rule.
    ZeroRelation,
    /// Encountered a non-zero scalar relation `c * 1 = 0` generating the unit ideal `(1)`.
    ScalarUnitRelation,
    /// Leading coefficient does not divide all lower-order coefficients in the base ring `R`.
    NonDivisibleLeadingCoeff,
    /// Explicit `RewriteRule` has a `rhs` term `>= lhs`.
    InvalidRuleOrientation,
}

impl fmt::Display for ShirshovError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ShirshovError::ZeroRelation => write!(f, "cannot orient the zero polynomial as a rule"),
            ShirshovError::ScalarUnitRelation => {
                write!(f, "non-zero scalar relation generates the degenerate unit ideal")
            }
            ShirshovError::NonDivisibleLeadingCoeff => {
                write!(f, "leading coefficient does not divide all lower terms in base ring")
            }
            ShirshovError::InvalidRuleOrientation => {
                write!(f, "rewrite rule rhs contains a word >= lhs under monomial order")
            }
        }
    }
}

impl std::error::Error for ShirshovError {}

/// Classification of a critical composition between two rewrite rules.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub enum CriticalPairKind<G> {
    /// Overlap composition on $w = a b c$ where $\text{lhs}_1 = a b$, $\text{lhs}_2 = b c$, $|b| \ge 1$.
    Overlap {
        /// Index of left rule $r_1$.
        left_rule: usize,
        /// Index of right rule $r_2$.
        right_rule: usize,
        /// Length $|b| \ge 1$ of the shared overlap subword.
        overlap_len: usize,
        /// Ambient overlap word $w = a b c$.
        ambient_word: Word<G>,
    },
    /// Inclusion composition on $w = \text{lhs}_1 = a\,\text{lhs}_2\,c$.
    Inclusion {
        /// Index of outer rule $r_1$.
        outer_rule: usize,
        /// Index of inner rule $r_2$.
        inner_rule: usize,
        /// Character offset $|a|$ of $\text{lhs}_2$ inside $\text{lhs}_1$.
        offset: usize,
        /// Ambient word $w = \text{lhs}_1$.
        ambient_word: Word<G>,
    },
}

/// Bounds controlling dynamic Buchberger–Shirshov completion.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct CompletionConfig {
    /// Optional cap on ambient composition word length $|w|$.
    pub max_degree: Option<usize>,
    /// Optional cap on `order.filtration_degree(&w)` of ambient composition words.
    pub max_filtration_order: Option<usize>,
    /// Maximum outer completion passes before stopping.
    pub max_iterations: usize,
}

impl Default for CompletionConfig {
    fn default() -> Self {
        Self {
            max_degree: None,
            max_filtration_order: None,
            max_iterations: 64,
        }
    }
}

/// Summary certificate emitted by [`ShirshovEngine::complete`].
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct CompletionCertificate {
    /// `true` iff every overlap and inclusion composition reduced to `0` with zero skipped pairs.
    pub is_complete: bool,
    /// Number of completion passes executed.
    pub iterations: usize,
    /// Final interreduced rule count.
    pub rules_count: usize,
    /// Total S-polynomial compositions reduced during completion.
    pub critical_pairs_tested: usize,
    /// Remaining non-zero S-polynomials when stopped early by `max_iterations`.
    pub unresolved_pairs: usize,
    /// Critical pairs skipped due to `max_degree` or `max_filtration_order`.
    pub skipped_by_bound: usize,
}

/// Dynamic non-commutative Gröbner–Shirshov basis and normal-form reduction engine.
#[derive(Clone, Debug)]
pub struct ShirshovEngine<G: Ord, R, O> {
    rules: Vec<RewriteRule<G, R>>,
    first_letter_index: BTreeMap<G, Vec<usize>>,
    unit_ideal: bool,
    order: O,
}

impl<G, R, O> ShirshovEngine<G, R, O>
where
    G: Ord + Clone + Hash + fmt::Debug,
    R: RingScalar,
    O: MonomialOrder<G>,
{
    /// Create an empty engine with the given admissible monomial order.
    pub fn new(order: O) -> Self {
        Self {
            rules: Vec::new(),
            first_letter_index: BTreeMap::new(),
            unit_ideal: false,
            order,
        }
    }

    /// Construct from explicit `RewriteRule`s (validating orientation against `order`).
    pub fn from_rules(rules: Vec<RewriteRule<G, R>>, order: O) -> Result<Self, ShirshovError> {
        for r in &rules {
            RewriteRule::try_new(r.lhs.clone(), r.rhs.clone(), &order)?;
        }
        let mut engine = Self {
            rules,
            first_letter_index: BTreeMap::new(),
            unit_ideal: false,
            order,
        };
        engine.rebuild_index();
        Ok(engine)
    }

    /// Construct from polynomial relations in $R\langle G \rangle$, ignoring exact zeros.
    pub fn from_relations<I: IntoIterator<Item = FreeAlg<G, R>>>(
        relations: I,
        order: O,
    ) -> Result<Self, ShirshovError> {
        let mut engine = Self::new(order);
        for rel in relations {
            if rel.is_zero() {
                continue;
            }
            match RewriteRule::from_relation(&rel, &engine.order) {
                Ok(rule) => engine.rules.push(rule),
                Err(ShirshovError::ScalarUnitRelation) => {
                    if let Some((_, lc)) = rel.leading_term(&engine.order) {
                        if lc.try_inv().is_some() {
                            engine.unit_ideal = true;
                            engine.rules.clear();
                            engine.first_letter_index.clear();
                            return Ok(engine);
                        }
                    }
                    return Err(ShirshovError::NonDivisibleLeadingCoeff);
                }
                Err(e) => return Err(e),
            }
        }
        engine.rebuild_index();
        Ok(engine)
    }

    /// Active rewrite rules.
    pub fn rules(&self) -> &[RewriteRule<G, R>] {
        &self.rules
    }

    /// Ambient monomial order.
    pub fn order(&self) -> &O {
        &self.order
    }

    /// Returns `true` if a unit scalar relation collapsed the quotient algebra to `{0}`.
    pub fn is_unit_ideal(&self) -> bool {
        self.unit_ideal
    }

    fn rebuild_index(&mut self) {
        self.rules
            .sort_by(|a, b| self.order.cmp_words(&a.lhs, &b.lhs));
        self.first_letter_index.clear();
        for (idx, r) in self.rules.iter().enumerate() {
            if let Some(first) = r.lhs.first() {
                self.first_letter_index
                    .entry(first.clone())
                    .or_default()
                    .push(idx);
            }
        }
    }

    /// Find the leftmost-shortest matching rule `(offset, rule_idx)` inside `word`.
    fn find_redex(&self, word: &[G]) -> Option<(usize, usize)> {
        for pos in 0..word.len() {
            let first = &word[pos];
            if let Some(candidates) = self.first_letter_index.get(first) {
                let rem = word.len() - pos;
                for &rule_idx in candidates {
                    let lhs = &self.rules[rule_idx].lhs;
                    if lhs.len() <= rem && &word[pos..pos + lhs.len()] == lhs.as_slice() {
                        return Some((pos, rule_idx));
                    }
                }
            }
        }
        None
    }

    fn reduce_word_memo(
        &self,
        word: &[G],
        memo: &mut FxHashMap<Word<G>, FreeAlg<G, R>>,
    ) -> FreeAlg<G, R> {
        if self.unit_ideal {
            return FreeAlg::zero();
        }
        if let Some(cached) = memo.get(word) {
            return cached.clone();
        }
        let result = match self.find_redex(word) {
            None => FreeAlg::word(word.to_vec()),
            Some((pos, rule_idx)) => {
                let rule = &self.rules[rule_idx];
                let prefix = &word[..pos];
                let suffix = &word[pos + rule.lhs.len()..];
                let mut acc = FreeAlg::zero();
                for (m, c) in rule.rhs.terms() {
                    let mut next_word = Vec::with_capacity(prefix.len() + m.len() + suffix.len());
                    next_word.extend_from_slice(prefix);
                    next_word.extend_from_slice(m);
                    next_word.extend_from_slice(suffix);
                    let red = self.reduce_word_memo(&next_word, memo);
                    acc.add_scaled_assign(&red, c);
                }
                acc
            }
        };
        memo.insert(word.to_vec(), result.clone());
        result
    }

    /// Enumerate all overlap and inclusion S-polynomials of the current rule set.
    ///
    /// For overlap $u_1 = a b$, $u_2 = b c$ ($|b| \ge 1$), returns
    /// $S_{\text{overlap}} = \text{rhs}_1 \cdot c - a \cdot \text{rhs}_2$.
    /// For inclusion $u_1 = a u_2 c$, returns
    /// $S_{\text{inclusion}} = \text{rhs}_1 - a \cdot \text{rhs}_2 \cdot c$.
    pub fn critical_pairs(&self) -> Vec<(CriticalPairKind<G>, FreeAlg<G, R>)> {
        let mut pairs = Vec::new();
        let n = self.rules.len();
        for i in 0..n {
            let u1 = &self.rules[i].lhs;
            let rhs1 = &self.rules[i].rhs;
            for j in 0..n {
                let u2 = &self.rules[j].lhs;
                let rhs2 = &self.rules[j].rhs;

                // 1. Overlap compositions: u1 = a b, u2 = b c with 1 <= |b| < min(|u1|, |u2|)
                let max_k = u1.len().min(u2.len()).saturating_sub(1);
                for k in 1..=max_k {
                    let a = &u1[..u1.len() - k];
                    let b1 = &u1[u1.len() - k..];
                    let b2 = &u2[..k];
                    let c = &u2[k..];
                    if b1 == b2 {
                        let mut ambient = Vec::with_capacity(u1.len() + c.len());
                        ambient.extend_from_slice(u1);
                        ambient.extend_from_slice(c);
                        let term1 = rhs1.bimul_words(&[], c, &R::one());
                        let term2 = rhs2.bimul_words(a, &[], &R::one());
                        let spoly = &term1 - &term2;
                        pairs.push((
                            CriticalPairKind::Overlap {
                                left_rule: i,
                                right_rule: j,
                                overlap_len: k,
                                ambient_word: ambient,
                            },
                            spoly,
                        ));
                    }
                }

                // 2. Inclusion compositions: u1 = a u2 c (skip trivial self-inclusion i == j)
                if i != j && u1.len() >= u2.len() {
                    let max_offset = u1.len() - u2.len();
                    for offset in 0..=max_offset {
                        if &u1[offset..offset + u2.len()] == u2.as_slice() {
                            let a = &u1[..offset];
                            let c = &u1[offset + u2.len()..];
                            let term2 = rhs2.bimul_words(a, c, &R::one());
                            let spoly = rhs1 - &term2;
                            pairs.push((
                                CriticalPairKind::Inclusion {
                                    outer_rule: i,
                                    inner_rule: j,
                                    offset,
                                    ambient_word: u1.clone(),
                                },
                                spoly,
                            ));
                        }
                    }
                }
            }
        }
        pairs.sort_by(|(k1, _), (k2, _)| {
            let w1 = match k1 {
                CriticalPairKind::Overlap { ambient_word, .. }
                | CriticalPairKind::Inclusion { ambient_word, .. } => ambient_word.as_slice(),
            };
            let w2 = match k2 {
                CriticalPairKind::Overlap { ambient_word, .. }
                | CriticalPairKind::Inclusion { ambient_word, .. } => ambient_word.as_slice(),
            };
            self.order.cmp_words(w1, w2)
        });
        pairs
    }

    /// Test whether the current rule set is already a Gröbner–Shirshov basis (all critical
    /// S-polynomials reduce to `0`).
    pub fn is_confluent(&self) -> bool {
        if self.unit_ideal {
            return true;
        }
        let mut memo = FxHashMap::default();
        for (_, spoly) in self.critical_pairs() {
            let mut acc = FreeAlg::zero();
            for (w, c) in spoly.terms() {
                let red = self.reduce_word_memo(w, &mut memo);
                acc.add_scaled_assign(&red, c);
            }
            if !acc.is_zero() {
                return false;
            }
        }
        true
    }

    /// Interreduce (`autoreduce`) the active rule set so no `lhs` contains another `lhs`
    /// as a subword and every `rhs` is in normal form with respect to all rules.
    pub fn autoreduce(&mut self) -> Result<(), ShirshovError> {
        if self.unit_ideal {
            return Ok(());
        }
        loop {
            self.rebuild_index();
            let mut changed = false;

            // Step A: eliminate any rule i whose lhs contains another rule j's lhs as subword.
            let mut redundant_idx = None;
            for i in 0..self.rules.len() {
                for j in 0..self.rules.len() {
                    if i == j || self.rules[i].lhs.len() < self.rules[j].lhs.len() {
                        continue;
                    }
                    let u_i = &self.rules[i].lhs;
                    let u_j = &self.rules[j].lhs;
                    if u_i.windows(u_j.len()).any(|win| win == u_j.as_slice()) {
                        redundant_idx = Some(i);
                        break;
                    }
                }
                if redundant_idx.is_some() {
                    break;
                }
            }

            if let Some(idx) = redundant_idx {
                let removed = self.rules.remove(idx);
                self.rebuild_index();
                let reduced = self.reduce(&removed.as_relation());
                if !reduced.is_zero() {
                    match RewriteRule::from_relation(&reduced, &self.order) {
                        Ok(new_rule) => self.rules.push(new_rule),
                        Err(ShirshovError::ScalarUnitRelation) => {
                            if let Some((_, lc)) = reduced.leading_term(&self.order) {
                                if lc.try_inv().is_some() {
                                    self.unit_ideal = true;
                                    self.rules.clear();
                                    self.first_letter_index.clear();
                                    return Ok(());
                                }
                            }
                            return Err(ShirshovError::NonDivisibleLeadingCoeff);
                        }
                        Err(e) => return Err(e),
                    }
                }
                continue;
            }

            // Step B: reduce every rule's rhs to normal form.
            let mut memo = FxHashMap::default();
            for i in 0..self.rules.len() {
                let mut new_rhs = FreeAlg::zero();
                for (w, c) in self.rules[i].rhs.terms() {
                    let red = self.reduce_word_memo(w, &mut memo);
                    new_rhs.add_scaled_assign(&red, c);
                }
                if new_rhs != self.rules[i].rhs {
                    self.rules[i].rhs = new_rhs;
                    changed = true;
                    memo.clear();
                }
            }

            if !changed {
                break;
            }
        }
        self.rebuild_index();
        Ok(())
    }

    /// Run Buchberger–Shirshov completion under `config`, returning an exact certificate.
    pub fn complete(
        &mut self,
        config: &CompletionConfig,
    ) -> Result<CompletionCertificate, ShirshovError> {
        self.autoreduce()?;
        if self.unit_ideal {
            return Ok(CompletionCertificate {
                is_complete: true,
                iterations: 0,
                rules_count: 0,
                critical_pairs_tested: 0,
                unresolved_pairs: 0,
                skipped_by_bound: 0,
            });
        }

        let mut total_tested = 0usize;
        let mut iterations = 0usize;

        while iterations < config.max_iterations {
            iterations += 1;
            let mut last_skipped = 0usize;
            let pairs = self.critical_pairs();
            let mut new_rules: Vec<RewriteRule<G, R>> = Vec::new();
            let mut memo = FxHashMap::default();

            for (kind, spoly) in pairs {
                let ambient = match &kind {
                    CriticalPairKind::Overlap { ambient_word, .. }
                    | CriticalPairKind::Inclusion { ambient_word, .. } => ambient_word.as_slice(),
                };
                if let Some(max_d) = config.max_degree {
                    if ambient.len() > max_d {
                        last_skipped += 1;
                        continue;
                    }
                }
                if let Some(max_f) = config.max_filtration_order {
                    if self.order.filtration_degree(ambient) > max_f {
                        last_skipped += 1;
                        continue;
                    }
                }

                total_tested += 1;
                let mut rem = FreeAlg::zero();
                for (w, c) in spoly.terms() {
                    let red = self.reduce_word_memo(w, &mut memo);
                    rem.add_scaled_assign(&red, c);
                }
                if !rem.is_zero() {
                    match RewriteRule::from_relation(&rem, &self.order) {
                        Ok(rule) => {
                            new_rules.push(rule);
                        }
                        Err(ShirshovError::ScalarUnitRelation) => {
                            if let Some((_, lc)) = rem.leading_term(&self.order) {
                                if lc.try_inv().is_some() {
                                    self.unit_ideal = true;
                                    self.rules.clear();
                                    self.first_letter_index.clear();
                                    return Ok(CompletionCertificate {
                                        is_complete: true,
                                        iterations,
                                        rules_count: 0,
                                        critical_pairs_tested: total_tested,
                                        unresolved_pairs: 0,
                                        skipped_by_bound: 0,
                                    });
                                }
                            }
                            return Err(ShirshovError::NonDivisibleLeadingCoeff);
                        }
                        Err(e) => return Err(e),
                    }
                }
            }

            if new_rules.is_empty() {
                return Ok(CompletionCertificate {
                    is_complete: last_skipped == 0,
                    iterations,
                    rules_count: self.rules.len(),
                    critical_pairs_tested: total_tested,
                    unresolved_pairs: 0,
                    skipped_by_bound: last_skipped,
                });
            }

            self.rules.extend(new_rules);
            self.autoreduce()?;
            if self.unit_ideal {
                return Ok(CompletionCertificate {
                    is_complete: true,
                    iterations,
                    rules_count: 0,
                    critical_pairs_tested: total_tested,
                    unresolved_pairs: 0,
                    skipped_by_bound: 0,
                });
            }
        }

        // Count any remaining unresolved pairs within the configured bounds:
        let mut unresolved = 0usize;
        let mut skipped = 0usize;
        let mut memo = FxHashMap::default();
        for (kind, spoly) in self.critical_pairs() {
            let ambient = match &kind {
                CriticalPairKind::Overlap { ambient_word, .. }
                | CriticalPairKind::Inclusion { ambient_word, .. } => ambient_word.as_slice(),
            };
            if config.max_degree.map_or(false, |d| ambient.len() > d)
                || config
                    .max_filtration_order
                    .map_or(false, |f| self.order.filtration_degree(ambient) > f)
            {
                skipped += 1;
                continue;
            }
            let mut rem = FreeAlg::zero();
            for (w, c) in spoly.terms() {
                let red = self.reduce_word_memo(w, &mut memo);
                rem.add_scaled_assign(&red, c);
            }
            if !rem.is_zero() {
                unresolved += 1;
            }
        }

        Ok(CompletionCertificate {
            is_complete: unresolved == 0 && skipped == 0,
            iterations,
            rules_count: self.rules.len(),
            critical_pairs_tested: total_tested,
            unresolved_pairs: unresolved,
            skipped_by_bound: skipped,
        })
    }
}

impl<G, R, O> NormalFormBasis<R, G> for ShirshovEngine<G, R, O>
where
    G: Ord + Clone + Hash + fmt::Debug,
    R: RingScalar,
    O: MonomialOrder<G>,
{
    fn reduce_word(&self, word: &[G]) -> FreeAlg<G, R> {
        let mut memo = FxHashMap::default();
        self.reduce_word_memo(word, &mut memo)
    }

    fn reduce(&self, elem: &FreeAlg<G, R>) -> FreeAlg<G, R> {
        if self.unit_ideal {
            return FreeAlg::zero();
        }
        let mut memo = FxHashMap::default();
        let mut acc = FreeAlg::zero();
        for (w, c) in elem.terms() {
            let red = self.reduce_word_memo(w, &mut memo);
            acc.add_scaled_assign(&red, c);
        }
        acc
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::order::DegLex;

    #[test]
    fn weyl_algebra_is_confluent_and_reduces_commutator() {
        // Weyl algebra A_1: y*x - x*y = 1, with x = 0 < y = 1 under DegLex => y*x -> x*y + 1
        let x = FreeAlg::<usize, i64>::generator(0);
        let y = FreeAlg::<usize, i64>::generator(1);
        let one = FreeAlg::<usize, i64>::one();
        let rel = &(&y * &x) - &(&(&x * &y) + &one);

        let mut engine = ShirshovEngine::from_relations(vec![rel], DegLex).unwrap();
        let cert = engine.complete(&CompletionConfig::default()).unwrap();
        assert!(cert.is_complete);
        assert_eq!(cert.rules_count, 1);

        // y^2 * x = x * y^2 + 2 * y
        let y2x = &(&y * &y) * &x;
        let expected = &(&x * &(&y * &y)) + &y.scale(&2);
        assert_eq!(engine.reduce(&y2x), expected);
    }

    #[test]
    fn truncated_nilpotent_ideal_respects_degree_bound() {
        // Relation x y x = y^2 generates an infinite chain unless bounded or completed
        let x = FreeAlg::<usize, i64>::generator(0);
        let y = FreeAlg::<usize, i64>::generator(1);
        let rel = &(&(&x * &y) * &x) - &(&y * &y);
        let mut engine = ShirshovEngine::from_relations(vec![rel], DegLex).unwrap();
        let cfg = CompletionConfig {
            max_degree: Some(5),
            max_filtration_order: None,
            max_iterations: 10,
        };
        let cert = engine.complete(&cfg).unwrap();
        assert!(!cert.is_complete);
        assert!(cert.skipped_by_bound > 0);
    }
}
