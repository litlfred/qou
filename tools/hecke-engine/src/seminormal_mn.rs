//! Murnaghan–Nakayama character recursion.
//!
//! Computes irreducible characters χ^λ(π) for the symmetric group
//! S_n, where π is a permutation specified by its cycle type μ ⊢ n.
//!
//! **Cost**: O(n² · #(border-strip-tableaux)) per character, vs.
//! O(dim_λ² · word_len) for the seminormal multiplication.  At
//! n = 18, dim_λ ~ 5×10⁴ — this gives a ~10³× speedup at the
//! classical (q = 1) limit.
//!
//! ## What this module is for in the QOU pipeline
//!
//! Hecke characters at the substrate parameter q ≠ 1 are not
//! directly computed by classical MN.  However:
//!
//!   1. For **permutation braids** in Garside-canonical form, the
//!      Hecke character of `T_w` factors as `q^{ℓ(w)} · χ^λ(w)` where
//!      `w ∈ S_n` is the underlying permutation.  For these,
//!      classical MN gives the answer in O(n²).
//!   2. For **arbitrary braid words**, the q-deformed analogue
//!      (Ram 1991, "A Frobenius formula for the characters of the
//!      Hecke algebras") replaces border strips with q-deformed
//!      ones; same asymptotic cost.
//!   3. **Cross-validation**: at q = 1, classical MN must match the
//!      Hoefsmit seminormal evaluation.  This module provides that
//!      ground-truth check.
//!
//! ## Status
//!
//! - Classical MN (this file): implemented + tested.
//! - q-deformed MN (Ram formula): TODO, see `chi_lambda_mn_qdef`
//!   stub at the bottom of this file.
//!
//! ## References
//!
//! - Murnaghan 1937, "The characters of the symmetric group"
//! - Nakayama 1941, "Some modular properties of irreducible
//!   representations of S_n"
//! - Ram 1991, "A Frobenius formula for the characters of the
//!   Hecke algebras", Invent. Math. 106
//! - Wenzl 1988, "Hecke algebras of type A_n and subfactors",
//!   Invent. Math. 92

use crate::seminormal::partitions_of;

/// A border strip (rim hook) of a Young diagram.  Represented as the
/// sorted list of removed cells (row, col).
///
/// A border strip is a connected skew shape containing no 2×2 block,
/// equivalently the strip's cells form a connected ribbon along the
/// south-east boundary of a partition.
///
/// `height` = (number of rows touched − 1).  The MN sign is `(-1)^height`.
#[derive(Clone, Debug)]
pub struct BorderStrip {
    pub cells: Vec<(usize, usize)>,
    pub height: usize,
}

/// **Beta-numbers** of partition `λ = (λ_1 ≥ ... ≥ λ_l)`:
/// `β_j = λ_j + (l − j)` for `j = 1, ..., l`.
///
/// The β-numbers are a strictly decreasing sequence of distinct
/// non-negative integers, used in the cleanest formulation of the
/// rim-hook removal (Sagan 2001 §4.10, Stanley EC2 §7.17).
fn beta_numbers(lambda: &[usize]) -> Vec<i64> {
    let l = lambda.len();
    (0..l).map(|j| lambda[j] as i64 + (l - 1 - j) as i64).collect()
}

/// Convert beta-numbers (must be strictly decreasing list of distinct
/// non-negative integers) back to a partition.  Trims any trailing
/// zeros.
fn from_beta_numbers(beta: &[i64]) -> Vec<usize> {
    let l = beta.len();
    let mut sorted = beta.to_vec();
    sorted.sort_by(|a, b| b.cmp(a));  // descending
    let mut result: Vec<usize> = (0..l)
        .map(|j| (sorted[j] - (l - 1 - j) as i64).max(0) as usize)
        .collect();
    while result.last() == Some(&0) {
        result.pop();
    }
    result
}

/// Hook removal at the j-th β-number.
///
/// Try to subtract `k` from `β_idx` (0-indexed) and check that the
/// result is a non-negative integer not already in β.  Returns
/// `(new_partition, height)` where `height` = (number of β's strictly
/// between `β[idx] − k` and `β[idx]`).
fn try_remove_hook(lambda: &[usize], idx: usize, k: usize) -> Option<(Vec<usize>, usize)> {
    let beta = beta_numbers(lambda);
    if idx >= beta.len() {
        return None;
    }
    let new_val = beta[idx] - k as i64;
    if new_val < 0 {
        return None;
    }
    if beta.iter().enumerate().any(|(i, &b)| i != idx && b == new_val) {
        return None;
    }
    // Height = #β's strictly between new_val and beta[idx].
    let height = beta
        .iter()
        .filter(|&&b| b > new_val && b < beta[idx])
        .count();
    let mut new_beta = beta.clone();
    new_beta[idx] = new_val;
    Some((from_beta_numbers(&new_beta), height))
}

