//! Littlewood-Richardson coefficients `c^λ_{μν}`.
//!
//! For partitions λ ⊢ n, μ ⊢ p, ν ⊢ q with n = p + q, the LR
//! coefficient `c^λ_{μν}` is the number of LR tableaux of skew shape
//! λ/μ with content ν.  Equivalently, it is the multiplicity of the
//! Specht module `S^λ` in the induced representation
//! `Ind_{S_p × S_q}^{S_n} S^μ ⊠ S^ν`.
//!
//! Used by F4 composer (`chi_via_factorization`) to combine cached
//! sub-character data: for a tensor-product factorization
//! `β = β_1 ⊗ β_2`,
//!
//!   χ_λ(β) = Σ_{μ ⊢ p, ν ⊢ q} c^λ_{μν} · χ_μ(β_1) · χ_ν(β_2)
//!
//! ## Algorithm
//!
//! Enumerate semistandard Young tableaux (SSYT) of skew shape λ/μ
//! with content ν, filter by the **lattice / reverse-reading-word**
//! property: every prefix of the reverse reading word must have
//! more `1`s than `2`s, more `2`s than `3`s, etc.
//!
//! ## References
//!
//! - **Stanley EC2** §7.18 (LR rule).
//! - **Sagan 2001** "The Symmetric Group" §4.9.
//! - **Macdonald 1995** "Symmetric Functions and Hall Polynomials" §I.9.

/// Compute Littlewood-Richardson coefficient `c^λ_{μν}`.
///
/// `lambda`: outer partition λ.
/// `mu`: inner partition μ (must satisfy μ ⊆ λ componentwise).
/// `nu`: content partition ν.
///
/// Returns 0 if `|λ| ≠ |μ| + |ν|` or if `μ ⊄ λ`.
pub fn lr_coefficient(lambda: &[usize], mu: &[usize], nu: &[usize]) -> i64 {
    let n_lambda: usize = lambda.iter().sum();
    let n_mu: usize = mu.iter().sum();
    let n_nu: usize = nu.iter().sum();
    if n_lambda != n_mu + n_nu {
        return 0;
    }
    // μ ⊆ λ check.
    for (i, &m) in mu.iter().enumerate() {
        if i >= lambda.len() || lambda[i] < m {
            return 0;
        }
    }
    // Enumerate SSYT of skew shape λ/μ with content ν, filter by
    // lattice property.  We use a recursive cell-by-cell filling.

    // Cells of λ/μ in standard reading order (top-to-bottom, left-
    // to-right).
    let mut cells: Vec<(usize, usize)> = Vec::new();
    for i in 0..lambda.len() {
        let start = if i < mu.len() { mu[i] } else { 0 };
        for j in start..lambda[i] {
            cells.push((i, j));
        }
    }
    if cells.len() != n_nu {
        return 0;
    }

    // Two-pass approach: enumerate all SSYTs using standard reading
    // order (top-to-bottom, left-to-right) for proper SSYT row/column
    // constraints; at each leaf, build the REVERSE reading word
    // (top-to-bottom, right-to-left within row) and verify ballot.

    let mut filling: Vec<usize> = vec![0; cells.len()];

    let mut count: i64 = 0;
    enumerate_ssyt_full(
        &cells, lambda, mu, nu,
        &mut filling,
        0,
        &mut count,
    );
    count
}

/// Enumerate all SSYTs with content ν, then verify ballot property
/// on the reverse reading word at each leaf.
fn enumerate_ssyt_full(
    cells: &[(usize, usize)],
    lambda: &[usize],
    mu: &[usize],
    nu: &[usize],
    filling: &mut [usize],
    cell_idx: usize,
    count: &mut i64,
) {
    if cell_idx == cells.len() {
        // Verify content matches ν.
        let mut content = vec![0usize; nu.len() + 1];
        for &v in filling.iter() {
            if v >= 1 && v <= nu.len() {
                content[v] += 1;
            }
        }
        for (v, &target) in nu.iter().enumerate() {
            if content[v + 1] != target {
                return;
            }
        }
        // Build reverse reading word using an incrementing pointer
        // since `cells` was populated in standard reading order
        // (Gemini review #r3143554489).
        let mut rrw: Vec<usize> = Vec::with_capacity(cells.len());
        let mut cell_ptr = 0;
        for i in 0..lambda.len() {
            let start = if i < mu.len() { mu[i] } else { 0 };
            let mut row_entries: Vec<usize> = Vec::with_capacity(lambda[i] - start);
            for _ in start..lambda[i] {
                row_entries.push(filling[cell_ptr]);
                cell_ptr += 1;
            }
            row_entries.reverse();
            rrw.extend(row_entries);
        }
        // Verify ballot: for every prefix, #(k) ≥ #(k+1) for all k.
        let mut prefix_count = vec![0usize; nu.len() + 2];
        for &v in &rrw {
            prefix_count[v] += 1;
            for k in 1..nu.len() {
                if prefix_count[k] < prefix_count[k + 1] {
                    return;
                }
            }
        }
        *count += 1;
        return;
    }
    let (r, c) = cells[cell_idx];
    let max_v = nu.len();
    let mut lb = 1usize;
    // Column-strict: > entry above (if above is in skew).
    if r > 0 && c >= mu_at(mu, r - 1) && c < lambda[r - 1] {
        if let Some(idx) = find_cell_idx(cells, r - 1, c) {
            lb = lb.max(filling[idx] + 1);
        }
    }
    // Row-weak: ≥ entry to the left (if left is in skew).
    if c > mu_at(mu, r) {
        if let Some(idx) = find_cell_idx(cells, r, c - 1) {
            lb = lb.max(filling[idx]);
        }
    }
    for v in lb..=max_v {
        filling[cell_idx] = v;
        enumerate_ssyt_full(cells, lambda, mu, nu, filling,
                             cell_idx + 1, count);
    }
}

