//! Monotone fine-Bratteli $1\times 1$ / $2\times 2$ Gelfand–Tsetlin edge transfer sweep.
//!
//! For a monotone product $\beta = \prod_{t} (c_t\,\sigma_{g_t} + d_t\,\mathbf{1}) \in H_n(q)$
//! with non-decreasing generator indices $0 \le g_0 \le g_1 \le \dots \le n - 2$ and balanced
//! Hecke relation $\sigma_g^2 = (q - q^{-1})\sigma_g + \mathbf{1}$:
//! 1. Factors sharing generator $g$ collapse via [`transfer_step`] to $O_g = \alpha_g\sigma_g + \beta_g\mathbf{1}$.
//! 2. In Young–Hoefsmit's seminormal Gelfand–Tsetlin basis indexed by standard Young tableau
//!    chains $\varnothing = s_0 \subset s_1 \subset \dots \subset s_n = \lambda$, $O_g$ acts
//!    only at step $s_{g+1}$, so trace closure projects $O_g$ onto its diagonal entry
//!    $$\alpha_g D(c_{\text{next}} - c_{\text{curr}}) + \beta_g, \qquad
//!    D(\delta') = \frac{q - q^{-1}}{1 - q^{-2\delta'}} =
//!    \begin{cases}
//!      q^{\delta'} / [\delta']_q & (\delta' > 0), \\
//!      -q^{\delta'} / [|\delta'|]_q & (\delta' < 0).
//!    \end{cases}$$
//! 3. Restricting to `max_rows = Some(2)` evaluates all two-row characters $\chi^{(n-k, k)}(\beta)$
//!    ($0 \le k \le \lfloor n/2 \rfloor$) in $\mathcal{O}(|E_{\mathrm{Bratteli}}^{(2)}(n)|)$
//!    Catalan-bounded operations, assembling the Temperley–Lieb / Jones–Markov trace
//!    $$\tau_{TL}(\beta) = \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{[n - 2k + 1]_q}{(q + q^{-1})^n}\,\chi^{(n-k, k)}(\beta)$$
//!    without constructing representation matrices.

use std::collections::BTreeMap;

use crate::peel::chain_transfer::transfer_step;
use crate::peel::markov_tower::LinearFactor;
use crate::scalar::RingScalar;

/// Partition $\lambda = (\lambda_0 \ge \lambda_1 \ge \dots > 0)$ of an integer $n$.
pub type Partition = Vec<usize>;

/// Errors returned by [`monotone_bratteli_characters`].
#[derive(Clone, PartialEq, Eq, Debug)]
pub enum BratteliTransferError {
    /// Generator sequence is not monotone non-decreasing (`g_{t+1} < g_t`).
    NonMonotoneWord {
        /// Earlier generator index.
        prev_gen: usize,
        /// Smaller subsequent generator index.
        next_gen: usize,
    },
    /// Generator index exceeds `num_strands - 2`.
    GeneratorOutOfRange {
        /// Offending generator index.
        gen: usize,
        /// Ambient strand count.
        num_strands: usize,
    },
    /// Either $q$ or a required quantum integer `\[m\]_q` ($1 \le m < n$) is not invertible in `R`.
    NonInvertibleQuantumInteger {
        /// Quantum integer index (`0` indicates `q` itself is non-invertible).
        index: usize,
    },
}

fn addable_boxes(shape: &[usize], max_rows: Option<usize>) -> Vec<(usize, usize)> {
    let mut out = Vec::new();
    let limit = match max_rows {
        Some(mr) => (shape.len() + 1).min(mr),
        None => shape.len() + 1,
    };
    for r in 0..limit {
        let cur = shape.get(r).copied().unwrap_or(0);
        if r == 0 || cur < shape[r - 1] {
            out.push((r, cur));
        }
    }
    out
}

fn add_box(shape: &[usize], row: usize) -> Partition {
    let mut next = shape.to_vec();
    if row == next.len() {
        next.push(1);
    } else {
        next[row] += 1;
    }
    next
}

fn quantum_int_in_ring<R: RingScalar>(m: usize, q: &R, q_inv: &R) -> R {
    assert!(m >= 1);
    let mut acc = R::zero();
    let m_i32 = m as i32;
    for k in 0..m_i32 {
        let exp = m_i32 - 1 - 2 * k;
        let term = if exp >= 0 {
            q.pow_u32(exp as u32)
        } else {
            q_inv.pow_u32(exp.unsigned_abs())
        };
        acc = acc.add_val(&term);
    }
    acc
}

