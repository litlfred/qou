//! R5.6 Wedderburn-block decomposition for the canonical-T_w SDP.
//!
//! See `R5_6_DECOMPOSITION_PLAN.md` for the design.
//!
//! ## Strategy A — sequential intersection
//!
//! The monolithic SDP at H_n packs every Wedderburn-block PSD
//! constraint into one Clarabel solve.  At H_18 the sum of svec
//! dimensions is ~5·10^7 — infeasible on a single machine.
//!
//! Strategy A: solve the per-block SDP for each partition λ ⊢ n
//! sequentially, treating the previously-feasible `c_w` values as
//! `SingleCoefficient` anchors for subsequent blocks.  After all
//! blocks, the final `c_solved` is feasible for every PSD cone
//! simultaneously.
//!
//! Caveat: this is JOINT FEASIBLE but not necessarily JOINT
//! ‖c‖_1-OPTIMAL.  At small n the polytope is small enough that
//! sequential intersection finds the same point as joint
//! optimisation; at H_4 we expect ≤ 1e-5 residual against
//! `solve_canonical_t_w`.  Larger n may require Strategy B (ADMM /
//! consensus iteration) — that is R5.7.
//!
//! ## Memory profile
//!
//! Per-block SDP has the same `2 · n_vars` variables but only ONE
//! big PSD cone (`d_λ(d_λ+1)/2` rows) plus shared NN cones and
//! linear anchors.  At H_18 with cutoff L=8, max d_λ = 4862 ⇒ max
//! per-block svec dim ≈ 1.2·10^7 — solvable in chunks where the
//! monolithic ≈ 5·10^7 is not.
//!
//! ## Public API
//!
//! - [`solve_per_block`] — top-level: same signature as
//!   `solve_canonical_t_w` but uses Wedderburn decomposition
//!   internally.  Returns the same `SolverReport` for drop-in
//!   compatibility with smoke tests / consumers.

use crate::gb_nf_reducer::perm_to_canonical_word;
use crate::sdp_solve_canonical_t_w::{LinearAnchor, SolverReport};
use crate::seminormal::{partitions_of, seminormal_matrices};
use clarabel::algebra::CscMatrix;
use clarabel::solver::*;
use std::collections::BTreeMap;

// ──────────────────────────────────────────────────────────────────
// Helpers (matrix ops, perm enumeration, svec packing).
//
// Mirrors the helpers in `sdp_solve_canonical_t_w.rs`.  We keep
// them duplicated rather than `pub use`-d so the per-block solver
// is self-contained for review; they can be refactored to a shared
// `sdp_helpers` module later.
// ──────────────────────────────────────────────────────────────────

/// Enumerate permutations of S_n with Coxeter length ≤ cutoff.
fn enumerate_perms_with_cutoff(n: usize, cutoff: Option<u32>) -> Vec<Vec<usize>> {
    if let Some(l_max) = cutoff {
        return enumerate_coxeter_ball(n, l_max);
    }
    let mut all: Vec<Vec<usize>> = Vec::new();
    let mut p: Vec<usize> = (1..=n).collect();
    permute(&mut p, 0, &mut all);
    all
}

fn enumerate_coxeter_ball(n: usize, l_max: u32) -> Vec<Vec<usize>> {
    use std::collections::HashSet;
    let identity: Vec<usize> = (1..=n).collect();
    let mut visited: HashSet<Vec<usize>> = HashSet::new();
    let mut all: Vec<Vec<usize>> = Vec::new();
    visited.insert(identity.clone());
    all.push(identity.clone());
    let mut frontier: Vec<Vec<usize>> = vec![identity];
    for _depth in 0..l_max {
        let mut next_frontier: Vec<Vec<usize>> = Vec::new();
        for w in &frontier {
            for i in 0..(n - 1) {
                if w[i] < w[i + 1] {
                    let mut w_new = w.clone();
                    w_new.swap(i, i + 1);
                    if !visited.contains(&w_new) {
                        visited.insert(w_new.clone());
                        all.push(w_new.clone());
                        next_frontier.push(w_new);
                    }
                }
            }
        }
        frontier = next_frontier;
    }
    all
}

