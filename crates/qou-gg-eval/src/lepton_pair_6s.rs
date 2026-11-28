//! 6-strand neutral `e^- + \bar\nu_e + unknot` `γγ` lepton-pair process words (`3B`).
//!
//! Enumerates all `4^1 + ... + 4^5 = 1,364` 6-strand `γγ` words in `{V(0), V(1), V(2), V(3)}`,
//! filters by 4-component braid closure + pairwise linking pattern `[0, 0, 0, 0, 0, ±1]` +
//! framing-corrected `U_q(sl_2)` quantum trace match to `Hopf_± ⊔ 0_1 ⊔ 0_1`
//! (`PhotonCrossingMonomials.pair_word_reduces`: `V_0 V_1 V_2 V_0 V_3 = sigma_0^2 sigma_1^-1 sigma_4^-1`),
//! and evaluates 80-dps Convention-D Markov traces, multi-level reading-3 margins on `H_6(q)`,
//! and restricted `b6` (`count_ones == 4`) `K`-sector factor `f_L` (`qbeta_gg_process_word_probe.py`).

use crate::scalars::{fmt_dps, parse_dec, Q0Params};
use crate::tower_gt::{HeckeLetter, TwoRowTowerRep};
use rug::ops::Pow;
use rug::Float;
use serde::{Deserialize, Serialize};

/// Analyze 6-strand signed braid word (`+1..+5` = `sigma_0..sigma_4`, `-1..-5` = `sigma_0^-1..sigma_4^-1`):
/// returns `(n_components, sorted_pairwise_linking, writhe, comp_of_strand)`.
pub fn analyze_b6_closure(signed_word: &[i32]) -> (usize, Vec<i32>, i32, [usize; 6]) {
    let mut pos_to_strand = [0usize, 1, 2, 3, 4, 5];
    let mut cross_sum = [[0i32; 6]; 6];
    let mut writhe = 0i32;

    for &letter in signed_word {
        let g = (letter.unsigned_abs() as usize) - 1;
        let sign = if letter > 0 { 1 } else { -1 };
        writhe += sign;
        let s_l = pos_to_strand[g];
        let s_r = pos_to_strand[g + 1];
        cross_sum[s_l][s_r] += sign;
        cross_sum[s_r][s_l] += sign;
        pos_to_strand.swap(g, g + 1);
    }

    let mut next_strand = [0usize; 6];
    for (p, &s) in pos_to_strand.iter().enumerate() {
        next_strand[s] = p;
    }
    let mut comp_of = [usize::MAX; 6];
    let mut n_comp = 0usize;
    for start in 0..6 {
        if comp_of[start] != usize::MAX {
            continue;
        }
        let mut cur = start;
        while comp_of[cur] == usize::MAX {
            comp_of[cur] = n_comp;
            cur = next_strand[cur];
        }
        n_comp += 1;
    }

    let mut lk_pairs = Vec::new();
    for c1 in 0..n_comp {
        for c2 in (c1 + 1)..n_comp {
            let mut s = 0i32;
            for a in 0..6 {
                if comp_of[a] != c1 {
                    continue;
                }
                for b in 0..6 {
                    if comp_of[b] != c2 {
                        continue;
                    }
                    s += cross_sum[a][b];
                }
            }
            lk_pairs.push(s / 2);
        }
    }
    lk_pairs.sort();
    (n_comp, lk_pairs, writhe, comp_of)
}

/// Check whether every strand `0..6` is touched by at least one vertex `V(s)` (`s` touches `{s, s+1, s+2}`).
fn touches_all_six_strands(seq: &[u8]) -> bool {
    let mut mask = 0u8;
    for &s in seq {
        mask |= 0b111u8 << s;
    }
    mask == 0b111111u8
}