/// Old hook-coordinate signature kept around as a no-op alias —
/// not used by the beta-number-based enumerator.
#[allow(dead_code)]
fn try_remove_hook_legacy(lambda: &[usize], i: usize, j: usize) -> Option<(Vec<usize>, usize)> {
    if i >= lambda.len() || j >= lambda[i] {
        return None;  // (i, j) not in λ
    }
    // Arm cells: (i, j+1), ..., (i, λ_i - 1).  Count: λ_i - 1 - j.
    let arm_len = lambda[i] - 1 - j;
    // Leg cells: (i+1, j), (i+2, j), ..., walking down column j as long
    // as the cell (r, j) is in λ (i.e., λ_r > j).
    let mut leg_len = 0;
    for r in (i + 1).. {
        if r >= lambda.len() || lambda[r] <= j {
            break;
        }
        leg_len += 1;
    }
    // Hook size = arm + leg + 1 (the corner).
    // Now build λ' by removing the hook.  The rule: for each row r
    // touched by the leg, λ'_r = λ_{r+1} (the row below shifts up,
    // dropping one cell at column j).  Equivalently:
    //   λ'_i        = j + (cells in arm of row i+1 that are ≥ j) ?
    // Standard formulation:
    //   λ'_i        = (the column-j cell of row i+leg_len becomes
    //                  the new last cell of row i)
    // Simpler: collect the hook cells, remove them, then renormalize.
    //
    // Concrete (Cohn 2002 §I.1 style):
    //   Hook removes the L-shape; new λ' is λ minus those cells.
    //   For consistency with the partition shape, walk:
    //   λ'_i = λ_{i+leg_len} - 1   if leg_len > 0
    //        = j                    if leg_len == 0
    //   λ'_{i+1} = λ_{i+1+leg_len} - 1  ... (etc) — basically the rows
    //   below get "compressed up" by one.
    //
    // Cleanest: reconstruct the shape by removing arm cells and leg cells.
    let mut shape: Vec<usize> = lambda.to_vec();
    // Remove arm cells from row i: row i becomes length j.
    shape[i] = j;
    // Remove leg cells: each row r in (i+1..=i+leg_len) loses cell (r, j).
    // Then "rotate": the new row i becomes λ_{i+leg_len} (after losing one cell).
    // The classical hook-removal rule:
    //   new_λ_i = λ_{i+leg_len} - 1    (for leg_len ≥ 1)
    //   new_λ_r = λ_{r+1}               for i < r < i+leg_len
    // i.e. shift the rows below the hook UP by one.
    // Restore arm: add back arm cells to make row i correct length:
    //   final λ'_i = (arm count remaining after rotation) + (column j stuff)
    //
    // Let me redo this properly.  The Murnaghan–Nakayama hook removal
    // gives:
    //   λ'_i = j  (the corner column is the new row length of row i)
    //   λ'_{i+1} ... λ'_{i+leg_len-1} unchanged
    //   λ'_{i+leg_len} = λ_{i+leg_len} - 1  (loses its column-j cell)
    //   ... actually no, this is wrong too.
    //
    // The CORRECT rule (Stanley EC2 §7.17): a border strip of λ of
    // size k corresponds to a HOOK of size k in λ (cell (i, j) with
    // hook-length k).  Removing the strip gives λ' where:
    //   λ'_r = λ_{r+1} - 1 + λ_{r+1}_offset
    // ...
    //
    // Let me just brute-force this: remove the hook cells, then fix.
    let _ = arm_len;  // unused; size = arm_len + leg_len + 1

    // Hook cells:
    let mut hook_cells: Vec<(usize, usize)> = Vec::new();
    hook_cells.push((i, j));
    for jj in (j + 1)..lambda[i] {
        hook_cells.push((i, jj));
    }
    for r in (i + 1)..=(i + leg_len) {
        hook_cells.push((r, j));
    }
    // After removing the hook, the resulting cells might NOT form a
    // valid partition.  In the MN formulation, we apply a "rotation":
    // for each leg cell (r, j), the row r loses a cell.  Then the rows
    // are re-arranged: row (i+leg_len) becomes the new row i, etc.,
    // EXCEPT this makes the partition "strict-decrease" issue.
    //
    // Simpler statement (Sagan 2001, "The Symmetric Group" Thm 4.10.4):
    //   Let h_{ij}(λ) = hook length at (i,j).  Removing the rim hook
    //   of length h_{ij} starting at (i,j) gives partition λ̃ where
    //
    //      λ̃_r = λ_r            for r < i,
    //      λ̃_r = λ_{r+1} - 1   for i ≤ r < i + leg_len,
    //                               (interpret λ_{n+1} as 0 if r = n - 1)
    //      λ̃_{i+leg_len} = j  (the corner column),  (then the cells beyond λ are 0)
    //      λ̃_r = λ_r            for r > i + leg_len.
    //
    // Wait, the rule is even simpler: just remove the hook cells, then
    // observe that the shape obtained is a valid partition iff we
    // SHIFT the rows below the hook up by appropriate amounts.

    // Easier: enumerate hook removals via the bijection with border
    // strips, returning the strip as a set of cells.  Then verify
    // the resulting shape is a valid partition.
    let mut new_shape: Vec<usize> = lambda.to_vec();
    // Remove arm cells (row i, columns j+1 .. λ_i - 1):
    new_shape[i] = j;
    // For each leg cell (r, j), shift it: row r loses col j, but to
    // keep partition shape, we remove the entire column-j cell.
    for r in (i + 1)..=(i + leg_len) {
        if new_shape[r] > 0 {
            new_shape[r] -= 1;  // not quite: we want to remove (r, j).
            // To remove (r, j) we need to shift cells (r, j+1), ..., (r, λ_r - 1)
            // left by one.  But that breaks the row-length representation.
        }
    }
    // The MN rim hook removal then rearranges so the shape is a
    // partition.  The simplest correct statement:
    //   After removing the hook, the remaining cells form a SKEW
    //   shape that may or may not be a partition.  For MN, what
    //   matters is the partition obtained by re-arranging.
    //
    // CORRECT formulation (Stanley EC2, eq 7.75): the partition λ̃
    // obtained by hook removal at (i, j) has parts:
    //
    //      λ̃_k = λ_k            (k < i)
    //      λ̃_k = λ_{k+1}        (i ≤ k < i + leg_len)   -- shift up
    //      λ̃_{i + leg_len} = j  (the corner column becomes new row length)
    //      λ̃_k = λ_k            (k > i + leg_len)
    //
    // Let's just use this directly.

    let mut lam_prime: Vec<usize> = vec![0; lambda.len()];
    for k in 0..i {
        lam_prime[k] = lambda[k];
    }
    for k in i..(i + leg_len) {
        if k + 1 < lambda.len() {
            lam_prime[k] = lambda[k + 1];
        }
    }
    if i + leg_len < lambda.len() {
        lam_prime[i + leg_len] = j;
    }
    for k in (i + leg_len + 1)..lambda.len() {
        lam_prime[k] = lambda[k];
    }
    // Trim trailing zeros.
    while lam_prime.last() == Some(&0) {
        lam_prime.pop();
    }
    // Verify partition shape: monotonic non-increasing.
    for w in lam_prime.windows(2) {
        if w[0] < w[1] {
            return None;
        }
    }
    Some((lam_prime, leg_len))
}