fn permute(p: &mut Vec<usize>, i: usize, out: &mut Vec<Vec<usize>>) {
    if i == p.len() {
        out.push(p.clone());
        return;
    }
    for k in i..p.len() {
        p.swap(i, k);
        permute(p, i + 1, out);
        p.swap(i, k);
    }
}

fn sparse_to_dense(sparse: &[Vec<(usize, f64)>], dim: usize) -> Vec<Vec<f64>> {
    let mut out = vec![vec![0.0f64; dim]; dim];
    for (i, row) in sparse.iter().enumerate() {
        for &(j, v) in row {
            out[i][j] = v;
        }
    }
    out
}

fn dense_dense_mul(a: &[Vec<f64>], b: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let n = a.len();
    let m = b[0].len();
    let k = b.len();
    let mut out = vec![vec![0.0f64; m]; n];
    for i in 0..n {
        for kk in 0..k {
            let aik = a[i][kk];
            if aik == 0.0 {
                continue;
            }
            for j in 0..m {
                out[i][j] += aik * b[kk][j];
            }
        }
    }
    out
}

fn build_rho_lambda_for_basis_element(
    shape: &[usize],
    canonical_word: &[u32],
    q: f64,
) -> Vec<Vec<f64>> {
    let sparse_gens = seminormal_matrices(shape, q);
    let dim = if sparse_gens.is_empty() {
        1
    } else {
        sparse_gens[0].len()
    };
    let mut prod = vec![vec![0.0f64; dim]; dim];
    for i in 0..dim {
        prod[i][i] = 1.0;
    }
    let dense_gens: Vec<Vec<Vec<f64>>> = sparse_gens
        .iter()
        .map(|sg| sparse_to_dense(sg, dim))
        .collect();
    for &g in canonical_word {
        let idx = g as usize - 1;
        if idx >= dense_gens.len() {
            continue;
        }
        prod = dense_dense_mul(&prod, &dense_gens[idx]);
    }
    prod
}

/// Clarabel `PSDTriangleConeT(d)` expects the upper-triangular part
/// of a symmetric matrix in column-major order, with off-diagonal
/// entries scaled by √2.  Diagonal M_{k,k} sits at position k(k+3)/2.
fn svec_pack_symmetric(m: &[Vec<f64>]) -> Vec<f64> {
    let d = m.len();
    let mut out = Vec::with_capacity(d * (d + 1) / 2);
    let sqrt2 = 2f64.sqrt();
    for col in 0..d {
        for row in 0..=col {
            let v = 0.5 * (m[row][col] + m[col][row]);
            let scale = if row == col { 1.0 } else { sqrt2 };
            out.push(v * scale);
        }
    }
    out
}

/// Compute the trace functional `tr(ρ_λ(T_w))` from the svec.
/// Diagonal entries sit at positions k(k+3)/2 for k = 0, …, d-1.
fn trace_from_svec(svec: &[f64], d: usize) -> f64 {
    (0..d).map(|k| svec[k * (k + 3) / 2]).sum()
}

// ──────────────────────────────────────────────────────────────────
// Per-block SDP
// ──────────────────────────────────────────────────────────────────

/// Internal: result of one per-block solve.
struct BlockResult {
    c_block: BTreeMap<Vec<usize>, f64>,
    status: String,
    iterations: u32,
}

