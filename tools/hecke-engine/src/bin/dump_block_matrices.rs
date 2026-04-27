//! Dump per-Wedderburn-block ρ_λ(T_w) matrices for an atom's braid
//! word at q_0. Lets us audit the d_λ ≥ 4 sign-convention question
//! flagged in `docs/audits/h3-alpha-star-investigation.md` (the
//! ³H/8_11 anomaly).
//!
//! Usage:
//!   cargo run --release --bin dump-block-matrices -- --atom tritium-3H
//!   cargo run --release --bin dump-block-matrices -- --atom proton
//!
//! Atoms (registry below):
//!   proton       — Borromean σ_1 σ_2^{-1} σ_1 σ_2^{-1} on B_3
//!   neutron      — Borromean σ_1 σ_2^{-1} σ_1 σ_2^{-1} on B_3
//!   helium3-3He  — Borromean σ_1^{-1} σ_2 (×3) on B_3
//!   tritium-3H   — 14-letter word on B_5 (see joint-tower-sdp-rust witness)
//!
//! Output: pretty-printed JSON to stdout, one block per partition λ.

use hecke_engine::seminormal::{partitions_of, seminormal_matrices};

const Q_0: f64 = 1.1099785955541806;

/// Sparse-times-dense matmul. `sparse[i]` is `Vec<(j, val)>` for row i.
fn sparse_to_dense(sparse: &[Vec<(usize, f64)>], dim: usize) -> Vec<Vec<f64>> {
    let mut out = vec![vec![0.0f64; dim]; dim];
    for (i, row) in sparse.iter().enumerate() {
        for &(j, v) in row {
            out[i][j] = v;
        }
    }
    out
}

fn invert_matrix(m: &[Vec<f64>], h: f64) -> Vec<Vec<f64>> {
    // Hecke quadratic: σ^{-1} = σ - h
    m.iter()
        .enumerate()
        .map(|(i, row)| {
            row.iter()
                .enumerate()
                .map(|(j, &v)| if i == j { v - h } else { v })
                .collect()
        })
        .collect()
}

fn dense_dense_mul(a: &[Vec<f64>], b: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let n = a.len();
    let mut out = vec![vec![0.0f64; n]; n];
    for i in 0..n {
        for k in 0..n {
            let aik = a[i][k];
            if aik == 0.0 {
                continue;
            }
            for j in 0..n {
                out[i][j] += aik * b[k][j];
            }
        }
    }
    out
}

fn build_block_matrix(
    n_strands: usize,
    braid_word: &[i32],
    shape: &[usize],
    q: f64,
) -> Vec<Vec<f64>> {
    let h = q - 1.0 / q;
    let sparse_gens = seminormal_matrices(shape, q);
    let dim = if sparse_gens.is_empty() {
        1
    } else {
        sparse_gens[0].len()
    };
    let dense_gens: Vec<Vec<Vec<f64>>> = sparse_gens
        .iter()
        .map(|sg| sparse_to_dense(sg, dim))
        .collect();
    let dense_inv_gens: Vec<Vec<Vec<f64>>> = dense_gens
        .iter()
        .map(|d| invert_matrix(d, h))
        .collect();

    let mut prod = vec![vec![0.0f64; dim]; dim];
    for i in 0..dim {
        prod[i][i] = 1.0;
    }
    let _ = n_strands;
    for &gen in braid_word {
        let idx = gen.unsigned_abs() as usize - 1;
        if idx >= dense_gens.len() {
            continue;
        }
        let g = if gen > 0 {
            &dense_gens[idx]
        } else {
            &dense_inv_gens[idx]
        };
        prod = dense_dense_mul(&prod, g);
    }
    prod
}

fn registry(name: &str) -> Option<(usize, Vec<i32>)> {
    match name {
        "proton" | "neutron" => {
            // Borromean: σ_1 σ_2^{-1} σ_1 σ_2^{-1} (positive σ_1 convention)
            Some((3, vec![1, -2, 1, -2]))
        }
        "helium3-3He" | "3He" => {
            // L_6a4 alternating: σ_1^{-1} σ_2 σ_1^{-1} σ_2 σ_1^{-1} σ_2
            Some((3, vec![-1, 2, -1, 2, -1, 2]))
        }
        "tritium-3H" | "3H" => {
            // 14-letter word from joint-tower-sdp-rust.witness.json
            Some((5, vec![-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2]))
        }
        _ => None,
    }
}

fn print_matrix(prefix: &str, m: &[Vec<f64>]) {
    for (i, row) in m.iter().enumerate() {
        print!("{prefix}row {i}: [");
        for (j, &v) in row.iter().enumerate() {
            if j > 0 {
                print!(", ");
            }
            print!("{:>10.6}", v);
        }
        println!("]");
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let atom_name = args
        .iter()
        .position(|a| a == "--atom")
        .and_then(|i| args.get(i + 1))
        .map(String::as_str)
        .unwrap_or("tritium-3H");

    let (n_strands, braid_word) = match registry(atom_name) {
        Some(r) => r,
        None => {
            eprintln!(
                "Unknown atom '{atom_name}'. Try: proton, neutron, helium3-3He, tritium-3H"
            );
            std::process::exit(2);
        }
    };

    println!("# atom: {atom_name}");
    println!("# n_strands: {n_strands}");
    println!("# q_0: {Q_0}");
    println!("# braid_word: {braid_word:?}");
    println!();

    for shape in partitions_of(n_strands) {
        let m = build_block_matrix(n_strands, &braid_word, &shape, Q_0);
        let dim = m.len();
        println!("## λ = {shape:?},  d_λ = {dim}");
        if dim > 8 {
            println!("(matrix omitted — d_λ > 8; use --dim-limit override)");
        } else {
            print_matrix("  ", &m);
        }
        // Compute trace and Frobenius norm for quick audit.
        let trace: f64 = (0..dim).map(|i| m[i][i]).sum();
        let frob: f64 = m
            .iter()
            .flat_map(|r| r.iter())
            .map(|v| v * v)
            .sum::<f64>()
            .sqrt();
        println!("  trace = {trace:.6}, Frobenius norm = {frob:.6}");
        // Min/max diagonal.
        let diag_min = (0..dim).map(|i| m[i][i]).fold(f64::INFINITY, f64::min);
        let diag_max = (0..dim)
            .map(|i| m[i][i])
            .fold(f64::NEG_INFINITY, f64::max);
        println!("  diag min = {diag_min:.6}, diag max = {diag_max:.6}");
        println!();
    }
}
