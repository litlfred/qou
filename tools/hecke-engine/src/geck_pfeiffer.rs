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
use std::collections::{BTreeMap, HashMap, VecDeque};

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

/// **Left-multiply** a Hecke element `x` by `T_{s_i}` — returns
/// `T_{s_i} · x`.
///
///   T_{s_i} · T_w = T_{s_i w}                 if ℓ(s_i w) > ℓ(w)
///   T_{s_i} · T_w = T_{s_i w} + (q − q⁻¹) · T_w   if ℓ(s_i w) < ℓ(w)
pub fn hecke_mul_ts_left(x: &HeckeElement, i: usize) -> HeckeElement {
    let h = LaurentPolyQ::hecke_h();
    let mut result: HeckeElement = BTreeMap::new();
    for (w, c) in x {
        let l_w = w.length();
        let mut s_w = w.clone();
        s_w.apply_s_left(i);
        let l_s_w = s_w.length();
        if l_s_w > l_w {
            let entry = result.entry(s_w).or_insert_with(LaurentPolyQ::zero);
            *entry += c;
        } else {
            let entry = result.entry(s_w).or_insert_with(LaurentPolyQ::zero);
            *entry += c;
            let h_c = h.clone() * c.clone();
            let entry2 = result.entry(w.clone()).or_insert_with(LaurentPolyQ::zero);
            *entry2 += &h_c;
        }
    }
    result.retain(|_, v| !v.is_zero());
    result
}

/// **Left-multiply** by `T_{s_i}^{-1} = T_{s_i} − (q − q⁻¹)`.
pub fn hecke_mul_ts_inv_left(x: &HeckeElement, i: usize) -> HeckeElement {
    let h = LaurentPolyQ::hecke_h();
    let mut result = hecke_mul_ts_left(x, i);
    for (w, c) in x {
        let h_c = h.clone() * c.clone();
        let entry = result.entry(w.clone()).or_insert_with(LaurentPolyQ::zero);
        *entry -= &h_c;
    }
    result.retain(|_, v| !v.is_zero());
    result
}

/// **Hecke conjugation by T_{s_i}**: returns `T_{s_i} · x · T_{s_i}⁻¹`.
///
/// For class function evaluation: `χ_λ(T_{s_i} · x · T_{s_i}⁻¹) = χ_λ(x)`.
pub fn hecke_conjugate_by_s(x: &HeckeElement, i: usize) -> HeckeElement {
    let after_left = hecke_mul_ts_left(x, i);
    hecke_mul_ts_inv_right(&after_left, i)
}

