//! Whole-word linking-neutrality cut (`QOU/StandardModel/PhotonU1NeutralCut.lean`).
//!
//! For a signed Artin braid word $w$ on $n \ge 2$ strands:
//! 1. Closing top strand position $k$ to bottom strand position $k$ decomposes $\{0, \dots, n-1\}$
//!    into connected link components $C_0, \dots, C_{c-1}$.
//! 2. Each crossing $\sigma_i^{\varepsilon}$ ($\varepsilon \in \{+1, -1\}$) between the strands
//!    currently at positions $(i, i+1)$ contributes $\varepsilon$ to the unordered component pair
//!    $\{\operatorname{comp}(p_i), \operatorname{comp}(p_{i+1})\}$:
//!    - when the two strands belong to the **same** closure component ($a = b$), this accumulates
//!      component self-writhe;
//!    - when they belong to **distinct** components ($a \ne b$), this accumulates twice the
//!      Gauss linking number $2\,\operatorname{lk}(C_a, C_b)$.
//! 3. A word $w$ is **linking-neutral** (`is_linking_neutral` / `is_u1_neutral`, matching
//!    `PhotonU1NeutralCut.Neutral` and the 2026-11-22 owner wording ruling) iff every self-writhe
//!    and every pairwise linking count vanishes. Linking neutrality implies $\operatorname{writhe}(w) = 0$
//!    and is strictly stronger.

use crate::photon::BraidWord;

/// Compute the connected link components of the standard braid closure of `word` on `num_strands`
/// strands. Each component is returned as a sorted list of initial strand labels in `0..num_strands`,
/// and components are ordered by their smallest strand label.
pub fn closure_components(word: &BraidWord, num_strands: usize) -> Vec<Vec<usize>> {
    assert!(num_strands >= 1, "num_strands must be >= 1");
    // Track `pos[k]` = initial strand label currently sitting at position `k`:
    let mut pos: Vec<usize> = (0..num_strands).collect();
    for c in word.crossings() {
        assert!(
            c.gen + 1 < num_strands,
            "crossing generator {} out of range for {} strands",
            c.gen,
            num_strands
        );
        pos.swap(c.gen, c.gen + 1);
    }

    // `step[x]` = final position where initial strand label `x` ends up:
    let mut step = vec![0usize; num_strands];
    for (final_idx, &label) in pos.iter().enumerate() {
        step[label] = final_idx;
    }

    let mut visited = vec![false; num_strands];
    let mut components = Vec::new();
    for start in 0..num_strands {
        if visited[start] {
            continue;
        }
        let mut cycle = Vec::new();
        let mut cur = start;
        while !visited[cur] {
            visited[cur] = true;
            cycle.push(cur);
            cur = step[cur];
        }
        cycle.sort_unstable();
        components.push(cycle);
    }
    components
}

/// Compute `(num_components, self_writhes, twice_pairwise_linkings)` for `word` on `num_strands` strands.
fn component_crossing_ledger(
    word: &BraidWord,
    num_strands: usize,
) -> (usize, Vec<i64>, Vec<Vec<i64>>) {
    let comps = closure_components(word, num_strands);
    let k = comps.len();
    let mut comp_of_label = vec![0usize; num_strands];
    for (cid, members) in comps.iter().enumerate() {
        for &lbl in members {
            comp_of_label[lbl] = cid;
        }
    }

    let mut self_w = vec![0i64; k];
    let mut link2 = vec![vec![0i64; k]; k];
    let mut pos: Vec<usize> = (0..num_strands).collect();

    for c in word.crossings() {
        let a_lbl = pos[c.gen];
        let b_lbl = pos[c.gen + 1];
        let ca = comp_of_label[a_lbl];
        let cb = comp_of_label[b_lbl];
        let eps = c.sign as i64;
        if ca == cb {
            self_w[ca] += eps;
        } else {
            link2[ca][cb] += eps;
            link2[cb][ca] += eps;
        }
        pos.swap(c.gen, c.gen + 1);
    }

    (k, self_w, link2)
}

/// Signed self-writhe of each closure component of `word` (ordered as in [`closure_components`]).
pub fn self_writhes(word: &BraidWord, num_strands: usize) -> Vec<i64> {
    component_crossing_ledger(word, num_strands).1
}

/// Symmetric $k \times k$ matrix of $2\,\operatorname{lk}(C_a, C_b)$ (off-diagonal; `0` on diagonal)
/// across the closure components of `word`.
pub fn pairwise_linkings_twice(word: &BraidWord, num_strands: usize) -> Vec<Vec<i64>> {
    component_crossing_ledger(word, num_strands).2
}

