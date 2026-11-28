//! End-to-end MPFR evaluation of `tr_M(β_atomic(Z, N), q₀)`.
//!
//! Combines:
//! - Tier 1.A reduce ([`crate::reduce_laurent::incremental_reduce`])
//! - Phase-2 trace recursion ([`crate::tr_m_word_lq::tr_m_word_lq`])
//! - MPFR-precision substitution at `q₀`
//!
//! into ONE Rust function callable through ONE PyO3 binding.  The
//! caller ships `(signed_word, n_strands, q_str, dps)` and gets back
//! a single decimal string for `mpmath.mpf` to parse on the Python
//! side.  No per-word PyO3 calls; no Python mpmath combine loop;
//! no Python ↔ Rust shuttling of BigInt decimal strings per
//! coefficient.
//!
//! This is the user-directed "put all that in rust" / "stop back
//! and forth rust and python of data" closure of Tier 1.A.
//!
//! Per AGENTS.md §Precision goals L1 (50-dps compute floor): every
//! intermediate quantity is exact (BigRational / BigInt) up to the
//! final MPFR substitution; precision is set by the `dps` argument
//! (production default 50, research-grade 100+).

use crate::atomic_reduce_cache;
use crate::laurent_hecke_element::LaurentHeckeElement;
use crate::reduce_laurent;
use crate::tr_m_word_lq;
use rug::ops::Pow;
use rug::Float;

/// Decimal precision (`dps`) → MPFR binary precision (bits).
///
/// `bits = ⌈dps · log₂10⌉ + 32 guard bits` — log₂(10) ≈ 3.3219.
/// Using `3.4` as the slope is conservative (an upper bound) but
/// integer-truncation (`as u32`) would still under-allocate by
/// one bit at small `dps` (e.g. `dps = 2` → `6.8` truncates to
/// `6`, but `⌈2 · log₂10⌉ = 7`).  `ceil()` enforces the
/// documented bound at every `dps`.
fn dps_to_prec(dps: u32) -> u32 {
    ((dps as f64 * 3.4).ceil() as u32) + 32
}

/// **Tier 1.A entry point — full pipeline in Rust + MPFR.**
///
/// Pipeline (all Rust, no Python crossings between stages):
///
/// 1. Reduce ([`reduce_laurent::incremental_reduce`]) — R1+R2+R3
///    fixpoint with exact BigRational coefficients.
/// 2. For each reduced σ-word:
///    a. Evaluate the BigRational coefficient at `q` via MPFR
///       string round-trip (preserves precision past f64 cap).
///    b. Compute `tr_M(word)` ZHLaurent via
///       [`tr_m_word_lq::tr_m_word_lq`] (already Rust-native).
///    c. Evaluate the ZHLaurent at `(q, z, h)` via MPFR, where
///       `z = q^3/(q^2+1)` (**trace convention D**, SU(2)/Temperley–Lieb;
///       convention C's `z = 1/(q^{1/2}+q^{-1/2})` was excised by owner
///       ruling 2026-08-09, see
///       `docs/coordination/trace-convention-registry.md`),
///       `h = q − q^{-1}`.
///    d. Accumulate into the running total.
/// 3. Return `total.to_string_radix(10, Some(dps + 5))` so the
///    Python caller can parse a single decimal string via
///    `mpmath.mpf(result_str)`.
///
/// `q_str`: substrate parameter as a decimal string (avoids f64
/// lossy conversion at the boundary; matches the existing
/// `chi_lambda_*_mpfr` API convention).
///
/// `dps`: working precision in decimal places.  Production floor
/// is 50 (AGENTS.md §Precision goals L1); use 100+ for substrate-
/// derivation cross-checks.
///
/// Returns `Err(message)` if the trace recursion hits Case C
/// (multiple top-1 in segment) on any reduced word — caller routes
/// to the sympy ocneanu fallback, same contract as
/// `tr_m_word_lq::tr_m_word_lq`.
pub fn tr_m_atomic_mpfr(
    signed_word: &[(i8, i32)],
    n_strands: usize,
    q_str: &str,
    dps: u32,
) -> Result<String, String> {
    let (val, _final) = tr_m_atomic_mpfr_with_state(
        signed_word,
        n_strands,
        q_str,
        dps,
        crate::laurent_hecke_element::LaurentHeckeElement::identity(),
    )?;
    Ok(val)
}