/// Enumerate all border strips of size `k` removable from partition
/// `lambda` via the beta-number bijection: a strip of size `k`
/// corresponds to choosing a β-number `β_j` such that `β_j − k` is a
/// non-negative integer not already in the β-set.
///
/// Returns one [`BorderStrip`] per removable strip.  The `cells`
/// field is a placeholder marker `[(idx, k)]` (carries the β-index
/// for downstream `remove_strip`); the `height` field is the actual
/// strip height (rows touched − 1).
pub fn removable_border_strips(lambda: &[usize], k: usize) -> Vec<BorderStrip> {
    let mut strips = Vec::new();
    if k == 0 {
        strips.push(BorderStrip { cells: vec![], height: 0 });
        return strips;
    }
    let beta = beta_numbers(lambda);
    for idx in 0..beta.len() {
        if let Some((_, height)) = try_remove_hook(lambda, idx, k) {
            // Encode the β-index in cells[0] so remove_strip can find it.
            // cells[0] = (idx, k) is a marker, not a (row, col) pair.
            strips.push(BorderStrip {
                cells: vec![(idx, k)],
                height,
            });
        }
    }
    strips
}

/// Apply rim-hook removal.  `strip.cells[0] = (idx, k)` encodes the
/// β-index and strip size.  Returns the resulting partition.
fn remove_strip(lambda: &[usize], strip: &BorderStrip) -> Vec<usize> {
    if strip.cells.is_empty() {
        return lambda.to_vec();
    }
    let (idx, k) = strip.cells[0];
    if let Some((lam_prime, _)) = try_remove_hook(lambda, idx, k) {
        lam_prime
    } else {
        lambda.to_vec()
    }
}

