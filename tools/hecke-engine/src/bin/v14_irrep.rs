// v14_irrep: Per-irrep Garside computation via Young's seminormal form.
//
// For typed quark orderings with 2-letter alphabet {u,d}, only
// 2-row partitions of S_n contribute (Schur-Weyl duality).
// This reduces 385 irreps of S_18 to just 10.
//
// Each irrep λ = (a,b) has dimension d_λ. The Garside element Δ_n
// is computed as a product of 153 crossing matrices (for n=18),
// each d_λ × d_λ. Only 2 matrices in memory at once (result + crossing).
//
// Memory: 2 × d² × 8 bytes. For d=13260: 2.8 GB.
// Time: d² × n_crossings per irrep, parallelizable across irreps.
//
// Usage:
//   hecke-irrep ORDERING [max_dim]

use std::time::Instant;
use rayon::prelude::*;

// ════════════════════════════════════════════════════════════════
// CODATA (same as v13)
// ════════════════════════════════════════════════════════════════

const VOL_FIGURE_EIGHT: f64 = 2.029883212819307;
const MASS_RATIO_MU_E: f64 = 206.7682830;
const M_E_MEV: f64 = 0.51099895000;

fn compute_q0() -> f64 {
    let hbar_q = (VOL_FIGURE_EIGHT / MASS_RATIO_MU_E).sqrt();
    1.0 / (1.0 - hbar_q)
}

// ════════════════════════════════════════════════════════════════
// Standard Young tableaux for 2-row partitions
// ════════════════════════════════════════════════════════════════

/// A standard Young tableau for shape (a,b) is encoded as a Vec<bool>
/// of length n = a+b. entry[i] = true means value i+1 is in row 1.
/// This is valid iff at every prefix, #row1 ≥ #row2 (ballot condition)
/// AND #row1 ≤ a, #row2 ≤ b.
fn generate_syt(a: usize, b: usize) -> Vec<Vec<bool>> {
    let n = a + b;
    let mut result = Vec::new();
    let mut current = Vec::with_capacity(n);

    fn recurse(current: &mut Vec<bool>, a: usize, b: usize, r1: usize, r2: usize, result: &mut Vec<Vec<bool>>) {
        let n = a + b;
        if current.len() == n {
            result.push(current.clone());
            return;
        }
        // Try row 1
        if r1 < a {
            current.push(true);
            recurse(current, a, b, r1 + 1, r2, result);
            current.pop();
        }
        // Try row 2 (must have r2 < r1 for standardness)
        if r2 < b && r2 < r1 {
            current.push(false);
            recurse(current, a, b, r1, r2 + 1, result);
            current.pop();
        }
    }

    recurse(&mut current, a, b, 0, 0, &mut result);
    result
}

/// Content of value v (1-indexed) in tableau T: col - row.
fn syt_content(tab: &[bool], v: usize) -> i32 {
    // v is 1-indexed, tab[v-1] gives the row
    let mut r1_count = 0;
    let mut r2_count = 0;
    for i in 0..v {
        if tab[i] { r1_count += 1; } else { r2_count += 1; }
    }
    // Position of v: if in row 1, it's at column r1_count-1, row 0
    // if in row 2, it's at column r2_count-1, row 1
    if tab[v - 1] {
        (r1_count - 1) as i32 // col - row = col - 0
    } else {
        (r2_count - 1) as i32 - 1 // col - row = col - 1
    }
}

/// Swap values k and k+1 in tableau. Returns None if result is not standard.
fn syt_swap(tab: &[bool], k: usize) -> Option<Vec<bool>> {
    // k is 1-indexed. Swap entries at positions k-1 and k.
    // They must be in different rows for the swap to potentially be standard.
    if tab[k - 1] == tab[k] { return None; } // same row, swap is identity in SYT terms

    let mut new_tab = tab.to_vec();
    new_tab[k - 1] = tab[k];
    new_tab[k] = tab[k - 1];

    // Check ballot condition: at every prefix, #row1 >= #row2
    let mut r1 = 0i32;
    let mut r2 = 0i32;
    for &in_row1 in &new_tab {
        if in_row1 { r1 += 1; } else { r2 += 1; }
        if r2 > r1 { return None; }
    }
    Some(new_tab)
}

// ════════════════════════════════════════════════════════════════
// Per-irrep Garside computation
// ════════════════════════════════════════════════════════════════

/// Compute σ_{gen_k} matrix element for two tableaux in seminormal form.
/// Returns (diagonal, off_diagonal_to_swapped).
fn seminormal_entry(tab: &[bool], gen_k: usize, q: f64) -> (f64, Option<f64>) {
    let k = gen_k + 1; // values to swap (1-indexed)
    let qi = 1.0 / q;
    let ha = q - qi;

    let d = syt_content(tab, k + 1) - syt_content(tab, k);

    if d == 0 { panic!("d=0 at gen_k={}", gen_k); }

    if d == 1 {
        (q, None)
    } else if d == -1 {
        (-qi, None)
    } else {
        let qd = q.powi(d);
        let qdi = q.powi(-d);
        let diag = ha / (qd - qdi);
        let off = (1.0 - diag * diag).max(0.0).sqrt();
        (diag, Some(off))
    }
}

/// Build the crossing list for the Garside staircase.
/// Returns Vec of (sweep, level+1) pairs.
fn garside_crossings(n: usize) -> Vec<(usize, usize)> {
    let mut crossings = Vec::new();
    for level in 0..n-1 {
        for sweep in (0..=level).rev() {
            crossings.push((sweep, level + 1));
        }
    }
    crossings
}