/// **Resume-from-state variant of [`tr_m_atomic_mpfr`].**
///
/// Takes an `initial_state` (a pre-reduced
/// [`crate::laurent_hecke_element::LaurentHeckeElement`]) and the
/// `signed_word` *suffix* to apply on top of it.  Returns
/// `(mpf_decimal_string, final_reduced_state)` so the caller can
/// persist the final state as a cache entry for future resumes.
///
/// Use case (per `markov_peel_rust_bridge` prefix-cache wiring):
/// computing `tr_M(β_{6Li})` after `β_{5Li}` is already cached.
/// Since the 5Li signed word is a strict prefix of the 6Li one,
/// the 5Li reduced state is the correct initial accumulator —
/// only the extra 12 crossings need to be applied (the part where
/// term-count growth would otherwise blow up).
///
/// Identity-state input (the `tr_m_atomic_mpfr` wrapper above)
/// reproduces the from-scratch path exactly.
pub fn tr_m_atomic_mpfr_with_state(
    signed_word_suffix: &[(i8, i32)],
    n_strands: usize,
    q_str: &str,
    dps: u32,
    initial_state: crate::laurent_hecke_element::LaurentHeckeElement,
) -> Result<(String, crate::laurent_hecke_element::LaurentHeckeElement), String> {
    let reduced = reduce_laurent::incremental_reduce_from_state(
        initial_state,
        signed_word_suffix,
        10_000,
    );
    let val = eval_reduced_to_mpfr(&reduced, n_strands, q_str, dps)?;
    Ok((val, reduced))
}

/// **Rust-side cached variant of [`tr_m_atomic_mpfr`].**
///
/// Looks up the longest cached prefix of `signed_word` in the
/// in-process [`atomic_reduce_cache`], resumes the reduce from
/// that state, applies the suffix, and caches the final state
/// under the full signed-word's hash for future calls.
///
/// **Zero FFI marshalling on cache hit.**  The cached
/// [`LaurentHeckeElement`] never crosses the Python ↔ Rust
/// boundary — Python passes only the signed word, hash + lookup
/// happen entirely in Rust.  This is the productive variant of
/// the prefix-cache infra (the disk-resident JSON path in
/// `_prefix_cache.py` is a net loss per
/// `docs/audits/2026-05-22-prefix-cache-negative-bench.md`).
pub fn tr_m_atomic_mpfr_cached(
    signed_word: &[(i8, i32)],
    n_strands: usize,
    q_str: &str,
    dps: u32,
) -> Result<String, String> {
    let (prefix_len, initial_state_opt) =
        atomic_reduce_cache::find_longest_cached_prefix(signed_word);
    let initial = initial_state_opt.unwrap_or_else(LaurentHeckeElement::identity);
    let suffix = &signed_word[prefix_len..];
    let reduced =
        reduce_laurent::incremental_reduce_from_state(initial, suffix, 10_000);
    atomic_reduce_cache::save_prefix_state(signed_word, &reduced);
    eval_reduced_to_mpfr(&reduced, n_strands, q_str, dps)
}

