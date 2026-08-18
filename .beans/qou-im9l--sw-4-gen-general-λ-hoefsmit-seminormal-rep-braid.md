---
# qou-im9l
title: 'SW-4-gen: general-λ Hoefsmit seminormal rep + braid (Yang-Baxter/axial-distance) — the residual sorry in HoefsmitRep.lean'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T20:13:08Z
updated_at: 2026-08-18T18:11:08Z
parent: qou-59vq
blocked_by:
    - qou-rsbf
---

Discharge the one Ref'd sorry in HoefsmitRep.lean (hoefsmit_seminormal_rep): SYT-indexed orthonormal basis of S^λ, block-diagonal (over s_i-orbits) seminormal matrices with axialDistance rational entries (generalizing S1 from the (2,1) case), and the braid relation for arbitrary λ (Hoefsmit's Yang-Baxter identity across 3 consecutive entries). This is the hard core; the (2,1) 2×2 braid is already proved sorry-free as the template. Ref: [hoefsmit1974], [ram1997].

## Construction roadmap (2026-08-10) — research-grade, multi-session

Assessed after landing the concrete (2,1) case (SW-4) + the n=3 dim-infra.
This is Hoefsmit's thesis theorem (general seminormal form), NOT a plumbing
task. Precise construction:

1. **SYT basis of S^λ.** Reuse `QOU.SchurWeyl.dLambda` / the in-repo
   `QOU.Mathlib.StandardYoungTableau` (SW-2). Index a free ℝ-module by `SYT λ`.
2. **Axial-distance data.** `cellContent`, `axialDistance` already exist
   (HoefsmitRep.lean, SW-4, sorry-free). For a SYT `t` and generator `σ_i`,
   let `d = axialDistance` between the cells of `i`, `i+1` in `t`.
3. **Seminormal matrices.** σ_i acts block-diagonally over the `s_i`-orbits of
   `SYT λ` (orbits are size 1 — `i,i+1` in same row/col, σ_i scalar `q`/`-q⁻¹`;
   or size 2 — the 2×2 axial-distance block generalizing S1 from the (2,1) case:
   diagonal `1/[d]`-type, off-diagonal the square-root-free entries realized for (2,1)).
4. **Relations.** Quadratic + far-commutation are per-block (reuse (2,1) template).
   The **braid relation for arbitrary λ** is the hard core: the Yang–Baxter /
   axial-distance identity across three consecutive entries i,i+1,i+2 — case
   analysis on their relative SYT positions. This is the multi-session piece.
5. **Assemble** via `Hecke.lift` (as `seminormalRep21` does) → `ρ_λ`.

Then SW-5-gen (irreducibility, general λ) and the general Wedderburn iso follow.
Ref: [hoefsmit1974] (thesis), [ram1997] (axial-distance formulas), [wenzl1988].
Honest scope: research project, not a one-session grind. Concrete (2,1) template
is in HoefsmitRep.lean/Irreducibility.lean/BurnsideSpan.lean as the pattern to generalize.


## Claimed 2026-08-18 — the roadmap's hard core is DONE; two gaps remain

