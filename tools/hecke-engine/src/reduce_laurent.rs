//! GS reduce loop for `LaurentHeckeElement`: rules R1, R2, R3.
//!
//! Port of `folio-assistant/computations/hecke_laurent_fast.py::
//! reduce_laurent_rules` (lines 119-213). Mirrors the structure
//! exactly — per-word, scan for the first rule that applies, rewrite,
//! continue. Fixpoint when a full pass produces no change.
//!
//! **R1 (Hecke quadratic):** `σ_i² → (q − q^{-1}) · σ_i + 1` at any
//! adjacent `(i, i)` with `i ≥ 0`.
//!
//! **R2 (far-comm + neg-gen commute):** `σ_i σ_j → σ_j σ_i` when
//! either (i) `i ≥ 0` and `j < 0` (formal variable commutes with a
//! Hecke generator) or (ii) `|i − j| ≥ 2` with `i > j` and both
//! `≥ 0` (far-apart Hecke generators commute; rewrite to lex-smaller).
//!
//! **R3 (Yang-Baxter to lex-smaller triple):** `σ_a σ_b σ_a →
//! σ_b σ_a σ_b` when `|a − b| = 1`, both `≥ 0`, and the new triple
//! `(b, a, b)` is lex-smaller than `(a, b, a)`.
//!
//! **R4 (whole-atom / sub-word quotient folding) is NOT here** — by
//! design; the LaurentQ inner loop is fast enough without it. See the
//! comment in `hecke_laurent_fast.py:230-246` for the rationale.
//!
//! Returns `(reduced_element, iter_count)` so callers can spot a
//! non-terminating loop (rare; usually only when `max_iterations`
//! is set too low).

use crate::laurent_hecke_element::{LaurentHeckeElement, Word};
use crate::laurent_rational_q::LaurentRationalQ;

/// Default per-step iteration cap, matching the Python default
/// (`max_iterations=10000` in `reduce_laurent_rules`).
pub const DEFAULT_MAX_ITERATIONS: usize = 10_000;

/// Apply R1/R2/R3 to a `LaurentHeckeElement` until fixpoint or
/// `max_iterations`. Returns the reduced element and the number of
/// iterations actually used (a no-op pass counts as one iteration).
///
/// The reduction is deterministic: at each iteration, every word in
/// the current element is examined in BTreeMap order; for each, the
/// first applicable rule wins. This matches the Python reference's
/// `for word, coeff in terms.items(): ... break` structure.
pub fn reduce_laurent_rules(
    elem: &LaurentHeckeElement,
    max_iterations: usize,
) -> (LaurentHeckeElement, usize) {
    let mut terms: LaurentHeckeElement = elem.clone();
    let hecke_a: LaurentRationalQ = LaurentRationalQ::hecke_a();
    let mut iteration = 0usize;
    let mut changed = true;

    while changed && iteration < max_iterations {
        changed = false;
        let mut new_terms = LaurentHeckeElement::zero();

        // Drain `terms` so we can iterate without borrowing it twice.
        let drained: Vec<(Word, LaurentRationalQ)> =
            std::mem::take(&mut terms.terms).into_iter().collect();

        for (word, coeff) in drained {
            if coeff.is_zero() {
                continue;
            }

            // R1: Hecke σ_i² → h · σ_i + 1
            if let Some(pos) = find_r1(&word) {
                let i = word[pos];
                let mut w1 = Vec::with_capacity(word.len() - 1);
                w1.extend_from_slice(&word[..pos]);
                w1.push(i);
                w1.extend_from_slice(&word[pos + 2..]);

                let mut w2 = Vec::with_capacity(word.len().saturating_sub(2));
                w2.extend_from_slice(&word[..pos]);
                w2.extend_from_slice(&word[pos + 2..]);

                let c1 = &coeff * &hecke_a;
                new_terms.accumulate(w1, c1);
                new_terms.accumulate(w2, coeff);
                changed = true;
                continue;
            }

            // R2: σ_i σ_j → σ_j σ_i (far-comm or neg-gen commute)
            if let Some(pos) = find_r2(&word) {
                let mut nw = word.clone();
                nw.swap(pos, pos + 1);
                new_terms.accumulate(nw, coeff);
                changed = true;
                continue;
            }

            // R3: Yang-Baxter to lex-smaller (a, b, a) → (b, a, b)
            if let Some(pos) = find_r3(&word) {
                let a = word[pos];
                let b = word[pos + 1];
                let mut nw = Vec::with_capacity(word.len());
                nw.extend_from_slice(&word[..pos]);
                nw.push(b);
                nw.push(a);
                nw.push(b);
                nw.extend_from_slice(&word[pos + 3..]);
                new_terms.accumulate(nw, coeff);
                changed = true;
                continue;
            }

            // No rule fired — word passes through unchanged.
            new_terms.accumulate(word, coeff);
        }

        terms = new_terms;
        iteration += 1;
    }

    (terms, iteration)
}