/// **Batched [`tr_m_atomic_mpfr`] with shared-prefix reduction.**
///
/// Returns, for every word of `signed_words` and in the same order,
/// exactly the string [`tr_m_atomic_mpfr`] returns for that word alone.
///
/// Why it is faster. [`tr_m_atomic_mpfr`] reduces each word from the
/// identity, one letter at a time. The reduced state after `k` letters
/// is a function of those `k` letters only, so two words that share a
/// prefix of length `k` share that state. A probe that expands a product
/// of linear combinations into `2^m` signed words, and then appends a
/// handful of suffixes to each, submits words that share long prefixes.
/// Here the words are sorted, walked depth-first, and the state at every
/// prefix that a later word still needs is kept and resumed from.
///
/// Why it is exact. Nothing is approximated: the same letters are applied
/// in the same order through [`reduce_laurent::incremental_reduce_from_state`],
/// with exact `LaurentRationalQ` coefficients. `LaurentHeckeElement` is a
/// `BTreeMap`, so its iteration order, and hence the MPFR summation order in
/// [`eval_reduced_to_mpfr`], does not depend on how the state was reached.
/// The output string is byte-identical to the per-word call; the tests below
/// assert that.
///
/// `parallel` splits the sorted list into contiguous chunks, one depth-first
/// walk per rayon task. A chunk boundary only costs recomputing the shared
/// prefix once more; it cannot change a value.
pub fn tr_m_atomic_mpfr_batch(
    signed_words: &[Vec<(i8, i32)>],
    n_strands: usize,
    q_str: &str,
    dps: u32,
    parallel: bool,
) -> Result<Vec<String>, String> {
    let mut order: Vec<usize> = (0..signed_words.len()).collect();
    order.sort_by(|&a, &b| signed_words[a].cmp(&signed_words[b]));
    let chunks: Vec<Vec<usize>> = if parallel && order.len() > 1 {
        // One contiguous chunk per thread. A chunk boundary forfeits the
        // prefixes shared across it, so more, smaller chunks cost more
        // reduction (measured: 16 chunks of a 256-word batch at n = 12 ran
        // at 0.49 s/word).
        let k = rayon::current_num_threads().max(1);
        let size = order.len().div_ceil(k).max(1);
        order.chunks(size).map(|c| c.to_vec()).collect()
    } else {
        vec![order]
    };
    let finish = |e: &LaurentHeckeElement| eval_reduced_to_mpfr(e, n_strands, q_str, dps);
    let run = |idx: &Vec<usize>| -> Result<Vec<(usize, String)>, String> {
        walk_sorted(signed_words, idx, &finish)
    };
    let parts: Vec<Result<Vec<(usize, String)>, String>> = if parallel {
        use rayon::prelude::*;
        chunks.par_iter().map(run).collect()
    } else {
        chunks.iter().map(run).collect()
    };
    let mut out: Vec<Option<String>> = vec![None; signed_words.len()];
    for part in parts {
        for (i, v) in part? {
            out[i] = Some(v);
        }
    }
    Ok(out.into_iter().map(|v| v.expect("every word evaluated")).collect())
}

fn common_prefix(a: &[(i8, i32)], b: &[(i8, i32)]) -> usize {
    a.iter().zip(b).take_while(|(x, y)| x == y).count()
}

/// Depth-first walk over words already sorted lexicographically.
fn walk_sorted<R>(
    words: &[Vec<(i8, i32)>],
    idx: &[usize],
    finish: &(dyn Fn(&LaurentHeckeElement) -> Result<R, String> + Sync),
) -> Result<Vec<(usize, R)>, String> {
    // stack[j] = (depth, reduced state after the first `depth` letters).
    let mut stack: Vec<(usize, LaurentHeckeElement)> =
        vec![(0, LaurentHeckeElement::identity())];
    let mut out = Vec::with_capacity(idx.len());
    for (pos, &i) in idx.iter().enumerate() {
        let w = &words[i];
        let lcp_prev = if pos == 0 { 0 } else { common_prefix(&words[idx[pos - 1]], w) };
        let lcp_next = if pos + 1 < idx.len() { common_prefix(w, &words[idx[pos + 1]]) } else { 0 };
        while stack.last().map(|(d, _)| *d > lcp_prev).unwrap_or(false) {
            stack.pop();
        }
        let (d0, base) = stack.last().expect("identity at depth 0 is never popped");
        let d0 = *d0;
        let mut elem = base.clone();
        let mut d = d0;
        if lcp_next > d0 {
            elem = reduce_laurent::incremental_reduce_from_state(elem, &w[d..lcp_next], 10_000);
            d = lcp_next;
            stack.push((d, elem.clone()));
        }
        elem = reduce_laurent::incremental_reduce_from_state(elem, &w[d..], 10_000);
        out.push((i, finish(&elem)?));
    }
    Ok(out)
}