The bean's item-4 "multi-session piece" (the braid relation for arbitrary λ,
the Yang-Baxter / axial-distance identity across three consecutive entries) is
**proved and merged** — `SeminormalRep.genMat_braid`, unconditionally on all of
`SYT μ`, dispatching over every orbit shape, alongside `genMat_quadratic` and
`genMat_far_comm`, packaged as the algebra map `SeminormalRep.seminormalRep`
(PR #5076, merged 0026a0e636). Items 1, 2, 3 and 5 of the roadmap are likewise
done.

**So this bean is no longer research-grade.** What separates `seminormalRep`
from the `hoefsmit_seminormal_rep` statement is exactly two things:

1. **Reindexing.** `seminormalRep` is indexed by `StandardYoungTableau μ`; the
   statement wants `Fin (dLambda lam)`. `dLambda` is *defined* as
   `Fintype.card (SYT lam)`, so this is `Fintype.equivFin` +
   `Matrix.reindexAlgEquiv`. Watch the `N = 0` edge: `N - 1` is ℕ-subtraction,
   so `μ.cells.card = n + 1` needs `N ≥ 1` and `N = 0` needs its own witness
   (the payload is vacuous there since `dLambda = 1`).
2. **Non-scalarity at `dLambda ≥ 2`** (bean SW-5). `genMat_ne_scalar` already
   gives it for any generator that MOVES some tableau, with no hypothesis on
   `q`. The missing step is that `#SYT μ ≥ 2` forces some generator to move
   some tableau.

**Planned route for (2), stated before attempting so it can be checked:**
`#SYT μ ≥ 2` implies μ is neither a single row nor a single column (both have
exactly one SYT), so μ has ≥ 2 rows and ≥ 2 columns. In the row-reading tableau
the entry `λ₁` sits at `(0, λ₁-1)` and `λ₁+1` at `(1, 0)`; with `λ₁ ≥ 2` those
cells differ in BOTH coordinates, which is `SwapAdmissible` at `k = λ₁`.
NOT claimed: that an arbitrary SYT admits an admissible k at an obvious index —
the `(2,1)` case shows the witness index depends on the tableau. The
construction picks a specific tableau on purpose.

**Hypothesis note.** Both `seminormalRep` and `hoefsmit_seminormal_rep` take
`q ≠ 0` and `q ^ 2 ≠ 1` — over ℝ exactly "not a root of unity" — so there is
NO hypothesis mismatch between them. An earlier note of mine said the
construction needs `0 < q ∧ q ≠ 1`; that was my misreading and it admits
negative q. See the correction commit on #5076.


## SW-5 CLOSED, and gap (i) is NOT mechanical — correcting my own claim (2026-08-18)

**Landed, sorry-free and axiom-clean** (`QOU/SchurWeyl/SytAdmissible.lean`, 7 theorems, PR #5266):
`exists_swapAdmissible_of_one_lt_card` — a shape with `#SYT μ ≥ 2` has a tableau admitting an
adjacent swap. That is gap (ii) / bean SW-5, and it is the substantive half.

**The route was not the one I wrote into this bean before starting.** I planned the geometric
argument (two rows + two columns ⇒ the row-reading tableau is admissible where row 0 ends). That
needs a proof that a single row/column has exactly one SYT *and* an explicit construction of a
standard tableau. Neither is needed: run the contradiction on the anti-diagonal `i + j` instead. An
inadmissible step shares a row or a column, so `sameRow_adjacent` / `sameCol_adjacent` make the
cells adjacent and `i + j` rises by exactly one; a tableau admissible nowhere therefore has
`entry i j = i + j + 1`, a filling forced by the shape alone, so two such tableaux are equal.
No shape classification, no tableau constructed.

## 🔻 Gap (i) is NOT mechanical. I said it was, twice, and it is wrong.

This bean's claim above — *"this is `Fintype.equivFin` + `Matrix.reindexAlgEquiv`"* — and the same
word in PR #5076's body (*"Mechanical."*) are both **wrong**, and not by a little. The reindexing
step itself is indeed two lines. Its **precondition** is not.

`seminormalRep` takes `(hN : μ.cells.card = n + 1)`. With `μ = partitionShape lam` and
`n = N - 1` that is `(partitionShape lam).cells.card = N` — the statement that a partition's Young
diagram has as many cells as the partition has units. **The pinned Mathlib does not have it.**
Measured, not assumed — probed against the actual olean tree:

| probed | result |
|---|---|
| `YoungDiagram.card_ofRowLens`, `card_eq_sum`, `card_cells_ofRowLens`, `ofRowLens_card`, `rowLens_sum_eq_card`, `sum_rowLens_eq_card`, `card_eq_rowLens_sum` | **all unknown constants** |
| `example (μ : YoungDiagram) : μ.cells.card = μ.rowLens.sum := by exact?` | **`exact?` could not close the goal** |
| present and usable | `rowLens_ofRowLens_eq_self` (needs `∀ x ∈ w, 0 < x` — `Nat.Partition.parts_pos` supplies it), `length_rowLens`, `get_rowLens`, `Nat.Partition.parts_sum`, `Matrix.reindexAlgEquiv`, `Fintype.equivFin` |

So closing gap (i) means first proving a **Young-diagram cardinality lemma that does not exist
upstream**: decompose `μ.cells` over its rows, `Finset.card_biUnion` with row-disjointness to get
`∑_{i < colLen 0} rowLen i`, reconcile that sum with `μ.rowLens.sum` via `length_rowLens` /
`get_rowLens`, then `rowLens_ofRowLens_eq_self` + `Multiset.sort` + `parts_sum` to land on `N`.
That is its own multi-lemma task, in Young-diagram plumbing rather than seminormal theory.

**Also needed for the `N = 0` edge**, and cheap once the above exists: `μ.cells.card = 0` gives
`Subsingleton (StandardYoungTableau μ)` (via `syt_ext_on_cells`, vacuously), hence
`dLambda ≤ 1`, which contradicts the `2 ≤ dLambda` payload — necessary because `Fin (N - 1)` is
empty at `N = 0` so the conclusion's `∃ i` is otherwise unprovable.

**Status: gap (ii) closed and merged-ready; gap (i) open, and larger than advertised.** Nothing here
claims `hoefsmit_seminormal_rep` is close to discharge — the remaining step is a real missing lemma,
not plumbing, and calling it mechanical twice is exactly the kind of under-estimate this bean should
not repeat a third time.
