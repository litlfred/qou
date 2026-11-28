//! Full-strand `A = 2..4` (`6, 9, 12`-strand) `T3` colour-valence (`M_T3(A) = 3 * floor(A/2)`)
//! `γγ`-bonded nuclear braid evaluator (`1 + 4`).
//!
//! Evaluates on EVERY strand (`6, 9, 12` strands, zero strand dropping) at `>= 80` dps (`rug::Float`):
//! 1. **Proper bare `γγ` nucleon `V^3` cell** (`x_free = V(0)^3 * V(3)^3 * ... * V(3A-3)^3`):
//!    - `A = 2` (`^2H`, 6 strands, 1 `T3` `V^3` bond `(0,1)`);
//!    - `A = 3` (`^3H / ^3He`, 9 strands, 3 `T3` `V^3` bonds on `K_3`, `over` & `under` transport, plus 2-bond chain);
//!    - `A = 4` (`^4He`, 12 strands, 6 `T3` `V^3` bonds on `K_4` across all 4 canonical formation routes
//!      `D+D pairing a`, `D+D pairing b`, `3H+p`, `3He+n` × `over`/`under`, PLUS the quark-disjoint Tait
//!      3-edge-colouring `k4HalfEdgeToQuark` × `over`/`under`, plus 3-bond chain);
//! 2. **Production typed `uud` / `udd` nucleon block cell** (`2H pn`, `3H pnn`, `3He ppn`, `4He ppnn`)
//!    across the identical bond routes for exact cross-check against `light_nuclei_a2_a3` / `he4_all_pairs_exact`.
//!
//! Reports exact 80-dps free & bound Convention-D Markov traces, trace ratio `r_A = tr_M(bound) / tr_M(free)`,
//! multi-level reading-3 positivity verdict (`m = 1..3A` and `m = 3..3A`), and unfitted `-E_0^tower ln(r_A)`
//! & `-E_0^(0) ln(r_A)` against AME2020 (`NO FITTING`).

use crate::scalars::{
    fmt_dps, parse_dec, Q0Params, AME2020_B_2H_MEV, AME2020_B_3HE_MEV, AME2020_B_3H_MEV,
    AME2020_B_4HE_MEV,
};
use crate::tower_gt::{HeckeLetter, TwoRowTowerRep};
use rug::Float;
use serde::{Deserialize, Serialize};

fn v3_at(s: usize) -> Vec<HeckeLetter> {
    let mut w = Vec::with_capacity(6);
    for _ in 0..3 {
        w.extend_from_slice(&HeckeLetter::v_pair(s));
    }
    w
}

fn proton_block(k: usize) -> Vec<HeckeLetter> {
    let mut w = v3_at(k);
    w.extend_from_slice(&[
        HeckeLetter::Pos(k),
        HeckeLetter::Half(k),
        HeckeLetter::Half(k + 1),
        HeckeLetter::Pos(k),
        HeckeLetter::Pos(k),
    ]);
    w
}

fn neutron_block(k: usize) -> Vec<HeckeLetter> {
    let mut w = v3_at(k);
    w.extend_from_slice(&[
        HeckeLetter::Half(k),
        HeckeLetter::Half(k),
        HeckeLetter::Inv(k + 1),
        HeckeLetter::Pos(k),
        HeckeLetter::Pos(k),
    ]);
    w
}

/// Transported `γγ` `V^3` bond between nucleons `(i, j)` (`0 <= i < j`), matching `hecke_flint.bond`:
/// transports strand `3*i + 2` across `3*i + 3 .. 3*j - 1` (`gens = 3*i + 2 ..= 3*j - 2`) to `3*j - 1`,
/// applies `V(3*j - 1)^3`, and transports back.
pub fn nucleon_pair_bond(i: usize, j: usize, variant: &str) -> Vec<HeckeLetter> {
    assert!(i < j);
    let mut w = Vec::new();
    let start_g = 3 * i + 2;
    let end_g_excl = 3 * j - 1; // gens = start_g .. end_g_excl
    let over = match variant {
        "over" | "-" => true,
        "under" => false,
        other => panic!("unknown transport variant {other:?}"),
    };
    for g in start_g..end_g_excl {
        w.push(if over {
            HeckeLetter::Pos(g)
        } else {
            HeckeLetter::Inv(g)
        });
    }
    w.extend(v3_at(3 * j - 1));
    for g in (start_g..end_g_excl).rev() {
        w.push(if over {
            HeckeLetter::Inv(g)
        } else {
            HeckeLetter::Pos(g)
        });
    }
    w
}

