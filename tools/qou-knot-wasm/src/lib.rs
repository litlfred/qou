//! Browser-side WASM kernel for the Recursive Knot-Atlas Viewer.
//!
//! Exports a small surface used by `folio-assistant/simulators/
//! knot_atlas_viewer.html` for live `q`-slider recomputes:
//!
//!   - [`markov_closure`] — given a braid word in `H_n`, return a
//!     deterministic identifier of its Markov closure (knot id when
//!     recognisable, else a canonical string).
//!   - [`gb_normal_form`] — apply the small subset of GS-relations
//!     needed for the viewer's display (length-reducing rewrites in
//!     the free group, no Hecke-quadratic relations).
//!   - [`wedderburn_blocks`] — return the Wedderburn-block dimensions
//!     of `H_n(q)` for small `n` (n ≤ 6), a witness-driven static
//!     table; the kernel does NOT recompute these from `q`.
//!   - [`hp_volume_estimate`] — analytic fallback estimator for the
//!     hyperbolic volume of the closure of a braid word.  Returns
//!     `f64`; the simulator only uses this when the witness has no
//!     pre-computed value.
//!
//! All exported functions take JSON-serialisable inputs and return
//! JSON-serialisable outputs via `serde-wasm-bindgen`, so the JS side
//! sees plain values / objects.
//!
//! ## Strict no-hardcoded-QOU-values contract
//!
//! This kernel must not bake `q₀` or any other QOU substrate constant
//! into its code.  Any constant the kernel emits is either
//!   (a) a *topological* invariant (writhe, exponent sum, strand
//!       count) computed from the input braid word, or
//!   (b) a *witness-table* entry (Wedderburn dims for fixed `n`)
//!       whose justification lives in the corresponding witness JSON.

use serde::{Deserialize, Serialize};
use wasm_bindgen::prelude::*;

// ── Markov closure ──────────────────────────────────────────────

/// Result of a Markov-closure analysis.
#[derive(Serialize, Deserialize)]
pub struct ClosureInfo {
    /// Best-effort knot id (e.g. "0_1", "3_1", "B_3") when recognisable
    /// from the braid word's signature; else `null`.
    pub knot_id: Option<String>,
    /// Number of components of the closure (= cycles of the underlying
    /// permutation in S_n).
    pub n_components: u32,
    /// Exponent sum (writhe of the closure under standard convention).
    pub writhe: i32,
    /// Number of strands `n` (one more than the largest |σ_i| in the word).
    pub n_strands: u32,
}

fn permutation_from_word(word: &[i32], n: u32) -> Vec<u32> {
    let mut perm: Vec<u32> = (0..n).collect();
    for &g in word {
        let i = (g.unsigned_abs() - 1) as usize;
        if i + 1 < perm.len() {
            perm.swap(i, i + 1);
        }
    }
    perm
}

fn cycle_count(perm: &[u32]) -> u32 {
    let mut seen = vec![false; perm.len()];
    let mut cycles: u32 = 0;
    for i in 0..perm.len() {
        if seen[i] {
            continue;
        }
        cycles += 1;
        let mut j = i;
        while !seen[j] {
            seen[j] = true;
            j = perm[j] as usize;
        }
    }
    cycles
}

fn detect_knot_id(word: &[i32], n_strands: u32, _n_components: u32, writhe: i32) -> Option<String> {
    if word.is_empty() {
        return Some("0_1".to_string());
    }
    if n_strands == 2 && word.iter().all(|&g| g == 1) {
        return match word.len() {
            // n_strands == 2 with empty word is unreachable (early return
            // above), so the smallest case here is σ_1 → unknot.
            1 => Some("0_1".to_string()),
            2 => Some("L_H".to_string()),
            3 => Some("3_1".to_string()),
            5 => Some("5_1".to_string()),
            7 => Some("7_1".to_string()),
            _ => None,
        };
    }
    if n_strands == 3 && word.len() == 6 && writhe == 0 {
        let target: Vec<i32> = vec![1, -2, 1, -2, 1, -2];
        if word == target.as_slice() {
            return Some("B_3".to_string());
        }
    }
    if n_strands == 3 && word.len() == 4 && writhe == 0 {
        let target: Vec<i32> = vec![1, -2, 1, -2];
        if word == target.as_slice() {
            return Some("4_1".to_string());
        }
    }
    None
}

#[wasm_bindgen]
pub fn markov_closure(word_js: JsValue) -> Result<JsValue, JsValue> {
    let word: Vec<i32> = serde_wasm_bindgen::from_value(word_js)
        .map_err(|e| JsValue::from_str(&format!("invalid braid word: {e}")))?;
    let n_strands = word
        .iter()
        .map(|g| g.unsigned_abs())
        .max()
        .map(|m| m + 1)
        .unwrap_or(1);
    let perm = permutation_from_word(&word, n_strands);
    let n_components = cycle_count(&perm);
    let writhe: i32 = word.iter().map(|&g| g.signum()).sum();
    let info = ClosureInfo {
        knot_id: detect_knot_id(&word, n_strands, n_components, writhe),
        n_components,
        writhe,
        n_strands,
    };
    serde_wasm_bindgen::to_value(&info).map_err(|e| JsValue::from_str(&e.to_string()))
}

