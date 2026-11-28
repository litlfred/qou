//! Specialized planar non-crossing diagram backend for the Temperley–Lieb algebra $TL_n(\delta)$
//! and its Iwahori–Hecke skein quotients.
//!
//! ## Conventions
//!
//! - **Planar diagrams (`PlanarMatching`):** $2n$ boundary points labelled `0..n` along the top
//!   edge (left to right) and `n..2n` along the bottom edge (left to right). Stacking $d_1$ above
//!   $d_2$ identifies bottom point `n + k` of $d_1$ with top point `k` of $d_2$; each closed
//!   interior loop multiplies the coefficient by the loop parameter $\delta$.
//! - **Defining relations:** Generators $e_0, \dots, e_{n-2}$ satisfy $e_i^2 = \delta e_i$,
//!   $e_i e_{i \pm 1} e_i = e_i$, and $e_i e_j = e_j e_i$ for $|i - j| \ge 2$.
//!   The basis of planar non-crossing matchings has Catalan dimension
//!   $C_n = \frac{1}{n+1}\binom{2n}{n}$ ($C_6 = 132$, $C_8 = 1430$, $C_9 = 4862$, $C_{12} = 208012$).
//! - **Hecke skein projections ([`SkeinConvention`]):**
//!   - [`SkeinConvention::BalancedMinus`]: $\sigma_i \mapsto q\,\mathbf{1} - e_i$ with
//!     $\delta = q + q^{-1} = \[2\]_q$. Satisfies the balanced Hecke quadratic relation
//!     $(q\,\mathbf{1} - e_i)^2 = (q - q^{-1})(q\,\mathbf{1} - e_i) + \mathbf{1}$ and the braid
//!     relation $(q\,\mathbf{1} - e_i)(q\,\mathbf{1} - e_{i+1})(q\,\mathbf{1} - e_i)
//!     = (q\,\mathbf{1} - e_{i+1})(q\,\mathbf{1} - e_i)(q\,\mathbf{1} - e_{i+1})$.
//!   - [`SkeinConvention::BalancedPlus`]: $\sigma_i \mapsto e_i - q^{-1}\,\mathbf{1}$ with
//!     $\delta = q + q^{-1}$ (dual sign choice, also satisfying $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$).
//!   - [`SkeinConvention::Iwahori`]: $T_i \mapsto v\,e_i - \mathbf{1}$ with $v\,\delta = v^2 + 1$,
//!     satisfying $(T_i - v^2)(T_i + 1) = 0$.
//!   - [`SkeinConvention::NativeTemperleyLieb`]: generator index $i$ maps directly to $e_i$.

use std::collections::{BTreeMap, VecDeque};
use std::sync::OnceLock;

use serde::{Deserialize, Serialize};

use crate::free_alg::{FreeAlg, Word};
use crate::scalar::RingScalar;
use crate::shirshov::NormalFormBasis;

/// Planar non-crossing matching of $2n$ boundary points (`0..n` top, `n..2n` bottom).
#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Hash, Debug, Serialize, Deserialize)]
pub struct PlanarMatching {
    num_strands: u16,
    partner: Vec<u16>,
}

impl PlanarMatching {
    /// Identity diagram $\mathbf{1}_n$ connecting top `k` straight down to bottom `n + k`.
    pub fn identity(num_strands: usize) -> Self {
        let n = num_strands as u16;
        let mut partner = vec![0u16; 2 * num_strands];
        for k in 0..num_strands {
            partner[k] = n + k as u16;
            partner[num_strands + k] = k as u16;
        }
        Self {
            num_strands: n,
            partner,
        }
    }