/// Evaluate irreducible characters $\chi^\lambda(\beta) \in R$ for all partitions $\lambda \vdash n$
/// (with at most `max_rows` rows when `Some(r)` is given; `Some(2)` gives the Catalan two-row
/// Temperley–Lieb sweep) on a monotone factor sequence $\beta$.
pub fn monotone_bratteli_characters<R: RingScalar>(
    factors: &[LinearFactor<R>],
    num_strands: usize,
    q: &R,
    max_rows: Option<usize>,
) -> Result<BTreeMap<Partition, R>, BratteliTransferError> {
    if num_strands == 0 {
        let mut m = BTreeMap::new();
        m.insert(Vec::new(), R::one());
        return Ok(m);
    }
    let q_inv = q
        .try_inv()
        .ok_or(BratteliTransferError::NonInvertibleQuantumInteger { index: 0 })?;
    let h = q.sub_val(&q_inv);

    // 1. Verify monotonicity and group linear factors by generator g in 0..n-1:
    let max_gens = num_strands.saturating_sub(1);
    let mut grouped: Vec<Vec<(R, R)>> = vec![Vec::new(); max_gens];
    let mut last_gen: Option<usize> = None;
    for f in factors {
        if f.gen >= max_gens {
            return Err(BratteliTransferError::GeneratorOutOfRange {
                gen: f.gen,
                num_strands,
            });
        }
        if let Some(prev) = last_gen {
            if f.gen < prev {
                return Err(BratteliTransferError::NonMonotoneWord {
                    prev_gen: prev,
                    next_gen: f.gen,
                });
            }
        }
        last_gen = Some(f.gen);
        grouped[f.gen].push((f.c.clone(), f.d.clone()));
    }

    // Collapse each generator's polynomial O_g = alpha_g * sigma_g + beta_g * 1:
    let mut alpha_beta: Vec<(R, R)> = Vec::with_capacity(max_gens);
    for blk in &grouped {
        let mut a = R::zero();
        let mut b = R::one();
        for (c, d) in blk {
            let (an, bn, _) = transfer_step(&h, c, d, &a, &b);
            a = an;
            b = bn;
        }
        alpha_beta.push((a, b));
    }

    // Precompute axial-distance diagonal entries D(delta') for |delta'| in 1..num_strands:
    let mut d_pos: Vec<R> = vec![R::zero(); num_strands + 1];
    let mut d_neg: Vec<R> = vec![R::zero(); num_strands + 1];
    for m in 1..num_strands {
        let qm_int = quantum_int_in_ring(m, q, &q_inv);
        let qm_inv = qm_int.try_inv().ok_or(
            BratteliTransferError::NonInvertibleQuantumInteger { index: m },
        )?;
        d_pos[m] = q.pow_u32(m as u32).mul_val(&qm_inv);
        d_neg[m] = q_inv.pow_u32(m as u32).mul_val(&qm_inv).neg_val();
    }

    if let Some(0) = max_rows {
        return Ok(BTreeMap::new());
    }

    // 2. Sweep across fine-Bratteli edges `(shape s_{g+1}, content_of_last_added_box)`:
    let mut amplitudes: BTreeMap<(Partition, i32), R> = BTreeMap::new();
    amplitudes.insert((vec![1], 0), R::one());

    for (alpha, beta) in &alpha_beta {
        let mut next_amp: BTreeMap<(Partition, i32), R> = BTreeMap::new();
        for ((shape, c_this), amp) in &amplitudes {
            if amp.is_zero() {
                continue;
            }
            for (r, col) in addable_boxes(shape, max_rows) {
                let c_other = (col as i32) - (r as i32);
                let delta = c_other - *c_this;
                let diag_sigma = if delta >= 0 {
                    d_pos[delta as usize].clone()
                } else {
                    d_neg[delta.unsigned_abs() as usize].clone()
                };
                let weight = alpha.mul_val(&diag_sigma).add_val(beta);
                let contrib = amp.mul_val(&weight);
                if contrib.is_zero() {
                    continue;
                }
                let next_shape = add_box(shape, r);
                let key = (next_shape, c_other);
                if let Some(existing) = next_amp.get_mut(&key) {
                    let sum = existing.add_val(&contrib);
                    if sum.is_zero() {
                        next_amp.remove(&key);
                    } else {
                        *existing = sum;
                    }
                } else {
                    next_amp.insert(key, contrib);
                }
            }
        }
        amplitudes = next_amp;
    }

    // 3. Sum edge amplitudes into final shapes s_n = lambda:
    let mut chars: BTreeMap<Partition, R> = BTreeMap::new();
    for ((lam, _), amp) in amplitudes {
        if amp.is_zero() {
            continue;
        }
        if let Some(existing) = chars.get_mut(&lam) {
            let sum = existing.add_val(&amp);
            if sum.is_zero() {
                chars.remove(&lam);
            } else {
                *existing = sum;
            }
        } else {
            chars.insert(lam, amp);
        }
    }
    Ok(chars)
}