/// **`tr_M(word_i · s_j)` for every word and every POSITIVE suffix.**
///
/// Returns `out[i][j]`. Each `word_i` is reduced once (prefixes shared as in
/// [`tr_m_atomic_mpfr_batch`]) to `X_i = Σ_u c_u·T_u`, and then
///
///     tr_M(X_i · T_s) = Σ_u c_u · tr_M(T_u · T_s),
///
/// where `T_u·T_s` is the positive word `u ++ s`, whose trace
/// [`tr_m_word_lq::tr_m_word_lq`] computes exactly from the word (it applies
/// the Hecke relation itself, so `u ++ s` need not be reduced). That is the
/// linearity of the trace and nothing else; it replaces reducing `X_i·T_s`,
/// which at n = 12 costs about 0.8 s per suffix letter.
///
/// Exactness: every `c_u` and every trace polynomial is exact; only the final
/// substitution at `q` is MPFR at `dps`. For the empty suffix the arithmetic
/// is operation-for-operation that of [`tr_m_atomic_mpfr`], so the string is
/// byte-identical. For a non-empty suffix the exact value is the same but the
/// MPFR additions are grouped differently, so the string agrees to the
/// working precision, not necessarily in its last digits (tested below to
/// `10^-dps`).
///
/// `suffixes` are generator indices (0-based, positive letters only); a
/// suffix with an inverse letter has no positive-word form and must go
/// through [`tr_m_atomic_mpfr_batch`] instead.
pub fn tr_m_atomic_mpfr_suffixes(
    signed_words: &[Vec<(i8, i32)>],
    suffixes: &[Vec<u32>],
    n_strands: usize,
    q_str: &str,
    dps: u32,
    parallel: bool,
) -> Result<Vec<Vec<String>>, String> {
    let mut order: Vec<usize> = (0..signed_words.len()).collect();
    order.sort_by(|&a, &b| signed_words[a].cmp(&signed_words[b]));
    let chunks: Vec<Vec<usize>> = if parallel && order.len() > 1 {
        let k = rayon::current_num_threads().max(1);
        let size = order.len().div_ceil(k).max(1);
        order.chunks(size).map(|c| c.to_vec()).collect()
    } else {
        vec![order]
    };
    let finish = |e: &LaurentHeckeElement| {
        eval_reduced_with_suffixes(e, suffixes, n_strands, q_str, dps)
    };
    let run = |idx: &Vec<usize>| walk_sorted(signed_words, idx, &finish);
    let parts: Vec<Result<Vec<(usize, Vec<String>)>, String>> = if parallel {
        use rayon::prelude::*;
        chunks.par_iter().map(run).collect()
    } else {
        chunks.iter().map(run).collect()
    };
    let mut out: Vec<Option<Vec<String>>> = vec![None; signed_words.len()];
    for part in parts {
        for (i, v) in part? {
            out[i] = Some(v);
        }
    }
    Ok(out.into_iter().map(|v| v.expect("every word evaluated")).collect())
}

/// MPFR evaluation of a reduced `LaurentHeckeElement` at `q₀`.
/// Shared by `tr_m_atomic_mpfr*` entry points (factored out so
/// the from-scratch / resume / cached paths reuse it bit-for-bit).
fn eval_reduced_to_mpfr(
    reduced: &LaurentHeckeElement,
    n_strands: usize,
    q_str: &str,
    dps: u32,
) -> Result<String, String> {
    let mut v = eval_reduced_with_suffixes(reduced, &[Vec::new()], n_strands, q_str, dps)?;
    Ok(v.pop().expect("one suffix in, one value out"))
}

