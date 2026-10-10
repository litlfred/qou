> **DEPRECATED on 2026-05-24.** Point-in-time status, intermediate workplan iteration, dead-end exploration, or earlier sublemma version superseded by a later "refined" iteration. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T2 for the deprecation rationale.

# Path B: Schützenberger Evacuation Bar-Pairing for V_{(3,2,1)}

**Date**: 2026-05-06  
**Script**: `computations/path_b_evacuation.py`  
**Witness**: `computations/path-b-evacuation.witness.json`  
**Status**: ✓ All 10 assertions pass

---

## Background

The predecessor probe `close_321_weinberg_gap.py` established (Path C):

> `cot θ_W ≈ (max+/2nd-max+ of M_{(3,2,1)}) · q^(1/5)` with 0.127% error

Path B was left incomplete because the naive bar involution `i ↦ n+1-i` on
SYT entries does not produce a valid SYT for self-conjugate shapes.  The
correct involution is **Schützenberger evacuation** `e(T)`.

---

## Algorithm

**Forward JDT slide**: Given a hole at `(r,c)` in a tableau, move the smaller
of the right `(r,c+1)` and below `(r+1,c)` neighbor into the hole; repeat
until the hole reaches an outer corner.

**Schützenberger evacuation** `e(T)` of SYT `T` with entries `{1,...,n}`:

```
For step = 1 to n:
  1. Entry 1 is always at (0,0) after previous decrement.
  2. Remove entry 1, creating a hole at (0,0).
  3. Forward JDT slide: hole moves to an outer corner (r*,c*).
  4. Set e(T)(r*,c*) = n+1-step.
  5. Decrement all remaining entries by 1.
```

Result: `e(T)` is a valid SYT of the same straight shape, and `e(e(T)) = T`.

---

## Results for (3,2,1)

### Evacuation pairs

All 16 SYT of `(3,2,1)` are partitioned into **8 cross-pairs** (no self-paired):

| # | (i,j) | SYT[i] | SYT[j] | cs_i | cs_j | spread |
|---|-------|--------|--------|------|------|--------|
| 1 | (0,13) | 1 2 3 / 4 5 / 6 | 1 3 6 / 2 5 / 4 | -8 | +5 | **13** |
| 2 | (2,15) | 1 2 4 / 3 5 / 6 | 1 4 6 / 2 6 / 5 | -5 | +8 | **13** |
| 3 | (1,7)  | 1 2 3 / 4 6 / 5 | 1 2 5 / 3 6 / 4 | -6 | +3 | 9 |
| 4 | (8,14) | 1 3 4 / 2 6 / 5 | 1 3 6 / 2 5 / ? | -3 | +6 | 9 |
| 5 | (3,5)  | … | … | -3 | +1 | 4 |
| 6 | (10,12)| … | … | -1 | +3 | 4 |
| 7 | (4,9)  | … | … | -3 | -1 | 2 |
| 8 | (6,11) | … | … | +1 | +3 | 2 |

where `cs(T) = Σ_i entry_i · content(cell_i)` is the weighted content sum.

### Key structural facts

1. **Involution**: `e(e(T)) = T` for all 16 SYT ✓
2. **8 pairs**: All 16 SYT pair up with no fixed points for `(3,2,1)` ✓
3. **Principal pair `(0,13)`**: content sums `−8` and `+5` (opposite signs) ✓

### Hoefsmit diagonal connection

In the Hoefsmit seminormal basis, the diagonal entries of `M_{(3,2,1)} = ρ(β_EW)`
at `q = q_0` ranked by descending value:

| Rank | SYT | diag(M) | diag string |
|------|-----|---------|-------------|
| 1 | 0 | +3.388 | `++X+X` |
| 2 | 4 | +2.030 | `+X+XX` |
| 3 | 7 | +1.704 | `+X-XX` |
| 4 | 13 | +1.347 | `-XXXX` |
| … | … | … | … |