/// Apply `U_q(sl_2)` R-matrix generator `sigma_g` (`inv = false`) or `sigma_g^-1 = sigma_g - h*I` (`inv = true`)
/// on `(C^2)^{tensor 6}` (`dim = 64`), where bit `s` in `0..6` is `0` (`e_1`, weight `q`) or `1` (`e_2`, weight `q^-1`).
fn apply_uq_sl2_letter_6s(
    prec: u32,
    q: &Float,
    q_inv: &Float,
    h: &Float,
    g: usize,
    inv: bool,
    v: &mut [Float; 64],
    out: &mut [Float; 64],
) {
    use rug::Assign;
    for x in out.iter_mut() {
        x.assign(0);
    }
    let bit_l = 1usize << g;
    let bit_r = 1usize << (g + 1);

    for mask in 0..64usize {
        let val = &v[mask];
        if val.is_zero() {
            continue;
        }
        let bl = (mask & bit_l) != 0;
        let br = (mask & bit_r) != 0;
        match (bl, br) {
            (false, false) | (true, true) => {
                let c = if inv { q_inv } else { q };
                out[mask] += Float::with_val(prec, val * c);
            }
            (false, true) => {
                let swapped = (mask | bit_l) & !bit_r;
                out[swapped] += val;
                if inv {
                    out[mask] -= Float::with_val(prec, val * h);
                }
            }
            (true, false) => {
                let swapped = (mask & !bit_l) | bit_r;
                out[swapped] += val;
                if !inv {
                    out[mask] += Float::with_val(prec, val * h);
                }
            }
        }
    }
    v.clone_from_slice(out);
}

