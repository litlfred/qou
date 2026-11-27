import Mathlib.GroupTheory.Perm.Cycle.Type

/-!
# Merges add over disjoint support components

Brief C2 front B (bean `qou-brng`). Audit: `docs/audits/2026-11-27-binding-merge-cap-invariant.md`.

The merge count of a bond word is `m = c(σ_free) − c(σ_atom)`; the γγ free word is classically
trivial, so `m = n − c(σ)` with `c` counting every orbit (fixed points included). Each non-trivial
cycle of length `ℓ` contributes `ℓ − 1`, so

    merges σ = |supp σ| − #(non-trivial cycles)   (`merges`, `merges_eq_sum`).

The measured q₀ merge cap is stated per connected component of the bond word's support (strand
intervals `[s, s+2]` of its vertices `V(s)`, joined when they overlap). Components act on
disjoint strand sets, so their permutations are disjoint. This file proves the reduction that
makes a per-component cap a global cap:

1. `merges_mul_of_disjoint` — merges add over a disjoint product.
2. `merges_prod_of_pairwise` — merges of a product of pairwise disjoint permutations is the sum.
3. `merges_prod_le` — a cap `k` per factor gives `k · #factors` for the product.
4. `merges_le_card_support_sub_one` — one factor supported on `s` points merges at most `s − 1`.

What is NOT proved here: that reading 3 at `q₀` caps a single component at 2. That is a measured
statement (scope (a), audit §3); no `q₀` and no empirical number appears in this file.
-/

namespace QOU.MassTheory.MergeComponentAdditivity

open Equiv Finset

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- Merges: `|supp σ|` minus the number of non-trivial cycles, i.e. `card α − #orbits`. -/
def merges (σ : Perm α) : ℕ := σ.support.card - Multiset.card σ.cycleType

theorem merges_eq_sum (σ : Perm α) :
    merges σ = σ.cycleType.sum - Multiset.card σ.cycleType := by
  rw [merges, Perm.sum_cycleType]

/-- Each non-trivial cycle has length at least 2, so `2 · #cycles ≤ |supp σ|`. -/
theorem two_mul_card_cycleType_le (σ : Perm α) :
    2 * Multiset.card σ.cycleType ≤ σ.support.card := by
  rw [← Perm.sum_cycleType]
  have h : ∀ x ∈ σ.cycleType, 2 ≤ x := fun x hx => Perm.two_le_of_mem_cycleType hx
  calc 2 * Multiset.card σ.cycleType = (σ.cycleType.map fun _ => 2).sum := by
        simp [mul_comm]
    _ ≤ σ.cycleType.sum := by
        simpa using Multiset.sum_map_le_sum_map (fun _ => 2) id h

@[simp] theorem merges_one : merges (1 : Perm α) = 0 := by simp [merges]

theorem merges_mul_of_disjoint {σ τ : Perm α} (h : σ.Disjoint τ) :
    merges (σ * τ) = merges σ + merges τ := by
  have hs := two_mul_card_cycleType_le σ
  have ht := two_mul_card_cycleType_le τ
  simp only [merges, h.cycleType_mul, Multiset.card_add, h.card_support_mul]
  omega

theorem merges_prod_of_pairwise (l : List (Perm α)) (hl : l.Pairwise Perm.Disjoint) :
    merges l.prod = (l.map merges).sum := by
  induction l with
  | nil => simp
  | cons g l ih =>
    rw [List.pairwise_cons] at hl
    rw [List.prod_cons, merges_mul_of_disjoint (Perm.disjoint_prod_right l hl.1), ih hl.2]
    simp

/-- **Per-component cap ⇒ global cap.** If every factor of a pairwise disjoint product merges at
most `k`, the product merges at most `k · #factors`. With `k = 2` this is the measured q₀ cap:
`merges ≤ 2 · (support components)`. -/
theorem merges_prod_le (l : List (Perm α)) (hl : l.Pairwise Perm.Disjoint) {k : ℕ}
    (hk : ∀ g ∈ l, merges g ≤ k) : merges l.prod ≤ k * l.length := by
  rw [merges_prod_of_pairwise l hl]
  induction l with
  | nil => simp
  | cons g l ih =>
    rw [List.pairwise_cons] at hl
    simp only [List.map_cons, List.sum_cons, List.length_cons, mul_add, mul_one]
    have h1 := hk g List.mem_cons_self
    have h2 := ih hl.2 (fun x hx => hk x (List.mem_cons_of_mem g hx))
    omega

/-- Permutations supported in disjoint sets are disjoint (components on disjoint strand sets). -/
theorem disjoint_of_support_subset {σ τ : Perm α} {S T : Finset α} (hS : σ.support ⊆ S)
    (hT : τ.support ⊆ T) (hST : Disjoint S T) : σ.Disjoint τ :=
  Perm.disjoint_iff_disjoint_support.mpr (hST.mono hS hT)

/-- A non-trivial permutation merges at most `|supp σ| − 1` (one cycle on its whole support). -/
theorem merges_le_card_support_sub_one {σ : Perm α} (h : σ ≠ 1) :
    merges σ ≤ σ.support.card - 1 := by
  have : 1 ≤ Multiset.card σ.cycleType := by
    rw [Nat.one_le_iff_ne_zero, Ne, Multiset.card_eq_zero, Perm.cycleType_eq_zero]
    exact h
  unfold merges
  omega

end QOU.MassTheory.MergeComponentAdditivity