/// Compute tr(ρ_λ(Δ_n)) for BOTH parent and daughter orderings
/// with common-prefix optimization.
///
/// Splits the Garside staircase into prefix / branch / suffix.
/// Prefix and suffix are computed once (shared crossings).
/// Branch is computed separately for parent and daughter.
fn garside_trace_pair(
    a: usize, b: usize,
    par_ordering: &[u8], dau_ordering: &[u8],
    q: f64,
) -> (f64, f64) {
    let n = a + b;
    assert_eq!(n, par_ordering.len());
    assert_eq!(n, dau_ordering.len());

    let ha = q - 1.0 / q;
    let tabs = generate_syt(a, b);
    let dim = tabs.len();
    if dim == 0 { return (0.0, 0.0); }

    let mut tab_idx: std::collections::HashMap<Vec<bool>, usize> = std::collections::HashMap::new();
    for (i, t) in tabs.iter().enumerate() {
        tab_idx.insert(t.clone(), i);
    }

    let crossings = garside_crossings(n);

    // Find which crossings differ
    let differs: Vec<bool> = crossings.iter().map(|&(s, l)| {
        par_ordering[s] != dau_ordering[s] || par_ordering[l] != dau_ordering[l]
    }).collect();

    let first_diff = differs.iter().position(|&d| d).unwrap_or(crossings.len());
    let last_diff = differs.iter().rposition(|&d| d).unwrap_or(0);

    // Helper: apply one crossing to matrix
    let apply_crossing = |result: &mut Vec<f64>, sweep: usize, ordering: &[u8]| {
        let ti = ordering[sweep];
        let tj = ordering[crossings.iter().find(|&&(s,_)| s == sweep).map(|&(_,l)| l).unwrap_or(0)];
        // Actually we need the specific (sweep, level) pair, not just sweep
        // This closure needs the level too. Let me restructure.
    };

    // Simpler: just split into prefix, branch_par, branch_dau, suffix
    // and use the existing garside_trace logic for each section.

    let apply_section = |result: &mut Vec<f64>, crossings_slice: &[(usize, usize)], ordering: &[u8]| {
        for &(sweep, level_plus_1) in crossings_slice {
            let ti = ordering[sweep];
            let tj = ordering[level_plus_1];
            let d_coeff = match (ti, tj) {
                (b'p', b'p') | (b'u', b'u') => 0.0,
                (b'n', b'n') | (b'd', b'd') => -ha,
                _ => -ha / 2.0,
            };

            let mut new_result = vec![0.0f64; dim * dim];
            for j in 0..dim {
                let (diag, off) = seminormal_entry(&tabs[j], sweep, q);
                let diag_total = diag + d_coeff;
                let swap_info = if let Some(off_val) = off {
                    if let Some(swapped) = syt_swap(&tabs[j], sweep + 1) {
                        tab_idx.get(&swapped).map(|&j2| (j2, off_val))
                    } else { None }
                } else { None };
                for i in 0..dim {
                    let r_ij = result[i * dim + j];
                    if r_ij.abs() < 1e-300 { continue; }
                    new_result[i * dim + j] += r_ij * diag_total;
                    if let Some((j2, off_val)) = swap_info {
                        new_result[i * dim + j2] += r_ij * off_val;
                    }
                }
            }
            *result = new_result;
        }
    };

    // Prefix: identical for parent and daughter
    let prefix = &crossings[..first_diff];
    let mut prefix_result = vec![0.0f64; dim * dim];
    for i in 0..dim { prefix_result[i * dim + i] = 1.0; }
    apply_section(&mut prefix_result, prefix, par_ordering); // same for both

    // Branch: different for parent and daughter
    let branch = &crossings[first_diff..=last_diff.min(crossings.len()-1)];
    let mut par_result = prefix_result.clone();
    let mut dau_result = prefix_result;
    apply_section(&mut par_result, branch, par_ordering);
    apply_section(&mut dau_result, branch, dau_ordering);

    // Suffix: identical again
    let suffix = &crossings[last_diff+1..];
    apply_section(&mut par_result, suffix, par_ordering);
    apply_section(&mut dau_result, suffix, dau_ordering);

    // Traces
    let tr_par: f64 = (0..dim).map(|i| par_result[i * dim + i]).sum();
    let tr_dau: f64 = (0..dim).map(|i| dau_result[i * dim + i]).sum();

    (tr_par, tr_dau)
}