// (Legacy `enumerate_ssyt` (filling-order lattice check) and helpers
// `mu_at`, `find_cell_idx` removed per Gemini review #r3143554491:
// superseded by `enumerate_ssyt_full` which performs the correct
// reverse-reading-word ballot check at each leaf.)

#[inline]
fn mu_at(mu: &[usize], i: usize) -> usize {
    if i < mu.len() { mu[i] } else { 0 }
}

#[inline]
fn find_cell_idx(cells: &[(usize, usize)], r: usize, c: usize) -> Option<usize> {
    cells.iter().position(|&(rr, cc)| rr == r && cc == c)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// LR coefficient of (λ, μ, ν) with μ = ν = ∅ and λ = ∅ is 1.
    #[test]
    fn lr_empty_partitions() {
        assert_eq!(lr_coefficient(&[], &[], &[]), 1);
    }

    /// `s_μ · s_∅ = s_μ`.  So c^μ_{μ, ∅} = 1.
    #[test]
    fn lr_with_empty_nu() {
        assert_eq!(lr_coefficient(&[3], &[3], &[]), 1);
        assert_eq!(lr_coefficient(&[2, 1], &[2, 1], &[]), 1);
    }

    /// `s_(1) · s_(1) = s_(2) + s_(1,1)`.
    /// So c^(2)_{(1),(1)} = c^(1,1)_{(1),(1)} = 1; others = 0.
    #[test]
    fn lr_pieri_simplest() {
        assert_eq!(lr_coefficient(&[2], &[1], &[1]), 1);
        assert_eq!(lr_coefficient(&[1, 1], &[1], &[1]), 1);
        assert_eq!(lr_coefficient(&[3], &[1], &[1]), 0);  // wrong size
    }

    /// `s_(2) · s_(1) = s_(3) + s_(2,1)`.
    /// `s_(1,1) · s_(1) = s_(2,1) + s_(1,1,1)`.
    #[test]
    fn lr_pieri_size_3() {
        assert_eq!(lr_coefficient(&[3], &[2], &[1]), 1);
        assert_eq!(lr_coefficient(&[2, 1], &[2], &[1]), 1);
        assert_eq!(lr_coefficient(&[1, 1, 1], &[2], &[1]), 0);
        assert_eq!(lr_coefficient(&[2, 1], &[1, 1], &[1]), 1);
        assert_eq!(lr_coefficient(&[1, 1, 1], &[1, 1], &[1]), 1);
    }

    /// `s_(2,1) · s_(1) = s_(3,1) + s_(2,2) + s_(2,1,1)`.
    #[test]
    fn lr_pieri_size_4() {
        assert_eq!(lr_coefficient(&[3, 1], &[2, 1], &[1]), 1);
        assert_eq!(lr_coefficient(&[2, 2], &[2, 1], &[1]), 1);
        assert_eq!(lr_coefficient(&[2, 1, 1], &[2, 1], &[1]), 1);
    }

    /// `s_(2) · s_(2) = s_(4) + s_(3,1) + s_(2,2)`.
    /// (Pieri rule: multiplying by s_(2) adds 2 cells in distinct columns.)
    #[test]
    fn lr_pieri_size_4_22() {
        assert_eq!(lr_coefficient(&[4], &[2], &[2]), 1);
        assert_eq!(lr_coefficient(&[3, 1], &[2], &[2]), 1);
        assert_eq!(lr_coefficient(&[2, 2], &[2], &[2]), 1);
        assert_eq!(lr_coefficient(&[2, 1, 1], &[2], &[2]), 0);
    }

    /// Symmetry: `c^λ_{μν} = c^λ_{νμ}`.
    #[test]
    fn lr_symmetry() {
        for (lam, mu, nu) in &[
            (vec![3, 1], vec![2, 1], vec![1]),
            (vec![2, 2], vec![2], vec![2]),
            (vec![3, 2, 1], vec![2, 1], vec![2, 1]),
        ] {
            assert_eq!(
                lr_coefficient(lam, mu, nu),
                lr_coefficient(lam, nu, mu),
                "λ={:?}, μ={:?}, ν={:?}", lam, mu, nu
            );
        }
    }
}