/// Evaluate all two-row characters $\chi^{(n-k, k)}(\beta)$ (`max_rows = Some(2)`) and assemble
/// the normalized Temperley–Lieb / Jones–Markov trace
/// $\tau_{TL}(\beta) = \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{[n - 2k + 1]_q}{(q + q^{-1})^n}\chi^{(n-k, k)}(\beta)$.
pub fn two_row_bratteli_trace<R: RingScalar>(
    factors: &[LinearFactor<R>],
    num_strands: usize,
    q: &R,
) -> Result<(R, BTreeMap<Partition, R>), BratteliTransferError> {
    let chars = monotone_bratteli_characters(factors, num_strands, q, Some(2))?;
    if num_strands == 0 {
        return Ok((R::one(), chars));
    }
    let q_inv = q
        .try_inv()
        .ok_or(BratteliTransferError::NonInvertibleQuantumInteger { index: 0 })?;
    let delta_two = q.add_val(&q_inv);
    let delta_inv = delta_two
        .try_inv()
        .ok_or(BratteliTransferError::NonInvertibleQuantumInteger { index: 2 })?;
    let delta_n_inv = delta_inv.pow_u32(num_strands as u32);

    let mut total = R::zero();
    for (lam, chi_val) in &chars {
        let r0 = lam.first().copied().unwrap_or(0);
        let r1 = lam.get(1).copied().unwrap_or(0);
        let qdim = quantum_int_in_ring(r0 - r1 + 1, q, &q_inv);
        let y_lam = qdim.mul_val(&delta_n_inv);
        total = total.add_val(&y_lam.mul_val(chi_val));
    }
    Ok((total, chars))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::peel::markov_tower::streaming_markov_trace;
    use crate::scalar::{rat, TruncatedJet};
    use crate::temperley_lieb::TemperleyLiebBasis;

    #[test]
    fn two_row_bratteli_matches_markov_tower_and_temperley_lieb_over_rationals_and_jets() {
        // Test 1: Exact rational q = 2 on n = 6 strands (Catalan C_6 = 132 regime):
        let q = rat(2, 1);
        let q_inv = rat(1, 2);
        let h = q.sub_val(&q_inv);
        let delta = q.add_val(&q_inv);
        // z_TL = q - 1/delta = q^3 / (q^2 + 1) = 8 / 5 at q = 2:
        let z_tl = q.sub_val(&delta.try_inv().unwrap());
        assert_eq!(z_tl, rat(8, 5));

        let factors = vec![
            LinearFactor::sigma(0),
            LinearFactor::sigma(0),
            LinearFactor::sigma_inv(1, &h),
            LinearFactor::new(rat(1, 1), rat(-3, 8), 2),
            LinearFactor::sigma(3),
            LinearFactor::sigma_inv(4, &h),
            LinearFactor::sigma(4),
        ];

        let (bratteli_tr, chars) = two_row_bratteli_trace(&factors, 6, &q).unwrap();
        // Two-row partitions of 6: (6), (5,1), (4,2), (3,3) => at most 4 partitions!
        assert!(chars.len() <= 4);

        let tower_tr = streaming_markov_trace(&factors, 6, &h, &z_tl);
        assert_eq!(bratteli_tr, tower_tr);

        // Also check against TemperleyLiebBasis loop trace / delta^6:
        let tl6 = TemperleyLiebBasis::with_hecke_projection(6, q.clone()).unwrap();
        let mut prod = crate::free_alg::FreeAlg::one();
        for f in &factors {
            prod = &prod * &f.to_free_alg();
        }
        let tl_tr = tl6
            .loop_trace_of(&prod)
            .mul_val(&delta.try_inv().unwrap().pow_u32(6));
        assert_eq!(bratteli_tr, tl_tr);

        // Test 2: Exact truncated h-jet Q[h]/(h^7) around q = 1!
        type J = TruncatedJet<num_rational::BigRational, 6>;
        let q_jet = J::q_from_h();
        let h_jet = J::h();
        let delta_jet = q_jet.add_val(&q_jet.try_inv().unwrap());
        let z_jet = q_jet.sub_val(&delta_jet.try_inv().unwrap());

        let jet_factors = vec![
            LinearFactor::sigma(0),
            LinearFactor::sigma_inv(1, &h_jet),
            LinearFactor::sigma(2),
            LinearFactor::sigma(2),
        ];
        let (jet_bratteli, _) = two_row_bratteli_trace(&jet_factors, 4, &q_jet).unwrap();
        let jet_tower = streaming_markov_trace(&jet_factors, 4, &h_jet, &z_jet);
        assert_eq!(jet_bratteli, jet_tower);

        // Test 3: S_3 3-cycle character chi^{(2,1)}(sigma_0 sigma_1) = -1 for ANY q!
        let s3_factors = vec![LinearFactor::sigma(0), LinearFactor::sigma(1)];
        let all_chars_3 = monotone_bratteli_characters(&s3_factors, 3, &q_jet, None).unwrap();
        assert_eq!(all_chars_3.get(&vec![2, 1]), Some(&J::from_i64(-1)));
    }
}