/// Compute tr(ρ_λ(Δ_n)) for a typed quark ordering (single).
/// Only builds ONE matrix at a time (the accumulated result).
/// The crossing matrix is applied row-by-row without materializing it.
fn garside_trace(a: usize, b: usize, quark_ordering: &[u8], q: f64) -> f64 {
    let n = a + b;
    assert_eq!(n, quark_ordering.len());

    let ha = q - 1.0 / q;
    let tabs = generate_syt(a, b);
    let dim = tabs.len();
    if dim == 0 { return 0.0; }

    // Index lookup for swapped tableaux
    let mut tab_idx: std::collections::HashMap<Vec<bool>, usize> = std::collections::HashMap::new();
    for (i, t) in tabs.iter().enumerate() {
        tab_idx.insert(t.clone(), i);
    }

    // Result matrix: start with identity
    let mut result = vec![0.0f64; dim * dim];
    for i in 0..dim { result[i * dim + i] = 1.0; }

    // Apply each crossing in Garside order (right-to-left sweep)
    for level in 0..n - 1 {
        for sweep in (0..=level).rev() {
            // Typed crossing coefficient
            let ti = quark_ordering[sweep];
            let tj = quark_ordering[level + 1];
            let d_coeff = match (ti, tj) {
                (b'u', b'u') | (b'p', b'p') => 0.0,
                (b'd', b'd') | (b'n', b'n') => -ha,
                _ => -ha / 2.0,
            };

            // SPARSE IN-PLACE: each crossing is a 2×2 block on column pairs.
            // Precompute the crossing structure for this generator.
            // Process swap pairs together, unpaired columns just scale.
            // NO allocation — update result in place.

            let mut processed = vec![false; dim];
            for j in 0..dim {
                if processed[j] { continue; }
                let (diag_j, off_j) = seminormal_entry(&tabs[j], sweep, q);
                let dj = diag_j + d_coeff;

                if let Some(off_val_j) = off_j {
                    // j has a swap partner — find it
                    if let Some(swapped) = syt_swap(&tabs[j], sweep + 1) {
                        if let Some(&j2) = tab_idx.get(&swapped) {
                            if !processed[j2] {
                                // Process pair (j, j2) as a 2×2 block
                                let (diag_j2, _) = seminormal_entry(&tabs[j2], sweep, q);
                                let dj2 = diag_j2 + d_coeff;
                                // The off-diagonal from j2 to j
                                let off_val_j2 = if let Some(sw2) = syt_swap(&tabs[j2], sweep + 1) {
                                    if tab_idx.get(&sw2) == Some(&j) {
                                        seminormal_entry(&tabs[j2], sweep, q).1.unwrap_or(0.0)
                                    } else { 0.0 }
                                } else { 0.0 };

                                // In-place 2×2: for each row i:
                                //   result[i,j]  = old[i,j]*dj + old[i,j2]*off_j2
                                //   result[i,j2] = old[i,j]*off_j + old[i,j2]*dj2
                                for i in 0..dim {
                                    let rj = result[i * dim + j];
                                    let rj2 = result[i * dim + j2];
                                    result[i * dim + j]  = rj * dj  + rj2 * off_val_j2;
                                    result[i * dim + j2] = rj * off_val_j + rj2 * dj2;
                                }
                                processed[j] = true;
                                processed[j2] = true;
                                continue;
                            }
                        }
                    }
                }

                // Unpaired or partner already processed: just scale column j
                if !processed[j] {
                    for i in 0..dim {
                        result[i * dim + j] *= dj;
                    }
                    processed[j] = true;
                }
            }
        }
    }

    // Trace
    let mut tr = 0.0;
    for i in 0..dim { tr += result[i * dim + i]; }
    tr
}

// ════════════════════════════════════════════════════════════════
// VECTOR ACTION: O(n_crossings × dim) per matrix element
// ════════════════════════════════════════════════════════════════

/// Apply the typed Garside element to a single vector: |ψ⟩ = Δ|v⟩.
/// Each crossing acts via sparse 2×2 blocks: O(dim) per crossing.
/// Total: O(n_crossings × dim) instead of O(n_crossings × dim²).
///
/// For dim=13260 and 153 crossings: ~2M ops vs ~27B ops (13260× speedup).
fn garside_apply_vector(
    a: usize, b: usize,
    quark_ordering: &[u8],
    initial: &[f64],
    q: f64,
) -> Vec<f64> {
    let n = a + b;
    assert_eq!(n, quark_ordering.len());

    let ha = q - 1.0 / q;
    let tabs = generate_syt(a, b);
    let dim = tabs.len();
    if dim == 0 { return vec![]; }

    let mut tab_idx: std::collections::HashMap<Vec<bool>, usize> = std::collections::HashMap::new();
    for (i, t) in tabs.iter().enumerate() {
        tab_idx.insert(t.clone(), i);
    }

    // Precompute swap partners and seminormal data for each generator
    // (sweep position). Cache: for each (gen, tableau_idx) → (diag, partner_idx, off_diag)
    struct CrossingData {
        diag: f64,
        partner: Option<(usize, f64)>,  // (partner_idx, off_diagonal)
    }

    let mut gen_crossing_data: Vec<Vec<CrossingData>> = Vec::with_capacity(n - 1);
    for gen in 0..n-1 {
        let mut data = Vec::with_capacity(dim);
        for j in 0..dim {
            let (diag_j, off_j) = seminormal_entry(&tabs[j], gen, q);
            let partner = if let Some(off_val) = off_j {
                if let Some(swapped) = syt_swap(&tabs[j], gen + 1) {
                    tab_idx.get(&swapped).map(|&j2| (j2, off_val))
                } else { None }
            } else { None };
            data.push(CrossingData { diag: diag_j, partner });
        }
        gen_crossing_data.push(data);
    }

    let mut vec = initial.to_vec();
    assert_eq!(vec.len(), dim);

    // Apply each crossing in Garside order
    for level in 0..n - 1 {
        for sweep in (0..=level).rev() {
            let ti = quark_ordering[sweep];
            let tj = quark_ordering[level + 1];
            let d_coeff = match (ti, tj) {
                (b'u', b'u') | (b'p', b'p') => 0.0,
                (b'd', b'd') | (b'n', b'n') => -ha,
                _ => -ha / 2.0,
            };

            let cdata = &gen_crossing_data[sweep];

            // Apply sparse crossing to vector
            let mut processed = vec![false; dim];
            for j in 0..dim {
                if processed[j] { continue; }
                let dj = cdata[j].diag + d_coeff;

                if let Some((j2, off_j)) = cdata[j].partner {
                    if !processed[j2] {
                        let dj2 = cdata[j2].diag + d_coeff;
                        // off_j2 = off-diagonal from j2 column to j row
                        let off_j2 = cdata[j2].partner
                            .filter(|&(p, _)| p == j)
                            .map(|(_, o)| o)
                            .unwrap_or(0.0);

                        // 2×2 block action on vector components j and j2:
                        //   new[j]  = old[j]*dj  + old[j2]*off_j2
                        //   new[j2] = old[j]*off_j + old[j2]*dj2
                        let vj = vec[j];
                        let vj2 = vec[j2];
                        vec[j]  = vj * dj  + vj2 * off_j2;
                        vec[j2] = vj * off_j + vj2 * dj2;

                        processed[j] = true;
                        processed[j2] = true;
                        continue;
                    }
                }

                // Unpaired: just scale
                if !processed[j] {
                    vec[j] *= dj;
                    processed[j] = true;
                }
            }
        }
    }

    vec
}

