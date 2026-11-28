//! Exact-rational `χ^λ` via the **asymmetric** seminormal gauge.
//!
//! # Why this module exists
//!
//! [`crate::seminormal::chi_q_atomic`] is `f64`, and its MPFR sibling is
//! arbitrary-precision but still *numeric*: both evaluate at one `q`. Neither
//! can produce the exact rational needed to reconstruct a character as a
//! Laurent polynomial.
//!
//! The obstacle was never the coefficient type. Hoefsmit's **symmetric**
//! seminormal form puts `b = sqrt(a·a' + 1)` off-diagonal
//! ([`crate::seminormal`], the `b_sq.abs().sqrt()` in
//! `seminormal_block_generators`), and that square root is irrational for
//! almost every `q` — so no rational or Laurent coefficient type can hold the
//! intermediate matrices, however wide.
//!
//! **The square root is a gauge artifact, not intrinsic.** Conjugating the
//! 2×2 block by `diag(1, b)` gives
//!
//! ```text
//!     [[a, b],[b, a']]   ->   [[a, b²],[1, a']]
//! ```
//!
//! which is *rational in `q`*, and conjugation leaves every trace unchanged.
//! With the root gone, and with the QOU interface weights themselves rational
//! in `q`, an entire atomic braid evaluates in exact `BigRational` arithmetic:
//! no square roots, no fraction field, no floating point.
//!
//! # Validation
//!
//! The gauge was checked before this module was written, in
//! `computations/probes/exact_rational_chi_gauge_probe.py`:
//!
//! * Hecke quadratic, braid, far-commutation and **equal traces** against the
//!   symmetric form, on all 15 shapes for `n = 3, 4, 5`.
//! * Every one of the deuteron's 11 committed symbolic characters reproduced
//!   exactly, at three independent rational `q`.
//!
//! # Scope
//!
//! This evaluates `χ^λ` exactly **at a rational `q`**. Recovering the Laurent
//! polynomial from such evaluations (interpolation) is a separate step and is
//! not done here.

use num_bigint::BigInt;
use num_rational::BigRational;
use num_traits::{One, Zero};

use crate::seminormal::standard_young_tableaux;

/// Diagonal content `col - row` of a Young cell.
fn content(row: usize, col: usize) -> i32 {
    col as i32 - row as i32
}

/// `q^e` for a signed exponent, by repeated multiplication.
///
/// Deliberately not `num_traits::Pow`: the exponent is small (bounded by the
/// content spread of the shape) and an explicit loop keeps the negative branch
/// obvious.
fn ratio_pow(q: &BigRational, e: i32) -> BigRational {
    let mut acc = BigRational::one();
    for _ in 0..e.unsigned_abs() {
        acc *= q;
    }
    if e < 0 {
        acc.recip()
    } else {
        acc
    }
}

/// One generator's action on a 1- or 2-dimensional invariant subspace, in the
/// asymmetric gauge. `b2` is `b²`; the square root is never taken.
#[derive(Debug, Clone)]
pub enum ExactBlock {
    /// `σ_k` acts diagonally: `e_i ↦ a · e_i`.
    One { i: usize, a: BigRational },
    /// `σ_k` acts as `[[a, b²], [1, a']]` on `span(e_i, e_j)`, `i < j`.
    Two {
        i: usize,
        j: usize,
        a: BigRational,
        ap: BigRational,
        b2: BigRational,
    },
}