    /// Temperley–Lieb generator $e_i$ ($0 \le i < n - 1$) cupping top `(i, i+1)` and capping
    /// bottom `(n+i, n+i+1)`.
    pub fn generator_e(num_strands: usize, i: usize) -> Self {
        assert!(
            num_strands >= 2 && i < num_strands - 1,
            "generator e_{i} out of range for TL_{num_strands}"
        );
        let mut d = Self::identity(num_strands);
        let i16 = i as u16;
        let b = num_strands as u16 + i16;
        d.partner[i] = i16 + 1;
        d.partner[i + 1] = i16;
        d.partner[num_strands + i] = b + 1;
        d.partner[num_strands + i + 1] = b;
        d
    }

    /// Number of strands $n$.
    pub fn num_strands(&self) -> usize {
        self.num_strands as usize
    }

    /// Partner endpoint of boundary vertex `p` (`0 <= p < 2n`).
    pub fn partner_of(&self, p: usize) -> usize {
        self.partner[p] as usize
    }

    /// Compose `self` (top) with `other` (bottom), returning `(composed_diagram, closed_loops)`.
    pub fn compose(&self, other: &Self) -> (Self, usize) {
        assert_eq!(
            self.num_strands, other.num_strands,
            "cannot compose TL diagrams with different strand counts"
        );
        let n = self.num_strands as usize;
        if n == 0 {
            return (Self::identity(0), 0);
        }

        // State space of 4n endpoints:
        // 0..n       : outer top (= top of self)
        // n..2n      : seam upper (= bottom of self, glued to seam lower 2n..3n)
        // 2n..3n     : seam lower (= top of other, glued to seam upper n..2n)
        // 3n..4n     : outer bottom (= bottom of other)
        let mut new_partner = vec![0u16; 2 * n];
        let mut seam_visited = vec![false; 2 * n]; // indices 0..n for seam upper, n..2n for seam lower

        let trace_from = |start_in_top: bool, start_local: usize, visited: &mut [bool]| -> (bool, usize) {
            let mut in_top = start_in_top;
            let mut cur = start_local;
            loop {
                let next = if in_top {
                    self.partner[cur] as usize
                } else {
                    other.partner[cur] as usize
                };
                if in_top {
                    if next < n {
                        // Exits at outer top `next`
                        return (true, next);
                    }
                    // Hits seam at index `k = next - n`; crosses into `other` top `k`
                    let k = next - n;
                    visited[k] = true;
                    visited[n + k] = true;
                    in_top = false;
                    cur = k;
                } else {
                    if next >= n {
                        // Exits at outer bottom `next - n` (which is `next` in 0..2n of composed)
                        return (false, next);
                    }
                    // Hits seam at `other` top `k = next`; crosses into `self` bottom `n + k`
                    let k = next;
                    visited[n + k] = true;
                    visited[k] = true;
                    in_top = true;
                    cur = n + k;
                }
            }
        };

        // 1. Trace from all 2n outer boundary vertices:
        for top_idx in 0..n {
            let (end_is_top, end_idx) = trace_from(true, top_idx, &mut seam_visited);
            let out_pos = if end_is_top { end_idx } else { end_idx };
            new_partner[top_idx] = out_pos as u16;
        }
        for bot_local in n..2 * n {
            let (end_is_top, end_idx) = trace_from(false, bot_local, &mut seam_visited);
            let out_pos = if end_is_top { end_idx } else { end_idx };
            new_partner[bot_local] = out_pos as u16;
        }

        // 2. Count closed interior loops among unvisited seam vertices:
        let mut loops = 0usize;
        for k in 0..n {
            if seam_visited[k] {
                continue;
            }
            loops += 1;
            // Walk closed cycle starting at self bottom `n + k` -> other top `k`:
            let mut in_top = false;
            let mut cur = k;
            seam_visited[k] = true;
            seam_visited[n + k] = true;
            loop {
                let next = if in_top {
                    self.partner[cur] as usize
                } else {
                    other.partner[cur] as usize
                };
                if in_top {
                    let sk = next - n;
                    if sk == k {
                        break;
                    }
                    seam_visited[sk] = true;
                    seam_visited[n + sk] = true;
                    in_top = false;
                    cur = sk;
                } else {
                    let sk = next;
                    seam_visited[n + sk] = true;
                    seam_visited[sk] = true;
                    in_top = true;
                    cur = n + sk;
                }
            }
        }

        (
            Self {
                num_strands: self.num_strands,
                partner: new_partner,
            },
            loops,
        )
    }