/// Compute the matrix element ⟨v|Δ|v⟩ for the typed Garside element.
fn garside_matrix_element(
    a: usize, b: usize,
    quark_ordering: &[u8],
    v: &[f64],
    q: f64,
) -> f64 {
    let result = garside_apply_vector(a, b, quark_ordering, v, q);
    // Inner product ⟨v|result⟩
    v.iter().zip(result.iter()).map(|(a, b)| a * b).sum()
}

/// Compute ALL diagonal elements ⟨e_i|Δ|e_i⟩ via vector action.
/// This gives the full trace as the sum: tr(Δ) = Σ_i ⟨e_i|Δ|e_i⟩.
/// Cost: O(dim × n_crossings × dim) — same as matrix method,
/// but uses O(dim) memory instead of O(dim²).
fn garside_all_diagonals(
    a: usize, b: usize,
    quark_ordering: &[u8],
    q: f64,
) -> Vec<f64> {
    let dim = generate_syt(a, b).len();
    (0..dim).map(|i| {
        let mut e_i = vec![0.0f64; dim];
        e_i[i] = 1.0;
        let result = garside_apply_vector(a, b, quark_ordering, &e_i, q);
        result[i]  // ⟨e_i|Δ|e_i⟩
    }).collect()
}

/// Kostka support check: K_{(a,b),(n_u,n_d)} > 0 iff a >= max(n_u, n_d).
fn kostka_supported(a: usize, b: usize, n_u: usize, n_d: usize) -> bool {
    let n = a + b;
    if n_u + n_d != n { return false; }
    a >= n_u.max(n_d)
}

// ════════════════════════════════════════════════════════════════
// CONFINEMENT EIGENVECTOR: q-torsion leaf projection
// ════════════════════════════════════════════════════════════════
//
// The T_{2,3} trefoil σ_k · σ_{k+1} · σ_k confines each nucleon triple.
// For A nucleons, the combined confinement operator is:
//   K_conf = Π_{nucleon m=0..A-1} T_{2,3}(strands 3m, 3m+1, 3m+2)
//
// The leading eigenvector of K_conf is the q-torsion leaf — the
// invariant submanifold where the q-curvature is minimized.
//
// Power iteration finds it in O(iterations × 3A × dim) time.

/// Apply a single generator σ_gen to a vector (sparse 2×2 blocks).
/// This is the core building block for trefoil and Garside actions.
fn apply_generator_to_vector(
    gen: usize,
    d_coeff: f64,
    vec: &mut [f64],
    gen_crossing_data: &[(f64, Option<(usize, f64)>)], // (diag, partner)
) {
    let dim = vec.len();
    let mut processed = vec![false; dim];
    for j in 0..dim {
        if processed[j] { continue; }
        let dj = gen_crossing_data[j].0 + d_coeff;

        if let Some((j2, off_j)) = gen_crossing_data[j].1 {
            if !processed[j2] {
                let dj2 = gen_crossing_data[j2].0 + d_coeff;
                let off_j2 = gen_crossing_data[j2].1
                    .filter(|&(p, _)| p == j)
                    .map(|(_, o)| o)
                    .unwrap_or(0.0);

                let vj = vec[j];
                let vj2 = vec[j2];
                vec[j]  = vj * dj  + vj2 * off_j2;
                vec[j2] = vj * off_j + vj2 * dj2;
                processed[j] = true;
                processed[j2] = true;
                continue;
            }
        }

        if !processed[j] {
            vec[j] *= dj;
            processed[j] = true;
        }
    }
}

/// Precompute crossing data for all generators of an irrep.
/// Returns: Vec<Vec<(diag, Option<(partner_idx, off_diag)>)>>
fn precompute_crossing_data(
    tabs: &[Vec<bool>],
    tab_idx: &std::collections::HashMap<Vec<bool>, usize>,
    n: usize,
    q: f64,
) -> Vec<Vec<(f64, Option<(usize, f64)>)>> {
    let dim = tabs.len();
    (0..n-1).map(|gen| {
        (0..dim).map(|j| {
            let (diag_j, off_j) = seminormal_entry(&tabs[j], gen, q);
            let partner = if let Some(off_val) = off_j {
                if let Some(swapped) = syt_swap(&tabs[j], gen + 1) {
                    tab_idx.get(&swapped).map(|&j2| (j2, off_val))
                } else { None }
            } else { None };
            (diag_j, partner)
        }).collect()
    }).collect()
}

// ════════════════════════════════════════════════════════════════
// KNOT OPERATOR LIBRARY
// ════════════════════════════════════════════════════════════════
//
// Each knot operator is a braid word acting on 3 strands (per nucleon).
// The combined operator for A nucleons applies the knot to each B₃ triple.
// Generator indices are offset by 3m for nucleon m.

/// A knot operator defined by its braid word on B₃.
/// Each entry is a generator index (0 or 1) and sign (+1 or -1).
/// The braid word is applied left-to-right.
struct KnotOperator {
    name: &'static str,
    /// Braid word: Vec of (generator_offset, sign).
    /// generator_offset 0 = σ₀, 1 = σ₁ within each B₃.
    /// sign: +1 for σ, -1 for σ⁻¹ = σ - h (Hecke inverse).
    word: Vec<(usize, i8)>,
}