/// `tr_M(reduced · T_s)` at `q₀` for each positive suffix `s` (see
/// [`tr_m_atomic_mpfr_suffixes`]). With the single suffix `[]` this is the
/// historical `eval_reduced_to_mpfr`, operation for operation.
fn eval_reduced_with_suffixes(
    reduced: &LaurentHeckeElement,
    suffixes: &[Vec<u32>],
    n_strands: usize,
    q_str: &str,
    dps: u32,
) -> Result<Vec<String>, String> {
    let prec = dps_to_prec(dps);
    let q = Float::with_val(
        prec,
        Float::parse(q_str)
            .map_err(|e| format!("tr_m_atomic_mpfr: q_str parse error: {}", e))?,
    );
    let q_inv = Float::with_val(prec, q.clone().recip());
    // z = q³/(q² + 1) — trace convention D (SU(2)/Temperley–Lieb).
    // Convention C (z = 1/(q^{1/2} + q^{-1/2})) was excised by owner ruling
    // 2026-08-09; see docs/coordination/trace-convention-registry.md.
    // D is rational in q, so the q^{1/2} round trip is gone: this is now
    // exact-to-`prec` from three MPFR ops instead of a sqrt plus two recips.
    let q_sq_z = Float::with_val(prec, &q * &q);
    let z = Float::with_val(
        prec,
        Float::with_val(prec, &q_sq_z * &q)
            / Float::with_val(prec, &q_sq_z + 1u32),
    );
    // h = q − q^{-1}
    let h = Float::with_val(prec, &q - &q_inv);

    let mut totals: Vec<Float> = suffixes.iter().map(|_| Float::with_val(prec, 0)).collect();
    for (word, coef) in &reduced.terms {
        // Skip formal-variable (negative gen) entries — they make
        // no contribution to the Markov trace (matches the Python
        // convention in `tr_M_element`).
        if word.iter().any(|&g| g < 0) {
            continue;
        }
        let coef_mpfr = coef.evaluate_mpfr(&q);
        if coef_mpfr.is_zero() {
            continue;
        }
        // Re-cast non-negative i32 → u32 for the trace API.  Bit-
        // identical for non-negative values; the filter above
        // guarantees safety.
        let word_u32: Vec<u32> = word.iter().map(|&g| g as u32).collect();
        for (j, suf) in suffixes.iter().enumerate() {
            let mut w = word_u32.clone();
            w.extend_from_slice(suf);
            let zh = tr_m_word_lq::tr_m_word_lq(&w, n_strands, 200)?;
            let mut zh_val = Float::with_val(prec, 0);
            for (&(z_exp, h_exp), poly) in &zh.terms {
                let c_zh = poly.evaluate_mpfr(&q);
                let z_pow: Float = Float::with_val(prec, z.clone().pow(z_exp));
                let h_pow: Float = Float::with_val(prec, h.clone().pow(h_exp));
                let mut term = Float::with_val(prec, &c_zh * &z_pow);
                term *= &h_pow;
                zh_val += term;
            }
            totals[j] += Float::with_val(prec, &coef_mpfr * &zh_val);
        }
    }

    // Emit at full precision so mpmath.mpf can reconstruct without
    // loss.  `Some(dps + 5)` gives a small over-precision buffer
    // so the decimal representation is unambiguous to `dps` places.
    Ok(totals
        .into_iter()
        .map(|t| t.to_string_radix(10, Some((dps + 5) as usize)))
        .collect())
}