    /// Number of closed loops formed by Markov closure (gluing top `k` to bottom `n + k`
    /// for all `k = 0..n`). Takes values in `1..=n` (or `0` when `n == 0`).
    pub fn closure_loops(&self) -> usize {
        let n = self.num_strands as usize;
        let mut visited = vec![false; 2 * n];
        let mut loops = 0usize;
        for start in 0..2 * n {
            if visited[start] {
                continue;
            }
            loops += 1;
            let mut cur = start;
            while !visited[cur] {
                visited[cur] = true;
                let p = self.partner[cur] as usize;
                visited[p] = true;
                cur = (p + n) % (2 * n);
            }
        }
        loops
    }
}

/// Sparse linear combination of planar non-crossing diagrams in $TL_n(\delta)$.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct TemperleyLiebElement<R> {
    terms: BTreeMap<PlanarMatching, R>,
}

impl<R: RingScalar> TemperleyLiebElement<R> {
    /// Zero element of $TL_n(\delta)$.
    pub fn zero() -> Self {
        Self {
            terms: BTreeMap::new(),
        }
    }

    /// Identity diagram $1 \cdot \mathbf{1}_n$.
    pub fn one(num_strands: usize) -> Self {
        Self::diagram(PlanarMatching::identity(num_strands), R::one())
    }

    /// Single scaled diagram $c \cdot d$.
    pub fn diagram(d: PlanarMatching, coeff: R) -> Self {
        let mut terms = BTreeMap::new();
        if !coeff.is_zero() {
            terms.insert(d, coeff);
        }
        Self { terms }
    }

    /// Returns `true` iff `self == 0`.
    pub fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    /// Number of non-zero planar diagrams in support.
    pub fn num_terms(&self) -> usize {
        self.terms.len()
    }

    /// Underlying non-zero `(diagram, coeff)` map.
    pub fn terms(&self) -> &BTreeMap<PlanarMatching, R> {
        &self.terms
    }

    /// Coefficient of planar diagram `d`.
    pub fn coeff(&self, d: &PlanarMatching) -> R {
        self.terms.get(d).cloned().unwrap_or_else(R::zero)
    }