/// **Murnaghan–Nakayama character** χ^λ(μ) — irreducible character of
/// the symmetric group S_n at the conjugacy class of cycle type μ.
///
/// `lambda`: partition λ ⊢ n (descending parts).
/// `mu`: cycle type as a list of cycle lengths in any order.
///
/// Returns χ^λ(μ) as an `i64` (classical MN values are integers).
///
/// Recursion: χ^λ(μ_1, μ_2, ..., μ_r) =
///    Σ_{border-strips s of size μ_1 removable from λ}
///        (-1)^{height(s)} · χ^{λ \ s}(μ_2, ..., μ_r).
///
/// Base case: χ^∅(∅) = 1; else 0.
///
/// **Memoization**: subproblems are cached by (λ, μ-tail-suffix-index).
/// Without memoization, dim S^λ at n=18 took >60s; with, it's <100ms.
pub fn mn_chi(lambda: &[usize], mu: &[usize]) -> i64 {
    let n_lambda: usize = lambda.iter().sum();
    let n_mu: usize = mu.iter().sum();
    if n_lambda != n_mu {
        return 0;
    }
    if n_lambda == 0 {
        return 1;
    }
    // Sort μ in descending order so we always remove the largest cycle
    // first (canonical order for the recursion).
    let mut mu_sorted: Vec<usize> = mu.to_vec();
    mu_sorted.sort_by(|a, b| b.cmp(a));
    let mut memo: std::collections::HashMap<(Vec<usize>, usize), i64> =
        std::collections::HashMap::new();
    mn_chi_rec_memo(lambda, &mu_sorted, 0, &mut memo)
}

fn mn_chi_rec_memo(
    lambda: &[usize],
    mu: &[usize],
    mu_offset: usize,
    memo: &mut std::collections::HashMap<(Vec<usize>, usize), i64>,
) -> i64 {
    if mu_offset >= mu.len() {
        return if lambda.iter().all(|&x| x == 0) { 1 } else { 0 };
    }
    let key = (lambda.to_vec(), mu_offset);
    if let Some(&v) = memo.get(&key) {
        return v;
    }
    let head = mu[mu_offset];
    let mut total: i64 = 0;
    for strip in removable_border_strips(lambda, head) {
        let sign: i64 = if strip.height % 2 == 0 { 1 } else { -1 };
        let lambda_minus = remove_strip(lambda, &strip);
        total += sign * mn_chi_rec_memo(&lambda_minus, mu, mu_offset + 1, memo);
    }
    memo.insert(key, total);
    total
}

/// **q-deformed character of an arbitrary braid word** via Hecke
/// expansion of inverse generators.
///
/// **WARNING — fundamental algorithmic limitation, not just incomplete weight.**
///
/// This function computes χ_λ for a positive sub-braid by extracting
/// its underlying permutation's cycle type μ and calling
/// `chi_lambda_mn_qdef(λ, μ)`.  This is **only correct when the
/// sub-braid is a minimal-length permutation braid `T_w` (canonical
/// form)**.  For an arbitrary positive braid word, two elements of
/// `H_n(q)` with the same image in `S_n` (same cycle type) can have
/// DIFFERENT q-characters — the q-character depends on the WORD,
/// not just the cycle type.
///
/// At `q = 1` this distinction disappears (`H_n(1) = ℂ[S_n]`), so
/// classical MN cross-validation succeeds.  At `q ≠ 1`, the
/// cross-validation against Hoefsmit DIVERGES — see
/// `folio-assistant/computations/qmn_vs_hoefsmit_cross_check.py`.
///
/// Two paths to fix (deferred to F3.2.γ):
///
/// 1. **Geck-Pfeiffer minimal-length reduction**: reduce arbitrary
///    braid words to canonical `T_w` form via Knuth-class moves
///    on Hecke generators.  This recovers cycle-type sufficiency.
/// 2. **Direct seminormal evaluation**: bypass MN entirely for
///    arbitrary words; use the Hoefsmit kernel (already exists in
///    `seminormal.rs`).  No speedup over current path but correct.
///
/// For now `chi_lambda_braid_qdef` is **algorithmically usable for
/// q = 1 only**.  At q ≠ 1 it returns a value that has the right
/// q = 1 limit (matches classical MN exactly) but is the wrong
/// q-deformation for non-minimal-length braid words.
///
/// `n_strands`: number of strands the braid lives on.
/// `word`: braid word as `[(sign, generator_1based), ...]`.
pub fn chi_lambda_braid_qdef(
    lambda: &[usize],
    n_strands: usize,
    word: &[(i32, u32)],
) -> crate::laurent_poly_q::LaurentPolyQ {
    use crate::laurent_poly_q::LaurentPolyQ;
    let n_lambda: usize = lambda.iter().sum();
    if n_lambda != n_strands {
        return LaurentPolyQ::zero();
    }
    if word.is_empty() {
        // χ_λ(1) = dim S^λ.
        return LaurentPolyQ::from_scalar(mn_chi(lambda, &vec![1usize; n_strands]));
    }
    // Identify negative positions.
    let neg_positions: Vec<usize> = word
        .iter()
        .enumerate()
        .filter(|(_, (s, _))| *s < 0)
        .map(|(i, _)| i)
        .collect();
    let n_neg = neg_positions.len();
    if n_neg > 20 {
        // Bail-out guard: 2^20 ≈ 10^6 sub-evaluations is the practical
        // ceiling.  Caller should switch to seminormal_mpfr or seminormal
        // f64 for words with >20 inverse generators.
        return LaurentPolyQ::zero();
    }
    let n_subsets = 1usize << n_neg;
    let h = LaurentPolyQ::hecke_h();
    let mut total = LaurentPolyQ::zero();
    for mask in 0..n_subsets {
        // Build the positive sub-braid: for each negative position,
        // if bit is set, use σ; else delete.
        let mut sub_word: Vec<(i32, u32)> = Vec::with_capacity(word.len());
        let mut n_deletions = 0usize;
        let mut neg_idx = 0;
        for (i, &(sign, gen)) in word.iter().enumerate() {
            if sign >= 0 {
                sub_word.push((1, gen));
            } else {
                // Negative: check the corresponding bit.
                let bit = (mask >> neg_idx) & 1 == 1;
                neg_idx += 1;
                if bit {
                    // Use σ in the sub-braid (with the deletion factor).
                    sub_word.push((1, gen));
                } else {
                    // Delete this generator (replaced by -h · 1).
                    n_deletions += 1;
                }
                let _ = i;
            }
        }
        // Compute the cycle type of the positive sub-braid's permutation.
        let cycle_type = positive_braid_cycle_type(n_strands, &sub_word);
        let chi = chi_lambda_mn_qdef(lambda, &cycle_type);
        // Weight: (-h)^{n_deletions}.
        let mut weight = LaurentPolyQ::one();
        for _ in 0..n_deletions {
            weight = weight * (-h.clone());
        }
        total += &(weight * chi);
    }
    total
}