/// Asymmetric-gauge generators for `shape` at an exact rational `q`.
///
/// Returns `(dim, blocks)` with one `Vec<ExactBlock>` per generator
/// `σ_1 … σ_{n-1}`, mirroring [`crate::seminormal::seminormal_block_generators`]
/// but over `BigRational` and without the square root.
pub fn seminormal_blocks_exact(
    shape: &[usize],
    q: &BigRational,
) -> (usize, Vec<Vec<ExactBlock>>) {
    let n: usize = shape.iter().sum();
    let syts = standard_young_tableaux(shape);
    let dim = syts.len();
    if n == 0 || dim == 0 {
        return (dim, Vec::new());
    }

    let mut index = std::collections::HashMap::with_capacity(dim);
    for (i, t) in syts.iter().enumerate() {
        index.insert(t.clone(), i);
    }

    let one = BigRational::one();
    let h = q - q.recip(); // h = q - q^{-1}

    let mut all_blocks = Vec::with_capacity(n.saturating_sub(1));
    for k in 1..n {
        let mut blocks = Vec::with_capacity(dim);
        let mut processed = vec![false; dim];

        for i in 0..dim {
            if processed[i] {
                continue;
            }
            let cell_k = syts[i][k - 1];
            let cell_k1 = syts[i][k];
            let rho = content(cell_k1.0, cell_k1.1) - content(cell_k.0, cell_k.1);

            // a = h / (1 - q^{-2ρ})
            let a = &h / (&one - ratio_pow(q, -2 * rho));

            let mut swapped = syts[i].clone();
            swapped[k - 1] = cell_k1;
            swapped[k] = cell_k;
            let partner = index.get(&swapped).copied().filter(|&j| j != i);

            match partner {
                None => {
                    blocks.push(ExactBlock::One { i, a });
                    processed[i] = true;
                }
                Some(j) => {
                    // a' = h / (1 - q^{2ρ});  b² = a·a' + 1  (never sqrt)
                    let ap = &h / (&one - ratio_pow(q, 2 * rho));
                    let b2 = &a * &ap + &one;
                    let (lo, hi) = (i.min(j), i.max(j));
                    let (aa, aap) = if i < j {
                        (a.clone(), ap.clone())
                    } else {
                        (ap.clone(), a.clone())
                    };
                    blocks.push(ExactBlock::Two {
                        i: lo,
                        j: hi,
                        a: aa,
                        ap: aap,
                        b2,
                    });
                    processed[i] = true;
                    processed[j] = true;
                }
            }
        }
        all_blocks.push(blocks);
    }

    (dim, all_blocks)
}

/// Apply one Hecke factor `c·σ_g + d·I` to `v` on the left, exactly.
fn apply_factor_exact(
    v: &mut Vec<BigRational>,
    blocks: &[ExactBlock],
    c: &BigRational,
    d: &BigRational,
) {
    let src = v.clone();
    for b in blocks {
        match b {
            ExactBlock::One { i, a } => {
                v[*i] = c * a * &src[*i] + d * &src[*i];
            }
            ExactBlock::Two { i, j, a, ap, b2 } => {
                v[*i] = c * (a * &src[*i] + b2 * &src[*j]) + d * &src[*i];
                v[*j] = c * (&src[*i] + ap * &src[*j]) + d * &src[*j];
            }
        }
    }
}

/// `χ^λ( Π_i (c_i·σ_{g_i} + d_i·I) )` exactly, at rational `q`.
///
/// `factors` are `(c, d, gen_1based)` applied left-to-right — factor 0 is
/// rightmost in the matrix product, matching
/// [`crate::seminormal::chi_q_atomic`].
///
/// # Panics
/// If a generator index is out of range for the shape.
pub fn chi_q_atomic_exact(
    shape: &[usize],
    factors: &[(BigRational, BigRational, u32)],
    q: &BigRational,
) -> BigRational {
    let n: usize = shape.iter().sum();
    if n == 0 {
        return BigRational::one();
    }
    let (dim, all_blocks) = seminormal_blocks_exact(shape, q);
    if dim == 0 {
        return BigRational::zero();
    }

    for &(_, _, gen) in factors {
        assert!(
            gen != 0 && (gen as usize) <= all_blocks.len(),
            "chi_q_atomic_exact: invalid generator index {} for n = {} (valid 1..={})",
            gen,
            n,
            all_blocks.len()
        );
    }

    let mut trace = BigRational::zero();
    for e in 0..dim {
        let mut v = vec![BigRational::zero(); dim];
        v[e] = BigRational::one();
        for (c, d, gen) in factors.iter().rev() {
            apply_factor_exact(&mut v, &all_blocks[*gen as usize - 1], c, d);
        }
        trace += &v[e];
    }
    trace
}

/// Convenience: build a `BigRational` from an `i64` numerator/denominator.
pub fn ratio(num: i64, den: i64) -> BigRational {
    BigRational::new(BigInt::from(num), BigInt::from(den))
}

#[cfg(test)]
mod tests {
    use super::*;