/// Transported `V^3` bond between explicit quark strands `(q_a, q_b)` (`0 <= q_a < q_b < 12`),
/// used for the `K_4` Tait 3-edge-colouring `k4HalfEdgeToQuark` (`TetrahedralFluxRingAndMajoranaCluster.lean`),
/// where each nucleon's 3 quark strands carry at most 1 bond half-edge!
/// Note: `V(s)` acts on strands `(s, s+1, s+2)` (`gens s, s+1`), so when `q_b >= q_a + 1` and `q_b + 1 < 12`
/// (or `q_b == 11`, where `V(9)` acts on `(9, 10, 11)`!), we transport `q_a` to `target = min(q_b - 1, 9)`.
pub fn tait_strand_pair_bond(q_a: usize, q_b: usize, variant: &str) -> Vec<HeckeLetter> {
    assert!(q_a < q_b && q_b < 12);
    let over = variant != "under";
    // V(v_site) uses strands (v_site, v_site + 1, v_site + 2).
    // For adjacent nucleon boundary (2,3)->V(2), (5,6)->V(5), (8,9)->V(8);
    // for (1,7)->transport 1..6 then V(6); for (4,10)->transport 4..9 then V(9);
    // for (0,11)->transport 0..9 then V(9) (touching strands 9,10,11 with strand 0 transported to 9!).
    let v_site = (q_b - 1).min(9);
    let mut w = Vec::new();
    for g in q_a..v_site {
        w.push(if over {
            HeckeLetter::Pos(g)
        } else {
            HeckeLetter::Inv(g)
        });
    }
    w.extend(v3_at(v_site));
    for g in (q_a..v_site).rev() {
        w.push(if over {
            HeckeLetter::Inv(g)
        } else {
            HeckeLetter::Pos(g)
        });
    }
    w
}

