//! F3.2.γ scaffolding: Geck-Pfeiffer minimal-length reduction.
//!
//! For the Iwahori-Hecke algebra `H_n(q)`, every element `T_β` arising
//! from a positive braid word has an expansion in the canonical basis
//! `{T_w : w ∈ S_n}`:
//!
//!   `T_β = Σ_{w ∈ S_n} c_w(q) · T_w`
//!
//! where the coefficients `c_w(q)` are Laurent polynomials in q.  This
//! module computes that expansion via the standard Hecke multiplication
//! rules, exposing it for use by q-MN character evaluation and the
//! discovery cache.
//!
//! ## Multiplication rules (Bourbaki LIE IV §2)
//!
//! For a simple reflection `s_i` and `w ∈ S_n`:
//!
//!   T_{s_i} · T_w = T_{s_i w}                 if ℓ(s_i w) > ℓ(w)
//!   T_{s_i} · T_w = T_{s_i w} + (q − q^{-1}) · T_w   if ℓ(s_i w) < ℓ(w)
//!
//! Equivalently, for the right action:
//!
//!   T_w · T_{s_i} = T_{w s_i}                 if ℓ(w s_i) > ℓ(w)
//!   T_w · T_{s_i} = T_{w s_i} + (q − q^{-1}) · T_w   if ℓ(w s_i) < ℓ(w)
//!
//! For inverse generators we use the Hecke relation `T_{s_i}^{-1} =
//! T_{s_i} − (q − q^{-1})`.
//!
//! ## Status
//!
//! This is **scaffolding** for F3.2.γ.  The full implementation
//! requires:
//!
//!   1. ✅ Permutation type (cycle representation or one-line form)
//!   2. ✅ Length function ℓ(w) = #inversions(w)
//!   3. ✅ Hecke basis multiplication primitives (Tw_mul_Ts)
//!   4. ✅ Word-to-Hecke expansion: T_β = Σ c_w · T_w
//!   5. 🚧 Memoization across multiplications
//!   6. 🚧 PyO3 export
//!   7. 🚧 Cross-validation with seminormal at q_0 on full atomic braids
//!
//! Cost: a single `T_β` expansion has worst-case O(n! · word_len)
//! coefficients but typical (sparse) braid words give smaller spans.

use crate::laurent_poly_q::LaurentPolyQ;
use std::collections::BTreeMap;

/// Permutation of `n` elements as a one-line representation (i.e.
/// `perm[i] = w(i)`, 0-indexed).
#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
pub struct Perm(pub Vec<usize>);

impl Perm {
    pub fn identity(n: usize) -> Self {
        Self((0..n).collect())
    }

    pub fn n(&self) -> usize {
        self.0.len()
    }

    /// Apply the simple transposition `s_i` (swap positions i, i+1)
    /// on the right: `w · s_i`.  This is the same as swapping
    /// `perm[i]` and `perm[i+1]`.
    pub fn apply_s_right(&mut self, i: usize) {
        if i + 1 < self.0.len() {
            self.0.swap(i, i + 1);
        }
    }

    /// Apply `s_i` on the left: `s_i · w`.  This swaps the positions
    /// where the elements `i` and `i+1` appear in the one-line form.
    pub fn apply_s_left(&mut self, i: usize) {
        // Find positions of i and i+1 in self.0 and swap their values.
        let mut pos_i = None;
        let mut pos_i1 = None;
        for (k, &v) in self.0.iter().enumerate() {
            if v == i { pos_i = Some(k); }
            if v == i + 1 { pos_i1 = Some(k); }
        }
        if let (Some(a), Some(b)) = (pos_i, pos_i1) {
            self.0.swap(a, b);
        }
    }

    /// Number of inversions = ℓ(w).
    pub fn length(&self) -> usize {
        let mut count = 0;
        for i in 0..self.0.len() {
            for j in (i + 1)..self.0.len() {
                if self.0[i] > self.0[j] {
                    count += 1;
                }
            }
        }
        count
    }
}

/// Element of `H_n(q)` as a sparse map `w → c_w(q)` in the T_w basis.
pub type HeckeElement = BTreeMap<Perm, LaurentPolyQ>;

/// Identity in the Hecke basis: `1 = T_e`.
pub fn hecke_identity(n: usize) -> HeckeElement {
    let mut m = BTreeMap::new();
    m.insert(Perm::identity(n), LaurentPolyQ::one());
    m
}

/// Right-multiply a Hecke element `x` by `T_{s_i}` (positive simple
/// generator).  Returns `x · T_{s_i}`.
pub fn hecke_mul_ts_right(x: &HeckeElement, i: usize) -> HeckeElement {
    let h = LaurentPolyQ::hecke_h();  // q − q^{-1}
    let mut result: HeckeElement = BTreeMap::new();
    for (w, c) in x {
        let l_w = w.length();
        let mut w_si = w.clone();
        w_si.apply_s_right(i);
        let l_w_si = w_si.length();
        if l_w_si > l_w {
            // T_w · T_{s_i} = T_{w s_i}.
            let entry = result.entry(w_si).or_insert_with(LaurentPolyQ::zero);
            *entry += c;
        } else {
            // T_w · T_{s_i} = T_{w s_i} + (q − q^{-1}) · T_w.
            let entry = result.entry(w_si).or_insert_with(LaurentPolyQ::zero);
            *entry += c;
            let h_c = h.clone() * c.clone();
            let entry2 = result.entry(w.clone()).or_insert_with(LaurentPolyQ::zero);
            *entry2 += &h_c;
        }
    }
    // Strip zero entries.
    result.retain(|_, v| !v.is_zero());
    result
}