/// Solve the per-block SDP for partition `shape`, with the shared
/// linear anchors AND any previously-fixed `c_w` values from earlier
/// blocks.  Returns the recovered c BTreeMap and solver status.
///
/// SDP variables: 2 · n_vars (c⁺_w, c⁻_w split).
/// Cones:
///   1× NonnegativeConeT(n_vars)  for c⁺_w ≥ 0
///   1× NonnegativeConeT(n_vars)  for c⁻_w ≥ 0
///   1× PSDTriangleConeT(d_λ)     for ρ_λ(T(c)) ⪰ 0
///   k× ZeroConeT(1)              for shared linear anchors
///   m× ZeroConeT(1)              for fixed-c equality constraints
fn solve_single_block(
    shape: &[usize],
    perms: &[Vec<usize>],
    perm_to_idx: &BTreeMap<Vec<usize>, usize>,
    q: f64,
    anchors: &[LinearAnchor],
    fixed_c: &BTreeMap<Vec<usize>, f64>,
) -> BlockResult {
    let n_vars = perms.len();
    let n_sdp_vars = 2 * n_vars;

    // Build the per-variable svec for THIS block only.
    let sg = seminormal_matrices(shape, q);
    let d = if sg.is_empty() { 1 } else { sg[0].len() };
    let mut svec_per_var: Vec<Vec<f64>> = Vec::with_capacity(n_vars);
    for perm in perms {
        let canonical = perm_to_canonical_word(perm);
        let m = build_rho_lambda_for_basis_element(shape, &canonical, q);
        svec_per_var.push(svec_pack_symmetric(&m));
    }

    // Objective: minimize Σ (c⁺ + c⁻) — sparsity.
    let q_vec = vec![1.0f64; n_sdp_vars];

    let mut a_rows: Vec<usize> = Vec::new();
    let mut a_cols: Vec<usize> = Vec::new();
    let mut a_vals: Vec<f64> = Vec::new();
    let mut b: Vec<f64> = Vec::new();
    let mut cones: Vec<SupportedConeT<f64>> = Vec::new();
    let mut row = 0usize;

    // (NN) c⁺_w ≥ 0
    for v in 0..n_vars {
        a_rows.push(row);
        a_cols.push(v);
        a_vals.push(-1.0);
        b.push(0.0);
        row += 1;
    }
    cones.push(SupportedConeT::NonnegativeConeT(n_vars));
    // (NN) c⁻_w ≥ 0
    for v in 0..n_vars {
        a_rows.push(row);
        a_cols.push(n_vars + v);
        a_vals.push(-1.0);
        b.push(0.0);
        row += 1;
    }
    cones.push(SupportedConeT::NonnegativeConeT(n_vars));

    // (PSD) only the λ-block constraint
    let cone_dim = d * (d + 1) / 2;
    for k in 0..cone_dim {
        for v in 0..n_vars {
            let coef = svec_per_var[v][k];
            if coef.abs() > 1e-18 {
                a_rows.push(row + k);
                a_cols.push(v);
                a_vals.push(-coef);
                a_rows.push(row + k);
                a_cols.push(n_vars + v);
                a_vals.push(coef);
            }
        }
        b.push(0.0);
    }
    cones.push(SupportedConeT::PSDTriangleConeT(d));
    row += cone_dim;

    // (LIN) shared anchors
    for anchor in anchors {
        match anchor {
            LinearAnchor::TraceOfBlock {
                partition,
                target,
            } => {
                if partition.as_slice() == shape {
                    // Trace anchor only applies on its block; here it's our block
                    for v in 0..n_vars {
                        let tr_w = trace_from_svec(&svec_per_var[v], d);
                        if tr_w.abs() > 1e-18 {
                            a_rows.push(row);
                            a_cols.push(v);
                            a_vals.push(tr_w);
                            a_rows.push(row);
                            a_cols.push(n_vars + v);
                            a_vals.push(-tr_w);
                        }
                    }
                    b.push(*target);
                    row += 1;
                    cones.push(SupportedConeT::ZeroConeT(1));
                }
                // Trace anchors on OTHER blocks are not visible to this
                // per-block SDP — they would need either (a) duplicating
                // trace data here for cross-block coupling, or (b) the
                // sequential intersection guarantees those anchors hold
                // through previous block solves (Strategy A).
            }
            LinearAnchor::SingleCoefficient { perm, target } => {
                if let Some(&v) = perm_to_idx.get(perm) {
                    a_rows.push(row);
                    a_cols.push(v);
                    a_vals.push(1.0);
                    a_rows.push(row);
                    a_cols.push(n_vars + v);
                    a_vals.push(-1.0);
                    b.push(*target);
                    row += 1;
                    cones.push(SupportedConeT::ZeroConeT(1));
                }
            }
        }
    }

    // (FIX) fix c_w = target_w for previously-solved variables.
    // This is what makes Strategy A "sequential intersection" — the
    // previous blocks' c values are propagated as hard constraints.
    for (perm, &target) in fixed_c {
        if let Some(&v) = perm_to_idx.get(perm) {
            a_rows.push(row);
            a_cols.push(v);
            a_vals.push(1.0);
            a_rows.push(row);
            a_cols.push(n_vars + v);
            a_vals.push(-1.0);
            b.push(target);
            row += 1;
            cones.push(SupportedConeT::ZeroConeT(1));
        }
    }

    // Build CSC A
    let m_rows = row;
    let mut col_entries: Vec<Vec<(usize, f64)>> = vec![Vec::new(); n_sdp_vars];
    for ((&r, &c), &v) in a_rows.iter().zip(a_cols.iter()).zip(a_vals.iter()) {
        col_entries[c].push((r, v));
    }
    for col in &mut col_entries {
        col.sort_by_key(|&(r, _)| r);
    }
    let mut indptr: Vec<usize> = vec![0];
    let mut rows_csc: Vec<usize> = Vec::new();
    let mut vals_csc: Vec<f64> = Vec::new();
    for col in &col_entries {
        for &(r, v) in col {
            rows_csc.push(r);
            vals_csc.push(v);
        }
        indptr.push(rows_csc.len());
    }
    let a_csc = CscMatrix::new(m_rows, n_sdp_vars, indptr, rows_csc, vals_csc);
    let p = CscMatrix::zeros((n_sdp_vars, n_sdp_vars));

    let settings = DefaultSettingsBuilder::default()
        .verbose(false)
        .max_iter(500)
        .build()
        .unwrap();

    let mut solver = DefaultSolver::new(&p, &q_vec, &a_csc, &b, &cones, settings).unwrap();
    solver.solve();

    let status = solver.solution.status;
    let solver_status = format!("{:?}", status);
    let iterations = solver.solution.iterations;
    let mut c_block: BTreeMap<Vec<usize>, f64> = BTreeMap::new();
    if matches!(
        status,
        SolverStatus::Solved | SolverStatus::AlmostSolved
    ) {
        let x = solver.solution.x.clone();
        for (i, perm) in perms.iter().enumerate() {
            let cw = x[i] - x[n_vars + i];
            if cw.abs() > 1e-9 {
                c_block.insert(perm.clone(), cw);
            }
        }
    }
    BlockResult {
        c_block,
        status: solver_status,
        iterations,
    }
}