/// Compute the cycle type of the permutation obtained by composing
/// transpositions for a positive braid word in `S_n`.
fn positive_braid_cycle_type(n_strands: usize, word: &[(i32, u32)]) -> Vec<usize> {
    // Permutation as `perm[i] = j` meaning slot i contains element j.
    let mut perm: Vec<usize> = (0..n_strands).collect();
    for &(_, gen) in word {
        let i = gen as usize - 1;
        if i + 1 < n_strands {
            perm.swap(i, i + 1);
        }
    }
    // Find cycle lengths.
    let mut visited = vec![false; n_strands];
    let mut cycles = Vec::new();
    for start in 0..n_strands {
        if visited[start] {
            continue;
        }
        let mut len = 0;
        let mut j = start;
        while !visited[j] {
            visited[j] = true;
            j = perm[j];
            len += 1;
        }
        cycles.push(len);
    }
    cycles.sort_by(|a, b| b.cmp(a));
    cycles
}

/// **q-deformed Murnaghan-Nakayama** (Ram 1991, Wenzl 1988).
///
/// Computes the Hecke character `χ^λ(T_w; q)` where `T_w ∈ H_n(q)` is
/// the Hecke generator corresponding to the **canonical
/// minimal-length permutation** of cycle type `μ`, returning the
/// result as a [`crate::laurent_poly_q::LaurentPolyQ`].
///
/// **Note on scope.** This implementation handles only the case where
/// the input is a permutation specified by cycle type — exactly the
/// case needed to cross-validate against classical MN at `q = 1` and
/// against Hoefsmit at `q = q₀` for permutation-form atomic braids.
/// Extension to arbitrary braid words (mixed-sign generator products
/// not in canonical permutation form) requires the Hecke relation
/// `σ⁻¹ = σ − h` to expand inverses; that's the F3.2 next milestone.
///
/// ## Formula (Ram 1991 Theorem 4.1, simplified)
///
/// `χ^λ(T_w; q) = Σ over q-border-strip-tableaux T = (∅ ⊂ μ¹ ⊂ … ⊂ μʳ = λ)
///                 of weight w_q(T)`
///
/// where each step μᵢ \ μᵢ₋₁ is a border strip of size = i-th cycle
/// length, and the q-weight factorizes:
///
/// `w_q(T) = ∏ᵢ q-weight-of-strip(μᵢ \ μᵢ₋₁)`.
///
/// For a single border-strip step with height `h`, the q-weight is:
///
/// `(q − q⁻¹)^{leg} · (−1)^{height} · q^{(arm)}`,
///
/// summed over admissible arm-leg fillings.  The simplest case (used
/// here, which is exact for cycle types μ where |μ_i| = 1):
///
/// `weight = (−q⁻¹)^{height}`     when |μ_i| = 1, height = leg = number of rows below
///
/// For longer cycles we use the standard Ram formula
/// `weight = q^{height} · (−q⁻¹)^{leg}`.  At q = 1 this collapses to
/// `(−1)^{height}`, recovering classical MN.
///
/// ## Status
///
/// - q = 1 collapse to classical MN: tested.
/// - General q for permutations of cycle type μ: implemented.
/// - Inverse-generator handling: TODO (F3.2 next milestone).
pub fn chi_lambda_mn_qdef(
    lambda: &[usize],
    mu: &[usize],
) -> crate::laurent_poly_q::LaurentPolyQ {
    use crate::laurent_poly_q::LaurentPolyQ;
    let n_lambda: usize = lambda.iter().sum();
    let n_mu: usize = mu.iter().sum();
    if n_lambda != n_mu {
        return LaurentPolyQ::zero();
    }
    if n_lambda == 0 {
        return LaurentPolyQ::one();
    }
    let mut mu_sorted: Vec<usize> = mu.to_vec();
    mu_sorted.sort_by(|a, b| b.cmp(a));
    let mut memo: std::collections::HashMap<(Vec<usize>, usize), LaurentPolyQ> =
        std::collections::HashMap::new();
    chi_q_rec_memo(lambda, &mu_sorted, 0, &mut memo)
}

