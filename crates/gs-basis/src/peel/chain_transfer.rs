//! Hecke-only $2 \times 2$ transfer-matrix normal-form reduction for block-ordered chain elements.
//!
//! For any block-ordered element
//! $$\Xi_n \;=\; \prod_{i=0}^{n-2} \;\prod_{k} \bigl(c_{i,k}\,\sigma_i + d_{i,k}\,\mathbf{1}\bigr) \in H_n(q)$$
//! with quadratic relation $\sigma_i^2 = h\,\sigma_i + \mathbf{1}$, each generator block
//! collapses via the $2 \times 2$ transfer matrix
//! $$T_h(c, d) = \begin{pmatrix} c h + d & c \\ c & d \end{pmatrix}, \qquad
//! \begin{pmatrix} a' \\ b' \end{pmatrix} = T_h(c, d)\begin{pmatrix} a \\ b \end{pmatrix}$$
//! using *only* the quadratic Hecke rule (zero Yang–Baxter and zero far-commutation steps).
//! The resulting chain product $\prod_{i=0}^{n-2} (a_i\,\sigma_i + b_i\,\mathbf{1})$ expands over
//! subsets $S \subseteq \{0, \dots, n-2\}$ directly into strictly increasing words $\sigma_S$,
//! which are already in Bokut–Shiao Gröbner–Shirshov normal form.

use std::collections::BTreeMap;

use crate::free_alg::{FreeAlg, Word};
use crate::scalar::RingScalar;

/// Single $2 \times 2$ transfer step $(c\,\sigma + d)(a\,\sigma + b) = a'\,\sigma + b'$
/// under $\sigma^2 = h\,\sigma + 1$.
///
/// Returns `(a_next, b_next, used_quadratic_step)`, where `used_quadratic_step` is `true` iff
/// both `a != 0` and `c != 0` (so $\sigma^2$ genuinely appeared).
pub fn transfer_step<R: RingScalar>(h: &R, c: &R, d: &R, a: &R, b: &R) -> (R, R, bool) {
    let ac = a.mul_val(c);
    let used_hecke = !ac.is_zero();
    // a' = a*c*h + a*d + b*c
    let a_next = ac
        .mul_val(h)
        .add_val(&a.mul_val(d))
        .add_val(&b.mul_val(c));
    // b' = a*c + b*d
    let b_next = ac.add_val(&b.mul_val(d));
    (a_next, b_next, used_hecke)
}

/// Compressed normal form $\prod_{i=0}^{n-2} (a_i\,\sigma_i + b_i\,\mathbf{1})$ of a
/// block-ordered chain element in $H_n(q)$.
#[derive(Clone, PartialEq, Eq, Debug)]
pub struct ChainNormalForm<R> {
    /// Linear coefficients `(a_i, b_i)` for `i = 0..num_strands - 1`.
    pub blocks: Vec<(R, R)>,
    /// Number of non-trivial quadratic Hecke reductions (`a*c != 0`) performed across all blocks.
    pub quadratic_block_steps: usize,
}

impl<R: RingScalar> ChainNormalForm<R> {
    /// Reduce a per-generator list of factor blocks `blocks[i] = [(c_{i,0}, d_{i,0}), ...]`
    /// (multiplied left-to-right within block `i`, blocks ordered `i = 0..n-2`) using the
    /// $2 \times 2$ Hecke transfer matrix.
    pub fn from_blocks(blocks: &[Vec<(R, R)>], h: &R) -> Self {
        let mut out_blocks = Vec::with_capacity(blocks.len());
        let mut total_steps = 0usize;

        for factors in blocks {
            // Multiply left-to-right: start from 0*sigma + 1, and right-multiply or left-multiply
            // (commutative inside R[sigma]/(sigma^2 - h*sigma - 1)!):
            let mut a = R::zero();
            let mut b = R::one();
            for (c, d) in factors {
                let (a_next, b_next, used) = transfer_step(h, c, d, &a, &b);
                if used {
                    total_steps += 1;
                }
                a = a_next;
                b = b_next;
            }
            out_blocks.push((a, b));
        }

        Self {
            blocks: out_blocks,
            quadratic_block_steps: total_steps,
        }
    }

