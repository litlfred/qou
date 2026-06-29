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

end QOU.BraidKnot.YoungStaircaseBound