/// Signed crossing sum `cnt(w, c_a, c_b)` matching `PhotonU1NeutralCut.cnt` (equals `self_writhes[c_a]`
/// when `c_a == c_b` and `pairwise_linkings_twice[c_a][c_b]` when `c_a != c_b`).
pub fn component_pair_count(
    word: &BraidWord,
    num_strands: usize,
    comp_a: usize,
    comp_b: usize,
) -> i64 {
    let (_, sw, lk2) = component_crossing_ledger(word, num_strands);
    if comp_a == comp_b {
        sw[comp_a]
    } else {
        lk2[comp_a][comp_b]
    }
}

/// Total algebraic writhe $\sum \varepsilon_t$ of `word`.
pub fn writhe(word: &BraidWord) -> i64 {
    word.crossings().iter().map(|c| c.sign as i64).sum()
}

/// Whole-word linking neutrality (`PhotonU1NeutralCut.Neutral`; 2026-11-22 owner ruling):
/// returns `true` iff every component self-writhe and every pairwise linking number vanishes.
pub fn is_linking_neutral(word: &BraidWord, num_strands: usize) -> bool {
    let (k, sw, lk2) = component_crossing_ledger(word, num_strands);
    if sw.iter().any(|&w| w != 0) {
        return false;
    }
    for a in 0..k {
        for b in (a + 1)..k {
            if lk2[a][b] != 0 {
                return false;
            }
        }
    }
    true
}

/// Alias of [`is_linking_neutral`] matching the Lean identifier `PhotonU1NeutralCut.Neutral`.
pub fn is_u1_neutral(word: &BraidWord, num_strands: usize) -> bool {
    is_linking_neutral(word, num_strands)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn photon_u1_neutral_cut_lean_table_and_theorems() {
        // Exact verification of `PhotonU1NeutralCut.table`, `hopf_not_neutral`, and
        // `writhe_eq_zero_of_neutral` on 3 strands:
        let s0 = BraidWord::sigma(0);
        let s1 = BraidWord::sigma(1);
        let v = BraidWord::vertex_v(0);

        // Single-photon non-identity terms:
        assert!(!is_u1_neutral(&s0, 3));
        assert!(!is_u1_neutral(&s1, 3));
        assert!(is_u1_neutral(&v, 3));

        // Remaining two-photon words:
        let s0_s0 = s0.concat(&s0); // Hopf link!
        let s0_s1 = s0.concat(&s1);
        let s1_s0 = s1.concat(&s0);
        let s1_s1 = s1.concat(&s1);
        let s0_v = s0.concat(&v);
        let v_s0 = v.concat(&s0);
        let s1_v = s1.concat(&v);
        let v_s1 = v.concat(&s1);
        let v2 = v.concat(&v);
        let v3 = v2.concat(&v); // Borromean rings beta_Bor!

        assert!(!is_u1_neutral(&s0_s0, 3)); // `hopf_not_neutral`
        assert!(!is_u1_neutral(&s0_s1, 3));
        assert!(!is_u1_neutral(&s1_s0, 3));
        assert!(!is_u1_neutral(&s1_s1, 3));
        assert!(!is_u1_neutral(&s0_v, 3));
        assert!(!is_u1_neutral(&v_s0, 3));
        assert!(!is_u1_neutral(&s1_v, 3));
        assert!(!is_u1_neutral(&v_s1, 3));

        // Only V and V^2 pass among the 12 non-identity two-photon words, and V^3 passes!
        assert!(is_u1_neutral(&v2, 3));
        assert!(is_u1_neutral(&v3, 3));

        // Borromean rings have 3 unlinked components (all pairwise lk = 0, self-writhe = 0):
        assert_eq!(closure_components(&v3, 3).len(), 3);
        assert_eq!(writhe(&v), 0);
        assert_eq!(writhe(&v2), 0);
        assert_eq!(writhe(&v3), 0);

        // Writhe-zero does NOT imply linking neutrality: e.g. sigma_0^2 sigma_1^{-2} has writhe 0
        // but non-zero linking!
        let writhe_zero_linked = BraidWord::from_pairs(&[(0, 1), (0, 1), (1, -1), (1, -1)]);
        assert_eq!(writhe(&writhe_zero_linked), 0);
        assert!(!is_u1_neutral(&writhe_zero_linked, 3));
    }
}