/// Find the leftmost position `p` where R1 applies (adjacent equal
/// non-negative gens). Returns `None` if no such position exists.
#[inline]
fn find_r1(word: &[i32]) -> Option<usize> {
    for p in 0..word.len().saturating_sub(1) {
        if word[p] == word[p + 1] && word[p] >= 0 {
            return Some(p);
        }
    }
    None
}

/// Find the leftmost position `p` where R2 applies (commute to
/// lex-smaller). Returns `None` if no such position exists.
///
/// R2 fires when either:
/// - `word[p] ≥ 0` and `word[p+1] < 0` (Hecke gen meets formal var)
/// - `word[p] > word[p+1]`, both `≥ 0`, and `|word[p] − word[p+1]| ≥ 2`
///   (far-apart Hecke generators in wrong lex order)
#[inline]
fn find_r2(word: &[i32]) -> Option<usize> {
    for p in 0..word.len().saturating_sub(1) {
        let ig = word[p];
        let jg = word[p + 1];
        let swap = (ig >= 0 && jg < 0)
            || ((ig - jg).abs() >= 2 && ig > jg && ig >= 0 && jg >= 0);
        if swap {
            return Some(p);
        }
    }
    None
}

/// Find the leftmost position `p` where R3 applies (Yang-Baxter to
/// lex-smaller). Returns `None` if no such position exists.
///
/// R3 fires at a triple `(a, b, a)` with `a, b ≥ 0`, `|a − b| = 1`,
/// and `(b, a, b) < (a, b, a)` lex. The latter holds iff `b < a`.
#[inline]
fn find_r3(word: &[i32]) -> Option<usize> {
    for p in 0..word.len().saturating_sub(2) {
        let a = word[p];
        let b = word[p + 1];
        let c = word[p + 2];
        if a == c && a >= 0 && b >= 0 && (a - b).abs() == 1 && b < a {
            return Some(p);
        }
    }
    None
}