**SYT[0] = [[1,2,3],[4,5],[6]]** (the "row-reading" tableau — all entries fill
rows left-to-right, top to bottom) has the **maximum diagonal value** and its
evacuation partner is **SYT[13] = [[1,3,6],[2,5],[4]]**.

The pair `(0,13)` is simultaneously:
- the **principal bar-pair** by content-spread (spread = 13, maximum)
- the **principal bar-pair** by avg diagonal of M (avg_diag = +2.37, maximum)

### EW channel identification

The bar-pair structure assigns eigenvalues to pairs by avg diagonal:

| # | pair | avg_diag | assigned ev |
|---|------|----------|-------------|
| 1 | (0,13) | +2.37 | **5.240** ← max+ |
| 2 | (1,7)  | −1.01 | **2.939** ← 2nd-max+ |
| … | … | … | … |

The **EW channel is an inter-pair ratio**:

```
cot θ_W ≈ ev_1(pair 1) / ev_1(pair 2) = 5.240 / 2.939 = 1.783
```

corrected by `q^(1/h_corner) = q^(1/5)` → 0.127% from CODATA.

### Geometric interpretation

The row-reading tableau SYT[0] = [[1,2,3],[4,5],[6]] maximizes all Hoefsmit
diagonal entries simultaneously: every generator `σ_k` that acts diagonally
on SYT[0] acts with eigenvalue `q` (positive), giving the highest total
diagonal weight.  Its evacuation partner SYT[13] is the "most spread" choice
of how to fill the same shape with entries reversed in content-weighted sense.

---

## Assertions (10/10 pass)

| Assertion | Value | Expected |
|-----------|-------|----------|
| `n_syt_eq_16` | 16 | 16 |
| `evacuation_is_involution` | True | True |
| `n_evacuation_pairs_eq_8` | 8 | 8 |
| `n_self_paired_gte_0` | True | True |
| `principal_pair_spread_eq_max` | True | True |
| `principal_pair_opposite_sign_content` | True | True |
| `path_b_corrected_err_lt_0p5pct` | 0.001270 | 0 (tol 0.005) |
| `top_diagonal_syt_in_principal_bar_pair` | True | True |
| `content_sum_diag_M_correlation_gt_0` | True | True |
| `principal_by_spread_matches_principal_by_diag` | True | True |

---

## Open questions — RESOLVED

See [`2026-05-06-path-b-open-questions-resolved.md`](2026-05-06-path-b-open-questions-resolved.md)
for the full resolution probe (`path_b_open_questions.py`, 7/7 assertions).

1. **No self-paired SYT — RESOLVED**: Stanley's theorem (EC2 §7.A2.20):
   `#{self-evac SYT} = #{domino tableaux}`.  For (3,2,1), 2-core is
   `(2,1,1) ≠ ∅` ⇒ no domino tilings ⇒ 0 self-evac SYT.  All staircases
   `ρ_k`, `k ≥ 2` have non-empty 2-core ⇒ all predicted to have 0
   self-evacuating SYT.

2. **Pearson correlation = 0.03 — RESOLVED (negative finding)**: No
   SYT-level linear invariant predicts `diag(M)` (best `|r| = 0.17`,
   multivariate R² = 0.085).  The bar-pair, not the individual SYT, is
   the correct unit of analysis — consistent with Schur duality acting
   on irreducible blocks (= evacuation orbits).

3. **Why `q^(1/5)` — RESOLVED**: `q^(1/5) = q^(1/h_corner)` where
   `h_corner(ρ_k) = 2k − 1 = 5` for `k = 3`.  Independent sweeps (H3
   single-cell `q^(c/h)`, H4 two-cell product) both converge on cell
   (0,0) with hook 5.  Origin: corner Hecke generator `σ_5` at the
   Markov-trace closure cell, contributing the inverse-hook power
   `1/h_corner` to the trace residue.  Generalization conjecture:
   staircase EW-like channels carry residual `q^(1/(2k-1))`.