/// Right-multiply by `T_{s_i}^{-1} = T_{s_i} − (q − q^{-1})`.
pub fn hecke_mul_ts_inv_right(x: &HeckeElement, i: usize) -> HeckeElement {
    let h = LaurentPolyQ::hecke_h();
    // x · T_{s_i}^{-1} = x · T_{s_i} − (q − q^{-1}) · x.
    let mut result = hecke_mul_ts_right(x, i);
    for (w, c) in x {
        let h_c = h.clone() * c.clone();
        let entry = result.entry(w.clone()).or_insert_with(LaurentPolyQ::zero);
        *entry -= &h_c;
    }
    result.retain(|_, v| !v.is_zero());
    result
}

/// Convert a braid word `[(sign, gen_1based), ...]` on `n` strands
/// into its expansion `T_β = Σ c_w(q) · T_w` in the Hecke basis.
pub fn braid_to_hecke(n: usize, word: &[(i32, u32)]) -> HeckeElement {
    let mut x = hecke_identity(n);
    for &(sign, gen) in word {
        let i = (gen as usize).saturating_sub(1);
        if i + 1 >= n {
            continue;
        }
        x = if sign >= 0 {
            hecke_mul_ts_right(&x, i)
        } else {
            hecke_mul_ts_inv_right(&x, i)
        };
    }
    x
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn perm_identity() {
        let id = Perm::identity(4);
        assert_eq!(id.length(), 0);
    }

    #[test]
    fn perm_length() {
        // s_0 (swap 0, 1): one inversion.
        let mut p = Perm::identity(3);
        p.apply_s_right(0);
        assert_eq!(p.length(), 1);
        // s_0 s_1 = (0 1)(1 2) in one-line: identity → s_0 → s_0 s_1.
        // After s_0: [1, 0, 2].  After s_1 (right): swap pos 1, 2 → [1, 2, 0].
        // Inversions of [1, 2, 0]: (1, 2) ↛, (1, 0) ✓, (2, 0) ✓ → 2 inversions.
        p.apply_s_right(1);
        assert_eq!(p.length(), 2);
    }

    #[test]
    fn hecke_identity_basis() {
        let id = hecke_identity(3);
        assert_eq!(id.len(), 1);
        let e = Perm::identity(3);
        assert!(id.contains_key(&e));
    }

    #[test]
    fn hecke_t_s_squared() {
        // T_{s_0}² = q² · T_e + (q − q^{-1}) · T_{s_0}.
        // (Hecke relation: T_s² = (q − q^{-1}) T_s + q · 1, but with
        // our conventions T_s² = q + (q − q⁻¹) T_s ... wait depends on
        // normalisation.)
        // Check: starting from 1, apply T_{s_0}, apply T_{s_0} again.
        let id = hecke_identity(3);
        let after_one = hecke_mul_ts_right(&id, 0);
        // After one s_0: just T_{s_0}, coefficient 1.
        assert_eq!(after_one.len(), 1);
        let s0 = Perm({
            let mut v = Perm::identity(3).0;
            v.swap(0, 1);
            v
        });
        assert_eq!(after_one.get(&s0), Some(&LaurentPolyQ::one()));

        let after_two = hecke_mul_ts_right(&after_one, 0);
        // T_{s_0} · T_{s_0}: ℓ(s_0 s_0) = 0 < 1 = ℓ(s_0).
        // So T_{s_0}² = T_e + (q − q^{-1}) · T_{s_0}.
        assert_eq!(after_two.len(), 2);
        assert_eq!(after_two.get(&Perm::identity(3)),
                   Some(&LaurentPolyQ::one()));
        assert_eq!(after_two.get(&s0), Some(&LaurentPolyQ::hecke_h()));
    }

    #[test]
    fn braid_word_to_hecke_simple() {
        // σ_1 σ_2 on 3 strands.
        let result = braid_to_hecke(3, &[(1, 1), (1, 2)]);
        // σ_1 σ_2 = s_0 s_1: one element, w = s_0 s_1 with one-line
        // form: id → s_0 → s_0 s_1 → ...
        // After s_0: [1, 0, 2].
        // After s_1 (right): swap pos 1, 2 → [1, 2, 0].
        let expected = Perm(vec![1, 2, 0]);
        assert_eq!(result.len(), 1);
        assert_eq!(result.get(&expected), Some(&LaurentPolyQ::one()));
    }

    #[test]
    fn inverse_generator() {
        // T_{s_0} · T_{s_0}^{-1} = T_e.
        let id = hecke_identity(3);
        let after_pos = hecke_mul_ts_right(&id, 0);
        let after_neg = hecke_mul_ts_inv_right(&after_pos, 0);
        // Should reduce to just T_e.
        assert_eq!(after_neg.len(), 1, "after positive*inverse = identity");
        assert_eq!(after_neg.get(&Perm::identity(3)), Some(&LaurentPolyQ::one()));
    }
}