// ── Tests ─────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;
    use num_bigint::BigInt;
    use num_rational::BigRational;

    fn lq_one() -> LaurentRationalQ {
        LaurentRationalQ::one()
    }
    fn lq_int(n: i64) -> LaurentRationalQ {
        LaurentRationalQ::from_int(BigInt::from(n))
    }

    #[test]
    fn r1_finds_adjacent_squared() {
        assert_eq!(find_r1(&[0, 0, 1]), Some(0));
        assert_eq!(find_r1(&[1, 0, 0]), Some(1));
        assert_eq!(find_r1(&[]), None);
        assert_eq!(find_r1(&[0]), None);
        assert_eq!(find_r1(&[0, 1, 0]), None);
        // Negative gens are formal variables — R1 does NOT apply.
        assert_eq!(find_r1(&[-1, -1, 0]), None);
    }

    #[test]
    fn r2_finds_far_comm_and_neg() {
        // i ≥ 0, j < 0 → commute
        assert_eq!(find_r2(&[0, -1]), Some(0));
        // 3, 0: far-comm, 3 > 0 → commute
        assert_eq!(find_r2(&[3, 0]), Some(0));
        // 0, 3: lex-smaller already, no commute
        assert_eq!(find_r2(&[0, 3]), None);
        // 1, 0: |i−j|=1 — adjacent Hecke gens DO NOT commute (R3 territory)
        assert_eq!(find_r2(&[1, 0]), None);
        // neg, pos: do not swap (we don't pull a neg gen LEFT past a pos)
        assert_eq!(find_r2(&[-1, 0]), None);
        assert_eq!(find_r2(&[]), None);
        assert_eq!(find_r2(&[0]), None);
    }

    #[test]
    fn r3_finds_yang_baxter_when_lex_reducing() {
        // (1, 0, 1): a=1, b=0, |a-b|=1, b<a → swap to (0,1,0)
        assert_eq!(find_r3(&[1, 0, 1]), Some(0));
        // (0, 1, 0): a=0, b=1, b>a → already lex-min, no rewrite
        assert_eq!(find_r3(&[0, 1, 0]), None);
        // (2, 1, 2): swap
        assert_eq!(find_r3(&[2, 1, 2]), Some(0));
        // (2, 3, 2): a=2, b=3, b>a → no
        assert_eq!(find_r3(&[2, 3, 2]), None);
        // (0, 2, 0): |a-b|=2, not Yang-Baxter
        assert_eq!(find_r3(&[0, 2, 0]), None);
    }

    #[test]
    fn reduce_identity_is_fixpoint() {
        let id = LaurentHeckeElement::identity();
        let (r, _) = reduce_laurent_rules(&id, 100);
        assert_eq!(r, id);
    }

    #[test]
    fn reduce_r1_single_square() {
        // σ_0² → h σ_0 + 1, where h = q − q^{-1}.
        let e = LaurentHeckeElement::monomial(vec![0, 0], lq_one());
        let (r, _) = reduce_laurent_rules(&e, 100);
        assert_eq!(r.n_terms(), 2);
        // word [0] should have coefficient h
        assert_eq!(r.terms[&vec![0]], LaurentRationalQ::hecke_a());
        // empty word should have coefficient 1
        assert_eq!(r.terms[&vec![]], lq_one());
    }

    #[test]
    fn reduce_r1_with_prefix_suffix() {
        // σ_1 σ_0 σ_0 σ_1 → h σ_1 σ_0 σ_1 + σ_1 σ_1 → R1 fires again on
        // the σ_1 σ_1 at the right.  Then R3 may reorder.  Just check
        // it terminates and the result is non-trivial.
        let e = LaurentHeckeElement::monomial(vec![1, 0, 0, 1], lq_one());
        let (r, iters) = reduce_laurent_rules(&e, 100);
        assert!(iters < 100, "should reach fixpoint quickly");
        assert!(!r.is_zero());
    }

    #[test]
    fn reduce_r2_far_comm_reorders_to_lex_smallest() {
        // σ_2 σ_0 → σ_0 σ_2 (|2−0|=2, swap)
        let e = LaurentHeckeElement::monomial(vec![2, 0], lq_one());
        let (r, _) = reduce_laurent_rules(&e, 100);
        assert_eq!(r.n_terms(), 1);
        assert_eq!(r.terms[&vec![0, 2]], lq_one());
    }

    #[test]
    fn reduce_r2_neg_gen_commutes_past_pos() {
        // σ_0 · v(-1) → v(-1) · σ_0
        let e = LaurentHeckeElement::monomial(vec![0, -1], lq_one());
        let (r, _) = reduce_laurent_rules(&e, 100);
        assert_eq!(r.n_terms(), 1);
        assert_eq!(r.terms[&vec![-1, 0]], lq_one());
    }

    #[test]
    fn reduce_r3_yang_baxter_to_lex_smaller() {
        // σ_1 σ_0 σ_1 → σ_0 σ_1 σ_0
        let e = LaurentHeckeElement::monomial(vec![1, 0, 1], lq_one());
        let (r, _) = reduce_laurent_rules(&e, 100);
        assert_eq!(r.n_terms(), 1);
        assert_eq!(r.terms[&vec![0, 1, 0]], lq_one());
    }

    #[test]
    fn reduce_lex_min_form_is_fixpoint() {
        // σ_0 σ_1 σ_0 is already lex-min for the Yang-Baxter pair.
        let e = LaurentHeckeElement::monomial(vec![0, 1, 0], lq_one());
        let (r, _) = reduce_laurent_rules(&e, 100);
        assert_eq!(r, e);
    }

    #[test]
    fn reduce_terminates_on_proton_like_word() {
        // A proton-ish atomic word: a few σ_0, σ_1, σ_2 generators with
        // intentional R1/R2/R3 candidates. The point is fixpoint
        // termination within the cap, not the exact value.
        let raw = vec![0i32, 1, 0, 0, 2, 1, 2, 1, 1, 0];
        let e = LaurentHeckeElement::monomial(raw, lq_one());
        let (r, iters) = reduce_laurent_rules(&e, 10_000);
        assert!(iters < 10_000, "proton-like word should reduce quickly");
        // Output is non-zero (these rules preserve the underlying
        // Hecke-algebra element, which is non-zero for any non-trivial
        // word; never zero on H_n).
        assert!(!r.is_zero());
    }

    #[test]
    fn reduce_preserves_coefficient_linearity() {
        // (5 · σ_2 σ_0) should reduce to (5 · σ_0 σ_2).
        let e = LaurentHeckeElement::monomial(vec![2, 0], lq_int(5));
        let (r, _) = reduce_laurent_rules(&e, 100);
        assert_eq!(r.terms[&vec![0, 2]], lq_int(5));
    }

    #[test]
    fn reduce_handles_rational_coefficients_exactly() {
        // (1/2) · σ_0² → (1/2)·h · σ_0 + (1/2)·1
        let half = LaurentRationalQ::from_rational(BigRational::new(
            1.into(),
            2.into(),
        ));
        let e = LaurentHeckeElement::monomial(vec![0, 0], half.clone());
        let (r, _) = reduce_laurent_rules(&e, 100);
        // (q − q^{-1})/2 on the σ_0 term, 1/2 on the empty word.
        let half_h = &LaurentRationalQ::hecke_a() * &half;
        assert_eq!(r.terms[&vec![0]], half_h);
        assert_eq!(r.terms[&vec![]], half);
    }

    #[test]
    fn reduce_iter_cap_returned_when_exceeded() {
        // Setting max_iterations very low on a word that needs more
        // passes should still return (no panic) with iter == cap.
        // σ_2 σ_1 σ_0 needs two R2 swaps to reach σ_0 σ_1 σ_2... wait,
        // actually σ_2 σ_1 has |2-1|=1 so R2 doesn't fire there.
        // Use a word that we KNOW needs ≥ 2 passes: σ_3 σ_0 σ_2 σ_0
        // needs R2 on (3,0) and (2,0).
        let e = LaurentHeckeElement::monomial(vec![3, 0, 2, 0], lq_one());
        let (_r, iters) = reduce_laurent_rules(&e, 1);
        assert_eq!(iters, 1, "cap should be honored");
    }
}