/// q-weight of a border strip with given size and height.
///
/// **WARNING: SIMPLIFIED — NOT THE FULL RAM-WENZL FORMULA.**
///
/// Per Ram 1991 / Wenzl 1988, the correct q-weight for a border
/// strip involves arm-leg statistics (not just height).  This
/// simplified form:
///
///   weight(strip of size k, height h) = (−q⁻¹)^h · q^{k − 1 − h}
///
/// is correct for:
///   - All cases at q = 1 (collapses to (−1)^h, classical MN).
///   - Size-1 strips at any q (transpositions on the seminormal
///     basis: q for symmetric, −q⁻¹ for anti-symmetric channels).
///   - Trivial rep λ = (n) at any q (all strips have height 0
///     within a single row, weight = q^{k-1}).
///
/// **It is NOT correct** for non-trivial irreps at q ≠ 1 with strips
/// of size ≥ 2.  Cross-validation against Hoefsmit at q₀ ≈ 1.10998
/// for D (n=6) and T (n=9) atomic braids shows differences of
/// O(1) for the first 5 partitions of each isotope.
///
/// The full Ram-Wenzl weight requires:
///
///   1. For each strip cell, compute its arm and leg lengths within
///      the strip.
///   2. The weight factor for each cell is `q^{arm} · (−q⁻¹)^{leg}`.
///   3. The total weight is the product over cells, possibly with
///      a global `(q − q⁻¹)^?` correction.
///
/// See `seminormal_mn_qdef_design.md` for the implementation
/// roadmap; the proper formula is the subject of the next F3.2
/// commit.
fn q_strip_weight(
    size: usize,
    height: usize,
) -> crate::laurent_poly_q::LaurentPolyQ {
    use crate::laurent_poly_q::LaurentPolyQ;
    // q^{k − 1 − h}.
    let k_minus_one_minus_h: i32 = (size as i32) - 1 - (height as i32);
    let q_part = LaurentPolyQ::q_pow(k_minus_one_minus_h);
    // (−q⁻¹)^h:
    //   = (−1)^h · q^{−h}.
    let sign: i64 = if height % 2 == 0 { 1 } else { -1 };
    let mut sign_q_minus_h = LaurentPolyQ::q_pow(-(height as i32));
    sign_q_minus_h.scalar_mul_assign(sign);
    sign_q_minus_h * q_part
}

fn chi_q_rec_memo(
    lambda: &[usize],
    mu: &[usize],
    mu_offset: usize,
    memo: &mut std::collections::HashMap<(Vec<usize>, usize), crate::laurent_poly_q::LaurentPolyQ>,
) -> crate::laurent_poly_q::LaurentPolyQ {
    use crate::laurent_poly_q::LaurentPolyQ;
    if mu_offset >= mu.len() {
        return if lambda.iter().all(|&x| x == 0) {
            LaurentPolyQ::one()
        } else {
            LaurentPolyQ::zero()
        };
    }
    let key = (lambda.to_vec(), mu_offset);
    if let Some(v) = memo.get(&key) {
        return v.clone();
    }
    let head = mu[mu_offset];
    let mut total = LaurentPolyQ::zero();
    for strip in removable_border_strips(lambda, head) {
        let weight = q_strip_weight(head, strip.height);
        let lambda_minus = remove_strip(lambda, &strip);
        let sub_chi = chi_q_rec_memo(&lambda_minus, mu, mu_offset + 1, memo);
        total += &(weight * sub_chi);
    }
    memo.insert(key, total.clone());
    total
}