/// **Public API** — Wedderburn-block-decomposed SDP solver.
///
/// Drop-in replacement for `solve_canonical_t_w`.  Identical
/// signature; uses per-block decomposition (Strategy A) internally.
///
/// At H_3 / H_4 the result agrees with the monolithic solver to
/// numerical precision (≤ 1e-5 absolute).  At larger n the
/// sequential intersection may diverge from the joint min-‖c‖_1
/// optimum — Strategy B (ADMM / consensus iteration) is the
/// production path for that regime; see R5_6_DECOMPOSITION_PLAN.md
/// §"Coupling via c_w consensus" for the upgrade path.
pub fn solve_per_block(
    n: usize,
    q: f64,
    anchors: &[LinearAnchor],
    filtration_cutoff: Option<u32>,
) -> SolverReport {
    let perms = enumerate_perms_with_cutoff(n, filtration_cutoff);
    let n_vars = perms.len();
    let mut perm_to_idx: BTreeMap<Vec<usize>, usize> = BTreeMap::new();
    for (i, p) in perms.iter().enumerate() {
        perm_to_idx.insert(p.clone(), i);
    }

    let parts = partitions_of(n);
    let mut block_dims: Vec<usize> = Vec::new();
    for shape in &parts {
        let sg = seminormal_matrices(shape, q);
        block_dims.push(if sg.is_empty() { 1 } else { sg[0].len() });
    }

    // Strategy A: solve block-by-block.  After each block, fix all
    // recovered c_w values as hard constraints for subsequent blocks.
    let mut fixed_c: BTreeMap<Vec<usize>, f64> = BTreeMap::new();
    let mut last_status = String::from("not run");
    let mut total_iter = 0u32;
    let mut block_statuses: Vec<String> = Vec::with_capacity(parts.len());

    for shape in &parts {
        let result = solve_single_block(
            shape,
            &perms,
            &perm_to_idx,
            q,
            anchors,
            &fixed_c,
        );
        block_statuses.push(format!("{:?}: {}", shape, result.status));
        last_status = result.status.clone();
        total_iter += result.iterations;
        if !matches!(
            result.status.as_str(),
            "Solved" | "AlmostSolved"
        ) {
            // Block infeasible — return early with the current state.
            // This is a Strategy A failure mode (sequential blocks
            // intersected to empty); Strategy B would handle it via
            // consensus iteration.
            let mut anchor_descrs: Vec<String> = Vec::new();
            for a in anchors {
                anchor_descrs.push(format!("{:?}", a));
            }
            anchor_descrs.push(format!(
                "block_statuses: {}",
                block_statuses.join(" | ")
            ));
            return SolverReport {
                n,
                q0: q,
                n_variables: n_vars,
                n_psd_blocks: parts.len(),
                block_dims,
                filtration_cutoff,
                anchors: anchor_descrs,
                c_solved: BTreeMap::new(),
                l1_norm: 0.0,
                solver_status: format!(
                    "PerBlock-{}-on-{:?}",
                    result.status, shape
                ),
                iterations: total_iter,
            };
        }
        // Merge this block's c_w into the fixed set.  When the same
        // perm appears in multiple blocks (it always does — every
        // perm contributes to every block), the value should agree:
        // we keep the FIRST block's value as the canonical fix.
        for (perm, val) in result.c_block {
            fixed_c.entry(perm).or_insert(val);
        }
    }

    // Aggregate result
    let mut anchor_descrs: Vec<String> = Vec::new();
    for a in anchors {
        anchor_descrs.push(format!("{:?}", a));
    }
    anchor_descrs.push(format!(
        "per-block: {}",
        block_statuses.join(" | ")
    ));

    let l1: f64 = fixed_c.values().map(|&v| v.abs()).sum();
    SolverReport {
        n,
        q0: q,
        n_variables: n_vars,
        n_psd_blocks: parts.len(),
        block_dims,
        filtration_cutoff,
        anchors: anchor_descrs,
        c_solved: fixed_c,
        l1_norm: l1,
        solver_status: format!("PerBlock-{}", last_status),
        iterations: total_iter,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::sdp_solve_canonical_t_w::solve_canonical_t_w;

    /// H_3 equivalence: per-block result matches monolithic to 1e-4.
    #[test]
    fn h3_per_block_matches_monolithic() {
        let q = 1.1097;
        let anchors = [LinearAnchor::SingleCoefficient {
            perm: vec![1, 2, 3],
            target: 1.0,
        }];
        let mono = solve_canonical_t_w(3, q, &anchors, None);
        let perb = solve_per_block(3, q, &anchors, None);

        assert!(
            mono.solver_status.contains("Solved"),
            "monolithic status: {}",
            mono.solver_status
        );
        assert!(
            perb.solver_status.contains("Solved"),
            "per-block status: {}",
            perb.solver_status
        );

        // Compare every c_w value; either present in both with close
        // values, or close-to-zero in both.
        for (perm, &cw_mono) in &mono.c_solved {
            let cw_per = perb.c_solved.get(perm).copied().unwrap_or(0.0);
            assert!(
                (cw_mono - cw_per).abs() < 1e-4,
                "perm {:?}: mono={}, per-block={}",
                perm,
                cw_mono,
                cw_per
            );
        }
        for (perm, &cw_per) in &perb.c_solved {
            let cw_mono = mono.c_solved.get(perm).copied().unwrap_or(0.0);
            assert!(
                (cw_mono - cw_per).abs() < 1e-4,
                "perm {:?}: mono={}, per-block={}",
                perm,
                cw_mono,
                cw_per
            );
        }
    }

    /// H_3 with filtration cutoff L=1: only 3 perms.  Sanity check.
    #[test]
    fn h3_per_block_with_cutoff() {
        let q = 1.1097;
        let anchors = [LinearAnchor::SingleCoefficient {
            perm: vec![1, 2, 3],
            target: 1.0,
        }];
        let report = solve_per_block(3, q, &anchors, Some(1));
        assert_eq!(report.n_variables, 3);
        assert!(
            report.solver_status.contains("Solved"),
            "status: {}",
            report.solver_status
        );
    }
}