    /// The asymmetric gauge must still be a representation: the Hecke
    /// quadratic and the braid relation hold exactly, with no square root
    /// anywhere. This is the property the whole module rests on.
    #[test]
    fn asymmetric_gauge_satisfies_hecke_and_braid() {
        let q = ratio(3, 2);
        let one = BigRational::one();
        let qi = q.recip();

        for shape in [vec![3usize], vec![2, 1], vec![1, 1, 1], vec![3, 1], vec![2, 2]] {
            let (dim, blocks) = seminormal_blocks_exact(&shape, &q);
            if dim == 0 || blocks.is_empty() {
                continue;
            }
            // Dense matrices from the block form.
            let dense = |bs: &[ExactBlock]| -> Vec<Vec<BigRational>> {
                let mut m = vec![vec![BigRational::zero(); dim]; dim];
                for b in bs {
                    match b {
                        ExactBlock::One { i, a } => m[*i][*i] = a.clone(),
                        ExactBlock::Two { i, j, a, ap, b2 } => {
                            m[*i][*i] = a.clone();
                            m[*j][*j] = ap.clone();
                            m[*i][*j] = b2.clone();
                            m[*j][*i] = one.clone();
                        }
                    }
                }
                m
            };
            let mul = |x: &Vec<Vec<BigRational>>, y: &Vec<Vec<BigRational>>| {
                let mut r = vec![vec![BigRational::zero(); dim]; dim];
                for i in 0..dim {
                    for k in 0..dim {
                        if x[i][k].is_zero() {
                            continue;
                        }
                        for j in 0..dim {
                            r[i][j] += &x[i][k] * &y[k][j];
                        }
                    }
                }
                r
            };

            let mats: Vec<_> = blocks.iter().map(|b| dense(b)).collect();

            // (σ - q)(σ + q^{-1}) = 0
            for m in &mats {
                let mut lhs = m.clone();
                let mut rhs = m.clone();
                for i in 0..dim {
                    lhs[i][i] -= &q;
                    rhs[i][i] += &qi;
                }
                let p = mul(&lhs, &rhs);
                for row in &p {
                    for x in row {
                        assert!(x.is_zero(), "Hecke quadratic failed for {:?}", shape);
                    }
                }
            }

            // braid: σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}
            for i in 0..mats.len().saturating_sub(1) {
                let l = mul(&mul(&mats[i], &mats[i + 1]), &mats[i]);
                let r = mul(&mul(&mats[i + 1], &mats[i]), &mats[i + 1]);
                for a in 0..dim {
                    for b in 0..dim {
                        assert_eq!(l[a][b], r[a][b], "braid failed for {:?}", shape);
                    }
                }
            }
        }
    }

    /// `χ` of the identity word is the dimension — a non-vacuity check that
    /// the trace loop actually sums the diagonal.
    #[test]
    fn chi_of_empty_product_is_dimension() {
        let q = ratio(2, 1);
        for shape in [vec![3usize], vec![2, 1], vec![2, 2]] {
            let (dim, _) = seminormal_blocks_exact(&shape, &q);
            let chi = chi_q_atomic_exact(&shape, &[], &q);
            assert_eq!(chi, BigRational::from(BigInt::from(dim as i64)));
        }
    }
}

#[cfg(test)]
mod a3_bench {
    //! Cost measurement for the A = 3 exact-rational route (bean `qou-lrnd`).
    //!
    //! Run with `cargo test --release --lib a3_bench -- --ignored --nocapture`.
    use super::*;
    use std::time::Instant;

    /// All partitions of `n`, weakly decreasing.
    fn partitions(n: usize) -> Vec<Vec<usize>> {
        fn go(n: usize, max: usize, cur: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
            if n == 0 {
                out.push(cur.clone());
                return;
            }
            for part in (1..=max.min(n)).rev() {
                cur.push(part);
                go(n - part, part, cur, out);
                cur.pop();
            }
        }
        let mut out = Vec::new();
        go(n, n, &mut Vec::new(), &mut out);
        out
    }