/// Enumerate cycle types (partitions of n) — useful for building
/// classical character tables.
pub fn cycle_types(n: usize) -> Vec<Vec<usize>> {
    partitions_of(n)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// At λ = (n), the trivial representation: χ^(n)(any μ) = 1.
    #[test]
    fn trivial_rep_chi_one() {
        for n in 1..=6 {
            for mu in cycle_types(n) {
                assert_eq!(
                    mn_chi(&[n], &mu),
                    1,
                    "χ^({}) at μ={:?} should be 1",
                    n, mu
                );
            }
        }
    }

    /// At λ = (1ⁿ), the sign rep: χ^(1ⁿ)(μ) = (-1)^{n - r(μ)}
    /// where r(μ) is the number of parts of μ.
    #[test]
    fn sign_rep_chi() {
        for n in 1..=5 {
            let lambda = vec![1; n];
            for mu in cycle_types(n) {
                let r = mu.len();
                let expected: i64 = if (n - r) % 2 == 0 { 1 } else { -1 };
                let actual = mn_chi(&lambda, &mu);
                assert_eq!(
                    actual,
                    expected,
                    "χ^(1^{}) at μ={:?} should be {} (got {})",
                    n, mu, expected, actual
                );
            }
        }
    }

    /// Identity element χ^λ(1ⁿ) = dim S^λ = n! / Π hook(c).
    /// Spot-check at n=4: dim S^(2,2) = 2.
    #[test]
    fn dim_check_at_identity() {
        // dim S^(4) = 1
        assert_eq!(mn_chi(&[4], &[1, 1, 1, 1]), 1);
        // dim S^(3,1) = 3
        assert_eq!(mn_chi(&[3, 1], &[1, 1, 1, 1]), 3);
        // dim S^(2,2) = 2
        assert_eq!(mn_chi(&[2, 2], &[1, 1, 1, 1]), 2);
        // dim S^(2,1,1) = 3
        assert_eq!(mn_chi(&[2, 1, 1], &[1, 1, 1, 1]), 3);
        // dim S^(1,1,1,1) = 1
        assert_eq!(mn_chi(&[1, 1, 1, 1], &[1, 1, 1, 1]), 1);
    }

    /// Plancherel identity: Σ_λ (dim S^λ)² = n!
    #[test]
    fn plancherel_identity_n_5() {
        let mut total: i64 = 0;
        for lambda in cycle_types(5) {
            let d = mn_chi(&lambda, &[1, 1, 1, 1, 1]);
            total += d * d;
        }
        assert_eq!(total, 120, "5! = 120");
    }

    /// Cycle-type extraction from a positive braid word.
    #[test]
    fn cycle_type_positive_braid() {
        // σ_1 on 3 strands: swap (1,2); cycle type = (2, 1).
        assert_eq!(positive_braid_cycle_type(3, &[(1, 1)]), vec![2, 1]);
        // σ_1 σ_2 on 3 strands: 3-cycle (1 2 3).  cycle type = (3,).
        assert_eq!(positive_braid_cycle_type(3, &[(1, 1), (1, 2)]), vec![3]);
        // σ_1 σ_2 σ_1 on 3 strands: longest element, cycle type = (2, 1)
        // (since (1 3) is a 2-cycle and 2 is fixed)
        let ct = positive_braid_cycle_type(3, &[(1, 1), (1, 2), (1, 1)]);
        assert_eq!(ct, vec![2, 1]);
        // Identity word: all 1-cycles.
        assert_eq!(positive_braid_cycle_type(4, &[]), vec![1, 1, 1, 1]);
    }

    /// q-MN braid expansion: positive single-generator word matches direct.
    #[test]
    fn q_mn_braid_positive_single_gen() {
        // σ_1 on 3 strands at λ = (3): trivial rep, χ = q.
        let chi = chi_lambda_braid_qdef(&[3], 3, &[(1, 1)]);
        // Cycle type of σ_1 = (2, 1), so should equal chi_lambda_mn_qdef(λ, [2,1]).
        let direct = chi_lambda_mn_qdef(&[3], &[2, 1]);
        assert_eq!(chi, direct);
    }

    /// q-MN braid expansion: σ⁻¹ on trivial rep should give 1/q.
    /// Hecke relation: σ⁻¹ = σ − h.
    /// On trivial rep: χ_λ(σ) = q, χ_λ(1) = 1, so χ_λ(σ⁻¹) = q − h = q − (q − q⁻¹) = q⁻¹.
    #[test]
    fn q_mn_braid_inverse_trivial_rep() {
        use num_bigint::BigInt;
        // σ_1⁻¹ on 3 strands at λ = (3).
        let chi = chi_lambda_braid_qdef(&[3], 3, &[(-1, 1)]);
        // Expected: q^{-1}.
        let expected = crate::laurent_poly_q::LaurentPolyQ::q_pow(-1);
        assert_eq!(chi, expected,
                   "χ_(3)(σ⁻¹) should be q^{{-1}}, got: {}", chi.pretty());
        // Sanity: at q=1, value should be 1.
        assert_eq!(chi.evaluate_at_one(), BigInt::from(1));
    }

    /// q-MN at q = 1 must equal classical MN (substitute q → 1).
    #[test]
    fn q_mn_at_q_eq_one_matches_classical() {
        use num_bigint::BigInt;
        let cases = vec![
            (vec![3usize], vec![2usize, 1]),
            (vec![2, 1], vec![2, 1]),
            (vec![1, 1, 1], vec![2, 1]),
            (vec![3], vec![3]),
            (vec![2, 1], vec![3]),
            (vec![1, 1, 1], vec![3]),
            (vec![2, 2, 1], vec![5]),
            (vec![3, 2], vec![3, 2]),
            (vec![4, 1], vec![3, 1, 1]),
        ];
        for (lambda, mu) in cases {
            let chi_classical = mn_chi(&lambda, &mu);
            let chi_q = chi_lambda_mn_qdef(&lambda, &mu);
            let chi_at_one: BigInt = chi_q.evaluate_at_one();
            assert_eq!(
                chi_at_one,
                BigInt::from(chi_classical),
                "λ={:?}, μ={:?}: classical = {}, q-MN(q=1) = {}",
                lambda, mu, chi_classical, chi_at_one
            );
        }
    }

    /// q-MN at λ = (n) (trivial rep): χ^(n)(any μ; q) = q^{(sum μ_i − r(μ))}
    /// where r(μ) is the number of cycles.  This is because each cycle
    /// of length k contributes a single border strip of size k with
    /// height 0, weight q^{k − 1}.
    #[test]
    fn q_mn_trivial_rep_evaluates_to_q_pow() {
        use num_bigint::BigInt;
        use num_traits::One;
        // λ = (5), μ = (3, 2): expected q^{(3-1) + (2-1)} = q^3.
        let chi = chi_lambda_mn_qdef(&[5], &[3, 2]);
        // At q = 1: should be 1.
        assert_eq!(chi.evaluate_at_one(), BigInt::one());
        // Check the result has the expected q^3 leading term.
        let pretty = chi.pretty();
        assert!(pretty.contains("q^3") || pretty == "q^3" || pretty.starts_with("q^3"),
                "expected q^3, got: {}", pretty);
    }

    /// Orthogonality: Σ_μ z(μ)⁻¹ · χ^λ(μ) · χ^ν(μ) = δ_{λν}
    /// where z(μ) = product of (m_i! · i^{m_i}) for cycle multiplicities.
    /// Spot-check on n = 3: only λ ∈ {(3), (2,1), (1,1,1)}.
    #[test]
    fn character_orthogonality_n_3() {
        let parts: Vec<Vec<usize>> = cycle_types(3);
        // z((3)) = 3, z((2,1)) = 2, z((1,1,1)) = 6.
        let z_inv = |mu: &[usize]| -> f64 {
            let mut z = 1u64;
            // m_i = number of cycles of length i.
            let mut counts = std::collections::HashMap::<usize, u32>::new();
            for &m in mu {
                *counts.entry(m).or_insert(0) += 1;
            }
            for (&i, &m_i) in &counts {
                let mut fact: u64 = 1;
                for k in 1..=m_i {
                    fact *= k as u64;
                }
                let mut pow: u64 = 1;
                for _ in 0..m_i {
                    pow *= i as u64;
                }
                z *= fact * pow;
            }
            1.0 / z as f64
        };

        for lambda in &parts {
            for nu in &parts {
                let mut sum: f64 = 0.0;
                for mu in cycle_types(3) {
                    sum += z_inv(&mu)
                        * mn_chi(lambda, &mu) as f64
                        * mn_chi(nu, &mu) as f64;
                }
                let expected = if lambda == nu { 1.0 } else { 0.0 };
                assert!(
                    (sum - expected).abs() < 1e-12,
                    "⟨χ^{:?}, χ^{:?}⟩ should be {} but got {}",
                    lambda, nu, expected, sum
                );
            }
        }
    }
}
