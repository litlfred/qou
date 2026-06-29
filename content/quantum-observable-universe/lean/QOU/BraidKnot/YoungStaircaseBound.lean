import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.YoungStaircaseBound — the conjugate-marginal staircase bound

The combinatorial heart of the Specht-module sign lemma (James §4 / Sagan §2.4.3),
isolated as a self-contained, representation-theory-free statement.

**Main result** (`young_staircase_bound`): if two functions `f g : Fin n → ℕ`
(think `f = ` the row of label `m` in a tableau `s`, `g = ` the column of `m` in a
tableau `t`) are *jointly injective* and have the marginals of a Young diagram
`μ` — each row `i` of `μ` is hit `μ.rowLen i` times by `f` — then every pair
`(f m, g m)` lies in `μ`.

The proof is a clean extremality / counting argument (no Hall's theorem):
`∑ₘ g m` equals both the cell-column-sum of `μ` (`= ∑ᵢ Σ_{k<rowLenᵢ} k`, the
minimum) and `∑ᵢ (sum of the distinct columns used in row i)` (each `≥` that same
minimum). Equality forces each row's column-set to be the initial segment
`{0,…,rowLenᵢ−1}`, i.e. `(f m, g m) ∈ μ`.

This file imports only `QOU.BraidKnot.Specht` (for the ambient Mathlib surface);
its results are pure `Finset`/`YoungDiagram` combinatorics.
-/

open scoped BigOperators
open Finset

namespace QOU.BraidKnot.YoungStaircaseBound

/-! ## 1. The distinct-naturals sum bound

A finite set of `k` naturals has sum `≥ 0+1+⋯+(k−1)`, with equality iff the set is
exactly `{0,…,k−1}`. -/

/-- A strictly monotone `Fin n → ℕ` dominates the identity: `i ≤ f i`. -/
theorem strictMono_fin_nat_le {n : ℕ} {f : Fin n → ℕ} (hf : StrictMono f) :
    ∀ (k : ℕ) (hk : k < n), k ≤ f ⟨k, hk⟩ := by
  intro k
  induction k with
  | zero => intro _; exact Nat.zero_le _
  | succ m ih =>
    intro hk
    have hm : m < n := Nat.lt_of_succ_lt hk
    have h2 : f ⟨m, hm⟩ < f ⟨m + 1, hk⟩ := hf (Fin.mk_lt_mk.2 (Nat.lt_succ_self m))
    have := ih hm
    omega

/-- The `i`-th smallest element of `s` is `≥ i`. -/
theorem le_orderEmbOfFin (s : Finset ℕ) (i : Fin s.card) :
    (i : ℕ) ≤ s.orderEmbOfFin rfl i := by
  have h := strictMono_fin_nat_le (s.orderEmbOfFin rfl).strictMono i.val i.isLt
  simpa using h

/-- Reindex a sum over `s ⊆ ℕ` by the increasing enumeration. -/
theorem sum_eq_orderEmb (s : Finset ℕ) :
    ∑ x ∈ s, x = ∑ i : Fin s.card, s.orderEmbOfFin rfl i := by
  conv_lhs => rw [← image_orderEmbOfFin_univ s rfl]
  rw [Finset.sum_image (fun a _ b _ h => (s.orderEmbOfFin rfl).injective h)]

/-- **Distinct-nat sum lower bound.** -/
theorem sum_range_card_le (s : Finset ℕ) :
    ∑ i ∈ Finset.range s.card, i ≤ ∑ x ∈ s, x := by
  rw [sum_eq_orderEmb s, ← Fin.sum_univ_eq_sum_range (fun i => i) s.card]
  exact Finset.sum_le_sum (fun i _ => le_orderEmbOfFin s i)

/-- **Distinct-nat sum equality case.** If the sum is the minimum, the set is the
initial segment `{0,…,card−1}`. -/
theorem eq_range_of_sum_eq (s : Finset ℕ)
    (h : ∑ x ∈ s, x = ∑ i ∈ Finset.range s.card, i) :
    s = Finset.range s.card := by
  rw [sum_eq_orderEmb s, ← Fin.sum_univ_eq_sum_range (fun i => i) s.card] at h
  -- termwise: orderEmbOfFin i = i
  have hpt : ∀ i : Fin s.card, s.orderEmbOfFin rfl i = (i : ℕ) := by
    have hle : ∀ i ∈ (Finset.univ : Finset (Fin s.card)), (i : ℕ) ≤ s.orderEmbOfFin rfl i :=
      fun i _ => le_orderEmbOfFin s i
    have heq := (Finset.sum_eq_sum_iff_of_le hle).1 h.symm
    exact fun i => (heq i (Finset.mem_univ i)).symm
  -- s = range card: x ∈ s ↔ x ∈ range (orderEmbOfFin) ↔ x < card
  ext x
  rw [← Finset.mem_coe, ← range_orderEmbOfFin s rfl, Set.mem_range, Finset.mem_range]
  constructor
  · rintro ⟨i, rfl⟩; rw [hpt i]; exact i.isLt
  · intro hx; exact ⟨⟨x, hx⟩, by rw [hpt ⟨x, hx⟩]⟩

/-! ## 2. Tableau fibres

For a tableau `u` (bijective filling `Fin (μ.card) ≃ μ.cells`), the labels in row
`i` of `u` have columns exactly `{0,…,rowLen i − 1}`. -/

open QOU.BraidKnot.Specht

variable {μ : YoungDiagram}

/-- The total column-sum of `u` equals the column-sum over the diagram's cells. -/
theorem colPattern_sum (u : Tableau μ) :
    ∑ m : Fin (nOf μ), colPattern u m = ∑ c ∈ μ.cells, c.2 := by
  have h := Equiv.sum_comp u (fun c : μ.cells => (c : ℕ × ℕ).2)
  rw [show (∑ m : Fin (nOf μ), colPattern u m) = ∑ m, (u m : ℕ × ℕ).2 from rfl, h,
    Finset.sum_coe_sort μ.cells (fun c => c.2)]

/-- `colPattern u` is injective on each row-fibre of `u`. -/
theorem colPattern_injOn_fiber (u : Tableau μ) (i : ℕ) :
    Set.InjOn (colPattern u)
      ((Finset.univ.filter (fun m => rowPattern u m = i) : Finset (Fin (nOf μ)))) := by
  intro m hm m' hm' hcol
  simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_univ, true_and] at hm hm'
  apply u.injective
  apply Subtype.ext
  apply Prod.ext
  · show (u m : ℕ × ℕ).1 = (u m' : ℕ × ℕ).1; rw [← rowPattern, ← rowPattern, hm, hm']
  · show (u m : ℕ × ℕ).2 = (u m' : ℕ × ℕ).2; exact hcol

/-- The columns occupied by row `i` of `u` are exactly `{0,…,rowLen i − 1}`. -/
theorem fiber_image_eq (u : Tableau μ) (i : ℕ) :
    (Finset.univ.filter (fun m => rowPattern u m = i)).image (colPattern u)
      = Finset.range (μ.rowLen i) := by
  ext j
  simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_range]
  constructor
  · rintro ⟨m, hrow, rfl⟩
    have hcell : ((rowPattern u m, colPattern u m) : ℕ × ℕ) ∈ μ.cells := by
      show (u m : ℕ × ℕ) ∈ μ.cells
      exact (u m).property
    rw [hrow, YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen] at hcell
    exact hcell
  · intro hj
    have hmem : (i, j) ∈ μ.cells := by
      rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen]; exact hj
    refine ⟨u.symm ⟨(i, j), hmem⟩, ?_, ?_⟩
    · show (u (u.symm ⟨(i, j), hmem⟩) : ℕ × ℕ).1 = i; rw [Equiv.apply_symm_apply]
    · show (u (u.symm ⟨(i, j), hmem⟩) : ℕ × ℕ).2 = j; rw [Equiv.apply_symm_apply]