    /// Scale all coefficients by `s`.
    pub fn scale(&self, s: &R) -> Self {
        if s.is_zero() {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        for (d, c) in &self.terms {
            let prod = c.mul_val(s);
            if !prod.is_zero() {
                terms.insert(d.clone(), prod);
            }
        }
        Self { terms }
    }

    /// Add `scale * rhs` into `self`.
    pub fn add_scaled_assign(&mut self, rhs: &Self, scale: &R) {
        if scale.is_zero() || rhs.is_zero() {
            return;
        }
        for (d, c) in &rhs.terms {
            let delta = c.mul_val(scale);
            if delta.is_zero() {
                continue;
            }
            if let Some(existing) = self.terms.get_mut(d) {
                let sum = existing.add_val(&delta);
                if sum.is_zero() {
                    self.terms.remove(d);
                } else {
                    *existing = sum;
                }
            } else {
                self.terms.insert(d.clone(), delta);
            }
        }
    }

    /// Multiply `self * rhs` in $TL_n(\delta)$, replacing each interior closed loop by `delta`.
    pub fn mul_tl(&self, rhs: &Self, delta: &R) -> Self {
        if self.is_zero() || rhs.is_zero() {
            return Self::zero();
        }
        let mut out = Self::zero();
        for (d1, c1) in &self.terms {
            for (d2, c2) in &rhs.terms {
                let (composed, loops) = d1.compose(d2);
                let loop_factor = delta.pow_u32(loops as u32);
                let coeff = c1.mul_val(c2).mul_val(&loop_factor);
                if !coeff.is_zero() {
                    out.add_scaled_assign(&Self::diagram(composed, R::one()), &coeff);
                }
            }
        }
        out
    }

    /// Unnormalized diagram loop-closure trace $\sum_d c_d \,\delta^{\text{closure\_loops}(d)}$
    /// ($\operatorname{tr}_{\mathrm{loop}}(\mathbf{1}_n) = \delta^n$).
    pub fn loop_closure_trace(&self, delta: &R) -> R {
        let mut acc = R::zero();
        for (d, c) in &self.terms {
            let factor = delta.pow_u32(d.closure_loops() as u32);
            acc = acc.add_val(&c.mul_val(&factor));
        }
        acc
    }
}

/// Skein homomorphism mapping generator $i$ into $TL_n(\delta)$.
#[derive(Clone, PartialEq, Eq, Debug)]
pub enum SkeinConvention<R> {
    /// Native $TL_n(\delta)$ generators: generator `i` maps directly to $e_i$.
    NativeTemperleyLieb,
    /// Balanced Hecke skein map $\sigma_i \mapsto q\,\mathbf{1} - e_i$ ($\delta = q + q^{-1}$).
    BalancedMinus {
        /// Quantum parameter $q$ satisfying $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$.
        q: R,
    },
    /// Dual balanced Hecke skein map $\sigma_i \mapsto e_i - q^{-1}\,\mathbf{1}$ ($\delta = q + q^{-1}$).
    BalancedPlus {
        /// Inverse quantum parameter $q^{-1}$.
        q_inv: R,
    },
    /// Iwahori normalisation $T_i \mapsto v\,e_i - \mathbf{1}$ ($v\,\delta = v^2 + 1$).
    Iwahori {
        /// Square-root parameter $v$ with $q = v^2$.
        v: R,
    },
}

/// Planar Temperley–Lieb basis $TL_n(\delta)$ implementing both diagram arithmetic and
/// [`NormalFormBasis<R, usize>`].
#[derive(Debug)]
pub struct TemperleyLiebBasis<R> {
    num_strands: usize,
    delta: R,
    skein: SkeinConvention<R>,
    canonical_words_cache: OnceLock<BTreeMap<PlanarMatching, Word<usize>>>,
}

impl<R: Clone> Clone for TemperleyLiebBasis<R> {
    fn clone(&self) -> Self {
        Self {
            num_strands: self.num_strands,
            delta: self.delta.clone(),
            skein: self.skein.clone(),
            canonical_words_cache: OnceLock::new(),
        }
    }
}

impl<R: RingScalar> TemperleyLiebBasis<R> {
    /// Construct native $TL_n(\delta)$ where generator `i` represents $e_i$.
    pub fn new(num_strands: usize, delta: R) -> Self {
        Self {
            num_strands,
            delta,
            skein: SkeinConvention::NativeTemperleyLieb,
            canonical_words_cache: OnceLock::new(),
        }
    }

    /// Construct $TL_n(q + q^{-1})$ equipped with the balanced Hecke skein map
    /// $\sigma_i \mapsto q\,\mathbf{1} - e_i$.
    pub fn with_hecke_projection(num_strands: usize, q: R) -> Option<Self> {
        let q_inv = q.try_inv()?;
        let delta = q.add_val(&q_inv);
        Some(Self {
            num_strands,
            delta,
            skein: SkeinConvention::BalancedMinus { q },
            canonical_words_cache: OnceLock::new(),
        })
    }

    /// Construct with an explicit `(delta, SkeinConvention)`.
    pub fn with_convention(num_strands: usize, delta: R, skein: SkeinConvention<R>) -> Self {
        Self {
            num_strands,
            delta,
            skein,
            canonical_words_cache: OnceLock::new(),
        }
    }