/// Assemble full `3*A`-strand word following `hecke_flint.atom_word`:
/// each bond `(i, j)` in route order is placed immediately after block `J = max_{so far} j`.
pub fn assemble_atom_word(
    nucleon_order: &str,
    bonds: &[(usize, usize)],
    variant: &str,
) -> Vec<HeckeLetter> {
    let a = nucleon_order.len();
    let mut after: Vec<Vec<HeckeLetter>> = vec![Vec::new(); a];
    let mut j_max = 0usize;
    for &(i, j) in bonds {
        if j > j_max {
            j_max = j;
        }
        after[j_max].extend(nucleon_pair_bond(i, j, variant));
    }
    let mut word = Vec::new();
    for (k, ch) in nucleon_order.chars().enumerate() {
        let base = match ch {
            'v' => v3_at(3 * k),
            'p' => proton_block(3 * k),
            'n' => neutron_block(3 * k),
            other => panic!("unknown nucleon code {other:?}"),
        };
        word.extend(base);
        word.extend_from_slice(&after[k]);
    }
    word
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LightNucleusT3Row {
    pub nuclide: String,
    pub a: usize,
    pub n_strands: usize,
    pub nucleon_cell: String,
    pub order_code: String,
    pub route: String,
    pub transport_variant: String,
    pub n_bonds: usize,
    pub m_t3_valence_cap: usize,
    pub word_len_letters: usize,
    pub epistemic_tag: String,
    pub tr_free: String,
    pub tr_bound: String,
    pub ratio: String,
    pub bound_attracts: bool,
    pub reading3_m1_to_3a: bool,
    pub reading3_m3_to_3a: bool,
    pub failing_levels_m1_to_3a: Vec<usize>,
    pub min_level_char_m1_to_3a: String,
    pub b_tower_mev: Option<String>,
    pub b_order_zero_mev: Option<String>,
    pub ame2020_b_mev: String,
    pub err_vs_ame_tower_pct: Option<String>,
    pub err_vs_ame_order_zero_pct: Option<String>,
}

pub fn evaluate_light_nuclei_t3(params: &Q0Params, dps: usize) -> Vec<LightNucleusT3Row> {
    let p = params.prec_bits;
    let one = Float::with_val(p, 1);
    let hundred = Float::with_val(p, 100);

    let rep6 = TwoRowTowerRep::new(params, 6);
    let rep9 = TwoRowTowerRep::new(params, 9);
    let rep12 = TwoRowTowerRep::new(params, 12);

    // Precompute free traces on 6, 9, 12 strands (and verify product property tr(free) = prod tr(block)!)
    let eval_cell = |rep: &TwoRowTowerRep,
                     nuclide: &str,
                     a: usize,
                     cell_kind: &str,
                     order_code: &str,
                     route: &str,
                     variant: &str,
                     n_bonds: usize,
                     free_tr: &Float,
                     bound_word: &[HeckeLetter],
                     ame_str: &str|
     -> LightNucleusT3Row {
        let ev = rep.evaluate_word(bound_word);
        let ratio = Float::with_val(p, &ev.tr_m / free_tr);
        let ame = parse_dec(p, ame_str);
        let attracts = ratio > 0 && ratio < one;
        let (bt_s, b0_s, errt_s, err0_s) = if ratio > 0 {
            let ln_r = Float::with_val(p, ratio.clone().ln());
            let bt: Float = -Float::with_val(p, &params.e0_tower_mev * &ln_r);
            let b0: Float = -Float::with_val(p, &params.e0_order_zero_mev * &ln_r);
            let errt = Float::with_val(
                p,
                Float::with_val(p, Float::with_val(p, &bt / &ame) - &one) * &hundred,
            );
            let err0 = Float::with_val(
                p,
                Float::with_val(p, Float::with_val(p, &b0 / &ame) - &one) * &hundred,
            );
            (
                Some(fmt_dps(&bt, dps)),
                Some(fmt_dps(&b0, dps)),
                Some(fmt_dps(&errt, dps)),
                Some(fmt_dps(&err0, dps)),
            )
        } else {
            (None, None, None, None)
        };

        LightNucleusT3Row {
            nuclide: nuclide.to_string(),
            a,
            n_strands: 3 * a,
            nucleon_cell: cell_kind.to_string(),
            order_code: order_code.to_string(),
            route: route.to_string(),
            transport_variant: variant.to_string(),
            n_bonds,
            m_t3_valence_cap: 3 * (a / 2),
            word_len_letters: bound_word.len(),
            epistemic_tag: "Conditional".to_string(),
            tr_free: fmt_dps(free_tr, dps),
            tr_bound: fmt_dps(&ev.tr_m, dps),
            ratio: fmt_dps(&ratio, dps),
            bound_attracts: attracts,
            reading3_m1_to_3a: ev.reading3_m1_to_n,
            reading3_m3_to_3a: ev.reading3_m3_to_n,
            failing_levels_m1_to_3a: ev.failing_levels_m1_to_n,
            min_level_char_m1_to_3a: fmt_dps(&ev.min_char_m1_to_n, dps),
            b_tower_mev: bt_s,
            b_order_zero_mev: b0_s,
            ame2020_b_mev: ame_str.to_string(),
            err_vs_ame_tower_pct: errt_s,
            err_vs_ame_order_zero_pct: err0_s,
        }
    };

    let mut rows = Vec::new();

    // ── A = 2 (6 strands): ^2H (1 T3 V^3 bond on K_2) ──────────────────────
    let free_2_vv = rep6.evaluate_word(&assemble_atom_word("vv", &[], "-")).tr_m;
    let w_2_vv = assemble_atom_word("vv", &[(0, 1)], "-");
    rows.push(eval_cell(
        &rep6,
        "2H",
        2,
        "bare_gg_V3",
        "vv",
        "K2 single bond (0,1)",
        "-",
        1,
        &free_2_vv,
        &w_2_vv,
        AME2020_B_2H_MEV,
    ));

    let free_2_pn = rep6.evaluate_word(&assemble_atom_word("pn", &[], "-")).tr_m;
    let w_2_pn = assemble_atom_word("pn", &[(0, 1)], "-");
    rows.push(eval_cell(
        &rep6,
        "2H",
        2,
        "typed_uud_udd",
        "pn",
        "K2 single bond (0,1)",
        "-",
        1,
        &free_2_pn,
        &w_2_pn,
        AME2020_B_2H_MEV,
    ));

    // ── A = 3 (9 strands): ^3H / ^3He (3 T3 V^3 bonds on K_3 + 2-bond chain) ──
    let k3_bonds = [(0usize, 1usize), (1, 2), (0, 2)];
    let chain3_bonds = [(0usize, 1usize), (1, 2)];

    let free_3_vvv = rep9.evaluate_word(&assemble_atom_word("vvv", &[], "-")).tr_m;
    for variant in ["over", "under"] {
        let w = assemble_atom_word("vvv", &k3_bonds, variant);
        rows.push(eval_cell(
            &rep9,
            "3H",
            3,
            "bare_gg_V3",
            "vvv",
            "K3 all-pairs [(0,1),(1,2),(0,2)]",
            variant,
            3,
            &free_3_vvv,
            &w,
            AME2020_B_3H_MEV,
        ));
        rows.push(eval_cell(
            &rep9,
            "3He",
            3,
            "bare_gg_V3",
            "vvv",
            "K3 all-pairs [(0,1),(1,2),(0,2)]",
            variant,
            3,
            &free_3_vvv,
            &w,
            AME2020_B_3HE_MEV,
        ));
    }
    let w_chain3_vvv = assemble_atom_word("vvv", &chain3_bonds, "-");
    rows.push(eval_cell(
        &rep9,
        "3H",
        3,
        "bare_gg_V3",
        "vvv",
        "chain control [(0,1),(1,2)]",
        "-",
        2,
        &free_3_vvv,
        &w_chain3_vvv,
        AME2020_B_3H_MEV,
    ));

    let free_3_pnn = rep9.evaluate_word(&assemble_atom_word("pnn", &[], "-")).tr_m;
    let free_3_ppn = rep9.evaluate_word(&assemble_atom_word("ppn", &[], "-")).tr_m;
    for variant in ["over", "under"] {
        let w_pnn = assemble_atom_word("pnn", &k3_bonds, variant);
        rows.push(eval_cell(
            &rep9,
            "3H",
            3,
            "typed_uud_udd",
            "pnn",
            "K3 all-pairs [(0,1),(1,2),(0,2)]",
            variant,
            3,
            &free_3_pnn,
            &w_pnn,
            AME2020_B_3H_MEV,
        ));
        let w_ppn = assemble_atom_word("ppn", &k3_bonds, variant);
        rows.push(eval_cell(
            &rep9,
            "3He",
            3,
            "typed_uud_udd",
            "ppn",
            "K3 all-pairs [(0,1),(1,2),(0,2)]",
            variant,
            3,
            &free_3_ppn,
            &w_ppn,
            AME2020_B_3HE_MEV,
        ));
    }

    // ── A = 4 (12 strands): ^4He (6 T3 V^3 bonds on K_4) ───────────────────
    let k4_routes: [(&str, [(usize, usize); 6]); 4] = [
        (
            "K4 D+D pairing a",
            [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
        ),
        (
            "K4 D+D pairing b",
            [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
        ),
        (
            "K4 3H+p",
            [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
        ),
        (
            "K4 3He+n",
            [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
        ),
    ];
    let chain4_bonds = [(0usize, 1usize), (1, 2), (2, 3)];

    let free_4_vvvv = rep12
        .evaluate_word(&assemble_atom_word("vvvv", &[], "-"))
        .tr_m;
    for (r_name, r_bonds) in &k4_routes {
        for variant in ["over", "under"] {
            let w = assemble_atom_word("vvvv", r_bonds, variant);
            rows.push(eval_cell(
                &rep12,
                "4He",
                4,
                "bare_gg_V3",
                "vvvv",
                r_name,
                variant,
                6,
                &free_4_vvvv,
                &w,
                AME2020_B_4HE_MEV,
            ));
        }
    }
    // Quark-disjoint Tait 3-edge-colouring on K_4 (`k4HalfEdgeToQuark`:
    // colour 0: (2,3), (8,9); colour 1: (5,6), (0,11); colour 2: (1,7), (4,10))
    let tait_pairs: [(usize, usize, usize); 6] = [
        (1, 2, 3),   // nucleon (0,1) -> after block 1
        (2, 5, 6),   // nucleon (1,2) -> after block 2
        (2, 1, 7),   // nucleon (0,2) -> after block 2
        (3, 8, 9),   // nucleon (2,3) -> after block 3
        (3, 4, 10),  // nucleon (1,3) -> after block 3
        (3, 0, 11),  // nucleon (0,3) -> after block 3
    ];
    for variant in ["over", "under"] {
        let mut after: Vec<Vec<HeckeLetter>> = vec![Vec::new(); 4];
        for &(blk_j, qa, qb) in &tait_pairs {
            after[blk_j].extend(tait_strand_pair_bond(qa, qb, variant));
        }
        let mut w_tait = Vec::new();
        for k in 0..4 {
            w_tait.extend(v3_at(3 * k));
            w_tait.extend_from_slice(&after[k]);
        }
        rows.push(eval_cell(
            &rep12,
            "4He",
            4,
            "bare_gg_V3",
            "vvvv",
            "K4 Tait 3-edge-coloured quark-disjoint",
            variant,
            6,
            &free_4_vvvv,
            &w_tait,
            AME2020_B_4HE_MEV,
        ));
    }
    let w_chain4_vvvv = assemble_atom_word("vvvv", &chain4_bonds, "-");
    rows.push(eval_cell(
        &rep12,
        "4He",
        4,
        "bare_gg_V3",
        "vvvv",
        "chain control [(0,1),(1,2),(2,3)]",
        "-",
        3,
        &free_4_vvvv,
        &w_chain4_vvvv,
        AME2020_B_4HE_MEV,
    ));

    // Production typed ppnn on A = 4
    let free_4_ppnn = rep12
        .evaluate_word(&assemble_atom_word("ppnn", &[], "-"))
        .tr_m;
    for (r_name, r_bonds) in &k4_routes {
        for variant in ["over", "under"] {
            let w = assemble_atom_word("ppnn", r_bonds, variant);
            rows.push(eval_cell(
                &rep12,
                "4He",
                4,
                "typed_uud_udd",
                "ppnn",
                r_name,
                variant,
                6,
                &free_4_ppnn,
                &w,
                AME2020_B_4HE_MEV,
            ));
        }
    }
    let w_chain4_ppnn = assemble_atom_word("ppnn", &chain4_bonds, "-");
    rows.push(eval_cell(
        &rep12,
        "4He",
        4,
        "typed_uud_udd",
        "ppnn",
        "chain control [(0,1),(1,2),(2,3)]",
        "-",
        3,
        &free_4_ppnn,
        &w_chain4_ppnn,
        AME2020_B_4HE_MEV,
    ));

    rows
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn deuteron_bare_gg_v3_passes_reading3_and_binds() {
        let params = Q0Params::proton_pinned(320, None);
        let p = params.prec_bits;
        let rep6 = TwoRowTowerRep::new(&params, 6);
        let free = rep6.evaluate_word(&assemble_atom_word("vv", &[], "-"));
        let bound = rep6.evaluate_word(&assemble_atom_word("vv", &[(0, 1)], "-"));
        assert!(free.reading3_m1_to_n);
        assert!(bound.reading3_m1_to_n);
        let ratio = Float::with_val(p, &bound.tr_m / &free.tr_m);
        // Must match gg_deuteron_bond / ACCURACY.md Table 3.2a (r ≈ 0.998497160633, B_0 ≈ 6.296 keV, B_tower ≈ 6.358 keV)
        let expected_r = parse_dec(p, "0.998497160633");
        let diff = (ratio - &expected_r).abs();
        assert!(
            diff < parse_dec(p, "1e-11"),
            "unexpected 2H bare V(2)^3 ratio diff: {diff}"
        );
    }
}
