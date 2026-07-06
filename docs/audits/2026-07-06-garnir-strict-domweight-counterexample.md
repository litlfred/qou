# Garnir straightening: the strict-`domWeight` dominance is FALSE — counterexample and reformulation sketch

**Date:** 2026-07-06
**Scope:** `content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtStandardBasisCore.lean`
— piece 2 (the Garnir coset-sum that closes `straightening_step_colMax`).
**Verdict:** the coset-sum *machinery* is proved sorry-free; the final *dominance*
step's naive formulation (`garnir_assembly`'s strict-`domWeight`-per-rep premise, and
by extension the framework's "each Garnir term strictly raises `domWeight`") is
**mathematically false**. This doc records the verified counterexample and sketches the
partial-order reformulation.

## 1. What is proved (sorry-free, `lean`-direct exit 0)

The entire algebraic + annihilation + reindexing half of the Garnir relation:

| lemma | content |
|---|---|
| `card_col_labels`, `card_col_labels_row_lt_of_le` | column label counts |
| `garnir_row_collision` | the pigeonhole (`|A|+|B| = colLen j + 1`) → same-row `(a∈A,b∈B)` collision |
| `garnir_full_annihilation` | `∑_{σ∈S_{A∪B}} sgn(σ)·(σ·e_t) = 0` |
| `sum_sign_rep_polytabloid_eq_zero_of_family` | rep-level annihilation ⟸ tabloid family |
| `sum_sign_rep_coset_collapse`, `transversal_sum_eq_zero` | `|S_A×S_B|` cancellation over `CharZero` |
| `garnirGSub`/`garnirHSub`, `*_coe`, `garnir_transversal_exists` | subgroups + left transversal (via `Subgroup.exists_left_transversal_of_le`) |
| `sum_over_garnirG_reindex` | Finset reindex `∑_G = ∑_T ∑_H` |
| `garnir_assembly` | isolate a sign-fixing `π₀ ∈ T`, reduce `e_t` to the other reps |

These compose: `garnir_full_annihilation → sum_over_garnirG_reindex → transversal_sum_eq_zero`
gives `∑_{π∈T} sgn(π)·(π·e_t) = 0`, and `garnir_assembly` isolates `e_t`. **The only
missing input is the dominance hypothesis `hdom`** — and that hypothesis is false.

## 2. The counterexample (verified)

`garnir_assembly` requires: for every non-identity transversal rep `π`,
`domWeight t < domWeight (π•t)` (strict). Take the Garnir set at the row descent
`(i,j),(i,j+1) ∈ μ` with `labelAt t (i,j+1) ≤ labelAt t (i,j)`:

- `A = {labels in col j, row ≥ i}`, `B = {labels in col j+1, row ≤ i}`.
- The **row-`i` overlap is essential**: it is exactly what makes
  `|A| + |B| = (colLen j − i) + (i+1) = colLen j + 1 > colLen j`, the strict inequality
  the pigeonhole (`garnir_row_collision`) needs.
- But then `a := labelAt t (i,j)` and `b := labelAt t (i,j+1)` are **both in row `i`**,
  and `π := Equiv.swap a b` satisfies:
  - `π ∈ garnirG` (fixes everything outside `A ∪ B`; `a∈A`, `b∈B`);
  - `π ∉ colStab t` (it moves `a` to column `j+1` and `b` to column `j`), so `π ∉ H`
    (`= garnirG ∩ colStab`) — a **non-identity coset element**;
  - `rowPattern (π•t) = rowPattern t` (both labels stay in row `i`), so
    **`domWeight (π•t) = domWeight t`** — not `>`;
  - `{π•t} = {t}` (same tabloid), so **no representative of that coset strictly
    dominates** `t`.

Hence `hdom` is unsatisfiable for *any* transversal, and the same-tabloid coset feeds
the coefficient of `e_t` **itself** (its leading tabloid is `{t}`, like `e_t`'s).

## 3. Why `garnir_assembly`'s shape is wrong

`garnir_assembly` assumes the Garnir relation has the form
`e_t = ∑_{π ≠ π₀} c_π · e_{π•t}` with every `e_{π•t}` strictly more dominant. The truth
is `(1 + κ)·e_t = (strictly-dominant terms)` where `κ` collects the same-tabloid cosets:
the correct straightening solves for `e_t` after absorbing those, using the **partial
dominance order + sign cancellation**, not a strict linear measure. `domWeight` (a strict
linear extension) cannot see the tie, so `domWeight`-strict induction cannot drive it.

This is not specific to `garnir_assembly`: the pre-existing `straightening_step` /
`standardPolytabloid_straightening` also carry the strict-`domWeight` shape (induction on
`domBound μ − domWeight t`), which the counterexample suggests needs the same rework.

## 4. Reformulation sketch (options)

**Option A — lexicographic measure `(domWeight, secondary)`.**
Add a secondary tie-breaker `sec t` (e.g. a count of within-row inversions of the
column-word) and induct on `(domBound − domWeight t, sec t)` lexicographically. Each
Garnir term then either (i) strictly raises `domWeight` (the genuinely-dominant cosets),
or (ii) ties `domWeight` and strictly lowers `sec` (the same-tabloid cosets, which fix a
local row-descent). *Cost:* one must pick the transversal so that the same-tabloid reps
provably lower `sec` — i.e. the classical **shuffle transversal** (reps increasing on `A`
and on `B`), not Mathlib's arbitrary `exists_left_transversal_of_le` output, plus a proof
that shuffle reps decrease the lex measure. This is the genuine combinatorial crux.

**Option B — James's route (avoid straightening-by-domWeight entirely).**
Prove the standard basis theorem via unitriangularity: (a) standard polytabloids are
linearly independent because `e_s` has *leading tabloid* `{s}` in the dominance order and
distinct standard `s` have distinct `{s}`; (b) they span by a dimension/counting argument
against `numSYT`, using the Garnir relations only to bound, not to strictly decrease. The
module docstring already gestures at this ("independence via the dominance/last-letter
order"). This sidesteps the strict-`domWeight` induction but needs the leading-term
machinery.

**Recommendation.** Option A is closest to the existing scaffolding (keep `domWeight`,
add `sec`, build the shuffle transversal). Option B is cleaner mathematically but further
from the current code. Either way the residual is the **shuffle transversal + its
dominance/tie-decrease proof** — the part Mathlib does not provide (no Specht modules in
Mathlib at all).

## 5. Concrete next steps

1. Replace `garnir_transversal_exists` (arbitrary transversal) with a **shuffle
   transversal** constructed from order-preserving bijections `A ≃ σ(A)`, `B ≃ σ(B)`.
2. Define `sec t` and prove the lex-decrease for shuffle reps (Option A), or the
   leading-tabloid lemma (Option B).
3. Re-shape `garnir_assembly` to the `(1+κ)·e_t = dominant` form (absorb same-tabloid
   cosets), and rework `straightening_step` / `standardPolytabloid_straightening` onto the
   lex measure.

The roadmap comment on `straightening_step_colMax` carries a condensed version of §2–§3
so the next pass does not re-wire the false `hdom`.

## References
- Sagan, *The Symmetric Group*, §2.6 (Garnir relations / straightening).
- James, *The Representation Theory of the Symmetric Groups*, §8 (standard basis).