    /// Number of strands $n$.
    pub fn num_strands(&self) -> usize {
        self.num_strands
    }

    /// Loop parameter $\delta$.
    pub fn delta(&self) -> &R {
        &self.delta
    }

    /// Active generator-to-$TL_n(\delta)$ skein convention.
    pub fn skein_convention(&self) -> &SkeinConvention<R> {
        &self.skein
    }

    /// Exact Catalan dimension $C_n = \frac{1}{n+1}\binom{2n}{n}$ of $TL_n(\delta)$.
    pub fn catalan_dimension(n: usize) -> usize {
        if n <= 1 {
            return 1;
        }
        let mut c = 1u128;
        for k in 0..n {
            c = c * (2 * (2 * k as u128 + 1)) / (k as u128 + 2);
        }
        c as usize
    }

    /// Enumerate all $C_n$ planar non-crossing matchings of $TL_n$ via perimeter Dyck words.
    pub fn enumerate_diagrams(num_strands: usize) -> Vec<PlanarMatching> {
        if num_strands == 0 {
            return vec![PlanarMatching::identity(0)];
        }
        // Clockwise perimeter order: top 0..n left-to-right, then bottom 2n-1..n right-to-left.
        let mut perimeter = Vec::with_capacity(2 * num_strands);
        for k in 0..num_strands {
            perimeter.push(k as u16);
        }
        for k in (0..num_strands).rev() {
            perimeter.push((num_strands + k) as u16);
        }

        let cap = Self::catalan_dimension(num_strands);
        let mut out = Vec::with_capacity(cap);
        let mut partner = vec![0u16; 2 * num_strands];
        let mut stack: Vec<u16> = Vec::with_capacity(num_strands);

        #[allow(clippy::too_many_arguments)]
        fn dfs(
            pos: usize,
            open_rem: usize,
            perimeter: &[u16],
            stack: &mut Vec<u16>,
            partner: &mut [u16],
            num_strands: u16,
            out: &mut Vec<PlanarMatching>,
        ) {
            if pos == perimeter.len() {
                out.push(PlanarMatching {
                    num_strands,
                    partner: partner.to_vec(),
                });
                return;
            }
            let v = perimeter[pos];
            // Option 1: open a chord at `v`
            if open_rem > 0 {
                stack.push(v);
                dfs(pos + 1, open_rem - 1, perimeter, stack, partner, num_strands, out);
                stack.pop();
            }
            // Option 2: close most recent open chord with `v`
            if let Some(u) = stack.pop() {
                partner[u as usize] = v;
                partner[v as usize] = u;
                dfs(pos + 1, open_rem, perimeter, stack, partner, num_strands, out);
                stack.push(u);
            }
        }

        dfs(
            0,
            num_strands,
            &perimeter,
            &mut stack,
            &mut partner,
            num_strands as u16,
            &mut out,
        );
        out
    }

    /// Image of generator index `i` ($0 \le i < n - 1$) in $TL_n(\delta)$ under `self.skein`.
    pub fn generator_image(&self, i: usize) -> TemperleyLiebElement<R> {
        let id = PlanarMatching::identity(self.num_strands);
        let ei = PlanarMatching::generator_e(self.num_strands, i);
        match &self.skein {
            SkeinConvention::NativeTemperleyLieb => TemperleyLiebElement::diagram(ei, R::one()),
            SkeinConvention::BalancedMinus { q } => {
                let mut el = TemperleyLiebElement::diagram(id, q.clone());
                el.add_scaled_assign(
                    &TemperleyLiebElement::diagram(ei, R::one()),
                    &R::one().neg_val(),
                );
                el
            }
            SkeinConvention::BalancedPlus { q_inv } => {
                let mut el = TemperleyLiebElement::diagram(ei, R::one());
                el.add_scaled_assign(
                    &TemperleyLiebElement::diagram(id, R::one()),
                    &q_inv.neg_val(),
                );
                el
            }
            SkeinConvention::Iwahori { v } => {
                let mut el = TemperleyLiebElement::diagram(ei, v.clone());
                el.add_scaled_assign(
                    &TemperleyLiebElement::diagram(id, R::one()),
                    &R::one().neg_val(),
                );
                el
            }
        }
    }