    /// The A = 3 (Z=2, N=1) canonical crossing list, transcribed from
    /// `canonical_braid_crossings.atom_canonical_crossings(2, 1, True)`.
    /// `(gen0, kind)` — gen is 0-based as in the Python.
    const A3_CROSSINGS: &[(u32, &str)] = &[
        (0, "sigma"),
        (0, "sigma"),
        (0, "sigma"),
        (0, "sigma"),
        (0, "averaged"),
        (0, "sigma"),
        (0, "sigma"),
        (1, "sigma_inv"),
        (1, "sigma_inv"),
        (1, "sigma_inv"),
        (1, "averaged"),
        (2, "sigma"),
        (3, "sigma"),
        (3, "sigma"),
        (3, "sigma"),
        (3, "sigma"),
        (3, "averaged"),
        (3, "sigma"),
        (3, "sigma"),
        (4, "sigma_inv"),
        (4, "sigma_inv"),
        (4, "sigma_inv"),
        (4, "averaged"),
        (5, "averaged_weighted"),
        (6, "sigma"),
        (6, "sigma"),
        (6, "sigma"),
        (6, "averaged"),
        (6, "averaged"),
        (6, "sigma"),
        (6, "sigma"),
        (7, "sigma_inv"),
        (7, "sigma_inv"),
        (7, "sigma_inv"),
        (7, "sigma_inv"),
    ];

    fn build_factors(q: &BigRational) -> Vec<(BigRational, BigRational, u32)> {
        let one = BigRational::one();
        let h = q.clone() - one.clone() / q.clone();
        let qm1 = q.clone() - one.clone();
        let qi = one.clone() / q.clone();
        let qi4 = qi.clone() * qi.clone() * qi.clone() * qi.clone();
        let three = BigRational::from_integer(3.into());
        let delta = qm1.clone() * qm1 * (one.clone() - qi4) / three;
        let half = BigRational::new(1.into(), 2.into());
        let quarter = BigRational::new(1.into(), 4.into());

        A3_CROSSINGS
            .iter()
            .map(|&(g, kind)| {
                let d = match kind {
                    "sigma" => BigRational::zero(),
                    "sigma_inv" => -h.clone(),
                    "averaged" => -(h.clone() * half.clone()),
                    "averaged_weighted" => {
                        -(h.clone() * (half.clone() - delta.clone() * quarter.clone()))
                    }
                    other => panic!("unknown crossing kind {other}"),
                };
                (one.clone(), d, g + 1)
            })
            .collect()
    }

    /// Does the cost depend on the HEIGHT of the sampled `q`?
    ///
    /// Interpolation needs ~157 distinct rational points, and exact rational
    /// arithmetic grows with numerator/denominator size, so a cost that scales
    /// with height would change the plan. Measured on the worst n=9 shape
    /// only (`[4,3,1,1]`, dim 216) — ~1/8 the full-partition cost and
    /// representative of it.
    #[test]
    #[ignore = "cost measurement, not a correctness gate"]
    fn a3_cost_vs_q_height() {
        let shape = vec![4usize, 3, 1, 1];
        for (num, den) in [
            (11i64, 10i64),
            (3, 2),
            (101, 100),
            (157, 1),
            (1_000_003, 999_983),
        ] {
            let q = BigRational::new(num.into(), den.into());
            let factors = build_factors(&q);
            let t = Instant::now();
            let _ = chi_q_atomic_exact(&shape, &factors, &q);
            println!("HEIGHT q={num}/{den}: {:.3} s", t.elapsed().as_secs_f64());
        }
    }

    #[test]
    #[ignore = "cost measurement, not a correctness gate"]
    fn time_one_a3_evaluation_point() {
        let q = BigRational::new(11.into(), 10.into());
        let factors = build_factors(&q);
        let shapes = partitions(9);
        assert_eq!(shapes.len(), 30, "p(9) = 30");
        println!(
            "A=3: n=9, {} factors, {} partitions",
            factors.len(),
            shapes.len()
        );

        let t0 = Instant::now();
        let mut worst = (0f64, Vec::new(), 0usize);
        let mut total_dim = 0usize;
        for shape in &shapes {
            let ts = Instant::now();
            let (dim, _) = seminormal_blocks_exact(shape, &q);
            let _chi = chi_q_atomic_exact(shape, &factors, &q);
            let el = ts.elapsed().as_secs_f64();
            total_dim += dim;
            if el > worst.0 {
                worst = (el, shape.clone(), dim);
            }
        }
        let total = t0.elapsed().as_secs_f64();
        println!("ALL 30 PARTITIONS: {total:.3} s   (sum of dims = {total_dim})");
        println!(
            "worst shape: {:?} dim={} at {:.3} s",
            worst.1, worst.2, worst.0
        );
        println!("=> one evaluation point costs {total:.3} s");
    }
}