/// Compute `(J_framed(w), f_L(w))` where:
/// - `J_framed(w) = q^(-2 * writhe) * Tr(K^{tensor 6} * rho(w))`
/// - `f_L(w) = Tr_{downs == 4}(K^{tensor 6} * rho(w)) / [2]_q^6` (`qbeta_gg_process_word_probe.py` line 126).
pub fn framed_quantum_and_sector_trace_6s(
    params: &Q0Params,
    signed_word: &[i32],
    writhe: i32,
) -> (Float, Float) {
    use rug::Assign;
    let p = params.prec_bits;
    let mut v: [Float; 64] = std::array::from_fn(|_| Float::with_val(p, 0));
    let mut scratch: [Float; 64] = std::array::from_fn(|_| Float::with_val(p, 0));
    let mut tr_k = Float::with_val(p, 0);
    let mut tr_sector_b6 = Float::with_val(p, 0);

    for start_mask in 0..64usize {
        for x in v.iter_mut() {
            x.assign(0);
        }
        v[start_mask].assign(1);
        for &letter in signed_word {
            let g = (letter.unsigned_abs() as usize) - 1;
            let inv = letter < 0;
            apply_uq_sl2_letter_6s(
                p,
                &params.q,
                &params.q_inv,
                &params.h,
                g,
                inv,
                &mut v,
                &mut scratch,
            );
        }
        let diag_val = &v[start_mask];
        let ones = start_mask.count_ones() as i32;
        let zeros = 6 - ones;
        let k_exp = zeros - ones;
        let k_weight = Float::with_val(p, params.q.clone().pow(k_exp));
        let term = Float::with_val(p, k_weight * diag_val);
        tr_k += &term;
        if ones == 4 {
            tr_sector_b6 += &term;
        }
    }

    let framing = Float::with_val(p, params.q.clone().pow(-2 * writhe));
    let j_framed = Float::with_val(p, framing * tr_k);
    let d2_pow6 = Float::with_val(p, params.q2_int.clone().pow(6u32));
    let f_l = Float::with_val(p, tr_sector_b6 / d2_pow6);
    (j_framed, f_l)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LeptonPairSampleRow {
    pub word: String,
    pub n_vertices: usize,
    pub no_idle_strand: bool,
    pub chirality: String,
    pub tr_m_h6: String,
    pub f_l_sector: String,
    pub j_framed_norm: String,
    pub reading3_m1_to_6: bool,
    pub min_level_char: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LeptonPair6sReport {
    pub max_vertices: usize,
    pub n_candidates_evaluated: usize,
    pub n_electron_antineutrino_words: usize,
    pub n_positron_neutrino_words: usize,
    pub n_electron_antineutrino_no_idle_strand: usize,
    pub min_vertices_any_6s: usize,
    pub min_vertices_no_idle_strand: usize,
    pub canonical_word: String,
    pub canonical_reduced_braid: String,
    pub canonical_two_photon_factorisation: String,
    pub canonical_tr_m_h6: String,
    pub canonical_f_l_sector: String,
    pub canonical_j_framed_norm: String,
    pub canonical_reading3_m1_to_6: bool,
    pub canonical_min_level_char: String,
    pub distinct_tr_m_count_among_60: usize,
    pub n_passing_reading3_of_60: usize,
    pub sample_words: Vec<LeptonPairSampleRow>,
}

pub fn evaluate_lepton_pair_6s(
    params: &Q0Params,
    max_vertices: usize,
    dps: usize,
) -> LeptonPair6sReport {
    let p = params.prec_bits;
    let rep6 = TwoRowTowerRep::new(params, 6);
    let tol = parse_dec(p, "1e-80");
    let q2_pow4 = Float::with_val(p, params.q2_int.clone().pow(4u32));

    let ref_pos_braid = [1i32, 1, -2, -5];
    let (nc_pos, lk_pos, wr_pos, _) = analyze_b6_closure(&ref_pos_braid);
    assert_eq!(nc_pos, 4);
    assert_eq!(lk_pos, vec![0, 0, 0, 0, 0, 1]);
    let (j_ref_pos, _) = framed_quantum_and_sector_trace_6s(params, &ref_pos_braid, wr_pos);

    let ref_neg_braid = [-1i32, -1, 2, 5];
    let (nc_neg, lk_neg, wr_neg, _) = analyze_b6_closure(&ref_neg_braid);
    assert_eq!(nc_neg, 4);
    assert_eq!(lk_neg, vec![-1, 0, 0, 0, 0, 0]);
    let (j_ref_neg, _) = framed_quantum_and_sector_trace_6s(params, &ref_neg_braid, wr_neg);

    let mut n_candidates = 0usize;
    // (seq, no_idle, tr_m, f_l, r3_ok, min_char)
    let mut pos_hits: Vec<(Vec<u8>, bool, Float, Float, bool, Float)> = Vec::new();
    let mut neg_count = 0usize;
    let mut min_hit_any = usize::MAX;
    let mut min_hit_no_idle = usize::MAX;

    for len in 1..=max_vertices {
        let total = 1usize << (2 * len);
        for code in 0..total {
            n_candidates += 1;
            let mut seq = Vec::with_capacity(len);
            let mut signed = Vec::with_capacity(2 * len);
            for step in (0..len).rev() {
                let s = ((code >> (2 * step)) & 3) as u8;
                seq.push(s);
                signed.push((s as i32) + 1);
                signed.push(-((s as i32) + 2));
            }

            let (nc, lk, wr, _) = analyze_b6_closure(&signed);
            if nc != 4 {
                continue;
            }
            if lk == [0, 0, 0, 0, 0, 1] {
                let (j_val, f_l) = framed_quantum_and_sector_trace_6s(params, &signed, wr);
                if (j_val - &j_ref_pos).abs() < tol {
                    let no_idle = touches_all_six_strands(&seq);
                    if len < min_hit_any {
                        min_hit_any = len;
                    }
                    if no_idle && len < min_hit_no_idle {
                        min_hit_no_idle = len;
                    }
                    let hecke_w: Vec<HeckeLetter> = seq
                        .iter()
                        .flat_map(|&s| HeckeLetter::v_pair(s as usize))
                        .collect();
                    let ev = rep6.evaluate_word(&hecke_w);
                    pos_hits.push((
                        seq,
                        no_idle,
                        ev.tr_m,
                        f_l,
                        ev.reading3_m1_to_n,
                        ev.min_char_m1_to_n,
                    ));
                }
            } else if lk == [-1, 0, 0, 0, 0, 0] {
                let (j_val, _) = framed_quantum_and_sector_trace_6s(params, &signed, wr);
                if (j_val - &j_ref_neg).abs() < tol {
                    if len < min_hit_any {
                        min_hit_any = len;
                    }
                    neg_count += 1;
                }
            }
        }
    }

    let canon_seq = vec![0u8, 1, 2, 0, 3];
    let canon_entry = pos_hits
        .iter()
        .find(|(s, _, _, _, _, _)| *s == canon_seq)
        .expect("canonical word V0V1V2V0V3 must be among 6-strand e^- + nu_bar hits");

    let mut distinct_tr: Vec<Float> = Vec::new();
    for (_, _, tr, _, _, _) in &pos_hits {
        if !distinct_tr
            .iter()
            .any(|u| (tr.clone() - u).abs() < tol)
        {
            distinct_tr.push(tr.clone());
        }
    }

    let n_no_idle = pos_hits.iter().filter(|(_, ni, _, _, _, _)| *ni).count();
    let n_r3 = pos_hits.iter().filter(|(_, _, _, _, ok, _)| *ok).count();
    let j_pos_norm = Float::with_val(p, &j_ref_pos / &q2_pow4);

    // Include canonical V0V1V2V0V3 plus earliest words in sample_words
    let mut sample_indices: Vec<usize> = (0..pos_hits.len().min(5)).collect();
    if let Some(c_idx) = pos_hits.iter().position(|(s, _, _, _, _, _)| *s == canon_seq) {
        if !sample_indices.contains(&c_idx) {
            sample_indices.push(c_idx);
        }
    }
    let sample_words: Vec<LeptonPairSampleRow> = sample_indices
        .into_iter()
        .map(|idx| {
            let (seq, ni, tr, fl, ok, min_c) = &pos_hits[idx];
            LeptonPairSampleRow {
                word: seq.iter().map(|&s| format!("V{s}")).collect(),
                n_vertices: seq.len(),
                no_idle_strand: *ni,
                chirality: "e^- + bar(nu_e) + 0_1".to_string(),
                tr_m_h6: fmt_dps(tr, dps),
                f_l_sector: fmt_dps(fl, dps),
                j_framed_norm: fmt_dps(&j_pos_norm, dps),
                reading3_m1_to_6: *ok,
                min_level_char: fmt_dps(min_c, dps),
            }
        })
        .collect();

    LeptonPair6sReport {
        max_vertices,
        n_candidates_evaluated: n_candidates,
        n_electron_antineutrino_words: pos_hits.len(),
        n_positron_neutrino_words: neg_count,
        n_electron_antineutrino_no_idle_strand: n_no_idle,
        min_vertices_any_6s: if min_hit_any == usize::MAX { 0 } else { min_hit_any },
        min_vertices_no_idle_strand: if min_hit_no_idle == usize::MAX {
            0
        } else {
            min_hit_no_idle
        },
        canonical_word: "V0V1V2V0V3".to_string(),
        canonical_reduced_braid: "sigma_0^2 sigma_1^-1 sigma_4^-1".to_string(),
        canonical_two_photon_factorisation:
            "h^2 * gamma_0(0, -h^-1, -1) * gamma_3(0, -h^-1, 0)".to_string(),
        canonical_tr_m_h6: fmt_dps(&canon_entry.2, dps),
        canonical_f_l_sector: fmt_dps(&canon_entry.3, dps),
        canonical_j_framed_norm: fmt_dps(&j_pos_norm, dps),
        canonical_reading3_m1_to_6: canon_entry.4,
        canonical_min_level_char: fmt_dps(&canon_entry.5, dps),
        distinct_tr_m_count_among_60: distinct_tr.len(),
        n_passing_reading3_of_60: n_r3,
        sample_words,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn lepton_pair_6s_finds_60_plus_60_and_no_idle_at_l5() {
        let params = Q0Params::proton_pinned(320, None);
        let rep = evaluate_lepton_pair_6s(&params, 5, 40);
        assert_eq!(rep.n_candidates_evaluated, 1364);
        assert_eq!(rep.min_vertices_any_6s, 3);
        assert_eq!(rep.min_vertices_no_idle_strand, 5);
        assert_eq!(rep.n_electron_antineutrino_words, 60);
        assert_eq!(rep.n_positron_neutrino_words, 60);
    }
}