    /// Project a word in generators `0..n-1` into the planar diagram basis of $TL_n(\delta)$.
    pub fn project_word_to_diagrams(&self, word: &[usize]) -> TemperleyLiebElement<R> {
        let mut acc = TemperleyLiebElement::one(self.num_strands);
        for &g in word {
            let img = self.generator_image(g);
            acc = acc.mul_tl(&img, &self.delta);
        }
        acc
    }

    /// Project an entire `FreeAlg<usize, R>` element into the planar diagram basis of $TL_n(\delta)$.
    pub fn project_to_diagrams(&self, elem: &FreeAlg<usize, R>) -> TemperleyLiebElement<R> {
        let mut out = TemperleyLiebElement::zero();
        for (w, c) in elem.terms() {
            let proj = self.project_word_to_diagrams(w);
            out.add_scaled_assign(&proj, c);
        }
        out
    }

    /// Evaluate the loop-closure trace $\operatorname{tr}_{\mathrm{loop}}(\pi_{TL}(x)) \in R$.
    pub fn loop_trace_of(&self, elem: &FreeAlg<usize, R>) -> R {
        self.project_to_diagrams(elem)
            .loop_closure_trace(&self.delta)
    }

    fn canonical_word_map(&self) -> &BTreeMap<PlanarMatching, Word<usize>> {
        self.canonical_words_cache.get_or_init(|| {
            // Exact DegLex BFS from identity(n) over e_0..e_{n-2}: every planar diagram is
            // reached first by its unique DegLex-minimal reduced e-word (with 0 closed loops!).
            let n = self.num_strands;
            let mut map: BTreeMap<PlanarMatching, Word<usize>> = BTreeMap::new();
            if n == 0 {
                map.insert(PlanarMatching::identity(0), Vec::new());
                return map;
            }
            let id = PlanarMatching::identity(n);
            let gens: Vec<PlanarMatching> =
                (0..n.saturating_sub(1)).map(|i| PlanarMatching::generator_e(n, i)).collect();
            let mut queue = VecDeque::new();
            map.insert(id.clone(), Vec::new());
            queue.push_back(id);

            while let Some(cur) = queue.pop_front() {
                let cur_word = map[&cur].clone();
                for (i, gi) in gens.iter().enumerate() {
                    let (next_diag, loops) = cur.compose(gi);
                    if loops == 0 && !map.contains_key(&next_diag) {
                        let mut next_word = Vec::with_capacity(cur_word.len() + 1);
                        next_word.extend_from_slice(&cur_word);
                        next_word.push(i);
                        map.insert(next_diag.clone(), next_word);
                        queue.push_back(next_diag);
                    }
                }
            }
            map
        })
    }
}

impl<R: RingScalar> NormalFormBasis<R, usize> for TemperleyLiebBasis<R> {
    fn reduce_word(&self, word: &[usize]) -> FreeAlg<usize, R> {
        let diag_elem = self.project_word_to_diagrams(word);
        let word_map = self.canonical_word_map();
        let mut terms = BTreeMap::new();
        for (diag, coeff) in diag_elem.terms() {
            if !coeff.is_zero() {
                let canon = word_map
                    .get(diag)
                    .expect("every planar diagram lies in the image of e_0..e_{n-2}");
                terms.insert(canon.clone(), coeff.clone());
            }
        }
        FreeAlg::from_terms(terms)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::hecke::BokutShiaoHecke;
    use crate::scalar::LaurentPoly;

    #[test]
    fn catalan_dimensions_and_planar_enumeration_through_c12() {
        assert_eq!(TemperleyLiebBasis::<i64>::catalan_dimension(1), 1);
        assert_eq!(TemperleyLiebBasis::<i64>::catalan_dimension(3), 5);
        assert_eq!(TemperleyLiebBasis::<i64>::catalan_dimension(6), 132);
        assert_eq!(TemperleyLiebBasis::<i64>::catalan_dimension(8), 1430);
        assert_eq!(TemperleyLiebBasis::<i64>::catalan_dimension(9), 4862);
        assert_eq!(TemperleyLiebBasis::<i64>::catalan_dimension(12), 208_012);

        assert_eq!(TemperleyLiebBasis::<i64>::enumerate_diagrams(6).len(), 132);
        assert_eq!(TemperleyLiebBasis::<i64>::enumerate_diagrams(8).len(), 1430);
        assert_eq!(TemperleyLiebBasis::<i64>::enumerate_diagrams(9).len(), 4862);
        assert_eq!(
            TemperleyLiebBasis::<i64>::enumerate_diagrams(12).len(),
            208_012
        );
    }

    #[test]
    fn hecke_skein_projection_annihilates_antisymmetric_idempotent_and_preserves_relations() {
        type L = LaurentPoly<i64>;
        let q = L::q();
        let h = L::h();
        let tl3 = TemperleyLiebBasis::with_hecke_projection(3, q.clone()).unwrap();
        let hecke3 = BokutShiaoHecke::new(3, h.clone());

        let s0 = FreeAlg::<usize, L>::generator(0);
        let s1 = FreeAlg::<usize, L>::generator(1);
        let one = FreeAlg::<usize, L>::one();

        // 1. Quadratic and braid relations map to 0 in TL_3(q + q^-1):
        let quad = &(&s0 * &s0) - &(&s0.scale(&h) + &one);
        let braid = &(&(&s1 * &s0) * &s1) - &(&(&s0 * &s1) * &s0);
        assert!(tl3.reduce(&quad).is_zero());
        assert!(tl3.reduce(&braid).is_zero());

        // 2. Factoring through BokutShiaoHecke agrees with direct TL reduction:
        let sample = FreeAlg::<usize, L>::word(vec![1, 0, 1, 0, 1]);
        assert_eq!(tl3.reduce(&sample), tl3.reduce(&hecke3.reduce(&sample)));

        // 3. The 6-term q-antisymmetrizer on 3 strands (generating ker(H_3 -> TL_3)) vanishes!
        // Under sigma_i |-> q*1 - e_i, e_i kills the trivial eigenvalue q... wait:
        // (q*1 - e_i) has eigenvalue q on ker(e_i) and q - (q + q^-1) = -q^-1 on im(e_i)!
        // On n=3, dim H_3 = 6 and dim TL_3 = C_3 = 5; the 1-dimensional kernel is spanned by
        // C_det = 1 - q^{-1}(s0 + s1) + q^{-2}(s0*s1 + s1*s0) - q^{-3}(s0*s1*s0)!
        let qi = L::q_inv();
        let qi2 = &qi * &qi;
        let qi3 = &qi2 * &qi;
        let kazhdan_lusztig_det = &(&(&one - &(&s0 + &s1).scale(&qi))
            + &(&(&s0 * &s1) + &(&s1 * &s0)).scale(&qi2))
            - &(&(&s0 * &s1) * &s0).scale(&qi3);
        assert!(tl3.project_to_diagrams(&kazhdan_lusztig_det).is_zero());
        assert!(tl3.reduce(&kazhdan_lusztig_det).is_zero());

        // 4. Loop closure trace of identity on 3 strands is delta^3 = (q + q^-1)^3:
        let delta = L::delta_two();
        assert_eq!(tl3.loop_trace_of(&one), delta.pow_u32(3));
    }
}