// ── Tests ─────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    /// `q₀` — the canonical substrate value.
    const Q0_STR: &str = "1.10997859555418057528159407960950937799328227995870";

    #[test]
    fn proton_word_smoke() {
        // The smallest non-empty signed word — a single Sigma+ crossing at
        // gen 0 — so tr_M(sigma_0) = z exactly. This USED to assert only
        // that the result parsed as a Float, which meant the MPFR path's
        // trace convention had no numeric guard at all: the C -> D switch
        // of 2026-08-09 (bean qou-wgta item 10) passed it untouched.
        //
        // Now it pins the value. At Q0_STR:
        //   convention D (production)  z = 0.61268805054558909983576288738850
        //   convention C (excised)     z = 0.49932033403359825002066908467672
        // 1e-40 tolerance, so a convention flip cannot slip through and a
        // stale docstring cannot cover for one.
        let signed_word = vec![(1i8, 0i32)];
        let result_str = tr_m_atomic_mpfr(&signed_word, 3, Q0_STR, 50).unwrap();
        let parsed = Float::parse(&result_str)
            .expect("result string must parse as Float");
        let v = Float::with_val(180, parsed);
        let expected = Float::with_val(
            180,
            Float::parse("0.61268805054558909983576288738850176397091162650391")
                .unwrap(),
        );
        let diff = Float::with_val(180, &v - &expected);
        assert!(
            diff.abs().to_f64() < 1e-40,
            "tr_M(sigma_0) = {} (convention D expects z = {})",
            v,
            expected
        );
    }

    /// The batch path must return byte-identical strings to the per-word
    /// path, including on words that share prefixes, on duplicates, on the
    /// empty word and in parallel mode.
    #[test]
    fn batch_matches_per_word_byte_for_byte() {
        let base: Vec<(i8, i32)> = vec![(1, 0), (-1, 1), (1, 0), (1, 2), (-1, 1), (1, 3)];
        let mut words: Vec<Vec<(i8, i32)>> = Vec::new();
        for m in 0u32..16 {
            let mut w = base.clone();
            for b in 0..4 {
                if (m >> b) & 1 == 1 {
                    w[b + 1].0 = -w[b + 1].0;
                }
            }
            words.push(w.clone());
            let mut s = w.clone();
            s.push((1, 0));
            words.push(s);
        }
        words.push(vec![]);
        words.push(words[3].clone());
        let expect: Vec<String> = words
            .iter()
            .map(|w| tr_m_atomic_mpfr(w, 5, Q0_STR, 40).unwrap())
            .collect();
        for par in [false, true] {
            let got = tr_m_atomic_mpfr_batch(&words, 5, Q0_STR, 40, par).unwrap();
            assert_eq!(got, expect, "parallel = {par}");
        }
    }

    /// The suffix path: byte-identical for the empty suffix, and within
    /// 10^-dps of the per-word path for positive suffixes, on words with
    /// inverse letters and shared prefixes.
    #[test]
    fn suffixes_match_per_word() {
        let base: Vec<(i8, i32)> = vec![(1, 0), (-1, 1), (1, 0), (1, 2), (-1, 1), (1, 3), (-1, 2)];
        let mut words: Vec<Vec<(i8, i32)>> = Vec::new();
        for m in 0u32..8 {
            let mut w = base.clone();
            for b in 0..3 {
                if (m >> b) & 1 == 1 {
                    w[b + 4].0 = -w[b + 4].0;
                }
            }
            words.push(w);
        }
        let sufs: Vec<Vec<u32>> = vec![vec![], vec![0], vec![0, 0], vec![2, 3], vec![3, 2, 1, 3]];
        for par in [false, true] {
            let got = tr_m_atomic_mpfr_suffixes(&words, &sufs, 5, Q0_STR, 40, par).unwrap();
            for (i, w) in words.iter().enumerate() {
                for (j, s) in sufs.iter().enumerate() {
                    let mut full = w.clone();
                    full.extend(s.iter().map(|&g| (1i8, g as i32)));
                    let want = tr_m_atomic_mpfr(&full, 5, Q0_STR, 40).unwrap();
                    if s.is_empty() {
                        assert_eq!(got[i][j], want, "empty suffix must be byte-identical");
                    }
                    let a = Float::with_val(200, Float::parse(&got[i][j]).unwrap());
                    let b = Float::with_val(200, Float::parse(&want).unwrap());
                    let d = Float::with_val(200, &a - &b).abs();
                    let tol = Float::with_val(200, Float::parse("1e-40").unwrap());
                    assert!(d < tol, "word {i} suffix {j}: {} vs {}", got[i][j], want);
                }
            }
        }
    }

    #[test]
    fn empty_word_is_one() {
        // tr_M(identity) = 1 at any q.
        let signed_word: Vec<(i8, i32)> = vec![];
        let result_str = tr_m_atomic_mpfr(&signed_word, 3, Q0_STR, 50).unwrap();
        let parsed = Float::parse(&result_str).unwrap();
        let v = Float::with_val(180, parsed);
        let one = Float::with_val(180, 1);
        let diff = Float::with_val(180, &v - &one);
        let diff_f64: f64 = diff.to_f64().abs();
        assert!(diff_f64 < 1e-40, "tr_M(identity) should be 1, got {}", result_str);
    }

    #[test]
    fn averaged_squared_at_q0() {
        // (σ_0 − h/2)² as derived in reduce_laurent::tests::
        //     incremental_reduce_averaged_squared:
        // reduces to q²/4 + 1/2 + q⁻²/4  on the empty word.
        // Markov trace of empty word is 1, so the contribution is
        // 1·(q²/4 + 1/2 + q⁻²/4).
        let signed_word = vec![(0i8, 0i32), (0i8, 0i32)];
        let result_str = tr_m_atomic_mpfr(&signed_word, 3, Q0_STR, 50).unwrap();
        let parsed = Float::parse(&result_str).unwrap();
        let v = Float::with_val(180, parsed);
        // Expected: q²/4 + 1/2 + q⁻²/4 at q₀.
        let q = Float::with_val(180, Float::parse(Q0_STR).unwrap());
        let q_sq = Float::with_val(180, q.clone() * &q);
        let q_inv_sq = Float::with_val(180, q_sq.clone().recip());
        let expected = Float::with_val(
            180,
            Float::with_val(180, &q_sq / 4)
                + Float::with_val(180, 1) / 2
                + Float::with_val(180, &q_inv_sq / 4),
        );
        let diff = Float::with_val(180, &v - &expected);
        let diff_f64: f64 = diff.to_f64().abs();
        assert!(
            diff_f64 < 1e-40,
            "averaged-squared mismatch at q₀: got {}, expected {}",
            result_str,
            expected.to_string_radix(10, Some(55))
        );
    }
}