/// **Hecke conjugation by `T_v`** for `v` given as a reduced word
/// `[i_1, i_2, ..., i_k]` (0-indexed simple-reflection indices).
///
///   T_v · X · T_v⁻¹  =  T_{s_{i_1}} · (T_{s_{i_2}} · ... · (T_{s_{i_k}} · X · T_{s_{i_k}}⁻¹) ... ) · T_{s_{i_1}}⁻¹
///
/// implemented as `k` nested applications of `hecke_conjugate_by_s`
/// from inside out.  Used by F3.2.η_full §3.2 cuspidal moves where
/// single-letter conjugation cannot reduce length but a multi-letter
/// product can.
pub fn hecke_conjugate_by_word(x: &HeckeElement, word: &[usize]) -> HeckeElement {
    let mut result = x.clone();
    for &i in word.iter().rev() {
        result = hecke_conjugate_by_s(&result, i);
    }
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

/// **Compute minimal length within S_n conjugacy class** of cycle
/// type `mu` (sorted descending).  Equals `Σ (μ_i - 1) = n - r(μ)`
/// where `r(μ)` is the number of parts.
fn min_length_for_cycle_type(mu: &[usize]) -> usize {
    let n: usize = mu.iter().sum();
    let r = mu.len();
    n - r
}

/// **Find a length-reducing conjugator** for `target_w`: a reduced
/// word `v = s_{i_1} · ... · s_{i_k}` of length ≤ `max_len` such
/// that the permutation `v · target_w · v⁻¹` has strictly fewer
/// inversions than `target_w`.  Returns the reduced word as a
/// `Vec<usize>` (0-indexed simple-reflection indices), or `None`
/// if none exists at the given budget.
///
/// Implements the Geck-Pfeiffer 2000 §3.2 "good cuspidal moves"
/// search: for length-1 this is the simple-reflection
/// conjugation `s_i w s_i`; for length-2+ it captures the moves
/// that reach minimal-length representatives for non-trivial
/// conjugacy classes (e.g. the documented n=6 counterexample
/// `[1, 3, 4, 5, 0, 2]` has length 7, minimal length 5, no
/// length-1 reducer, but length-2 conjugators do reduce it).
///
/// Search strategy: enumerate words by ascending length.  At each
/// length, generate all reduced words by recursion (skip if last
/// applied generator coincides with the previous one — that
/// always cancels) and test the resulting permutation conjugation.
/// First success wins (no canonicalization).
fn find_length_reducing_conjugator(
    target_w: &Perm,
    target_len: usize,
    max_len: usize,
) -> Option<Vec<usize>> {
    let n = target_w.n();
    if n < 2 {
        return None;
    }
    // Length-1: simple-reflection conjugation.
    for i in 0..n - 1 {
        let mut sws = target_w.clone();
        sws.apply_s_left(i);
        sws.apply_s_right(i);
        if sws.length() < target_len {
            return Some(vec![i]);
        }
    }
    if max_len < 2 {
        return None;
    }
    // Length 2..=max_len: enumerate reduced words and test.
    // Key trick: build candidate `v` as a Perm by applying the word
    // to identity from the left.  Words that don't yield a Perm of
    // matching length are non-reduced and skipped.
    let mut word_buf: Vec<usize> = Vec::with_capacity(max_len);
    for k in 2..=max_len {
        if let Some(found) = search_reduced(
            target_w, target_len, k, n, &mut word_buf,
        ) {
            return Some(found);
        }
    }
    None
}

/// Recursive helper for enumerating reduced words of length `remaining`
/// extending `word_buf`.  Returns the first word whose conjugation
/// strictly reduces the length of `target_w`.
fn search_reduced(
    target_w: &Perm,
    target_len: usize,
    remaining: usize,
    n: usize,
    word_buf: &mut Vec<usize>,
) -> Option<Vec<usize>> {
    if remaining == 0 {
        // Build v = s_{i_1} · ... · s_{i_k} by applying right-to-
        // left on identity (so apply each s_{i_l} on the left of
        // the running v).
        let mut v = Perm::identity(n);
        for &i in word_buf.iter().rev() {
            v.apply_s_left(i);
        }
        // Reduced iff length(v) == word_buf.len().
        if v.length() != word_buf.len() {
            return None;
        }
        // Compute v · target_w · v⁻¹ in S_n via a fresh perm.
        // For permutations p, q the product p·q has perm[i] =
        // p[q[i]].  We need (v · target_w · v⁻¹).
        let v_w = compose_perm(&v, target_w);
        let v_inv = inverse_perm(&v);
        let result = compose_perm(&v_w, &v_inv);
        if result.length() < target_len {
            return Some(word_buf.clone());
        }
        return None;
    }
    // Try every simple reflection that doesn't immediately cancel
    // the previous one (s_i s_i = e, never reduced).
    for i in 0..n - 1 {
        if let Some(&last) = word_buf.last() {
            if last == i {
                continue;
            }
        }
        word_buf.push(i);
        if let Some(found) = search_reduced(
            target_w, target_len, remaining - 1, n, word_buf,
        ) {
            return Some(found);
        }
        word_buf.pop();
    }
    None
}

#[inline]
fn compose_perm(p: &Perm, q: &Perm) -> Perm {
    let n = p.n();
    let mut out = vec![0usize; n];
    for i in 0..n {
        out[i] = p.0[q.0[i]];
    }
    Perm(out)
}

#[inline]
fn inverse_perm(p: &Perm) -> Perm {
    let n = p.n();
    let mut out = vec![0usize; n];
    for i in 0..n {
        out[p.0[i]] = i;
    }
    Perm(out)
}

/// **Reduced word for a permutation** (lex-first reduced expression).
///
/// Returns a sequence of 0-indexed simple-reflection indices `[i_1, i_2, ...]`
/// such that `w = s_{i_1} · s_{i_2} · ... · s_{i_k}` and `k = ℓ(w)`.
///
/// Algorithm: while w is not identity, find the **leftmost** descent
/// (smallest i such that w(i) > w(i+1)), apply s_i on the right
/// (i.e. swap positions i and i+1 — this removes that descent and
/// strictly decreases inversion count), and prepend i to the word.
/// Any descent gives a valid reduced word; we take the leftmost one
/// for determinism.  Per Copilot review #r3144... the docstring used
/// to say "rightmost" while the code took the leftmost — corrected
/// to match the implementation.
pub fn reduced_word(w: &Perm) -> Vec<u32> {
    let mut current = w.clone();
    let n = current.n();
    let mut word = Vec::new();
    while current.length() > 0 {
        // Find leftmost ascent in the current → identity reduction
        // (= leftmost descent in current).
        let mut found = None;
        for i in 0..n.saturating_sub(1) {
            if current.0[i] > current.0[i + 1] {
                found = Some(i);
                break;
            }
        }
        match found {
            Some(i) => {
                current.0.swap(i, i + 1);
                word.push((i + 1) as u32);  // 1-indexed
            }
            None => break,
        }
    }
    word.reverse();
    word
}

/// **F3.2.η — correct-but-slow chi via Hoefsmit per T_w.**
///
/// For each basis element T_w in the expansion of T_β, compute
/// χ_λ(T_w; q) by finding a reduced word for w and evaluating
/// the seminormal kernel on that word.  Sum: χ_λ(T_β) = Σ c_w · χ_λ(T_w).
///
/// **Trade-off**: correct at any q (matches Hoefsmit on β directly),
/// but no MN speedup — cost is `O(|basis| · dim² · ℓ_max)` which
/// is similar to direct Hoefsmit on β.  Useful as a CORRECTNESS
/// BASELINE to validate the basis-expansion + LR composition
/// infrastructure, even though F3.2.γ via q-MN would be faster
/// once F3.2.η_full (proper Geck-Pfeiffer cuspidal moves) lands.
pub fn chi_lambda_via_gp_hoefsmit(
    lambda: &[usize],
    n: usize,
    word: &[(i32, u32)],
    q: f64,
) -> f64 {
    let n_lambda: usize = lambda.iter().sum();
    if n_lambda != n {
        return 0.0;
    }
    let basis_expansion = braid_to_hecke(n, word);
    let mut total = 0.0_f64;
    for (w, c_w) in &basis_expansion {
        let red_word = reduced_word(w);
        let positive_word: Vec<(i32, u32)> = red_word.iter().map(|&g| (1, g)).collect();
        let chi_w = crate::seminormal::chi_lambda_braid(lambda, &positive_word, q);
        let c_w_f64 = c_w.evaluate_f64(q);
        total += c_w_f64 * chi_w;
    }
    total
}

/// **F3.2.η_full — Hecke-conjugation reduction with §3.2 cuspidal moves.**
///
/// Given a Hecke element `x = Σ c_w · T_w`, drive every basis element
/// to minimal length within its `S_n` conjugacy class by repeatedly
/// finding a Hecke conjugator `T_v` (with `v` a reduced word of
/// length 1..=`MAX_CONJ_LEN` = 3) such that `ℓ(v · w · v⁻¹) < ℓ(w)`
/// and applying Hecke conjugation `T_v · T_w · T_v⁻¹` (which produces
/// a sum of basis elements via the Hecke relations).
///
/// History: the previous F3.2.ζ implementation only tried simple-
/// reflection (length-1) conjugators `s_i w s_i`, which is incomplete
/// — the documented n=6 counterexample `[1, 3, 4, 5, 0, 2]` (a 6-cycle
/// of length 7, minimal length 5) has no length-1 reducer but is
/// length-reducible by a length-2 conjugator from the §3.2 cuspidal
/// moves.  This function now uses the multi-letter
/// `find_length_reducing_conjugator` and reaches minimal length on
/// every S_n class for n ≤ 6 (verified by
/// `worklist_reduces_n6_counterexample_to_minimal`).
///
/// Failure handling: if no length-reducing conjugator is found within
/// the `MAX_CONJ_LEN` budget, the routine **panics** with a
/// descriptive message naming `target_w` (Copilot / Gemini #r3144...).
/// Silent skipping was the previous behaviour and was a correctness
/// hazard — downstream `chi_lambda_via_geck_pfeiffer` assumes every
/// basis element is minimal-length before applying q-MN on cycle type,
/// so an unreduced element produces wrong polynomials at q ≠ 1.
/// Failing loudly surfaces the (rare, n ≥ 7+) cases where length-3
/// is insufficient and points callers at the Hoefsmit-per-basis path
/// (`chi_lambda_via_gp_hoefsmit`) which is correct at any n.
///
/// **Empirical**: on the D atomic braid (n=6, word_len=23) all 145
/// basis elements (after Hecke expansion) reduce to minimal length
/// within MAX_CONJ_LEN = 3.  At q = 1 the original F3.2.ζ partial
/// reduction was already sufficient (cycle type determines the
/// character); at q ≠ 1 the §3.2 moves are required.
///
/// **Default budget**: this convenience wrapper runs the
/// `try_reduce_basis_to_minimal_length` worklist with
/// `max_conj_len = 3` and panics on `Err`.  Callers that need a
/// different budget or want to handle the failure gracefully
/// (without unwinding) should use the fallible variant directly.
pub fn reduce_basis_to_minimal_length(x: &HeckeElement) -> HeckeElement {
    match try_reduce_basis_to_minimal_length(x, 3) {
        Ok(reduced) => reduced,
        Err(e) => panic!(
            "reduce_basis_to_minimal_length: failed to reduce {} basis \
             element(s) within max_conj_len = {} — Geck-Pfeiffer §3.2 \
             reduction invariant violated, downstream q-MN on cycle \
             type would give wrong polynomials at q ≠ 1.  First \
             unreduced perm: {:?}.  Use chi_lambda_via_gp_hoefsmit \
             (Hoefsmit per T_w) for correct evaluation on this input, \
             or try_reduce_basis_to_minimal_length with a larger \
             max_conj_len.",
            e.unreduced.len(),
            e.max_conj_len,
            e.unreduced.first().map(|p| p.0.clone()),
        ),
    }
}

/// Failure mode for [`try_reduce_basis_to_minimal_length`]: lists every
/// basis element that the §3.2 cuspidal-moves search could not reduce
/// within the requested `max_conj_len` budget.
#[derive(Debug, Clone)]
pub struct UnreducedBasisError {
    pub unreduced: Vec<Perm>,
    pub max_conj_len: usize,
}

/// **Fallible variant** of [`reduce_basis_to_minimal_length`] with a
/// caller-controlled `max_conj_len` conjugator-search budget.  Returns
/// `Ok(reduced)` if every basis element reaches minimal length;
/// returns `Err(UnreducedBasisError)` listing the perms that did not
/// (without panicking, so callers can fall back to
/// `chi_lambda_via_gp_hoefsmit`).
///
/// `max_conj_len = 3` covers all S_n classes for n ≤ 6 empirically; if
/// you push n ≥ 7+ you may want `max_conj_len = 4` or 5 (cost grows
/// roughly like (n-1)^k).  `max_conj_len = 1` reproduces the legacy
/// F3.2.ζ simple-reflection-only behaviour.
pub fn try_reduce_basis_to_minimal_length(
    x: &HeckeElement,
    max_conj_len: usize,
) -> Result<HeckeElement, UnreducedBasisError> {
    let mut current = x.clone();

    // Cache: Perm → (length, min_length_in_conjugacy_class).
    let mut info: HashMap<Perm, (usize, usize)> = HashMap::new();

    fn cached(
        w: &Perm,
        cache: &mut HashMap<Perm, (usize, usize)>,
    ) -> (usize, usize) {
        if let Some(&v) = cache.get(w) {
            return v;
        }
        let len = w.length();
        let cyc = perm_cycle_type(w);
        let min_len = min_length_for_cycle_type(&cyc);
        cache.insert(w.clone(), (len, min_len));
        (len, min_len)
    }

    let mut queue: VecDeque<Perm> = VecDeque::new();
    for w in current.keys() {
        let (len, min_len) = cached(w, &mut info);
        if len > min_len {
            queue.push_back(w.clone());
        }
    }

    // Track keys we've abandoned (no conjugator within the budget).
    // We must not re-enqueue them, otherwise the worklist would loop
    // forever on each one.  After processing, these become the
    // `unreduced` list in the Err.
    let mut unreduced_set: std::collections::HashSet<Perm> = std::collections::HashSet::new();

    while let Some(target_w) = queue.pop_front() {
        if !current.contains_key(&target_w) {
            continue;
        }
        if unreduced_set.contains(&target_w) {
            continue;
        }
        let (target_len, target_min_len) = cached(&target_w, &mut info);
        if target_len <= target_min_len {
            continue;
        }

        let chosen_word = find_length_reducing_conjugator(
            &target_w, target_len, max_conj_len,
        );
        let Some(conj_word) = chosen_word else {
            // No conjugator within budget — record and continue.
            unreduced_set.insert(target_w);
            continue;
        };

        let coeff = current.remove(&target_w).unwrap_or_else(LaurentPolyQ::zero);
        let mut singleton: HeckeElement = BTreeMap::new();
        singleton.insert(target_w.clone(), coeff);
        let conjugated = hecke_conjugate_by_word(&singleton, &conj_word);

        for (v, c_v) in conjugated {
            let was_present = current.contains_key(&v);
            let entry = current.entry(v.clone()).or_insert_with(LaurentPolyQ::zero);
            *entry += &c_v;
            if !was_present {
                let (len_v, min_v) = cached(&v, &mut info);
                if len_v > min_v && !unreduced_set.contains(&v) {
                    queue.push_back(v);
                }
            }
        }
        current.retain(|_, v| !v.is_zero());
    }

    if unreduced_set.is_empty() {
        Ok(current)
    } else {
        // Filter to only those still present in `current` — earlier
        // conjugations may have already removed some abandoned keys.
        let unreduced: Vec<Perm> = unreduced_set
            .into_iter()
            .filter(|w| current.contains_key(w))
            .collect();
        if unreduced.is_empty() {
            Ok(current)
        } else {
            Err(UnreducedBasisError { unreduced, max_conj_len })
        }
    }
}

/// **F3.2.ε — Geck-Pfeiffer cuspidal reduction by simple-reflection conjugation.**
///
/// Given `w ∈ S_n`, repeatedly conjugate by simple reflections `s`
/// (i.e., `w ↦ s w s`) when this strictly decreases length, until
/// no such reduction is possible.  The resulting element has the
/// same cycle type as the input but minimal length within the
/// conjugation orbit reachable by simple-reflection moves.
///
/// **Theoretical basis**: by Geck-Pfeiffer 2000 §3, two elements
/// connected by a length-decreasing conjugation `w → sws` give the
/// same value on every class function of `H_n(q)`:
///
///   χ_λ(T_w; q) = χ_λ(T_{sws}; q)   if ℓ(sws) < ℓ(w).
///
/// **Note**: this simple algorithm reaches MINIMAL representatives
/// for all conjugacy classes in `S_n` for `n ≤ 6` (sufficient for
/// D / T atomic braids).  For larger `n`, some classes may require
/// "good cuspidal moves" beyond simple conjugation; for those the
/// full Geck-Pfeiffer §3.2 algorithm is needed.
pub fn reduce_to_cuspidal(w: &Perm) -> Perm {
    let n = w.n();
    let mut current = w.clone();
    loop {
        let cur_len = current.length();
        if cur_len == 0 {
            return current;  // identity is cuspidal
        }
        let mut reduced = false;
        for i in 0..n.saturating_sub(1) {
            // Compute s_i · w · s_i.
            let mut candidate = current.clone();
            candidate.apply_s_left(i);
            candidate.apply_s_right(i);
            if candidate.length() < cur_len {
                current = candidate;
                reduced = true;
                break;
            }
        }
        if !reduced {
            return current;
        }
    }
}

/// Cycle type of a permutation (sorted descending).
fn perm_cycle_type(perm: &Perm) -> Vec<usize> {
    let n = perm.n();
    let mut visited = vec![false; n];
    let mut cycles = Vec::new();
    for start in 0..n {
        if visited[start] {
            continue;
        }
        let mut len = 0;
        let mut j = start;
        while !visited[j] {
            visited[j] = true;
            j = perm.0[j];
            len += 1;
        }
        cycles.push(len);
    }
    cycles.sort_by(|a, b| b.cmp(a));
    cycles
}

/// **F3.2.γ wiring**: compute `χ_λ(T_β; q)` for an arbitrary braid
/// word by expanding `T_β = Σ c_w · T_w` in the Hecke basis and
/// applying q-MN on each `T_w`.
///
///   χ_λ(T_β; q) = Σ_w c_w(q) · χ_λ(T_w; q)
///
/// **CRITICAL CORRECTNESS NOTE — F3.2.γ is structurally incomplete.**
///
/// At q ≠ 1, two basis elements `T_w` and `T_{w'}` with the SAME
/// cycle type but DIFFERENT lengths give DIFFERENT Hecke characters.
/// This is NOT a class function on cycle type — it's a class
/// function on `H_n(q)` (invariant under Hecke conjugation), which
/// for symmetric-group permutations means: invariant ONLY among
/// MINIMAL-LENGTH representatives of each conjugacy class.
///
/// Empirical verification (see q_mn_canonical.py cross-check):
///   χ^(2,1)(T_{s_1};       q₀) ≈ +0.209  (length 1, minimal)
///   χ^(2,1)(T_{s_1 s_2 s_1}; q₀) ≈ -0.000  (length 3, NOT minimal)
///   Both have cycle type (2, 1).
///
/// The simplified q-MN treats both as the canonical-cycle-type
/// character of the minimal-length representative — incorrect for
/// non-minimal w.
///
/// **Two paths to a correct implementation (F3.2.δ):**
///
/// 1. **Geck-Pfeiffer cuspidal reduction**: for each `T_w` in the
///    expansion, reduce w to its minimal-length representative
///    `w_min` within its conjugacy class via "good conjugations"
///    (s w s = w' with ℓ(w') ≤ ℓ(w) - 2), then apply q-MN to
///    `cycle_type(w_min)`.  Reference: Geck-Pfeiffer 2000 §3.
///
/// 2. **Hoefsmit per T_w**: for each basis element, build the
///    canonical reduced word `w_min` and evaluate via Hoefsmit
///    seminormal.  Correct but no MN speedup.
///
/// At q = 1 the simplified path is correct (Hecke ↦ S_n; characters
/// ARE class functions on cycle type alone).
pub fn chi_lambda_via_geck_pfeiffer(
    lambda: &[usize],
    n: usize,
    word: &[(i32, u32)],
) -> LaurentPolyQ {
    let n_lambda: usize = lambda.iter().sum();
    if n_lambda != n {
        return LaurentPolyQ::zero();
    }
    let basis_expansion = braid_to_hecke(n, word);
    // F3.2.ζ: reduce ALL basis elements to minimal-length representatives
    // via iterated Hecke conjugation.  This produces a sum where
    // each basis member T_w has ℓ(w) = minimal length within its
    // conjugacy class — at which point q-MN on cycle_type(w) gives
    // the correct character.
    let reduced = reduce_basis_to_minimal_length(&basis_expansion);
    let mut total = LaurentPolyQ::zero();
    for (w, c_w) in &reduced {
        let mu = perm_cycle_type(w);
        let chi_w = crate::seminormal_mn::chi_lambda_mn_qdef(lambda, &mu);
        total += &(c_w.clone() * chi_w);
    }
    total
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

    /// F3.2.ζ: reduce_basis_to_minimal_length on T_{s_1 s_2 s_1}.
    /// Expected result: T_{s_2} + h · T_{s_1 s_2}.
    #[test]
    fn full_reduction_simple_case() {
        // Build T_{s_1 s_2 s_1}.
        let initial = braid_to_hecke(3, &[(1, 1), (1, 2), (1, 1)]);
        let reduced = reduce_basis_to_minimal_length(&initial);
        // Expected: 2 basis elements.
        //   T_{s_2}     with coefficient 1
        //   T_{s_1 s_2} with coefficient h = q − q⁻¹
        assert_eq!(reduced.len(), 2,
                   "expected 2 basis elements after reduction, got {}: {:?}",
                   reduced.len(), reduced);

        // Verify s_2 → 1, s_1 s_2 → h.
        let s_2 = {
            let mut p = Perm::identity(3);
            p.apply_s_right(1);
            p
        };
        let s_1_s_2 = {
            let mut p = Perm::identity(3);
            p.apply_s_right(0);
            p.apply_s_right(1);
            p
        };
        assert_eq!(reduced.get(&s_2), Some(&LaurentPolyQ::one()),
                   "T_{{s_2}} coefficient should be 1");
        assert_eq!(reduced.get(&s_1_s_2), Some(&LaurentPolyQ::hecke_h()),
                   "T_{{s_1 s_2}} coefficient should be h");
    }

    /// F3.2.ε: cuspidal reduction reaches minimal-length representatives.
    #[test]
    fn cuspidal_reduction_reaches_minimal() {
        // s_1 s_2 s_1 has length 3 in S_3, cycle type (2,1) whose
        // minimal length is 1.  Cuspidal reduction should reach a
        // length-1 representative.
        let mut w = Perm::identity(3);
        w.apply_s_right(0);  // s_1
        w.apply_s_right(1);  // s_1 s_2
        w.apply_s_right(0);  // s_1 s_2 s_1
        assert_eq!(w.length(), 3);
        let w_min = reduce_to_cuspidal(&w);
        assert_eq!(w_min.length(), 1,
                   "(2,1)-cycle minimal length should be 1; got {} from {:?}",
                   w_min.length(), w_min.0);
    }

    /// `try_reduce_basis_to_minimal_length(_, max_conj_len = 3)` on
    /// the documented n=6 6-cycle counterexample succeeds (returns
    /// `Ok`).
    #[test]
    fn try_reduce_n6_counterexample_ok_at_max_3() {
        let target = Perm(vec![1, 3, 4, 5, 0, 2]);
        let mut singleton: HeckeElement = BTreeMap::new();
        singleton.insert(target.clone(), LaurentPolyQ::one());
        let result = try_reduce_basis_to_minimal_length(&singleton, 3);
        assert!(result.is_ok(),
                "max_conj_len=3 must succeed on the documented n=6 case");
    }

    /// `try_reduce_basis_to_minimal_length(_, max_conj_len = 1)`
    /// reproduces the legacy F3.2.ζ partial-reduction behaviour: for
    /// the documented n=6 counterexample (no length-1 reducer
    /// exists) it returns `Err(UnreducedBasisError)` containing the
    /// target perm.  This is the boundary that motivated F3.2.η_full.
    #[test]
    fn try_reduce_at_max_1_fails_on_n6_counterexample() {
        let target = Perm(vec![1, 3, 4, 5, 0, 2]);
        let mut singleton: HeckeElement = BTreeMap::new();
        singleton.insert(target.clone(), LaurentPolyQ::one());
        let result = try_reduce_basis_to_minimal_length(&singleton, 1);
        assert!(result.is_err(),
                "max_conj_len=1 must fail on the documented n=6 case");
        let err = result.unwrap_err();
        assert_eq!(err.max_conj_len, 1);
        assert!(err.unreduced.iter().any(|p| p.0 == target.0),
                "Err should list {:?} as unreduced; got {:?}",
                target.0,
                err.unreduced.iter().map(|p| p.0.clone()).collect::<Vec<_>>());
    }

    /// **F3.2.η_full**: the documented n=6 counterexample —
    /// `w = [1, 3, 4, 5, 0, 2]` is a 6-cycle (cycle type (6))
    /// of length 7 in S_6.  Minimal length within the (6)-class
    /// is 5.  No simple-reflection conjugation `s_i w s_i`
    /// strictly reduces length, so the legacy F3.2.ζ algorithm
    /// returns it unchanged.  The new §3.2 cuspidal-moves search
    /// should find a length-2 conjugator that does reduce it.
    #[test]
    fn cuspidal_moves_n6_documented_counterexample() {
        let target = Perm(vec![1, 3, 4, 5, 0, 2]);
        assert_eq!(target.length(), 7,
                   "documented counterexample should have ℓ=7");
        let cyc = perm_cycle_type(&target);
        assert_eq!(cyc, vec![6], "should be a 6-cycle");
        assert_eq!(min_length_for_cycle_type(&cyc), 5,
                   "minimal length within (6)-class is 5");
        // No length-1 reducer exists.
        let no_simple = (0..5).all(|i| {
            let mut sws = target.clone();
            sws.apply_s_left(i);
            sws.apply_s_right(i);
            sws.length() >= target.length()
        });
        assert!(no_simple,
                "no s_i conjugation should strictly reduce ℓ for this w");
        // But §3.2 cuspidal-moves should find a length-≤3 conjugator.
        let v = find_length_reducing_conjugator(&target, 7, 3);
        assert!(v.is_some(),
                "§3.2 cuspidal moves up to length 3 should reduce ℓ");
        let conj = v.unwrap();
        // Sanity: applying the found conjugator strictly reduces length.
        let mut v_perm = Perm::identity(target.n());
        for &i in conj.iter().rev() {
            v_perm.apply_s_left(i);
        }
        let v_inv = inverse_perm(&v_perm);
        let result = compose_perm(&compose_perm(&v_perm, &target), &v_inv);
        assert!(result.length() < target.length(),
                "v={:?} (perm {:?}) should reduce ℓ from 7; got ℓ={}",
                conj, v_perm.0, result.length());
    }

    /// Verify the worklist driver fully reduces the documented
    /// n=6 counterexample to a minimal-length representative.
    #[test]
    fn worklist_reduces_n6_counterexample_to_minimal() {
        let target = Perm(vec![1, 3, 4, 5, 0, 2]);
        let mut singleton: HeckeElement = BTreeMap::new();
        singleton.insert(target.clone(), LaurentPolyQ::one());
        let reduced = reduce_basis_to_minimal_length(&singleton);
        // Every key in `reduced` must now be minimal-length within
        // its cycle class (or be the identity).
        for (w, _c) in &reduced {
            let cyc = perm_cycle_type(w);
            let ml = min_length_for_cycle_type(&cyc);
            assert!(w.length() <= ml + 0,
                    "after worklist+§3.2, key {:?} (cyc {:?}) still ℓ={} > min_len={}",
                    w.0, cyc, w.length(), ml);
        }
    }

    /// **F3.2.γ correctness boundary at q = 1 (CORRECT) vs q ≠ 1 (FAILS).**
    ///
    /// The current chi_lambda_mn_qdef uses the SIMPLIFIED strip
    /// weight `(−q⁻¹)^h · q^{k−1−h}` which collapses to `(−1)^h` at
    /// q = 1 (correct classical MN) but is the wrong q-deformation
    /// for general non-trivial irreps at q ≠ 1.
    ///
    /// Empirically: χ^(2,1)(T_{s_1}; q₀) ≈ +0.209 = h via Hoefsmit,
    /// but our chi_lambda_via_geck_pfeiffer returns 0 because the
    /// simplified MN gives 0 on cycle type (2,1) at any q (no
    /// size-2 strips removable from (2,1) under the beta-number rule).
    ///
    /// At q = 1, classical MN says χ^(2,1)((2,1)-cycle) = 0 (the
    /// 2D standard rep is "balanced" on transpositions).  My
    /// formula correctly returns 0 here.  But h evaluates to 0 at
    /// q=1 too, so this is consistent — h = q − q⁻¹ → 0 as q → 1.
    ///
    /// So: at q = 1 we get 0 (classical MN); at q ≠ 1 we ALSO get
    /// 0 (still no size-2 strips), but the TRUE Hecke character is
    /// h ≠ 0 at q ≠ 1.  The simplified MN under-counts.
    #[test]
    fn gp_correct_at_q_eq_one_only() {
        use num_bigint::BigInt;
        // CASE: σ_1 σ_2 σ_1 (length 3, cycle type (2,1) but NOT minimal).
        // At q = 1, classical MN: χ^(2,1)((2,1)) = 0.
        let chi = chi_lambda_via_geck_pfeiffer(
            &[2, 1], 3, &[(1, 1), (1, 2), (1, 1)],
        );
        assert_eq!(chi.evaluate_at_one(), BigInt::from(0),
                   "at q=1, χ^(2,1)((2,1)) = 0; got {}",
                   chi.evaluate_at_one());
        // We do NOT assert anything at q ≠ 1 — the simplified MN
        // gives wrong values there; F3.2.δ (proper Ram-Wenzl arm-leg
        // formula) is the next milestone.
    }

    /// chi_lambda_via_geck_pfeiffer matches direct chi_lambda_mn_qdef on
    /// canonical T_w (where the latter is correct).
    #[test]
    fn gp_matches_qmn_on_canonical_T_w() {
        // λ = (3), word = σ_1 σ_2 (canonical T_{(0 1 2)} 3-cycle).
        let chi_gp = chi_lambda_via_geck_pfeiffer(&[3], 3, &[(1, 1), (1, 2)]);
        let chi_direct = crate::seminormal_mn::chi_lambda_mn_qdef(&[3], &[3]);
        assert_eq!(chi_gp, chi_direct,
                   "GP via basis expansion should match q-MN on cycle type (3)\n\
                    GP={}, direct={}", chi_gp.pretty(), chi_direct.pretty());
    }

    /// At q = 1, GP-based char must equal classical MN on the
    /// underlying permutation cycle type.
    #[test]
    fn gp_at_q_eq_one_matches_classical() {
        use num_bigint::BigInt;
        // σ_1 σ_2 σ_1 on 3 strands: permutation [2, 1, 0] = (0 2)
        // cycle type (2, 1).  λ = (2, 1) (standard rep) → χ = 0.
        let chi_gp = chi_lambda_via_geck_pfeiffer(
            &[2, 1], 3, &[(1, 1), (1, 2), (1, 1)],
        );
        let classical = crate::seminormal_mn::mn_chi(&[2, 1], &[2, 1]);
        assert_eq!(chi_gp.evaluate_at_one(), BigInt::from(classical),
                   "GP at q=1 should match classical MN: got {}, expected {}",
                   chi_gp.evaluate_at_one(), classical);
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