// ── GB normal form (length-reducing free-group rewrites) ───────

fn reduce_word(mut word: Vec<i32>) -> Vec<i32> {
    loop {
        let mut changed = false;
        let mut i = 0;
        while i + 1 < word.len() {
            if word[i] == -word[i + 1] {
                word.remove(i);
                word.remove(i);
                changed = true;
            } else {
                i += 1;
            }
        }
        if !changed {
            break;
        }
    }
    word
}

#[wasm_bindgen]
pub fn gb_normal_form(word_js: JsValue) -> Result<JsValue, JsValue> {
    let word: Vec<i32> = serde_wasm_bindgen::from_value(word_js)
        .map_err(|e| JsValue::from_str(&format!("invalid braid word: {e}")))?;
    let reduced = reduce_word(word);
    serde_wasm_bindgen::to_value(&reduced).map_err(|e| JsValue::from_str(&e.to_string()))
}

// ── Wedderburn-block dimensions (witness table for n ≤ 6) ──────

fn wedderburn_table(n: u32) -> Option<Vec<u32>> {
    match n {
        0 | 1 => Some(vec![1]),
        2 => Some(vec![1, 1]),
        3 => Some(vec![1, 2, 1]),
        4 => Some(vec![1, 3, 2, 3, 1]),
        5 => Some(vec![1, 4, 5, 6, 5, 4, 1]),
        6 => Some(vec![1, 5, 9, 5, 10, 16, 5, 10, 9, 5, 1]),
        _ => None,
    }
}

#[wasm_bindgen]
pub fn wedderburn_blocks(n: u32) -> Result<JsValue, JsValue> {
    match wedderburn_table(n) {
        Some(v) => serde_wasm_bindgen::to_value(&v).map_err(|e| JsValue::from_str(&e.to_string())),
        None => Err(JsValue::from_str(&format!(
            "wedderburn_blocks: n={n} not in table (supported: n ≤ 6)"
        ))),
    }
}

// ── Hyperbolic-volume estimator (analytic fallback) ────────────

#[wasm_bindgen]
pub fn hp_volume_estimate(word_js: JsValue) -> Result<f64, JsValue> {
    let word: Vec<i32> = serde_wasm_bindgen::from_value(word_js)
        .map_err(|e| JsValue::from_str(&format!("invalid braid word: {e}")))?;
    if word.is_empty() {
        return Ok(0.0);
    }
    let n_strands = word
        .iter()
        .map(|g| g.unsigned_abs())
        .max()
        .map(|m| m + 1)
        .unwrap_or(1);
    if n_strands <= 1 {
        return Ok(0.0);
    }
    if word.iter().all(|&g| g == word[0]) {
        return Ok(0.0);
    }
    const V_OCT: f64 = 3.66386237670887606;
    // V_OCT is the volume of the regular ideal hyperbolic octahedron —
    // a universal constant of hyperbolic 3-geometry, NOT a QOU
    // substrate parameter.  It appears as the natural unit for
    // analytic-fallback estimates of the volume of an alternating
    // link complement (Lackenby's bound).  Documented here so it is
    // not confused with the witness-only QOU values forbidden by the
    // module-level no-hardcoded-QOU-values contract.
    let len = word.len() as i32;
    let n = n_strands as i32;
    let est = V_OCT * (((len - n).max(0)) as f64);
    Ok(est)
}

// ── Version string ─────────────────────────────────────────────

#[wasm_bindgen]
pub fn version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

// ── Tests ──────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn closure_unknot_empty() {
        let perm = permutation_from_word(&[], 1);
        assert_eq!(cycle_count(&perm), 1);
    }

    #[test]
    fn closure_trefoil_signature() {
        let word = vec![1, 1, 1];
        let perm = permutation_from_word(&word, 2);
        assert_eq!(cycle_count(&perm), 1);
        let writhe: i32 = word.iter().map(|g| g.signum()).sum();
        assert_eq!(writhe, 3);
        assert_eq!(detect_knot_id(&word, 2, 1, 3), Some("3_1".into()));
    }

    #[test]
    fn closure_borromean_detected() {
        let word = vec![1, -2, 1, -2, 1, -2];
        let perm = permutation_from_word(&word, 3);
        assert_eq!(cycle_count(&perm), 3);
        let writhe: i32 = word.iter().map(|g| g.signum()).sum();
        assert_eq!(detect_knot_id(&word, 3, 3, writhe), Some("B_3".into()));
    }

    #[test]
    fn gb_nf_cancels_inverses() {
        assert_eq!(reduce_word(vec![1, 2, -2, 3]), vec![1, 3]);
        assert_eq!(reduce_word(vec![1, -1, 2, -2]), Vec::<i32>::new());
        assert_eq!(reduce_word(vec![1, 2, 3]), vec![1, 2, 3]);
    }

    #[test]
    fn wedderburn_n3_matches_partitions_of_3() {
        assert_eq!(wedderburn_table(3), Some(vec![1, 2, 1]));
    }
}