fn knot_operators() -> Vec<KnotOperator> {
    vec![
        KnotOperator {
            name: "T_{2,3}",  // trefoil = electron
            word: vec![(0, 1), (1, 1), (0, 1)],  // σ₀σ₁σ₀
        },
        KnotOperator {
            name: "T_{2,5}",  // cinquefoil = muon
            word: vec![(0, 1), (1, 1), (0, 1), (1, 1), (0, 1)],  // σ₀σ₁σ₀σ₁σ₀
        },
        KnotOperator {
            name: "T_{3,4}",  // Hopf² color
            word: vec![(0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (0, 1), (1, 1), (0, 1)],
        },
        KnotOperator {
            name: "T_{3,5}",  // weak force
            word: vec![(0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1)],
        },
        KnotOperator {
            name: "Borromean",  // σ₀σ₁⁻¹σ₀σ₁⁻¹σ₀σ₁⁻¹
            word: vec![(0, 1), (1, -1), (0, 1), (1, -1), (0, 1), (1, -1)],
        },
        KnotOperator {
            name: "figure-8",  // σ₀σ₁⁻¹σ₀σ₁⁻¹
            word: vec![(0, 1), (1, -1), (0, 1), (1, -1)],
        },
    ]
}

/// Apply a knot operator to a vector for ALL nucleons.
/// For inverse generators (sign = -1): σ⁻¹ = σ - h (Hecke relation).
/// So σ⁻¹|v⟩ = σ|v⟩ - h|v⟩ = (σ + (-h)·I)|v⟩.
fn apply_knot_operator(
    knot: &KnotOperator,
    n_nucleons: usize,
    n: usize,
    vec: &mut [f64],
    cdata: &[Vec<(f64, Option<(usize, f64)>)>],
    ha: f64,
) {
    for m in 0..n_nucleons {
        for &(gen_offset, sign) in &knot.word {
            let gen = 3 * m + gen_offset;
            if gen >= n - 1 { continue; }
            // For positive sign: apply σ_gen with d_coeff = 0
            // For negative sign (inverse): σ⁻¹ = σ - h, so d_coeff = -h
            let d_coeff = if sign > 0 { 0.0 } else { -ha };
            apply_generator_to_vector(gen, d_coeff, vec, &cdata[gen]);
        }
    }
}

/// Find the MINIMUM eigenvalue eigenvector via shift-and-invert power iteration.
///
/// The confinement LP MINIMIZES action. The ground state = minimum eigenvalue
/// of the knot operator = tightest confinement = q⁻¹ channel (antisymmetric).
///
/// Method:
///   1. Power iteration on K to find λ_max (a few iterations suffice)
///   2. Shift: B = λ_max·I - K (flips spectrum: λ_min of K → λ_max of B)
///   3. Power iteration on B to find eigenvector of λ_max(B) = λ_min(K)
///
/// The shift-and-invert is exact because applying B|v⟩ = λ_max|v⟩ - K|v⟩
/// only requires K|v⟩ (which we already have).
fn knot_eigenvector(
    a: usize, b: usize,
    knot: &KnotOperator,
    n_nucleons: usize,
    q: f64,
    max_iter: usize,
    tol: f64,
) -> (Vec<f64>, f64) {
    let n = a + b;
    let ha = q - 1.0 / q;
    let tabs = generate_syt(a, b);
    let dim = tabs.len();

    let mut tab_idx: std::collections::HashMap<Vec<bool>, usize> = std::collections::HashMap::new();
    for (i, t) in tabs.iter().enumerate() {
        tab_idx.insert(t.clone(), i);
    }

    let cdata = precompute_crossing_data(&tabs, &tab_idx, n, q);

    if dim <= 1 {
        // 1D: only one eigenvector
        let mut v = vec![1.0; dim];
        let mut w = v.clone();
        apply_knot_operator(knot, n_nucleons, n, &mut w, &cdata, ha);
        let eigenvalue = if dim == 1 { w[0] } else { 0.0 };
        return (v, eigenvalue);
    }

    // Step 1: Find λ_max via standard power iteration (20 iterations suffice)
    let inv_sqrt_dim = 1.0 / (dim as f64).sqrt();
    let mut v = vec![inv_sqrt_dim; dim];
    let mut lambda_max = 0.0f64;

    for _ in 0..30 {
        apply_knot_operator(knot, n_nucleons, n, &mut v, &cdata, ha);
        let norm: f64 = v.iter().map(|x| x * x).sum::<f64>().sqrt();
        if norm < 1e-300 { break; }
        lambda_max = norm;
        for x in v.iter_mut() { *x /= norm; }
    }

    // Step 2: Power iteration on B = λ_shift·I - K to find λ_min(K).
    // Use λ_shift slightly above λ_max to ensure B is positive definite.
    let lambda_shift = lambda_max * 1.1 + 1.0;

    let mut v = vec![inv_sqrt_dim; dim];
    // Perturb to avoid landing on the same eigenvector as λ_max
    v[0] += 0.1;
    let norm0: f64 = v.iter().map(|x| x * x).sum::<f64>().sqrt();
    for x in v.iter_mut() { *x /= norm0; }

    let mut eigenvalue_b = 0.0f64;

    for _iter in 0..max_iter {
        // Compute K|v⟩
        let mut kv = v.clone();
        apply_knot_operator(knot, n_nucleons, n, &mut kv, &cdata, ha);

        // B|v⟩ = λ_shift·|v⟩ - K|v⟩
        for j in 0..dim {
            kv[j] = lambda_shift * v[j] - kv[j];
        }

        let norm: f64 = kv.iter().map(|x| x * x).sum::<f64>().sqrt();
        if norm < 1e-300 { break; }
        let new_eigenvalue_b = norm;
        for x in kv.iter_mut() { *x /= norm; }
        v = kv;

        if (new_eigenvalue_b - eigenvalue_b).abs() / (eigenvalue_b.abs() + 1e-15) < tol {
            eigenvalue_b = new_eigenvalue_b;
            break;
        }
        eigenvalue_b = new_eigenvalue_b;
    }

    // λ_min(K) = λ_shift - λ_max(B)
    let lambda_min = lambda_shift - eigenvalue_b;

    (v, lambda_min)
}

/// Compute matrix element ⟨v_K|Δ|v_K⟩ for a specific knot operator K.
fn garside_knot_element(
    a: usize, b: usize,
    quark_ordering: &[u8],
    knot: &KnotOperator,
    n_nucleons: usize,
    q: f64,
) -> (f64, f64) {
    let (v_knot, eigenvalue) = knot_eigenvector(a, b, knot, n_nucleons, q, 200, 1e-12);
    let me = garside_matrix_element(a, b, quark_ordering, &v_knot, q);
    (me, eigenvalue)
}

// ════════════════════════════════════════════════════════════════
// Main
// ════════════════════════════════════════════════════════════════

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let use_vector = args.iter().any(|a| a == "--vector" || a == "-v");
    let use_confine = args.iter().any(|a| a == "--confine" || a == "-c");
    let positional: Vec<&String> = args[1..].iter().filter(|a| !a.starts_with('-')).collect();

    if positional.is_empty() {
        eprintln!("hecke-irrep v14 — Per-irrep Garside via Young's seminormal form");
        eprintln!();
        eprintln!("Usage: hecke-irrep [--vector|--confine] PARENT DAUGHTER [max_dim]");
        eprintln!("  Orderings: u/d strings (quark level, length must be 3×A)");
        eprintln!("  --vector:  Compute diagonal ⟨e_i|Δ|e_i⟩ via O(dim) vector action");
        eprintln!("  --confine: Compute ⟨v_conf|Δ|v_conf⟩ where v_conf is the");
        eprintln!("             leading eigenvector of the T_{{2,3}} confinement operator.");
        eprintln!("             This is the q-torsion leaf projection — the physical");
        eprintln!("             state selected by Borromean B₃ confinement.");
        eprintln!("             Cost: O(n_crossings × dim) per irrep (same as --vector)");
        eprintln!("  max_dim:   skip irreps with dim > this (default: unlimited)");
        std::process::exit(1);
    }

    let q0 = compute_q0();
    let ha = q0 - 1.0 / q0;

    let par_str = positional[0].as_str();
    let dau_str = if positional.len() > 1 { positional[1].as_str() } else { par_str };
    let max_dim: usize = positional.get(2).and_then(|s| s.parse().ok()).unwrap_or(usize::MAX);

    let par_types: Vec<u8> = par_str.chars().map(|c| match c {
        'u' | 'p' | '1' => b'p', _ => b'n',
    }).collect();
    let dau_types: Vec<u8> = dau_str.chars().map(|c| match c {
        'u' | 'p' | '1' => b'p', _ => b'n',
    }).collect();

    let n = par_types.len();
    assert_eq!(n, dau_types.len(), "Parent and daughter must have same length");

    let n_u_par = par_types.iter().filter(|&&t| t == b'p').count();
    let n_d_par = par_types.iter().filter(|&&t| t == b'n').count();
    let n_u_dau = dau_types.iter().filter(|&&t| t == b'p').count();
    let n_d_dau = dau_types.iter().filter(|&&t| t == b'n').count();

    eprintln!("hecke-irrep v14 — q₀ = {:.15} (derived from CODATA)", q0);
    eprintln!("  mode:     {}", if use_vector { "VECTOR (O(dim) per element)" } else { "MATRIX (O(dim²) full product)" });
    eprintln!("  parent:   {} (n={}, {}u+{}d)", par_str, n, n_u_par, n_d_par);
    eprintln!("  daughter: {} ({}u+{}d)", dau_str, n_u_dau, n_d_dau);

    // 2-row partitions of n
    let all_partitions: Vec<(usize, usize)> = (0..=n/2).map(|b| (n - b, b)).collect();

    // Kostka support filtering
    let partitions: Vec<(usize, usize)> = all_partitions.iter()
        .filter(|&&(a, b)| {
            let k_par = kostka_supported(a, b, n_u_par, n_d_par);
            let k_dau = kostka_supported(a, b, n_u_dau, n_d_dau);
            // Need support for at least one of parent/daughter to have nonzero Δ
            k_par || k_dau
        })
        .cloned()
        .collect();

    let skipped_kostka = all_partitions.len() - partitions.len();
    eprintln!("  {} two-row irreps ({} skipped by Kostka K=0)", partitions.len(), skipped_kostka);

    let t_total = Instant::now();

    // ────────────────────────────────────────────────────────────
    //  VECTOR MODE: O(dim) per crossing, O(dim) memory
    // ────────────────────────────────────────────────────────────
    if use_vector {
        eprintln!("  Vector mode: computing diagonal elements ⟨e_i|Δ|e_i⟩");
        eprintln!("  Memory per irrep: O(dim) instead of O(dim²)");

        // ALL irreps can run in parallel — only O(dim) memory each
        let results: Vec<(usize, usize, usize, f64, f64, f64, f64)> = partitions.par_iter()
            .filter_map(|&(a, b)| {
                let dim = generate_syt(a, b).len();
                if dim > max_dim || dim == 0 { return None; }

                let t0 = Instant::now();

                // Compute all diagonal elements for parent and daughter
                let diag_par = garside_all_diagonals(a, b, &par_types, q0);
                let diag_dau = garside_all_diagonals(a, b, &dau_types, q0);

                let tr_par: f64 = diag_par.iter().sum();
                let tr_dau: f64 = diag_dau.iter().sum();
                let dtr = tr_dau - tr_par;

                let elapsed = t0.elapsed().as_secs_f64();
                let mem_kb = dim * 8 * 2 / 1024;  // 2 vectors

                eprintln!("  λ=({},{}): dim={:>6} ({} KB), tr_par={:>+12.4}, tr_dau={:>+12.4}, Δtr={:>+14.6e}, {:.1}s",
                    a, b, dim, mem_kb, tr_par, tr_dau, dtr, elapsed);

                Some((a, b, dim, tr_par, tr_dau, dtr, elapsed))
            })
            .collect();

        let total_dtr: f64 = results.iter().map(|r| r.5).sum();
        let q_pred = total_dtr.abs() * M_E_MEV;
        let elapsed_total = t_total.elapsed().as_secs_f64();

        eprintln!("\n  Σ Δtr = {:+.10e}", total_dtr);
        eprintln!("  Q = |Σ Δtr| × m_e = {:.6} MeV", q_pred);
        eprintln!("  Total: {:.1}s", elapsed_total);

        // JSON output
        print!("{{\"mode\":\"vector\",\"parent\":\"{}\",\"daughter\":\"{}\",\"n\":{},\"n_irreps\":{}", par_str, dau_str, n, results.len());
        print!(",\"irreps\":[");
        for (i, (a, b, dim, tr_p, tr_d, dtr, t)) in results.iter().enumerate() {
            if i > 0 { print!(","); }
            print!("{{\"a\":{},\"b\":{},\"dim\":{},\"tr_par\":{:.10e},\"tr_dau\":{:.10e},\"dtr\":{:.10e},\"time\":{:.3}}}",
                a, b, dim, tr_p, tr_d, dtr, t);
        }
        println!("],\"total_dtr\":{:.10e},\"q_mev\":{:.6},\"q0\":{:.15},\"m_e_mev\":{},\"elapsed_s\":{:.3}}}",
            total_dtr, q_pred, q0, M_E_MEV, elapsed_total);

        return;
    }

    // ────────────────────────────────────────────────────────────
    //  CONFINE / KNOTS MODE: knot operator eigenvector channels
    // ────────────────────────────────────────────────────────────
    if use_confine {
        assert_eq!(n % 3, 0, "Quark ordering length must be 3×A for confinement mode");
        let n_nucleons = n / 3;

        let knots = knot_operators();
        eprintln!("  Knot operator mode: {} operators × {} irreps", knots.len(), partitions.len());
        eprintln!("  {} nucleons, {} quarks", n_nucleons, n);
        eprintln!("  Operators: {}", knots.iter().map(|k| k.name).collect::<Vec<_>>().join(", "));

        // For each irrep, compute matrix elements for ALL knot operators
        // Each knot gives a different q-torsion leaf → different channel
        // The LP dual will select optimal weights

        // Structure: per irrep, per knot → (me_par, me_dau, eigenvalue)
        let results: Vec<(usize, usize, usize, Vec<(String, f64, f64, f64, f64)>, f64)> = partitions.par_iter()
            .filter_map(|&(a, b)| {
                let dim = generate_syt(a, b).len();
                if dim > max_dim || dim == 0 { return None; }

                let t0 = Instant::now();

                let mut knot_results: Vec<(String, f64, f64, f64, f64)> = Vec::new();

                for knot in &knots {
                    let (v_knot, lambda) = knot_eigenvector(a, b, knot, n_nucleons, q0, 200, 1e-12);
                    let me_par = garside_matrix_element(a, b, &par_types, &v_knot, q0);
                    let me_dau = garside_matrix_element(a, b, &dau_types, &v_knot, q0);
                    let dme = me_dau - me_par;
                    knot_results.push((knot.name.to_string(), me_par, me_dau, dme, lambda));
                }

                let elapsed = t0.elapsed().as_secs_f64();

                // Print summary for this irrep
                eprintln!("  λ=({},{}): dim={:>6}, {:.1}s", a, b, dim, elapsed);
                for (kname, me_p, me_d, dme, lam) in &knot_results {
                    eprintln!("    {:>12}: λ_K={:.4e}, ⟨v|Δ_p|v⟩={:>+10.4}, ⟨v|Δ_d|v⟩={:>+10.4}, Δme={:>+12.6e}",
                        kname, lam, me_p, me_d, dme);
                }

                Some((a, b, dim, knot_results, elapsed))
            })
            .collect();

        let elapsed_total = t_total.elapsed().as_secs_f64();

        // Per-knot-operator totals across all irreps
        eprintln!("\n  PER-OPERATOR TOTALS (Σ_λ Δme):");
        let knot_names: Vec<&str> = knots.iter().map(|k| k.name).collect();
        let mut knot_totals: Vec<f64> = vec![0.0; knots.len()];
        for (_, _, _, knot_results, _) in &results {
            for (ki, (_, _, _, dme, _)) in knot_results.iter().enumerate() {
                knot_totals[ki] += dme;
            }
        }

        for (ki, name) in knot_names.iter().enumerate() {
            let q_pred = knot_totals[ki].abs() * M_E_MEV;
            eprintln!("    {:>12}: Σ Δme = {:>+12.6e}, Q = {:.6} MeV", name, knot_totals[ki], q_pred);
        }
        eprintln!("  Total: {:.1}s", elapsed_total);

        // JSON output: full per-irrep, per-knot data for LP solver
        print!("{{\"mode\":\"knots\",\"parent\":\"{}\",\"daughter\":\"{}\",\"n\":{},\"n_nucleons\":{},\"n_irreps\":{},\"n_knots\":{}",
            par_str, dau_str, n, n_nucleons, results.len(), knots.len());
        print!(",\"knot_names\":[{}]", knot_names.iter().map(|n| format!("\"{}\"", n)).collect::<Vec<_>>().join(","));

        // Per-knot totals
        print!(",\"knot_totals\":[{}]", knot_totals.iter().map(|t| format!("{:.10e}", t)).collect::<Vec<_>>().join(","));

        // Per-irrep data
        print!(",\"irreps\":[");
        for (ri, (a, b, dim, knot_results, t)) in results.iter().enumerate() {
            if ri > 0 { print!(","); }
            print!("{{\"a\":{},\"b\":{},\"dim\":{},\"time\":{:.3},\"channels\":[", a, b, dim, t);
            for (ki, (kname, me_p, me_d, dme, lam)) in knot_results.iter().enumerate() {
                if ki > 0 { print!(","); }
                print!("{{\"knot\":\"{}\",\"me_par\":{:.10e},\"me_dau\":{:.10e},\"dme\":{:.10e},\"lambda\":{:.10e}}}",
                    kname, me_p, me_d, dme, lam);
            }
            print!("]}}");
        }
        println!("],\"q0\":{:.15},\"m_e_mev\":{},\"elapsed_s\":{:.3}}}", q0, M_E_MEV, elapsed_total);

        return;
    }

    // ────────────────────────────────────────────────────────────
    //  MATRIX MODE (original): O(dim²) per crossing
    // ────────────────────────────────────────────────────────────

    // Memory-aware scheduling: parallel for small irreps, sequential for large
    // Each irrep needs 2 × dim² × 8 bytes of working memory
    let mem_limit: usize = 2 * 1024 * 1024 * 1024; // 2 GB budget
    let dim_threshold = ((mem_limit / 16) as f64).sqrt() as usize; // max dim for parallel

    eprintln!("  Memory budget: {} GB, parallel threshold: dim ≤ {}", mem_limit / (1024*1024*1024), dim_threshold);

    // Split into small (parallel) and large (sequential)
    let mut small_parts: Vec<(usize, usize)> = Vec::new();
    let mut large_parts: Vec<(usize, usize)> = Vec::new();

    for &(a, b) in &partitions {
        let dim = generate_syt(a, b).len();
        if dim > max_dim { continue; }
        if dim <= dim_threshold { small_parts.push((a, b)); }
        else { large_parts.push((a, b)); }
    }

    eprintln!("  {} small irreps (parallel), {} large irreps (sequential)",
        small_parts.len(), large_parts.len());

    // Small irreps in parallel — use pair optimization
    let small_results: Vec<(usize, usize, usize, f64, f64, f64, f64)> = small_parts.par_iter()
        .map(|&(a, b)| {
            let dim = generate_syt(a, b).len();
            let t0 = Instant::now();
            let (tr_par, tr_dau) = garside_trace_pair(a, b, &par_types, &dau_types, q0);
            let dtr = tr_par - tr_dau;
            let elapsed = t0.elapsed().as_secs_f64();
            eprintln!("  λ=({},{}): dim={:>6}, Δtr={:>+14.6e}, {:.1}s", a, b, dim, dtr, elapsed);
            (a, b, dim, tr_par, tr_dau, dtr, elapsed)
        })
        .collect();

    // Large irreps sequentially — use pair optimization
    let mut large_results: Vec<(usize, usize, usize, f64, f64, f64, f64)> = Vec::new();
    for &(a, b) in &large_parts {
        let dim = generate_syt(a, b).len();
        let mem_mb = 3 * dim * dim * 8 / (1024 * 1024); // prefix + par + dau
        eprintln!("  λ=({},{}): dim={:>6} ({} MB, prefix/branch/suffix) ...", a, b, dim, mem_mb);
        let t0 = Instant::now();
        let (tr_par, tr_dau) = garside_trace_pair(a, b, &par_types, &dau_types, q0);
        let dtr = tr_par - tr_dau;
        let elapsed = t0.elapsed().as_secs_f64();
        eprintln!("    Δtr={:>+14.6e}, {:.1}s", dtr, elapsed);
        large_results.push((a, b, dim, tr_par, tr_dau, dtr, elapsed));
    }

    let mut results: Vec<(usize, usize, usize, f64, f64, f64, f64)> = small_results;
    results.extend(large_results);
    results.sort_by_key(|r| r.1); // sort by b (second part of partition)

    let total_dtr: f64 = results.iter().map(|r| r.5).sum();
    let q_pred = total_dtr.abs() * M_E_MEV;
    let elapsed_total = t_total.elapsed().as_secs_f64();

    eprintln!("\n  Σ Δtr = {:+.10e}", total_dtr);
    eprintln!("  Q = |Σ Δtr| × m_e = {:.4} MeV", q_pred);
    eprintln!("  Total: {:.1}s", elapsed_total);

    // JSON output
    print!("{{\"parent\":\"{}\",\"daughter\":\"{}\",\"n\":{},\"n_irreps\":{}", par_str, dau_str, n, results.len());
    print!(",\"irreps\":[");
    for (i, (a, b, dim, tr_p, tr_d, dtr, t)) in results.iter().enumerate() {
        if i > 0 { print!(","); }
        print!("{{\"a\":{},\"b\":{},\"dim\":{},\"tr_par\":{:.10e},\"tr_dau\":{:.10e},\"dtr\":{:.10e},\"time\":{:.3}}}",
            a, b, dim, tr_p, tr_d, dtr, t);
    }
    println!("],\"total_dtr\":{:.10e},\"q_mev\":{:.6},\"q0\":{:.15},\"m_e_mev\":{},\"elapsed_s\":{:.3}}}",
        total_dtr, q_pred, q0, M_E_MEV, elapsed_total);
}