/-- Row `i` of `u` has `rowLen i` labels. -/
theorem fiber_card (u : Tableau μ) (i : ℕ) :
    (Finset.univ.filter (fun m => rowPattern u m = i)).card = μ.rowLen i := by
  rw [← Finset.card_image_of_injOn (colPattern_injOn_fiber u i), fiber_image_eq u i,
    Finset.card_range]

/-- The columns of row `i` of `u` sum to the triangular number `0+⋯+(rowLen i−1)`. -/
theorem fiber_colSum (u : Tableau μ) (i : ℕ) :
    ∑ m ∈ Finset.univ.filter (fun m => rowPattern u m = i), colPattern u m
      = ∑ k ∈ Finset.range (μ.rowLen i), k := by
  rw [← fiber_image_eq u i,
    Finset.sum_image (fun a ha b hb h => colPattern_injOn_fiber u i ha hb h)]

/-! ## 3. The staircase bound

If `(rowPattern s, colPattern t)` is jointly injective, every mixed pair
`(rowPattern s m, colPattern t m)` lies in `μ`. -/

/-- `colPattern t` is injective on each `rowPattern s`-fibre, given joint
injectivity of `(rowPattern s, colPattern t)`. -/
theorem colPattern_t_injOn (s t : Tableau μ)
    (Hinj : Function.Injective (fun m : Fin (nOf μ) => (rowPattern s m, colPattern t m)))
    (i : ℕ) :
    Set.InjOn (colPattern t)
      ((Finset.univ.filter (fun m => rowPattern s m = i) : Finset (Fin (nOf μ)))) := by
  intro m hm m' hm' hcol
  simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_univ, true_and] at hm hm'
  apply Hinj
  show ((rowPattern s m, colPattern t m) : ℕ × ℕ) = (rowPattern s m', colPattern t m')
  rw [Prod.ext_iff]
  exact ⟨by rw [hm, hm'], hcol⟩

/-- **The conjugate-marginal staircase bound.** -/
theorem young_staircase_bound (s t : Tableau μ)
    (Hinj : Function.Injective (fun m : Fin (nOf μ) => (rowPattern s m, colPattern t m))) :
    ∀ m, ((rowPattern s m, colPattern t m) : ℕ × ℕ) ∈ μ := by
  classical
  set N := μ.colLen 0 with hN
  -- the rows used by `s` are `< N`
  have hfN : ∀ m : Fin (nOf μ), rowPattern s m < N := by
    intro m
    have hcell : (s m : ℕ × ℕ) ∈ μ.cells := (s m).property
    rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_colLen] at hcell
    exact lt_of_lt_of_le hcell (μ.colLen_anti 0 (s m : ℕ × ℕ).2 (Nat.zero_le _))
  have hmaps : ∀ m ∈ (Finset.univ : Finset (Fin (nOf μ))), rowPattern s m ∈ Finset.range N :=
    fun m _ => Finset.mem_range.2 (hfN m)
  -- group `∑ colPattern t` and `∑ colPattern s` by the `rowPattern s`-fibres
  have hT_fiber : (∑ m, colPattern t m)
      = ∑ i ∈ Finset.range N,
          ∑ m ∈ Finset.univ.filter (fun m => rowPattern s m = i), colPattern t m :=
    (Finset.sum_fiberwise_of_maps_to hmaps _).symm
  have hS_fiber : (∑ i ∈ Finset.range N, ∑ k ∈ Finset.range (μ.rowLen i), k)
      = ∑ m, colPattern s m := by
    rw [← Finset.sum_fiberwise_of_maps_to hmaps (fun m => colPattern s m)]
    exact Finset.sum_congr rfl (fun i _ => (fiber_colSum s i).symm)
  -- the column totals agree (both = column-sum over cells)
  have hTS : (∑ m, colPattern t m) = ∑ m, colPattern s m := by
    rw [colPattern_sum t, colPattern_sum s]
  -- per-fibre lower bound
  have hle : ∀ i ∈ Finset.range N,
      (∑ k ∈ Finset.range (μ.rowLen i), k)
        ≤ ∑ m ∈ Finset.univ.filter (fun m => rowPattern s m = i), colPattern t m := by
    intro i _
    have hinj := colPattern_t_injOn s t Hinj i
    have hcard : ((Finset.univ.filter (fun m => rowPattern s m = i)).image (colPattern t)).card
        = μ.rowLen i := by
      rw [Finset.card_image_of_injOn hinj, fiber_card s i]
    calc ∑ k ∈ Finset.range (μ.rowLen i), k
        = ∑ k ∈ Finset.range
            ((Finset.univ.filter (fun m => rowPattern s m = i)).image (colPattern t)).card, k := by
            rw [hcard]
      _ ≤ ∑ x ∈ (Finset.univ.filter (fun m => rowPattern s m = i)).image (colPattern t), x :=
            sum_range_card_le _
      _ = ∑ m ∈ Finset.univ.filter (fun m => rowPattern s m = i), colPattern t m :=
            (Finset.sum_image (fun a ha b hb h => hinj ha hb h))
  -- equality of the two grouped totals
  have hsum_eq :
      (∑ i ∈ Finset.range N, ∑ k ∈ Finset.range (μ.rowLen i), k)
        = ∑ i ∈ Finset.range N,
            ∑ m ∈ Finset.univ.filter (fun m => rowPattern s m = i), colPattern t m := by
    rw [hS_fiber, ← hTS, hT_fiber]
  -- termwise equality
  have heq := (Finset.sum_eq_sum_iff_of_le hle).1 hsum_eq
  -- extract the bound at `m`
  intro m
  have himg : (Finset.univ.filter (fun m' => rowPattern s m' = rowPattern s m)).image (colPattern t)
      = Finset.range (μ.rowLen (rowPattern s m)) := by
    have hinj := colPattern_t_injOn s t Hinj (rowPattern s m)
    have hcard : ((Finset.univ.filter (fun m' => rowPattern s m' = rowPattern s m)).image
        (colPattern t)).card = μ.rowLen (rowPattern s m) := by
      rw [Finset.card_image_of_injOn hinj, fiber_card s (rowPattern s m)]
    have hsum : ∑ x ∈ (Finset.univ.filter (fun m' => rowPattern s m' = rowPattern s m)).image
        (colPattern t), x = ∑ k ∈ Finset.range (μ.rowLen (rowPattern s m)), k := by
      rw [Finset.sum_image (fun a ha b hb h => hinj ha hb h),
        ← heq (rowPattern s m) (Finset.mem_range.2 (hfN m))]
    have := eq_range_of_sum_eq _ (by rw [hsum, hcard])
    rwa [hcard] at this
  have hmFi : m ∈ Finset.univ.filter (fun m' => rowPattern s m' = rowPattern s m) := by
    simp
  have hmem : colPattern t m ∈ Finset.range (μ.rowLen (rowPattern s m)) := by
    rw [← himg]; exact Finset.mem_image_of_mem _ hmFi
  rw [YoungDiagram.mem_iff_lt_rowLen]
  exact Finset.mem_range.1 hmem

end QOU.BraidKnot.YoungStaircaseBound