    /// Evaluate the exact normalized Markov trace $\operatorname{tr}_M(\Xi_n) = \prod_{i=0}^{n-2} (a_i z + b_i)$
    /// in $O(n)$ ring operations without expanding the $2^{n-1}$ normal-form terms.
    pub fn markov_trace(&self, z: &R) -> R {
        let mut prod = R::one();
        for (a, b) in &self.blocks {
            let factor = a.mul_val(z).add_val(b);
            prod = prod.mul_val(&factor);
        }
        prod
    }

    /// Expand $\prod_{i=0}^{n-2} (a_i\,\sigma_i + b_i\,\mathbf{1})$ into its explicit $2^{n-1}$-subset
    /// Bokut–Shiao normal form $\sum_{S \subseteq \{0..n-2\}} (\prod_{i\in S} a_i)(\prod_{i\notin S} b_i)\,\sigma_S$.
    pub fn expand_to_normal_form(&self) -> FreeAlg<usize, R> {
        let m = self.blocks.len();
        assert!(
            m < (usize::BITS as usize),
            "explicit 2^m subset expansion requires m < {}",
            usize::BITS
        );
        let mut terms: BTreeMap<Word<usize>, R> = BTreeMap::new();
        let total_subsets = 1usize << m;
        for mask in 0..total_subsets {
            let mut coeff = R::one();
            let mut word = Vec::new();
            for (i, (a, b)) in self.blocks.iter().enumerate() {
                if (mask >> i) & 1 == 1 {
                    coeff = coeff.mul_val(a);
                    word.push(i);
                } else {
                    coeff = coeff.mul_val(b);
                }
                if coeff.is_zero() {
                    break;
                }
            }
            if !coeff.is_zero() {
                terms.insert(word, coeff);
            }
        }
        FreeAlg::from_terms(terms)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::hecke::BokutShiaoHecke;
    use crate::order::DegLex;
    use crate::scalar::LaurentPoly;
    use crate::shirshov::{NormalFormBasis, ShirshovEngine};

    #[test]
    fn chain_transfer_matches_bokut_shiao_and_counts_binomial_steps() {
        type L = LaurentPoly<i64>;
        let h = L::h();
        let q = L::q();

        // Build Xi_A on A = 5 strands: block i (i = 0..3) has (A - 1 - i) factors => 4 + 3 + 2 + 1 = 10 factors,
        // so quadratic block multiplications = C(4, 2) = 6 (3 + 2 + 1 + 0)!
        let a_strands = 5usize;
        let mut blocks: Vec<Vec<(L, L)>> = Vec::new();
        let mut explicit_prod = FreeAlg::<usize, L>::one();

        for i in 0..(a_strands - 1) {
            let mut blk = Vec::new();
            for j in ((i + 1)..a_strands).rev() {
                let c = L::monomial((j - i) as i32, 1);
                let d = L::from_i64((i + j) as i64);
                let lin = &FreeAlg::term(vec![i], c.clone()) + &FreeAlg::scalar(d.clone());
                explicit_prod = &explicit_prod * &lin;
                blk.push((c, d));
            }
            blocks.push(blk);
        }

        let chain = ChainNormalForm::from_blocks(&blocks, &h);
        // C(A - 1, 2) = C(4, 2) = 6 quadratic steps!
        assert_eq!(chain.quadratic_block_steps, 6);

        let expanded = chain.expand_to_normal_form();
        let fast_hecke = BokutShiaoHecke::new(a_strands, h.clone());
        let gs_engine =
            ShirshovEngine::from_rules(BokutShiaoHecke::completed_rules(a_strands, &h), DegLex)
                .unwrap();

        assert_eq!(expanded, fast_hecke.reduce(&explicit_prod));
        assert_eq!(expanded, gs_engine.reduce(&explicit_prod));

        // Scalar crossing (c = 0) spends zero Hecke steps:
        let scalar_chain = ChainNormalForm::from_blocks(&[vec![(L::zero(), q.clone()); 4]], &h);
        assert_eq!(scalar_chain.quadratic_block_steps, 0);
        assert_eq!(scalar_chain.blocks[0], (L::zero(), q.pow_u32(4)));
    }
}
